# PROP-0012 IV-14 — Direct Reduced-Matrix Reconstruction from Perturbative Ground-State Amplitudes

**Date:** 2026-11-21  
**Scope:** Reconstruct one-site and two-site reduced density matrices directly from perturbative ground-state amplitudes; check leading eigenbranches and edge derivatives without relying on the prior branch ledger.  
**Disposition:** PASS for direct leading-order matrix reconstruction; higher-order remainder closure is NOT independently established.

## 1. Setup

Use the transverse-field Ising convention
\[
H_0=-h\sum_i\sigma_i^x,\qquad r=J/h,
\]
and the unperturbed state \(|\emptyset\rangle\) in the x-spin-flip representation. A pair flip has gap \(4h\), so the first-order pair amplitude is
\[
a_{ij}=J_{ij}/(4h)=r(1+u_{ij})/4.
\]
The sign convention of the amplitude does not affect the leading probabilities or eigenvalues below.

## 2. One-site reduced matrix

Tracing all sites except \(i\), parity removes off-diagonal terms at the displayed leading order. The small eigenvalue is the probability that site \(i\) is flipped:
\[
p_i=\sum_{j\ne i}|a_{ij}|^2+O_N(r^3).
\]
At the uniform point,
\[
p_i=(N-1)r^2/16+O_N(r^3).
\]
The edge \(13\) contributes to \(p_1\), but not to \(p_2\), hence
\[
\partial_{u_{13}}p_1=r^2/8+O_N(r^3),\quad
\partial_{u_{13}}p_2=O_N(r^3).
\]
The disjoint edge \(34\) gives
\[
\partial_{u_{34}}p_1=O_N(r^3),\quad
\partial_{u_{34}}p_2=O_N(r^3).
\]
This reproduces the one-site leading coefficients by direct probability tracing.

## 3. Two-site odd-parity block

In basis \((|+-\rangle,|-+\rangle)\), environmental states are orthogonal. Explicit trace over environment gives the leading Gram matrix
\[
M_{\rm odd}=
\begin{pmatrix}
\sum_{k\ge3}|a_{2k}|^2 & \sum_{k\ge3}a_{2k}\overline{a_{1k}}\\
\sum_{k\ge3}a_{1k}\overline{a_{2k}} & \sum_{k\ge3}|a_{1k}|^2
\end{pmatrix}+O_N(r^3).
\]
At uniform coupling,
\[
M_{\rm odd}=\frac{N-2}{16}r^2
\begin{pmatrix}1&1\\1&1\end{pmatrix}+O_N(r^3),
\]
with leading eigenvalues \(q=(N-2)r^2/8\) and zero. Direct differentiation of the leading Gram entries yields
\[
\partial_{u_{13}}q=r^2/8+O_N(r^3),\quad
\partial_{u_{34}}q=O_N(r^3).
\]
Thus the odd positive-branch coefficient is confirmed from direct matrix reconstruction.

## 4. Two-site even-parity block

Direct environment tracing gives
\[
L=\sum_E|c_E|^2,\quad X=\sum_Ec_E\overline{c_{E\cup\{1,2\}}},\quad
S=\sum_E|c_{E\cup\{1,2\}}|^2.
\]
The empty-environment terms \((|c_\emptyset|^2,c_\emptyset\overline{c_{12}},|c_{12}|^2)\) form a rank-one outer product and therefore have zero determinant. Nonempty environments determine the residual determinant.

This confirms the shared-amplitude cancellation structure, but this pass does **not** independently prove all higher-order overlapping-path amplitude coefficients, the pair-flip Taylor-support induction, differentiated tail estimates, or the positive small-branch logarithmic scale. The conditional \(O_N(r^4)\) small-even-branch estimate is not promoted to an unconditional result here.

## 5. Checks

- One-site coefficient \((N-1)/16\): count the \(N-1\) incident pair amplitudes.
- Odd positive branch \((N-2)/8\): count \(N-2\) environment sites and diagonalize the rank-one leading Gram matrix.
- Adjacent edge 13 yields derivative coefficient \(1/8\); disjoint edge 34 is absent from this leading block.
- Full entropy-derivative bookkeeping is not rederived in this leading-matrix audit.

## 6. Open obligations

Fixed finite \(N\), local weak coupling only. This is an independent reconstruction of leading reduced-matrix entries/eigenbranches, not an all-orders reduced-density proof.

Remaining: frozen-source reconciliation; mechanically checked pair-flip support/derivative induction; higher-order reduced-matrix remainders for every branch; small even-branch logarithmic scale control; Lean formalization/build; and any global \(B-C\) sign theorem.

**PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
