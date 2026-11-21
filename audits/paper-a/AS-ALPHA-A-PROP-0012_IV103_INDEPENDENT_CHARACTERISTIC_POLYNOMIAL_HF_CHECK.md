# IV-103 — Independent Fourth-Order Check via Characteristic Polynomial and Hellmann–Feynman

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Independent analytic cross-check; not Lean-verified  
**Date:** 2026-11-22

## 1. Independent route

This audit independently checks IV-102's middle-spin probability by adding an auxiliary field `- k X_2), differentiating the ground energy (Hellmann–Feynman), and extracting the perturbation series from the characteristic polynomial. It does not use IV-102's eigenvector-amplitude expansions.

Use `a=J_{12}/(4h)`, `b=J_{23}/(4h)`, scale `a=εA`, `b=εB`, and energies in units of h. In the even-parity basis `(000,110,101,011)`, the auxiliary-field matrix is
\[
M(k)=
\begin{pmatrix}
-3-k&-4a&0&-4b\\
-4a&1+k&-4b&0\\
0&-4b&1-k&-4a\\
-4b&0&-4a&1+k
\end{pmatrix}.
\]
At zero coupling the ground energy is `E_0(k)=-3-k`. This field dependence is retained in the expansion; omitting it would give an incorrect derivative.

## 2. Characteristic polynomial

Let `P(E,k)=det(E I-M(k))`. Direct determinant expansion gives
\[
\begin{aligned}
P={}&E^4-6E^2+8E-3\\
&-32(a^2+b^2)(E^2-1)\\
&+256(a^4+b^4-2a^2b^2)\\
&-2E^2k^2-4E^2k+8Ek+k^4+4k^3+2k^2-4k.
\end{aligned}
\]
Equivalently the last lines are the field-only terms, while the coupling-dependent terms are explicit. This polynomial is an independently checkable determinant identity for the 4-by-4 block.

## 3. Ground-energy series

Substitute
\[
E(ε,k)=-3-k+ε^2e_2(k)+ε^4e_4(k)+O(ε^6)
\]
into `P(E,k)=0`, equate coefficients, and solve. The coefficients are
\[
e_2(k)=-\frac{8(A^2+B^2)}{k+2},
\]
\[
e_4(k)=\frac{32(A^4-2A^2B^2-B^4)}{(k+2)^3}.
\]
The energy series is locally analytic in the couplings and auxiliary field near the nondegenerate zero-coupling ground state.

## 4. Hellmann–Feynman yields middle-spin probability

Since `∂_k H=-X_2`,
\[
\frac{∂E}{∂k}=-\langle X_2\rangle,qquad
q=\Pr(X_2=-1)=\frac{1+∂_kE|_{k=0}}2.
\]
Differentiating the energy series and setting `k=0` gives
\[
\boxed{
q=ε^2(A^2+B^2)+ε^4(-3A^4+2A^2B^2-3B^4)+O(ε^6).
}
\]
Thus, after restoring `a,b`,
\[
\boxed{q=a^2+b^2-3a^4+2a^2b^2-3b^4+O(6).}
\]

## 5. IV-102 comparison

The independent characteristic-polynomial/Hellmann–Feynman route reproduces all three fourth-order coefficients from IV-102:
- coefficient of `a^4`: `-3`
- mixed coefficient of `a^2 b^2`: `+2`
- coefficient of `b^4`: `-3`

This cross-check supports the perturbative coefficients but is not a formal proof artifact and has not been machine-checked in Lean. It is an independent derivation route: IV-102 uses normalized eigenvector components, while IV-103 uses the energy derivative with an auxiliary field.

## 6. Status and next step

Middle-spin probability fourth-order coefficients are **cross-checked analytically by two routes**. Paper A's target response identity and Proposition remain **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

Next: IV-104 should use this verified local q expansion to audit the binary entropy expansion `H(q)` and its error order, carefully tracking logarithmic terms `q log q`; do not claim a regular polynomial remainder in the couplings when the entropy is nonanalytic at zero coupling.
