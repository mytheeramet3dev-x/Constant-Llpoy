# IV-229 — Higher-Order Gram Lifting and Physical Odd-Block Positivity Audit

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, retained odd reduced block near uniform coupling with edge \(u=u_{13}\)  
**Status:** CONDITIONAL SCHUR-COMPLEMENT CRITERION DERIVED / HIGHER-ORDER MODEL COEFFICIENTS NOT COMPUTED / NOT LEAN-FORMALIZED  
**Scope:** Determine exactly what additional estimates are needed to transfer the first-order amplitude-Gram small-eigenvalue coefficient from IV-228 to the physical reduced odd block. No positivity claim for the full TFIM odd block is made.

## 1. IV-228 first-order matrix in common/null basis

Let \(n=N-2\ge2\). IV-228's first-order amplitude Gram matrix is
\[
M_2(u)=\begin{pmatrix}
n/16+u/8+u^2/16 & n/16+u/16\\
n/16+u/16 & n/16
\end{pmatrix}.
\]
Use the orthonormal basis
\[
p=(1,1)/\sqrt2,\qquad v=(1,-1)/\sqrt2.
\]
Then the entries are
\[
L_2=p^TM_2p=\frac n8+\frac u8+\frac{u^2}{32},
\]
\[
t_2=p^TM_2v=\frac u{16}+\frac{u^2}{32},
\qquad
s_2=v^TM_2v=\frac{u^2}{32}.
\]
At \(u=0\), \(L_2=n/8>0\), while \(t_2=s_2=0\).

For a symmetric \(2\times2\) block \(\begin{pmatrix}L&t\\t&s\end{pmatrix}\) with \(L>0\), the Schur complement is \(s-t^2/L\). Here
\[
s_2-\frac{t_2^2}{L_2}
=\frac{n-1}{32n}u^2+O(u^3),
\]
which agrees with IV-228's exact eigenvalue expansion to quadratic order.

## 2. Physical block and its exact Schur criterion

Write the actual reduced odd block in the same orthonormal basis:
\[
O(r,u)=\begin{pmatrix}L(r,u)&t(r,u)\\t(r,u)&s(r,u)\end{pmatrix}.
\]
If \(L(r,u)>0\), then
\[
O(r,u)\succeq0
\quad\Longleftrightarrow\quad
s(r,u)-\frac{t(r,u)^2}{L(r,u)}\ge0.
\]
Strict positivity is equivalent to strict positivity of both \(L\) and the Schur complement. This identity is exact; it is not a perturbative approximation.

## 3. What a generic remainder bound does and does not prove

Suppose a reconstruction has the form
\[
O(r,u)=r^2M_2(u)+E(r,u).
\]
Weyl's inequality yields
\[
\lambda_{\min}(O)\ge r^2\lambda_{\min}(M_2(u))-\|E(r,u)\|_2.
\]
For fixed nonzero \(u\), the leading coefficient from IV-228 is positive. However, a remainder bound merely of size \(\|E\|=O(r^3)\), independent of \(u\), is insufficient to prove positivity uniformly as \(u\to0\): the positive leading term is of order \(r^2u^2\), and the bound may dominate it.

A sufficient fixed-\(u\) condition is, for some verified \(C,r_0>0\),
\[
\|E(r,u)\|_2\le C r^3,\qquad
0<r<r_0(u),\quad
Cr<\lambda_{\min}(M_2(u)).
\]
This is only a conditional transfer criterion. It supplies no uniform radius near \(u=0\) unless the error is controlled with additional \(u\)-dependence or symmetry.

## 4. Symmetry-sensitive lifting: required estimates

Along \(u=0\), retained-site exchange symmetry forces the antisymmetric eigenvalue to vanish for the symmetry-preserving model family. Therefore any physical lifting away from \(u=0\) must be analyzed with a remainder that respects this symmetry. A useful sufficient local structure would be bounds on the common/null entries such as
\[
L(r,u)\ge \ell r^2,\quad
t(r,u)=r^2(\alpha u+O(u^2))+R_t(r,u),\quad
s(r,u)=r^2(\beta u^2+O(u^3))+R_s(r,u),
\]
with \(\ell>0\) and remainder estimates that preserve the exact zero at \(u=0\) and are sufficiently small relative to \(r^2u^2\) after forming the Schur complement. These bounds are proposed proof obligations, not established facts for this TFIM reduced block.

## 5. IV-229 findings

- Exact Schur-complement positivity criterion for the physical 2×2 block: **DERIVED**.
- IV-228 common/null basis entries and quadratic Schur coefficient: **DERIVED**.
- Transfer of first-order-Gram positivity to the full physical block: **CONDITIONAL ONLY**; no verified higher-order error bounds presently supplied.
- Uniform positivity near \(u=0\): **OPEN**, and generic \(O(r^3)\) operator-norm control alone is insufficient.
- Exact symmetry zero on the symmetry-preserving \(u=0\) family: **SYMMETRY-DEPENDENT**, subject to the model family preserving retained-site exchange.
- Full physical TFIM positivity, entropy response, manuscript parameter reconciliation, global \(B-C\) sign, and Lean formalization: **OPEN**.

## 6. Next verification obligation

IV-230 should compute or bound the physical reduced odd-block entries \(L,t,s\) from the normalized ground-state/environment amplitudes through the first order capable of deciding the Schur complement, explicitly keeping the edge-perturbation dependence. Until those terms are reconstructed, do not promote IV-228's coefficient to a physical-block theorem or claim PROP-0012 verified.
