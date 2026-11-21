# IV-100 — Middle Reduced State: Exact Expansion Audit

Status: ANALYTIC PARTIAL. This note provides a compact symmetry-based reduction and coefficient check; it does not claim a Lean proof.

## 1. Hamiltonian in the X-product basis
Let \(|0\rangle,|1\rangle\) denote X eigenstates with eigenvalues +1,-1. The unperturbed Hamiltonian is \(H_0=-h\sum_i X_i\), ground state \(|000\rangle\), energy \(-3h\). The perturbation flips two bits:
\[
V=-J_{12}(Z_1Z_2)-J_{23}(Z_2Z_3).
\]
Each pair flip connects \(|000\rangle\) to \(|110\rangle\) or \(|011\rangle\) with gap \(4h\).

## 2. First-order vector and reduced state
Set \(a=J_{12}/(4h)\), \(b=J_{23}/(4h)\). To first order,
\[
|\psi\rangle=|000\rangle+a|110\rangle+b|011\rangle+O(J^2).
\]
Tracing spins 1 and 3, the middle-spin marginal has flipped probability \(a^2+b^2+O(J^4)\). Its off-diagonal entry vanishes through this order: middle-bit sectors have endpoint states whose overlaps with the unperturbed endpoint vector are zero at first order. Thus
\[
\rho_2=\begin{pmatrix}1-a^2-b^2& O(J^3)\\O(J^3)&a^2+b^2\end{pmatrix}
\]
in the X basis, with the displayed diagonal terms understood only through quadratic order, not as a complete fourth-order expansion. Symmetry under independent sign changes of \(J_{12},J_{23}\) further restricts the eigenvalues to analytic even functions in each coupling.

## 3. Small eigenvalue to quadratic order
For a trace-one 2x2 state with diagonal flipped probability \(s=a^2+b^2+O(J^4)\) and off-diagonal \(c\), the small eigenvalue is
\[
q=\frac{1-\sqrt{(1-2s)^2+4|c|^2}}2.
\]
If \(c=O(J^3)\), then \(|c|^2=O(J^6)\); hence it does not change the quadratic term. Therefore
\[
q=a^2+b^2+O(J^4)=x+y+O((x+y)^2)
\]
locally, using fixed \(h>0\) and analyticity.

## 4. What is not computed
The normalized state coefficients through second order and reduced-state entries through fourth order have not been fully expanded. Consequently the exact coefficients of \(x^2,xy,y^2\) in \(q\) are not reported. The expression above supports the quadratic coefficient only. The stated off-diagonal order is a perturbative estimate to be checked explicitly in the full expansion.

## 5. Verification plan
- Compute second-order amplitudes and normalization consistently.
- Construct \(\rho_2\) from the truncated normalized state and retain terms to fourth order.
- Derive \(q\) using trace and determinant.
- Validate the fourth-order coefficients with independent high-precision diagonalization.
- Keep Paper A / Proposition 0012 OPEN until all analytic and proof-assistant obligations are discharged.
