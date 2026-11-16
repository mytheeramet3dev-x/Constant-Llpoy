# Internal Analytic Review — General-Edge \(B-C\) Strong-Coupling Proof

**Target:** Fixed-\(N\) strong-coupling asymptotic for \(B-C\) at the uniform all-to-all TFIM point.  
**Proof under review:** working/paper-a/GENERAL_EDGE_B_MINUS_C_DERIVATIVE_PROOF.md  
**Supporting uniform coefficient:** audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md  
**Numerical cross-check:** audits/paper-a/EDGE_RESPONSE_FINITE_DIFFERENCE_DIAGNOSTIC.md  
**Review type:** Internal mathematical audit; not a Lean proof and not an external referee report.

## 1. Hypotheses checked

The proof requires:
- fixed finite \(N\ge4\);
- uniform reference coupling \(J>0\);
- a sufficiently small real neighborhood in which every \(J_{ij}>0\);
- \(\varepsilon=h/J\to0^+\);
- response derivatives evaluated at the uniform point in the ambient real edge-coupling space.

These hypotheses keep every nontrivial Ising cut gap positive and permit two-sided edge perturbations around the uniform point.

## 2. Step-by-step review

| Step | Obligation | Review |
|---|---|---|
| 1 | Isolated even-parity cat eigenvalue in a positive-coupling neighborhood | **PASS** — every nontrivial cut has positive energy; on a smaller compact neighborhood the gap has a positive lower bound. |
| 2 | Joint analyticity in \(\varepsilon\) and independent edge variables | **PASS** — finite-dimensional analytic matrix family with a simple isolated eigenvalue in the even sector. |
| 3 | First-order amplitude \(b_i=h/[2\sum_{j\ne i}J_{ij}]\) | **PASS** — single-spin-flip gap is \(2\sum_{j\ne i}J_{ij}\), and the perturbation matrix element is \(-h\). |
| 4 | Two-site parity block decomposition | **PASS** — global bit-flip parity commutes with the Hamiltonian and induces the two \(2\times2\) blocks. |
| 5 | First-order partial-trace entries | **PASS** — the environment-all-zero/all-one amplitudes give \(X_\pm=(b_1\pm b_2)/2+O(\varepsilon^3)\) and \(S_\pm=(b_1\pm b_2)^2/2+O(\varepsilon^4)\). |
| 6 | Cancellation of the order-\(\varepsilon^2\) Schur term | **PASS** — \(S_\pm-X_\pm^2/L_\pm=O(\varepsilon^4)\) identically in the nearby edge variables. |
| 7 | Differentiated small-eigenvalue order | **PASS** — joint analyticity plus the identity cancellation makes each small branch \(\varepsilon^4a_\pm(\mathbf u)+O(\varepsilon^6)\), so \(\partial_{u_e}\lambda_\pm=O(\varepsilon^4)\). |
| 8 | Positive small branch logarithm | **PASS** — the uniform coefficient \(c_N>0\) gives a two-sided \(\lambda_+\asymp_N\varepsilon^4\) bound in a smaller neighborhood. |
| 9 | Zero small branch logarithm | **PASS** — at the uniform point the branch is exactly zero and nonnegative in every real edge direction; analyticity gives quadratic-or-higher opening, so the first directional derivative of \(-\lambda\ln\lambda\) is zero. |
| 10 | Large-eigenvalue entropy derivative | **PASS** — the large branches are even analytic, equal \(1/2\) at \(\varepsilon=0\) for all nearby couplings, and their first edge derivatives are \(O(\varepsilon^2)\); trace conservation cancels the constant first-derivative term to order \(O(\varepsilon^4)\). |
| 11 | One-site leading response | **PASS** — differentiating \(-2b_i^2\) gives \(h^2/R_i^3\) for an incident edge and zero for a disjoint edge. |
| 12 | Full \(B-C\) subtraction | **PASS** — the positive one-site term dominates the \(O_N(\varepsilon^4|\ln\varepsilon|/J)\) two-site entropy derivative remainder. |

## 3. Central entropy issue: zero eigenvalue branch

This is the delicate point and must remain explicit in any future Lean statement or manuscript proof.

For fixed \(\varepsilon>0\), let \(t\mapsto\lambda_-(\varepsilon,t)\) be the small eigenvalue branch along any real edge direction through the uniform point. Positivity of the reduced density matrix gives \(\lambda_-(\varepsilon,t)\ge0\), and permutation symmetry gives \(\lambda_-(\varepsilon,0)=0\). Thus \(t=0\) is an interior minimum and analyticity implies

\[
\lambda_-(\varepsilon,t)=O_{\varepsilon}(t^2).
\]

Consequently,

\[
-\lambda_-(\varepsilon,t)\ln\lambda_-(\varepsilon,t)
=O_{\varepsilon}(t^2|\ln|t||),
\]

whose first derivative at \(t=0\) is zero. This avoids the invalid step of bounding \(|\ln\lambda_-|\) by a fourth-order upper bound. The positive branch is treated separately using its strictly positive fourth-order coefficient.

## 4. Result

The internal review finds no remaining gap in the proposed fixed-\(N\) leading asymptotic, provided the joint-analyticity neighborhood and the displayed first-order block expansions are included as hypotheses/lemmas exactly as written.

The derived result is

\[
B-C
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(
\frac{h^4}{J^5}
\left[1+\left|\ln(h/J)\right|\right]
\right).
\]

Hence, for each fixed finite \(N\ge4\), there exists some \(\varepsilon_N>0\) such that \(B-C>0\) whenever \(0<h/J<\varepsilon_N\).

**Review disposition:** INTERNAL ANALYTIC REVIEW PASS — fixed finite \(N\), local strong-coupling regime.  
**Not claimed:** explicit \(\varepsilon_N\); uniformity in \(N\); positivity away from the strong-coupling endpoint; global \(B-C>0\); Lean verification; source/manuscript correspondence.

## 5. Independent numerical diagnostic

The full-Hilbert-space finite-difference diagnostic for \(N=4,5,6\) shows the ratio of the computed \(B-C\) to \(h^2/[J^3(N-1)^3]\) approaching \(1\) as \(h/J\to0\). This supports the coefficient but is not used as proof.

## 6. Repository and source boundary

- All proof and audit files are in Constant Llapoy.
- No source snapshot was edited.
- No Absolute Symmetry branch, file, or commit was changed.
- No manuscript claim status is promoted to fully Verified by this internal review.
