"""Fail-closed recovery classification for authenticated registry-anchor incidents.

Recovery never promotes staged files automatically. Orphan staging files are forensic
artifacts; a valid final anchor is authenticated against independently supplied keys
and sequence floor before a recovery decision can be PASS.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Mapping

from paper_a_authenticated_registry_anchor import (
    AnchorAuthenticationError, verify_authenticated_anchor,
)

class AnchorRecoveryError(RuntimeError):
    pass

def classify_anchor_recovery(database_path, anchor_path, trusted_keys: Mapping[str, bytes],
                            externally_held_minimum_sequence: int):
    """Return conservative recovery classification and forensic inventory.

    PASS means the final anchor authenticates and matches the live registry.
    INDETERMINATE means no final anchor is available or orphan stage files exist.
    FAIL_CLOSED means an existing final anchor is malformed, unauthenticated,
    rolled back, or mismatched. Staged files are never trusted or auto-promoted.
    """
    path = Path(anchor_path)
    parent = path.parent
    if not parent.exists() or not parent.is_dir():
        return {"status": "FAIL_CLOSED", "reason": "anchor parent missing or invalid",
                "staged_files": []}
    staged = sorted(p.name for p in parent.glob(".anchor-stage-*") if p.is_file())
    if not path.exists():
        return {"status": "INDETERMINATE", "reason": "final anchor missing",
                "staged_files": staged, "recovery_action": "manual authenticated recovery required"}
    try:
        anchor = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {"status": "FAIL_CLOSED", "reason": "final anchor unreadable or malformed",
                "staged_files": staged}
    if not isinstance(anchor, dict):
        return {"status": "FAIL_CLOSED", "reason": "final anchor is not an object",
                "staged_files": staged}
    try:
        result = verify_authenticated_anchor(database_path, anchor, trusted_keys,
                                           externally_held_minimum_sequence)
    except (AnchorAuthenticationError, OSError, ValueError, TypeError):
        return {"status": "FAIL_CLOSED", "reason": "anchor authentication or registry verification failed",
                "staged_files": staged}
    if result.get("integrity") != "PASS":
        return {"status": "FAIL_CLOSED", "reason": "authenticated anchor does not match live registry",
                "staged_files": staged}
    if staged:
        return {"status": "INDETERMINATE", "reason": "valid final anchor plus orphan staging files",
                "staged_files": staged, "recovery_action": "preserve stages for forensic review; do not promote"}
    return {"status": "PASS", "reason": "final anchor authenticated and registry matched",
            "staged_files": [], "recovery_action": "no recovery required"}
