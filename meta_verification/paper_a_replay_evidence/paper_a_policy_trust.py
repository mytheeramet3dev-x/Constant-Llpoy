"""Verifier-side policy integrity pin gate (not a signature/authentication system)."""
from __future__ import annotations
import hashlib
import json
import re

_PIN_KEYS = {"policy_id", "version", "sha256", "approval_status", "approval_reference"}
_HEX = re.compile(r"^[0-9a-f]{64}$")

def canonical_policy_bytes(policy: dict) -> bytes:
    """Stable JSON representation; rejects non-JSON values and NaN."""
    return json.dumps(policy, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")

def policy_sha256(policy: dict) -> str:
    return hashlib.sha256(canonical_policy_bytes(policy)).hexdigest()

def verify_policy_pin(policy: dict, pin: dict) -> dict:
    """Fail closed unless policy exactly matches a verifier-maintained approved pin."""
    if not isinstance(policy, dict):
        return {"status": "FAIL", "reason": "policy_not_object"}
    if not isinstance(pin, dict) or set(pin) != _PIN_KEYS:
        return {"status": "FAIL", "reason": "pin_shape_invalid"}
    if any(not isinstance(pin.get(k), str) or not pin[k].strip() for k in ("policy_id", "version", "approval_reference")):
        return {"status": "FAIL", "reason": "pin_metadata_missing"}
    if pin.get("approval_status") != "approved":
        return {"status": "FAIL", "reason": "pin_not_approved"}
    if not isinstance(pin.get("sha256"), str) or not _HEX.fullmatch(pin["sha256"]):
        return {"status": "FAIL", "reason": "pin_digest_invalid"}
    if policy.get("policy_id") != pin["policy_id"] or policy.get("version") != pin["version"]:
        return {"status": "FAIL", "reason": "policy_identity_mismatch"}
    try:
        actual = policy_sha256(policy)
    except (TypeError, ValueError):
        return {"status": "FAIL", "reason": "policy_not_canonicalizable"}
    if actual != pin["sha256"]:
        return {"status": "FAIL", "reason": "policy_digest_mismatch"}
    return {"status": "PASS", "policy_id": pin["policy_id"], "version": pin["version"],
            "sha256": actual, "scope": "integrity_against_verifier_pin",
            "limitations": ["Pin approval provenance is not cryptographically authenticated here.",
                           "Digest pinning does not prove policy correctness or evidence completeness."]}
