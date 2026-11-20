# Phase 5.3I-8.26 — Authenticated Single-Use Retry-Intent Tickets

## Objective
Turn a retry candidate into a scoped, authenticated, one-use intent token while keeping the retry executor outside this layer.

## Implementation
- `paper_a_retry_intent_ticket.py` issues HMAC-SHA256 tickets bound to key ID, nonce, previous sequence, previous digest, and intended sequence.
- Redemption verifies the MAC against a trusted key map, validates exact sequence/digest expectations, and consumes the nonce through the existing persistent SQLite replay guard.
- Successful redemption returns `REDEEMED`, `single_use=true`, `execution_performed=false`, and `requires_writer_cas=true`.
- Tests: `test_paper_a_retry_intent_ticket.py`.

## Adversarial test coverage
Valid redemption; duplicate redemption; MAC tampering; expectation mismatch; untrusted key; sequence jump rejected at issuance; bool-as-int rejected; nonce reuse scoped across key IDs.

## Safety boundary
The ticket is an authorization artifact, not a retry operation. It does not prevent a race between ticket redemption and writer execution. The writer must re-read authenticated state while holding its serialization lock and enforce compare-and-swap. SQLite replay safety is limited by deployment, backups, and rollback of its database. No distributed idempotency or mathematical certification is claimed.

## CI
Tests are authored and trigger the repository workflows. Their actual CI conclusions must be inspected before marking this phase complete.
