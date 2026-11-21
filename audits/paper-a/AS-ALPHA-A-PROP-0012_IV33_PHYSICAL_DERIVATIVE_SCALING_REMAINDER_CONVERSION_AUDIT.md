# IV-33 — Physical-Derivative Scaling and Remainder Conversion Audit

**Target:** AS-ALPHA-A-PROP-0012, \(B-C\)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Audit dimensional conversion from dimensionless edge directions to physical coupling derivatives, and consistency of the candidate remainder scaling.

## 1. Parameter conversion

With \(J_e=J(1+u_e)\) at the uniform reference, the chain rule gives
\[
\partial_{u_e}=J\partial_{J_e},\qquad
\partial_{J_e}=J^{-1}\partial_{u_e}.
\]
This is exact for the specified parametrization, evaluated at the reference point.

## 2. Leading-order conversion

The displayed entropy bookkeeping gives a dimensionless-direction leading term
\[
\frac{r^2}{8}\ln\frac{q}{p},
\qquad r=J/h.
\]
Since \(r^2/J=J/h^2\), conversion yields
\[
\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}.
\]
Units are inverse energy, consistent with a derivative of dimensionless mutual information with respect to an energy-valued coupling.

## 3. Remainder conversion

If the dimensionless-direction remainder is controlled as
\[
O_N(r^3|\ln r|),
\]
then physical differentiation converts it to
\[
\frac1J O_N(r^3|\ln r|)
=O_N\left(\frac{J^2}{h^3}|\ln(J/h)|\right).
\]
This is dimensionally consistent with the leading term. The earlier conservative physical remainder stated in the working document is compatible with this conversion **only if** the underlying edge-differentiated entropy remainder is actually proved to have the assumed dimensionless order. IV-33 does not establish that estimate.

## 4. Logarithm and domain

The logarithm is \(\ln r\) with \(r=J/h\), a dimensionless ratio; no dimensional quantity is logged. The leading ratio \(q/p\) is also dimensionless. For fixed finite \(N\ge4\), \(2(N-2)/(N-1)>1\), so its logarithm is positive.

## 5. Disposition

- Chain-rule conversion: **PASS**.
- Leading dimensional scale \(J/h^2\): **PASS**.
- Remainder dimensional conversion, conditional on dimensionless derivative estimate: **PASS**.
- Actual dimensionless remainder estimate: **OPEN**, inherited from prior entropy/spectral audits.
- Uniform-in-N constants: **NOT CLAIMED**.
- Exact proposition / Lean: **NOT VERIFIED / NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 6. Next

IV-34: **Leading-Term Positivity and Fixed-N Asymptotic Dominance Audit** — verify the candidate logarithmic coefficient is strictly positive for the stated N range, and identify exactly what remainder bound would suffice to infer the sign for sufficiently small coupling without claiming a uniform threshold.
