# PROP-0012 — Complete Entropy-Branch Bookkeeping Audit

**Date:** 2026-11-21  
**Scope:** Fixed finite N >= 4, weak coupling r=J/h -> 0+, first independent real-edge directional derivatives at the uniform point. Paper-level analytic bookkeeping; no Lean formalization/build.

## Goal

Check that all eigenvalue branches in the one-site and two-site entropies are accounted for, including the even-block large eigenvalue near 1, and identify what this closes versus what remains conditional.

## 1. Entropy derivative identity and trace cancellation

For a positive eigenvalue branch λ, the entropy term derivative is
\[
\frac{d}{du}[-\lambda\ln\lambda]=-(1+\ln\lambda)\lambda'.
\]
For a normalized reduced density matrix, \(\sum_j\lambda_j=1\), so \(\sum_j\lambda_j'=0\). Consequently the total entropy derivative may be written
\[
S'=-\sum_j(\ln\lambda_j)\lambda_j',
\]
for positive branches, with zero branches handled by the nonnegative analytic directional-derivative lemma rather than by evaluating \(\ln0\). This trace identity is essential: bounding the large branch using its raw \(-(1+\ln\lambda_L)\lambda_L'\) term without cancellation would leave an artificial order-\(r^2\) constant contribution.

## 2. Even-block large branch

The \((++,--)\) block has entries \(L=1+O_N(r^2)\), \(X=O_N(r)\), and \(S=O_N(r^2)\), with the corresponding first edge derivatives at these orders. The branch near one satisfies
\[
\lambda_L=1-O_N(r^2),\quad \lambda_L'=O_N(r^2).
\]
Therefore \(\ln\lambda_L=O_N(r^2)\), and its trace-cancelled entropy contribution is
\[
-(\ln\lambda_L)\lambda_L'=O_N(r^4).
\]
This follows from the analytic 2x2 eigenvalue formula/local simple-branch perturbation at the isolated eigenvalue 1 and the stated entry/derivative orders. The estimate is fixed-N.

## 3. Even-block small branch

The environment-resolved pair-flip argument and Schur/determinant integration report the candidate
\[
\lambda_s,\;\lambda_s'=O_N(r^4).
\]
For a positive branch whose first nonzero analytic coefficient at the reference point is finite and positive, \(|\ln\lambda_s|=O_N(1+|\ln r|)\), hence its entropy derivative is \(O_N(r^4(1+|\ln r|))\). If it vanishes at the reference for all sufficiently small r, its first directional derivative is zero by nonnegativity and an interior minimum. This remains conditional on validating the branch-scale/zero-branch alternative for the exact frozen source.

## 4. Odd-block branches

- Positive branch \(q=r^2Q_+(u)+O_N(r^3)\), with \(Q_+(0)=(N-2)/8>0\) and differentiated expansion, contributes the already-audited leading term and remainder \(O_N(r^3(1+|\ln r|))\).
- The other branch is nonnegative and zero at the symmetric reference point; its first real edge-direction entropy derivative is zero under the analytic interior-minimum lemma. No uniform-in-N or higher-derivative assertion is made.

## 5. One-site entropy branches

For each one-site small eigenvalue \(p_i=(N-1)r^2/16+O_N(r^3)\), first edge derivatives have the audited orders. Its binary entropy derivative is exactly \(H'(p_i)p_i'\), yielding the previously recorded leading logarithmic contrast and remainder at fixed N.

## 6. Integrated bookkeeping result

Under the analytic branch estimates above, the large even branch and even small branch contribute no term at the leading \(r^2\) logarithmic scale to the edge contrast. Combining the one-site terms and odd positive branch retains the previously derived conditional leading formula
\[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\!\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right).
\]
The leading coefficient is positive for fixed N >= 4.

## Verdict and boundaries

**ENTROPY BRANCH BOOKKEEPING — ANALYTICALLY CLOSED AT THE CLAIMED FIXED-N ORDERS, CONDITIONAL.** The trace cancellation for the large branch is now explicit, and all entropy branches have an assigned derivative order/zero-branch treatment.

This does **not** promote full PROP-0012 to PASS. Remaining obligations include exact frozen-source reconciliation (currently blocked by unavailable frozen ref), independently verifying the analytic amplitude recursion and branch-scale conditions against that source, formal Lean proof/build, independent review, and the manuscript's global sign claim. No global \(B-C>0\) theorem is established.
