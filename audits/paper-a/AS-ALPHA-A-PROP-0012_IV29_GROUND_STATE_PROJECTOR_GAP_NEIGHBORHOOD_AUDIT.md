# IV-29 — Analytic Ground-State Projector and Gap-Neighborhood Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Audit the finite-N isolated-ground-state premise, persistence of a gap, parameter neighborhood, and projector analyticity used by the weak-coupling derivative ledger.

## 1. Unperturbed spectrum

The working derivation uses \(H_0=-h\sum_i\sigma_i^x\), with \(h>0\). The ground state \(|+\cdots+\rangle\) is unique. Flipping one x-spin costs \(2h\); hence the unperturbed ground-to-first-excited gap is \(2h\).

## 2. Finite-dimensional perturbation principle

For fixed finite \(N\), the Hilbert space is finite dimensional and the Hamiltonian depends analytically on the real edge variables and coupling parameter (indeed polynomially for the stated interaction). If the perturbation norm is sufficiently small compared with the unperturbed gap, eigenvalue separation persists. The isolated spectral projector can then be represented by a Riesz contour integral around the ground eigenvalue and is analytic in the parameters throughout a neighborhood where the contour remains separated from the spectrum.

This establishes the analytic-projector route in principle. The admissible radius and constants depend on \(N\), the number of edges, and the chosen norm; no uniform-in-N statement follows from the finite-dimensional argument.

## 3. What the working document explicitly supplies

The working derivation states the fixed-finite-N scope, unique uncoupled ground state, gap \(2h\), independent edge perturbations in a neighborhood, and joint analyticity of the ground-state projector. IV-29 confirms that these are the right hypotheses for the local projector argument.

## 4. What is not quantitatively audited

- Explicit perturbation-norm bound guaranteeing a chosen contour remains valid throughout the edge neighborhood.
- A numerical or symbolic lower bound for the gap on the full neighborhood.
- Uniform-in-N radius or constants.
- Complete verification that every subsequent amplitude and reduced-matrix remainder is covered by the same analytic domain.
- Analytic labeling of individual eigenvalues in degenerate excited subspaces (not required for the ground projector, but relevant to later spectral arguments).

## 5. Adversarial disposition

- Unperturbed unique ground state: **PASS**.
- Unperturbed gap \(2h\): **PASS**.
- Finite-dimensional analytic ground-projector principle: **PASS (standard contour argument, conditional neighborhood)**.
- Gap persistence in some sufficiently small finite-N perturbation neighborhood: **PASS (principle)**.
- Explicit quantitative common neighborhood for the full working remainder ledger: **OPEN**.
- Uniform-in-N analyticity/gap control: **NOT CLAIMED**.
- Counterexample to target proposition: **not established**.
- Lean formalization/build: **not performed**.

## 6. Disposition

IV-29 validates the analytic ground-projector premise at the level of standard finite-dimensional perturbation theory and the stated source setup. It does not certify the full quantitative neighborhood or close entropy/logarithmic remainder obligations. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 7. Next

IV-30: **Remainder Ledger Cross-Audit and Dependency Graph** — map every remaining estimate used in the candidate \(B-C\) asymptotic to its source, assumptions, derivative status, and unresolved downstream dependencies; identify duplicated or circular assumptions.
