# IV-67 — Fourth-Order Energy Correction: Closed Walks, Repeated Edges, and Vacuum Subtraction

**Status:** Analytic derivation with a single-edge exact consistency check; not Lean verified.

## 1. Vacuum return criterion
For pair edge operators \(W_e=\sigma_i^z\sigma_j^z\), an ordered four-edge sequence returns to the x-basis vacuum iff
\[
e_1\triangle e_2\triangle e_3\triangle e_4=\varnothing,
\]
equivalently every vertex has even incidence degree in the multigraph with edge multiplicities.

## 2. Valid four-operation vacuum-return multigraph types
The parity criterion permits:
- one edge used four times;
- two distinct edges each used twice;
- four distinct edges forming a 4-cycle.

A purported triangle-with-repeated-edge example (12),(12),(23),(31) is **not** vacuum-return: vertices 1 and 2 have odd degree (3). Reject this example. The parity criterion, not visual graph labels, governs classification.

## 3. Fourth-order recurrence and corrected energy expression
Under intermediate normalization, with \(E_1=0\):
\[
\psi_1=R_0V\psi_0,\quad \psi_2=R_0V\psi_1,\quad
\psi_3=R_0(V\psi_2-E_2\psi_1).
\]
Then \(E_4=\langle0|V|\psi_3\rangle\), so
\[
\boxed{E_4=\langle0|VR_0VR_0VR_0V|0\rangle
-E_2\langle0|VR_0^2V|0\rangle.}
\]
The vacuum projection in the chain is enforced by Q in each resolvent. The subtraction has \(R_0^2\); it is not \(E_2^2\). The latter was an erroneous intermediate expression and is corrected here.

## 4. Single-edge exact consistency check
For \(H=-h(\sigma_1^x+\sigma_2^x)-J\sigma_1^z\sigma_2^z\), exact ground energy:
\[
E_{\rm exact}=-\sqrt{4h^2+J^2}
=-2h-\frac{J^2}{4h}+\frac{J^4}{64h^3}+O(J^6).
\]
Thus \(E_2=-J^2/(4h)\), \(E_4=+J^4/(64h^3)\). In this one-edge case, the four-resolvent chain vanishes due to a projected intermediate vacuum; the correction term with \(E_2R_0^2\) reproduces the positive fourth-order coefficient. This is a hand-derived consistency check, not an independent code-based verification.

## 5. Remaining obligations
Complete explicit four-edge sequence enumeration under the parity rule, verify denominators for each surviving ordered path, derive a graph-support ledger, perform independent exact diagonalization/symbolic checks on small graphs, formalize in Lean. Proposition 0012 remains unproven.