"""Authenticate every required component's exact evidence bytes with GitHub/Sigstore.

This module is the only production path that can produce the in-memory authentication
records consumed by status_aggregator. Caller-supplied JSON reports are never accepted.
"""
from __future__ import annotations
import base64, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from typing import Any, Callable
from status_aggregator import validate_policy as validate_bundle_policy, BUNDLE_KEYS, COMPONENT_KEYS, PROVENANCE_KEYS
from verify_signed_provenance import (
    ProvenanceError, validate_policy as validate_provenance_policy,
    validate_cli_version, validate_cli_output,
)

SHA256 = re.compile(r"^[0-9a-f]{64}$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
RECEIPT_KEYS = {"receipt_schema_version", "subject_sha256", "source_commit",
                "attestation_run_id", "attestation_run_attempt", "attestation_workflow_revision"}

class ComponentProvenanceError(ValueError):
    """Component provenance could not be authenticated; aggregation must fail closed."""

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ComponentProvenanceError(message)

def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result

def _decode_json(raw: str, label: str) -> Any:
    try:
        return json.loads(raw, object_pairs_hook=_unique_object,
                          parse_constant=lambda value: (_ for _ in ()).throw(
                              ComponentProvenanceError(f"{label}: non-standard JSON constant {value}")))
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise ComponentProvenanceError(f"{label}: malformed JSON: {exc}") from None

def authenticate_components(policy_bytes: bytes, provenance_policy_bytes: bytes,
                            provenance_policy: Any, bundle: Any, expected_commit: str,
                            expected_provenance_policy_sha256: str,
                            runner: Callable = subprocess.run) -> dict[str, dict]:
    """Verify one signed SLSA v1 attestation for each exact required component subject."""
    require(isinstance(policy_bytes, bytes) and 0 < len(policy_bytes) <= 1024 * 1024,
            "aggregation policy bytes are empty or oversized")
    require(isinstance(provenance_policy_bytes, bytes) and 0 < len(provenance_policy_bytes) <= 1024 * 1024,
            "provenance policy bytes are empty or oversized")
    require(isinstance(expected_provenance_policy_sha256, str)
            and SHA256.fullmatch(expected_provenance_policy_sha256) is not None,
            "external provenance-policy pin is missing or malformed")
    actual_policy_sha = hashlib.sha256(provenance_policy_bytes).hexdigest()
    require(actual_policy_sha == expected_provenance_policy_sha256,
            "provenance policy bytes differ from external pin")
    require(isinstance(expected_commit, str) and SHA40.fullmatch(expected_commit) is not None,
            "expected source commit must be a lowercase 40-character Git SHA")
    try:
        parsed_policy = _decode_json(policy_bytes.decode("utf-8"), "aggregation policy")
        parsed_provenance_policy = _decode_json(provenance_policy_bytes.decode("utf-8"), "provenance policy")
    except UnicodeError as exc:
        raise ComponentProvenanceError(f"policy input is not UTF-8: {exc}") from None
    require(parsed_provenance_policy == provenance_policy,
            "provenance policy object does not match exact externally pinned bytes")
    bundle_policy = validate_bundle_policy(parsed_policy)
    require(isinstance(bundle, dict) and set(bundle) == BUNDLE_KEYS,
            "component bundle has missing or unknown fields")
    require(bundle.get("source_commit") == expected_commit,
            "bundle source commit differs from expected attestation source commit")
    components = bundle.get("components")
    require(isinstance(components, list), "bundle.components must be a list")
    indexed = {}
    for index, component in enumerate(components):
        require(isinstance(component, dict) and set(component) == COMPONENT_KEYS,
                f"components[{index}] has missing or unknown fields")
        cid = component.get("component_id")
        require(isinstance(cid, str) and cid.strip(), f"components[{index}].component_id is invalid")
        require(cid not in indexed, f"duplicate component receipt: {cid}")
        indexed[cid] = component
    required = set(bundle_policy["required_components"])
    require(set(indexed) == required,
            f"component set mismatch; missing={sorted(required-set(indexed))}, unknown={sorted(set(indexed)-required)}")
    p = validate_provenance_policy(provenance_policy)
    version = runner(["gh", "version"], capture_output=True, text=True, timeout=20, check=False)
    require(version.returncode == 0, "gh version command failed")
    try:
        validate_cli_version(version.stdout, p)
    except ProvenanceError as exc:
        raise ComponentProvenanceError(str(exc)) from None

    authenticated = {}
    for cid in bundle_policy["required_components"]:
        component = indexed[cid]
        encoded = component.get("evidence_base64")
        require(isinstance(encoded, str), f"{cid}: evidence_base64 must be a string")
        try:
            subject_bytes = base64.b64decode(encoded, validate=True)
        except (ValueError, base64.binascii.Error):
            raise ComponentProvenanceError(f"{cid}: invalid evidence base64") from None
        require(0 < len(subject_bytes) <= 8 * 1024 * 1024, f"{cid}: evidence subject is empty or oversized")
        subject_sha = hashlib.sha256(subject_bytes).hexdigest()
        require(component.get("evidence_sha256") == subject_sha, f"{cid}: evidence digest mismatch before attestation verification")
        receipt = component.get("provenance")
        require(isinstance(receipt, dict) and set(receipt) == RECEIPT_KEYS,
                f"{cid}: provenance receipt has missing or unknown fields")
        require(receipt["receipt_schema_version"] == "2.0", f"{cid}: unsupported receipt schema")
        require(receipt["subject_sha256"] == subject_sha, f"{cid}: receipt subject digest mismatch")
        require(receipt["source_commit"] == expected_commit, f"{cid}: receipt source commit mismatch")
        run_id, attempt = receipt["attestation_run_id"], receipt["attestation_run_attempt"]
        require(type(run_id) is int and run_id > 0, f"{cid}: attestation run ID must be a positive integer")
        require(type(attempt) is int and attempt > 0, f"{cid}: attestation run attempt must be a positive integer")
        require(receipt["attestation_workflow_revision"] == expected_commit,
                f"{cid}: attestation workflow revision differs from source commit")
        invocation_id = f"https://github.com/{p['repository']}/actions/runs/{run_id}/attempts/{attempt}"
        with tempfile.TemporaryDirectory() as td:
            subject_path = Path(td) / f"{cid}.evidence"
            subject_path.write_bytes(subject_bytes)
            command = [
                "gh", "attestation", "verify", str(subject_path),
                "--repo", p["repository"],
                "--signer-workflow", p["signer_workflow"],
                "--cert-oidc-issuer", p["oidc_issuer"],
                "--predicate-type", p["predicate_type"],
                "--source-ref", p["source_ref"],
                "--source-digest", expected_commit,
                "--signer-digest", expected_commit,
                "--deny-self-hosted-runners",
                "--format", "json",
            ]
            try:
                completed = runner(command, capture_output=True, text=True, timeout=180, check=False)
            except (OSError, subprocess.TimeoutExpired) as exc:
                raise ComponentProvenanceError(f"{cid}: attestation verification could not complete: {exc}") from None
        require(completed.returncode == 0,
                f"{cid}: gh attestation verify rejected provenance: {(completed.stderr or '').strip()}")
        require(isinstance(completed.stdout, str), f"{cid}: gh attestation output is not text")
        output = _decode_json(completed.stdout, f"{cid}: gh attestation output")
        try:
            report = validate_cli_output(output, subject_bytes, p, expected_commit,
                                         expected_invocation_id=invocation_id)
        except ProvenanceError as exc:
            raise ComponentProvenanceError(f"{cid}: {exc}") from None
        authenticated[cid] = {
            "subject_sha256": subject_sha,
            "source_commit": expected_commit,
            "attestation_run_id": run_id,
            "attestation_run_attempt": attempt,
            "attestation_workflow_revision": expected_commit,
            "repository_id": report["repository_id"],
            "signer_workflow": report["signer_workflow"],
            "provenance_policy_sha256": actual_policy_sha,
            "verified_attestation_count": len(report["verified_attestations"]),
        }
    return authenticated
