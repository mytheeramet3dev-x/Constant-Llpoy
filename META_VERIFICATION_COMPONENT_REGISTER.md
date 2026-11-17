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
| MVC-001 | GitHub Actions workflow | Repository-owned orchestration | Runs Lean build and configured axiom audit | Observed; challenge tests absent from workflow |
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
| MVC-012 | Meta-verification test harness / mutation runner | Checker-challenge infrastructure | Should test checker and status logic | Not observed in tracked tree snapshot |
| MVC-013 | Dedicated certificate parser/checker | Certificate validation | Would validate certificate evidence independently | Not observed in tracked tree snapshot |
| MVC-014 | Repository-owned report generator/status aggregator | Evidence aggregation | Would convert required evidence into claim status | Not observed in tracked tree snapshot |

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
| `StrongCoupling.lean` | not captured in this initial register |
| `WeakCoupling.lean` | `10ae888e5f2c89565621213237c0fa7067a42744` |
| `ZeroEigenvalueEntropy.lean` | not captured in this initial register |

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

The recursive tree contained 151 entries. The following dedicated repository-owned components were not observed in that snapshot:

- a standalone certificate parser or certificate checker;
- a meta-verification challenge-test harness;
- mutation operators or a mutation runner;
- fault-injection tests for CI/workflow status;
- a repository-owned status aggregator or report generator;
- a second independent formal prover workflow;
- a workflow job that tests stale/missing/skipped evidence aggregation.

This is a bounded observation about the inspected tracked tree only. It does not establish that no such capability exists outside this repository, in a hosted service, or in an untracked local environment.

## 7. Immediate assurance gaps and priority

| Priority | Gap | Why it matters | Required next action |
|---|---|---|---|
| P0 | No observed meta-verification test harness or aggregation tests | The workflow's own false-acceptance paths are not challenged by repository tests | Add a small, deterministic test suite for status decisions and workflow evidence validation |
| P0 | Current workflow has only one decisive job and no independent workflow audit | A skipped/misconfigured job or action defect may not be detected by a second route | Add explicit workflow contract checks and an independent review checklist; do not call this a second proof checker |
| P1 | Runner image is `ubuntu-latest` | Environment can change without source revision changes | Capture exact runner metadata and bind it to evidence |
| P1 | No exact current-head status evidence returned | Current snapshot cannot inherit historical run success | Trigger or inspect a run for the exact current commit and bind its SHA |
| P1 | No separate status aggregator implementation observed | No tested policy currently demonstrates fail-closed claim aggregation | Implement a small pure status evaluator with exhaustive state-table tests before using aggregate badges/status |
| P2 | Diagnostic scripts are not wired into a controlled test harness | Outputs may be run ad hoc and are not revision-bound by a standard evidence package | Define reproducible commands, environment pins, and raw-output capture for any diagnostic used as evidence |
| P2 | External action/toolchain supply chain not independently reviewed | SHA pinning alone does not establish trustworthiness | Perform source/dependency/TCB review and record residual trust |

## 8. Initial component-level disposition

- **Repository-owned workflow:** Observed; not meta-verified.
- **Pinned action references:** Observed; source/contract review pending.
- **Lean toolchain and manifest:** Observed and version-pinned in source; independent provenance review pending.
- **Lean proof inputs:** Observed; mathematical obligations remain claim-specific.
- **Python diagnostics:** Observed; exploratory only, not proof checkers.
- **Status and artifact infrastructure:** external dependency; assurance evidence incomplete.
- **Dedicated checker/mutation/status harness:** not observed in the tracked snapshot.

**Overall register status: PARTIAL INVENTORY / NOT VALIDATED.**

## 9. Required follow-up sequence

1. Add a repository-owned meta-verification test harness that parses an explicit evidence record schema and evaluates statuses without invoking the checker under test.
2. Add exhaustive table-driven tests for `ACCEPTED`, `REJECTED`, `ERROR`, `TIMEOUT`, `INCONCLUSIVE`, `NOT_RUN`, missing, stale, skipped, contradictory, and partial evidence.
3. Add mutation cases for wrong commit, altered checker/workflow revision, omitted required job, missing axiom audit, and forged success metadata.
4. Run tests in CI and bind their results to the exact workflow and source revisions.
5. Independently review the harness and its expected outcomes; document shared assumptions and residual risks.
6. Reassess whether the meta-verification lifecycle is sufficiently distinct to justify a dedicated layer only after this operational evidence exists.

## 10. Governing rule

> Inventory only what is evidenced. A pinned component is not thereby trusted; an absent entry is not proof of nonexistence; a successful historical job is not evidence for a different commit; and a diagnostic is not a theorem.
