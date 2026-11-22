# IV-163 — Derivative Bound Preparation for Normalized Probability Factors

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PARTIAL; component/prefactor bounds only; normalized Q derivatives not certified

## 1. Correction to IV-162

The previous IV-162 radial derivative estimate used an incorrect denominator. The inherited conservative estimate is
\[
R_t\le \frac{16d^3}{(d^2-4)^2},
\]
so using \(d\le d_*=256/63\) and \(d^2-4\ge12\) gives
\[
\boxed{0\le d_t\le\frac{16d_*^3}{144}<7.455139.}
\]
The IV-162 record was corrected and fetchback-verified. This is an explicit correction, not a change to the probability-factor bounds.

## 2. Angular derivative of the implicit spectral parameter

Since
\[
R_m=-\frac{256t^2}{dF},\quad
d_m=\frac{R_m}{1-R_d},\quad 1-R_d\ge1,
\]
we have
\[
|d_m|\le\frac{256t_*^2}{4F_*}<0.000992064,
\]
and, for \(m=(2p-1)^2\), \(|m_p|\le4\),
\[
\boxed{|d_p|<0.003968254.}
\]

## 3. Bounds on elementary factors

Let \(H_*=d_*^2+1/4\). With
\[
A=d^2+16t(1-2p),\quad
G=d^2+16t(2p-1),\quad F=d^2-16t,
\]
we obtain
\[
|A|,|G|\le H_*,
\]
\[
|F_t|\le 2d_*\,(7.455139)+16<76.587796,
\quad |F_p|\le2d_*\,(0.003968254)<0.032250.
\]
Likewise,
\[
|A_t|,|G_t|<76.587796,
\quad |A_p|,|G_p|<0.532250.
\]
These estimates are direct chain-rule bounds, not grid estimates.

## 4. Common rational prefactor

For \(B=16/(d^2F^2)\),
\[
B\le B_*:=\frac{1}{F_*^2}<0.004031243.
\]
Using logarithmic differentiation,
\[
\left|\frac{B_t}{B}\right|
\le\frac{2|d_t|}{4}+\frac{2|F_t|}{F_*}
<13.453004,
\]
hence
\[
\boxed{|B_t|<0.054232316.}
\]
Similarly,
\[
\left|\frac{B_p}{B}\right|<0.006079358,
\quad
\boxed{|B_p|<2.450737\times10^{-5}.}
\]

## 5. Remaining derivative obligations

These component and prefactor estimates do not yet certify \(Q_t,Q_p,Q_{3,t},Q_{3,p}\). The remaining step is to bound derivatives of the weighted numerator expressions and the normalization
\[
D=1+u^2+w^2+z^2,
\]
then combine using quotient rules. This record does not claim a completed normalized derivative theorem or Taylor remainder certification.

## 6. Next

IV-164: derive interval bounds for \(u/\sqrt t, z/\sqrt t, w/\sqrt t\) and their \(t,p\) derivatives using the rational expressions; then bound \(D_t,D_p\) before closing normalized-factor derivative inequalities.
