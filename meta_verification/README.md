# Meta-verification harness

## Policy evaluator
`status_evaluator.py` checks schema completeness, revision binding, obligation coverage,
and SHA-256 consistency of embedded artifact bytes. It is not a proof checker or authenticity oracle.

## GitHub Actions run evidence collector
`github_run_collector.py` queries GitHub REST API over HTTPS using a read-only
`GITHUB_TOKEN`. It binds the upstream run to the triggering event's run ID and
head commit, then checks repository, branch, event, workflow ID/path, pinned
workflow-file and evaluator-file blob SHAs, exact job set, required steps, and
completion conclusions. It emits a normalized JSON record with a deterministic
SHA-256 digest.

## Signed provenance generation and verification
`meta-verification-evidence.yml` checks out the exact default-branch commit
associated with the workflow-run event, collects the upstream run record, and
uses the pinned `actions/attest` action to generate a GitHub/Sigstore-signed
SLSA provenance attestation for the exact evidence file bytes.

`verify_signed_provenance.py` invokes `gh attestation verify` against the
repository's attestation API (not a caller-supplied bundle), enforcing:
- exact repository and signer workflow identity;
- GitHub Actions OIDC issuer;
- SLSA provenance v1 predicate;
- `refs/heads/main` source ref and exact source commit;
- no self-hosted runner;
- signing certificate repository ID;
- verified transparency-log/timestamp evidence; and
- SHA-256 of the exact local subject bytes.

The verifier fails closed on missing or ambiguous subjects, stale commits,
wrong repository identity, missing timestamps, malformed output, or failed
signature verification. Its JSON output is a verification report, not itself
a cryptographic attestation.

This is a **bounded cryptographic provenance check**, not proof that the
collector's predicate claims are true, that the collector is defect-free, or
that the mathematical proof is correct. The SLSA predicate body is producer
controlled; policy relies on verified certificate fields and exact subject
digest. A repository administrator able to change the workflow and policy can
still alter the trust policy. Independent governance/branch protection and a
trusted reusable builder outside the producer's control remain residual
requirements.

Artifact attestations are supported here because this repository is public.
The implementation uses GitHub's hosted public Sigstore trust infrastructure;
it is not an independently operated trust root.

## Tests
```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```
Tests use fixed certificate/statement fixtures and mock-free policy validation;
the actual signature and certificate-chain verification is delegated to the
GitHub CLI's `gh attestation verify` implementation in CI.
