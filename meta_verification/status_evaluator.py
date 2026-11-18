#!/usr/bin/env python3
"""Fail-closed evidence-policy evaluator.

This module checks structural consistency and revision binding of supplied evidence.
It is NOT a mathematical proof checker, signature verifier, or authenticity oracle.
Evidence JSON and embedded artifact bytes can be forged by their producer; use an
independent trusted acquisition/attestation route when authenticity is required.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
POLICY_KEYS = {"schema_version", "claim_id", "checker_revision", "workflow_revision", "required_obligations"}
EVIDENCE_KEYS = {"schema_version", "claim_id", "source_commit", "checker_revision", "workflow_revision", "obligations"}
ITEM_KEYS = {"obligation_id", "result", "artifact_base64", "artifact_sha256"}
RESULTS = {"ACCEPTED", "REJECTED", "ERROR", "TIMEOUT", "INCONCLUSIVE", "NOT_RUN"}
HEX_40_OR_64 = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
HEX_64 = re.compile(r"^[0-9a-f]{64}$")
MAX_ARTIFACT_BYTES = 8 * 1024 * 1024


class EvaluationError(ValueError):
    """Malformed policy or evidence; never interpreted as acceptance."""


def _object(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise EvaluationError(f"{label} must be a JSON object")
    missing = keys - value.keys()
    unknown = value.keys() - keys
    if missing:
        raise EvaluationError(f"{label} missing fields: {', '.join(sorted(missing))}")
    if unknown:
        raise EvaluationError(f"{label} has unknown fields: {', '.join(sorted(unknown))}")
    return value


def _nonempty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvaluationError(f"{label} must be a non-empty string")
    return value


def validate_policy(policy: Any) -> dict[str, Any]:
    p = _object(policy, POLICY_KEYS, "policy")
    if p["schema_version"] != SCHEMA_VERSION:
        raise EvaluationError("unsupported policy schema_version")
    for key in ("claim_id", "checker_revision", "workflow_revision"):
        _nonempty_string(p[key], f"policy.{key}")
    obligations = p["required_obligations"]
    if not isinstance(obligations, list) or not obligations:
        raise EvaluationError("policy.required_obligations must be a non-empty list")
    if any(not isinstance(x, str) or not x.strip() for x in obligations):
        raise EvaluationError("required obligation IDs must be non-empty strings")
    if len(obligations) != len(set(obligations)):
        raise EvaluationError("policy contains duplicate required obligation IDs")
    return p


def evaluate(policy: Any, evidence: Any, expected_commit: str) -> dict[str, Any]:
    """Return ACCEPTED only when every policy obligation has current valid evidence."""
    p = validate_policy(policy)
    _nonempty_string(expected_commit, "expected_commit")
    if not HEX_40_OR_64.fullmatch(expected_commit):
        raise EvaluationError("expected_commit must be a lowercase 40- or 64-character Git object ID")

    e = _object(evidence, EVIDENCE_KEYS, "evidence")
    if e["schema_version"] != SCHEMA_VERSION:
        raise EvaluationError("unsupported evidence schema_version")
    for key in ("claim_id", "source_commit", "checker_revision", "workflow_revision"):
        _nonempty_string(e[key], f"evidence.{key}")

    stale = []
    comparisons = (
        ("claim_id", p["claim_id"]),
        ("source_commit", expected_commit),
        ("checker_revision", p["checker_revision"]),
        ("workflow_revision", p["workflow_revision"]),
    )
    for field, expected in comparisons:
        if e[field] != expected:
            stale.append(field)

    items = e["obligations"]
    if not isinstance(items, list):
        raise EvaluationError("evidence.obligations must be a list")

    seen: dict[str, dict[str, Any]] = {}
    duplicate_ids: set[str] = set()
    unknown_ids: set[str] = set()
    for index, raw in enumerate(items):
        item = _object(raw, ITEM_KEYS, f"evidence.obligations[{index}]")
        oid = _nonempty_string(item["obligation_id"], f"obligations[{index}].obligation_id")
        if oid in seen:
            duplicate_ids.add(oid)
        seen[oid] = item
        if oid not in p["required_obligations"]:
            unknown_ids.add(oid)

    required = set(p["required_obligations"])
    missing_ids = required - seen.keys()
    if stale or duplicate_ids or unknown_ids or missing_ids:
        return {
            "status": "INCONCLUSIVE",
            "reasons": {
                "stale_fields": sorted(stale),
                "duplicate_obligations": sorted(duplicate_ids),
                "unknown_obligations": sorted(unknown_ids),
                "missing_obligations": sorted(missing_ids),
            },
        }

    rejected = []
    nonaccepted = []
    artifact_errors = []
    for oid in p["required_obligations"]:
        item = seen[oid]
        result = item["result"]
        if not isinstance(result, str) or result not in RESULTS:
            raise EvaluationError(f"obligation {oid}: unsupported result state")
        encoded = item["artifact_base64"]
        digest = item["artifact_sha256"]
        if not isinstance(encoded, str) or not isinstance(digest, str) or not HEX_64.fullmatch(digest):
            raise EvaluationError(f"obligation {oid}: malformed artifact encoding or SHA-256")
        try:
            raw_bytes = base64.b64decode(encoded, validate=True)
        except (ValueError, base64.binascii.Error):
            raise EvaluationError(f"obligation {oid}: invalid base64 artifact") from None
        if len(raw_bytes) > MAX_ARTIFACT_BYTES:
            raise EvaluationError(f"obligation {oid}: artifact exceeds size limit")
        actual = hashlib.sha256(raw_bytes).hexdigest()
        if actual != digest:
            artifact_errors.append(oid)
        if result == "REJECTED":
            rejected.append(oid)
        elif result != "ACCEPTED":
            nonaccepted.append({"obligation_id": oid, "result": result})

    if artifact_errors:
        return {"status": "REJECTED", "reasons": {"artifact_digest_mismatch": sorted(artifact_errors)}}
    if rejected:
        return {"status": "REJECTED", "reasons": {"rejected_obligations": sorted(rejected)}}
    if nonaccepted:
        return {"status": "INCONCLUSIVE", "reasons": {"nonaccepted_obligations": nonaccepted}}
    return {"status": "ACCEPTED", "reasons": {}}


def _load_json(path: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise EvaluationError(f"cannot read valid JSON from {path}: {exc}") from None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", required=True, help="trusted policy JSON path")
    parser.add_argument("--evidence", required=True, help="untrusted evidence JSON path")
    parser.add_argument("--expected-commit", required=True, help="commit SHA supplied by trusted CI context")
    args = parser.parse_args(argv)
    try:
        result = evaluate(_load_json(args.policy), _load_json(args.evidence), args.expected_commit)
    except EvaluationError as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "ACCEPTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
