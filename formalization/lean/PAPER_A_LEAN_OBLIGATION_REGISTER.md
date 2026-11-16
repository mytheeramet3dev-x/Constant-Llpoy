# Paper A — Lean Formalization Obligation Register

**Project:** Constant Llapoy  
**Scope:** Paper A only  
**Current module:** ConstantLlapoy/PaperA/WeakCoupling.lean  
**Toolchain:** Lean 4.36.0; Mathlib commit 96f6b8b8e029545577421f198a89fb174a4d62e6  
**Current evidence state:** Initial CI submitted; no successful build has yet been recorded.

## Status vocabulary

- **SOURCE_SPECIFIED:** mathematical obligation and source evidence are identified.
- **FORMALIZED_UNBUILT:** Lean declaration exists but has not passed a pinned build.
- **BUILD_VERIFIED:** pinned Lean build passed; this is not by itself manuscript correspondence.
- **INDEPENDENTLY_CHECKED:** a second checker or independent proof route has checked the declaration.
- **OPEN:** no complete formalization yet.
- **BLOCKED:** a specific obstacle is recorded.

## Obligation register

| ID | Mathematical obligation | Current state | Evidence / next requirement |
|---|---|---|---|
| PA-LEAN-001 | Positivity of alpha_N = log(2(N-2)/(N-1))/8 for N >= 4 | FORMALIZED_UNBUILT | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-002 | Positive leading term plus an explicit half-leading-term remainder bound implies positive total | FORMALIZED_UNBUILT | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-003 | Weak-coupling endpoint sign conditional on the explicit remainder bound | FORMALIZED_UNBUILT | WeakCoupling.lean; does not prove the remainder bound itself |
| PA-LEAN-004 | Chain rule for the entropy contribution -f log f when f(x)>0 | FORMALIZED_UNBUILT | WeakCoupling.lean; obtain successful pinned build |
| PA-LEAN-005 | Analytic factorization/order of vanishing for a nonnegative eigenvalue branch at a zero | OPEN | Formalize joint analyticity, nonnegativity on a two-sided parameter neighborhood, and the first nonzero Taylor coefficient |
| PA-LEAN-006 | Directional derivative of -lambda log(lambda) at a rank-changing zero branch | OPEN | Must derive the logarithmic bound from the analytic factorization; an upper bound alone is insufficient |
| PA-LEAN-007 | One-site reduced-state eigenvalue expansion and all required edge derivatives | OPEN | Formalize perturbation expansion with explicit quantified remainder |
| PA-LEAN-008 | Two-site odd-block Gram matrix, coherence, positive eigenvalue branch, and edge derivatives | OPEN | Formalize the reduced density matrix and eigenvalue perturbation |
| PA-LEAN-009 | Even-block Schur-complement cancellation and small-eigenvalue remainder | OPEN | Prove the order-r^2 cancellation and a joint differentiated bound |
| PA-LEAN-010 | Pair-entropy remainder derivative, including the large eigenvalue correction | OPEN | Derive from the complete eigenvalue expansions |
| PA-LEAN-011 | Differentiated weak-coupling remainder O_N(r^3(1+|log r|)) in dimensionless edge coordinates | OPEN | This is the key bridge from formalized local expansions to the endpoint sign |
| PA-LEAN-012 | Existence of a sufficiently small coupling threshold from the asymptotic remainder | OPEN | Prove the relevant limit/bound; no threshold is currently formalized |
| PA-LEAN-013 | Strong-coupling endpoint proof | OPEN | Separate module and independent obligation review |
| PA-LEAN-014 | Exact correspondence between Lean declarations and frozen Paper A manuscript statements | OPEN | Line-level statement and hypothesis mapping, including known source conflicts |

## Critical logical boundary

The declarations PA-LEAN-001 through PA-LEAN-004 do **not** prove the weak-coupling endpoint theorem by themselves. PA-LEAN-003 assumes an explicit remainder inequality. PA-LEAN-011 and PA-LEAN-012 are still open and are required to derive that inequality from the analytic asymptotic estimate.

Likewise, a successful lake build checks only that Lean accepts the declarations under the pinned environment. It does not prove that the formal declarations match the manuscript, nor does it validate any unformalized perturbation expansion.

No theorem status in CLAIM_REGISTRY.md is upgraded by the existence of these initial Lean source files.
