# IV-21 — Spectral Projection Differentiability, Gap Dependence & Cluster Boundary Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** analytic threat-model review; no mechanized proof claimed

## Scope

Test whether the small spectral cluster invoked in IV-20 can be isolated uniformly in the edge parameter, whether its projector derivative is controlled, and what happens when the cluster gap collapses or the cluster boundary is crossed.

## 1. Riesz-projector derivative is gap-dependent

For a finite-dimensional Hermitian matrix family \(H(u)\), an isolated spectral cluster projector can be represented locally by a contour integral
\[
P(u)=\frac{1}{2\pi i}\oint_\Gamma(z-H(u))^{-1}\,dz.
\]
Differentiating gives
\[
P_u=\frac{1}{2\pi i}\oint_\Gamma(z-H)^{-1}H_u(z-H)^{-1}\,dz.
\]
If the contour remains separated from the spectrum by distance \(\delta>0\), a resolvent estimate yields a bound scaling with inverse powers of \(\delta\) and contour geometry. Therefore, uniform projector-derivative control requires a uniform gap and a controlled contour, not merely pointwise isolation.

## 2. Gap collapse obstruction

As \(\delta\to0\), these estimates may diverge. At a cluster-boundary crossing, a fixed-rank cluster projector may cease to be differentiable or may no longer be uniquely defined. Aggregation across eigenvalue crossings internal to a cluster is stable as a concept, but crossing the chosen boundary is a different issue.

## 3. Entropy does not remove the projector obligation

The entropy is a function of the full density matrix and does not depend on labels of eigenvalues. Nevertheless, using a cluster decomposition in a proof introduces a projector and cluster boundary. The proof must either establish the gap/projector assumptions or avoid the cluster split and prove a direct full-spectrum bound.

## 4. Audit checks

- Is cluster isolated uniformly over the edge-parameter neighborhood? **Not established from available derivation.**
- Is the gap lower bound independent of weak-coupling parameter \(r\)? **Not established.**
- Is the projector derivative bound uniform? **Not established; contour/resolvent constants depend on gap.**
- Can boundary crossings invalidate a fixed cluster? **Yes, if no separation assumption is available; this is a structural obstruction to that proof route.**
- Does this refute the target proposition? **No. It identifies a missing premise for the cluster method.**

## 5. Disposition

- Local isolated-cluster differentiability: **conditional PASS under spectral separation**.
- Uniform cluster projector differentiability: **OPEN**.
- Gap-independent cluster derivative bound: **not justified**.
- Cluster-boundary crossing: **proof-route obstruction unless avoided or controlled**.
- Counterexample to exact target formula: **not established**.
- Lean formalization/build: **not performed**.

## 6. Next

IV-22: **Gap-Free Full-Spectrum Entropy Derivative Estimate Audit** — investigate a route that avoids fixed-rank cluster projectors and branch tracking, directly bounding the full normalized entropy derivative under only premises already justified for Paper A.
