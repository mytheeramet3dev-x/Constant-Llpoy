# IV-56 — Fourth-Order Excitation-Sector Dependency Map

**Status:** STRUCTURAL MAP / PATH ENUMERATION NOT COMPLETE / DIRECT c_vv OPEN  
**Scope:** Classify the perturbative excitation sectors that may enter a fourth-order reduced odd-block coefficient for the transverse-field Ising model, using the weak-coupling expansion in J/h around the transverse-field product ground state.

## 1. Perturbative convention

Take the unperturbed Hamiltonian H0=-h sum_i sigma_i^x (h>0) and perturbation V=-sum_{i<j} J_ij sigma_i^z sigma_j^z. In the H0 eigenbasis, V flips two x-basis spins. An excitation with 2q flipped spins has H0 energy gap 4q h above the vacuum. A perturbative amplitude at order n in V can only contain even-flip sectors 2q with q<=n, but this is a necessary sector bound, not a proof every such sector contributes.

## 2. Order/sector dependency table

| Wavefunction order n | Candidate flipped-spin sectors | Note |
|---|---|---|
| 0 | 0 | vacuum |
| 1 | 2 | one pair-flip edge |
| 2 | 2, 4 | repeated/shared-edge paths may return to two flips; disjoint-edge paths may reach four |
| 3 | 2, 4, 6 | pair-edge path sequences; amplitudes require complete path sums and intermediate-state denominators |
| 4 | 0, 2, 4, 6, 8 | vacuum normalization/return, and candidate sectors through eight flips |

This table is sector-level bookkeeping only. It does not provide path multiplicities, amplitude coefficients, or prove nonzero contributions.

## 3. Terms that can enter reduced density matrix at total order four

For reduced-state matrix elements, products of wavefunction amplitudes whose perturbative orders sum to four are candidates:
- (0,4) and (4,0): vacuum–fourth-order amplitude interference, with its trace/normalization role;
- (1,3) and (3,1): first–third amplitude interference;
- (2,2): second-order amplitude products.
Which survive in the retained two-site partial trace depends on equality of traced-environment x-basis configurations. That matching must be checked element-by-element; sector counting alone cannot determine it.

## 4. Requirements for a complete path audit

Each amplitude must be indexed by a target flipped set S and enumerated as ordered pair-edge sequences e1,...,en, with intermediate flipped sets S_k, energy denominators E0-E(S_k), exclusions/reducible terms handled according to the selected perturbation scheme, and a normalization convention. Paths that reach the same S must be summed before products are formed. A complete fourth-order calculation also requires the chosen perturbative wavefunction normalization and any lower-order normalization corrections.

## 5. Disposition

- Sector bound and order bookkeeping: structural derivation under H0/V convention.
- Explicit ordered path sums and denominators through fourth order: OPEN.
- Environment-match enumeration for retained sites 1,2: OPEN.
- Complete normalized reduced density matrix O(r^4): OPEN.
- Direct c_vv: OPEN/BLOCKED pending path data.
- Mixing correction and full low-branch coefficient: not closed.
- B-C response, entropy derivative, Lean: OPEN/NOT PERFORMED.

PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
