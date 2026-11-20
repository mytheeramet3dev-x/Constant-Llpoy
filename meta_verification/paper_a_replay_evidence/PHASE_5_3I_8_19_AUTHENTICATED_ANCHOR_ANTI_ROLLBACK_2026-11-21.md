# Phase 5.3I-8.19 — Authenticated Anchor & Anti-Rollback Verification (2026-11-21)

## Scope
- Canonical HMAC-SHA256 authentication of an external replay-registry anchor.
- Trusted-key lookup via verifier-supplied key registry.
- Explicit externally maintained minimum sequence floor; authenticated anchor below floor is rejected.
- Live registry digest and entry-count comparison; drift returns FAIL.
- Tests cover valid anchor, digest/MAC tampering, unknown key, rollback floor, live state drift, invalid sequence, and missing database.

## Trust boundary
The trusted-key map and minimum sequence floor are supplied independently. The module does not secure key custody, maintain a monotonic counter, rotate/revoke keys, store anchors, or advance the floor. HMAC is shared-secret authentication, not a public-key signature. If attacker can replace the key registry/floor and anchor together, rollback can evade detection. Certification is not performed.
