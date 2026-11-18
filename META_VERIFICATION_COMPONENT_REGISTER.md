# Constant Llpoy — Meta-Verification Component Register

**Document status:** Initial evidence-based inventory; partial coverage, not an operational validation
**Version:** 0.1.0
**Snapshot date:** 2026-11-18
**Repository:** `mytheeramet3dev-x/Constant-Llpoy`
**Observed repository tree SHA:** `70268efc1ea2eca4fbff0aaaf7bb7e9364d3f88a`
**Normative requirements:** `META_VERIFICATION_SPECIFICATION.md`
**Scope:** Components visible in the tracked repository tree and the directly observed CI evidence path

---

## 1. Purpose and evidence rules

This register identifies the concrete components currently visible in the repository that can affect formal verification, its execution, or the reporting of its result. It distinguishes repository-owned files from external services and distinguishes decisive checkers from exploratory diagnostics.

**Evidence labels:**
- **Observed:** directly inspected in the tracked tree or fetched file content.
- **Documented:** stated in a repository document but not independently re-executed in this assessment.
- **Not observed:** not present in the inspected tracked-tree snapshot; this is not proof that no external or untracked component exists.
- **Unknown:** exact implementation/version/behavior is not established.

Blob SHAs identify the inspected file contents. The tree SHA identifies the repository snapshot used for this initial inventory. A file SHA is not a proof of correctness.

## 2. Inventory summary

| Component ID | Component | Current classification | Assurance role | Initial status |
|---|---|---|---|---|
| MVC-001 | GitHub Actions workflow | Repository-owned orchestration | Runs Lean build and configured axiom audit | Observed; Lean workflow remains separate from meta-verification challenge workflow |
| MVC-002 | `actions/checkout` action | External action dependency | Retrieves source at workflow revision | Pinned by commit SHA; behavior not independently audited here |
| MVC-003 | `leanprover/lean-action` | External action / build orchestration | Invokes Lean/Lake build and axiom audit | Pinned by commit SHA; contract not independently audited here |
| MVC-004 | Lean toolchain | Compiler, elaborator, kernel runtime | Type-checks Lean declarations | Version pinned in repository; runtime not executed in this assessment |
| MVC-005 | Lake project configuration | Build configuration | Declares package, library, and Mathlib dependency | Observed; configuration not mutation-tested |
| MVC-006 | Lake dependency manifest | Dependency lock/provenance input | Pins Mathlib and transitive package revisions | Observed; provenance and supply chain not independently verified here |
| MVC-007 | Lean proof modules | Candidate proof inputs | Mathematical declarations submitted to Lean | Observed; not themselves independent checkers |
| MVC-008 | GitHub Actions run/job status | External status and execution evidence | Reports job state and steps | One historical successful run inspected; current snapshot has no status entries returned |
| MVC-009 | Python/SymPy/MPmath diagnostic scripts | Exploratory computational tools | Numerical/exact finite diagnostics; not decisive proof checkers | Observed; explicitly documented as diagnostic evidence |
| MVC-010 | GitHub-hosted runner (`ubuntu-latest`) | External execution environment | Hosts workflow steps | Observed as moving runner label; exact image/build not pinned in workflow |
| MVC-011 | GitHub artifact/log storage and status API | External evidence infrastructure | Retains/exposes run evidence | Service dependency inferred from workflow/status use; exact retention/attestation policy not inventoried |
| MVC-012 | Meta-verification test harness / mutation runner | Checker-challenge infrastructure | Exercises evidence-policy logic and selected adversarial cases | Policy evaluator plus 21 policy tests and 13 GitHub-run collector tests implemented; no mutation runner against the Lean checker |
| MVC-013 | Dedicated certificate parser/checker | Certificate validation | Would validate certificate evidence independently | Not observed in tracked tree snapshot |
| MVC-014 | Repository-owned report generator/status aggregator | Evidence aggregation | Would convert required evidence into claim status | A limited fail-closed evidence-policy evaluator and API run collector exist; no production theorem-status aggregator |
| MVC-015 | Meta-verification CI workflow | Test orchestration | Runs evaluator, collector, and provenance-policy tests | 52 tests passed in run 44209941107 on commit 51d341c354a09ecfdeb11f6b687e9105e7d61408 |
| MVC-016 | Post-run evidence collection workflow | External evidence acquisition | Queries GitHub API and emits normalized run evidence | Run 44209966698 reported ACCEPTED for harness run 44209941107; subject artifact 14386160694 uploaded |
| MVC-017 | GitHub/Sigstore attestation producer | Provenance signing | Signs exact evidence JSON subject with SLSA provenance via OIDC | Validated in producer run 44209966698 using actions/attest pinned to 1e69f48acb82d1966a394da916b4c1698aa569d6 |
| MVC-018 | Separate signed-provenance verifier workflow | Independent evidence verification | Downloads producer artifact and verifies signature, certificate identity, source commit, timestamp, and subject digest | Run 44210006677 completed successfully; report artifact 14384409245 uploaded |
| MVC-019 | Provenance policy verifier and adversarial tests | Evidence-policy checker | Applies repo ID, source ref/commit, signer commit, predicate, timestamp, and digest policy after gh verification | 18 adversarial tests included in 52-test suite; run 44209941107 passed |
| MVC-020 | GitHub CLI provenance verifier | Cryptographic verification dependency | Verifies Sigstore signature, certificate chain, transparency evidence, and signer policy | Runner-provided `gh` version 2.103.3 is pinned in policy and checked fail-closed; exact binary provenance remains external |
| MVC-021 | External trust-root package verifier | Trust-anchor policy checker | Checks immutable external repository checkout, clean tree, manifest/key digests, Ed25519 signature, repository IDs, signer/builder identities, and validity window | Implemented in `meta_verification/external_trust_root.py`; 27 adversarial tests included in 89-test harness, run 44211770333 passed |
| MVC-022 | External trust-root bootstrap workflow | Protected trust-anchor activation gate | Manually checks out a separately governed trust-root package under `meta-trust-root` Environment protection | Implemented in `.github/workflows/meta-trust-root-bootstrap.yml`; not yet run because external root and protected Environment are not provisioned |
| MVC-023 | Independent trusted-builder authority | Build/signing authority | Supplies a reusable workflow pinned to a separately administered repository and commit | Contract specified; no external builder repository provisioned and current producer does not delegate to it |
| MVC-024 | Trusted-builder contract and report schema | Normative interface / output contract | Defines immutable builder identity, caller authorization, subject validation, signing constraints, independent verifier requirements, and activation gates | Specified in `meta_verification/TRUSTED_BUILDER_CONTRACT.md`; JSON report schema in `meta_verification/trusted_builder_report.schema.json`; not yet implemented by an external builder |
| MVC-025 | Trusted-builder contract regression tests | Structural contract checker | Checks strict report schema invariants and required contract/activation statements | 10 tests added; combined harness run `44212792319` passed 89 tests on commit `ea217ddce37f76f02a29e96eb34839ddf06d1164`; collector `44212816996` accepted it (subject artifact `14386168406`) and verifier `44212845744` reported `VERIFIED` (report artifact `14387166418`); tests validate artifact structure, not external builder implementation |
| MVC-026 | Component provenance authenticator | Direct cryptographic evidence verifier | Verifies every required component's exact evidence bytes against GitHub/Sigstore SLSA provenance, certificate identity, subject digest, source commit, and run invocation ID/attempt | Implemented in `meta_verification/component_provenance_authenticator.py`; tests use controlled fake CLI output; no live component artifact authenticated |
| MVC-027 | Component receipt schema 2.0 and authentication-gated aggregator | Receipt contract / aggregation control | Removes self-asserted VERIFIED status and requires an in-memory authenticated map before ACCEPTED | Implemented in `status_aggregator.py` and `policy_activation_gate.py`; standalone aggregator CLI cannot accept unauthenticated JSON; external pin and production activation remain NOT ACTIVE |
| MVC-028 | Component provenance mutation suite | Checker challenge infrastructure | Applies selected bypasses to policy pin, evidence digest, run ID/attempt, workflow revision, CLI failure, invocation ID, subject digest, and aggregation gate | 10/10 selected mutants killed in full harness run [44238894962](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238894962) on commit `e8da7e8923440716a1b1dbf85c6f2c7b0408c9dc` |\n| MVC-029 | Live component-provenance smoke workflow | Real-signature integration test | Downloads the exact signed collector evidence artifact and verifies it through the component authenticator and aggregator | Live smoke run [44240468560](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240468560) succeeded on signer commit `7d5f778e9cd05cd1ef1095dd23f139d83aba8248`; actual producer run `44240436570`, run attempt 1; exact subject SHA-256 `b2cbc1a74afc06e47ba9b0cba2feee31aca9fb59f459562338329ce5964119aa`; aggregator returned `ACCEPTED`; scope remains one collector subject, not theorem evidence |

## 3. Observed repository-owned components

### MVC-001 — GitHub Actions workflow

- **Path:** `.github/workflows/constant-llpoy-lean.yml`
- **Blob SHA:** `592de198ac37aae08eb1a2021af1131b5682d5a8`
- **Observed workflow name:** `Constant Llapoy Lean Formalization`
- **Observed job:** `lean-build` (`Pinned Lean and Mathlib build`)
- **Runner:** `ubuntu-latest`
- **Timeout:** 45 minutes
- **Triggers:** push to `main` and pull requests when `formalization/lean/**` or this workflow file changes; also `workflow_dispatch`.
- **Permissions:** `contents: read`
- **Concurrency:** keyed by `github.ref`, with in-progress runs cancelled.
- **Steps:** checkout repository; run pinned Lean action with `lake-package-directory: formalization/lean`, `use-mathlib-cache: true`, `build: true`, and `axiom-audit: true`.

**Meta-verification observations:**
- The workflow has one job in the inspected revision; no separate meta-verification, mutation, malformed-input, aggregator truth-table, or independent-checker job is declared.
- The path filter does not include the governance documents or diagnostic scripts. A change to those files alone does not trigger this Lean workflow. This is not automatically a defect in the Lean build workflow; it means the current workflow is not a meta-verification test pipeline.
- `ubuntu-latest` is a moving runner label. The workflow does not pin an exact runner image or OS build.
- The configured Mathlib cache is a build acceleration dependency; cache provenance and cache-miss/fallback behavior are not audited in this register.

**Required challenge tests:** simulate skipped/missing job, wrong source revision, action revision change, missing axiom-audit step, timeout, cancelled run, and stale successful run. The expected aggregate result for every such required-evidence failure is non-passing.

### MVC-002 — Checkout action

- **Reference in workflow:** `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`
- **Pin type:** full commit SHA in workflow source.
- **Role:** source checkout.
- **Known limitation:** pinning identifies the requested action revision; it does not establish that the action is defect-free or that the checkout result was the intended source unless the resulting commit/tree identity is recorded and checked.
- **Required tests:** assert checked-out `HEAD` equals the event's expected commit; reject detached/mismatched/stale source evidence.

### MVC-003 — Lean action

- **Reference in workflow:** `leanprover/lean-action@498ce7030982ff0e0cecd98a8f5a7c90615b4e41`
- **Pin type:** full commit SHA in workflow source.
- **Role:** invokes the configured Lean/Lake build and axiom audit.
- **Known limitation:** action pinning does not independently validate the action implementation, its transitive dependencies, or the semantic completeness of its axiom audit.
- **Required tests:** inspect action contract and source at pinned revision; introduce a controlled failing Lean declaration and verify the job fails; verify an axiom-audit violation is surfaced; test timeout and missing-step handling.

### MVC-004 — Lean toolchain

- **Path:** `formalization/lean/lean-toolchain`
- **Blob SHA:** `00f848359b1cdaf7c12cd6b7acc5b4364752e154`
- **Declared toolchain:** `leanprover/lean4:v4.36.0`
- **Role:** Lean compiler/elaborator/kernel environment used by the project.
- **Limitation:** the toolchain label is pinned in the repository, but this inventory has not downloaded, hashed, or independently reproduced the actual toolchain binary distribution.
- **Required tests:** record resolved toolchain version and binary provenance in each run; rebuild from a clean environment; assess cache and platform dependence.

### MVC-005 — Lake project configuration

- **Path:** `formalization/lean/lakefile.lean`
- **Blob SHA:** `c135825a39770b3f26860aeae9983b8351d490f6`
- **Observed package:** `constantLlapoy`, version `0.1.0`
- **Observed library target:** `ConstantLlapoy`
- **Observed direct dependency:** Mathlib at commit `96f6b8b8e029545577421f198a89fb174a4d62e6`.
- **Required tests:** compare the resolved package graph with the committed manifest; reject unreviewed dependency drift.

### MVC-006 — Lake dependency manifest

- **Path:** `formalization/lean/lake-manifest.json`
- **Blob SHA:** `50c9c6c7b804d78fc77aeb6eaba1f676d18ce399`
- **Observed direct dependency:** Mathlib `96f6b8b8e029545577421f198a89fb174a4d62e6`.
- **Observed transitive package revisions:** plausible `054b228ce0ac61d767c6e71ba73a24728f191b72`; LeanSearchClient `4fb58e749ef3fc0395fe274f6cab70c2ea85f1c9`; importGraph `8370c640afcd1cc3fb1cb9bf1560cc66eafee5e0`; ProofWidgets4 `2f0f3520daeac2d9310ff25b7a877a0e5cdaa203`; aesop `66ff77cf0c4c898799e4b94d14db55f7a02d0c5a`; quote4/Qq `ff055a2fcc835935e0ae607339b455a5f5896b4b`; batteries `b4b25a3886a16daacaf6615c2eea7170a6e8f458`; lean4-cli/Cli `50810f72af7618bee62fe9800dc26e806c188703`.
- **Limitation:** these are observed lock entries, not a completed independent supply-chain audit. Package source integrity, build provenance, and all transitive build-time dependencies remain to be assessed.
- **Required tests:** clean resolution without `lake update`; compare exact revisions; detect manifest edits; test whether cache use can mask missing or altered source dependencies.

### MVC-007 — Lean proof modules

Observed modules under `formalization/lean/ConstantLlapoy/PaperA/`:

| Module | Blob SHA |
|---|---|
| `PerronFrobeniusCore.lean` | `78942634383ca8eba93b487f5f6fb58e38dbb6ac` |
| `StrongCoupling.lean` | `4ffbbc0e39616cfc4e27c00a86e4110331190b27` |
| `WeakCoupling.lean` | `10ae888e5f2c89565621213237c0fa7067a42744` |
| `ZeroEigenvalueEntropy.lean` | `4088d32b90369da91f6703d0146ff3c0359767b7` |

These are proof inputs, not independent checkers. The Lean kernel's acceptance is the primary formal evidence route under the declared Lean toolchain and assumptions. The repository's obligation register distinguishes build-verified and axiom-audited declarations from open obligations; that distinction must be preserved.

## 4. Exploratory diagnostics (not decisive proof checkers)

The tracked tree contains the following Python diagnostics. Their own docstrings explicitly characterize them as numerical/reproducibility diagnostics rather than proofs:

| Component ID | Path | Blob SHA | Dependencies / method | Intended evidential role |
|---|---|---|---|---|
| MVC-009a | `working/paper-a/dicke_even_basis_exact_diagnostic.py` | `56089c375e623caa8ddf22db1781aba3283146ed` | SymPy; exact/symbolic Dicke-basis perturbation diagnostic | Exploratory finite-order symbolic evidence; not a universal proof |
| MVC-009b | `working/paper-a/edge_response_finite_difference_diagnostic.py` | `1f4323685a1f992f20f1e6b43f72056b0265109a` | mpmath; high-precision full-Hilbert-space finite differences | Numerical diagnostic only |
| MVC-009c | `working/paper-a/edge_response_weak_coupling_diagnostic.py` | `53040cdfa1858f791170abae201402604254d8da` | mpmath; high-precision finite-difference weak-coupling check | Numerical diagnostic only |
| MVC-009d | `working/paper-a/finite_n_strong_coupling_exact_diagnostic.py` | `dbd1ca5334dfe2547290099d998a984ccbe911eb` | SymPy; exact-rational finite-N perturbation diagnostic | Finite-N reproducibility diagnostic; not a uniform-in-N theorem |

These scripts are not wired into the inspected GitHub Actions workflow. Their presence does not establish that they have been executed on the current snapshot. Their outputs MUST NOT be promoted to proof or to a universal statement without a separate mathematical argument and appropriate formal/exact evidence.

## 5. External services and unpinned execution boundaries

### MVC-008 — GitHub Actions run/job status

- **Historical run inspected:** `43998392546`.
- **Observed job:** `Pinned Lean and Mathlib build`.
- **Observed result:** completed / success; checkout and Lean build plus configured axiom-audit step completed successfully.
- **Commit associated with that historical evidence, as documented in `formalization/lean/PAPER_A_LEAN_OBLIGATION_REGISTER.md`:** `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`.
- **Scope limitation:** this historical run is not evidence for the current tree SHA `70268efc1ea2eca4fbff0aaaf7bb7e9364d3f88a`.
- **Current snapshot status lookup:** the GitHub combined-status query for the observed current tree SHA returned no status entries. This is recorded as `NO_STATUS_ENTRIES_RETURNED`, not as success or failure.

### MVC-010 — GitHub-hosted runner

- **Observed label:** `ubuntu-latest`.
- **Exact image/build:** unknown from the workflow source inspected.
- **Risk:** the runner image may change while the workflow file remains unchanged.
- **Required control:** record OS image/version, architecture, runtime, and relevant environment details for decisive runs; consider a pinned container/toolchain environment where reproducibility requires it.

### MVC-011 — GitHub evidence infrastructure

- **Role:** external execution, status, logs, and artifact infrastructure.
- **Exact retention configuration, attestation policy, and administrative trust boundary:** not established in this initial inventory.
- **Required control:** preserve raw logs and run metadata; record run ID, attempt, event, ref, commit, workflow revision, job IDs, and artifact digests; independently verify the evidence links.

## 6. Not observed in the inspected tracked-tree snapshot

The recursive tree contained 151 entries. The following components were not observed in the initial 151-entry snapshot; subsequent implementation status is recorded below:

- a standalone certificate parser or certificate checker;
- a meta-verification challenge-test harness (subsequently added);
- mutation operators or a mutation runner;
- fault-injection tests for CI/workflow status;
- a repository-owned status aggregator or report generator;
- a second independent formal prover workflow;
- a post-run GitHub API evidence collector (subsequently added; it is not an independent signature/attestation verifier).

This is a bounded observation about the inspected tracked tree only. It does not establish that no such capability exists outside this repository, in a hosted service, or in an untracked local environment.

## 7. Immediate assurance gaps and priority

| Priority | Gap | Why it matters | Required next action |
|---|---|---|---|
| P0 | External trust-root bootstrap is implemented but not activated | No external trust-root package, Ed25519 private key custody, or external trusted-builder identity was supplied or provisioned in this work; protected Environment reviewer/pins have not been verified; current producer still signs inside the relying-party repository | Provision the three separately governed repositories/roles, configure protected Environment and independent branch/ruleset review, run bootstrap, then delegate signing to the pinned reusable builder |
| P0 | Current Lean workflow has only one decisive job and no independent workflow audit | A skipped/misconfigured job or action defect may not be detected by a second route | Add explicit workflow contract checks and an independent review checklist; do not call this a second proof checker |
| P0 | Evaluator correctness beyond the current test set is not established | Passing tests cover only enumerated cases and may share assumptions with the evaluator | Independent review, additional property-based/mutation tests, and retained external challenge evidence are still required |
| P1 | Runner image is `ubuntu-latest` | Environment can change without source revision changes | Capture exact runner metadata and bind it to evidence |
| P1 | No exact current-head Lean proof-build result is established by the meta-verification run | The successful meta-verification workflow tests its harness, not the Lean proof build | Collect and bind the Lean workflow's own run, jobs, steps, toolchain, and commit evidence |

| P2 | Diagnostic scripts are not wired into a controlled test harness | Outputs may be run ad hoc and are not revision-bound by a standard evidence package | Define reproducible commands, environment pins, and raw-output capture for any diagnostic used as evidence |
| P2 | External action/toolchain supply chain not independently reviewed | SHA pinning alone does not establish trustworthiness | Perform source/dependency/TCB review and record residual trust |

## 8. Initial component-level disposition

- **Repository-owned workflow:** Observed; not meta-verified.
- **Pinned action references:** Observed; source/contract review pending.
- **Lean toolchain and manifest:** Observed and version-pinned in source; independent provenance review pending.
- **Lean proof inputs:** Observed; mathematical obligations remain claim-specific.
- **Python diagnostics:** Observed; exploratory only, not proof checkers.
- **Status and artifact infrastructure:** GitHub API collection, artifact upload, Sigstore signing, and separate provenance verification are exercised; service trust and external trust-root governance remain incomplete.
- **Policy evaluator and adversarial tests:** implemented; original 21-test suite passed in run `44207325850`.
- **GitHub run collector and adversarial tests:** implemented; combined 34-test suite passed in run `44208176534` on commit `4d1c97e6c4c25ec6569ecbae33062bcc4b9bdb17`.
- **Post-run API collection:** run `44208206996` completed successfully; collector reported `ACCEPTED` for run `44208176534`; artifact `14385166179` was uploaded. A cancelled upstream run (`44208158463`) was recorded as `REJECTED`, not accepted.
- **Signed provenance:** bounded end-to-end validation passed. Harness run `44209941107` passed 52 tests; producer run `44209966698` accepted that run and signed its evidence; separate verifier run `44210006677` reported `VERIFIED` for one attestation. Producer artifact `14386160694`; verifier report artifact `14384409245`.
- **External trust-root verifier:** 27 additional adversarial tests, including real Ed25519 signature verification, RSA-key rejection, path-traversal rejection, GitHub repository-ID binding, immutable checkout and tampered-manifest rejection; combined harness run `44211770333` passed 89 tests on commit `a9b582a4a24761af14ed7e64292746c7cb600245`. Collector run `44211799128` accepted that harness run and uploaded signed evidence artifact `14385663249`; separate verifier run `44211832036` reported `VERIFIED`, report artifact `14386925435`.
- **Pinned provenance tooling:** `actions/attest` commit `1e69f48acb82d1966a394da916b4c1698aa569d6`; `actions/download-artifact` commit `d3f86a106a0bac45b974a628896c90dbdf5c8093`; GitHub CLI version `2.103.3` enforced by policy.
- **Not active:** independent external trust-root repository/key, protected Environment/reviewer configuration, and reusable trusted builder. The verifier and bootstrap workflow are implemented; the external trusted-builder contract and strict report schema are specified. They cannot establish independent governance until those external controls are provisioned and the builder is independently implemented and tested. Mutation runner against Lean, independent certificate-semantics checker beyond GitHub CLI, and theorem-status aggregation also remain absent.

**Overall register status: PARTIAL INVENTORY / SIGNED-PROVENANCE VALIDATED (BOUNDED) / EXTERNAL TRUST-ROOT BOOTSTRAP IMPLEMENTED BUT NOT ACTIVATED.**

## 9. Required follow-up sequence

1. **Done (initial):** repository-owned policy evaluator and adversarial unit tests.
2. **Done (bounded):** GitHub REST API run collector, revision pins, required-job/step validation, and post-run evidence artifact workflow.
3. **Done (bounded):** Sigstore-signed evidence production and a separate verifier validated in runs `44209734212` and `44209776450`; the verifier checked exact repository ID, source commit, signer workflow, predicate, timestamp evidence, and subject digest.
4. Extend negative end-to-end tests for wrong signer, wrong repository, stale source, missing attestation, and modified subject.
5. Add a trusted reusable builder or external policy authority outside repository maintainer control; independently review policy and workflow change control.
6. Add mutation/property-based tests and collect/verify Lean proof-build evidence separately from harness-test evidence.

## 10. Governing rule

> Inventory only what is evidenced. A pinned component is not thereby trusted; an absent entry is not proof of nonexistence; a successful historical job is not evidence for a different commit; and a diagnostic is not a theorem.


## 11. Trusted-builder local reference inventory

- `meta_verification/trusted_builder_reference.py`: implemented non-signing reference validator; status is local/untrusted only.
- `meta_verification/test_trusted_builder_reference.py`: adversarial tests for valid local evidence, subject digest mismatch, caller identity/ref mismatch, failed/cancelled/skipped/incomplete upstream runs, replayed run IDs, source commit mismatch, absolute/traversal/dot/backslash paths, symlink and directory rejection, oversized/empty subjects, invalid UTF-8, duplicate JSON keys, malformed JSON, unknown fields, stale record digest, rejected evidence, and upstream repository ID mismatch.
- `meta_verification/TRUSTED_BUILDER_REFERENCE_IMPLEMENTATION.md`: explicit assurance boundary and non-implementation list.
- Commit `d8494c4f13aecf133ae156510e72ec689ee16fef` passed 117 tests in harness run [44217266945](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217266945). It adds descriptor-relative no-follow path traversal, FIFO rejection, bounded descriptor reads, and non-standard JSON constant rejection. Evidence producer run [44217302386](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217302386) accepted the exact harness run, and separate verifier run [44217348019](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44217348019) reported `VERIFIED` for one attestation and subject SHA-256 `215bc65558198d13f520266d0f6ec7e20363e44013c4c982c3a63010a0278a6d`. This remains bounded in-repository provenance, not an independent builder.

This local implementation is not an external builder and does not satisfy independent trust-root, signer, or builder governance. The normative activation gate remains NOT ACTIVE.


## 12. Trusted-builder black-box conformance suite

### MVC-026 — Local trusted-builder CLI conformance harness

- **Implementation under test:** `meta_verification/trusted_builder_reference.py`.
- **Independent test driver:** `meta_verification/test_trusted_builder_conformance.py`.
- **Method:** separate-process CLI invocation; the conformance tests do not import the implementation module. The test driver independently creates a known-answer evidence record and checks process exit status, JSON stdout, output report fields, and output-file framing.
- **Positive control:** accepts a known-answer evidence subject only as `VALIDATED_LOCAL_UNTRUSTED`; asserts signing, attestation, and trust flags are false.
- **Negative vectors:** subject digest substitution; caller repository ID/workflow/ref mismatch; failed and incomplete upstream run; replayed run ID; source revision mismatch; absolute and traversal paths; subject and parent-directory symlinks; duplicate JSON keys; malformed UTF-8; non-standard JSON constants; unknown evidence fields; stale canonical record digest; rejected evidence; oversized subject.
- **Observed result:** harness run [44220321270](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220321270) passed 137 tests on commit `7eae9f587f8426407b54abc58d9c1e78e374827c`. Producer run [44220345819](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220345819) completed successfully and signed the exact harness evidence. Separate verifier run [44220402372](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44220402372) completed successfully and reported `VERIFIED` for one attestation, exact signer source commit `7eae9f587f8426407b54abc58d9c1e78e374827c`, and subject SHA-256 `40ec934fbc0c1e4dff64bb78260cf9a396333c86412b4307c16a56a4e7593ee8`; verifier report artifact `14389712788`.
- **Independence limitation:** black-box relative to the Python implementation, but the test suite remains in the same repository and CI governance. It is not a reviewer-controlled external test authority, does not authenticate caller/upstream metadata independently, and does not test real external OIDC/Sigstore signing.
- **Status:** Implemented and validated for the local reference CLI's stated input class; external trusted-builder contract remains NOT ACTIVE.

This component is an implementation-level conformance harness, not a trusted-builder deployment. Its positive result must never be interpreted as signed provenance or as evidence of independent administration.


## 13. Trusted-builder mutation adequacy harness

### MVC-027 — Controlled mutation testing for black-box conformance

- **Test driver:** `meta_verification/test_trusted_builder_mutations.py`.
- **Tested suite:** `meta_verification/test_trusted_builder_conformance.py`.
- **Method:** for each mutation, create an isolated temporary copy of the CLI and conformance test, apply one targeted source mutation, syntax-check the mutant, then run the conformance suite against it as a subprocess.
- **Mutant-kill criterion:** the suite must execute and fail through an assertion/test failure. Syntax errors, import errors, or harness failures do not count as killed mutants.
- **Seven mutants:** subject byte digest bypass; canonical evidence digest bypass; acceptance-status bypass; caller repository-ID bypass; upstream run-ID/replay bypass; path traversal guard bypass; and local status escalation to `SIGNED`.
- **Observed result:** all 7/7 selected mutants killed. Full harness run [44229439161](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229439161) passed 138 tests on commit `ad73206847bc15ca4d3d0b1db68f74ad1b3d6901`; logs explicitly list each mutant as `MUTANT KILLED`.
- **Status:** Implemented and validated for the enumerated mutant set. This is a bounded adequacy result, not proof of exhaustive test strength or independent builder trust.

The suite's path-traversal test includes a matching byte-identical subject outside the checkout root. This ensures that bypassing the traversal guard cannot be accidentally masked by the later subject-digest check.


## 14. Adversarial input-space expansion and safe report output

### MVC-028 — Trusted-builder reference CLI boundary hardening

- **Implementation:** `trusted_builder_reference.py`; **black-box suite:** `test_trusted_builder_conformance.py`.
- **Metadata shape:** caller and upstream objects now reject both missing and unknown keys; boolean values are rejected where exact integer identifiers are required.
- **Request parser:** duplicate JSON keys and non-standard JSON constants are rejected at the CLI boundary.
- **Output path:** report creation traverses parent directories using directory file descriptors and no-follow opens, rejects symlink components, uses exclusive creation, and refuses to overwrite an existing file.
- **Provenance policy:** `repository_id` must have exact integer type; booleans are rejected.
- **Adversarial tests:** boolean caller repository ID; boolean upstream run ID; extra/missing caller fields; extra/missing upstream fields; duplicate request key; NaN request constant; output symlink; output parent symlink; existing output preservation; boolean provenance policy repository ID.
- **Observed result:** run [44229925358](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44229925358) passed 150 tests on commit `32befb3a3bda45705794e4484f94abe8cbb9b677`. Its job log also records all seven selected mutation tests as killed.
- **Status:** Implemented and validated for these explicit local CLI and policy-validation cases. No claim of exhaustive adversarial coverage or external builder activation.

The safe output writer is deliberately local and fail-closed. It does not make the request inputs authoritative, and a report remains `VALIDATED_LOCAL_UNTRUSTED`.


## 15. Signed-provenance verifier mutation harness

### MVC-029 — Mutation adequacy for provenance verification

- **Test driver:** `meta_verification/test_provenance_mutations.py`.
- **System under test:** `meta_verification/verify_signed_provenance.py`.
- **Oracle tests:** `meta_verification/test_signed_provenance.py`.
- **Method:** isolated temporary source copies; one targeted mutation at a time; syntax validation; execute the existing test suite; count only assertion-driven suite failures as kills.
- **Ten mutants:** certificate repository ID, source ref, source commit, signer workflow commit, verified timestamp requirement, predicate type, subject digest, unique subject matching, boolean repository ID policy, and exact pinned CLI version.
- **Observed result:** 10/10 selected mutants killed. Harness run [44230310401](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230310401) passed 151 tests on commit `8740ee0c024d4c30105d766d54679f563ee211cc`; log explicitly records all ten kills.
- **Test-quality correction:** the first run showed the boolean-ID mutant survived because another certificate-ID mismatch independently rejected the fixture. The fixture was corrected to align the certificate field with the boolean policy so the type-validation control is isolated; the rerun killed the mutant.
- **Status:** Implemented and validated for this selected set. No claim of exhaustive coverage or independent external assurance.


## 16. GitHub Actions run collector hardening and mutation tests

### MVC-030 — Collector identity and completeness controls

- **Implementation:** `meta_verification/github_run_collector.py`.
- **Unit/adversarial tests:** `meta_verification/test_github_run_collector.py`.
- **Mutation driver:** `meta_verification/test_collector_mutations.py`.
- **New controls:** exact integer type checks for workflow/run IDs and job count; positive run-attempt validation; equality of repository and head-repository numeric IDs; positive and unique job IDs; exact job-page count; existing workflow/evaluator blob SHA pins retained.
- **Selected mutants:** 13, covering policy/API boolean-ID confusion, run attempt, repository identity/name bindings, job pagination and IDs, workflow revision pin, and evaluator revision pin.
- **Observed result:** 13/13 selected mutants killed; full harness [44230994871](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44230994871) passed 164 tests on commit `8d23997fd0d746ba04f2528a5e34721293ae5514`.
- **Test development record:** initial executions failed on missing job-ID validation and three test-fixture masking conditions. The implementation and fixtures were corrected before the successful run.
- **Status:** Implemented and validated for the named test and mutant set. This is not exhaustive testing, a formal proof of collector correctness, or an independent audit of GitHub's API.



## 17. GitHub API response contract and replay resistance

### MVC-031 — Exact attempt binding and bounded API response parsing

- **Implementation:** `meta_verification/github_run_collector.py`.
- **Producer workflow:** `.github/workflows/meta-verification-evidence.yml` passes the upstream event's `run_attempt` in addition to run ID and head SHA.
- **Unit/adversarial suite:** `meta_verification/test_github_run_collector.py`.
- **Mutation suite:** `meta_verification/test_collector_mutations.py`.
- **Attempt binding:** API run attempt must equal the event-supplied attempt; each job's run ID and run attempt must equal the parent run/attempt.
- **API JSON contract:** UTF-8 object only; duplicate keys, non-standard constants, non-object roots, invalid UTF-8, and bodies over 10 MiB are rejected.
- **Transport behavior:** HTTP errors and timeouts fail closed.
- **Pagination:** jobs requested with `per_page=100`; mismatched `total_count`, incomplete result, or more than 100 jobs is rejected. No silent first-page acceptance.
- **Selected mutations:** 17, including boolean identity confusion, attempt mismatch, job/run attempt mixing, API duplicate-key acceptance, repository identity, pagination, and immutable workflow/evaluator blob pin bypass.
- **Observed result:** all 17/17 selected collector mutants killed; full harness run [44231737913](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44231737913) passed 176 tests on commit `295eea3e0e717569c3f981a3e272dc31b4de567d`.
- **Status:** Implemented and validated for the selected contract and mutation cases. This is not independent validation of GitHub's API or exhaustive replay resistance.



## 18. Meta-verification aggregation and status authority prototype

### MVC-032 — Deterministic component evidence aggregator

- **Implementation:** `meta_verification/status_aggregator.py`.
- **Unit/adversarial tests:** `meta_verification/test_status_aggregator.py`.
- **Mutation driver:** `meta_verification/test_status_aggregator_mutations.py`.
- **Policy inputs:** exact claim ID, immutable policy revision, and unique required component set.
- **Bundle binding:** expected source commit is supplied independently; claim and policy revision must match; missing, duplicate, unknown, stale, and conflicting records fail closed.
- **Component state model:** PASS / FAIL / INCONCLUSIVE / ERROR / TIMEOUT / NOT_RUN.
- **Evidence binding:** non-empty bounded bytes, Base64 validation, SHA-256 digest; schema 2.0 receipt structure and source/subject binding; exact positive integer attestation run ID/attempt and workflow revision.
- **Status semantics:** digest mismatch or authenticated FAIL → REJECTED; malformed contract → ERROR; missing authentication, incomplete/stale/duplicate/non-PASS → INCONCLUSIVE; ACCEPTED requires every required component to have a matching in-memory result from the direct attestation authenticator.
- **Output limitation:** standalone aggregator CLI never receives authenticated records and therefore cannot return ACCEPTED. The internal Python function is not a security sandbox; production must use the activation-gate CLI, which performs direct attestation verification first. Provenance does not prove mathematical correctness.
- **Selected mutation set:** 12; all 12/12 killed. Corrected full harness [44232385272](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44232385272) passed 202 tests on commit `0c1bc5d2e5bd3bb8808222c71868edfa81b83bce`.
- **Test correction record:** initial harness run [44232264438](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44232264438) failed. It exposed an incorrect escalation from duplicate conflicting component records to REJECTED; duplicate IDs are now excluded from state authority and force INCONCLUSIVE. A stale mutation anchor was also corrected.
- **Status:** Implemented and validated as a structural prototype only. It is not yet an independently authenticated or production-integrated status authority.



## 19. Policy authority and change control prototype

- **Implementation:** meta_verification/policy_change_control.py.
- **Adversarial tests:** meta_verification/test_policy_change_control.py.
- **Mutation suite:** meta_verification/test_policy_change_mutations.py.
- **Contract:** meta_verification/POLICY_AUTHORITY_AND_CHANGE_CONTROL.md.
- **Controls:** externally supplied authority-set SHA-256 pin; distinct Ed25519 reviewers; threshold signatures; exact policy content digest; parent digest; monotonic next sequence; validity window; duplicate/unknown reviewer rejection.
- **Activation boundary:** POLICY_CHANGE_AUTHORIZED is not activation. External policy-pin update and protected reviewer controls remain mandatory.
- **Limitations:** authority-set digest is supplied by caller; OpenSSL runtime is not independently pinned; no external authority/reviewer identities/protected Environment are provisioned; verifier is not in production status workflow.
- **Status:** prototype implementation; do not claim independent policy governance or mathematical theorem acceptance.


**Validation update:** commit 56f4ac5678ab5dc1225075fa242e442f2601da57 passed the full harness (219 tests; run [44233157563](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233157563)) and killed 8/8 selected policy-change mutants. Its evidence producer [44233215756](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233215756) succeeded; separate provenance verifier [44233252327](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233252327) returned VERIFIED. These results are bounded to the tested commit and selected tests, not independent policy governance.


## Policy activation integration component

Added `meta_verification/policy_activation_gate.py` as an activation gate around the existing structural `status_aggregator.py`; no duplicate aggregator was introduced. It requires separately supplied external SHA-256 pins for the authority set and active-policy record, then checks exact policy bytes, policy ID, sequence, authority binding, ACTIVE state, validity interval, and threshold Ed25519 signatures before calling the structural aggregator.

The final status is now `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`. The activation CLI requires a separately supplied provenance-policy digest and directly verifies every required component's exact evidence bytes before invoking the aggregator. No production workflow currently emits attestations for every component, no real component bundle has been authenticated, and no external authority/provenance pin source is active.


### Policy activation CLI

`meta_verification/policy_activation_gate.py` now provides an executable CLI with explicit required inputs and no default trust pins. The caller must provide exact policy, authority-set, activation-record, and bundle files; expected source commit; authority-set and activation-record SHA-256 pins; policy ID and sequence; and trusted epoch time. It rejects symlinks, non-regular files, oversized files, duplicate JSON keys, and missing or malformed pins. The caller's pin/time trust is outside the CLI: production must inject them from separately administered protected controls. No production workflow currently invokes it.


## 20. Component provenance receipt authentication

- **Normative contract:** `meta_verification/COMPONENT_PROVENANCE_RECEIPT_AUTHENTICATION.md`.
- **Authenticator:** `meta_verification/component_provenance_authenticator.py`.
- **Receipt schema:** exact schema 2.0 fields: subject SHA-256, source commit, attestation run ID, run attempt, and attestation workflow revision. A caller-controlled `status: VERIFIED` field is rejected.
- **Cryptographic checks:** direct `gh attestation verify` on each exact evidence subject; repository numeric identity, source ref, source commit, signer commit, verified timestamp, SLSA v1 predicate, unique subject digest, and SLSA `invocationId` bound to the receipt's run ID/attempt.
- **Policy binding:** provenance-policy raw bytes must match an externally supplied SHA-256 pin; parsed policy object must match those exact bytes.
- **Aggregation:** standalone aggregator CLI has no authenticated-map input and cannot return ACCEPTED for JSON-only receipts. The activation CLI constructs the in-memory map after direct verification and then aggregates.
- **Tests:** `test_component_provenance_authenticator.py` uses fake GitHub CLI outputs to test the contract; it is not a live signature test. `test_component_provenance_mutations.py` covers a selected set of deliberate bypasses.
- **Limitations:** existing evidence producer signs only `github-run-evidence.json`, not every component artifact. No per-component attestation producer or real end-to-end component bundle is operational. External provenance-policy pin, authority pins, protected controls, and trusted time are not provisioned. Production activation remains NOT ACTIVE.


**Validation record — component provenance integration:** on commit `e8da7e8923440716a1b1dbf85c6f2c7b0408c9dc`, the full harness passed 263 tests (28.235 seconds); component provenance mutation 10/10, aggregator mutation 12/12, activation mutation 9/9. Evidence producer run [44238972702](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238972702) succeeded; separate verifier run [44239010485](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44239010485) reported VERIFIED for the collector evidence subject only. No live per-component attestation was authenticated.


## 10. Paper A first execution-pipeline components

| Component | Implementation | Evidence scope | Explicit non-claim |
|---|---|---|---|
| Lean build | Paper A evidence producer workflow and component pipeline script | Pinned Lean build, configured axiom audit, captured lake build transcript and module/dependency hashes | Does not prove unformalized claims or manuscript correspondence |
| Exact diagnostics | Same producer workflow | Two finite-N symbolic diagnostic outputs | Not a proof or uniform-in-N result |
| Numerical diagnostics | Same producer workflow | High-precision finite-difference outputs for bounded N and parameter samples | Numerical evidence only |
| Claim traceability | Traceability generator | Resolves all 15 Paper A registry rows to records and frozen source snapshots; hashes files and candidate links | Candidate links do not establish semantic correspondence |
| 14-layer plan | Layer-plan generator | Emits applicability, status, and rationale for all 14 layers | Plan generation is not a layer PASS |
| Component verifier | Component authenticator and separate workflow | Verifies seven exact subjects and binds producer run ID, attempt, and source revision | Policy digest remains same-checkout; external trust is not active |

The pipeline's overall status is scoped to execution evidence and provenance. The report must retain overall_paper_status as NOT_VERIFIED.


### 10.1 First observed Paper A Lean execution

The first producer attempt at revision dc3273a0a2f75c8e32e47407b1e972edcc882a23 failed in the pinned Lean build at ConstantLlapoy.PaperA.PerronFrobeniusCore. The log reports RCLike (RCLike Real) typeclass synthesis failures and unsolved goals around lines 690–709. The initial fail-fast run emitted no component artifact. The producer has since been changed to capture the failed Lean transcript, continue other diagnostics, and let the 14-layer assessment mark L-04 FAILED. No Lean proof was edited or weakened to make the pipeline green.


### 10.2 Observed first Paper A evidence run

| Evidence | Observed result |
|---|---|
| Producer run | 44248949683 SUCCESS at source commit 1173aba070abd89fcb5f62f14e7fd8494bdaa464 |
| Separate verifier run | 44249207601 SUCCESS |
| Attested subjects | 7 |
| Authenticated component subjects | 7/7 |
| Aggregator | REJECTED due to one authenticated failed check |
| Missing / duplicate / stale / digest mismatch / unauthenticated receipts | 0 / 0 / 0 / 0 / 0 |
| Failed component | PAPER_A_LEAN_BUILD |
| Claim traceability | 15/15 Paper A registry records resolved and hashed |
| 14-layer assessment | 14 rows emitted; L-04 FAILED, L-02 BLOCKED, L-05/L-13 NOT_RUN, L-14 NOT_ASSESSED, remaining layers PARTIAL |
| Mathematical result | NOT_VERIFIED |

The four exact/numerical diagnostic commands completed with exit code 0. The Lean build command exited 1 and its exact output was included in the attested evidence. All seven evidence subjects were authenticated, so the failed Lean outcome is not an artifact-integrity failure. It is a genuine formalization/build failure. External trust-root activation remains NOT ACTIVE.
