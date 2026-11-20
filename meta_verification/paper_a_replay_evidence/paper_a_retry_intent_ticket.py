"""Authenticated single-use retry-intent tickets (Phase 5.3I-8.26).

This module issues and redeems retry intents, not anchor writes. Redemption is
single-use per key_id + nonce via the persistent SQLite replay guard.
"""
from __future__ import annotations
import hashlib
import hmac
import json
from typing import Mapping

from paper_a_persistent_replay_guard import PersistentReplayGuard, PersistentReplayError


TICKET_SCHEMA = "paper-a-anchor-retry-intent-v1"
_FIELDS = ("schema", "key_id", "nonce", "expected_previous_sequence",
           "expected_previous_digest", "intended_sequence")


def _canonical(fields):
    if not isinstance(fields, dict) or any(k not in fields for k in _FIELDS):
        raise ValueError("retry ticket fields missing")
    if fields["schema"] != TICKET_SCHEMA:
        raise ValueError("retry ticket schema invalid")
    for k in ("key_id", "nonce", "expected_previous_digest"):
        if not isinstance(fields[k], str) or not fields[k].strip():
            raise ValueError(f"{k} invalid")
    for k in ("expected_previous_sequence", "intended_sequence"):
        if type(fields[k]) is not int or fields[k] < 1:
            raise ValueError(f"{k} invalid")
    if fields["intended_sequence"] != fields["expected_previous_sequence"] + 1:
        raise ValueError("retry sequence must advance exactly one")
    if len(fields["expected_previous_digest"]) != 64 or any(c not in "0123456789abcdef" for c in fields["expected_previous_digest"]):
        raise ValueError("previous digest malformed")
    return json.dumps({k: fields[k] for k in _FIELDS}, sort_keys=True,
                     separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def issue_retry_intent_ticket(*, key_id, nonce, expected_previous_sequence,
                              expected_previous_digest, intended_sequence, secret):
    fields = {"schema": TICKET_SCHEMA, "key_id": key_id, "nonce": nonce,
              "expected_previous_sequence": expected_previous_sequence,
              "expected_previous_digest": expected_previous_digest,
              "intended_sequence": intended_sequence}
    payload = _canonical(fields)
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise ValueError("ticket secret must be at least 32 bytes")
    return {**fields, "hmac_sha256": hmac.new(secret, payload, hashlib.sha256).hexdigest()}


def redeem_retry_intent_ticket(*, ticket, trusted_keys: Mapping[str, bytes],
                               expected_previous_sequence, expected_previous_digest,
                               intended_sequence, replay_guard: PersistentReplayGuard):
    if not isinstance(ticket, dict):
        return {"status": "DENY", "reason": "ticket must be a mapping"}
    try:
        # Validate caller expectations strictly; bool is an int subclass in Python.
        if (type(expected_previous_sequence) is not int or expected_previous_sequence < 1 or
            type(intended_sequence) is not int or intended_sequence != expected_previous_sequence + 1 or
            not isinstance(expected_previous_digest, str) or len(expected_previous_digest) != 64 or
            any(c not in "0123456789abcdef" for c in expected_previous_digest)):
            return {"status": "DENY", "reason": "retry expectations malformed"}
        payload = _canonical(ticket)
        key_id = ticket["key_id"]
        secret = trusted_keys.get(key_id) if isinstance(trusted_keys, Mapping) else None
        mac = ticket.get("hmac_sha256")
        if not isinstance(secret, bytes) or len(secret) < 32:
            raise ValueError("ticket key is untrusted")
        if not isinstance(mac, str) or len(mac) != 64:
            raise ValueError("ticket MAC malformed")
        expected_mac = hmac.new(secret, payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_mac, mac):
            raise ValueError("ticket authentication failed")
        if (ticket["expected_previous_sequence"] != expected_previous_sequence or
            ticket["expected_previous_digest"] != expected_previous_digest or
            ticket["intended_sequence"] != intended_sequence):
            return {"status": "DENY", "reason": "ticket does not match current retry expectations"}
        replay_guard.consume(key_id, "anchor-retry-ticket", ticket["nonce"])
        return {"status": "REDEEMED", "single_use": True,
                "execution_performed": False, "requires_writer_cas": True}
    except Exception:
        # Fail closed even when a replay-guard adapter raises an unexpected error.
        return {"status": "DENY", "reason": "ticket invalid, untrusted, replay guard unavailable, or already consumed"}
