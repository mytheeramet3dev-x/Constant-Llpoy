"""Crash-safe authenticated registry-anchor advancement (Phase 5.3I-8.20).

The external rollback floor remains independently held by the caller. This module
cannot make a local anchor monotonic against an attacker able to roll back files.
"""
from __future__ import annotations
import fcntl
import json
import os
import tempfile
from pathlib import Path
from typing import Mapping

from paper_a_authenticated_registry_anchor import (
    ANCHOR_SCHEMA, AnchorAuthenticationError, sign_anchor,
    verify_authenticated_anchor,
)
from paper_a_replay_registry_audit import logical_snapshot

class AnchorAdvanceError(RuntimeError):
    pass

def _read_anchor(path: Path):
    try:
        raw = path.read_bytes()
        obj = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AnchorAdvanceError("existing anchor missing or unreadable") from exc
    if not isinstance(obj, dict):
        raise AnchorAdvanceError("existing anchor is not an object")
    return obj

def _durable_replace(path: Path, data: bytes):
    parent = path.parent
    fd, temp_name = tempfile.mkstemp(prefix=".anchor-stage-", dir=str(parent))
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "wb", closefd=True) as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
        dir_fd = os.open(parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise

def advance_authenticated_anchor(
    database_path,
    anchor_path,
    trusted_keys: Mapping[str, bytes],
    key_id: str,
    secret: bytes,
    externally_held_minimum_sequence: int,
    expected_current_sequence: int,
    expected_current_digest: str,
    new_sequence: int,
):
    """Validate the existing signed anchor, then atomically advance its file.

    A stable lock path serializes cooperating processes. CAS expectations prevent
    stale writers. Sequence floor is supplied from independent custody.
    """
    path = Path(anchor_path)
    if not path.parent.exists() or not path.parent.is_dir():
        raise AnchorAdvanceError("anchor parent directory must already exist")
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise AnchorAdvanceError("signing secret must be at least 32 bytes")
    if key_id not in trusted_keys or trusted_keys[key_id] != secret:
        raise AnchorAdvanceError("signing key is not present in trusted key map")
    if type(expected_current_sequence) is not int or expected_current_sequence < 1:
        raise AnchorAdvanceError("expected current sequence invalid")
    if type(new_sequence) is not int or new_sequence <= expected_current_sequence:
        raise AnchorAdvanceError("new sequence must strictly increase")
    if not isinstance(expected_current_digest, str) or len(expected_current_digest) != 64:
        raise AnchorAdvanceError("expected digest malformed")
    lock_path = path.with_name(path.name + ".lock")
    with open(lock_path, "a+b") as lock_stream:
        fcntl.flock(lock_stream.fileno(), fcntl.LOCK_EX)
        current = _read_anchor(path)
        try:
            verified = verify_authenticated_anchor(
                database_path, current, trusted_keys,
                externally_held_minimum_sequence,
            )
        except (AnchorAuthenticationError, OSError, ValueError) as exc:
            raise AnchorAdvanceError("current anchor failed authentication/integrity gate") from exc
        if verified.get("integrity") != "PASS":
            raise AnchorAdvanceError("current registry state does not match anchor")
        if current.get("sequence") != expected_current_sequence:
            raise AnchorAdvanceError("stale writer: current sequence mismatch")
        if current.get("snapshot_sha256") != expected_current_digest:
            raise AnchorAdvanceError("stale writer: current digest mismatch")
        snap = logical_snapshot(database_path)
        fields = {
            "schema": ANCHOR_SCHEMA,
            "key_id": key_id,
            "sequence": new_sequence,
            "snapshot_sha256": snap["snapshot_sha256"],
            "entry_count": snap["entry_count"],
        }
        next_anchor = {**fields, "mac_sha256": sign_anchor(fields, secret)}
        encoded = (json.dumps(next_anchor, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        _durable_replace(path, encoded)
        # Read-back verifies that the committed bytes parse and match what was written.
        committed = _read_anchor(path)
        if committed != next_anchor:
            raise AnchorAdvanceError("atomic anchor read-back mismatch")
        return {**snap, "anchor_sequence": new_sequence, "integrity": "PASS",
                "atomic_commit": True, "key_id": key_id}
