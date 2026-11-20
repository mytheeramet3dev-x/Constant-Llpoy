# Phase 5.3I-8.12 — Independent Evidence Status Semantics

Date: 2026-11-21

## Purpose
Define conservative status meaning and reject status mutation, unsupported PASS,
and downstream status leakage within an evaluation record.

## Status vocabulary
- `PASS`: only the declared scope was checked; requires evidence IDs and valid context digests.
- `FAIL`: declared scope failed; requires a reason.
- `NOT_EVALUATED`: scope was not checked; requires a reason.
- `INDETERMINATE`: available information cannot decide; requires a reason.
- `NOT_APPLICABLE`: scope is explicitly inapplicable; requires a reason.
- `FAIL_CLOSED`: an upstream gate blocked execution; downstream must be `NOT_EVALUATED`.

## Context binding and continuity
Records bind an evaluation ID, scope, evidence bundle SHA-256, and policy SHA-256.
Same evaluation ID must preserve the entire record; changing status, evidence, or digest
requires a new evaluation ID. This rejects within-record PASS elevation and stale-context
mutation. New evaluation IDs permit re-evaluation but are not evidence of correctness.

## Implementation
- `paper_a_evidence_status_semantics.py`: record validation and continuity guard.
- `test_paper_a_evidence_status_semantics.py`: adversarial unit tests.

## Limitations
This module is a status-contract validator, not a full lifecycle database or signed
record store. It cannot authenticate evaluation IDs, enforce uniqueness across
distributed storage, establish digest provenance, or certify mathematical claims.
PASS is never equivalent to overall certification; certification remains
`NOT_PERFORMED` unless a separate authorized certification procedure exists.
