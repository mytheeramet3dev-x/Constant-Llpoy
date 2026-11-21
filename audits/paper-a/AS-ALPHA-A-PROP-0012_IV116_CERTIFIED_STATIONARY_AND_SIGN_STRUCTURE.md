# IV-116 — Certified stationary point and sign structure of Phi

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** analytic convexity proof plus numerical root location; function-level result only.

## Function

For r>0:
\[
\Phi(r)=(3-2r+3r^2)\ln(1+r)+(5r-3r^2)\ln r+\frac12+r.
\]

## Exact derivative

Differentiation and simplification gives
\[
\Phi'(r)=\frac{
-6r^2\ln r+6r^2\ln(1+r)-r\ln r+4r\ln(1+r)
+r+5\ln r-2\ln(1+r)+9}{r+1}.
\]

A compact expression for the second derivative is
\[
\Phi''(r)=\frac{N(r)}{r(r+1)^2},
\]
where
\[
N(r)=6r(r+1)^2\ln(1+1/r)-3r^2-6r+5.
\]

## Convexity certificate

For all r>0, the standard logarithm inequality
\[
\ln(1+x)>\frac{x}{1+x}\quad(x>0)
\]
applied to x=1/r gives
\[
\ln(1+1/r)>\frac1{r+1}.
\]
Therefore
\[
6r(r+1)^2\ln(1+1/r)>6r(r+1),
\]
and consequently
\[
N(r)>6r(r+1)-3r^2-6r+5=3r^2+5>0.
\]
Since r(r+1)^2>0, this proves \(\Phi''(r)>0\) on the entire positive domain. Thus Phi is strictly convex, and Phi' is strictly increasing.

## Endpoint derivative behavior

From the exact derivative, \(\Phi'(r)\to-\infty\) as r->0+ and \(\Phi'(r)\to+\infty\) as r->infinity. Combined with strict monotonicity, Phi' has exactly one zero; Phi has exactly one global minimizer.

## Numerical location (not an exact closed form)

A bracketed numerical root of Phi' gives
\[
r_*\approx0.1492465750171368,
\quad\Phi(r_*)\approx-0.25800248676068105.
\]
This numerical location/value are not interval-certified. Strict convexity and uniqueness, however, are analytically proved.

## Sign structure

Because \(\Phi(r)\to1/2\) as r->0+ and \(\Phi(r)\to+\infty\) as r->infinity, while its unique minimum is negative, Phi has exactly two positive zeros. Strict convexity proves at most two intersections with zero; the endpoint limits and negative minimum prove existence of two. Their numerical locations are not certified in this audit.

## Scope

This proves structural properties of the ratio function Phi only. It does not validate the probability coefficients used to form IV-114, establish sign of the full entropy difference, or prove Proposition 0012. Proposition remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
