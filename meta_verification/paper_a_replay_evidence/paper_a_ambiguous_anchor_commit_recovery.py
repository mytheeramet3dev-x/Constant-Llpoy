"""Recovery classification after ambiguous atomic-anchor commit outcomes (8.24).

This module is read-only: it never retries, advances, rewrites, or promotes stages.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Mapping

from paper_a_authenticated_registry_anchor import (
    AnchorAuthenticationError, verify_authenticated_anchor,
)


def classify_ambiguous_anchor_commit(
    database_path,
    anchor_path,
    trusted_keys: Mapping[str, bytes],
    externally_held_minimum_sequence: int,
    expected_previous_sequence: int,
    expected_previous_digest: str,
    intended_sequence: int,
):
    """Classify an uncertain writer outcome using the authenticated live state.

    COMMITTED: authenticated anchor is exactly the intended sequence and matches live registry.
    NOT_COMMITTED: authenticated anchor is exactly the previous sequence/digest, live registry
      matches it, and no stage artifacts exist; safe to consider retry after caller review.
    INDETERMINATE: missing anchor, orphan stages, unexpected sequence, or unverifiable state.
    FAIL_CLOSED: final anchor exists but is malformed/authentication/registry verification fails.
    This function never asserts durability across power loss.
    """
    path = Path(anchor_path)
    parent = path.parent
    if not parent.exists() or not parent.is_dir():
        return {"status": "FAIL_CLOSED", "retry_advice": "DO_NOT_RETRY",
                "reason": "anchor parent missing or invalid"}
    stages = sorted(p.name for p in parent.glob(".anchor-stage-*") if p.is_file())
    if not path.exists():
        return {"status": "INDETERMINATE", "retry_advice": "DO_NOT_RETRY",
                "reason": "final anchor missing", "staged_files": stages}
    try:
        anchor = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {"status": "FAIL_CLOSED", "retry_advice": "DO_NOT_RETRY",
                "reason": "final anchor unreadable or malformed", "staged_files": stages}
    if not isinstance(anchor, dict):
        return {"status": "FAIL_CLOSED", "retry_advice": "DO_NOT_RETRY",
                "reason": "final anchor is not an object", "staged_files": stages}
    try:
        verified = verify_authenticated_anchor(
            database_path, anchor, trusted_keys, externally_held_minimum_sequence
        )
    except (AnchorAuthenticationError, OSError, ValueError, TypeError):
        return {"status": "FAIL_CLOSED", "retry_advice": "DO_NOT_RETRY",
                "reason": "authentication or registry verification failed", "staged_files": stages}
    if verified.get("integrity") != "PASS":
        return {"status": "FAIL_CLOSED", "retry_advice": "DO_NOT_RETRY",
                "reason": "authenticated anchor mismatches live registry", "staged_files": stages}
    if stages:
        return {"status": "INDETERMINATE", "retry_advice": "DO_NOT_RETRY",
                "reason": "staging artifacts remain; preserve for forensic review",
                "staged_files": stages, "anchor_sequence": anchor.get("sequence")}
    seq = anchor.get("sequence")
    if seq == intended_sequence:
        return {"status": "COMMITTED", "retry_advice": "DO_NOT_RETRY",
                "reason": "intended sequence authenticated and matches live registry",
                "anchor_sequence": seq, "snapshot_sha256": anchor.get("snapshot_sha256")}
    if seq == expected_previous_sequence and anchor.get("snapshot_sha256") == expected_previous_digest:
        return {"status": "NOT_COMMITTED", "retry_advice": "RETRY_REQUIRES_CALLER_REVALIDATION",
                "reason": "previous anchor remains authenticated and matches live registry",
                "anchor_sequence": seq, "snapshot_sha256": anchor.get("snapshot_sha256")}
    return {"status": "INDETERMINATE", "retry_advice": "DO_NOT_RETRY",
            "reason": "anchor sequence is outside expected previous/intended states",
            "anchor_sequence": seq}
