# IV-101 — Exact Middle-State Parity Correction

Status: exact structural result; correction to IV-100 wording.

## Global parity
The Hamiltonian commutes with P = X1 X2 X3:
- each X_i commutes with P;
- each Z_i Z_j anticommutes with X_i and X_j individually, so the two sign changes cancel and it commutes with P.

In the X-product basis, P has eigenvalue (-1)^(n1+n2+n3). Near zero coupling, the unique ground state continues in the even parity sector.

## Middle-spin reduced density matrix
For a parity eigenstate, matrix elements of rho_2 between middle X-basis states |0> and |1> vanish exactly. The trace over endpoint basis states requires the same endpoint pair in both amplitudes; the two full basis states then differ only in the middle bit and have opposite P parity, so they cannot both occur in a single parity-sector wavefunction.

Hence rho_2 is exactly diagonal in the X basis throughout the nondegenerate region connected to the uncoupled ground state:
rho_2 = diag(1-s, s), where s is the exact middle-bit probability in the chosen X basis (ordering may be swapped outside the weak-coupling neighborhood).

Consequently the small eigenvalue q equals the middle-bit probability exactly in this region; there is no off-diagonal eigenvalue correction. This sharpens and corrects IV-100's tentative statement that the off-diagonal entry is merely higher order.

## What this does not establish
This parity fact does not provide the fourth-order coefficient of s. The exact probability still requires a ground-state expansion. Quadratic coefficient q = J12^2/(16h^2)+J23^2/(16h^2) remains the perturbative result. Fourth-order coefficients and uniform entropy remainder are still open.

## Correction scope
IV-100's description of the middle reduced-state off-diagonal as an unresolved higher-order term is superseded by this exact symmetry argument. No other IV-100 claims are upgraded.

## Status
Paper A / Proposition 0012 remains OPEN, ANALYTIC-PARTIAL, NOT VERIFIED.
