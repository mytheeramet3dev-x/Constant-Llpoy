# IV-120 — Downstream invalidation ledger and corrected asymptotic expansion

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** correction ledger; replaces the entropy-series formulas from IV-110 and the derived fourth-order claims in IV-114–IV-118.

## Correct expansion

For binary entropy and \(q=\varepsilon^2s+\varepsilon^4t+O(\varepsilon^6)\), fixed \(s>0\):
\[
h(q)=\varepsilon^2s(1-\ln(\varepsilon^2s))
+\varepsilon^4[-t\ln(\varepsilon^2s)-s^2/2]
+O(\varepsilon^6|\ln\varepsilon|).
\]
SymPy expansion of the binary entropy was directly executed and confirms the sign and coefficients.

For provisional probabilities \(q=\varepsilon^2S+\varepsilon^4T\), \(q_3=\varepsilon^2R+\varepsilon^4T_3\):
\[
\Delta h=\varepsilon^2[S(1-\ln(\varepsilon^2S))-R(1-\ln(\varepsilon^2R))]
+\varepsilon^4[-T\ln(\varepsilon^2S)-S^2/2+T_3\ln(\varepsilon^2R)+R^2/2]
+O(\varepsilon^6|\ln\varepsilon|).
\]

## Corrected generic ratio form

With \(X=A^2>0\), \(r=B^2/A^2>0\), \(L=\ln(\varepsilon^2X)\), \(S=X(1+r)\), \(R=Xr\), \(T=X^2(-3+2r-3r^2)\), \(T_3=X^2(5r-3r^2)\):
\[
\Delta h=\varepsilon^2X C_2(r,L)+\varepsilon^4X^2 C_4^{\rm corr}(r,L)+O(\varepsilon^6|\ln\varepsilon|),
\]
\[
C_2=1-L-(1+r)\ln(1+r)+r\ln r,
\]
\[
C_4^{\rm corr}=3(1+r)L+(3-2r+3r^2)\ln(1+r)+(5r-3r^2)\ln r-\frac{1+2r}{2}.
\]

## Downstream status ledger

- **IV-110:** second-order term survives; fourth-order entropy coefficient is invalid and superseded.
- **IV-114:** fourth-order ratio form superseded.
- **IV-115–IV-117:** their convexity/root/sign statements about the previously defined Phi are mathematically separate facts, but they are not sign certificates for the corrected \(C_4^{corr}\). Do not present them as results for the corrected entropy coefficient.
- **IV-118:** fourth-order sign-transfer analysis superseded. Its fixed-r leading-order positivity statement is conditionally retained because the second-order term is unchanged, but its derivation must be restated using the corrected expansion/remainder.
- **IV-119:** critical correction note remains in force.

## Fixed-parameter leading sign (conditional)

For fixed \(X>0,r>0\), \(C_2=-L+K(r)\to+\infty\) as \(\varepsilon\to0^+\). The corrected \(C_4\) grows at most linearly in \(|L|\) for fixed r, so the \(\varepsilon^4\) contribution is smaller than the \(\varepsilon^2\) contribution in this fixed-parameter limit. Thus \(\Delta h>0\) for sufficiently small epsilon, conditional on the probability expansions and remainder being valid.

This is not uniform in r or X, and it is not the target proposition proof.

## Next mandatory verification

Independent re-derivation of endpoint probability coefficients (IV-107), with actual computational work, before any further entropy conclusion. No Lean proof is claimed. Proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
