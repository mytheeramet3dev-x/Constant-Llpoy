# Phase 5.3I-8.20 — Atomic Anchor Advancement & Crash-Safe Transition

**Status:** implemented; CI validation pending.

## Scope
Introduces a local atomic update protocol for the authenticated replay-registry anchor. Advancement is serialized for cooperating processes using an advisory file lock, validates the current authenticated anchor and registry state first, checks caller-supplied compare-and-swap expectations (current sequence and digest), requires a strictly increasing next sequence, and writes the replacement using a same-directory temporary file, file fsync, atomic replace, and directory fsync.

## Fail-closed gates
- Current anchor must parse and authenticate against caller-supplied trusted keys.
- Current registry must match the anchor.
- External sequence floor is caller-supplied.
- Stale sequence/digest expectations are rejected.
- New sequence must strictly exceed expected sequence.
- Key must be trusted and signing secret must be at least 32 bytes.
- Read-back must exactly match committed anchor.

## Tests added
Atomic success/read-back, stale sequence, stale digest, non-increasing sequence, corrupt current anchor, untrusted signing key, replace failure preserving old anchor, and registry drift.

## Limitations
The lock serializes cooperating local processes only. The external sequence floor must remain independently held and updated by a trusted actor/system; storing it beside the anchor defeats rollback resistance. Atomic replacement is filesystem-dependent. No secure key custody, distributed locking, external monotonic hardware, WORM storage, recovery automation, mathematical certification, or theorem verification is provided.

## Files
- `paper_a_atomic_anchor_advance.py`
- `test_paper_a_atomic_anchor_advance.py`
