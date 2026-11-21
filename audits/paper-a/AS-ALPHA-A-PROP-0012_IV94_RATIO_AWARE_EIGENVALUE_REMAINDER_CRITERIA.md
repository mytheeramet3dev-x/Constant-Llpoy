# IV-94 — Ratio-Aware Eigenvalue Error Criteria for Entropy Remainders

**Status:** ANALYTIC-PARTIAL / CONDITIONAL LEMMA; no reduced-state eigenvalue estimates proved yet.

## Objective
Turn IV-93's uniform-remainder question into explicit eigenvalue error conditions sufficient for a uniform entropy remainder, without assuming an additive error is harmless near zero.

## Notation
Let t=x+y, and use natural logarithms in this note. Define h(p)=-p ln p-(1-p)ln(1-p). The candidate leading MI is
F_nat(x,y)=t ln t-x ln x-y ln y,
with 0 ln 0 :=0. Conversion to bits divides by ln 2.

For the endpoint marginals, write their small eigenvalues p_x and p_y; for the joint endpoint state, write its small eigenvalue q. The leading perturbative targets are p_x=x, p_y=y, q=t.

## Conditional ratio-aware criterion
Suppose for sufficiently small t there are constants C,c independent of x/y such that:
- |p_x-x| <= C x t,
- |p_y-y| <= C y t,
- |q-t| <= C t^2,
and all these eigenvalues remain in [0,1/2].

Then the entropy combination I=h(p_x)+h(p_y)-h(q) has a uniform remainder bounded by O(t^2 log(1/t)) relative to F_nat, as t→0.

### Why the marginal errors must scale with their own leading eigenvalues
For 0<z<=t, the entropy derivative is h'(z)=ln((1-z)/z), so |h'(z)| <= ln(1/z) for z<=1/2. If |p_x-x|<=Cxt, intermediate values remain comparable to x for small t, hence
|h(p_x)-h(x)| <= C' x t (1+ln(1/x)).
Because x<=t and t small, x ln(1/x) is bounded by a constant multiple of t ln(1/t) (up to a fixed constant), giving O(t^2 ln(1/t)). The same applies to y.

For q=t+delta, |delta|<=Ct^2. The mean-value bound gives
|h(q)-h(t)| <= C' t^2 ln(1/t)
for sufficiently small t, since q is comparable to t. Summing yields the stated conditional bound.

## What this conditional lemma does NOT establish
It does not prove that the actual path-3 reduced density matrices satisfy these ratio-aware eigenvalue estimates. Those are the remaining spectral perturbation obligations. Generic additive O(t^2) control on p_x or p_y is insufficient to imply the required relative bounds when x or y is much smaller than t.

## Required derivation for next audit
1. Use symmetries and partial trace structure to show the marginal small eigenvalues vanish at the corresponding zero-edge boundary, and quantify their dependence with factors x and y.
2. For the joint endpoint state, establish q=t+O(t^2) uniformly.
3. Verify positivity and the eigenvalue ordering uniformly near the axes.
4. If a bound fails, record the counterexample and revise the leading term rather than weakening the estimate.

## Status
This note records a conditional analytic implication only. It is not a proof of the criterion for the Hamiltonian, not a verified uniform asymptotic theorem, and does not close Proposition 0012. Paper A remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
