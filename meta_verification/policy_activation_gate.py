#!/usr/bin/env python3
"""Externally pinned activation gate for the structural status aggregator.

A policy proposal signature is not activation. This gate requires an externally
pinned authority-set digest AND an externally pinned, threshold-signed ACTIVE
record before delegating to the existing structural aggregator.
"""
from __future__ import annotations
import base64, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from typing import Any
from status_aggregator import aggregate, AggregationError

SHA256 = re.compile(r"^[0-9a-f]{64}$")
AUTHORITY_KEYS = {"schema_version", "authority_set_id", "threshold", "reviewers"}
RECORD_KEYS = {"schema_version", "policy_id", "policy_sha256", "sequence",
               "authority_set_sha256", "status", "issued_at", "expires_at", "signatures"}
SIGNATURE_KEYS = {"reviewer_id", "signature_base64"}

class ActivationError(ValueError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ActivationError(message)

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result

def strict_json(raw: bytes, label: str) -> Any:
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                          parse_constant=lambda x: (_ for _ in ()).throw(ActivationError(f"{label}: non-standard constant {x}")))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ActivationError(f"{label}: invalid UTF-8 JSON: {exc}") from None

def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")

def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def exact(value: Any, keys: set[str], label: str) -> dict:
    require(isinstance(value, dict) and set(value) == keys, f"{label} has missing or unknown fields")
    return value

def positive_int(value: Any, label: str) -> int:
    require(type(value) is int and value > 0, f"{label} must be a positive integer")
    return value

def verify_activation(policy_bytes: bytes, policy: Any, authority_bytes: bytes, activation_bytes: bytes,
                      *, expected_authority_sha256: str, expected_activation_sha256: str,
                      expected_policy_id: str, expected_policy_sequence: int, now_epoch: int) -> dict:
    require(isinstance(expected_authority_sha256, str) and SHA256.fullmatch(expected_authority_sha256) is not None,
            "external authority pin is missing or malformed")
    require(isinstance(expected_activation_sha256, str) and SHA256.fullmatch(expected_activation_sha256) is not None,
            "external active-policy pin is missing or malformed")
    require(digest(authority_bytes) == expected_authority_sha256, "authority-set digest differs from external pin")
    require(digest(activation_bytes) == expected_activation_sha256, "activation-record digest differs from external pin")
    authorities = exact(strict_json(authority_bytes, "authority set"), AUTHORITY_KEYS, "authority set")
    require(authorities["schema_version"] == "1.0", "unsupported authority-set schema")
    require(isinstance(authorities["authority_set_id"], str) and authorities["authority_set_id"].strip(),
            "authority_set_id must be non-empty")
    threshold = positive_int(authorities["threshold"], "authority threshold")
    reviewers = authorities["reviewers"]
    require(isinstance(reviewers, list) and bool(reviewers), "reviewers must be non-empty")
    keys = {}
    for index, item in enumerate(reviewers):
        exact(item, {"reviewer_id", "public_key_pem_base64"}, f"reviewers[{index}]")
        rid = item["reviewer_id"]
        require(isinstance(rid, str) and rid.strip() and rid not in keys, "reviewer identity is empty or duplicated")
        try:
            pem = base64.b64decode(item["public_key_pem_base64"], validate=True)
        except (ValueError, TypeError):
            raise ActivationError(f"reviewer {rid}: invalid public-key encoding") from None
        with tempfile.NamedTemporaryFile() as f:
            f.write(pem); f.flush()
            check = subprocess.run(["openssl", "pkey", "-pubin", "-in", f.name, "-text", "-noout"],
                                   capture_output=True, text=True, timeout=15)
        require(check.returncode == 0 and "ED25519 Public-Key:" in check.stdout,
                f"reviewer {rid}: key must be Ed25519")
        keys[rid] = pem
    require(threshold <= len(keys), "authority threshold exceeds reviewer count")

    record = exact(strict_json(activation_bytes, "activation record"), RECORD_KEYS, "activation record")
    require(record["schema_version"] == "1.0", "unsupported activation-record schema")
    require(record["policy_id"] == expected_policy_id, "active policy ID mismatch")
    require(record["policy_sha256"] == digest(policy_bytes), "active policy digest does not match exact policy bytes")
    require(type(record["sequence"]) is int and record["sequence"] == expected_policy_sequence,
            "active policy sequence mismatch")
    require(record["authority_set_sha256"] == expected_authority_sha256,
            "activation record authority-set digest mismatch")
    require(record["status"] == "ACTIVE", "policy is authorized but not marked ACTIVE")
    for field in ("issued_at", "expires_at"):
        require(isinstance(record[field], str) and record[field].isdigit(), f"{field} must be an epoch string")
    issued, expires = int(record["issued_at"]), int(record["expires_at"])
    require(issued < expires and issued <= now_epoch < expires, "active policy record is outside its validity interval")
    signatures = record["signatures"]
    require(isinstance(signatures, list), "activation signatures must be a list")
    signed_fields = {key: record[key] for key in RECORD_KEYS if key != "signatures"}
    message = canonical(signed_fields)
    accepted = set()
    for index, signature in enumerate(signatures):
        item = exact(signature, SIGNATURE_KEYS, f"signatures[{index}]")
        rid = item["reviewer_id"]
        require(isinstance(rid, str) and rid.strip() and rid not in accepted,
                "activation contains an empty or duplicate reviewer")
        require(rid in keys, f"activation signer is not authorized: {rid}")
        try:
            raw_signature = base64.b64decode(item["signature_base64"], validate=True)
        except (ValueError, TypeError):
            raise ActivationError(f"reviewer {rid}: invalid signature encoding") from None
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); key = root / "key.pem"; sig = root / "signature"; msg = root / "message"
            key.write_bytes(keys[rid]); sig.write_bytes(raw_signature); msg.write_bytes(message)
            checked = subprocess.run(["openssl", "pkeyutl", "-verify", "-pubin", "-inkey", str(key),
                                       "-rawin", "-in", str(msg), "-sigfile", str(sig)],
                                      capture_output=True, timeout=15)
        require(checked.returncode == 0, f"reviewer {rid}: invalid activation signature")
        accepted.add(rid)
    require(len(accepted) >= threshold, "activation signature threshold not met")
    return {"status": "POLICY_ACTIVE", "policy_id": expected_policy_id,
            "policy_sha256": digest(policy_bytes), "sequence": expected_policy_sequence,
            "authority_set_sha256": expected_authority_sha256,
            "activation_record_sha256": expected_activation_sha256,
            "valid_reviewer_ids": sorted(accepted), "threshold": threshold}

def evaluate_active_policy(policy_bytes: bytes, policy: Any, authority_bytes: bytes, activation_bytes: bytes,
                           bundle: Any, expected_commit: str, *, expected_authority_sha256: str,
                           expected_activation_sha256: str, expected_policy_id: str,
                           expected_policy_sequence: int, now_epoch: int) -> dict:
    active = verify_activation(policy_bytes, policy, authority_bytes, activation_bytes,
        expected_authority_sha256=expected_authority_sha256,
        expected_activation_sha256=expected_activation_sha256,
        expected_policy_id=expected_policy_id, expected_policy_sequence=expected_policy_sequence,
        now_epoch=now_epoch)
    result = aggregate(policy, bundle, expected_commit)
    return {"status": ("POLICY_ACTIVE_AND_BUNDLE_STRUCTURALLY_ACCEPTED"
                       if result["status"] == "ACCEPTED" else result["status"]),
            "status_scope": "ACTIVE_POLICY_GATED_STRUCTURAL_BUNDLE_EVALUATION_ONLY",
            "assurance_level": "AUTHORITY_AND_ACTIVATION_PINS_REQUIRED_BUT_COMPONENT_RECEIPTS_REMAIN_STRUCTURAL",
            "active_policy": active, "bundle_evaluation": result}

