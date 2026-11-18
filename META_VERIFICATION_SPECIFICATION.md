# Constant Llpoy — Meta-Verification Specification

**Document status:** Normative specification with policy evaluation, API evidence collection, and initial signed-provenance production/verification implementations; assurance remains partial
**Version:** 0.1.0
**Date:** 2026-11-18
**Scope:** Assurance of the tools, checkers, workflows, evidence pipelines, and decision logic that produce or communicate verification results
**Threat linkage:** T21; FM-14, FM-20 through FM-25
**Current architecture placement:** Cross-layer obligation provisionally assigned to L-08, L-10, L-11, and L-12. A dedicated layer decision is deferred pending the criteria in Section 12.
**Normative language:** MUST and MUST NOT are mandatory; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Purpose and assurance claim

Meta-verification evaluates whether the machinery used to verify mathematical claims is itself sufficiently specified, tested, traceable, and independently challenged. It covers certificate producers and checkers, parsers, validators, build and test orchestration, CI workflows, report generators, status aggregators, artifact stores, and the scripts that connect them.

The assurance claim is deliberately limited:

> For a named toolchain revision and a named verification run, the project has evidence that specified failure classes in the verification machinery were challenged by declared tests and independent review, that the evidence is bound to the exact inputs and revisions, and that the reported status follows the fail-closed rules in this specification.

This is **not** a claim that the verification machinery is bug-free, that its own consistency has been proved, or that unknown failure modes are impossible. Meta-verification reduces and exposes risk; it does not eliminate the need to state residual trust.

## 2. Scope and protected assets

Meta-verification MUST cover every component whose behavior can change:

- whether a mathematical obligation is executed;
- which source, theorem, assumptions, dependencies, or certificate are checked;
- whether a check is considered successful;
- whether evidence is retained and linked to the run; or
- how a result is summarized, promoted, or published.

At minimum, the inventory MUST consider:

1. certificate and proof producers;
2. certificate checkers and proof-kernel interfaces;
3. parsers, serializers, schema validators, and deserializers;
4. build scripts, test runners, workflow definitions, and job orchestration;
5. report generators, badge generators, and status aggregators;
6. revision, dependency, and provenance binding mechanisms;
7. artifact upload, download, storage, and retrieval mechanisms;
8. configuration, environment, and secret/permission boundaries where they affect execution;
9. scripts or agents that decide which obligations are required or skipped.

An unlisted component MUST NOT silently influence a verification conclusion. If discovered, it must be added to the inventory and the affected evidence re-evaluated.

## 3. Assurance model and separation of responsibilities

### 3.1 Roles

| Role | Responsibility | Independence requirement |
|---|---|---|
| Producer | Generates a proof, certificate, report input, or candidate result | Its output is untrusted until checked |
| Primary checker | Validates the candidate result under a declared contract | Must not rely on producer assertions as proof of validity |
| Checker challenge harness | Exercises checker behavior using valid, invalid, malformed, boundary, and adversarial inputs | Test cases and expected outcomes must be reviewable; harness must not simply reuse the checker implementation |
| Independent reviewer | Inspects checker contract, test design, trust boundary, and observed evidence | Must challenge assumptions and common dependencies, not merely approve a green run |
| Status authority | Applies the normative status rules to evidence | Must not convert missing, stale, skipped, failed, or inconclusive evidence into PASS |
| Maintainer | Versions tools, workflows, schemas, and inventories | Must disclose changes and trigger impact analysis |

One person or system MAY hold multiple roles for low-risk work, but the role combination and resulting loss of independence MUST be recorded. For critical checkers and release decisions, producer, checker implementation, and independent reviewer SHOULD be separated where feasible.

### 3.2 What checks the checker?

No infinite chain of checkers is required. Instead, assurance is decomposed into distinct evidence routes:

- **Contract review:** a reviewer inspects the checker's accepted language, preconditions, rejection behavior, and claimed guarantees.
- **Known-answer tests:** independently curated valid and invalid examples establish expected behavior.
- **Negative and malformed-input tests:** deliberately invalid encodings, truncated inputs, ambiguous encodings, unexpected fields, and boundary values must be rejected safely.
- **Mutation testing:** controlled defects are introduced into inputs, certificates, workflow configuration, revision metadata, or status evidence; the assurance process must detect them or the surviving blind spot must be documented.
- **Differential checking:** where feasible, a technically distinct checker or method evaluates the same object.
- **Source and dependency review:** the checker, parser, runtime, and transitive dependencies are inspected and inventoried.
- **External reproduction/review:** a reviewer who did not author the checker or its test harness follows the documented procedure and inspects the retained evidence.

These routes are not automatically independent. Their shared specifications, libraries, parsers, languages, build tools, people, infrastructure, and data sources MUST be recorded. A test harness that calls the same defective parser to construct both test input and expected output is not an independent challenge.

## 4. Required inventories and contracts

### 4.1 Verification-component inventory

Each in-scope component MUST have a stable component ID and record:

- name, purpose, owner, and repository path;
- component class (producer, checker, parser, runner, aggregator, storage, or other);
- exact source revision and release/version;
- direct and transitive dependencies, including versions or immutable references where available;
- input and output formats, schema versions, and validation rules;
- trust classification and TCB impact;
- the claims and workflows that depend on it;
- tests, independent challenge route, reviewer, and retained evidence;
- known limitations, unresolved defects, and residual risk;
- last reviewed revision and next review trigger.

Unknown or unpinned dependencies MUST be explicitly marked unknown; they MUST NOT be represented as verified or absent.

### 4.2 Checker contract

Every checker used as decisive evidence MUST specify:

1. the exact proposition or artifact property it checks;
2. accepted input grammar and schema, including version;
3. preconditions and assumptions;
4. the meaning of acceptance and rejection;
5. behavior for malformed, truncated, oversized, ambiguous, or unsupported inputs;
6. resource limits, timeouts, and partial-result behavior;
7. dependencies and trusted computing base;
8. whether the checker is sound, complete, both, or neither for the stated input class, with justification;
9. known excluded cases and failure modes;
10. the independent tests and review evidence supporting its use.

A checker MUST NOT claim completeness merely because it accepts all examples in a test suite. If it is only a validator for a restricted certificate class, that restriction MUST be explicit.

### 4.3 Output contract

Checker output MUST be machine-readable or otherwise unambiguous and distinguish at least:

- `ACCEPTED` — the checker accepted the exact input under its declared contract;
- `REJECTED` — the input failed the declared check;
- `ERROR` — execution or infrastructure failed;
- `TIMEOUT` — the time/resource limit prevented a conclusion;
- `INCONCLUSIVE` — the checker cannot decide the case;
- `NOT_RUN` — the check did not execute.

`ACCEPTED` is not synonymous with a mathematically verified manuscript claim. It is one evidence item whose scope is limited by the checker contract and the claim-to-artifact correspondence record.

## 5. Required challenge and test program

Every decisive checker and every status-affecting workflow MUST have a versioned challenge plan. The plan MUST define expected behavior before the test is run and preserve both passing and failing outcomes.

### 5.1 Test classes

| Test class | Minimum challenge | Required interpretation |
|---|---|---|
| Positive controls | Known-valid inputs, including representative boundary cases | Must be accepted only within the declared contract |
| Negative controls | Invalid proofs/certificates, false claims, invalid signatures or inconsistent metadata where applicable | Must be rejected; otherwise the checker is not fit for that use |
| Malformed-input tests | Truncation, invalid encoding, duplicate/conflicting fields, unknown schema version, oversized input | Must reject safely or return a non-accepting error state |
| Boundary tests | Empty/minimal/maximal structures, endpoints, zero-length cases, extreme permitted sizes | Must follow the contract exactly |
| Mutation tests | Deliberately alter a valid certificate, source revision, dependency lock, required-job list, result state, or report field | The relevant validation or status gate must detect the mutation |
| Fault-injection tests | Simulate missing job, failed job, timeout, unavailable artifact, stale commit, and partial upload | Must not produce a passing aggregate status |
| Regression tests | Preserve every previously discovered defect as a test | A recurrence must fail the assurance gate |
| Differential tests | Compare with a distinct checker or independent computation where feasible | Disagreement blocks acceptance pending investigation |

### 5.2 Mutation adequacy

Mutation testing MUST report which mutations were detected, which survived, which were not applicable, and why. A mutation score MUST NOT be used as a standalone proof of checker correctness. Surviving mutations require one of: a justified non-impact argument, an additional test, an alternate control, or an explicit residual-risk entry.

At minimum, mutation scenarios MUST include:

- changing the checked source revision while retaining an old successful result;
- deleting or skipping a required job;
- replacing a required successful result with timeout, error, or inconclusive;
- altering a certificate after it was checked;
- changing the schema or parser version without invalidating prior evidence;
- removing a required obligation from the execution plan;
- changing a dependency or toolchain revision without triggering revalidation;
- altering the report summary while leaving underlying evidence unchanged.

### 5.3 Test independence

Test inputs, expected outputs, mutation operators, and the test harness MUST be reviewed for common-mode dependencies with the checker under test. Where full independence is infeasible, the exact shared components and the resulting limitation MUST be disclosed.

## 6. Revision binding, provenance, and evidence integrity

Every decisive result MUST be bound to an immutable or otherwise verifiable identity for:

- repository and commit/source tree;
- claim ID and claim-specification revision;
- manuscript revision and formalization revision;
- checker and producer revisions;
- workflow/configuration revision;
- schema and certificate format versions;
- dependency lock/SBOM or equivalent environment record;
- exact input artifact digest and output/evidence digest;
- run identifier, execution time, and result state.

A result from a different commit, claim revision, checker version, schema, or required configuration MUST be treated as stale unless a documented compatibility rule establishes otherwise and is independently reviewed.

Mutable labels such as `latest`, branch names, or a green badge are not sufficient revision identity. Where cryptographic hashes or signed attestations are used, their algorithm, key ownership, verification procedure, and trust assumptions MUST be documented. A hash establishes identity/integrity relative to the hash value; it does not establish mathematical correctness.

Evidence MUST preserve enough raw output and metadata for a reviewer to reconstruct what ran and what was checked. A summary report alone is insufficient for decisive claims.

## 7. Fail-closed status aggregation

### 7.1 Invariants

The status aggregator MUST satisfy all of the following:

1. Every required obligation is enumerated before aggregation.
2. Every required obligation is matched to evidence for the exact claim and source revision.
3. Missing, skipped, stale, failed, errored, timed-out, or inconclusive required evidence cannot be mapped to PASS.
4. An optional check cannot silently replace a failed required check.
5. A job that did not run cannot be counted as successful.
6. A partial matrix cannot be presented as a complete matrix.
7. A report cannot claim a stronger status than its weakest required evidence permits.
8. Changes to the obligation set, checker, workflow, schema, or source invalidate affected prior results until impact analysis is completed.
9. Aggregation logic itself is versioned, tested, and included in the component inventory.
10. Manual overrides are prohibited for mathematical acceptance; administrative exceptions may annotate a report but cannot turn failed or missing evidence into verified status.

### 7.2 Minimum aggregation rule

For a claim with required obligations `O`, a passing aggregate is permitted only if every `o ∈ O` has current, revision-bound evidence whose result satisfies that obligation's acceptance condition, all required meta-verification gates are current, and no unresolved blocking discrepancy exists.

If any required result is `REJECTED`, `ERROR`, `TIMEOUT`, `INCONCLUSIVE`, `NOT_RUN`, missing, stale, or unbound, the aggregate MUST NOT be `Verified`. The report MUST preserve the more informative underlying state rather than collapsing all failures into a generic red/green result.

### 7.3 Aggregator tests

The aggregator MUST be tested against a truth table covering all combinations of required evidence states, including at least one case each for missing, skipped, stale, failed, timeout, inconclusive, contradictory, and partially uploaded evidence. Tests MUST assert that no such case produces `Verified`.

## 8. Independent evidence and review

### 8.1 Independence record

For each claimed independent route, record shared and distinct:

- mathematical specification and encoding;
- algorithms and proof libraries;
- parser, checker, compiler, runtime, and operating system;
- dependencies and package sources;
- test data and expected-result generation;
- people, review process, and incentives;
- CI provider, credentials, storage, and network infrastructure.

Independence is a graded, claim-specific property, not a binary label inferred from different tool names.

### 8.2 Minimum independent review

Before a checker or workflow is used as decisive evidence for a high-impact claim, a reviewer other than its author SHOULD:

- inspect its contract and TCB declaration;
- inspect positive, negative, malformed-input, and mutation tests;
- inspect at least one raw execution record;
- confirm source/configuration/evidence revision binding;
- challenge skipped/stale/timeout handling;
- inspect known limitations and surviving mutations;
- record approval, rejection, or unresolved concerns.

If no independent reviewer is available, the evidence MUST be marked as lacking independent review and MUST NOT be described as independently validated.

## 9. Assurance evidence package

Each meta-verification assessment MUST retain a package containing:

1. component inventory snapshot;
2. checker contracts and schema versions;
3. threat-to-control mapping for relevant T21/FM failure modes;
4. challenge plan and test vectors;
5. raw positive/negative/malformed/fault-injection results;
6. mutation inventory and surviving-mutant analysis;
7. differential-check results or documented infeasibility;
8. source, workflow, checker, dependency, and artifact revision identities;
9. independent-review record and dissent;
10. status-aggregation truth-table results;
11. unresolved defects, exclusions, and residual-risk statement;
12. final assessment decision with scope and date.

Every package item MUST be traceable to the exact assessment revision. Missing items must be marked missing, not silently omitted.

## 10. Acceptance gates and failure conditions

### 10.1 Design gate

Meta-verification design is **Specified** only when:

- all status-affecting components have an inventory schema and named ownership;
- decisive checkers have explicit contracts;
- challenge classes and minimum mutations are defined;
- revision-binding fields are specified;
- fail-closed aggregation invariants are normative;
- independent review and residual-risk requirements are explicit;
- claim-level applicability and evidence mapping are defined.

### 10.2 Operational gate

A component or workflow is **Validated** for a stated scope only when:

- the inventory is populated with exact revisions and dependencies;
- contract and TCB review is complete;
- positive, negative, malformed, boundary, and relevant mutation/fault-injection tests have executed;
- surviving mutations and exclusions have been reviewed;
- aggregation truth-table tests pass;
- evidence is revision-bound and reproducible by the stated procedure;
- independent review is recorded or the lack of it is explicitly reflected in status;
- no unresolved blocking defect remains.

Validation applies only to the tested component revision, configuration, input class, and scope. It MUST be re-evaluated after material changes.

### 10.3 Immediate failure conditions

Meta-verification MUST be marked **Failed** or **Inconclusive**, as appropriate, if:

- invalid or malformed decisive evidence is accepted contrary to contract;
- stale or skipped required evidence can yield a passing aggregate;
- source/checker/workflow identity cannot be established;
- the checker contract materially overstates its guarantee;
- a required challenge test is missing or cannot be executed and no justified alternative exists;
- a known blocking defect is suppressed or omitted;
- the independent route is falsely represented as independent.

## 11. Change control and invalidation

Reassessment is mandatory after changes to checker source, parser, schema, certificate format, proof kernel interface, producer, dependency, runtime, build configuration, workflow, status logic, obligation inventory, artifact storage, or provenance mechanism.

Change impact MUST identify affected claims and evidence. Unaffected evidence may be retained only with a documented rationale. Re-running a workflow does not automatically repair a semantic or specification defect.

Every discovered checker or workflow defect MUST become a regression case where feasible. Prior reports affected by the defect MUST be identified and corrected or annotated; silent historical rewriting is prohibited.

## 11A. Independent trusted-builder contract

The external trusted-builder interface and mandatory security properties are specified in `meta_verification/TRUSTED_BUILDER_CONTRACT.md`; the report structure is specified in `meta_verification/trusted_builder_report.schema.json`. These are contracts, not evidence that an external builder exists or is active. A local reusable workflow is deliberately not substituted because it would remain within the relying-party repository's administrative trust boundary. Activation requires a real external repository identity, a trust-root-signed immutable workflow commit, caller delegation pinned to that commit, conformance evidence, and separate attestation verification.

## 12. Architecture placement: cross-layer obligation or dedicated layer?

**No L-15 decision is made by this document.** The current allocation remains provisional:

| Existing layer | Meta-verification responsibility |
|---|---|
| L-08 | Checker contracts, producer/checker separation, certificate negative tests, checker acceptance semantics |
| L-10 | Exact revision binding, claim-to-evidence traceability, stale artifact detection, report synchronization |
| L-11 | TCB/component inventory, dependencies, provenance, trust-boundary and common-mode analysis |
| L-12 | Independent review, reproducibility, mutation/fault testing governance, failure preservation, honest status reporting |

A dedicated layer SHOULD be proposed only if a documented architecture review establishes all of the following:

1. Meta-verification has a coherent lifecycle and acceptance gate not adequately represented by the existing layer interfaces.
2. It has distinct required inputs, outputs, evidence artifacts, and accountable ownership.
3. Its obligations are genuinely cross-cutting and cannot be assigned to L-08/L-10/L-11/L-12 without ambiguity, duplication, or an unowned gap.
4. It requires a distinct independent assurance route or decision authority.
5. A failure-mode and obligation-matrix migration demonstrates improved coverage without weakening existing requirements.
6. The proposed layer does not merely rename existing responsibilities or create a false impression of an infinite self-certifying hierarchy.

If these criteria are not met, retain meta-verification as a normative cross-layer obligation with explicit ownership and claim-level evidence. The number of layers is not a target.

## 13. Mapping to existing governance documents

| Source | Required integration |
|---|---|
| `THREAT_MODEL.md` | T21 remains the threat statement; this document operationalizes its controls |
| `14_LAYER_FAILURE_MODE_COVERAGE_MATRIX.md` | FM-14/FM-20–FM-25 and G-01 map to the challenge, binding, and aggregation requirements here |
| `VERIFICATION_OBLIGATION_MATRIX.md` | Section K maps each applicable claim to component inventory, checker tests, revision binding, aggregation, review, and residual risk |
| `TRUST_BOUNDARY_TCB_INVENTORY.md` | Every status-affecting component is classified and its TCB relationship recorded |
| `TOOLCHAIN_DEPENDENCY_INVENTORY.md` | Exact versions, immutable references, dependency graph, and provenance feed the assurance package |
| `14_LAYER_VERIFICATION_STANDARD.md` | L-08/L-10/L-11/L-12 retain the allocated responsibilities unless architecture review changes them |
| `LAYER_CATALOG.md` | Catalog points to this specification and the current component register without implying implementation or validation |
| `META_VERIFICATION_COMPONENT_REGISTER.md` | Evidence-based snapshot of observed repository components, external boundaries, exact revisions, and current assurance gaps |
| `meta_verification/README.md` and `meta_verification/status_evaluator.py` | Initial evaluator contract, invocation, fail-closed behavior, and explicit limitations |

## 14. Current status and limitations

- **Specified:** This document defines the meta-verification design requirements.
- **Component inventory:** An initial partial snapshot is recorded in `META_VERIFICATION_COMPONENT_REGISTER.md`; it identifies one Lean CI workflow, pinned action references, Lean/Lake configuration, locked dependencies, exploratory diagnostics, and external GitHub runner/status boundaries.
- **Implemented (initial, limited):** `meta_verification/status_evaluator.py` implements strict-schema fail-closed evidence policy; `meta_verification/test_status_evaluator.py` provides adversarial tests; `.github/workflows/meta-verification.yml` runs them. This is not a proof or certificate-semantics checker.
- **Implemented (API evidence collection):** `meta_verification/github_run_collector.py` queries GitHub REST API over HTTPS with a read-only token and checks run identity, event, branch, source SHA, workflow/evaluator blob revisions, required jobs, and required steps. `meta_verification/github_run_policy.json` pins the expected workflow and evaluator revisions.
- **Implemented (signed provenance producer):** `.github/workflows/meta-verification-evidence.yml` uses the commit-pinned `actions/attest` action to create a Sigstore-signed SLSA provenance attestation over the exact normalized evidence JSON bytes. The workflow has only the OIDC, attestations, and artifact-metadata permissions required for signing.
- **Implemented (separate provenance verifier):** `.github/workflows/meta-verification-provenance-verify.yml` runs after the producer, checks out the producer run's exact source commit, downloads that run's artifact, and invokes `gh attestation verify` with exact repository, signer workflow, OIDC issuer, predicate type, source ref, source commit, and hosted-runner constraints. `meta_verification/verify_signed_provenance.py` additionally checks the certificate repository ID, source ref, source and signer commit digests, verified timestamp evidence, and SHA-256 of the exact subject bytes. The policy is in `meta_verification/signed_provenance_policy.json`.
- **Tests implemented:** `meta_verification/test_signed_provenance.py` adds 18 adversarial policy tests, including exact GitHub CLI version parsing. The original evaluator, collector, and signed-provenance suite contains 52 tests; the external trust-root suite adds 27 adversarial tests, for 79 total. Actual signature and certificate-chain verification is delegated to GitHub CLI in the separate workflow; unit fixtures do not simulate cryptographic verification.
- **Validated (bounded end-to-end):** Harness run `44209941107` passed all 52 tests on commit `51d341c354a09ecfdeb11f6b687e9105e7d61408`; the inspected log records `Ran 52 tests` and `OK`. Producer run `44209966698` queried GitHub API and reported `ACCEPTED` for that exact harness run and source SHA, generated the SLSA/Sigstore attestation, and uploaded subject artifact `14386160694` (ZIP digest `sha256:2d37a3b5f0aea16e4fb7c415dbc143cd3d9fa903db369cb5344241f4527b3061`). Separate verifier run `44210006677` completed successfully and reported `VERIFIED`, repository ID `1460417275`, producer source commit `669532f0d93fd1087a18ea00a0cba10bf030fd14`, one verified attestation, and subject SHA-256 `2b27a3ef80a59946de3d3ea4fe81ced9fb5cc6cdd85c5d77623d3a24041aa591`. Verification report artifact `14384409245` was uploaded (ZIP digest `sha256:8dbc5a5a695bd014c8add4a8cf89b5f9f3999ed70a3e9f9bb6cfece2f208f2ea`). The verifier checked exact repository ID, signer workflow, OIDC issuer, source branch and commit, signer commit, SLSA predicate, timestamp evidence, hosted-runner policy, exact evidence-file bytes, and GitHub CLI version `2.103.3`.
- **Negative behavior:** Cancelled, incomplete, or failed upstream runs are not promoted to `ACCEPTED`; the collector emits `REJECTED` or `ERROR` as appropriate. Failed historical runs are not counted as successful provenance evidence.
- **External trust-root verifier validation:** Harness run `44211770333` passed 79 tests on commit `a9b582a4a24761af14ed7e64292746c7cb600245`; the inspected log records `Ran 79 tests` and `OK`. Collector run `44211799128` accepted that exact harness run and produced signed evidence artifact `14385663249`. Separate verifier run `44211832036` reported `VERIFIED` for one attestation and uploaded report artifact `14386925435`. The Ed25519 integration test generated a test keypair, signed a manifest, checked the signature against the public key, and verified exact Git checkout identity. This validates verifier code and fixtures, not an independently provisioned production trust root.
- **Implemented (external trust-root bootstrap, activation pending):** `meta_verification/external_trust_root.py` verifies an Ed25519-signed manifest from a separate repository, exact manifest/public-key SHA-256 pins, immutable checkout commit and clean tree, GitHub API repository IDs, strict duplicate-key-free schema, signer and builder identities, and validity interval. `.github/workflows/meta-trust-root-bootstrap.yml` runs this check only through the protected `meta-trust-root` Environment. Its 27 adversarial tests include a real generated Ed25519 signature verification, RSA-key rejection, path-traversal rejection, and tampered-digest rejection. This is a verifier and activation mechanism, not evidence that an external root is already provisioned.
- **Not active / not implemented:** no external trust-root package, private signing key, or trusted-builder identity was supplied or provisioned in this work, and protected Environment/reviewer configuration has not been verified. The GitHub API returned no repository rulesets; branch-protection details were not accessible to the connected integration. The current producer still signs within the relying-party repository; the trusted-builder identity in the external manifest is only a contract and is not yet used. Independent certificate-semantics checker beyond GitHub CLI verification, mutation runner against Lean checker, and theorem-status aggregation also remain absent.
- **Claim-level application:** Not yet populated by this document.
- **Independent review:** Not yet evidenced by this document.
- **Residual risk:** The checker, its test harness, the operating environment, reviewers, and evidence infrastructure may still share defects or assumptions. Assurance is bounded by declared contracts, tested failure classes, and the trust boundary.

Design completion is not operational completion. No checker, workflow, paper, theorem, or repository-wide verification result is certified by the existence of this specification.

## 15. Governing principle

> A verification result is only as trustworthy as the exact evidence path that produced and interpreted it. That path must itself be inventoried, challenged, revision-bound, independently reviewed where claimed, and reported within its demonstrated limits.


## Trusted-builder contract regression evidence

The trusted-builder contract and report schema are covered by 10 structural regression tests. The combined meta-verification harness run `44212792319` passed all 89 tests on commit `ea217ddce37f76f02a29e96eb34839ddf06d1164`. Collector run `44212816996` accepted that exact run and produced signed subject artifact `14386168406`; separate verifier run `44212845744` reported `VERIFIED` for one attestation and uploaded report artifact `14387166418`. This confirms the contract artifacts' structural invariants and required policy statements only; it does not validate an external builder implementation, establish independent governance, or activate external signing.


## 16. Local trusted-builder reference implementation (non-trusted)

A contract-validation reference has been implemented in `meta_verification/trusted_builder_reference.py`, with adversarial tests in `meta_verification/test_trusted_builder_reference.py`. It checks subject path confinement and symlink rejection, regular-file and size constraints, strict UTF-8 JSON and duplicate-key rejection, exact subject SHA-256, normalized collector evidence schema and canonical digest, caller repository/workflow/ref fields, and upstream run identity/completion/success/source binding.

**Assurance boundary:** caller and upstream metadata are supplied to the local function by its harness and are not independently authenticated. The implementation does not invoke OIDC, construct a provenance predicate, sign, attest, verify a signature, or establish an independent trust domain. It emits only `VALIDATED_LOCAL_UNTRUSTED` and explicit false values for signing, attestation, and trust. It is not the external trusted builder specified by the contract and cannot satisfy L-11 independent-governance obligations.

The reference was subsequently hardened against symlink races by opening each path component relative to a directory descriptor with `O_NOFOLLOW`, requiring intermediate directories, checking the final descriptor with `fstat`, and reading no more than the configured byte limit. FIFO subjects and non-standard JSON constants are rejected. The full harness passed 117 tests on commit `d8494c4f13aecf133ae156510e72ec689ee16fef` (run [44217266945](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217266945)). Evidence producer run [44217302386](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217302386) accepted that exact harness run; separate verifier run [44217348019](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217348019) reported `VERIFIED` for one attestation and the exact subject digest.


## 17. Black-box trusted-builder conformance suite (local reference scope)

`meta_verification/test_trusted_builder_conformance.py` is a black-box CLI conformance suite. It deliberately does not import the reference implementation. It independently constructs a known-answer normalized evidence record, invokes the documented CLI in a separate process, parses its machine-readable output, and checks the output file and exit status.

The suite currently covers a positive local-validation case and negative vectors for subject digest substitution, caller identity/workflow/ref mismatch, failed or incomplete upstream runs, replayed run IDs, source revision mismatch, absolute/traversal paths, subject and parent-directory symlinks, duplicate JSON keys, malformed UTF-8, non-standard JSON constants, unknown evidence fields, stale record digests, rejected evidence, and size limits. It also asserts that successful output remains `VALIDATED_LOCAL_UNTRUSTED`, with signing, attestation, and trust flags all false.

**Observed result:** commit `7eae9f587f8426407b54abc58d9c1e78e374827c` passed 137 tests in harness run [44220321270](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220321270). The separate provenance verifier run [44220332663](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220332663) independently reported `VERIFIED` for the evidence artifact from producer run `44220303616`, whose exact signer source was commit `d1d7db78e2c3bc32a3fbace9b10f41a5ac860148`. This provenance validates the evidence artifact and signer identity for that earlier commit; it must not be misrepresented as signing the later `7eae9f` harness evidence.

The suite is independent of the implementation at the Python import/oracle level, but it remains in the same repository, shares the same CI platform and maintainer trust boundary, and tests only the local non-signing reference CLI. It is **not** independent governance, does not validate an external builder, does not test OIDC/Sigstore signing, and does not satisfy the external builder activation gate. A future external builder must pass a reviewer-controlled adaptation of these vectors and produce a real attestation that a separate verifier validates.


## 18. Mutation adequacy testing for trusted-builder conformance

`meta_verification/test_trusted_builder_mutations.py` performs controlled mutation testing against the black-box CLI conformance suite. For each mutant, it creates an isolated temporary copy of the implementation and conformance tests, applies exactly one targeted weakening, syntax-checks the mutated implementation, then executes the black-box suite against that mutant. A mutant counts as killed only when the suite runs and fails through a test failure; syntax/import failures do not count.

The current mutation set contains seven security-relevant mutants:
1. bypass subject-byte SHA-256 comparison;
2. bypass canonical evidence-record digest comparison;
3. accept a non-`ACCEPTED` upstream evidence record;
4. bypass caller repository-ID matching;
5. bypass upstream run-ID matching (replay defense);
6. bypass path-traversal rejection; and
7. escalate the local report status to `SIGNED`.

**Observed result:** all seven selected mutants were killed (7/7, 100% for this explicit mutation set) by the conformance suite. The full GitHub Actions harness passed 138 tests on commit `ad73206847bc15ca4d3d0b1db68f74ad1b3d6901` in run [44229439161](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229439161). The job log explicitly records all seven mutant names as killed.

This score is limited to the seven authored mutants. It is not a general mutation-adequacy guarantee, does not establish complete security coverage, and does not turn the local reference into an independently trusted builder. Future work should expand the mutant catalogue based on the threat model, including malformed identity types, missing/extra metadata, report-field tampering, filesystem race attempts, and producer/verifier policy mutations where safely testable.


## 19. Adversarial input-space expansion and safe report output

The local reference CLI's adversarial suite now covers JSON/type and metadata boundary cases beyond the original threat vectors:

- Boolean-vs-integer confusion for caller repository IDs and upstream run IDs.
- Missing and unexpected keys in caller and upstream identity objects; these objects now require exact key sets rather than silently ignoring extension fields.
- Duplicate top-level request keys and non-standard JSON constants in the CLI request file.
- Report output final-component symlink, parent-directory symlink, and pre-existing-file attacks.

The CLI now creates report files using directory file descriptors, no-follow opens for every parent component, and exclusive creation of a new final file. It refuses platforms lacking the required no-follow flags and does not overwrite an existing report. This is a fail-closed local-reference hardening measure; it does not authenticate request metadata or establish builder trust.

The provenance policy validator now rejects boolean values for `repository_id` instead of accepting Python's boolean-as-integer subtype behavior.

**Observed result:** commit `32befb3a3bda45705794e4484f94abe8cbb9b677` passed the full harness: 150 tests in run [44229925358](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229925358). The same run's logs also explicitly show all seven previously selected mutation cases killed. The mutation score remains bounded to those seven authored mutants.


## 20. Signed-provenance verifier mutation adequacy

`meta_verification/test_provenance_mutations.py` adds controlled mutation testing for the separate signed-provenance verifier. It creates isolated copies of `verify_signed_provenance.py` and `test_signed_provenance.py`, applies one targeted weakening, syntax-checks the mutant, and requires the unit suite to execute and fail through an assertion. Import/syntax failures do not count as kills.

Ten verifier mutants are currently tested:
1. certificate repository-ID binding bypass;
2. certificate source-ref binding bypass;
3. certificate source-commit binding bypass;
4. signer-workflow commit binding bypass;
5. verified timestamp requirement bypass;
6. SLSA predicate-type binding bypass;
7. exact subject-byte digest matching bypass;
8. ambiguous duplicate matching subject acceptance;
9. boolean repository-ID policy acceptance; and
10. pinned GitHub CLI version comparison bypass.

**Observed result:** all 10/10 selected verifier mutants were killed. Full harness run [44230310401](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230310401) passed 151 tests on commit `8740ee0c024d4c30105d766d54679f563ee211cc`. The job log records all ten `PROVENANCE MUTANT KILLED` lines and the run concluded success.

An initial run exposed a test-fixture masking issue: the boolean repository-ID mutant was not detected because the fixture's certificate ID did not match the mutated policy value. The fixture was corrected to align those values so the test isolates the exact type guard. The corrected run killed the mutant. This demonstrates why mutation testing is useful for detecting weaknesses in tests as well as in the implementation.

The 10/10 score applies only to these ten authored mutations. It is not an exhaustive proof of verifier correctness, and the unit suite does not replace actual GitHub CLI/Sigstore verification against live attestations.


## 21. GitHub Actions run collector mutation adequacy

The collector is tested with isolated, single-change mutants against `test_github_run_collector.py`. A mutant counts as killed only when the suite executes and fails through an assertion; syntax/import failures do not count.

### Collector hardening performed

- Require exact integer types (not Python booleans) for policy workflow ID, expected run ID, API run ID, and API workflow ID.
- Require a present, positive exact-integer workflow `run_attempt`.
- Bind the API repository and head-repository numeric IDs to each other, in addition to requiring both repository names to match the expected repository.
- Require positive exact-integer job IDs and reject duplicate job IDs.
- Require exact-integer `total_count` and equality with the returned job count; a partial first page is rejected rather than silently accepted.
- Preserve exact workflow-file and evaluator-file blob SHA pinning.

### Mutation evidence

Thirteen selected mutants were tested:
1. Boolean workflow ID accepted in policy.
2. Boolean expected run ID accepted.
3. Boolean API run ID accepted.
4. Boolean API workflow ID accepted.
5. Missing/invalid run-attempt validation bypassed.
6. Numeric repository identity comparison bypassed.
7. Primary repository-name binding bypassed.
8. Head-repository-name binding bypassed.
9. Job pagination/completeness check bypassed.
10. Job ID type/range check bypassed.
11. Duplicate job ID check bypassed.
12. Workflow file blob pin bypassed.
13. Evaluator file blob pin bypassed.

**Observed result:** 13/13 selected collector mutants were killed. GitHub Actions run [44230994871](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230994871) passed 164 tests on commit `8d23997fd0d746ba04f2528a5e34721293ae5514`.

The first runs correctly failed: they exposed missing job-ID validation and three mutation fixtures that were masked by adjacent identity checks. The collector guard and fixtures were corrected; the successful run confirms each mutant was independently detected. The mutation score is limited to these thirteen authored changes. It is not exhaustive assurance, and the collector still relies on the GitHub API response and the repository's configured policy/trust boundary.


## 22. GitHub API response contract and replay binding

The collector now binds evidence to the exact upstream workflow run attempt supplied by the GitHub `workflow_run` event, not merely to the run ID and head commit.

### Exact run and job attempt binding

- The producer passes `github.event.workflow_run.run_attempt` to the collector as `UPSTREAM_RUN_ATTEMPT`.
- The collector requires a positive exact-integer expected attempt and requires the API run's `run_attempt` to equal it.
- Every returned job must carry the exact expected `run_id` and `run_attempt`, each as exact positive integers.
- This prevents a previous or later rerun attempt's jobs from being mixed into the evidence for the triggering attempt.
- The normalized evidence retains the validated `run_attempt`.

### API response parsing and boundedness

- API JSON must decode as a UTF-8 JSON object.
- Duplicate object keys, non-standard JSON constants, non-object top-level values, invalid UTF-8, and responses larger than 10 MiB are rejected.
- HTTP errors, network errors, and timeouts fail closed.
- The jobs endpoint is requested with `per_page=100`. The collector deliberately rejects any response whose `total_count` differs from the number of returned jobs or exceeds 100; it does not silently accept a first page as a complete result or attempt unbounded pagination.
- The job list must be bound to the exact run and attempt, have positive unique job IDs, and match the exact policy job set.

### Adversarial and mutation evidence

New tests cover stale/replayed run attempts, expected attempt type/range, job-to-run and job-to-attempt binding, oversized job pages, duplicate JSON keys, non-standard JSON constants, invalid UTF-8, non-object responses, a 10 MiB response bound, HTTP 503, and timeout behavior.

The collector mutation suite now contains 17 selected mutants, adding run-attempt equality, job run ID, job attempt, and duplicate-key rejection bypasses. GitHub Actions run [44231737913](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44231737913) passed 176 tests on commit `295eea3e0e717569c3f981a3e272dc31b4de567d`; the log explicitly records all 17 collector mutants killed.

This is bounded API-contract and replay-resistance testing. It does not authenticate GitHub's API independently, prove the API is truthful, or protect against a privileged repository administrator who can change the producer and policy. Pagination is fail-closed at 100 jobs rather than fully traversed; a future policy needing more than 100 jobs requires an explicit cursor/next-page contract and tests before enabling it.


## 23. Component provenance authentication and status aggregation

### 23.1 Authority boundary

`meta_verification/status_aggregator.py` validates component completeness, evidence bytes/digests, policy/source binding, and the shape of provenance receipts. Structural consistency is not cryptographic authentication. A JSON field claiming `VERIFIED` MUST NOT authorize acceptance.

The standalone `status_aggregator.py` CLI supplies no authenticated-receipt map and therefore MUST return `INCONCLUSIVE` for otherwise complete but unauthenticated bundles. Its internal `aggregate()` API accepts an in-memory authentication map only from the direct component authenticator. Because arbitrary Python code can fabricate Python objects, the function API is not itself a process or security boundary. The supported production path is the `policy_activation_gate.py` CLI, which creates the map internally after direct verification.

### 23.2 Component receipt schema 2.0

Each component provenance object MUST have exactly:
- `receipt_schema_version = "2.0"`;
- `subject_sha256`, equal to the SHA-256 of the exact decoded evidence bytes;
- `source_commit`, equal to the expected source commit;
- positive exact-integer `attestation_run_id`;
- positive exact-integer `attestation_run_attempt`; and
- immutable 40-character `attestation_workflow_revision`, equal to the expected source/workflow revision.

Legacy self-asserted fields such as `status: VERIFIED`, `verifier_run_id`, and `verifier_revision` are rejected by the exact schema. The run ID and attempt MUST be bound to the signed SLSA v1 `predicate.runDetails.metadata.invocationId`, using the GitHub Actions invocation URI:

`https://github.com/OWNER/REPOSITORY/actions/runs/RUN_ID/attempts/RUN_ATTEMPT`.

### 23.3 Direct attestation authentication

`component_provenance_authenticator.py` MUST:
1. validate the exact aggregation policy and complete, unique required component set;
2. verify the exact provenance-policy bytes against a separately supplied SHA-256 pin and ensure the parsed object equals those bytes;
3. decode each component's exact evidence bytes and recompute its SHA-256;
4. require receipt schema, source commit, workflow revision, run ID, and attempt to match;
5. invoke the pinned-version GitHub CLI `gh attestation verify` on each exact evidence subject with explicit repository, signer-workflow, OIDC issuer, predicate, source-ref, source-digest, signer-digest, and self-hosted-runner denial constraints;
6. verify repository numeric identity, source ref, source commit, signer commit, verified timestamps, predicate type, unique subject digest, and exact invocation ID; and
7. return an in-memory authenticated record for each required component.

The verifier MUST NOT accept caller-supplied verification reports or a `VERIFIED` string as a substitute for direct attestation verification. A missing attestation, failed verification, wrong signer, wrong source, wrong subject, wrong invocation ID, stale attempt, or missing/mismatched external provenance-policy pin MUST fail closed.

### 23.4 Aggregation and status

The production activation CLI MUST require all of:
- external authority-set SHA-256 pin;
- external active-policy-record SHA-256 pin;
- external provenance-policy SHA-256 pin;
- expected source commit, policy ID and sequence; and
- trusted epoch time.

It MUST authenticate every required component before calling the existing aggregator. The success status is `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`. This means only that the active-policy gate passed and component evidence subjects have authenticated provenance under the supplied signer policy. It does NOT mean the component evidence is mathematically correct, complete, relevant, or a proof of the theorem.

### 23.5 Tests and limitations

The authenticator tests use controlled fake GitHub CLI output. They test policy and receipt binding, not live cryptographic signatures. The mutation suite challenges selected pin, digest, identity, run-attempt, invocation-ID, and aggregation-authentication checks; its score is bounded to the authored mutant set.

No current component-evidence producer workflow emits an attestation for every component artifact, and no real component bundle has been authenticated end to end. The existing evidence producer attests `github-run-evidence.json`; that does not attest arbitrary component subjects. External provenance-policy pins, external authority pins, protected controls, and trusted-time injection remain unprovisioned. GitHub CLI is version-pinned but its binary/runtime remains runner-provided. Repository administrators able to alter workflows and policies remain in the trust boundary.

This subsystem is infrastructure provenance assurance, not a mathematical proof checker or theorem-status authority.

## 24. Policy authority and change control

Normative contract: [POLICY_AUTHORITY_AND_CHANGE_CONTROL.md](meta_verification/POLICY_AUTHORITY_AND_CHANGE_CONTROL.md).

Implementation: meta_verification/policy_change_control.py. Tests: test_policy_change_control.py. Mutation suite: test_policy_change_mutations.py.

The verifier checks a supplied external authority-set digest, 2-of-3 (default authority policy) distinct Ed25519 signatures, exact policy bytes digest, parent policy digest, next sequence, and validity interval. It emits POLICY_CHANGE_AUTHORIZED only; activation requires external pin publication and protected controls. The authority-set digest remains an externally supplied trust input, and OpenSSL is part of the runtime trust boundary. No external authority, reviewer identity, protected Environment, or production workflow integration is established. The prototype is not a theorem acceptance authority.


## Policy activation gate and end-to-end integration

The existing `status_aggregator.py` remains the structural component-bundle evaluator; it is not duplicated or promoted to an authenticated theorem-status authority. `policy_change_control.py` verifies proposal authorization, but `POLICY_CHANGE_AUTHORIZED` is not activation.

The new `policy_activation_gate.py` adds a separate activation check before invoking the structural aggregator. It requires (i) an externally supplied SHA-256 pin for the authority set and (ii) a separately externally supplied SHA-256 pin for a threshold-signed active-policy record. The record binds exact policy bytes, policy ID, sequence, authority-set digest, ACTIVE state, validity interval, and distinct Ed25519 signatures. Missing pins, stale sequence, mismatched digests, invalid signatures, or expired records fail closed.

The final integration status is `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`. The CLI now requires an externally pinned provenance policy and directly verifies each required component's exact evidence bytes with GitHub/Sigstore before invoking the existing aggregator. The standalone aggregator CLI cannot accept unauthenticated JSON receipts. This status still does not prove the component evidence is mathematically correct or constitute theorem acceptance.

The implementation is a prototype only. No external authority repository, independent reviewer key custody, protected Environment/pins, or production workflow invocation has been provisioned or verified. Rollback resistance depends on the external pin source advancing the expected sequence and activation-record digest; if the relying repository can control both expected pins and supplied bytes, the trust boundary collapses. See `meta_verification/POLICY_ACTIVATION_GATE.md` for the contract and limitations.


The activation-gate implementation also has a selected mutation suite (`test_policy_activation_mutations.py`) covering nine deliberate bypasses of the authority pin, active-record pin, ACTIVE state, sequence, policy digest, exact parsed-policy binding, expiry, signature threshold, and Ed25519 verification. A mutation score is limited to this selected set and does not establish exhaustive robustness.


Observed bounded validation for the activation-gate revision `b09293fc018144d43829c3a1b6b2dbbed93beef8`: full harness [44235070461](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235070461) passed 239 tests; the nine selected activation-gate mutants were all killed; evidence producer [44235147267](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235147267) succeeded; separate provenance verifier [44235183026](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235183026) reported VERIFIED for that exact commit. This is bounded CI evidence and does not activate an external policy authority.


The policy activation component includes a CLI contract requiring explicit policy/authority/activation/bundle files, externally sourced authority and active-record digests, expected policy ID and sequence, expected source commit, and trusted epoch time. The CLI rejects symlink/non-regular inputs, oversized inputs, duplicate JSON keys, and missing/malformed pins. It has no repository-local pin defaults. CLI test coverage is included in the meta-verification harness. Production invocation remains NOT ACTIVE because external pin custody, trusted time injection, and protected deployment controls have not been provisioned or verified.
