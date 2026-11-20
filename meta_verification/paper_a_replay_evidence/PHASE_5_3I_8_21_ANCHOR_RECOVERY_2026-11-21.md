# Phase 5.3I-8.21 — Anchor Recovery Classification & Fail-Closed Forensics

## Scope
Adds a recovery classifier for interrupted anchor advancement. It examines the final anchor, authenticates it against caller-supplied trusted keys and an independently held sequence floor, and compares it to the live registry. Orphan staging files are inventoried but never automatically promoted.

## Status semantics
- PASS: final anchor authenticates and matches the live registry; no orphan stage files.
- INDETERMINATE: final anchor missing, or a valid final anchor coexists with stage artifacts requiring forensic review.
- FAIL_CLOSED: final anchor malformed, non-object, unauthenticated, rolled back, or registry mismatch.

## Tests
Valid anchor; orphan-stage preservation/no promotion; missing final anchor; malformed final anchor; registry drift; external floor rollback; non-object anchor.

## Limitations
This is a classifier, not automated recovery. Staged-file contents are not trusted. Filesystem-level attacker, rollback of independently held floor, key compromise, and forensic custody are outside this implementation. Manual recovery requires an independently authenticated source and operator decision.
