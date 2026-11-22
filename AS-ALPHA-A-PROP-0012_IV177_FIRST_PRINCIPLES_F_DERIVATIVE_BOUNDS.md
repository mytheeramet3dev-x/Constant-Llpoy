# IV-177 — First-Principles Derivative Bounds for the Denominator F

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional component bound.

## 1. Definitions

\[
F(d,t)=d^2-16t.
\]
Along the implicit branch \(d=d(t,p)\), chain rule gives
\[
F_t=2d d_t-16,\qquad F_p=2d d_p.
\]
Hence
\[
|F_t|\le2d|d_t|+16,\qquad |F_p|\le2d|d_p|.
\]

## 2. Insert audited partial-derivative enclosures

Using the conditional bounds inherited from IV-175/176:
\[
d\le\frac{256}{63},\quad |d_t|<4.194,\quad |d_p|\le\frac1{252},
\]
we obtain
\[
|F_t|<2\frac{256}{63}(4.194)+16
=\boxed{50.084572},
\]
and
\[
|F_p|\le2\frac{256}{63}\frac1{252}
=\boxed{0.032249938}.
\]
These values are rounded upward.

## 3. Status / limitations

The chain-rule arithmetic is explicit. The result remains conditional on the inherited spectral-domain and implicit-branch assumptions, especially the audited bounds on \(d,d_t,d_p\). It does not independently establish those premises or certify downstream normalized probabilities/entropy derivatives.
