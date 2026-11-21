# PROP-0012 IV-17 — Adversarial Audit of the Pair-Flip Taylor Recursion

**Date:** 2026-11-21  
**Target:** IV-16 support/order induction, including scalar eigenvalue corrections, normalization/gauge terms, intermediate-state degeneracies, and edge differentiation.  
**Disposition:** PASS for the support-preservation argument at the analytic recurrence level, with explicit scope limitations. No counterexample found. Not mechanically verified or Lean formalized.

## 1. Recurrence model and graph support

In the x-basis, index states by flip sets F. The unperturbed operator is diagonal and the interaction connects F only to F△e for pair edges e. Thus the perturbation graph is a graph on subsets whose transitions change exactly two sites.

For a non-vacuum coefficient, the analytic eigenvector equation in a fixed local gauge can be rearranged schematically as
[
Delta_F c_F(r,u)=rsum_{e}v_e(u)c_{F	riangle e}(r,u)+
sum_{kge1}r^k,a_k(u)c_F(r,u)+	ext{gauge/normalization scalar terms},
]
where (Delta_F
e0) for F≠empty at the uncoupled point. This is a support/order schematic, not a claimed exact coefficient formula; exact recurrence signs and coefficients depend on the chosen eigenvector normalization.

## 2. Attack: eigenvalue corrections

Energy coefficients are scalar in flip-set space. At perturbative order k they multiply an already existing amplitude at a lower Taylor order, but cannot add sites to its support. Since their order is nonnegative (and nonconstant corrections enter with positive r order), they cannot create an amplitude on F before a path of pair-flip insertions reaches F.

**Outcome:** no support/order counterexample from scalar eigenvalue corrections, conditional on the standard analytic coefficient recursion.

## 3. Attack: normalization and gauge

Normalization or a local gauge condition modifies the eigenvector by scalar analytic factors and/or determines the vacuum coefficient. Multiplication by a scalar Taylor series with nonnegative powers of r cannot lower the first nonzero r order of any component. The vacuum component is handled separately and is O(1), consistent with the bound.

**Outcome:** no support/order counterexample from normalization or gauge terms.

## 4. Attack: intermediate degeneracies

The excited eigenspaces of the uncoupled Hamiltonian are degenerate, but the ground eigenvalue is isolated and simple. The ground-state analytic projector/eigenvector exists locally without selecting or analytically tracking individual excited eigenvectors. The recursion for a ground vector uses the diagonal resolvent on the orthogonal complement; its denominators are nonzero at r=0, so degeneracy within the excited subspace does not create a zero-denominator obstruction or a new flip transition.

**Outcome:** excited-state degeneracy does not defeat the support count for this ground-state expansion. This assumes the perturbation/eigenvector setup is indeed the finite-dimensional TFIM with h>0 and fixed N.

## 5. Attack: edge-variable differentiation

Differentiating with respect to u_e differentiates scalar path weights/coefficients. It does not change the graph transition F→F△e' for any interaction edge e', and it does not remove the r factor carried by an interaction insertion. Therefore first edge derivatives obey the same lower Taylor-order support bound. This is coefficientwise in a local analytic neighborhood; constants may depend on N and the chosen neighborhood.

## 6. Induction summary

Let d(F) be the minimum number of pair-edge transitions from the vacuum to F. Every path changes at most two sites per step, so d(F)≥|F|/2. The recurrence preserves the graph-path lower bound; thus c_F has no Taylor term before d(F). For even F this yields c_F=O_N(r^{|F|/2}). Odd F are forbidden by the global even-flip parity symmetry and have identically zero amplitudes in the parity-even ground state.

## 7. Findings and remaining limits

No counterexample found in the five attacked mechanisms: scalar energy corrections, normalization/gauge, excited-space degeneracy, edge differentiation, or pair-transition support. However, this is an argument-level audit. The exact normalized recurrence has not been written and mechanically checked coefficient-by-coefficient; the support-preservation step is not Lean formalized. No uniform-in-N constants, entropy/log branch closure, frozen-source reconciliation, or global B-C sign theorem is established.

**IV-17 disposition:** PASS for adversarial support-preservation reasoning under the finite-dimensional locally analytic ground-state setup; not a formal certificate.

**PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
