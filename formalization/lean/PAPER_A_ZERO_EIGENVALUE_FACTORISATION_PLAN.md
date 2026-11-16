# Paper A — Zero-Eigenvalue Entropy Factorisation Plan

**Repository:** Constant Llapoy  
**Scope:** Paper A only  
**Status:** Mathematical proof obligations specified; partial Lean lemmas compile. Latest pinned CI (run 43979057358, commit `af6e2eb9515d50801f47dadde7e2ee06a0bd1715`) passed the full Lake build and axiom audit. The factorisation theorem itself remains open.

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

If lambda(0,u0)=0 and lambda >= 0 on a two-sided neighborhood, Fermat's theorem gives partial_r lambda(0,u0)=0. The Lean declaration `hasDerivAt_local_min_branch_eq_zero` formalizes Fermat's theorem under an explicit `IsLocalMin` hypothesis. The conversion from two-sided nonnegativity plus `lambda(0,u0)=0` to `IsLocalMin` is not yet formalized.

That fact alone is insufficient to differentiate -lambda log lambda at the zero branch. A differentiable nonnegative function can vanish to a rate that is too slow for the product with its logarithm to have the desired derivative. The analytic finite-order factorisation (or a stronger explicit modulus estimate) is required.

If the analytic branch is not identically zero in r, its first nonzero Taylor order at an interior two-sided nonnegative zero must be even and its leading coefficient positive. The case where every Taylor coefficient vanishes corresponds locally to an identically zero analytic branch and must be handled separately.

## 4. Uniformity and stratification risks

A pointwise order m at u0 does not automatically give a uniform order on an arbitrary neighborhood in u. If the leading coefficient g(0,u) vanishes at nearby parameter values, the order can change. The formal proof must either:

1. restrict to a parameter stratum where the leading coefficient is uniformly bounded below by a positive constant; or
2. stratify the parameter set by vanishing order and prove the required estimate on each stratum.

No uniform-in-u, uniform-in-N, or global-in-coupling conclusion may be inferred before those hypotheses are established.

## 5. Lean decomposition

The planned proof is split into independently reviewable obligations:

- **ZF-1:** formalize the local power-series coefficient representation for the real-analytic branch. This is the next mathematical formalization target; do not assume a fixed order m without proving or explicitly stratifying it.
- **ZF-2:** prove the first nonzero order is even at a two-sided nonnegative zero.
- **ZF-3:** factor r^m and prove continuity/analyticity of the quotient g.
- **ZF-4:** establish compact-neighborhood lower and upper bounds for g.
- **ZF-5:** establish the differentiated coefficient bound for partial_u g.
- **ZF-6:** derive the two-sided logarithmic control for lambda from the proved lower/upper factorisation bounds; do not assume the log-control bound independently in the final application.
- **ZF-7:** discharge the hypotheses of entropy_derivative_bound_of_log_control.
- **ZF-8:** treat the identically-zero branch separately and prove the entropy contribution is identically zero there.
- **ZF-9:** verify the resulting estimates match the exact eigenvalue branches and edge derivative in the frozen Paper A manuscript.

Each obligation requires its own assumptions, constants, domains, and proof. None is marked complete by the current positive-branch algebraic lemma.
