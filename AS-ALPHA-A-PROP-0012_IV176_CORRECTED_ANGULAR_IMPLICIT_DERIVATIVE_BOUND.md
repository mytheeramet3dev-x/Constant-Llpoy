# IV-176 — Corrected Angular Derivative Bound for the Implicit Spectral Parameter

## Scope
Correct and restate the angular derivative estimate for the implicit root d. This is conditional on the inherited implicit equation and bounds recorded in IV-163/IV-175; those upstream premises are not independently certified here.

Let
\[
d-4=R(d,t,p),\quad R=\frac{16tN}{dF},\quad
N=d^2-16mt,\quad F=d^2-16t,\quad m=(2p-1)^2.
\]
At fixed d,t,
\[
m_p=4(2p-1),\quad R_p=-\frac{256t^2m_p}{dF}
=-\frac{1024t^2(2p-1)}{dF}.
\]
Implicit differentiation gives
\[
d_p=\frac{R_p}{1-R_d}.
\]
Assuming the inherited condition \(R_d\le0\), we have \(1-R_d\ge1\), hence
\[
|d_p|\le|R_p|\le\frac{1024t^2}{dF}.
\]
Using \(t\le1/64\), \(d\ge4\), and \(F\ge63/4\),
\[
1024(1/64)^2=1/4,\quad dF\ge4(63/4)=63,
\]
so the sharp arithmetic simplification from these stated bounds is
\[
\boxed{|d_p|\le\frac1{252}\approx0.003968253968.}
\]
The previous IV-163 value 0.003968254 is the upward-rounded decimal for this exact bound. The sign of \(d_p\) is opposite to \(2p-1\), except where that factor is zero.

## Status
This verifies the arithmetic simplification and restates the conditional estimate. It does not independently verify the implicit-root existence, the bound \(R_d\le0\), or the inherited spectral domain inequalities.
