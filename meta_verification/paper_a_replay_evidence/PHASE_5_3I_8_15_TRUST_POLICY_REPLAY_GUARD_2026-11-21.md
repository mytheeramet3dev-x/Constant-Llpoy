# Phase 5.3I-8.15 — Independent Trust Policy and Replay Guard

**Status: implementation committed; CI validation pending.**

## Implemented
- Verifier-side trusted-key registry lookup by key identifier; unknown keys fail closed.
- Explicit revoked-key rejection.
- Authentication over full provenance record, including key_id, nonce, issued_at, status, and other fields.
- Freshness checks with configurable maximum age and future-clock skew.
- Nonce length requirement and evaluation/nonce replay rejection through an in-memory guard.
- Authentication result is explicitly non-certifying.

## Adversarial tests
10 tests cover accepted trusted record, unknown key, revoked key, tampering, expiration, future timestamp, replay, weak nonce, missing timestamp, and boolean timestamp rejection.

## Important residual risks
- The trust registry and secret are supplied by caller; this module does not securely provision or store secrets.
- Replay guard is in-memory only; restart, concurrent workers, and distributed replay are not covered. Production needs persistent atomic replay storage.
- Time input is caller-supplied and requires a trusted clock.
- This phase does not provide key rotation, hardware custody, signature-based non-repudiation, or mathematical certification.

## CI update

- Replay Evidence Intake workflow for the corrected implementation commit `a7fbf4a` completed **success**: [run 44789093806](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44789093806).
- The first attempt failed because phase 8.14's canonical serializer incorrectly required all metadata to be strings, while 8.15 uses an integer `issued_at`. This was corrected by validating required identity strings and digests separately, allowing JSON-typed fields, and rejecting non-finite JSON numbers. The corrected intake run passed.
- Meta-verification harness run [44789093747](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44789093747) is still in progress; do not count it as passed yet.
