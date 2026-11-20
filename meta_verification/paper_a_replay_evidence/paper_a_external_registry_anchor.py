"""Verify replay-registry state against a separately retained external anchor.

The anchor is an input from an external trust/custody channel. This module does
not create, store, authenticate, or advance that anchor.
"""
from __future__ import annotations
from paper_a_replay_registry_audit import logical_snapshot, ReplayRegistryAuditError

ANCHOR_SCHEMA = "paper-a-replay-registry-anchor-v1"

def verify_external_anchor(database_path, anchor):
    if not isinstance(anchor, dict):
        raise ReplayRegistryAuditError("external anchor must be an object")
    if anchor.get("schema") != ANCHOR_SCHEMA:
        raise ReplayRegistryAuditError("external anchor schema mismatch")
    digest = anchor.get("snapshot_sha256")
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise ReplayRegistryAuditError("external anchor digest invalid")
    count = anchor.get("entry_count")
    if type(count) is not int or count < 0:
        raise ReplayRegistryAuditError("external anchor entry_count invalid")
    snapshot = logical_snapshot(database_path)
    if snapshot["snapshot_sha256"] != digest or snapshot["entry_count"] != count:
        return {**snapshot, "integrity": "FAIL", "reason": "registry state differs from external anchor", "anchor_schema": ANCHOR_SCHEMA}
    return {**snapshot, "integrity": "PASS", "external_anchor_match": True, "anchor_schema": ANCHOR_SCHEMA}
