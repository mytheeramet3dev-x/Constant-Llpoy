# Paper A — Lean Formalization Obligation Register

**Project:** Constant Llapoy  
**Scope:** Paper A only  
**Current modules:** ConstantLlapoy/PaperA/WeakCoupling.lean; StrongCoupling.lean; ZeroEigenvalueEntropy.lean  
**Toolchain:** Lean 4.36.0; Mathlib commit 96f6b8b8e029545577421f198a89fb174a4d62e6  
**Latest CI evidence:** ZF-2 run 43998392546, commit `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`; the sole workflow job completed the pinned Lean/Mathlib build and configured axiom audit successfully. `lake test` and `lake lint` were not run and are not recorded as passing.

## Status vocabulary

- **SOURCE_SPECIFIED:** mathematical obligation and source evidence are identified.
- **FORMALIZED_UNBUILT:** Lean declaration exists but has not passed a pinned build.
- **BUILD_VERIFIED:** pinned Lean build passed; this is not by itself manuscript correspondence.
- **AXIOM_AUDITED:** declaration was included in a successful axiom-audit run and its axioms were within the configured allowlist; this is not an independent proof checker.
- **INDEPENDENTLY_CHECKED:** a second checker or independent proof route has checked the declaration.
- **OPEN:** no complete formalization yet.
- **BLOCKED:** a specific obstacle is recorded.

## Obligation register

| ID | Mathematical obligation | Current state | Evidence / next requirement |
|---|---|---|---|
| PA-LEAN-001 | Positivity of alpha_N = log(2(N-2)/(N-1))/8 for N >= 4 | BUILD_VERIFIED; AXIOM_AUDITED | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-002 | Positive leading term plus an explicit half-leading-term remainder bound implies positive total | BUILD_VERIFIED; AXIOM_AUDITED | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-003 | Weak-coupling endpoint sign conditional on the explicit remainder bound | BUILD_VERIFIED; AXIOM_AUDITED | WeakCoupling.lean; does not prove the remainder bound itself |
| PA-LEAN-004 | Chain rule for the entropy contribution -f log f when f(x)>0 | BUILD_VERIFIED; AXIOM_AUDITED | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-005 | Analytic factorization/order of vanishing for a nonnegative eigenvalue branch at a zero | PARTIALLY BUILD_VERIFIED; AXIOM_AUDITED | `exists_local_power_factorization_of_analytic_nontrivial` supplies a one-variable finite-order factorization for a nontrivial analytic branch. ZF-2 parity and positivity are now separately BUILD_VERIFIED; joint `(r,u)` uniformity and the identically-zero case remain open |
| PA-LEAN-006 | Directional derivative of -lambda log(lambda) at a rank-changing zero branch | OPEN | Positive-branch bound is now separated as PA-LEAN-016; still need analytic order-of-vanishing at the zero branch and a rigorous entropy derivative limit |
| PA-LEAN-007 | One-site reduced-state eigenvalue expansion and all required edge derivatives | OPEN | Formalize perturbation expansion with explicit quantified remainder |
| PA-LEAN-008 | Two-site odd-block Gram matrix, coherence, positive eigenvalue branch, and edge derivatives | OPEN | Formalize the reduced density matrix and eigenvalue perturbation |
| PA-LEAN-009 | Even-block Schur-complement cancellation and small-eigenvalue remainder | OPEN | Prove the order-r^2 cancellation and a joint differentiated bound |
| PA-LEAN-010 | Pair-entropy remainder derivative, including the large eigenvalue correction | OPEN | Derive from the complete eigenvalue expansions |
| PA-LEAN-011 | Differentiated weak-coupling remainder O_N(r^3(1+|log r|)) in dimensionless edge coordinates | OPEN | This is the key bridge from formalized local expansions to the endpoint sign |
| PA-LEAN-012 | Existence of a sufficiently small coupling threshold from the asymptotic remainder | OPEN | Prove the relevant limit/bound; no threshold is currently formalized |
| PA-LEAN-013 | Positivity of the strong-coupling leading coefficient and conditional sign step | BUILD_VERIFIED; AXIOM_AUDITED | StrongCoupling.lean; obtain successful pinned build |
| PA-LEAN-015 | Strong-coupling differentiated remainder and endpoint threshold | OPEN | Prove the model-specific differentiated asymptotic and derive an explicit eventual bound |
| PA-LEAN-016 | Positive-branch entropy derivative bound under explicit logarithmic control and derivative bound | BUILD_VERIFIED; AXIOM_AUDITED | ZeroEigenvalueEntropy.lean; assumptions must be derived from two-sided eigenvalue factorization and differentiated perturbation estimates |
| PA-LEAN-017 | A differentiable function at a local minimum has zero derivative; apply it to a nonnegative zero branch | BUILD_VERIFIED; AXIOM_AUDITED | `hasDerivAt_local_min_branch_eq_zero` and `hasDerivAt_nonnegative_branch_eq_zero` both compile. The latter formalizes the conversion from eventual two-sided nonnegativity and `f x = 0` to a local minimum. This concerns the eigenvalue derivative only; it does not establish differentiability of -lambda log(lambda) at the zero branch |
| PA-LEAN-018 | Finite-order analytic factorization for a nontrivial real branch | BUILD_VERIFIED; AXIOM_AUDITED | `exists_local_power_factorization_of_analytic_nontrivial`; pinned CI run 43983006064. The theorem returns analytic quotient and nonzero leading coefficient but does not prove parity or positivity |
| PA-LEAN-019 | ZF-2: even vanishing order and positive leading coefficient for a nonnegative finite-order branch | BUILD_VERIFIED; AXIOM_AUDITED | `even_order_and_positive_leading_coefficient_of_nonnegative_factorization`; pinned CI run 43998392546 at commit `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`. Uses explicit eventual nonnegativity/factorization and continuity/nonzero quotient hypotheses. Does not establish joint parameter uniformity or ZF-8 identically-zero branch handling |
| PA-LEAN-020 | ZF-3a: local two-sided bounds for a positive continuous scalar quotient | BUILD_VERIFIED; AXIOM_AUDITED | `eventually_quotient_two_sided_bounds`; pinned CI run 44003303543 at commit `d6a92c2e032e10eb8764754d875cc18b145024e3`. Proves `g(0)/2 < g(r) < 3g(0)/2` eventually from continuity and `g(0)>0`; does not yet transfer bounds through `r^m), prove differentiated estimates, or establish parameter uniformity |

| PA-LEAN-021 | ZF-3b: transfer local quotient bounds through an even-order scalar factorization | BUILD_VERIFIED; AXIOM_AUDITED | `eventually_factored_branch_two_sided_bounds`; pinned CI run 44003303543 at commit `d6a92c2e032e10eb8764754d875cc18b145024e3`. Gives non-strict two-sided bounds for `f(r)=r^m g(r)) on a two-sided neighborhood when `m` is even. Scalar only; no parameter-uniformity, differentiated bound, or logarithmic control. |
| PA-LEAN-014 | Exact correspondence between Lean declarations and frozen Paper A manuscript statements | OPEN | Line-level statement and hypothesis mapping, including known source conflicts |

## Critical logical boundary

The declarations PA-LEAN-001 through PA-LEAN-004 and PA-LEAN-016 do **not** prove the weak-coupling endpoint theorem by themselves. PA-LEAN-003 assumes an explicit remainder inequality. PA-LEAN-011 and PA-LEAN-012 are still open and are required to derive that inequality from the analytic asymptotic estimate. PA-LEAN-016 is only an algebraic entropy-derivative estimate under explicit hypotheses; it does not prove those hypotheses. PA-LEAN-017 now formalizes Fermat's theorem for a supplied local-minimum hypothesis. The implication from two-sided nonnegativity and a zero value to that local-minimum hypothesis is now formalized by `hasDerivAt_nonnegative_branch_eq_zero`. It does not prove that -lambda log(lambda) is differentiable at the zero branch. For that, a higher-order analytic order-of-vanishing estimate is still required.

CI run 43979057358 completed the pinned Lake build and the configured axiom audit successfully. The audit reported 13 declarations, all using only the configured allowlist. The workflow did not execute `lake test` or `lake lint`, because their preliminary `lake check-test` and `lake check-lint` checks failed. A successful Lake build checks only that Lean accepts the declarations under the pinned environment. It does not prove that the formal declarations match the manuscript, nor does it validate any unformalized perturbation expansion.

No theorem status in CLAIM_REGISTRY.md is upgraded by the existence of these initial Lean source files.


The latest CI run 43983006064 completed successfully at commit `e4129b888a7ffe1bc00028fe23e840b83ed5f087`. Its sole job built the pinned Lean/Mathlib project and ran the configured axiom audit. It did not run `lake test` or `lake lint`. The new finite-order analytic factorization wrapper is build-verified and axiom-audited, but the parity and positive-leading-coefficient consequences remain open.


## ZF-2 verification update

The combined ZF-2 theorem `even_order_and_positive_leading_coefficient_of_nonnegative_factorization` is BUILD_VERIFIED and AXIOM_AUDITED by CI run `43998392546` at commit `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`. The run's sole job succeeded, including the pinned Lean build and configured axiom audit. The workflow did not run `lake test` or `lake lint`.

This theorem is conditional on explicit eventual nonnegativity, eventual factorization, continuity at zero, and a nonzero quotient value. The analytic factorization wrapper supplies an analytic quotient and nonzero value for a nontrivial analytic branch; the application must still connect these hypotheses. This does not prove uniformity in auxiliary parameters, compact-neighborhood two-sided bounds, the identically-zero branch, or entropy differentiability at the zero branch.
