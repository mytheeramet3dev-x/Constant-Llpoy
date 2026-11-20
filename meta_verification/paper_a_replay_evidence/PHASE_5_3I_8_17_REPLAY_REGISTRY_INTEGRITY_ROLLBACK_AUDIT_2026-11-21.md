# Phase 5.3I-8.17 — Replay Registry Integrity, Recovery & Rollback Audit

**Status: implementation committed; CI validation pending.**

## Implemented
- `paper_a_replay_registry_audit.py` performs SQLite `PRAGMA integrity_check`, checks the expected table exists, reads a deterministic sorted logical snapshot, and computes SHA-256 over canonical JSON.
- `verify_snapshot` compares the live logical snapshot to an expected digest held outside the database. Drift returns FAIL; malformed expected digest fails closed.
- Audit tests cover clean empty DB, expected snapshot match, post-insertion drift, missing DB, missing table, and malformed anchor.

## Security boundary
The snapshot digest is a detection mechanism only when the expected digest is retained independently and protected. If an attacker can modify the DB and the expected digest, they can defeat this check. It cannot detect rollback to an older DB when the expected anchor is also stale/rolled back. No external transparency log, hardware-backed anchor, trusted backup, automatic recovery, or mathematical certification is implemented.
