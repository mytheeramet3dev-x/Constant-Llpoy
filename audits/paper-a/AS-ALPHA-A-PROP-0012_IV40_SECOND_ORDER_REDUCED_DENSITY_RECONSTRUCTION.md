# IV-40 — Second-Order Reduced Density Matrix Reconstruction

**Status:** ONE-SITE STRUCTURE PASS / FULL TWO-SITE RECONSTRUCTION OPEN / ENTROPY COEFFICIENT NOT VERIFIED

## 1. Perturbative state bookkeeping

In the transverse-field x-basis, interactions flip spins in pairs. The normalized state is organized by perturbative degree:
- ground-state component: 1 + c0(2)
- pair-flip states: a_e(1) + a_e(2)
- four-flip states: c_F(2)
- higher-degree terms omitted

Here a_ij(1) = J_ij/(4h); a_ij(2) receives shared-vertex paths; c_F(2) is the coherent four-flip coefficient from IV-39. This bookkeeping is not a complete fourth-order probability or entropy expansion.

## 2. Exact one-site structure from parity

The Hamiltonian commutes with global transverse parity Px = product_i sigma_i^x. In the nondegenerate ground-state regime, the ground state is a parity eigenstate. Since parity factors into site and environment parity, tracing out the environment implies rho_i commutes with sigma_i^x. Thus rho_i is diagonal in the x-basis:

rho_i = diag(1-p_i, p_i).

The leading small eigenvalue is:
p_i(2) = sum_(j != i) |a_ij(1)|^2
        = sum_(j != i) J_ij^2/(16h^2).

At symmetric coupling J_ij=J and r=J/h:
p_i(2) = (N-1)r^2/16.

Degree-three bookkeeping includes the interference term:
p_i(3) = 2 Re sum_(j != i) conjugate(a_ij(1))*a_ij(2).

This is not a complete expansion through degree four. Fourth-order contributions include four-flip amplitudes squared, higher-order pair amplitudes, and normalization terms.

## 3. Two-site reduced matrix

For global amplitudes c_(a,b), with a labeling the two-site basis and b the environment basis, the exact partial trace is:
(rho_ij)_(a,a') = sum_b c_(a,b) conjugate(c_(a',b)).

A full entropy-order expansion requires consistent inclusion of amplitudes, normalization, two-flip corrections, four-flip channels, and off-diagonal matrix blocks. IV-39 amplitudes alone do not constitute this complete reconstruction.

## 4. Entropy-response implication

The one-site symmetry structure and leading p_i are confirmed. However, the complete B-C coefficient requires differentiated one-site and two-site entropy contributions from an order-consistent matrix expansion. A bound p=O(r^2) alone does not control p_u ln(p) or its differentiated remainder.

## 5. Findings

- One-site parity/diagonal structure: PASS (exact in nondegenerate ground-state regime).
- Leading one-site small eigenvalue: PASS.
- Degree-three interference structure: derived; full coefficient not independently evaluated.
- Exact two-site partial-trace formula: PASS.
- Complete two-site matrix expansion at entropy-required order: OPEN.
- Entropy derivative and B-C recomputation: OPEN.
- Lean verification: NOT PERFORMED.

IV-40 is partial structural progress only. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
