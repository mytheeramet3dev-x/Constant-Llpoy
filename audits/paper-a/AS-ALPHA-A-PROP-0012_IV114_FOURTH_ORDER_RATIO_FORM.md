# IV-114 — Fourth-order generic entropy-difference ratio form

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** algebraic reduction only; generic asymptotic sector (A\ne0, B\ne0). Not a proof of the proposition.

## Definitions

Let (X=A^2>0), (r=B^2/A^2>0), and (L=\ln(\varepsilon^2X)). Then (S=A^2+B^2=X(1+r)), (R=B^2=Xr), and the previously stated fourth-order probability coefficients are
[
T=X^2(-3+2r-3r^2),\quad T_3=X^2(5r-3r^2).
]

Starting from the IV-110 fourth-order difference coefficient
[
F_4=T(1-\ln(\varepsilon^2S))+\frac{S^2}{2}
-T_3(1-\ln(\varepsilon^2R))-\frac{R^2}{2},
]
substitution of (\ln(\varepsilon^2S)=L+\ln(1+r)) and (\ln(\varepsilon^2R)=L+\ln r) yields

[
F_4=X^2\left[
-3(1+r)(1-L)
+(3-2r+3r^2)\ln(1+r)
+(5r-3r^2)\ln r
+\frac{1+2r}{2}
\right].
]

Thus the generic entropy difference has the ratio form
[
\Delta h=\varepsilon^2X\left[
(1+r)(1-\ln(\varepsilon^2X)-\ln(1+r))
-r(1-\ln(\varepsilon^2X)-\ln r)
\right]+\varepsilon^4F_4
+O(\varepsilon^6|\ln\varepsilon|).
]
(Equivalent forms of the second-order term may be used; the expression above retains the original (S) and (R) substitutions.)

## Independent symbolic check

SymPy simplification was performed on the ratio substitution: the difference between the original coefficient expression and the displayed closed form simplifies identically to zero. This verifies only the algebraic rearrangement, not the probability expansions (T,T_3), the entropy remainder, or Proposition 0012.

## Scope / caveats

- Requires (A\ne0) and (B\ne0); axis cases are handled separately in IV-111 and IV-112.
- Uses IV-110's probability coefficients as inputs; those coefficients still require independent verification.
- No Lean formalization or proposition proof is claimed.
- Proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
