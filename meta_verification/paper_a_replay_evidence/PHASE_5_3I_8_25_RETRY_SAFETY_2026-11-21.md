# Phase 5.3I-8.25 — Retry Safety, Idempotency & Duplicate Commit Prevention

## Goal
Prevent ambiguous anchor outcomes from being treated as permission for blind retries or duplicate sequence advancement.

## Added
- `paper_a_ambiguous_anchor_retry_gate.py`: read-only decision gate for recovery outcomes.
- `test_paper_a_ambiguous_anchor_retry_gate.py`: adversarial policy tests.
- README documentation.

## Decision behavior
- COMMITTED: deny retry (duplicate commit prevention).
- INDETERMINATE / FAIL_CLOSED / unknown state: deny retry.
- NOT_COMMITTED: still deny unless caller marks fresh revalidation and the observed sequence/digest exactly match expectations.
- Retry candidate requires a strict one-step sequence (`intended = previous + 1`) and previous sequence at/above independently held rollback floor.
- Candidate output deliberately reports `retry=false` and `execution_performed=false`; this module never performs a retry and requires the downstream writer to enforce compare-and-swap.

## Tests authored
10 unittest cases cover candidate-only outcome, missing revalidation, already committed state, indeterminate state, sequence jump, rollback floor, sequence mismatch, digest mismatch, bool-as-int rejection, and non-mapping recovery.

## Limitations / remaining threat
This is policy logic, not atomic idempotency enforcement. Fresh revalidation is represented by a caller assertion; a race can still occur after revalidation. The writer must independently re-read authenticated state under its lock and enforce CAS. No distributed idempotency key or external custody is added. Tests are authored but require CI execution; no local test run is claimed. No mathematical certification.
