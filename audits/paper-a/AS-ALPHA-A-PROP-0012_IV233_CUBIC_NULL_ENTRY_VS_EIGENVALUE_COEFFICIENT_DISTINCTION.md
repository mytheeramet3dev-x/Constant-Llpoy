# IV-233 — Cubic Null Entry Versus Cubic Eigenvalue Coefficient

**Date:** 2026-11-23  
**Target:** IV-232 single-edge perturbation \(g_{13}=1+u\)  
**Status:** PERTURBATIVE BOOKKEEPING CORRECTION / FULL EIGENVALUE CUBIC COEFFICIENT OPEN / NOT LEAN-FORMALIZED

## 1. Correction and scope

IV-232 correctly computes the cubic coefficient of the odd-block null-direction diagonal entry in the common/null basis:
\[
Q_3(u)=-u^2/32
\]
under its stated first- and second-order amplitude formulas.

This is **not automatically the cubic coefficient of the smallest eigenvalue**. For a symmetric block
\[
O=\begin{pmatrix}L&t\\t&s\end{pmatrix},
\]
the small eigenvalue is controlled by the Schur complement \(s-t^2/L\). If \(L=O(r^2)\), \(t=t_2r^2+t_3r^3+\cdots\), and \(s=s_2r^2+s_3r^3+\cdots\), then \(t^2/L\) contributes at orders \(r^2\) and \(r^3\), including cross terms between \(t_2\) and \(t_3\), and corrections from \(L\)'s expansion. Thus cubic eigenvalue bookkeeping must include all these pieces, not just \(s_3\).

## 2. Required expansion

Write
\[
L=r^2(L_0+rL_1+\cdots),\quad
t=r^2(t_0+rt_1+\cdots),\quad
s=r^2(s_0+rs_1+\cdots).
\]
Then
\[
\frac{t^2}{L}=r^2\frac{t_0^2}{L_0}
+r^3\left(\frac{2t_0t_1}{L_0}
-\frac{t_0^2L_1}{L_0^2}\right)+O(r^4),
\]
assuming \(L_0>0\). Consequently,
\[
S=s-\frac{t^2}{L}
\]
has cubic coefficient
\[
s_1-\frac{2t_0t_1}{L_0}
+\frac{t_0^2L_1}{L_0^2}.
\]
Here subscripts denote coefficients in the displayed \(r\)-series, not derivatives. A corresponding eigenvalue expansion requires accounting for the difference between the Schur complement and the eigenvalue, which begins with higher-order corrections when the common eigenvalue scale is \(r^2\).

## 3. Disposition

- IV-232 null diagonal cubic coefficient: **RETAINED, CORRECT WITHIN ITS AMPLITUDE MODEL**.
- IV-232 as a complete cubic small-eigenvalue coefficient: **NOT CLAIMED**.
- Cubic Schur/eigenvalue coefficient including off-diagonal and common-block corrections: **OPEN**.
- Full finite-\(r\) positivity and target response sign: **OPEN**.

This correction preserves the valid coefficient calculation and prevents overinterpreting it as an eigenvalue coefficient.
