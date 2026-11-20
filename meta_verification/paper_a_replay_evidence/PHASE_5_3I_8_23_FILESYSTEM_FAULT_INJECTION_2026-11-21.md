# Phase 5.3I-8.23 — Filesystem Fault Injection at Anchor-Commit Boundaries

**Scope:** Controlled Python-level fault injection against the existing 8.20 atomic anchor writer. This is not power-loss testing, kernel crash simulation, filesystem certification, or a proof of durability.

## Added test coverage

`test_paper_a_anchor_filesystem_fault_injection.py` injects failures at:
- staging write,
- first fsync (staged file data),
- atomic replace,
- second fsync (parent directory after replacement),
- post-commit read-back.

The test checks whether the original anchor remains, whether staging artifacts are cleaned, and whether the newly replaced anchor is visible after errors occurring after replacement.

## Key finding / commit boundary

Failures **before** `os.replace` (staging write, file fsync, replace itself) are expected by these tests to leave the original anchor intact.

A failure **after** `os.replace` is different: the new anchor may already be visible even though the operation raises. The directory-fsync failure and read-back-failure tests explicitly assert sequence 6 is visible. Callers must treat such exceptions as **commit outcome uncertain**, not as proof that the update rolled back; blindly retrying with the old expected sequence can produce stale-writer rejection.

## Limitations

- Mocked exceptions exercise Python call boundaries only; they do not simulate power loss, kernel termination, device-cache behavior, storage-controller faults, or filesystem-specific guarantees.
- The tests do not establish durability across reboot.
- No production key custody, external sequence-floor custody, distributed writer coordination, or mathematical certification is provided.
- This suite is supplementary to the protocol state-machine model in 8.22 and the existing 8.20 tests.

## Verification status

Tests were committed to the repository. Their execution and CI status must be checked independently; repository write success is not a test-pass claim.
