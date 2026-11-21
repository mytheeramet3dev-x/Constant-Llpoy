# IV-102 — Fourth-Order Middle-Spin Probability from the Even-Parity Block

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Analytic perturbative result (local expansion); not a Lean proof  
**Date:** 2026-11-22

## 1. Hamiltonian and convention

\[
H=-J_{12}Z_1Z_2-J_{23}Z_2Z_3-h(X_1+X_2+X_3),\quad h>0.
\]

Use the product-(X) basis and dimensionless couplings
\[
a=J_{12}/(4h),\qquad b=J_{23}/(4h).
\]
The unperturbed ground state is (|000\rangle_X), energy (-3h). Flipping two (X)-spins costs (4h), so the first-order pair-flip amplitudes are (a) and (b). This confirms the IV-99 leading-order normalization (J/(4h)).

## 2. Exact even-parity sector

The global parity (P=X_1X_2X_3) commutes with (H). The ground-state branch near (J_{12}=J_{23}=0) lies in the even sector with basis
\[
|000\rangle, |110\rangle, |101\rangle, |011\rangle.
\]
In units of (h), its matrix is
\[
\begin{pmatrix}
-3&-4a&0&-4b\\
-4a&1&-4b&0\\
0&-4b&1&-4a\\
-4b&0&-4a&1
\end{pmatrix}.
\]
Let the eigenvalue be (E/h=-3+\delta) and set the ground component to (1). Denote the remaining components in order by (u,w,z). The equations are
\[
\begin{aligned}
(4-\delta)u-4bw&=4a,\\
(4-\delta)w-4bu-4az&=0,\\
(4-\delta)z-4aw&=4b,\\
\delta&=-4au-4bz.
\end{aligned}
\]

## 3. Perturbative amplitudes

Solving these coupled equations order-by-order (with (a,b) both scaled by a bookkeeping parameter) yields
\[
\begin{aligned}
u&=a-a^3+ab^2+O(5),\\
z&=b+a^2b-b^3+O(5),\\
w&=2ab+O(4),\\
\delta&=-4(a^2+b^2)+4(a^4+b^4)-8a^2b^2+O(6).
\end{aligned}
\]
Here (O(k)) denotes terms of total degree at least (k) in (a,b); the amplitude expansions retain terms through total degree three.

## 4. Middle-spin probability

The middle spin is (1) in (|110\rangle) and (|011\rangle), so parity gives an exactly diagonal middle reduced density matrix. For the unnormalized vector ((1,u,w,z)),
\[
q=\Pr(X_2=-1)=\frac{u^2+z^2}{1+u^2+w^2+z^2}.
\]
Substituting the amplitudes and expanding to degree four:
\[
\boxed{q=a^2+b^2-3a^4+2a^2b^2-3b^4+O(6).}
\]
Equivalently, in the original couplings,
\[
\boxed{
q=\frac{J_{12}^2+J_{23}^2}{16h^2}
-3\frac{J_{12}^4+J_{23}^4}{256h^4}
+2\frac{J_{12}^2J_{23}^2}{256h^4}
+O(J^6/h^6).
}
\]
Therefore the fourth-order coefficients in the requested convention are
\[
\alpha=-3/256,\quad \beta=2/256=1/128,\quad \gamma=-3/256.
\]
The mixed coefficient is **nonzero** and positive in this local expansion.

## 5. Scope / limitations

- This is a local analytic perturbation expansion around (J_{12}=J_{23}=0), on the nondegenerate ground-state branch for (h>0).
- The symbolic expansion was calculated by solving the even-sector eigenvector equations order-by-order and expanding the normalized probability. The displayed coefficients are not a global-in-coupling statement.
- No conclusion is drawn about the target response identity (chi_1-\chi_2=(N-2)(B-C)), nor about the full proposition. The paper remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
- This report is a derivation record, not a formal Lean verification. It should be independently checked before being relied on as a final manuscript proof.

## 6. Next audit

IV-103 should independently check this series by a second derivation (e.g. resolvent/Schrieffer-Wolff expansion or direct characteristic-polynomial eigenvector identities), and then audit its contribution to the entropy/MI expansion without assuming the response identity.
