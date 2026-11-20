"""HMAC-SHA256 authentication for Paper A provenance records.

Authentication is only as strong as the externally provisioned secret and its
custody. This module does not create a production trust root or certify claims.
"""
from __future__ import annotations
import hashlib
import hmac
import json
from typing import Any, Mapping

REQUIRED = {
    "evaluation_id", "evidence_bundle_sha256", "policy_sha256",
    "verifier_id", "verifier_version", "environment_id", "result_record_sha256",
}
HEX64 = set("0123456789abcdef")

class ProvenanceAuthError(ValueError):
    pass

def canonical_payload(record: Mapping[str, Any]) -> bytes:
    if not isinstance(record, Mapping):
        raise ProvenanceAuthError("record must be a mapping")
    missing = REQUIRED - set(record)
    if missing:
        raise ProvenanceAuthError(f"missing fields: {sorted(missing)}")
    payload = dict(record)
    for k in REQUIRED - {"evidence_bundle_sha256", "policy_sha256", "result_record_sha256"}:
        if not isinstance(payload[k], str) or not payload[k].strip():
            raise ProvenanceAuthError(f"{k} must be a non-empty string")
    for k in ("evidence_bundle_sha256", "policy_sha256", "result_record_sha256"):
        v = payload[k]
        if len(v) != 64 or any(c not in HEX64 for c in v):
            raise ProvenanceAuthError(f"{k} must be lowercase SHA-256 hex")
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")

def authenticate_record(record: Mapping[str, Any], secret: bytes) -> str:
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise ProvenanceAuthError("secret must be at least 32 bytes")
    return hmac.new(secret, canonical_payload(record), hashlib.sha256).hexdigest()

def verify_record_authentication(record: Mapping[str, Any], secret: bytes, mac_hex: str) -> bool:
    if not isinstance(mac_hex, str) or len(mac_hex) != 64 or any(c not in HEX64 for c in mac_hex):
        raise ProvenanceAuthError("MAC must be lowercase 64-character hex")
    expected = authenticate_record(record, secret)
    return hmac.compare_digest(expected, mac_hex)
