# IV-32 — Exact Edge-Direction Entropy Bookkeeping Audit

**Target:** AS-ALPHA-A-PROP-0012, \(B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}\)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Reconcile IV-31's leading-coefficient discrepancy by explicitly bookkeeping the entropy derivative contributions in both edge directions, using the leading branches displayed in the working derivation. This is a leading-order cross-check; it does not independently verify all spectral remainders.

## 1. Definitions and parameter conversion

\[
I_{12}=S(\rho_1)+S(\rho_2)-S(\rho_{12}),\quad
J_e=J(1+u_e),\
\partial_{J_e}=J^{-1}\partial_{u_e}\quad\text{at the uniform reference}.
\]

For binary small eigenvalue \(x\), \(H'(x)=-\ln x-1+O(x)\).

## 2. Edge 13: term-by-term leading bookkeeping

Working-source leading derivatives:
- Site 1: \(p_{1,u_{13}}=r^2/8+O_N(r^3)\).
- Site 2: \(p_{2,u_{13}}=O_N(r^3)\).
- Positive odd two-site branch: \(q_{u_{13}}=r^2/8+O_N(r^3)\).
- Even-block small branch and zero branch: no \(r^2\) leading entropy-derivative term under the prior conditional bounds.

Thus the leading logarithmic/regular contribution from the displayed branches is
\[
\frac{r^2}{8}(-\ln p-1)-\frac{r^2}{8}(-\ln q-1)
=\frac{r^2}{8}\ln(q/p).
\]
The regular \(-1\) terms cancel because the two leading directional derivatives are equal. Site 2 and other branches do not supply a displayed order-\(r^2\) term.

Since \(p=(N-1)r^2/16\), \(q=(N-2)r^2/8\), the logarithm is \(\ln[2(N-2)/(N-1)]\).

## 3. Edge 34: term-by-term leading bookkeeping

The working-source statements give:
- Both one-site derivatives \(p_{i,u_{34}}=O_N(r^3)\).
- Odd-block positive-branch derivative \(q_{u_{34}}=O_N(r^3)\).
- Even-block/small-spectrum contributions are at most their separately conditional \(O_N(r^4(1+|\ln r|))\)-type scale; the exact zero branch is not differentiated through \(\ln0\).

Therefore the edge-34 direction has no displayed order-\(r^2\) logarithmic or regular term. Its contribution is absorbed in the conservative higher-order remainder **provided** the differentiated remainders and low-spectrum entropy controls are valid.

## 4. Coefficient reconciliation

At the level of displayed leading branches and matching edge-13 derivative coefficients, the \(-1\) entropy constants cancel. The supported leading coefficient is therefore
\[
\boxed{\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}}
\]
rather than the earlier bracketed candidate with an extra \(+1\).

This resolves the *algebraic source* of the discrepancy in IV-31, but not the complete proposition: the underlying derivative/remainder assumptions are conditional and other spectral contributions still need rigorous closure.

## 5. Remaining uncertainty / status

- Leading displayed-branch edge-direction bookkeeping: **PASS algebraically**.
- Extra \(+1\) from the displayed leading branches: **NOT SUPPORTED; cancels**.
- Edge-34 absence of order-\(r^2\) contribution: **PASS at displayed leading order; higher terms conditional**.
- Complete even/zero/low-spectrum entropy derivative control: **OPEN**.
- Independent full derivation from the exact Hamiltonian and all block eigenvalues: **OPEN**.
- Lean formalization/build: **NOT PERFORMED**.
- Counterexample to the exact target proposition: **NOT ESTABLISHED**.

The corrected leading candidate is not promoted to theorem. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 6. Next

IV-33: **Physical-Derivative Scaling and Remainder Conversion Audit** — check the conversion \(\partial_{u_e}=J\partial_{J_e}\), dimensions, remainder scaling, and whether the conservative remainder is compatible with the leading candidate.
