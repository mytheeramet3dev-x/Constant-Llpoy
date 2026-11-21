# PROP-0012 — Leading Log Coefficient and Entropy Constant Cancellation Check

**Date:** 2026-11-21  
**Scope:** Fixed finite N >= 4, uniform weak-coupling reference r=J/h -> 0+, leading edge-contrast algebra only. Independent algebraic cross-check of the branch-bookkeeping formula; no source reconciliation and no Lean build.

## 1. Leading small eigenvalues and edge derivatives

Use the audited leading quantities
\[
p=\frac{N-1}{16}r^2,\qquad q=\frac{N-2}{8}r^2,
\]
with the adjacent-edge direction at the uniform point
\[
\partial_{u_{13}}p_1=\frac{r^2}{8},\qquad
\partial_{u_{13}}q=\frac{r^2}{8},
\]
and disjoint-edge derivatives plus the other one-site derivatives contributing only at higher order to the contrast. Here \(J_e=J(1+u_e)\), so \(\partial_{J_e}=J^{-1}\partial_{u_e}\) at the reference.

## 2. One-site entropy leading term

For binary entropy \(H(p)=-p\ln p-(1-p)\ln(1-p)\),
\[
H'(p)=\ln\frac{1-p}{p}=-\ln p+O(p).
\]
Thus the leading adjacent-minus-disjoint one-site entropy derivative is
\[
\frac{r^2}{8}(-\ln p)+O_N(r^3(1+|\ln r|)).
\]

## 3. Two-site entropy: trace-normalized branch cancellation

For normalized \(\rho_{12}\), \(\sum_j\lambda_j'=0\). Therefore, for positive branches and with zero branches treated by the analytic directional lemma,
\[
S'(\rho_{12})=-\sum_j(1+\ln\lambda_j)\lambda_j'
=-\sum_j\ln\lambda_j\,\lambda_j'.
\]
The even large branch near 1 contributes only at order \(O_N(r^4)\) after this cancellation. The odd positive branch supplies the leading logarithmic derivative; zero branches have zero first directional entropy derivative at the symmetric reference under the audited interior nonnegative-branch condition. Hence the leading adjacent-minus-disjoint two-site entropy derivative is
\[
-\frac{r^2}{8}\ln q+O_N(r^3(1+|\ln r|)).
\]
No isolated \(+1\) remains in the leading term. This explicitly verifies the constant cancellation rather than relying on informal term-by-term entropy differentiation.

## 4. Mutual-information contrast

Subtracting the two-site entropy derivative from the one-site entropy derivative gives
\[
\partial_{u_{13}}I_{12}-\partial_{u_{34}}I_{12}
=\frac{r^2}{8}\ln\frac{q}{p}
+O_N(r^3(1+|\ln r|)).
\]
Since
\[
\frac qp=\frac{2(N-2)}{N-1}>1\quad(N\ge4),
\]
and converting to physical edge derivatives yields
\[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\!\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right).
\]
The coefficient and sign of the local leading term are algebraically consistent and positive for fixed N >= 4.

## Verdict

**LEADING LOG COEFFICIENT / CONSTANT CANCELLATION — ALGEBRAIC CROSS-CHECK PASS, CONDITIONAL.** This confirms the leading coefficient once the branch and derivative estimates are granted. It is not an independent source reconciliation, formal verification, or proof of global \(B-C>0\). Full PROP-0012 stays OPEN.
