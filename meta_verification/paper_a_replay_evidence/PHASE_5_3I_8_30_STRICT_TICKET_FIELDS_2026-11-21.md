# Phase 5.3I-8.30 — Strict Ticket Field Allowlist

## Change
Ticket redemption now requires the mapping keys to exactly match the defined ticket fields plus `hmac_sha256`. Unknown extensions and missing fields are rejected.

## Adversarial tests
- Injected unknown field is denied.
- Missing nonce field is denied.

## Scope
This reduces ambiguity from silently ignored fields. Schema extensions require an explicit versioned change. It does not execute anchor writes, replace writer CAS, provide distributed coordination, or certify mathematics.

## Verification
CI status is pending on this report commit and must be inspected before closing the phase.
