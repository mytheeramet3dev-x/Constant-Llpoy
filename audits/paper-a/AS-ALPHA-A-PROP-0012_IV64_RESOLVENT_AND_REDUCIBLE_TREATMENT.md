# IV-64 — Resolvent Structure and Reducible-Path Treatment

## 1. Scope
This audit formalizes the reduced-resolvent bookkeeping convention for perturbation paths in Paper A. It deliberately does not derive a full fourth-order target-state coefficient.

## 2. Hamiltonian split and unperturbed gaps
\[
H=H_0+V,\qquad H_0=-h\sum_i\sigma_i^x,\quad h>0,
\]
\[
V=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z.
\]
The unperturbed ground state is the all-\(+x\) state \(|0\rangle\). A flip set \(S\) has gap
\[
\Delta E(S)=E_S-E_0=2h|S|.
\]
A pair operation changes the parity set by symmetric difference with its endpoints.

## 3. Reduced resolvent convention
Let \(P=|0\rangle\langle0|\), \(Q=I-P\). Define the reduced resolvent at the ground energy:
\[
R_0=Q(E_0-H_0)^{-1}Q.
\]
For an excited flip state \(|S\rangle\), its diagonal factor is
\[
\langle S|R_0|S\rangle=-\frac{1}{2h|S|},\qquad S\ne\varnothing.
\]
The vacuum is excluded by Q; its denominator is not evaluated as zero. Therefore naive sequential products containing an intermediate vacuum are not terms of the ordinary reduced-resolvent chain.

## 4. Non-vacuum chain skeleton
A four-operation chain with non-vacuum intermediate states has a schematic matrix element
\[
\langle v|V R_0 V R_0 V R_0 V|0\rangle,
\]
where each intermediate state in the chain must lie in Q. This is only the chain contribution/skeleton. It is not asserted to equal the complete fourth-order coefficient of a normalized perturbed state. Depending on target and perturbation convention, other terms involving lower-order coefficients and energy/normalization corrections must be derived separately.

## 5. Vacuum-return classifications from IV-63
- Step-2 return: first two pair edges identical; the raw sequence has a vacuum at its second intermediate state.
- Step-3 return: three-edge triangle prefix returns to vacuum at the third intermediate state.
These sequences cannot be inserted into the chain above with a vacuum denominator. Their treatment is governed by the Q projection and by the full perturbative recurrence/correction terms, not by dropping them without accounting.

## 6. Obligation ledger
| Obligation | Status |
|---|---|
| Define P/Q exclusion of ground state | Formal convention specified |
| Excited-state resolvent gap | Derived from \(2h|S|\) |
| Identify vacuum intermediate sequences | IV-63 exhaustive combinatorial classification |
| Determine complete fourth-order target-state coefficient | OPEN |
| Derive reducible and energy-correction terms for target coefficient | OPEN |
| Derive normalization contribution | OPEN |
| Combine all paths and couplings | OPEN |
| Obtain reduced density entries and mutual information response B-C | OPEN |
| Lean formalization / verification | OPEN |

## 7. Important distinction
Excluding vacuum from the reduced resolvent is a formal definition, not proof that vacuum-return paths have no physical contribution. The complete perturbation expansion must account for their effects through the applicable recurrence/correction structure. This audit makes no correction formula claim.

**Paper A status: OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
