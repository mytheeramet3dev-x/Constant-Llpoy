"""Independent status semantics for Paper A evidence evaluations.

Statuses are scoped claims, not certification. A record is immutable within its
evaluation_id; any re-evaluation must use a new ID. This module intentionally
does not decide whether evidence is mathematically true.
"""
from __future__ import annotations

import re
from typing import Any, Mapping

STATUSES = {
    "PASS", "FAIL", "NOT_EVALUATED", "INDETERMINATE",
    "NOT_APPLICABLE", "FAIL_CLOSED",
}
_DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")


class StatusSemanticsError(ValueError):
    """A status record violates the independent status contract."""


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_digest(value: Any) -> bool:
    return isinstance(value, str) and bool(_DIGEST_RE.fullmatch(value))


def validate_status_record(record: Mapping[str, Any]) -> dict[str, Any]:
    """Validate shape and status-specific proof obligations; return a copy."""
    if not isinstance(record, Mapping):
        raise StatusSemanticsError("record must be a mapping")
    required = {
        "evaluation_id", "scope", "status", "evidence_bundle_sha256",
        "policy_sha256", "evidence_ids", "reason",
    }
    missing = required - set(record)
    if missing:
        raise StatusSemanticsError(f"missing fields: {sorted(missing)}")
    if not _nonempty_string(record["evaluation_id"]):
        raise StatusSemanticsError("evaluation_id must be non-empty")
    if not _nonempty_string(record["scope"]):
        raise StatusSemanticsError("scope must be non-empty")
    status = record["status"]
    if status not in STATUSES:
        raise StatusSemanticsError("unknown status")
    if not _valid_digest(record["evidence_bundle_sha256"]):
        raise StatusSemanticsError("invalid evidence bundle digest")
    if not _valid_digest(record["policy_sha256"]):
        raise StatusSemanticsError("invalid policy digest")
    evidence_ids = record["evidence_ids"]
    if not isinstance(evidence_ids, list) or any(not _nonempty_string(x) for x in evidence_ids):
        raise StatusSemanticsError("evidence_ids must be a list of non-empty strings")
    if len(evidence_ids) != len(set(evidence_ids)):
        raise StatusSemanticsError("duplicate evidence IDs")
    reason = record["reason"]
    if reason is not None and not isinstance(reason, str):
        raise StatusSemanticsError("reason must be string or null")

    if status == "PASS":
        if not evidence_ids:
            raise StatusSemanticsError("PASS requires evidence IDs")
        if reason is not None and not reason.strip():
            raise StatusSemanticsError("reason cannot be blank")
    elif status in {"FAIL", "NOT_EVALUATED", "INDETERMINATE", "NOT_APPLICABLE", "FAIL_CLOSED"}:
        if not _nonempty_string(reason):
            raise StatusSemanticsError(f"{status} requires a non-empty reason")
    if status == "FAIL_CLOSED" and record.get("downstream_status") != "NOT_EVALUATED":
        raise StatusSemanticsError("FAIL_CLOSED requires downstream_status NOT_EVALUATED")
    if status != "FAIL_CLOSED" and "downstream_status" in record:
        raise StatusSemanticsError("downstream_status is reserved for FAIL_CLOSED records")
    return dict(record)


def validate_status_continuity(previous: Mapping[str, Any], current: Mapping[str, Any]) -> dict[str, Any]:
    """Reject mutation/status promotion within one evaluation ID.

    A fresh evaluation may use a new ID. Records with the same ID must be
    byte-for-byte equivalent at the contract level (all fields identical).
    """
    old = validate_status_record(previous)
    new = validate_status_record(current)
    if old["evaluation_id"] != new["evaluation_id"]:
        return new  # distinct evaluation: allowed, not a transition
    if old != new:
        raise StatusSemanticsError(
            "evaluation record mutated: status/context/evidence changes require a new evaluation_id"
        )
    return new
