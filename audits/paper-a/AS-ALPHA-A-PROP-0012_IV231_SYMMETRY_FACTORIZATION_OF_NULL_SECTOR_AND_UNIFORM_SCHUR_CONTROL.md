# IV-231 — Symmetry Factorization of the Null Sector and Uniform Schur Control

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, physical reduced odd block near the retained-site exchange-symmetric locus  
**Status:** CONDITIONAL FACTORIZATION LEMMA DERIVED / MODEL-SPECIFIC FACTORIZATION AND COEFFICIENTS OPEN / NOT LEAN-FORMALIZED  
**Scope:** Derive the precise symmetry-factorized entry structure that would make higher-order corrections controllable uniformly as the edge asymmetry \(u\to0\). This is a conditional matrix lemma, not a TFIM derivation.

## 1. Exchange symmetry and null coordinate

Write the physical symmetric block in the common/null basis:
\[
O(r,u)=\begin{pmatrix}L(r,u)&t(r,u)\\t(r,u)&s(r,u)\end{pmatrix}.
\]
Assume the model is invariant under retained-site exchange at \(u=0\), and the null/antisymmetric coordinate changes sign under that exchange. For an analytic coupling-dependent family whose perturbation \(u\) is exchange-odd, the entries obey:
- \(L(r,u)\) is even in \(u\);
- \(t(r,u)\) is odd in \(u\);
- \(s(r,u)\) is even in \(u\), with the exact symmetry-locus null \(s(r,0)=0\).

Consequently, analytic factorization gives \(t(r,u)=u\,\widehat t(r,u)\) and \(s(r,u)=u^2\,\widehat s(r,u)\), provided the exact null conditions and analyticity are valid for this block. The latter factorization needs the vanishing of both the value and first derivative at \(u=0\); symmetry plus \(s(r,0)=0\) gives this for an even analytic entry.

## 2. Uniformly scaled coefficient representation

Suppose the following quantitative bounds are verified in a neighborhood \(0<r<r_0,\ |u|<u_0\):
\[
L(r,u)\ge \ell r^2,\quad \ell>0,
\]
\[
t(r,u)=r^2u\,(\alpha+\delta_t(r,u)),
\]
\[
s(r,u)=r^2u^2\,(\beta+\delta_s(r,u)),
\]
where \(|\delta_t|\le K_t(r+|u|)\) and \(|\delta_s|\le K_s(r+|u|)\). Then the Schur complement is exactly
\[
S(r,u)=s-\frac{t^2}{L}
=r^2u^2\left[\beta+\delta_s-
\frac{(\alpha+\delta_t)^2}{L/r^2}\right].
\]
If also \(L/r^2\ge\ell\) and \(|L/r^2-\Lambda|\le K_L(r+|u|)\) for \(\Lambda>0\), then
\[
S(r,u)=r^2u^2\left(\beta-\frac{\alpha^2}{\Lambda}
+O(r+|u|)\right),
\]
where the error constant is controlled by the displayed bounds and \(\ell,\Lambda\). Therefore, if the physical coefficient
\[
\kappa_{\rm phys}=\beta-\frac{\alpha^2}{\Lambda}>0
\]
is independently computed and the remainder constant is \(K\), restricting to \(r+|u|<\kappa_{\rm phys}/(2K)\) yields \(S(r,u)\ge \frac12\kappa_{\rm phys}r^2u^2>0\) for \(u\ne0\). This would establish local strict positivity uniformly in the joint limit, excluding the symmetry point itself where the null eigenvalue is exactly zero.

## 3. Comparison with IV-228

IV-228 computes a positive coefficient for its specific first-order amplitude Gram. It does not establish \(\Lambda,\alpha,\beta\) for the full physical block. In particular, \(\kappa_{\rm phys}\) must be computed from normalized ground-state/environment amplitudes; it must not be replaced by IV-228's coefficient without a proven amplitude-to-block identity.

## 4. Disposition

- Conditional analytic symmetry factorization: **DERIVED** under stated parity/null assumptions.
- Uniform Schur-control implication: **DERIVED** under explicit quantitative remainder assumptions and positive \(\kappa_{\rm phys}\).
- Exact factorization for the TFIM block and actual values of \(\Lambda,\alpha,\beta\): **OPEN**.
- Physical odd-block positivity, global \(B-C>0\), full manuscript claim, and Lean formalization: **OPEN**.

Next audit: derive the exact physical reduced block as a Gram matrix from the normalized TFIM ground-state/environment amplitudes and determine whether the factorization hypotheses are true in the target convention.
