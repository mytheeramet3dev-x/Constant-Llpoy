# Phase 5.3I-8.24 — Recovery Semantics After Ambiguous Commit

## Purpose
Classify the current authenticated anchor after a writer reports an error around replacement/read-back. This is read-only decision support; it does not retry, repair, delete staging files, or advance anchors.

## Outcomes
- **COMMITTED** — the intended sequence is present, authenticated, and the live replay registry matches it. Do not retry.
- **NOT_COMMITTED** — the previous sequence and digest remain authenticated and match live registry, with no staging artifacts. This is only a candidate safe-to-retry state; retry requires caller revalidation.
- **INDETERMINATE** — missing anchor, unexpected sequence, or any staging artifact; do not retry automatically.
- **FAIL_CLOSED** — malformed, unauthenticated, rolled-back below the external floor, or live registry mismatch; do not retry.

## Implementation
- `paper_a_ambiguous_anchor_commit_recovery.py` classifies expected previous/intended sequence states using trusted keys, independent sequence floor, and live-registry verification.
- `test_paper_a_ambiguous_anchor_commit_recovery.py` covers previous-state, intended-state, staging artifacts, missing anchor, unexpected sequence, digest mismatch, live registry drift, and malformed anchor.

## Safety boundary
The classifier is read-only and never promotes staging files. `NOT_COMMITTED` is not an automatic retry instruction. A successful authenticated read does not establish durability across power loss or reboot. External key and floor custody, filesystem durability, and mathematical certification remain outside this component.
