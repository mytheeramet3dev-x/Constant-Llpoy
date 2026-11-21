# PROP-0012 IV-18 — Entropy Branch Logarithmic Remainder Audit

Date: 2026-11-21
Claim: AS-ALPHA-A-PROP-0012
Scope: Fixed finite N, local weak coupling r=J/h, edge-coordinate differentiation, entropy contributions from small eigenbranches.

## Questions audited

1. Does an eigenvalue bound \(\lambda=O_N(r^4)\) alone control its edge derivative?
2. Does that bound alone justify the entropy derivative estimate \(O_N(r^4(1+|\ln r|))\)?
3. What branch-scale hypotheses are sufficient, and what happens when the leading coefficient vanishes?
4. Are trace normalization and derivative constants handled correctly?

## Findings

**Finding 1 — eigenvalue order alone is insufficient.** A pointwise statement \(\lambda=O(r^4)\) does not imply \(\partial_u\lambda=O(r^4)\) for an edge coordinate \(u\). The differentiated order requires a joint expansion/regularity estimate, such as \(\lambda=r^4 a(u,r)\) with bounded \(\partial_u a\), or an independently established derivative bound. IV-16/17 support-order reasoning is relevant but must be connected to the actual normalized branch and coordinate.

**Finding 2 — logarithmic scale matters.** If \(\lambda=r^4a(u,r)\), with \(a\) and \(\partial_u a\) bounded and \(a\ge a_0>0\) on the local domain, then \(|\ln\lambda|=O(1+|\ln r|)\) and
\[
\partial_u[-\lambda\ln\lambda]=-(1+\ln\lambda)\partial_u\lambda
=O_N(r^4(1+|\ln r|)).
\]
Thus the desired entropy-derivative remainder follows with the positive-scale hypothesis.

**Finding 3 — zero leading coefficient needs a separate local argument.** At a parameter point where a differentiable nonnegative eigenbranch is exactly zero in an interior edge parameter, its first derivative in that parameter is zero. That pointwise fact does not by itself give a uniform neighborhood estimate for \(\lambda\ln\lambda\). A local analytic/Puiseux branch description, its nonnegative structure, and derivative control are needed. In the analytic nonnegative setting, finite-order zeros can be handled by factoring the vanishing scale and controlling the derivative-times-log expression; an identically zero branch contributes zero. This audit does not establish that factorization for every branch in the frozen manuscript.

**Finding 4 — trace normalization constant cancellation.** For positive eigenvalues, differentiating entropy gives \(-\sum_i(1+\ln\lambda_i)\lambda_i'\). Since trace is fixed, \(\sum_i\lambda_i'=0\), the additive \(-1\) constants cancel in the complete branch sum. This does not permit dropping constants from an isolated branch before the complete trace-normalized sum is assembled.

**Finding 5 — large eigenbranch.** If \(\lambda_L=1-O(r^2)\) and \(\lambda_L'=O(r^2)\), then the trace-cancelled term \(-\ln\lambda_L\,\lambda_L'\) is \(O(r^4)\), since \(\ln\lambda_L=O(r^2)\). This remains conditional on the branch expansions.

## Disposition

IV-18 **CONDITIONAL PASS / GAP IDENTIFIED**: the positive-scale case gives the claimed logarithmic entropy-derivative order when both the branch factorization and edge derivative are controlled. The \(O(r^4)\) eigenvalue order by itself is not enough. The zero-leading-coefficient case needs a separate analytic factorization/uniform estimate; pointwise nonnegativity and a zero derivative at the exact zero are not a substitute for that neighborhood control.

No source convention reconciliation, exact frozen-source branch factorization, mechanical Taylor recurrence check, Lean formalization/build, or global \(B-C>0\) theorem is claimed. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
