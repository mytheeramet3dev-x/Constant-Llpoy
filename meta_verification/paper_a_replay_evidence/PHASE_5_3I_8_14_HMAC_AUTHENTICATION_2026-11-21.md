# Phase 5.3I-8.14 — Cryptographic Provenance Record Authentication

**Status: implemented; CI validation pending.**

## Scope
Added HMAC-SHA256 authentication over the complete provenance record using deterministic JSON serialization (sorted keys, compact separators, UTF-8). Core identity and digest fields are required and validated; SHA-256 fields must be lowercase hexadecimal. MAC comparison uses `hmac.compare_digest`.

## Adversarial coverage
Tests cover valid authentication, status/evidence/certification field tampering, wrong key, insufficient key length, missing fields, malformed digest/MAC and invalid field types.

## Trust and limitations
HMAC is symmetric: signing and verification share a secret. This provides record integrity/authentication only if the secret is securely provisioned and held by trusted parties. No production secret, key custody, rotation, revocation, hardware protection, external anchoring, or authenticated trust-root provisioning is configured. CI uses test-only key material. Authentication does not validate numerical evidence or mathematical truth, and it does not certify the Paper A claim.

## Files
- `paper_a_provenance_hmac.py`
- `test_paper_a_provenance_hmac.py`

