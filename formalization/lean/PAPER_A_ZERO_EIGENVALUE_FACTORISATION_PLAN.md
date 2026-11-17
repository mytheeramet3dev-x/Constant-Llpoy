# Paper A — Zero-Eigenvalue Entropy Factorisation Plan

**Repository:** Constant Llapoy  
**Scope:** Paper A only  
**Status:** Partial Lean formalization verified. Latest pinned CI (run 43983006064, commit `e4129b888a7ffe1bc00028fe23e840b83ed5f087`) passed the pinned Lean/Mathlib build and configured axiom audit. The analytic finite-order factorization wrapper and the nonnegative-branch-to-local-minimum lemma compile. The parity/positive-leading-coefficient theorem and the entropy derivative at the zero branch remain open. `lake test` and `lake lint` were not run.

## 1. Target statement

Let lambda(r,u) be a nonnegative real-analytic eigenvalue branch near (0,u0), with r the endpoint parameter and u an edge-response parameter. For a fixed stratum on which the first nonzero order in r is m, the intended local factorisation is

    lambda(r,u) = r^m g(r,u),   g(0,u0) > 0.

After shrinking to a compact parameter neighborhood, the proof must establish constants c,C > 0 such that, for 0 < r < r0,

    c r^m <= lambda(r,u) <= C r^m,
    |partial_u lambda(r,u)| <= C r^m.

The first pair of inequalities is essential: an upper bound alone does not control |log lambda|. The derivative estimate follows only after proving the factorisation with a sufficiently regular coefficient g, and bounding g and partial_u g on the chosen compact neighborhood.

## 2. Entropy derivative consequence

For lambda > 0,

    partial_u[-lambda log lambda]
      = -(1 + log lambda) partial_u lambda.

The two-sided comparison gives

    |log lambda(r,u)| <= C0 + m |log r|

for a constant C0 on the selected neighborhood. Combining it with
|partial_u lambda| <= C r^m yields

    |partial_u[-lambda log lambda]|
      <= C1 r^m(1 + |log r|).

The Lean module ZeroEigenvalueEntropy.lean currently formalizes the chain rule and final algebraic implication from explicit logarithmic-control and derivative-bound hypotheses. It does not derive these hypotheses from analyticity. The module compiles under the pinned toolchain; the successful axiom audit is a declaration-level audit, not a second proof checker.

## 3. Why the zero branch needs a separate argument

If lambda(0,u0)=0 and lambda >= 0 on a two-sided neighborhood, Fermat's theorem gives partial_r lambda(0,u0)=0. The Lean declarations `hasDerivAt_local_min_branch_eq_zero` and `hasDerivAt_nonnegative_branch_eq_zero` formalize Fermat's theorem and the conversion from two-sided eventual nonnegativity plus a zero value to `IsLocalMin`.

That fact alone is insufficient to differentiate -lambda log lambda at the zero branch. A differentiable nonnegative function can vanish to a rate that is too slow for the product with its logarithm to have the desired derivative. The analytic finite-order factorisation (or a stronger explicit modulus estimate) is required.

If the analytic branch is not identically zero in r, its first nonzero Taylor order at an interior two-sided nonnegative zero must be even and its leading coefficient positive. The case where every Taylor coefficient vanishes corresponds locally to an identically zero analytic branch and must be handled separately.

## 4. Uniformity and stratification risks

A pointwise order m at u0 does not automatically give a uniform order on an arbitrary neighborhood in u. If the leading coefficient g(0,u) vanishes at nearby parameter values, the order can change. The formal proof must either:

1. restrict to a parameter stratum where the leading coefficient is uniformly bounded below by a positive constant; or
2. stratify the parameter set by vanishing order and prove the required estimate on each stratum.

No uniform-in-u, uniform-in-N, or global-in-coupling conclusion may be inferred before those hypotheses are established.

## 5. Lean decomposition

The planned proof is split into independently reviewable obligations:

- **ZF-1:** formalize the finite-order local factorization for a nontrivial real-analytic one-variable branch. Partially discharged by `exists_local_power_factorization_of_analytic_nontrivial`, which wraps the pinned Mathlib isolated-zero theorem and returns analytic `g`, `g(0) ≠ 0`, and eventual equality `f(r)=r^m g(r)`. This is not yet a coefficient-by-coefficient Taylor development, nor does it use nonnegativity.
- **ZF-2:** prove the first nonzero order is even and the leading coefficient is positive at a two-sided nonnegative zero. OPEN; this is the next target.
- **ZF-3:** factor `r^m` and prove regularity of the quotient `g`. Analyticity of `g` is supplied by the ZF-1 wrapper at a single base point; the remaining work is to connect the factorization to the model's joint `(r,u)` branch and uniform parameter estimates.
- **ZF-4:** establish compact-neighborhood lower and upper bounds for g.
- **ZF-5:** establish the differentiated coefficient bound for partial_u g.
- **ZF-6:** derive the two-sided logarithmic control for lambda from the proved lower/upper factorisation bounds; do not assume the log-control bound independently in the final application.
- **ZF-7:** discharge the hypotheses of entropy_derivative_bound_of_log_control.
- **ZF-8:** treat the identically-zero branch separately and prove the entropy contribution is identically zero there.
- **ZF-9:** verify the resulting estimates match the exact eigenvalue branches and edge derivative in the frozen Paper A manuscript.

Each obligation requires its own assumptions, constants, domains, and proof. None is marked complete by the current positive-branch algebraic lemma.


## 6. Latest verified Lean state

At commit `e4129b888a7ffe1bc00028fe23e840b83ed5f087`, CI run [43983006064](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/43983006064) completed successfully. Its only job, “Pinned Lean and Mathlib build”, completed the build and configured axiom audit successfully. This run did not execute `lake test` or `lake lint`.

The module now contains:
- `exists_local_power_factorization_of_analytic_nontrivial`: finite-order factorization for a nontrivial analytic branch in one real variable;
- `hasDerivAt_nonnegative_branch_eq_zero`: derivative of a differentiable branch is zero if it vanishes and is eventually nonnegative on a two-sided neighborhood;
- the positive-branch entropy chain-rule and conditional logarithmic derivative bound.

The first item does not establish that `m` is even or `g 0 > 0). The second item concerns only the eigenvalue branch, not the entropy function at its zero. Do not infer the zero-branch entropy derivative from it.
