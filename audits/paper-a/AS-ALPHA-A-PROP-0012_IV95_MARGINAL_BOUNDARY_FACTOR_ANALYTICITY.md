# IV-95 — Marginal Boundary Factorization via Analyticity and Symmetry

**Status:** ANALYTIC-PARTIAL / CONDITIONAL STRUCTURAL ARGUMENT. Does not close Proposition 0012.

## Setup
Three-spin path with transverse-field Hamiltonian
H = -J12 Z1 Z2 - J23 Z2 Z3 - h(X1+X2+X3), h>0.
Work near J12=J23=0. The ground state is nondegenerate at the origin (gap 2h to the one-flip sector), so for sufficiently small couplings its spectral projector and reduced states are analytic in couplings. The small marginal eigenvalue p1 of rho_1 is analytic near the origin.

## Symmetry and boundary
Conjugation by X1 changes Z1 -> -Z1, leaving the field and J23 term invariant and mapping J12 -> -J12. The spectrum of rho_1 is unchanged under this unitary conjugation; hence p1(J12,J23) is even in J12. At J12=0 spin 1 is exactly decoupled and in the pure field ground state, so p1(0,J23)=0 for all sufficiently small J23. Analyticity therefore implies factorization
p1(J12,J23)=J12^2 g1(J12^2,J23)
locally, with g1 analytic (the displayed dependence on squares is supported by sign-flip symmetries on the path; at minimum evenness in J12 gives a J12^2 factor and analytic residual in the other variable).

By the analogous endpoint symmetry,
p3(J12,J23)=J23^2 g3(J12,J23^2)
locally.

First-order perturbation gives the single-edge flip amplitude J/(4h), so the leading probability is J^2/(16h^2). Thus g1(0,0)=g3(0,0)=1/(16h^2), when using dimensional J variables.

## Consequence (local conditional bound)
If g1 and g3 are analytic and bounded derivatives on a sufficiently small compact neighborhood, then
p1 = x + O(x (J12^2+J23^2)/h^2),
p3 = y + O(y (J12^2+J23^2)/h^2),
where x=J12^2/(16h^2), y=J23^2/(16h^2).
This yields the ratio-aware marginal error pattern required by IV-94 (up to equivalent dimensionless constants), locally uniformly including the axes.

## Caveats
1. This argument concerns marginal eigenvalues, not the joint endpoint state's eigenvalue structure.
2. A fully formal write-up should state the analytic neighborhood and justify analyticity of the ordered small eigenvalue; near zero the eigenvalue is isolated from the large eigenvalue, so this is locally valid.
3. A uniform entropy remainder still requires control of joint-state additional eigenvalues and q=t+O(t^2), plus precise bounds.
4. The leading coefficient is asserted from first-order perturbation; this note is a structural derivation, not a Lean proof or independent verified artifact.

## Status
This closes a structural route for the marginal ratio-aware bounds, conditional on completing explicit constants/analytic neighborhood estimates. It does not close the joint-state obligations or Proposition 0012. Paper A remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
