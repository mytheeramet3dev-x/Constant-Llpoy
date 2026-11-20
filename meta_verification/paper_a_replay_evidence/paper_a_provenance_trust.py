"""Verifier-side trust registry and replay guard for authenticated provenance.
Trust records are supplied by the verifier; this module is not secure key storage.
"""
from __future__ import annotations
import hashlib
import hmac
from typing import Mapping, MutableSet
from paper_a_provenance_hmac import ProvenanceAuthError, canonical_payload

class TrustPolicyError(ValueError): pass
class ReplayDetected(TrustPolicyError): pass

class InMemoryReplayGuard:
    """Process-local guard only; not persistent or multi-process safe."""
    def __init__(self):
        self._seen: MutableSet[str] = set()
    def consume(self, evaluation_id: str, nonce: str) -> None:
        token = hashlib.sha256((evaluation_id + "\\0" + nonce).encode("utf-8")).hexdigest()
        if token in self._seen:
            raise ReplayDetected("evaluation/nonce pair already consumed")
        self._seen.add(token)

def verify_with_trust_policy(record: Mapping, mac_hex: str, trusted_keys: Mapping,
                            replay_guard: InMemoryReplayGuard, *, now: int,
                            max_age_seconds: int = 300, allowed_future_skew: int = 30) -> dict:
    required = {"key_id", "nonce", "issued_at"}
    if not isinstance(record, Mapping) or required - set(record):
        raise TrustPolicyError("record missing key_id, nonce, or issued_at")
    key_id, nonce, issued = record["key_id"], record["nonce"], record["issued_at"]
    if not isinstance(key_id, str) or not key_id.strip():
        raise TrustPolicyError("key_id must be non-empty")
    if not isinstance(nonce, str) or len(nonce) < 16:
        raise TrustPolicyError("nonce must be at least 16 characters")
    if not isinstance(issued, int) or isinstance(issued, bool):
        raise TrustPolicyError("issued_at must be integer timestamp")
    entry = trusted_keys.get(key_id)
    if not isinstance(entry, Mapping):
        raise TrustPolicyError("unknown key_id")
    if entry.get("revoked") is True:
        raise TrustPolicyError("key revoked")
    secret = entry.get("secret")
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise TrustPolicyError("trusted key material invalid")
    if issued > now + allowed_future_skew:
        raise TrustPolicyError("record issued too far in future")
    if now - issued > max_age_seconds:
        raise TrustPolicyError("record expired")
    if not isinstance(mac_hex, str) or len(mac_hex) != 64:
        raise ProvenanceAuthError("MAC format invalid")
    expected = hmac.new(secret, canonical_payload(record), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, mac_hex):
        raise TrustPolicyError("authentication failed")
    replay_guard.consume(record["evaluation_id"], nonce)
    return {"authenticated": True, "key_id": key_id, "replay_checked": True,
            "certification": "NOT_PERFORMED"}
