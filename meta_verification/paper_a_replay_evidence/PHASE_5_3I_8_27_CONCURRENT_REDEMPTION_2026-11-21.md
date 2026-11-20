# Phase 5.3I-8.27 — Concurrent Retry-Intent Ticket Redemption

## Scope
Test whether multiple concurrent callers can redeem the exact same authenticated retry-intent ticket against the persistent SQLite replay guard.

## Test change
- Eight worker threads use independent `PersistentReplayGuard` instances pointing at the same file-backed database.
- A barrier releases the workers together to contend on the same signed ticket/nonce.
- The test requires exactly one `REDEEMED` result and seven `DENY` results.
- Worker joins are bounded and any hung thread fails the test.

## Security boundary
This test exercises local concurrent nonce consumption through SQLite's transactional uniqueness behavior. It is not a distributed or multi-host concurrency proof. Redemption does not execute an anchor write; the eventual writer must independently re-read authenticated live state and enforce compare-and-swap (CAS). Post-redemption races, filesystem crash durability, malicious storage rollback, and mathematical certification remain outside scope.

## Verification status
The test is committed and CI is triggered by repository workflows. CI must be checked against the final commit SHA before this phase is declared closed. No local test execution is claimed.


## CI correction record
The initial test commit introduced an accidental dangling test variable in the key-scoped nonce test. The replay-intake CI run exposed the test failure; the variable was removed in corrective commit `eafed96f013ce456a7ead7054686dfd9eccc6fb6`. The replay-intake workflow on that corrected SHA completed successfully. The meta-verification workflow was still pending at the time this report was updated.
