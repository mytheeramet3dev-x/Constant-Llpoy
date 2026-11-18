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


## Mutation adequacy testing

`test_trusted_builder_mutations.py` creates an isolated copy of the local CLI and black-box suite for each controlled mutant. It applies one targeted weakening, syntax-checks the mutated CLI, and requires the black-box suite to fail through a test assertion. Syntax or import failures do not count as mutant kills.

The current seven mutants target: subject-byte digest comparison, canonical evidence-record digest, `ACCEPTED` status, caller repository ID, upstream run ID/replay, path traversal, and escalation to `SIGNED`. The path-traversal vector uses a byte-identical file outside the checkout root so the later digest check cannot mask a traversal bypass.

**Observed result:** 7/7 selected mutants were killed. GitHub Actions run [44229439161](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229439161) passed 138 tests on commit `ad73206847bc15ca4d3d0b1db68f74ad1b3d6901`; logs explicitly report each mutant as killed. The 100% score applies only to this deliberately selected set and is not a claim of complete mutation coverage or external trust.


## Adversarial input-space expansion

The reference CLI now requires exact caller/upstream metadata key sets, rejects boolean-as-integer identity values, rejects duplicate JSON request keys and non-standard constants, and creates report files without following symlinks in parent or final path components. It uses exclusive file creation and preserves any pre-existing output rather than overwriting it. The provenance policy also requires an exact integer repository ID.

These defenses are covered by black-box CLI tests and provenance policy tests. GitHub Actions run [44229925358](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229925358) passed 150 tests on commit `32befb3a3bda45705794e4484f94abe8cbb9b677`; all seven selected mutation tests remained killed.

Coverage is explicit and bounded. The local reference still does not authenticate caller/upstream metadata, sign, create attestations, or establish trust.


## Signed-provenance verifier mutation tests

`test_provenance_mutations.py` tests whether `test_signed_provenance.py` detects ten controlled regressions in `verify_signed_provenance.py`: certificate repository ID, source ref, source commit, signer commit, timestamp, predicate type, subject digest, ambiguous subject matching, boolean repository ID policy, and pinned CLI version.

All 10/10 selected mutants were killed. GitHub Actions run [44230310401](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230310401) passed 151 tests on commit `8740ee0c024d4c30105d766d54679f563ee211cc`. The first attempt revealed a fixture-masking issue for the boolean-ID mutant; the fixture was corrected to isolate that check, and the corrected run killed it.

The score is bounded to the ten authored mutants and does not replace real attestation verification or external review.


## GitHub Actions run collector mutation testing

The collector now validates exact integer identity fields, requires a positive run attempt, checks repository/head-repository numeric identity, validates positive unique job IDs, and rejects incomplete/paginated job responses. Existing workflow and evaluator blob pins remain enforced.

The mutation harness applies 13 selected weakenings to the collector and requires the adversarial test suite to detect each through assertion failures. All 13/13 were killed. GitHub Actions run [44230994871](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230994871) passed 164 tests on commit `8d23997fd0d746ba04f2528a5e34721293ae5514`.

Initial runs exposed missing job-ID validation and three test fixtures that were masked by adjacent checks; both implementation and fixtures were corrected before the passing run. Coverage remains bounded to the 13 authored mutants. The collector is still an API evidence collector, not a cryptographic attestation verifier or an independent trust root.


## GitHub API response contract and replay resistance

The evidence producer now passes the triggering `workflow_run.run_attempt` to the collector. The collector requires the API run and every job to match the exact run ID and attempt, preventing cross-attempt job mixing. It also requires job IDs to be positive and unique.

API JSON parsing is bounded and strict: UTF-8 JSON object only, duplicate keys and non-standard constants rejected, top-level arrays/scalars rejected, and a 10 MiB response limit. HTTP errors and timeouts fail closed. The jobs endpoint is requested at 100 per page and the collector rejects incomplete counts or more than 100 jobs rather than accepting a partial page.

The test suite covers stale attempts, job/run mismatch, malformed/ambiguous JSON, oversized responses, HTTP errors, and timeouts. The mutation suite now tests 17 selected collector regressions; all 17/17 were killed. Full harness [44231737913](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44231737913) passed 176 tests on commit `295eea3e0e717569c3f981a3e272dc31b4de567d`.

This remains bounded testing against GitHub API responses; it is not an independent API trust root. Pagination intentionally fails closed above 100 jobs until a separately specified and tested multi-page contract is implemented.


## Component status aggregation (structural prototype)

`status_aggregator.py` evaluates a policy-bound bundle of component results. It binds claim ID, expected source commit, policy revision, required component set, per-component evidence bytes/digests, and the structure of provenance receipts. Missing, duplicate, unknown, stale, conflicting, non-PASS, or unverified inputs cannot produce acceptance. A verified component failure or evidence digest mismatch is rejected; malformed contracts return an error.

**Important authority boundary:** its `ACCEPTED` means only that the supplied bundle structurally satisfies the supplied policy. Output explicitly says `BUNDLE_POLICY_EVALUATION_ONLY` and `STRUCTURAL_ONLY_UNAUTHENTICATED_INPUTS`. It does not cryptographically authenticate a receipt merely because a JSON field says `VERIFIED`, does not verify mathematical proofs, and is not integrated as the production theorem-status gate. Do not use it to claim theorem acceptance.

Tests are in `test_status_aggregator.py`; selected mutation checks are in `test_status_aggregator_mutations.py`. The corrected full harness [44232385272](https://github.com/mytheeramet3-dev-x/Constant-Llpoy/actions/runs/44232385272) passed 202 tests and killed all 12 selected aggregator mutants. The initial run [44232264438](https://github.com/mytheeramet3-dev-x/Constant-Llpoy/actions/runs/44232264438) exposed a duplicate-record escalation bug and a mutation-fixture anchor problem; both were corrected before the passing run.

Production use still requires authenticated receipt acquisition, independently governed policy authority, exact verifier identity binding, and an end-to-end workflow integration audit.


## Policy authority and change control

See [POLICY_AUTHORITY_AND_CHANGE_CONTROL.md](POLICY_AUTHORITY_AND_CHANGE_CONTROL.md). The verifier and adversarial tests are in policy_change_control.py and test_policy_change_control.py; selected mutation checks are in test_policy_change_mutations.py. The verifier requires a separately supplied authority-set SHA-256 pin, a threshold of distinct Ed25519 reviewers, exact policy digest, parent digest, next sequence and validity interval. A valid proposal remains NOT_ACTIVATED until the external authority updates protected pins. This is a prototype; no independent authority or reviewer keys are provisioned, and no production workflow consumes it.


Policy-change verifier validation: full harness [44233157563](https://github.com/mytheeramet3-dev-x/Constant-Llpoy/actions/runs/44233157563) passed 219 tests; all 8/8 selected policy-change mutants were killed by assertion-driven tests. Evidence producer [44233215756](https://github.com/mytheeramet3-dev-x/Constant-Llpoy/actions/runs/44233215756) succeeded; separate provenance verifier [44233252327](https://github.com/mytheeramet3-dev-x/Constant-Llpoy/actions/runs/44233252327) reported VERIFIED for the exact tested commit. External policy authority remains NOT ACTIVE.


## Policy activation gate

`policy_activation_gate.py` wraps the existing structural `status_aggregator.py`; it does not replace or duplicate it. It requires separate externally supplied SHA-256 pins for the reviewer authority set and active-policy record. The record binds exact policy bytes, policy ID, sequence, authority-set digest, ACTIVE state, validity interval, and threshold Ed25519 signatures. Only after verification does the gate invoke the structural aggregator.

The final success status is `POLICY_ACTIVE_AND_BUNDLE_STRUCTURALLY_ACCEPTED`, not bare `ACCEPTED`. This is still a structural bundle result, not mathematical proof verification. Component provenance receipt fields are not cryptographically authenticated by this gate.

The design, status semantics, trust boundary, and non-activation limitations are in [POLICY_ACTIVATION_GATE.md](POLICY_ACTIVATION_GATE.md). Tests are in `test_policy_activation_gate.py`. No external authority, independent reviewer key custody, protected pin source, or production workflow invocation has been provisioned; therefore production activation remains NOT ACTIVE.


### Policy activation gate mutation testing

`test_policy_activation_mutations.py` applies nine selected activation-gate weakenings in isolated copies and requires the gate test suite to kill each through assertion failures. The selected cases cover external pins, ACTIVE-state distinction, sequence, policy digest, exact bytes/object binding, expiry, threshold, and signature verification. Results are bounded to this authored mutant set.
