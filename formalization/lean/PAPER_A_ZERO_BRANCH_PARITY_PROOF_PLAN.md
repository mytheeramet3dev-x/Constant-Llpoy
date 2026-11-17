# Paper A — ZF-2: Parity and Positive Leading Coefficient

**Repository:** Constant Llapoy  
**Scope:** Paper A, one-variable local branch only  
**Status:** BUILD_VERIFIED; AXIOM_AUDITED — the complete ZF-2 conclusion is formalized in `ZeroEigenvalueEntropy.lean` and passed pinned CI run `43998392546` at commit `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`. The workflow's Lean build and configured axiom audit succeeded. `lake test` and `lake lint` were not run.

## Target

Let (f,g:\mathbb R\to\mathbb R), (m\in\mathbb N), and suppose:

1. (f) is nonnegative on a two-sided neighborhood of (0);
2. (f(r)=r^m g(r)) on a neighborhood of (0);
3. (g) is continuous at (0);
4. (g(0)\ne0).

The intended conclusion is:

[
m\text{ is even},\qquad g(0)>0.
]

This is a local one-variable statement. It does not yet establish joint uniformity in an edge parameter (u).

## Proof structure

**A. Preserve the exact factorization.** Use the factorization returned by
`exists_local_power_factorization_of_analytic_nontrivial`; do not replace eventual equality with a global identity.

**B. Determine the sign of (g(0)).** Since (g(0)\ne0) and (g) is continuous at zero, its sign is constant on a sufficiently small neighborhood. If (g(0)<0), choose a sufficiently small positive (r). Then (r^m>0), so (r^m g(r)<0), contradicting (f(r)\ge0). Thus (g(0)>0).

**C. Determine the parity of (m).** Continuity and (g(0)>0) imply (g(r)>0) for all sufficiently small positive and negative (r). Choose a sufficiently small negative (r). Since
[
0\le f(r)=r^m g(r),\qquad g(r)>0,
]
we obtain (r^m\ge0). A negative real number has a nonnegative (m)-th power only when (m) is even.

## Lean decomposition

Formalize the proof as separate lemmas so each filter and sign argument is reviewable:

- **ZF-2a:** continuity plus (g(0)\ne0) gives a neighborhood on which (g) has the same strict sign as (g(0)).
- **ZF-2b:** if (f\ge0) near zero, (f(r)=r^m g(r)) near zero, and (g(0)\ne0), then (g(0)>0), using a positive witness in the neighborhood.
- **ZF-2c:** if (g>0) near zero and (f\ge0) near zero with the factorization, then (m) is even, using a negative witness.
- **ZF-2d:** combine the previous lemmas into the target theorem.

Do not hide the positive/negative witness construction inside an unproved assumption. Verify the exact pinned Mathlib filter APIs before using them. If a helper lemma is not yet formalized, record it as open rather than weakening the theorem.

## Boundaries

- The analytic factorization theorem currently in Lean supplies (g) analytic and (g(0)\ne0), but not the sign or parity conclusions.
- The nonnegative-branch derivative theorem is not a substitute for ZF-2.
- The conclusion is pointwise in the base parameter. It does not establish a common order (m), a uniform positive lower bound for (g(0,u)), or compact-neighborhood estimates in (u).
- The identically-zero analytic branch is excluded by the nontriviality assumption and must be handled separately under ZF-8.
- No entropy derivative at the zero branch is claimed by this document.


## Verified Lean declarations

- `eventually_pos_of_continuousAt_of_pos`: continuity preserves positivity near zero.
- `eventually_neg_of_continuousAt_of_neg`: continuity preserves negativity near zero.
- `positive_leading_coefficient_of_nonnegative_factorization`: nonnegativity plus a local factorization and a nonzero continuous quotient force (g(0)>0).
- `even_order_of_negative_factorization_witness`: the negative-side algebraic parity contradiction.
- `even_order_and_positive_leading_coefficient_of_nonnegative_factorization`: combines the positive and negative witness constructions to conclude `Even m ∧ 0 < g 0`.

**Evidence:** commit `0c4f6ed29e8ef20d8870d6d9e60c9b8c104ec133`; CI run [43998392546](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/43998392546), job `Pinned Lean and Mathlib build`, including the configured axiom audit.

## Exact scope of the verified result

The combined theorem takes eventual nonnegativity, eventual factorization, continuity of (g) at zero, and (g(0)\ne0) as explicit hypotheses. The analytic factorization theorem can supply the factorization and nonzero quotient for a nontrivial analytic branch, but the full application still requires passing those outputs and the branch's nonnegativity into the combined theorem. No joint parameter-uniform order or lower bound is established here.


## ZF-3a — Scalar quotient bounds (verified)

The declaration `eventually_quotient_two_sided_bounds` in
`ZeroEigenvalueEntropy.lean` proves that if `g` is continuous at zero and
`g 0 > 0), then on some neighborhood of zero,

[
g(0)/2 < g(r) < 3g(0)/2.
]

This is a scalar continuity estimate for the quotient only. It does not yet
multiply the estimate through the factorization `f(r)=r^m g(r)`, establish
bounds for `f`, prove a derivative bound, or establish uniformity in an
auxiliary parameter.

**Evidence:** commit `d6a92c2e032e10eb8764754d875cc18b145024e3`,
CI run [44003303543](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44003303543).
The sole workflow job completed the pinned Lean/Mathlib build and configured
axiom audit successfully. `lake test` and `lake lint` were not run.

**Next obligations:** combine the quotient estimate with the even-order
factorization on the correct one-sided or two-sided domain; then prove the
differentiated coefficient estimate and the two-sided logarithmic control
needed by the positive-branch entropy derivative lemma.
