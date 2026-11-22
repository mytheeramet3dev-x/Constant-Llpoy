# IV-176 — First-Principles Angular Derivative Audit for the Implicit Spectral Parameter

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Partial conditional derivative enclosure; inherited domain/branch hypotheses not independently certified.

## 1. Implicit system

Use
\[
d-4=R(d,t,p),\quad R=\frac{16tN}{dF},\quad
N=d^2-16mt,\quad F=d^2-16t,\quad m=(2p-1)^2.
\]
The derivative \(R_p\) is taken with \(d,t\) fixed. Since
\[
m_p=4(2p-1),\qquad N_p=-16t m_p,
\]
we get
\[
R_p=\frac{16tN_p}{dF}
=-\frac{256t^2m_p}{dF}
=\boxed{-\frac{1024t^2(2p-1)}{dF}}.
\]

Implicit differentiation gives
\[
d_p=\frac{R_p}{1-R_d}.
\]
On the assumed branch \(R_d\le0\), so \(1-R_d\ge1\) and
\[
|d_p|\le |R_p|
\le\frac{1024t^2}{dF}.
\]

## 2. Correct endpoint-uniform arithmetic

Assuming \(t\le1/64\), \(d\ge4\), and \(F\ge63/4\),
\[
1024t^2\le\frac{1024}{4096}=\frac14,
\qquad dF\ge4\cdot\frac{63}{4}=63.
\]
Therefore
\[
\boxed{|d_p|\le\frac1{252}\approx0.003968254.}
\]
The previously used \(1/63\) bound is also valid but unnecessarily loose by a factor of four; the exact simplification above is recorded to avoid confusing the sharp arithmetic with the older conservative value.

The sign is determined by
\[
\operatorname{sgn}(d_p)=-\operatorname{sgn}(2p-1)
\]
when the implicit denominator is positive, except at \(p=1/2\), where this derivative is zero.

## 3. Scope

This derivation audits the formula and arithmetic conditional on the inherited bounds and \(R_d\le0\). It is **not** an independent proof of those branch/domain hypotheses, nor a complete re-certification of IV-163–165. Downstream bounds must be revisited if tighter constants are used; the old rounded value \(0.003968254\) coincides numerically with \(1/252\), while the earlier \(1/63\) statement was the loose bound.

