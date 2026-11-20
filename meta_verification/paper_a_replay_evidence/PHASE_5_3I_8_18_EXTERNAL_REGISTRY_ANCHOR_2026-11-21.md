# Phase 5.3I-8.18 — External Registry Anchor Verification (2026-11-21)

## Implemented
- Added `paper_a_external_registry_anchor.py`, a verifier that compares the live registry logical snapshot digest and entry count with a separately supplied anchor.
- Missing, malformed, or wrong-schema anchors are rejected; missing/corrupt registry state fails closed; digest or count drift returns explicit `FAIL`.
- Added unit tests for anchor match, drift, database deletion, absent/malformed anchor, count mismatch, and schema mismatch.

## Trust boundary and limitations
- The anchor must be retained outside the registry and supplied independently by the operator/verifier.
- This module does **not** authenticate, protect, persist, advance, or recover the anchor.
- If an attacker can replace both the registry and the externally retained anchor, rollback may evade detection.
- No WORM storage, hardware monotonic counter, transparency log, backup custody, distributed consensus, or mathematical certification is implemented.
