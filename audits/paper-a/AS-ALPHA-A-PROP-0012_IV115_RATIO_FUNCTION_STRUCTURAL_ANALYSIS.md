# IV-115 — Ratio-function structural analysis

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** computational exploration of the IV-114 ratio function; not a proposition proof.

## Function

For r>0,
\[
\Phi(r)=(3-2r+3r^2)\ln(1+r)+(5r-3r^2)\ln r+\frac{1+2r}{2}.
\]

## Actual symbolic checks

A Python/SymPy calculation checked that the IV-114 fourth-order coefficient, after substitution X=A^2 and r=B^2/A^2, minus its displayed ratio form simplifies exactly to zero.

Series expansions computed:
- As r -> 0+: \(\Phi(r)=\frac12+r(5\ln r+4)+r^2(-3\ln r-\frac72)+O(r^3)\).
- As r -> infinity: \(\Phi(r)=3r\ln r+4r+3\ln r-3+O(1/r)\) (equivalent expression in log(1/r) from CAS output).

## Numerical stationary-point exploration

On a logarithmic scan r in [10^-6,10^6] (5,000 sample points), followed by bracketed root-finding for derivative sign changes, one stationary point was detected:
\[
r_*\approx0.14924657501713684,\qquad \Phi(r_*)\approx-0.25800248676068105.
\]
This is **numerical evidence only**: the scan is not a proof that there are no additional stationary points outside the sampled interval or between unresolved sign changes, nor that r_* is the unique global minimum.

Selected values:
\[
\Phi(10^{-6})\approx0.4999349225,\quad
\Phi(0.1)\approx-0.2124871849,\quad
\Phi(1)\approx4.2725887222,\quad
\Phi(10)\approx113.4580889534.
\]
These show the function is not nonnegative for all r>0 (the sampled negative value at r=0.1 is a counterexample).

## Conclusions / limits

- The ratio function is not globally nonnegative; \(\Phi(0.1)<0\).
- The detected stationary point and value are approximate, not certified.
- No global uniqueness, convexity, symmetry, or exact zero locations are claimed.
- This function is a fourth-order correction component only. Its sign alone does not establish the sign of the full entropy difference or prove Proposition 0012.
- Generic ratio sector r>0; axis cases remain separate.
- Proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
