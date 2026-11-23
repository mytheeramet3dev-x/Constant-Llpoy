# IV-232 — Explicit Cubic Null Coefficient Under Single-Edge Asymmetry

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, retained sites 1,2; edge \(g_{13}=1+u\); other edges \(g=1\); finite \(N\ge4\)  
**Status:** CUBIC NULL COEFFICIENT EXPLICITLY EVALUATED / HIGHER-ORDER POSITIVITY OPEN / NOT LEAN-FORMALIZED  
**Scope:** Independently evaluate the IV-221 cubic null combination as a function of the single perturbation \(u\), using the stated independent-edge amplitude formulas. This is a coefficient computation in the perturbative amplitude model, not a physical finite-\(r\) positivity theorem.

## 1. Definitions

For retained \(i\in\{1,2\}\) and environment \(k\in\{3,\ldots,N\}\),
\[
a_{ik}=\frac{g_{ik}}4,\qquad
b_{ik}=\frac18\sum_{m\ne i,k}g_{im}g_{mk}.
\]
Define the cubic null coefficient
\[
Q_3(u)=\sum_{k=3}^N(a_{1k}-a_{2k})(b_{1k}-b_{2k}).
\]

Set \(g_{13}=1+u\), with every other edge equal to one.

## 2. Environment coordinate \(k=3\)

The first-order difference is
\[
a_{13}-a_{23}=\frac u4.
\]
For \(b_{13}\), the path sum excludes \(m=1,3\); all remaining edges on paths \(1-m-3\) equal one, so \(b_{13}=(N-2)/8\).
For \(b_{23}\), the path sum excludes \(m=2,3\). The path through \(m=1\) contributes \(g_{21}g_{13}=1+u\), while the remaining \(N-3\) paths contribute one:
\[
b_{23}=\frac{N-2+u}{8}.
\]
Thus
\[
b_{13}-b_{23}=-\frac u8,\qquad
(a_{13}-a_{23})(b_{13}-b_{23})=-\frac{u^2}{32}.
\]

## 3. Environment coordinates \(k\ge4\)

For each such \(k\), \(a_{1k}=a_{2k}=1/4\), so the first-order difference is zero and its contribution to \(Q_3\) vanishes, regardless of the second-order difference.

## 4. Exact cubic coefficient

Therefore, in this independent-edge model,
\[
\boxed{Q_3(u)=-\frac{u^2}{32}}
\]
for every finite \(N\ge4\). The cubic null contribution to the odd block is \(r^3Q_3(u)\) under the amplitude expansion convention of IV-221.

Consequences:
- At the uniform point \(u=0\), \(Q_3=0\).
- Its first derivative at \(u=0\) also vanishes.
- For nonzero \(u\), the cubic coefficient is negative.
- The cubic term alone cannot establish the physical block is negative; it competes with the positive quadratic \(r^2u^2\) coefficient and higher-order terms.

## 5. Cross-check and interpretation

This calculation is compatible with IV-221's zero cubic null coefficient and zero first edge derivative at the uniform point, while sharpening the result away from that point. The exact \(-u^2/32\) is a perturbative coefficient, not a controlled remainder bound. In particular, no finite-\(r\) sign conclusion follows without a bound on fourth and higher orders.

The cubic null coefficient is not symmetry-forbidden for the \(u_{13}\) direction. Its dependence begins quadratically in \(u\), and its sign is negative in the stated convention.

## 6. Disposition

- Explicit \(Q_3(u)\) in the single-edge model: **DERIVED**.
- Independence of \(N\) for this cubic coefficient: **DERIVED** under the formulas above.
- Cubic cancellation at \(u=0\) and vanishing first derivative there: **CONFIRMED**.
- Quartic Schur coefficient, physical finite-\(r\) positivity, global \(B-C\) sign, full manuscript mapping, and Lean formalization: **OPEN**.
