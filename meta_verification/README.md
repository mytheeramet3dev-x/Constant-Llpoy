# Meta-verification test harness (initial implementation)

## What this is

A small Python-standard-library policy evaluator and adversarial unit-test suite.
It checks whether a supplied evidence bundle is structurally complete, bound to
the expected claim/commit/checker/workflow revisions, and internally consistent
with the SHA-256 digests of the exact artifact bytes embedded in the bundle.

It is **not** a mathematical proof checker, Lean kernel, certificate semantics
checker, cryptographic signature verifier, or proof of evidence authenticity.
An evidence producer able to replace both artifact bytes and their digest can
forge a self-consistent bundle. Authenticity requires an independently trusted
acquisition or attestation route, which is not implemented here.

## Run tests

From the repository root:

```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```

## Evaluate an evidence bundle

```sh
python meta_verification/status_evaluator.py \
  --policy path/to/trusted-policy.json \
  --evidence path/to/evidence.json \
  --expected-commit "$GITHUB_SHA"
```

The policy is the trusted input and defines the required obligation IDs and
checker/workflow revisions. The expected commit must come from a trusted CI
context, not from the untrusted evidence document.

Exit codes: 0 = ACCEPTED; 1 = non-accepting result (REJECTED or INCONCLUSIVE);
2 = malformed policy/evidence or unsupported schema (ERROR).

## Fail-closed behavior

- Every policy obligation must appear exactly once.
- Missing, duplicate, unknown, stale, skipped, failed, errored, timed-out, or
  inconclusive evidence cannot produce ACCEPTED.
- Unknown fields and unsupported schema versions fail with ERROR.
- A REJECTED obligation or mismatched artifact digest yields REJECTED.
- A status string or `success=true` field supplied by the evidence producer
  is never used as an acceptance signal.
- Artifact bytes are embedded as base64 and hashed by this evaluator. The
  evaluator does not trust a supplied digest without recomputing it.

## Current limits

This first implementation has no signature/attestation verification, external
artifact retrieval, GitHub job-status ingestion, independent certificate
semantics checker, mutation runner against the Lean checker, or independent
review. Unit tests challenge the evaluator's policy logic; they do not prove
that evaluator correct or that upstream evidence is genuine.
