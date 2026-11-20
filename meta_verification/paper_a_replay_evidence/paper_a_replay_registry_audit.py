"""Audit integrity of persistent replay registry using SQLite checks and snapshots.
A snapshot digest detects drift only relative to an independently retained expected digest.
It does not authenticate the anchor or detect rollback if the anchor is also rolled back.
"""
from __future__ import annotations
import hashlib, json, sqlite3
from pathlib import Path
from paper_a_persistent_replay_guard import PersistentReplayError

class ReplayRegistryAuditError(RuntimeError): pass

def logical_snapshot(database_path):
    path = Path(database_path)
    if not path.is_file():
        raise ReplayRegistryAuditError("registry database missing")
    try:
        with sqlite3.connect(str(path)) as conn:
            integrity = [row[0] for row in conn.execute("PRAGMA integrity_check")]
            if integrity != ["ok"]:
                raise ReplayRegistryAuditError("SQLite integrity_check failed")
            rows = conn.execute(
                "SELECT key_id, nonce, evaluation_id, consumed_at_utc "
                "FROM consumed_nonces ORDER BY key_id, nonce"
            ).fetchall()
            schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='consumed_nonces'").fetchone()
            if schema is None:
                raise ReplayRegistryAuditError("expected registry table absent")
    except ReplayRegistryAuditError:
        raise
    except (sqlite3.Error, OSError) as exc:
        raise ReplayRegistryAuditError("cannot audit registry database") from exc
    payload = {"schema":schema[0],"entries":[list(r) for r in rows]}
    encoded = json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    return {"integrity":"PASS","entry_count":len(rows),"snapshot_sha256":hashlib.sha256(encoded).hexdigest()}

def verify_snapshot(database_path, expected_snapshot_sha256):
    if not isinstance(expected_snapshot_sha256,str) or len(expected_snapshot_sha256)!=64 or any(c not in "0123456789abcdef" for c in expected_snapshot_sha256):
        raise ReplayRegistryAuditError("expected snapshot digest must be lowercase SHA-256 hex")
    current = logical_snapshot(database_path)
    if current["snapshot_sha256"] != expected_snapshot_sha256:
        return {**current,"integrity":"FAIL","reason":"logical snapshot digest mismatch"}
    return {**current,"integrity":"PASS","snapshot_match":True}
