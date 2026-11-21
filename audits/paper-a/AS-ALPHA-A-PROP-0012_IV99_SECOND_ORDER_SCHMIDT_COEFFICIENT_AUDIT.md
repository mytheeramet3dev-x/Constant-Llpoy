# IV-99 — Second-Order Schmidt Coefficient Audit (Path-3)

Status: ANALYTIC PARTIAL; no higher-order coefficient is claimed.

## Model and convention
\[
H=-J_{12}Z_1Z_2-J_{23}Z_2Z_3-h(X_1+X_2+X_3),\quad h>0.
\]
Use the product-X basis, with \(|0\rangle\) the +1 eigenvector of X. The unperturbed ground state is \(|000\rangle\), energy \(-3h\). Each pair-flip state costs \(4h\). Edge perturbations flip the two endpoint bits, with matrix element \(-J_e\).

## First-order ground-state amplitudes
Nondegenerate perturbation theory gives
\[
|\psi\rangle=|000\rangle+\frac{J_{12}}{4h}|110\rangle
+\frac{J_{23}}{4h}|011\rangle+O(J^2),
\]
up to normalization and second-order terms. Thus the probability mass for middle-spin X-basis bit 1 at quadratic order is
\[
t=\frac{J_{12}^2+J_{23}^2}{16h^2}=x+y.
\]
This establishes the quadratic coefficient of the middle reduced state's small eigenvalue, provided one accounts for the fact that its small eigenvalue agrees with the flipped-bit probability to this order; off-diagonal terms of \(\rho_2\) begin at higher order.

## Symmetry constraints
Conjugation by \(X_1\) changes \(J_{12}\to-J_{12}\) while leaving \(J_{23}\) fixed; conjugation by \(X_3\) changes \(J_{23}\to-J_{23}\). The middle-spin reduced state is invariant under these unitaries (they act on traced-out spins), so its eigenvalues are even separately in both edge couplings. In the analytic neighborhood where the ground state is nondegenerate, the small eigenvalue therefore has an expansion in \(J_{12}^2,J_{23}^2\), and degree-four corrections may include \(J_{12}^4,J_{12}^2J_{23}^2,J_{23}^4\), but no odd powers in either coupling.

## Important correction / limitation
The exact degree-four coefficients have **not** been derived in this audit. The previous argument establishes only the quadratic term and the allowed parity structure. It does not, by itself, calculate or prove the remainder coefficient, nor provide a validated numerical diagonalization. The claim \(q=x+y+O((x+y)^2)\) is a local analytic consequence once the small eigenvalue is identified and analyticity is established; the stronger coefficient-level expansion remains open.

## Next proof obligations
1. Compute the middle-spin reduced matrix through fourth order, including normalization and all second-order state amplitudes needed for its entries.
2. Derive the small eigenvalue from its determinant/trace rather than equating it prematurely with a basis probability.
3. Check whether any fourth-order mixed coefficient survives.
4. Independently verify the expansion with high-precision numerical diagonalization before using it in an entropy remainder.

## Paper status
Paper A / Proposition 0012 remains OPEN, ANALYTIC-PARTIAL, NOT VERIFIED. This note is a derivation audit, not a Lean proof.
