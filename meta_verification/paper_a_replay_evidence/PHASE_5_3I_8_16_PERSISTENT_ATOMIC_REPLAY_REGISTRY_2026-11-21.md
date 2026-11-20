# Phase 5.3I-8.16 — Persistent and Atomic Replay Registry

**Status: implementation committed; CI validation pending.**

## Design
- SQLite file-backed registry with a UNIQUE/PRIMARY KEY constraint on `(key_id, nonce)`.
- Replay scope is key identifier + nonce, intentionally blocking reuse across evaluation IDs under the same key.
- Each consume operation uses `BEGIN IMMEDIATE` and commits the insertion atomically.
- The database survives process restart; opening a new guard instance does not reset replay state.
- Concurrent duplicate insertion is serialized by SQLite; only one insert can succeed.
- Initialization and storage failures reject the operation (fail closed); in-memory databases are prohibited.

## Tests
- Persistent duplicate detection after reopening the registry, including a changed evaluation ID.
- Nonce scope across key IDs.
- Two concurrent consumers competing for the same nonce.
- Empty identity rejection, in-memory DB rejection, and storage initialization failure.

## Limits
This is a durable local registry, not a distributed consensus service. Reliability depends on filesystem/database durability, deployment permissions, backup/restore behavior, and SQLite locking semantics. A rollback from a stale backup could re-enable previously consumed nonces. No production deployment, multi-host coordination, trusted time, secret custody, or mathematical certification is established.
