# IV-224 — Independent Uniform Third-Order Path Enumeration

**Date:** 2026-11-23
**Target:** AS-ALPHA-A-PROP-0012, pair target p={i,k}, finite N>=4
**Status:** UNIFORM THIRD-ORDER PATH COUNTS AND COEFFICIENT DERIVED / SYMBOLIC ARITHMETIC CROSS-CHECKED / EDGE DERIVATIVES OPEN / NOT VERIFIED
**Scope:** Independently classify the intermediate flip-set states entering the third-order pair amplitude recursion from IV-223 and evaluate its uniform-coupling coefficient. This is a finite-N coefficient audit, not a controlled perturbation theorem.

## 1. Frozen convention

Take h=1 for coefficient evaluation, H0=-sum_j sigma_j^x, W=-sum_e g_e sigma_e^z sigma_e^z, and H=H0+rW. The vacuum coefficient of the intermediate-normalized state is fixed to one. For a nonempty flip-set S, Delta_S=E0-E_S=-2|S|. Recursion:
\[
c_n^{(1)}=W_{n0}/\Delta_n,\quad
c_n^{(2)}=\frac{\sum_{m\ne0}W_{nm}c_m^{(1)}}{\Delta_n},\quad
c_n^{(3)}=\frac{\sum_{m\ne0}W_{nm}c_m^{(2)}-E_2c_n^{(1)}}{\Delta_n},
\]
where E1=0 and E2=\sum_{m\ne0}W_{0m}c_m^{(1)}. Edge transitions toggle two vertices. This recursion is the starting point; path counts below independently classify all allowed m for a pair target.

## 2. Exhaustive intermediate-state classification for pair target

Let target p={i,k}. An intermediate state m is connected to p by one edge e, so m=p\triangle e. Exclude m=empty (which occurs for e=p and is handled through the energy correction, not the intermediate sum).

Exactly two classes remain:
- **Pair class P:** e shares exactly one vertex with p. Then m is another pair. There are 2(N-2) such edges/states. Each pair-state second-order coefficient at uniform g is b=(N-2)/8.
- **Four-flip class Q:** e is disjoint from p. Then m is a four-element flip-set containing p. There are binom(N-2,2) such states, one per outside edge. Each second-order four-flip coefficient is D=3/16 from IV-223.
No other flip-set cardinalities can occur in this recursion. This is exhaustive because an edge toggles exactly two vertices and the target has cardinality two.

## 3. Energy and third-order numerator at uniform coupling

The first-order pair coefficient is c_p^(1)=1/4. The second-order ground-energy coefficient is
\[
E_2=-\frac14\binom N2.
\]
The intermediate-state sum splits as
\[
\sum_{m\ne0}W_{pm}c_m^{(2)}
=-2(N-2)\frac{N-2}{8}
-\binom{N-2}{2}\frac3{16}
=-\frac{(N-2)^2}{4}-\frac3{16}\binom{N-2}{2}.
\]
Then
\[
c_p^{(3)}=\frac{\sum_m W_{pm}c_m^{(2)}-E_2c_p^{(1)}}{-4}
=\boxed{\frac{5N^2-23N+25}{64}}.
\]
The expression was independently simplified by exact symbolic arithmetic from the enumerated counts and terms.

## 4. Normalization correction

The first-order norm coefficient is
\[
Q=\sum_{S\ne0}|c_S^{(1)}|^2=\binom N2\frac1{16}.
\]
The normalized state is multiplied by 1-r²Q/2+O(r³). Thus the normalized third-order pair coefficient is
\[
C_p=c_p^{(3)}-\frac12Q c_p^{(1)}
=\boxed{\frac{19N^2-91N+100}{256}}.
\]
Checks: at N=4, c_p^(3)=13/64 and C_p=5/32. These checks verify arithmetic in this convention; they do not prove agreement with manuscript conventions or with a separately constructed reduced-block amplitude.

## 5. Status and limitations

- Intermediate-state classes P and Q exhaustive for pair target: **DERIVED**.
- Counts 2(N-2) and binom(N-2,2): **DERIVED**.
- Uniform E2 and third-order intermediate-normalized pair coefficient: **DERIVED**.
- Normalized third-order coefficient C_p: **DERIVED**.
- Exact arithmetic simplification cross-check: **PERFORMED**.
- Independently executable graph/path code and edge-derivative cross-check: **NOT PERFORMED**.
- Nonuniform edge-weight coefficient and u13/u34 derivatives: **OPEN**.
- IV-222 quartic M4, Schur coefficient kappa, positivity, analytic remainder, entropy closure, global sign, and Lean: **OPEN / NOT VERIFIED**.

## 6. Next obligation

IV-225 should compute the uniform quartic odd-block coefficient from the now-explicit normalized third-order pair coefficient and the four-flip amplitudes, while carefully separating the amplitude convention used in IV-222 from the normalized global state and checking whether additional sectors or normalization terms alter the mapping. Only after this convention reconciliation should kappa be evaluated.
