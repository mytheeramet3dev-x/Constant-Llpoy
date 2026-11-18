#!/usr/bin/env python3
"""Deterministic, fail-closed aggregation of component evidence.

The standalone CLI is structural-only and has no route to supply authenticated
receipt records, so it cannot return ACCEPTED from caller-controlled JSON alone.
The internal aggregate() API accepts an in-memory authentication map only from
component_provenance_authenticator; arbitrary Python callers can forge that object,
so this module is not itself a process or trust boundary. Production invocation
must use policy_activation_gate.py, which performs cryptographic verification
before constructing the map. This is not a proof checker or source of mathematical truth.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, re, sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
POLICY_KEYS = {"schema_version", "claim_id", "policy_revision", "required_components"}
BUNDLE_KEYS = {"schema_version", "claim_id", "source_commit", "policy_revision", "components"}
COMPONENT_KEYS = {"component_id", "status", "evidence_base64", "evidence_sha256", "provenance"}
PROVENANCE_KEYS = {"receipt_schema_version", "subject_sha256", "source_commit", "attestation_run_id", "attestation_run_attempt", "attestation_workflow_revision"}
AUTHENTICATED_KEYS = {"subject_sha256", "source_commit", "attestation_run_id", "attestation_run_attempt",
                     "attestation_workflow_revision", "repository_id", "signer_workflow",
                     "provenance_policy_sha256", "verified_attestation_count"}
COMPONENT_STATES = {"PASS", "FAIL", "INCONCLUSIVE", "ERROR", "TIMEOUT", "NOT_RUN"}
SHA40_OR_64 = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
MAX_EVIDENCE_BYTES = 8 * 1024 * 1024

class AggregationError(ValueError):
    """Malformed policy or bundle; never interpreted as acceptance."""

def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AggregationError(message)

def _exact_object(value: Any, keys: set[str], label: str) -> dict:
    _require(isinstance(value, dict), f"{label} must be an object")
    missing, unknown = keys - value.keys(), value.keys() - keys
    _require(not missing, f"{label} missing fields: {', '.join(sorted(missing))}")
    _require(not unknown, f"{label} unknown fields: {', '.join(sorted(unknown))}")
    return value

def _nonempty(value: Any, label: str) -> str:
    _require(isinstance(value, str) and bool(value.strip()), f"{label} must be a non-empty string")
    return value

def _sha(value: Any, pattern: re.Pattern, label: str) -> str:
    _require(isinstance(value, str) and pattern.fullmatch(value) is not None, f"{label} has invalid SHA format")
    return value

def validate_policy(policy: Any) -> dict:
    p = _exact_object(policy, POLICY_KEYS, "policy")
    _require(p["schema_version"] == SCHEMA_VERSION, "unsupported policy schema_version")
    _nonempty(p["claim_id"], "policy.claim_id")
    _sha(p["policy_revision"], SHA40, "policy.policy_revision")
    required = p["required_components"]
    _require(isinstance(required, list) and bool(required), "required_components must be a non-empty list")
    _require(all(isinstance(x, str) and bool(x.strip()) for x in required), "component IDs must be non-empty strings")
    _require(len(required) == len(set(required)), "duplicate required component IDs")
    return p

def aggregate(policy: Any, bundle: Any, expected_commit: str, authenticated_receipts: dict | None = None) -> dict:
    """Evaluate completeness and consistency, requiring authenticated component receipts.

    ACCEPTED requires an in-memory authentication map returned by the direct GitHub
    attestation verifier. The standalone CLI never supplies that map and therefore
    cannot emit ACCEPTED. Even authenticated provenance does not establish claim truth.
    """
    p = validate_policy(policy)
    _sha(expected_commit, SHA40_OR_64, "expected_commit")
    auth_map = {} if authenticated_receipts is None else authenticated_receipts
    _require(isinstance(auth_map, dict), "authenticated_receipts must be an object")
    _require(set(auth_map).issubset(set(p["required_components"])),
             "authenticated_receipts contains unknown component IDs")
    b = _exact_object(bundle, BUNDLE_KEYS, "bundle")
    _require(b["schema_version"] == SCHEMA_VERSION, "unsupported bundle schema_version")
    _nonempty(b["claim_id"], "bundle.claim_id")
    _sha(b["source_commit"], SHA40_OR_64, "bundle.source_commit")
    _sha(b["policy_revision"], SHA40, "bundle.policy_revision")

    stale = []
    for field, expected in (("claim_id", p["claim_id"]), ("source_commit", expected_commit),
                            ("policy_revision", p["policy_revision"])):
        if b[field] != expected:
            stale.append(field)

    raw_components = b["components"]
    _require(isinstance(raw_components, list), "bundle.components must be a list")
    seen: dict[str, dict] = {}
    duplicates, unknown = set(), set()
    for index, raw in enumerate(raw_components):
        c = _exact_object(raw, COMPONENT_KEYS, f"components[{index}]")
        cid = _nonempty(c["component_id"], f"components[{index}].component_id")
        if cid in seen:
            duplicates.add(cid)
        seen[cid] = c
        if cid not in p["required_components"]:
            unknown.add(cid)
    required = set(p["required_components"])
    missing = required - seen.keys()

    component_results = []
    verified_failures, pending, unauthenticated = [], [], []
    digest_errors = []
    for cid in p["required_components"]:
        if cid not in seen:
            continue
        if cid in duplicates:
            continue
        c = seen[cid]
        state = c["status"]
        _require(isinstance(state, str) and state in COMPONENT_STATES, f"component {cid}: unsupported status")
        encoded, digest = c["evidence_base64"], c["evidence_sha256"]
        _require(isinstance(encoded, str), f"component {cid}: evidence_base64 must be a string")
        _sha(digest, SHA256, f"component {cid}: evidence_sha256")
        try:
            evidence_bytes = base64.b64decode(encoded, validate=True)
        except (ValueError, base64.binascii.Error):
            raise AggregationError(f"component {cid}: invalid base64 evidence") from None
        _require(0 < len(evidence_bytes) <= MAX_EVIDENCE_BYTES,
                 f"component {cid}: evidence must be non-empty and within size limit")
        actual = hashlib.sha256(evidence_bytes).hexdigest()
        if actual != digest:
            digest_errors.append(cid)

        receipt = _exact_object(c["provenance"], PROVENANCE_KEYS, f"component {cid}.provenance")
        _require(receipt["receipt_schema_version"] == "2.0", f"component {cid}: unsupported receipt schema")
        _sha(receipt["subject_sha256"], SHA256, f"component {cid}: provenance subject_sha256")
        _sha(receipt["source_commit"], SHA40_OR_64, f"component {cid}: provenance source_commit")
        _require(type(receipt["attestation_run_id"]) is int and receipt["attestation_run_id"] > 0,
                 f"component {cid}: invalid attestation_run_id")
        _require(type(receipt["attestation_run_attempt"]) is int and receipt["attestation_run_attempt"] > 0,
                 f"component {cid}: invalid attestation_run_attempt")
        _sha(receipt["attestation_workflow_revision"], SHA40, f"component {cid}: attestation_workflow_revision")
        auth = auth_map.get(cid)
        auth_valid = False
        if auth is not None:
            auth = _exact_object(auth, AUTHENTICATED_KEYS, f"authenticated_receipts[{cid}]")
            _sha(auth["subject_sha256"], SHA256, f"authenticated receipt {cid}: subject_sha256")
            _sha(auth["source_commit"], SHA40, f"authenticated receipt {cid}: source_commit")
            _require(type(auth["attestation_run_id"]) is int and auth["attestation_run_id"] > 0,
                     f"authenticated receipt {cid}: invalid attestation_run_id")
            _require(type(auth["attestation_run_attempt"]) is int and auth["attestation_run_attempt"] > 0,
                     f"authenticated receipt {cid}: invalid attestation_run_attempt")
            _sha(auth["attestation_workflow_revision"], SHA40, f"authenticated receipt {cid}: workflow revision")
            _require(type(auth["repository_id"]) is int and auth["repository_id"] > 0,
                     f"authenticated receipt {cid}: invalid repository ID")
            _nonempty(auth["signer_workflow"], f"authenticated receipt {cid}: signer workflow")
            _sha(auth["provenance_policy_sha256"], SHA256, f"authenticated receipt {cid}: policy digest")
            _require(type(auth["verified_attestation_count"]) is int and auth["verified_attestation_count"] > 0,
                     f"authenticated receipt {cid}: no verified attestations")
            auth_valid = (auth["subject_sha256"] == actual
                          and auth["source_commit"] == expected_commit
                          and auth["attestation_run_id"] == receipt["attestation_run_id"]
                          and auth["attestation_run_attempt"] == receipt["attestation_run_attempt"]
                          and auth["attestation_workflow_revision"] == receipt["attestation_workflow_revision"])
        receipt_valid = (auth_valid and receipt["subject_sha256"] == actual
                         and receipt["source_commit"] == expected_commit
                         and receipt["attestation_workflow_revision"] == expected_commit)
        if not receipt_valid:
            unauthenticated.append(cid)
        if state == "FAIL" and receipt_valid and cid not in digest_errors:
            verified_failures.append(cid)
        if state != "PASS" or not receipt_valid:
            pending.append({"component_id": cid, "status": state,
                            "provenance_status": "AUTHENTICATED" if receipt_valid else "UNAUTHENTICATED"})
        component_results.append({"component_id": cid, "status": state,
                                  "evidence_sha256": actual,
                                  "provenance_cryptographically_authenticated": receipt_valid})

    reasons = {
        "stale_fields": sorted(stale),
        "duplicate_components": sorted(duplicates),
        "unknown_components": sorted(unknown),
        "missing_components": sorted(missing),
        "evidence_digest_mismatches": sorted(digest_errors),
        "verified_failures": sorted(verified_failures),
        "pending_or_unverified": pending,
        "unauthenticated_provenance": sorted(unauthenticated),
    }
    if digest_errors or verified_failures:
        status = "REJECTED"
    elif stale or duplicates or unknown or missing or pending:
        status = "INCONCLUSIVE"
    else:
        status = "ACCEPTED"
    return {
        "status": status,
        "status_scope": "BUNDLE_POLICY_AND_COMPONENT_PROVENANCE_EVALUATION",
        "assurance_level": "COMPONENT_ATTESTATIONS_AUTHENTICATED" if status == "ACCEPTED" else "STRUCTURAL_ONLY_OR_PARTIALLY_AUTHENTICATED",
        "claim_id": p["claim_id"],
        "source_commit": b["source_commit"],
        "policy_revision": p["policy_revision"],
        "components": component_results,
        "reasons": reasons,
    }

def _load(path: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AggregationError(f"cannot read valid JSON from {path}: {exc}") from None

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--expected-commit", required=True)
    args = parser.parse_args(argv)
    try:
        result = aggregate(_load(args.policy), _load(args.bundle), args.expected_commit)
    except AggregationError as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return {"ACCEPTED": 0, "REJECTED": 1, "INCONCLUSIVE": 1}[result["status"]]

if __name__ == "__main__":
    raise SystemExit(main())
