"""Durable, atomic replay nonce registry backed by SQLite.

Replay consumption is scoped to key_id + nonce, not evaluation_id, so a nonce
cannot be reused across different evaluations under the same key. Each consume
operation uses BEGIN IMMEDIATE and a UNIQUE constraint. Storage errors fail closed.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Union

class PersistentReplayError(RuntimeError):
    """Registry unavailable or unable to safely process a replay check."""

class PersistentReplayDetected(PersistentReplayError):
    """Nonce has already been consumed for this key."""

class PersistentReplayGuard:
    def __init__(self, database_path: Union[str, Path], *, timeout_seconds: float = 10.0):
        self.database_path = str(database_path)
        if self.database_path == ":memory:":
            raise ValueError("persistent replay guard requires a file-backed database")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self.timeout_seconds = timeout_seconds
        try:
            with self._connect() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS consumed_nonces (
                        key_id TEXT NOT NULL,
                        nonce TEXT NOT NULL,
                        evaluation_id TEXT NOT NULL,
                        consumed_at_utc TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                        PRIMARY KEY (key_id, nonce)
                    )
                """)
        except (sqlite3.Error, OSError) as exc:
            raise PersistentReplayError("cannot initialize persistent replay registry") from exc

    def _connect(self):
        conn = sqlite3.connect(self.database_path, timeout=self.timeout_seconds,
                              isolation_level=None)
        conn.execute("PRAGMA busy_timeout = %d" % int(self.timeout_seconds * 1000))
        return conn

    def consume(self, key_id: str, evaluation_id: str, nonce: str) -> None:
        if not all(isinstance(v, str) and v.strip() for v in (key_id, evaluation_id, nonce)):
            raise ValueError("key_id, evaluation_id and nonce must be non-empty strings")
        try:
            conn = self._connect()
            try:
                conn.execute("BEGIN IMMEDIATE")
                conn.execute("INSERT INTO consumed_nonces (key_id, nonce, evaluation_id) VALUES (?, ?, ?)",
                             (key_id, nonce, evaluation_id))
                conn.execute("COMMIT")
            except sqlite3.IntegrityError as exc:
                try:
                    conn.execute("ROLLBACK")
                except sqlite3.Error:
                    pass
                raise PersistentReplayDetected("nonce already consumed for this key") from exc
            except Exception:
                try:
                    conn.execute("ROLLBACK")
                except sqlite3.Error:
                    pass
                raise
            finally:
                conn.close()
        except PersistentReplayDetected:
            raise
        except (sqlite3.Error, OSError) as exc:
            raise PersistentReplayError("replay registry storage failure; rejected fail-closed") from exc
