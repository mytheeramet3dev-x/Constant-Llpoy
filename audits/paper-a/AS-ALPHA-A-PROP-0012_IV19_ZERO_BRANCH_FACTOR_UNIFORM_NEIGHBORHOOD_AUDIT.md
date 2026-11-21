# IV-19 — Independent Zero-Branch Factorization & Uniform Neighborhood Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign (B-C)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** adversarial analytic audit; no Lean or numerical proof claims

## Scope

This audit tests the entropy derivative remainder when an eigenbranch's leading coefficient vanishes, and whether an estimate near a zero branch can be uniform in an edge parameter (u).

## Findings

### 1. An (O(r^4)) branch bound alone does not control its logarithmic derivative

Knowing only (0\le \lambda(u,r)\le Cr^4) is insufficient to infer a uniform bound for \(\lambda_u\), or for \(\lambda_u\ln\lambda\). Derivative control is a separate obligation.

### 2. Positive-scale branch

If on a specified neighborhood
\[
\lambda(u,r)=r^4a(u,r),\qquad 0<c\le a(u,r)\le C,
\]
and \(a_u\) is bounded, then
\[
\partial_u[-\lambda\ln\lambda]
=-r^4a_u(4\ln r+\ln a+1)
=O(r^4(1+|\ln r|)).
\]
This is conditional and neighborhood-specific.

### 3. Zero-leading-coefficient branch

If \(a(u_0,0)=0\), the positive-scale hypothesis fails at \(u_0\). A factorization with bounded analytic factor may still exist, but its vanishing order and dependence on \(u-u_0\) must be established; the positive-scale estimate cannot be carried across the zero by assertion.

For a nonnegative differentiable eigenvalue at an interior zero, \(\lambda_u(u_0,r)=0\) for fixed \(r\) when the zero is a local minimum. This pointwise fact alone does not provide a uniform neighborhood estimate for \(\lambda_u\ln\lambda\).

### 4. Finite-order vanishing versus flat behavior

Analyticity can constrain branch behavior to finite-order vanishing (or an identically-zero branch) under suitable analytic spectral hypotheses, but the audit does not establish those hypotheses for the exact entropy eigenbranch, nor does it derive uniform factorization in the joint parameters. Puiseux behavior, branch crossings, and parameter neighborhoods need to be handled explicitly if present.

### 5. Trace normalization

Trace normalization may cancel additive derivative contributions across the full spectrum, but it cannot by itself bound a small branch's individual \(\lambda_u\ln\lambda\) term. The cancellation must be shown in the normalized full entropy expression and must not be used to silently discard branch-local remainder estimates.

## Obstruction / open proof obligation

The uniform entropy remainder across a zero-leading-coefficient branch is **not closed**. Required additional input: a joint branch decomposition or controlled spectral cluster, a proven vanishing-order/factorization statement, and derivative bounds on the factor with a neighborhood/range explicit. Alternatively, derive a direct bound for the aggregate entropy derivative of the small spectral cluster without relying on branchwise logarithmic estimates.

## Status by obligation

- Positive-scale logarithmic remainder: **CONDITIONAL PASS**.
- Zero-leading coefficient and uniform-neighborhood estimate: **OPEN**.
- (O(r^4)) alone implying derivative/log control: **FAIL (insufficient premise)**.
- Trace normalization as a substitute for branch control: **FAIL (not sufficient)**.
- Counterexample to the exact target formula: **not established**.
- Global \(B-C>0\): **not proved**.
- Mechanized verification / Lean build: **not performed**.

## Next

IV-20: **Aggregate Small-Spectral-Cluster Entropy Derivative Audit** — investigate whether cluster-level entropy estimates avoid branchwise factorization difficulties and identify the assumptions required for a uniform bound.
