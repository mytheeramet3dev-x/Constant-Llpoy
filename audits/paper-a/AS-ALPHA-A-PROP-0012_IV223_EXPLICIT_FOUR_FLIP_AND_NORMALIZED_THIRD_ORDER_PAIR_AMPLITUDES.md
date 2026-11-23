# IV-223 — Explicit Four-Flip and Normalized Third-Order Pair Amplitudes

**Date:** 2026-11-23
**Target:** AS-ALPHA-A-PROP-0012, retained odd subsystem \{1,2\}, fixed finite N
**Status:** FOUR-FLIP SECOND-ORDER COEFFICIENT DERIVED / THIRD-ORDER PAIR COEFFICIENT RECURSION DERIVED / COEFFICIENT EVALUATION OPEN / NOT VERIFIED
**Scope:** Freeze explicit path multiplicities and denominators for four-flip amplitudes, and give a correct perturbative recursion for normalized third-order pair amplitudes. No quartic positivity or full claim is established.

## 1. Convention

Use
\[
H_0=-h\sum_j\sigma_j^x,\quad V=rW,\quad
W=-h\sum_{e}g_e\sigma_e^z,
\]
where an edge \(e=\{p,q\}\) toggles flip-set \(S\) to \(S\triangle e\). The unperturbed vacuum is \(|\varnothing\rangle\); for any nonempty flip-set, \(\Delta_S=E_0-E_S=-2h|S|\). This is nondegenerate ground-state perturbation theory for \(h>0\), finite N.

## 2. Four-flip target: exact second-order paths

Let \(T=\{a,b,c\}\subset\{3,\ldots,N\}\) and target \(S=\{i,a,b,c\}\), where \(i\in\{1,2\}\). A two-edge path from vacuum to S must use two disjoint edges whose union is S. There are exactly three perfect matchings:
\[
\{ia,bc\},\quad \{ib,ac\},\quad \{ic,ab\}.
\]
Each matching has two orderings, giving six ordered paths. The intermediate state is a two-flip state (gap 4h) and the target is a four-flip state (gap 8h); thus every ordered path has denominator
\[
(E_0-E_S)(E_0-E_m)=(-8h)(-4h)=32h^2.
\]
The numerator for each path is \(r^2h^2 g_e g_f\). Therefore the coefficient of \(r^2\) in the four-flip amplitude is
\[
D_{iT}=\frac{1}{32}\sum_{\text{six ordered paths}}g_eg_f
=\boxed{\frac1{16}(g_{ia}g_{bc}+g_{ib}g_{ac}+g_{ic}g_{ab})}.
\]
At uniform couplings, \(D_{iT}=3/16\). This is independently countable as 3 matchings × 2 orderings × 1/32 per path. No normalization correction enters at order r² for this amplitude.

## 3. Third-order pair-flip coefficient: recursion that includes all intermediate sectors

For a pair target \(n=\{i,k\}\), use intermediate-normalized perturbation coefficients
\[
|\psi(r)\rangle=|0\rangle+\sum_{S\ne\varnothing}c_S(r)|S\rangle,
\quad c_S(r)=r c_S^{(1)}+r^2c_S^{(2)}+r^3c_S^{(3)}+\cdots,
\]
with vacuum coefficient fixed to 1. Write \(W_{ST}=\langle S|W|T\rangle\), and let \(E(r)=E_0+rE_1+r^2E_2+\cdots\). In this convention, \(E_1=W_{00}=0\) and
\[
E_2=\sum_{m\ne0}W_{0m}c_m^{(1)}.
\]
The recursion from the eigenvalue equation (with sums over all non-vacuum intermediate flip sets connected by one edge) is
\[
c_n^{(1)}=\frac{W_{n0}}{\Delta_n},
\]
\[
c_n^{(2)}=\frac{\sum_{m\ne0}W_{nm}c_m^{(1)}-E_1c_n^{(1)}}{\Delta_n}
=\frac{\sum_{m\ne0}W_{nm}c_m^{(1)}}{\Delta_n},
\]
\[
\boxed{c_n^{(3)}=\frac{\sum_{m\ne0}W_{nm}c_m^{(2)}-E_2c_n^{(1)}}{\Delta_n}.}
\]
The third-order recursion includes all allowed intermediate configurations m (pair and four-flip sectors for a pair target), rather than retaining only pair-to-pair paths. It is a coefficient recursion, not yet an explicit closed path sum or numerical evaluation.

## 4. Conversion to normalized-state amplitude

Let
\[
Q=\sum_{S\ne0}|c_S^{(1)}|^2.
\]
The norm of the intermediate-normalized state is \(1+r^2Q+O(r^3)\), so multiplying by \(Z^{-1/2}\) gives normalized pair amplitude coefficient at order r³:
\[
\boxed{C_{ik}=c_{\{i,k\}}^{(3)}-\frac12Q c_{\{i,k\}}^{(1)}.}
\]
Normalization does not change the pair coefficient at order r², but it does change the order-r³ coefficient. Omitting this correction would affect the quartic odd-block coefficient in IV-222.

## 5. Cross-checks and limitations

- Four-flip paths: 3 matchings, 2 orderings each, denominator 32h²; all six contribute positively for uniform real g.
- Uniform four-flip coefficient: \(3/16\), cross-check by direct count.
- Third-order pair coefficient: recursion is derived directly from the intermediate-normalized eigenvalue equation and includes the second-order energy correction \(E_2\).
- The third-order recursion has not been exhaustively enumerated or evaluated for general edge weights or uniform coupling.
- No independent symbolic/computer implementation has yet cross-checked the recursion.
- Mapping the full normalized coefficients into IV-222's \(A,B,C,D\) requires consistent normalization and amplitude conventions throughout.
- \(\kappa\), its derivatives, strict quartic positivity, controlled remainder, entropy closure, global response sign, and Lean verification remain open.

## 6. Disposition

- Four-flip amplitude \(D_{iT}\): **DERIVED**.
- Path multiplicities and denominators: **DERIVED / COUNT CROSS-CHECKED BY MATCHING ENUMERATION**.
- Intermediate-normalized third-order pair coefficient recursion: **DERIVED**.
- Normalization correction to third-order pair amplitude: **DERIVED**.
- Explicit third-order pair coefficient evaluation and independent executable cross-check: **OPEN**.
- Quartic branch coefficient and positivity: **OPEN / NOT VERIFIED**.

## 7. Next obligation

IV-224 should independently enumerate the recursion's allowed intermediate flip-set paths and energy denominators (preferably using a small exact symbolic/executable cross-check for finite N), evaluate \(C_{ik}\) at the uniform point and edge directions, then assemble the IV-222 quartic coefficient without asserting positivity prematurely.
