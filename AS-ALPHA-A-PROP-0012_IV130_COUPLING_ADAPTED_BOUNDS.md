# IV-130 — Coupling-Adapted Coordinate and Quotient Bounds

**Status:** LOCAL BOUNDS DERIVED; ENTROPY POSITIVITY LOCALLY SUPPORTED BY THE ORDERING ESTIMATE, SUBJECT TO THE STATED MATRIX/PROBABILITY DEFINITIONS. NOT FORMALLY VERIFIED.  
**Proposition AS-ALPHA-A-PROP-0012:** remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.

## 1. Setup and certified constants from the previous box
Let \(r=10^{-3}\), \(|x|,|y|\le r\), and \(d=4-\delta\). From IV-129, \(|\delta|\le0.008\), hence
\[
3.992\le d\le4.008.
\]
Define
\[
t_+=\frac4{3.992}=1.0040160642570282,\quad
t_- =\frac4{4.008}=0.998003992015968.
\]
Taking absolute values in the lower eigenvector equations gives
\[
|u|\le t_+(|x|+|y||w|),\quad
|z|\le t_+(|y|+|x||w|),\]
\[
|w|\le t_+(|y||u|+|x||z|).
\]

## 2. Derive the xy bound for w
Substitute the first two inequalities into the third:
\[
|w|\le 2t_+^2|xy|+t_+^2(x^2+y^2)|w|.
\]
Since \(t_+^2(x^2+y^2)\le2t_+^2r^2<1\), rearrangement yields
\[
|w|\le C_w|xy|,\quad
C_w=\frac{2t_+^2}{1-2t_+^2r^2}
=2.0161005792256965.
\]
The inequality also yields \(w=0\) on either axis.

## 3. Quotient bounds for u and z
Using the w bound:
\[
|u|\le t_+|x|(1+C_wr^2),\quad
|z|\le t_+|y|(1+C_wr^2).
\]
Thus
\[
|u|\le C_u|x|,\quad |z|\le C_u|y|,\quad
C_u=t_+(1+C_wr^2)=1.0040180884543968.
\]
These bounds are valid including axes and provide continuous quotient bounds for \(u/x\) and \(z/y\) away from their zero denominators; the analytic extension at axes follows from IV-128.

## 4. Lower bound on u and ordering of u² and w²
From the first eigenvector equation,
\[
|u|=\frac4d|x+yw|\ge t_- (|x|-|y||w|).
\]
Using \(|w|\le C_w|xy|\):
\[
|u|\ge t_-|x|(1-C_wr^2)=C_{u,\mathrm{lo}}|x|,
\quad C_{u,\mathrm{lo}}=0.9980019799395417.
\]
Also \(|w|\le C_wr|x|\). Therefore
\[
u^2-w^2\ge |x|^2
\left(C_{u,\mathrm{lo}}^2-(C_wr)^2\right),
\]
where the explicit factor equals \(0.9960038873016998>0\). Consequently, for \(x\ne0\), \(q-q_3=(u^2-w^2)/D>0\) in this box.

## 5. Entropy-range bounds
The coordinate bounds imply
\[
q\le u^2+z^2\le C_u^2(x^2+y^2)\le2C_u^2r^2<2.02\times10^{-6},
\]
and
\[
q_3\le z^2+w^2\le C_u^2r^2+C_w^2r^4<1.02\times10^{-6}.
\]
So \(0\le q_3<q<1/2\) when \(x\ne0\), throughout the box. Binary entropy is strictly increasing on \((0,1/2)\), proving the local sign \(\Delta S>0\) for \(x\ne0\), and equality when \(x=0\), under the recorded definitions.

## 6. Limits of this result
- This is a local result for \(|x|,|y|\le10^{-3}\), not for arbitrary coupling.
- Constants derive from matrix equations and norm/eigenvalue bounds, but the derivation has not been formalized in Lean or independently proof-checked.
- The original Proposition 0012 scope must still be checked against this local box; no global claim is made.
- This step advances the local positivity route by bounding quotients and establishing \(u^2>w^2\) explicitly.

## 7. Reproducible arithmetic
Constants above were evaluated with Python floating-point arithmetic. The algebraic inequalities and rational definitions are primary; decimal values are presentation-only. For machine-certified numerical constants, replace decimal rounding by rational interval arithmetic.
