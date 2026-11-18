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

`status_aggregator.py` evaluates a policy-bound component bundle and now requires an in-memory authenticated-receipt map before it can return `ACCEPTED`. Its standalone CLI never receives that map and therefore returns `INCONCLUSIVE` for otherwise complete but unauthenticated bundles. The production `policy_activation_gate.py` CLI creates the map internally only after `component_provenance_authenticator.py` verifies every required component's exact evidence bytes with GitHub/Sigstore.

**Important authority boundary:** a JSON field saying `VERIFIED` is never sufficient. Component provenance schema 2.0 binds exact subject digest, source commit, attestation run ID/attempt, and workflow revision. The direct verifier checks the GitHub certificate identity, source and signer commit, timestamps, SLSA predicate, exact subject digest, and signed `invocationId`. Even authenticated provenance does not verify mathematical proofs or theorem truth. The internal Python API is not a sandbox; production use must go through the CLI path.

Tests are in `test_status_aggregator.py`; selected mutation checks are in `test_status_aggregator_mutations.py`. The corrected full harness [44232385272](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44232385272) passed 202 tests and killed all 12 selected aggregator mutants. The initial run [44232264438](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44232264438) exposed a duplicate-record escalation bug and a mutation-fixture anchor problem; both were corrected before the passing run.

Tests use synthetic/fake GitHub CLI outputs and do not prove that real component artifacts currently have attestations. The existing producer signs `github-run-evidence.json`, not every component artifact. No component-evidence producer workflow or external policy pin source is active.


## Policy authority and change control

See [POLICY_AUTHORITY_AND_CHANGE_CONTROL.md](POLICY_AUTHORITY_AND_CHANGE_CONTROL.md). The verifier and adversarial tests are in policy_change_control.py and test_policy_change_control.py; selected mutation checks are in test_policy_change_mutations.py. The verifier requires a separately supplied authority-set SHA-256 pin, a threshold of distinct Ed25519 reviewers, exact policy digest, parent digest, next sequence and validity interval. A valid proposal remains NOT_ACTIVATED until the external authority updates protected pins. This is a prototype; no independent authority or reviewer keys are provisioned, and no production workflow consumes it.


Policy-change verifier validation: full harness [44233157563](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233157563) passed 219 tests; all 8/8 selected policy-change mutants were killed by assertion-driven tests. Evidence producer [44233215756](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233215756) succeeded; separate provenance verifier [44233252327](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233252327) reported VERIFIED for the exact tested commit. External policy authority remains NOT ACTIVE.


## Policy activation gate

`policy_activation_gate.py` wraps the existing structural `status_aggregator.py`; it does not replace or duplicate it. It requires separate externally supplied SHA-256 pins for the reviewer authority set and active-policy record. The record binds exact policy bytes, policy ID, sequence, authority-set digest, ACTIVE state, validity interval, and threshold Ed25519 signatures. Only after verification does the gate invoke the structural aggregator.

The final success status is `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`. The gate requires an externally pinned provenance-policy digest and verifies every component's exact evidence bytes directly before aggregation. It still does not establish mathematical correctness. The required external pins and per-component signed artifacts are not yet provisioned, so production activation remains NOT ACTIVE.

The design, status semantics, trust boundary, and non-activation limitations are in [POLICY_ACTIVATION_GATE.md](POLICY_ACTIVATION_GATE.md). Tests are in `test_policy_activation_gate.py`. No external authority, independent reviewer key custody, protected pin source, or production workflow invocation has been provisioned; therefore production activation remains NOT ACTIVE.


### Policy activation gate mutation testing

`test_policy_activation_mutations.py` applies nine selected activation-gate weakenings in isolated copies and requires the gate test suite to kill each through assertion failures. The selected cases cover external pins, ACTIVE-state distinction, sequence, policy digest, exact bytes/object binding, expiry, threshold, and signature verification. Results are bounded to this authored mutant set.


Activation-gate validation: full harness [44235070461](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235070461) passed 239 tests; 9/9 selected activation-gate mutants were killed by assertion-driven tests. Producer [44235147267](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235147267) succeeded and separate verifier [44235183026](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235183026) reported `VERIFIED` for the exact source commit. External activation remains NOT ACTIVE.


### Policy activation CLI

`policy_activation_gate.py` is also directly executable. It requires exact input files and explicit externally sourced authority/activation SHA-256 pins, policy identity/sequence, expected source commit, and trusted epoch time. It rejects symlink/non-regular inputs, oversized files, duplicate JSON keys, missing pins, and failed activation checks. No repository defaults are used. CLI tests cover successful pinned invocation, missing external pin, duplicate JSON keys, and symlink rejection.

The CLI is not activated in production. Pins and time passed by a caller are only as trustworthy as that caller; a production deployment must source them from separately administered protected controls and trusted time. The GitHub workflow runs tests only.


## Component provenance receipt authentication

Normative contract: [COMPONENT_PROVENANCE_RECEIPT_AUTHENTICATION.md](COMPONENT_PROVENANCE_RECEIPT_AUTHENTICATION.md).

Implementation: `component_provenance_authenticator.py`; adversarial tests: `test_component_provenance_authenticator.py`; selected mutation tests: `test_component_provenance_mutations.py`. Receipt schema 2.0 removes self-asserted `VERIFIED` status and binds the exact SLSA invocation ID to the receipt's run ID and attempt. The production activation CLI requires a separately supplied provenance-policy SHA-256 pin and authenticates each exact component subject before aggregation.

**Activation limitation:** the current evidence producer signs only `github-run-evidence.json`; it does not issue a distinct attestation for every component artifact. The new tests use fake CLI output and are not evidence of real component attestations. No production workflow invokes the gate, and the external provenance-policy pin is not yet provisioned. Therefore this integration remains a validated prototype, not an active trust authority or theorem-acceptance mechanism.


**Observed validation for commit `e8da7e8923440716a1b1dbf85c6f2c7b0408c9dc`:** full meta-verification harness [44238894962](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238894962) passed 263 tests in 28.235 seconds. The selected mutation suites killed 10/10 component-provenance mutants, 12/12 aggregator mutants, and 9/9 policy-activation mutants. Evidence producer [44238972702](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238972702) succeeded; separate verifier [44239010485](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44239010485) reported `VERIFIED` for the exact commit and one attestation (subject SHA-256 `bcf1a81a2aa0bf9d708c3fb78d427c1b2fc0b531a465a912933be3ea3309f73a`). This signed subject is the collector's `github-run-evidence.json`, not per-component evidence. The authenticator tests still use fake CLI output; no live component artifact has been authenticated.


## Live component-provenance integration smoke test

`.github/workflows/component-provenance-live-smoke.yml` runs after the signed evidence producer and downloads that exact producer run's subject artifact. `component_provenance_live_smoke.py` builds a one-component bundle for the downloaded `github-run-evidence.json`, binds the actual producer run ID/attempt and source revision, calls the direct GitHub/Sigstore authenticator, and requires the existing aggregator to accept the authenticated smoke bundle. The report is uploaded as a workflow artifact.

This is a real-signature integration test for one collector evidence subject, not a per-Paper/per-Lean component producer. The policy digest is computed from the repository checkout solely for this smoke test; it is not an external trust pin. External policy activation remains NOT ACTIVE, and the result is not mathematical verification. Adapter unit tests are in `test_component_provenance_live_smoke.py`.


### Observed live smoke result

On commit `7d5f778e9cd05cd1ef1095dd23f139d83aba8248`, the harness passed 267 tests (run [44240363793](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240363793)); selected component-provenance, aggregator, and activation mutants were killed 10/10, 12/12, and 9/9. Producer run [44240436570](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240436570) and separate provenance verifier run [44240468328](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240468328) succeeded. Crucially, live smoke run [44240468560](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240468560) verified the actual collector evidence artifact with the component authenticator and aggregator; it reported `LIVE_COMPONENT_PROVENANCE_SMOKE_VERIFIED`, one verified attestation, and aggregator `ACCEPTED`.

This validates one real GitHub/Sigstore subject path only. It does not produce or authenticate all Paper A/Lean/numerical evidence, does not activate external policy pins, and does not establish mathematical correctness.


## Paper A first 14-layer trial pipeline

The new Paper A producer workflow runs the pinned Lean build and four bounded diagnostics, generates a source-linked manifest for all 15 Paper A claim records, and emits a 14-row layer assessment plan. Each of the seven evidence JSON subjects is separately attested with GitHub/Sigstore. A distinct verifier workflow downloads the artifact from the exact producer run and authenticates every subject before fail-closed aggregation.

A component PASS means only that the named execution or manifest-generation task completed. It does not mean that the associated mathematical claim passed. The layer report preserves PARTIAL, BLOCKED, NOT_RUN, and NOT_ASSESSED states. Overall Paper A remains NOT_VERIFIED. The provenance-policy digest is currently computed from the same checkout, so this is bounded in-repository provenance verification, not external trust-root activation.


### First observed Paper A execution finding

The first producer attempt on source revision dc3273a0a2f75c8e32e47407b1e972edcc882a23 reached the pinned Lean action but failed while building ConstantLlapoy.PaperA.PerronFrobeniusCore. The log reports unsynthesized RCLike (RCLike Real) instances and unresolved goals around source lines 690–709. The action stopped the initial attempt before component evidence could be emitted. This is recorded as a real L-04 blocker, not normalized to PASS. The producer was then changed to preserve failed command transcripts as evidence and continue other independent checks; the final verifier will report authenticated evidence with failed checks rather than hide the failure.


## Observed first Paper A evidence run

- Producer workflow run: 44248949683 — SUCCESS, source commit 1173aba070abd89fcb5f62f14e7fd8494bdaa464.
- Separate component provenance verifier: 44249207601 — SUCCESS.
- Seven evidence subjects were emitted and each subject's GitHub/Sigstore attestation was cryptographically authenticated. The component report records true for all seven provenance-authentication flags.
- The aggregator returned REJECTED because PAPER_A_LEAN_BUILD is an authenticated FAIL. There were no missing or duplicate components, no stale fields, no evidence digest mismatches, and no unauthenticated provenance. The verified failure list contains exactly PAPER_A_LEAN_BUILD.
- The final verifier status is PAPER_A_EVIDENCE_BUNDLE_AUTHENTICATED_WITH_FAILED_CHECKS. This means the evidence bytes and origin were authenticated; it does not mean Paper A passed.
- Claim traceability completed for all 15 Paper A registry records and resolved frozen upstream source commit 8deb7de4a49cb2060720246b7101820ee7e08c91.
- Both exact symbolic diagnostics and both high-precision numerical diagnostics exited successfully. They remain finite-N / sampled diagnostics, not proofs.

### Observed 14-layer result

| Layer | Result |
|---|---|
| L-01 | PARTIAL |
| L-02 | BLOCKED |
| L-03 | PARTIAL |
| L-04 | FAILED |
| L-05 | NOT_RUN |
| L-06 | PARTIAL |
| L-07 | PARTIAL |
| L-08 | PARTIAL |
| L-09 | PARTIAL |
| L-10 | PARTIAL |
| L-11 | PARTIAL |
| L-12 | PARTIAL |
| L-13 | NOT_RUN |
| L-14 | NOT_ASSESSED |

The overall Paper A status remains NOT_VERIFIED. The Lean failure is in ConstantLlapoy.PaperA.PerronFrobeniusCore, with RCLike (RCLike Real) synthesis errors and unresolved goals around lines 690–709. No theorem was weakened or promoted to PASS.


### Latest Paper A run (2026-11-18)

Current exact source revision \`1aff68f49d95c2d186576362cd1d392ae474269b\`: 275 harness tests passed; Lean 4.36.0 build and axiom audit passed (79 declarations, configured allowlist only); the Paper A producer and separate provenance verifier succeeded, authenticating all seven required component subjects. The component bundle was ACCEPTED for artifact completeness/provenance only. The 14-layer plan remains partial/blocked/not-run as recorded in \`PAPER_A_FIRST_14_LAYER_TRIAL.md\`; Paper A itself remains \`NOT_VERIFIED\`.


### TFIM formalization increment

The Paper A Lean source now includes a kernel-checked computational-basis TFIM matrix and an explicit nonnegative shift \(K=cI-H\), with exact single-spin-flip positive support. At commit \`4f6efbe9a1140007d73250940ed7c0ee97411842\), Lean built 18,266 jobs and axiom-audit checked 103 declarations against the configured allowlist. The producer and separate provenance verifier succeeded. Hypercube connectivity, positive top-eigenvector existence, and spectral transfer remain open; Paper A remains NOT_VERIFIED.


## Paper A L-02 audit integrity checker

Added \`paper_a_semantic_audit_validator.py\` and adversarial tests. The checker recomputes Git blob identities for all 15 frozen claim records and all five Lean modules, enforces the exact claim registry set, checks listed declaration names exist in the pinned modules, recomputes classification counts, rejects duplicate JSON keys and unknown statuses, and prevents a structural check from promoting L-02 or claim verification.

Its only success status is \`STRUCTURALLY_VALID_NOT_SEMANTICALLY_VERIFIED\`. It does **not** establish that a Lean declaration is mathematically equivalent to a manuscript claim, that model hypotheses are discharged, or that the audit classifications are correct. L-02 remains BLOCKED pending independent mathematical review and model-specific formalization.


### Collector pin recovery — 2026-11-18

After adding the L-02 structural validator to the harness, the next evidence-collection run correctly failed closed because the collector policy still pinned the previous harness workflow blob. The policy is now updated to the exact current workflow blob and exact required step set. No failed run was treated as accepted evidence.
