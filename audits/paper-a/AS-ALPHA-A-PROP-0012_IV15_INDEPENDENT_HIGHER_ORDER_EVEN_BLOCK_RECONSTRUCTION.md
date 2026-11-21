# PROP-0012 IV-15 — Independent Higher-Order Reconstruction of the Even Block

**Date:** 2026-11-21  
**Scope:** Adversarial order counting of second-order overlapping pair-flip paths in the two-site even-parity block, including the Schur/determinant cancellation and first edge derivatives.  
**Disposition:** ANALYTIC-PARTIAL PASS for the order-counting/cancellation algebra, conditional on the pair-flip Taylor-support lemma and local analytic eigenvector setup. Not a mechanized proof.

## 1. Environment indexing and amplitude order

For the reduced pair (1,2), let E be an even flip set in the environment {3,...,N}. The two relevant amplitudes in the even block are c_E and c_{E∪{1,2}}. Pair-flip perturbation theory changes the x-basis flip set by two sites per interaction. Thus the minimal perturbation order for a set F is at least |F|/2 when F is even, with fixed finite N and analytic perturbation expansion.

For nonempty E, |E|≥2:
- c_E=O_N(r) when |E|=2, and more generally O_N(r^{|E|/2});
- c_{E∪{1,2}}=O_N(r^2) for |E|=2, and generally O_N(r^{(|E|+2)/2}).

The first edge derivatives in any fixed u_e preserve these r-orders: differentiating Taylor coefficients does not reduce perturbation order. This order-support statement remains conditional on the pair-flip recursion/induction being fully checked.

## 2. Direct tail orders

Write the exact environment sums
\[
L=A+R_L,\quad X=x_0+R_X,\quad S=s_0+R_S,
\]
where A=|c_empty|^2, x_0=c_empty\overline{c_{12}}, and s_0=|c_{12}|^2. The nonempty environment terms obey:
\[
R_L=O_N(r^2),\quad R_X=O_N(r^3),\quad R_S=O_N(r^4),
\]
and their first edge derivatives have the same orders.

The potentially dangerous overlapping second-order path is explicitly represented by c_{12}: it may differ from its first-order value by O_N(r^2). This does not break cancellation, because the same exact c_{12} is used in x_0 and s_0. We do not replace it by a truncated amplitude in the cancellation.

## 3. Exact Schur cancellation with a shared amplitude

Consider
\[
D=S-|X|^2/L.
\]
Ignoring nonempty environments, D is exactly zero:
\[
s_0-|x_0|^2/A=|c_{12}|^2-
\frac{|c_empty|^2|c_{12}|^2}{|c_empty|^2}=0.
\]
With tails included,
\[
D=R_S-\frac{|x_0+R_X|^2}{A+R_L}
+|c_{12}|^2.
\]
The normalization denominator A remains bounded away from zero near r=0. The correction from replacing A by A+R_L in the shared-amplitude term is O_N(|c_12|^2 R_L)=O_N(r^4). The cross term x_0\overline{R_X} is O_N(r·r^3)=O_N(r^4), and |R_X|^2 is O_N(r^6). R_S is O_N(r^4). Therefore
\[
D=O_N(r^4).
\]
Differentiating the exact expressions in a fixed edge direction gives the same orders (derivative of c_12 is O_N(r), derivative of R_X is O_N(r^3), derivative R_L is O_N(r^2), derivative R_S is O_N(r^4)); product-rule terms remain O_N(r^4). Thus \partial_{u_e}D=O_N(r^4), conditionally on the amplitude-order derivative lemma.

For the positive even block, its large eigenvalue remains bounded away from zero. The determinant identity \lambda_s=\det(M)/\lambda_L, together with det(M)=L D, then gives the small eigenbranch and first edge derivatives O_N(r^4).

## 4. Adversarial outcome

No second-order overlapping pair-flip path found that creates an O(r^2) or O(r^3) small eigenbranch: the empty-environment contribution is rank one and uses the exact shared amplitude; nonempty environments enter the Schur residual only at fourth order. The argument is robust against c_12=a_12+O(r^2), precisely because the cancellation uses c_12 without truncation.

This conclusion is conditional and fixed-N. The induction/support estimate and differentiated coefficients have not been independently mechanized, all branch-scale/logarithm requirements for entropy derivatives are not closed in this report, and frozen-source reconciliation is still unavailable.

## 5. Status

IV-15 is a conditional analytic order-counting/cancellation PASS. It does **not** upgrade PROP-0012. Still open: frozen manuscript-source reconciliation, independent mechanical verification of the amplitude support induction, full higher-order entropy-branch remainder closure and small-branch logarithmic scale, Lean formalization/build, and any global B-C sign theorem.

**PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
