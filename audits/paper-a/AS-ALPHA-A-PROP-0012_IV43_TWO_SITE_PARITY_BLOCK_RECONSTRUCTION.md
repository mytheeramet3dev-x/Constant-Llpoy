# IV-43 — Two-Site Reduced Matrix: Parity Block Reconstruction

**Status:** EXACT SYMMETRY/BLOCK STRUCTURE PASS / MATRIX ELEMENT EXPANSION OPEN  
**Scope:** Derive the two-site parity block structure from the frozen Hamiltonian and identify matrix entries required for a full reduced-state expansion.

## 1. Symmetry

For H = -sum_(a<b) J_ab sigma_a^z sigma_b^z - h sum_a sigma_a^x, the global operator P_x = product_a sigma_a^x commutes with H. In a nondegenerate ground-state regime, the ground state can be chosen as a P_x eigenstate.

For subsystem {i,j}, the corresponding subsystem parity is P_ij = sigma_i^x sigma_j^x. Tracing out the complement yields [rho_ij, P_ij] = 0. This is exact, subject to the ground state being a parity eigenstate.

## 2. Block decomposition in the x-basis

Order the two-site x-basis as |++>, |+->, |-+>, |-->. P_ij has eigenvalue +1 on {|++>,|-->} and -1 on {|+->,|-+>}. Thus rho_ij has no matrix elements between these two sectors and is block diagonal:

rho_ij = blockdiag(M_even, M_odd),

where M_even acts on {|++>,|-->} and M_odd acts on {|+->,|-+>}. Each block is a 2x2 Hermitian positive semidefinite matrix. Trace(M_even)+trace(M_odd)=1.

Each block has two eigenvalues obtained from its trace and determinant:
lambda_(s,±) = (tr M_s ± sqrt((tr M_s)^2 - 4 det M_s))/2, s in {even, odd}.
This formula is exact, but coefficient expansions require explicit expansions of all block entries.

## 3. Matrix elements and entropy obligations

The IV-38/39 amplitude results and IV-40 partial-trace rule establish ingredients, not a complete rho_ij block expansion. To certify entropy coefficients, the following remain required:
- diagonal entries in both parity blocks through entropy-required order;
- complex/off-diagonal entries and their interference terms;
- normalization corrections;
- coupling-direction derivatives of each entry;
- branch splitting and zero-leading cases for determinants/discriminants.

## 4. Entropy from blocks

Once block eigenvalues are controlled, S(rho_ij) = -sum_(s,±) lambda_(s,±) ln lambda_(s,±). The derivative must account for all four branches, including low eigenvalues. Block diagonalization by symmetry does not eliminate the logarithmic remainder or justify dropping off-diagonal terms inside a block.

## 5. Audit disposition

Exact parity block structure: **PASS**.  
Exact 2x2 eigenvalue formula: **PASS**.  
Full perturbative block entries: **OPEN**.  
Low-branch expansions and differentiated remainder: **OPEN**.  
B-C coefficient: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
