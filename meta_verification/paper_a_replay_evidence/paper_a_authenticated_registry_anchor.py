"""Authenticated external registry anchors with explicit anti-rollback floor.

The key registry and minimum sequence floor must be supplied by an independent
trusted channel; this module does not provide secure custody for either.
"""
from __future__ import annotations
import hashlib, hmac, json
from typing import Mapping
from paper_a_replay_registry_audit import logical_snapshot, ReplayRegistryAuditError

ANCHOR_SCHEMA = "paper-a-replay-registry-anchor-auth-v1"
SIGNED_FIELDS = ("schema", "key_id", "sequence", "snapshot_sha256", "entry_count")
HEX64 = set("0123456789abcdef")

class AnchorAuthenticationError(ReplayRegistryAuditError):
    pass

def canonical_anchor_payload(anchor):
    if not isinstance(anchor, dict):
        raise AnchorAuthenticationError("anchor must be an object")
    missing = [field for field in SIGNED_FIELDS if field not in anchor]
    if missing:
        raise AnchorAuthenticationError("anchor missing signed fields")
    payload = {field: anchor[field] for field in SIGNED_FIELDS}
    if payload["schema"] != ANCHOR_SCHEMA:
        raise AnchorAuthenticationError("anchor schema mismatch")
    if not isinstance(payload["key_id"], str) or not payload["key_id"].strip():
        raise AnchorAuthenticationError("key_id invalid")
    if type(payload["sequence"]) is not int or payload["sequence"] < 1:
        raise AnchorAuthenticationError("sequence invalid")
    digest = payload["snapshot_sha256"]
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in HEX64 for c in digest):
        raise AnchorAuthenticationError("snapshot digest invalid")
    if type(payload["entry_count"]) is not int or payload["entry_count"] < 0:
        raise AnchorAuthenticationError("entry_count invalid")
    try:
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise AnchorAuthenticationError("anchor cannot be canonicalized") from exc

def sign_anchor(anchor_fields, secret):
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise AnchorAuthenticationError("anchor secret must be at least 32 bytes")
    payload = canonical_anchor_payload(anchor_fields)
    return hmac.new(secret, payload, hashlib.sha256).hexdigest()

def verify_authenticated_anchor(database_path, anchor, trusted_keys: Mapping[str, bytes], minimum_sequence: int):
    payload = canonical_anchor_payload(anchor)
    key_id = anchor["key_id"]
    secret = trusted_keys.get(key_id) if isinstance(trusted_keys, Mapping) else None
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise AnchorAuthenticationError("anchor key not trusted or invalid")
    mac = anchor.get("mac_sha256")
    if not isinstance(mac, str) or len(mac) != 64 or any(c not in HEX64 for c in mac):
        raise AnchorAuthenticationError("anchor MAC malformed")
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, mac):
        raise AnchorAuthenticationError("anchor authentication failed")
    if type(minimum_sequence) is not int or minimum_sequence < 1:
        raise AnchorAuthenticationError("trusted minimum sequence invalid")
    if anchor["sequence"] < minimum_sequence:
        raise AnchorAuthenticationError("anchor rollback detected")
    snapshot = logical_snapshot(database_path)
    if snapshot["snapshot_sha256"] != anchor["snapshot_sha256"] or snapshot["entry_count"] != anchor["entry_count"]:
        return {**snapshot, "integrity": "FAIL", "reason": "registry state differs from authenticated anchor", "anchor_sequence": anchor["sequence"]}
    return {**snapshot, "integrity": "PASS", "authenticated_anchor": True, "anchor_sequence": anchor["sequence"], "key_id": key_id}
