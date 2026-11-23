# IV-222 — Quartic Odd-Block Coefficient Reconstruction Framework

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, retained odd subsystem \(\{1,2\}\), fixed finite \(N\ge4\)  
**Status:** QUARTIC COEFFICIENT IDENTITY DERIVED / MODEL COEFFICIENTS NOT EVALUATED / REMAINDER OPEN / NOT VERIFIED  
**Scope:** Derive the exact bookkeeping obligations for the fourth-order odd-block coefficient after IV-221 establishes cubic null-branch cancellation at the uniform point. No strict quartic positivity, numerical validation, or Lean proof is claimed.

## 1. Why fourth order now becomes the next obligation

IV-221 derived \(B_{vv}=0\) at the uniform point and its first edge derivatives for the explicit amplitude convention. The odd block therefore has the expansion
\[
O(r)=r^2M_2+r^3M_3+r^4M_4+O(r^5),
\]
with \(M_2\) rank one at the uniform point and \((M_3)_{vv}=0\). This makes the fourth-order small-branch coefficient the next algebraic target, but it does not automatically establish a controlled remainder or strict positivity.

## 2. Environment sectors that contribute through fourth order

For retained-odd basis index \(i\in\{1,2\}\), the global x-basis flip set has odd cardinality. Through fourth order in the reduced-block products, two environment sectors contribute:

- Environment one-flip sets \(\{k\}\), \(k\ge3\): their pair-flip global amplitudes have expansions through third order.
- Environment three-flip sets \(T\subset\{3,\ldots,N\}\), \(|T|=3\): their four-global-flip amplitudes begin at second order, so their Gram products enter at order \(r^4\).

Environment five-flip amplitudes first arise at order at least three and their squared contributions are at least order \(r^6\), so they do not affect the quartic coefficient.

## 3. Amplitude-coefficient notation and normalization

Write normalized amplitudes in the one-environment-flip sector as
\[
c_{ik}(r)=rA_{ik}+r^2B_{ik}+r^3C_{ik}+O(r^4),
\]
and three-environment-flip sector as
\[
d_{iT}(r)=r^2D_{iT}+O(r^3).
\]
Here \(C_{ik}\) must include the normalized-state correction. If intermediate-normalized perturbation theory is used, the second-order norm correction contributes to the third-order one-flip coefficient; omitting it would corrupt the quartic reduced-block term. The coefficients are definitions of required data, not evaluated numbers.

## 4. Reduced odd-block coefficients

Taking the environment Gram sum gives
\[
(M_2)_{ij}=\sum_k A_{ik}\overline{A_{jk}},
\]
\[
(M_3)_{ij}=\sum_k(A_{ik}\overline{B_{jk}}+B_{ik}\overline{A_{jk}}),
\]
and the fourth-order coefficient
\[
\boxed{
(M_4)_{ij}=\sum_k
(A_{ik}\overline{C_{jk}}+C_{ik}\overline{A_{jk}}+
B_{ik}\overline{B_{jk}})
+\sum_{|T|=3}D_{iT}\overline{D_{jT}}.
}
\]
The first sum is over environment single-flip configurations \(k\ge3\), and the second over all environment triple-flip sets. This is a coefficient identity from the Gram construction. Contributions from higher environment sectors are beyond fourth order.

## 5. Schur/eigenvalue coefficient

At the uniform point, choose the leading normalized eigenbasis \(u=(1,1)/\sqrt2\), \(v=(1,-1)/\sqrt2\) so that
\[
M_2=\begin{pmatrix}a_+&0\\0&0\end{pmatrix},\quad a_+>0.
\]
Given IV-221's pointwise cubic null result \((M_3)_{vv}=0\), formal matrix perturbation yields
\[
\lambda_{\rm small}(r)=r^4\kappa+O(r^5),\qquad
\boxed{\kappa=(M_4)_{vv}-\frac{|(M_3)_{uv}|^2}{a_+}.}
\]
The negative Schur correction is essential: quartic positivity cannot be inferred from \((M_4)_{vv}\) alone. PSD of the exact Gram block implies nonnegative small eigenvalue for physical \(r\), but does not by itself give a strictly positive coefficient \(\kappa\) without evaluating the coefficient and establishing the branch expansion.

## 6. Edge derivatives and remaining coefficient obligations

For \(u_q\in\{u_{13},u_{34}\}\), a coefficient-level derivative requires evaluating
\[
\partial_{u_q}\kappa
=\partial_{u_q}(M_4)_{vv}
-\partial_{u_q}\left(\frac{|(M_3)_{uv}|^2}{a_+}\right),
\]
including derivatives of normalized third-order one-flip amplitudes \(C_{ik}\), second-order amplitudes \(B_{ik}\), and four-flip/three-environment amplitudes \(D_{iT}\). None of those full model coefficient sets has been evaluated in this audit.

The following remain open:
- explicit normalized third-order pair-flip amplitudes \(C_{ik}\);
- explicit second-order four-flip amplitudes \(D_{iT}\), with all pair-path multiplicities and denominators;
- numerical/algebraic evaluation of \((M_4)_{vv}\), \((M_3)_{uv}\), and \(a_+\);
- explicit edge derivatives of all quartic terms;
- proof of \(\kappa>0\), or determination of whether it vanishes and the branch begins later;
- rigorous analytic remainder bounds and entropy/log derivative closure;
- global \(B-C\) sign theorem;
- Lean or executable verification.

## 7. Disposition

- Fourth-order environment-sector bookkeeping: **DERIVED**.
- Quartic reduced-block coefficient identity: **DERIVED**.
- Schur coefficient formula after cubic null cancellation: **DERIVED FORMALLY / COEFFICIENTS OPEN**.
- Strict quartic branch positivity: **OPEN**.
- Model-specific quartic coefficients and edge derivatives: **OPEN**.
- Controlled remainder, entropy response, and full PROP-0012 claim: **OPEN / NOT VERIFIED**.

## 8. Next obligation

IV-223 should explicitly enumerate the second-order four-global-flip amplitudes \(D_{iT}\) for each environment triple and the third-order normalized pair-flip coefficients \(C_{ik}\). Prioritize an exact symbolic path enumeration for finite \(N\) and independently cross-check path multiplicities/energy denominators before substituting into \(M_4\).
