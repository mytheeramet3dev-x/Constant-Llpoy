# IV-48 — Odd-Block Low-Eigenvalue Reconstruction

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response difference B-C  
**Status:** ANALYTIC-PARTIAL / OPEN / NOT VERIFIED  
**Scope:** Determine the correct perturbative obligation for the small eigenvalue of the odd two-site block. No numerical or Lean verification is claimed.

## 1. Leading block and null direction

For uniform coupling, the leading odd block recorded in IV-47 is
\[
O(r)=r^2 a\begin{pmatrix}1&1\\1&1\end{pmatrix}+\cdots,
\qquad a=(N-2)/8
\]
when r=J/h. Its normalized leading eigenvectors are u=(1,1)/sqrt(2), v=(1,-1)/sqrt(2); leading eigenvalues are 2a r^2 and 0. The null direction is therefore a perturbative branch, not a positive eigenvalue controlled at order r^2.

## 2. General expansion and branch coefficient

Write a Hermitian expansion in the u,v basis:
\[
O(r)=r^2 A+r^3B+r^4C+O(r^5),\
A=\begin{pmatrix}a_+&0\\0&0\end{pmatrix},\quad a_+>0.
\]
The small eigenvalue can be expanded using the Schur complement (equivalently nondegenerate perturbation theory after factoring r^2). Its r^3 coefficient is B_vv. Thus an r^4 start is **not automatic**: it requires B_vv=0. Under that condition, and with the stated expansion and regularity, the r^4 coefficient is
\[
\lambda_{\rm small}(r)=r^4\left(C_{vv}-\frac{|B_{uv}|^2}{a_+}\right)+O(r^5).
\]
The formula shows that the off-diagonal r^3 coupling contributes at the same order as C_vv and cannot be dropped. If the bracket vanishes, the branch starts later or identically zero; its order must be investigated further. Positivity constrains the coefficient but does not supply its value or strict positivity.

## 3. Determinant shortcut and its limits

The identity for a 2x2 block, lambda_small = det(O)/lambda_large, is exact when lambda_large is nonzero. But an expansion of det(O) is reliable only if all entries, including their remainders, are reconstructed to sufficient order and the large-eigenvalue expansion is controlled. Using the leading rank-one block alone does not determine det(O) at r^4.

## 4. Edge derivatives and logarithms

For a coupling parameter u, the branch coefficient must be differentiated only after its dependence on the reconstructed matrices is established. If lambda_small = r^4 k(u,r), with k bounded away from zero and k_u controlled, then its entropy contribution -lambda ln lambda has derivative of order r^4(1+|ln r|). If k can vanish, this estimate is not uniform and branch order may change. IV-41/42 remain relevant for derivative and entropy control.

## 5. Audit outcome

- Leading rank-one odd block and its null vector: carried forward as prior conditional result.
- General r^3/r^4 low-branch coefficient formula: derived conditionally from matrix perturbation / Schur complement.
- Claim that the branch necessarily begins at r^4: **OPEN; not established**.
- Exact higher-order odd-block entries and coefficients: **OPEN**.
- B- and C-direction derivatives of the low branch: **OPEN**.
- Entropy logarithmic remainder and uniformity: **OPEN**.
- Full B-C sign/coefficient: **OPEN**.
- Lean verification: **NOT PERFORMED**.

## 6. Next obligation

IV-49 should reconstruct the odd block in the (u,v) basis through cubic order and determine whether B_vv vanishes for the actual Hamiltonian and selected edge directions, rather than relying on rank-one leading structure alone.
