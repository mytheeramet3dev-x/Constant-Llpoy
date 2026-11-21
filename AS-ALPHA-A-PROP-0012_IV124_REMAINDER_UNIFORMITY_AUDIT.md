# IV-124 — Uniform Remainder Control for the Entropy Difference

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** Uniformity audit identifies two different regimes. The previously quoted O(epsilon^6 |ln epsilon|) remainder is justified only away from probability-zero parameter axes unless stronger structure is proved. A uniform near-axis bound is weaker.

## 1. Regime away from axes

Fix a compact parameter set K on which S=A^2+B^2 is bounded below by s0>0, and assume the eigenvector/probability expansions are analytic with uniform derivative bounds there. Then
q=epsilon^2 S+epsilon^4 T+epsilon^6 U(epsilon,A,B),
q3=epsilon^2 R+epsilon^4 T3+epsilon^6 U3,
with U,U3 uniformly bounded and with R bounded below if the q3 entropy is expanded in the same logarithmic way.

Taylor expansion of h at q0=epsilon^2 S is legitimate because q0 is bounded away from zero relative to epsilon^2, and h'''(x)=O(x^{-2}) for small positive x. The induced probability perturbation is O(epsilon^4), so the second-order Taylor error is O(epsilon^8 * epsilon^{-4})=O(epsilon^4); more carefully, to extract the epsilon^4 coefficient with remainder O(epsilon^6 |ln epsilon|), one must include the epsilon^6 probability coefficient and corresponding entropy terms. Thus the expansion truncated at epsilon^4 does **not** by itself establish an O(epsilon^6 |ln epsilon|) remainder unless the probability expansion is known through epsilon^6 and the Taylor bookkeeping includes it.

For the entropy expansion with probability known through epsilon^4 and an O(epsilon^6) probability error, on such a compact set the remainder after the displayed epsilon^4 terms is O(epsilon^6 |ln epsilon|), under uniform coefficient bounds.

## 2. Near axes / vanishing probabilities

As S or R approaches zero, logarithmic derivatives of h diverge. The constants in the away-from-axis Taylor argument depend on the lower bound for S (or R) and cannot be claimed uniform as that bound tends to zero.

A basic global modulus bound is available: for probabilities x,y in [0,1/2], |h(x)-h(y)| is bounded by a constant times |x-y| (1+|ln |x-y||). Thus an O(epsilon^4) probability perturbation alone gives at best an O(epsilon^4 |ln epsilon|) entropy perturbation uniformly near axes—not the claimed O(epsilon^6 |ln epsilon|) remainder.

Axis cases must be handled separately using exact reductions, and shrinking neighborhoods of axes require a matched or direct estimate.

## 3. Audit verdict

- IV-119's remainder statement is not a uniform-in-(A,B) claim as written; it needs a parameter-domain qualifier.
- IV-124 does not prove uniform positivity of the full entropy difference.
- A rigorous next step is to derive a compact-away-from-axes theorem with explicitly stated constants, then separately analyze axis and near-axis regimes.
- No proposition closure or Lean proof is claimed.
