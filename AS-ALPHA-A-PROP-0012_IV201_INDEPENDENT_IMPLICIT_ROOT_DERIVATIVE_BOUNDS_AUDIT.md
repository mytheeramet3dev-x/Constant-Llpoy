# IV-201 — Independent Recalculation of Implicit Root Derivative Bounds

## Scope
Independently audit uniform bounds for the implicit root derivatives \(d_t\) and \(d_p\) using the IV-198–200 root equation and domain. This does not establish source fidelity of the reconstructed equation.

## Assumptions / domain
\[
4\le d\le 256/63,\quad 0\le t\le1/64,\quad 0\le p\le1,
\]
\[
m=(2p-1)^2\in[0,1],\quad F=d^2-16t\ge63/4.
\]
The implicit equation is \(d=4+R(d,t,p)\), with
\[
R=\frac{16t(d^2-16mt)}{d(d^2-16t)}.
\]
From IV-198, \(R_d\le0\), so \(1-R_d\ge1\). The derivative formulas are
\[
d_t=\frac{R_t}{1-R_d},\quad d_p=\frac{R_p}{1-R_d},
\]
where
\[
R_t=\frac{16(d^4-32d^2mt+256mt^2)}{d(d^2-16t)^2},
\quad
R_p=-\frac{1024t^2(2p-1)}{d(d^2-16t)}.
\]

## 1. Uniform bound for \(d_t\)
The coefficient of \(m\) in the numerator of \(R_t\) is
\[
t(-32d^2+256t)\le0
\]
throughout the box (since \(d^2\ge16\), \(t\le1/64\)). Therefore the numerator is maximized at \(m=0\). Since \(F=d^2-16t\) decreases with \(t\), the resulting upper bound increases with \(t\):
\[
0\le R_t\le\frac{16d^3}{(d^2-1/4)^2}.
\]
The function \(g(d)=16d^3/(d^2-1/4)^2\) is strictly decreasing for \(d\ge4\), because
\[
\frac{g'(d)}{g(d)}=\frac{3}{d}-\frac{4d}{d^2-1/4}
=\frac{-d^2-3/4}{d(d^2-1/4)}<0.
\]
Thus
\[
R_t\le g(4)=\frac{16384}{3969}
=4.127991937515747\ldots<4.128.
\]
Using \(1-R_d\ge1\) and nonnegativity,
\[
\boxed{0\le d_t\le R_t<4.128.}
\]
This independently improves the previously inherited ceiling 4.194, conditional on the stated equation/domain and IV-198 sign result.

## 2. Uniform bound for \(d_p\)
Using \(|2p-1|\le1\), \(t^2\le1/4096\), \(d\ge4\), and \(F\ge63/4\),
\[
|R_p|\le\frac{1024(1/4096)}{4(63/4)}
=\frac{1/4}{63}=\frac1{252}.
\]
Since \(1-R_d\ge1\),
\[
\boxed{|d_p|\le|R_p|\le1/252
=0.003968253968253968\ldots.}
\]
This ceiling remains valid; it is a conservative bound and is not claimed sharp for the implicit root.

## 3. Findings and status
- **PASS (conditional):** analytic uniform bound \(d_t<4.128\), replacing the earlier 4.194 ceiling.
- **PASS (conditional):** \(|d_p|\le1/252\); the earlier bound is retained.
- The bounds rely on the reconstructed root equation, domain, and IV-198 denominator/sign result; source fidelity and upstream proof closure remain open.
- This audit does not propagate the improved \(d_t\) ceiling through downstream quantities. That recalculation is a separate required audit.

## Reproducibility
Exact rational ceiling for the first bound: \(16384/3969\). Decimal shown above. No floating-point calculation is needed for the inequality proofs.
