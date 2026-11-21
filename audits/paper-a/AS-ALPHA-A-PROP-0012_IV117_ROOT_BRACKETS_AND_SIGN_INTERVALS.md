# IV-117 — Root isolation brackets and certified sign intervals for Phi

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** interval endpoint evaluations plus IV-116 analytic strict-convexity argument; function-level only.

## Definition and global structural fact

\[
\Phi(r)=(3-2r+3r^2)\ln(1+r)+(5r-3r^2)\ln r+\tfrac12+r,\quad r>0.
\]

IV-116's analytic inequality proves \(\Phi''(r)>0\) for every positive r. Hence Phi is strictly convex, has exactly one global minimum, and—given the endpoint limits and the negative minimum—exactly two positive zeros.

## Root brackets

Using interval arithmetic (mpmath interval arithmetic, 40 decimal digits) at the bracket endpoints, the sign evaluations are:

- \(\Phi(0.04409622)\in[3.7391482933\times10^{-8},3.7391482934\times10^{-8}]>0\).
- \(\Phi(0.04409623)\in[-2.4546677971\times10^{-8},-2.4546677970\times10^{-8}]<0\).
- \(\Phi(0.29387382)\in[-1.8712966146\times10^{-8},-1.8712966145\times10^{-8}]<0\).
- \(\Phi(0.29387383)\in[1.2869401180\times10^{-8},1.2869401181\times10^{-8}]>0\).

Therefore, by continuity, the two roots are isolated in:
\[
r_-\in(0.04409622,0.04409623),\quad
r_+\in(0.29387382,0.29387383).
\]
These brackets are valid sign-change brackets. With strict convexity and the endpoint/negative-minimum arguments from IV-116, they enclose the only two positive roots. (Endpoint evaluations are interval-checked; root intervals themselves are not claims of interval Newton certification.)

Numerical root estimates:
\[
r_-\approx0.044096226036609544,\quad
r_+\approx0.29387382592513084.
\]
Numerical minimizer:
\[
r_*\approx0.14924657501713684,\quad\Phi(r_*)\approx-0.25800248676068105.
\]
Minimizer decimal is not interval-certified.

## Sign intervals

The global root count and endpoint signs give:
- \(\Phi(r)>0\) for \(0<r<r_-\).
- \(\Phi(r)<0\) for \(r_-<r<r_+\).
- \(\Phi(r)>0\) for \(r>r_+\).

## Audit limitations

- This certifies sign-bracket endpoints using interval evaluations, not interval Newton/root enclosure machinery.
- It proves the sign structure of Phi only.
- It does not independently verify the IV-107 endpoint probability expansions or IV-110 entropy expansion; therefore the fourth-order coefficient's role in Proposition 0012 remains conditional on those inputs.
- No Lean proof is claimed. Proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
