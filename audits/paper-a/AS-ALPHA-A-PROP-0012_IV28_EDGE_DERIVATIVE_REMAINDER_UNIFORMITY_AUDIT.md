# IV-28 — Edge-Derivative Remainder Uniformity Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Verify which derivative-order claims follow from joint analyticity and uniform neighborhoods, and identify what the current working derivation actually states.

## 1. Current analytic setup

The working derivation states that, for fixed finite \(N\), the ground-state projector is jointly analytic in coupling \(r\) and independent edge variables \(\mathbf u\) in a sufficiently small neighborhood of the uncoupled point, based on the isolated ground state and gap at \(r=0\). It also asserts that first edge derivatives of the displayed amplitude expansions/remainders are included.

This is a legitimate route to derivative remainder control only when the expansion and remainder bounds are uniform on an edge-variable neighborhood (or are obtained from a common complex analytic neighborhood).

## 2. Cauchy derivative principle

If a remainder \(R(r,\mathbf u)\) is holomorphic in a complex neighborhood in \(u_e\), and \(|R|\le C_N|r|^k\) uniformly on a circle of radius \(\delta\) around the evaluation point, Cauchy's estimate gives
\[
|\partial_{u_e}R(r,\mathbf u)|\le \frac{C_N}{\delta}|r|^k.
\]
Thus the same power of \(r\) is preserved for edge differentiation, but constants depend on the neighborhood radius and finite \(N\). This conclusion does not follow from a pointwise real-variable \(O(r^k)\) statement alone.

## 3. Uniformity caveats

- The edge neighborhood must remain inside the analytic/gap region.
- The radius used for Cauchy bounds must be uniform for the evaluation set, not shrink uncontrolled with \(r\).
- Constants may depend on fixed finite \(N\); no uniform-in-\(N\) claim follows.
- The remainder must be genuinely holomorphic/analytic in edge variables, not merely continuous or pointwise bounded.
- If derivatives are asserted after a spectral decomposition, cluster/eigenbranch regularity and gap conditions are additional obligations; analyticity of the full projector does not guarantee globally analytic labeling of individual eigenvalues through degeneracies.

## 4. Adversarial result

The working document explicitly states a joint analytic setup and first-edge-derivative expansions, but IV-28 does not independently derive the required complex neighborhood radius, quantitative Cauchy constants, or verify every remainder in the amplitude recursion. Therefore the analytic principle is valid, while its full application to every ledger remainder remains conditional.

## 5. Disposition

- Joint finite-\(N\) analytic ground-state projector premise: **PASS as stated setup, subject to explicit neighborhood/gap proof in source**.
- Uniform edge-variable Cauchy derivative estimate: **PASS as a mathematical implication under the stated holomorphic bound**.
- Pointwise \(O(r^k)\) implies same-order derivative: **FAIL (not implied)**.
- Full remainder ledger independently certified by common analytic neighborhood: **OPEN**.
- Spectral low-branch/logarithmic remainder after differentiation: **OPEN**.
- Counterexample to exact target proposition: **not established**.
- Lean formalization/build: **not performed**.

## 6. Disposition

IV-28 clarifies that the same perturbative power after edge differentiation can be justified by Cauchy estimates, but only from a uniform holomorphic remainder bound on a common edge neighborhood. The working source claims joint analyticity and differentiated expansions; the complete quantitative neighborhood/remainder ledger has not been independently certified here. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 7. Next

IV-29: **Analytic Ground-State Projector and Gap-Neighborhood Audit** — check the isolated-ground-state perturbation argument, parameter domain, spectral gap persistence, projector analyticity, and finite-N dependence of constants.
