#!/usr/bin/env python3
"""Deterministic, fail-closed aggregation of component evidence.

This is a structural policy evaluator, NOT an authentication oracle, proof checker,
or source of mathematical truth. A provenance receipt's signature must be verified
by a separately trusted acquisition path before its fields are relied upon.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, re, sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
POLICY_KEYS = {"schema_version", "claim_id", "policy_revision", "required_components"}
BUNDLE_KEYS = {"schema_version", "claim_id", "source_commit", "policy_revision", "components"}
COMPONENT_KEYS = {"component_id", "status", "evidence_base64", "evidence_sha256", "provenance"}
PROVENANCE_KEYS = {"status", "subject_sha256", "source_commit", "verifier_run_id", "verifier_run_attempt", "verifier_revision"}
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

def aggregate(policy: Any, bundle: Any, expected_commit: str) -> dict:
    """Evaluate completeness, consistency, revision binding and receipt structure.

    ACCEPTED means only that this bundle satisfies the supplied structural policy.
    It does not mean the receipts were authenticated or the underlying claims are true.
    """
    p = validate_policy(policy)
    _sha(expected_commit, SHA40_OR_64, "expected_commit")
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
    verified_failures, pending = [], []
    digest_errors = []
    for cid in p["required_components"]:
        if cid not in seen:
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
        _require(isinstance(receipt["status"], str) and receipt["status"] in {"VERIFIED", "UNVERIFIED", "FAILED"},
                 f"component {cid}: unsupported provenance status")
        _sha(receipt["subject_sha256"], SHA256, f"component {cid}: provenance subject_sha256")
        _sha(receipt["source_commit"], SHA40_OR_64, f"component {cid}: provenance source_commit")
        _require(type(receipt["verifier_run_id"]) is int and receipt["verifier_run_id"] > 0,
                 f"component {cid}: invalid verifier_run_id")
        _require(type(receipt["verifier_run_attempt"]) is int and receipt["verifier_run_attempt"] > 0,
                 f"component {cid}: invalid verifier_run_attempt")
        _sha(receipt["verifier_revision"], SHA40, f"component {cid}: verifier_revision")
        receipt_valid = (receipt["status"] == "VERIFIED"
                         and receipt["subject_sha256"] == actual
                         and receipt["source_commit"] == expected_commit)
        if state == "FAIL" and receipt_valid and cid not in digest_errors:
            verified_failures.append(cid)
        if state != "PASS" or not receipt_valid:
            pending.append({"component_id": cid, "status": state,
                            "provenance_status": receipt["status"] if not receipt_valid else "VERIFIED"})
        component_results.append({"component_id": cid, "status": state,
                                  "evidence_sha256": actual,
                                  "provenance_structurally_consistent": receipt_valid})

    reasons = {
        "stale_fields": sorted(stale),
        "duplicate_components": sorted(duplicates),
        "unknown_components": sorted(unknown),
        "missing_components": sorted(missing),
        "evidence_digest_mismatches": sorted(digest_errors),
        "verified_failures": sorted(verified_failures),
        "pending_or_unverified": pending,
    }
    if digest_errors or verified_failures:
        status = "REJECTED"
    elif stale or duplicates or unknown or missing or pending:
        status = "INCONCLUSIVE"
    else:
        status = "ACCEPTED"
    return {
        "status": status,
        "status_scope": "BUNDLE_POLICY_EVALUATION_ONLY",
        "assurance_level": "STRUCTURAL_ONLY_UNAUTHENTICATED_INPUTS",
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
