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

## Signed provenance generation and independent verification
`.github/workflows/meta-verification-evidence.yml` runs after the harness,
checks out the exact default-branch commit associated with the event, collects
the upstream run record, and uses the commit-pinned `actions/attest` action to
create a Sigstore-signed SLSA provenance attestation for the exact evidence bytes.

A separate `.github/workflows/meta-verification-provenance-verify.yml` runs
after the producer workflow completes. It checks out the producer run's exact
source commit, downloads the evidence artifact from that run, and invokes
`gh attestation verify` without accepting a caller-supplied attestation bundle.
It enforces repository and signer-workflow identity, GitHub Actions OIDC issuer,
SLSA provenance v1, source branch and exact source commit, and rejects
self-hosted runners. The verifier additionally checks the certificate's
repository ID, source ref, source commit, signer commit, verified timestamp
evidence, and the SHA-256 digest of the exact local subject bytes.

The verifier pins GitHub CLI to version `2.103.3` and fails closed if the runner
provides another version. It also fails closed on missing or ambiguous subjects,
stale commits, wrong repository identity, missing timestamps, malformed output,
or failed signature verification. Its JSON output is a verification report, not itself
a cryptographic attestation.

This is **bounded cryptographic provenance verification**, not proof that the
collector's predicate claims are true, that the collector is defect-free, or
that the mathematical proof is correct. SLSA predicate contents are producer
controlled; policy relies on verified certificate fields and exact subject
digest. Repository administrators able to change both producer and verifier
workflows/policy remain inside the trust boundary. A separately governed trust-root bootstrap verifier now exists in `meta_verification/external_trust_root.py`, with a manual workflow at `.github/workflows/meta-trust-root-bootstrap.yml`. It verifies an Ed25519-signed external manifest, pinned manifest/key digests, immutable external checkout commit, actual GitHub repository IDs, signer identity, trusted-builder identity, and validity window. It fails closed when protected Environment inputs are missing.

**Activation is not complete:** no external trust-root package, signing key, or trusted-builder identity was supplied or provisioned in this work, and the protected `meta-trust-root` Environment/reviewer configuration has not been verified. The GitHub API returned no repository rulesets; branch-protection details were not accessible to the connected integration. The current evidence producer still signs in the relying-party repository. The external manifest's builder identity is an authorization contract only; it is not yet the active builder. The bootstrap workflow also requires independently configured Environment reviewers and branch/ruleset protection. A repository administrator able to change both workflow code and Environment governance remains privileged.

Artifact attestations are supported here because this repository is public.
The current evidence attestation uses GitHub's hosted public Sigstore trust infrastructure; the new Ed25519 root-package verifier is designed to consume a separately governed root but is not active until external provisioning is completed.

## Tests
```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```
Tests use fixed certificate/statement fixtures to test policy enforcement.
The actual evidence signature and certificate-chain verification is delegated to
GitHub CLI's `gh attestation verify` in the separate verification workflow. The external trust-root package uses OpenSSL Ed25519 verification and pinned SHA-256 values. Neither route is a mathematical proof checker.


## Independent trusted-builder contract

The normative external builder interface and activation requirements are in [`TRUSTED_BUILDER_CONTRACT.md`](TRUSTED_BUILDER_CONTRACT.md), with the strict output structure in [`trusted_builder_report.schema.json`](trusted_builder_report.schema.json). Structural regression tests are in [`test_trusted_builder_contract.py`](test_trusted_builder_contract.py).

These files specify a contract only. No independent builder repository, repository ID, immutable workflow commit, or external trust-root authorization has been provisioned. The current in-repository signer remains the bounded implementation and must not be represented as an independent trusted builder.


## Local builder reference (non-trusted)

A local contract-validation reference is now implemented in `trusted_builder_reference.py`, with adversarial tests in `test_trusted_builder_reference.py` and its limitations documented in `TRUSTED_BUILDER_REFERENCE_IMPLEMENTATION.md`. It validates the exact normalized collector evidence shape, canonical record digest, subject byte digest, strict UTF-8/duplicate-key behavior, path confinement, caller identity fields, upstream run metadata, and success state. It does **not** sign, request OIDC, create an attestation, independently authenticate the supplied metadata, or establish trust. Its only positive status is `VALIDATED_LOCAL_UNTRUSTED`.

The reference was hardened to use descriptor-relative `O_NOFOLLOW` traversal, regular-file checks via `fstat`, bounded reads, and rejection of FIFO paths and non-standard JSON constants. The full harness passed 117 tests on commit `d8494c4f13aecf133ae156510e72ec689ee16fef` (run [44217266945](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217266945)). Its evidence was accepted by producer run [44217302386](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217302386), and separate verifier run [44217348019](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217348019) reported `VERIFIED` for one attestation and the exact subject digest. This local reference does not satisfy the external builder activation gate.


## Black-box Trusted Builder conformance tests

`test_trusted_builder_conformance.py` exercises `trusted_builder_reference.py` through its CLI in a separate process. It does not import the implementation module: known-answer evidence is constructed independently, exact process exit codes and JSON output are checked, and negative vectors cover caller/upstream identity, replay, revision binding, digest substitution, unsafe paths/symlinks, malformed JSON, unknown fields, rejected evidence, and size limits.

The suite also asserts the local-only status `VALIDATED_LOCAL_UNTRUSTED` and that signing, attestation, and trust remain false. On commit `7eae9f587f8426407b54abc58d9c1e78e374827c`, the full harness passed 137 tests in run [44220321270](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220321270).

This is black-box testing relative to the Python implementation, not an independently administered test authority: it remains in the same repository/CI trust boundary and tests a non-signing reference only. It does not activate or validate an external trusted builder.
