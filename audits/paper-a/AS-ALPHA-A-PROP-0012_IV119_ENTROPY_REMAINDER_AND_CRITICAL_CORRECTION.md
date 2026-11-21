# IV-119 — Entropy remainder control and correction of IV-110 onward

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** direct symbolic expansion verified with SymPy; major correction to earlier entropy-series audits.

## Critical correction

Earlier IV-110 and follow-up IV-114–IV-118 used the incorrect sign for the quadratic term in binary entropy and an incorrect fourth-order coefficient from expanding q(1-ln q).

The correct binary entropy series is:
\[
h(q)=q(1-\ln q)-\frac{q^2}{2}-\frac{q^3}{6}-\frac{q^4}{12}+O(q^5).
\]
This was directly checked using SymPy series.

For \(q=\varepsilon^2s+\varepsilon^4t+O(\varepsilon^6)\), fixed \(s>0\):
\[
h(q)=\varepsilon^2s(1-\ln(\varepsilon^2s))
+\varepsilon^4\left[-t\ln(\varepsilon^2s)-\frac{s^2}{2}\right]
+O(\varepsilon^6|\ln\varepsilon|).
\]
The previous IV-110 formula's fourth-order term \(t(1-\ln(\varepsilon^2s))+s^2/2\) was wrong.

## Corrected entropy-difference fourth-order coefficient

Given the same provisional probability expansions \(q=\varepsilon^2S+\varepsilon^4T\) and \(q_3=\varepsilon^2R+\varepsilon^4T_3\), with \(S=X(1+r), R=Xr\):
\[
F_4^{\rm corr}=-T\ln(\varepsilon^2S)-\frac{S^2}{2}
+T_3\ln(\varepsilon^2R)+\frac{R^2}{2}.
\]
Writing \(L=\ln(\varepsilon^2X)\), \(T=X^2(-3+2r-3r^2)\), \(T_3=X^2(5r-3r^2)\):
\[
F_4^{\rm corr}=X^2\left[
3(1+r)L
+(3-2r+3r^2)\ln(1+r)
+(5r-3r^2)\ln r
-\frac{1+2r}{2}
\right].
\]
This is the corrected fourth-order expression; it is not the IV-114 expression.

## Remainder control (fixed s)

For \(0<q\le q_0<1\), the Taylor expansion of \(-(1-q)\ln(1-q)\) has bounded remainder on compact subintervals, and the omitted terms after quadratic order are bounded by a constant times \(q^3\). For fixed \(s>0\) and \(t\), substitution gives remainder of order \(O(\varepsilon^6|\ln\varepsilon|)\), provided the probability expansion itself has a controlled remainder and q remains in the small-q domain.

This is a fixed-s statement only. It is not uniform as s approaches zero or if s,t vary with epsilon without additional bounds.

## Downstream status

- IV-110's fourth-order entropy expansion is corrected by this audit.
- IV-114's displayed fourth-order ratio expression is superseded by \(F_4^{corr}\) above.
- IV-115–IV-117 analyze the previously defined ratio function \(\Phi\), whose contribution to the corrected entropy coefficient is not the same sign structure; those function-level calculations may remain valid as standalone facts but do not certify the corrected entropy coefficient.
- IV-118's fourth-order decomposition/dominance analysis must be revisited; do not rely on its incorrect fourth-order formula.
- The leading second-order coefficient is unchanged. Fixed-r weak-coupling positivity remains conditional on correct probability coefficients and controlled remainder.
- No Lean proof is claimed. Proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## Required next work

Recompute the full corrected \(\Delta h\) expansion, update/supersede IV-110 and IV-114–IV-118, and independently verify probability coefficients before making any downstream claim.
