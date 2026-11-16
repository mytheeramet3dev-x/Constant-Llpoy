# Internal Analytic Review — Corrected Weak-Coupling \(B-C\) Asymptotic

**Target:** Fixed-\(N\) weak-coupling response at the uniform all-to-all TFIM point.  
**Proof under review:** working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md  
**Reusable entropy lemma:** audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md  
**Source snapshots:** source_snapshots/paper-a/docs/lemma_5_2_proof.md and lemma_5_2_audit.md  
**Review type:** Internal analytic review; not Lean formalization or external referee report.

## 1. Source conflict

The original supporting Lemma 5.2 concludes \(B-C<0\) by retaining only diagonal entries of the order-\(r^2\) odd pair block. This omits

\[
\rho_{-+,+-}=\sum_{k\ge3}a_{1k}a_{2k}.
\]

At the uniform point this coherence makes the block rank one at leading order, with eigenvalues \(2(N-2)w\) and \(0\). The corrected sign is therefore positive, not negative. The later source audit identified this sign correction but did not bound the differentiated remainder.

## 2. Step-by-step review

| Step | Obligation | Review |
|---|---|---|
| 1 | Unique transverse-field ground state and joint analyticity | **PASS** — at zero coupling the ground state is simple and gapped; finite-dimensional analytic perturbation applies to independent edge variables. |
| 2 | First-order pair-flip amplitude \(a_{ij}=J_{ij}/(4h)\) | **PASS** — the pair-flip energy gap is \(4h\) and the perturbation matrix element is \(-J_{ij}\). |
| 3 | One-site small eigenvalue \(p_i=\sum_{j\ne i}a_{ij}^2+O(r^3)\) | **PASS** — the one-site state is diagonal in the \(x\)-basis; the expansion and its edge derivatives are jointly analytic. |
| 4 | Full odd-block coherence | **PASS** — the Gram matrix includes \(\sum a_{1k}a_{2k}\); omitting it changes the leading eigenvalue and sign. |
| 5 | Positive odd-block eigenvalue \(q\) | **PASS** — after factoring \(r^2\), its leading eigenvalue is simple and positive at the uniform point, so the branch is analytic and \(q\asymp_N r^2\). |
| 6 | Shared-edge derivative of \(q\) | **PASS** — the eigenvector \((1,1)/\sqrt2\) gives \(\partial_{u_{13}}q=r^2/8+O(r^3)\). |
| 7 | Disjoint-edge derivative of \(q\) | **PASS** — \(J_{34}\) is absent from the leading Gram matrix, so its derivative is \(O(r^3)\). |
| 8 | Small eigenvalue of the \((++ , --)\) block | **PASS** — the order-\(r^2\) Schur term cancels; the conservative jointly analytic bound \(O(r^3)\) is sufficient. |
| 9 | Entropy derivatives of zero/rank-changing branches | **PASS** — handled by the separate analytic nonnegative-eigenvalue entropy lemma, not by an invalid logarithmic upper bound. |
| 10 | Pair entropy remainder derivative | **PASS** — replacing the pair large eigenvalue by \(1-q\) leaves an \(O(r^3|\ln r|)\) edge-derivative remainder. |
| 11 | One-site derivatives | **PASS** — \(\partial_{u_{13}}p_1=r^2/8+O(r^3)\), while the other leading edge derivatives vanish. |
| 12 | Cancellation of logarithms and leading coefficient | **PASS** — the common \(r^2/8\) derivative cancels the \(-\ln r^2\) terms, leaving \(\ln(2(N-2)/(N-1))\). |

## 3. Result

The internally reviewed candidate asymptotic is

\[
B-C
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)
+O_N\!\left(
\frac{J^2}{h^3}
\left[1+\left|\ln(J/h)\right|\right]
\right).
\]

For every fixed finite \(N\ge4\), the logarithm is positive and the relative remainder is \(O_N((J/h)|\ln(J/h)|)\to0\). Therefore \(B-C>0\) for sufficiently small \(J/h>0\).

The conservative remainder is intentionally weaker than the \(O(J^3/h^4)\) remainder claimed in the old source proof. No stronger order is adopted without a separate derivation.

**Review disposition:** INTERNAL ANALYTIC REVIEW PASS — fixed finite \(N\), local weak-coupling regime.  
**Not claimed:** an explicit threshold; uniformity in \(N\); global positivity for all \(J/h\); Lean verification; proof-to-manuscript correspondence.

## 4. Numerical consistency

The full-Hilbert-space high-precision finite-difference calculations for \(N=4,5,6\) show the ratio of \(B-C\) to the corrected leading term approaching \(1\) as \(J/h\to0\). The observed finite-\(J\) corrections are substantial, consistent with retaining the conservative \(O((J/h)|\ln(J/h)|)\) relative remainder.

## 5. Repository boundary

All new proof and audit work is stored in Constant Llapoy. The source proof and source audit are preserved as immutable snapshots. No Absolute Symmetry file or branch was modified.
