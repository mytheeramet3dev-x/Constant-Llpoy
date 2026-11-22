# IV-149 — Radial Derivative Sign Analysis and Monotonicity Certification

**Status:** ANALYTICAL RESULT for the stated matrix model; not Lean-verified; source reconciliation remains open.

## Radial-angular scalar equation
For \(t=\rho^2\), \(m=(x^2-y^2)^2/\rho^4=\cos^2(2\theta)\in[0,1]\) when \(\rho>0\), IV-148's Schur equation is
\[
d-4=R(d,t,m)=\frac{16t(d^2-16mt)}{d(d^2-16t)}.
\]
At the origin, \(d=4\). In the disk \(0<t<1/4\), ground branch satisfies \(d\ge4\), and denominators are positive.

## Partial derivative in radial variable
Holding \(d,m\) fixed,
\[
R_t=\frac{16\left[d^4-32md^2t+256mt^2\right]}{d(d^2-16t)^2}.
\]
The numerator bracket is strictly positive for \(d^2\ge16\), \(0<t<1/4\), and \(m\in[0,1]\): as a function of t its derivative is \(-32md^2+512mt\le0\) on this region, so its minimum over the interval occurs at \(t=1/4\); there it is \(d^4-8md^2+16m\ge d^4-8d^2+16>0\) for \(d^2\ge16\). (For m=0 it is simply d^4.) Hence \(R_t>0\).

## Implicit derivative and monotonicity
Set \(G(d,t,m)=d-4-R(d,t,m)\). From the resolvent identity, \(R_d=-b^T(dI+K)^{-2}b\le0\), hence \(G_d=1-R_d>0\). By implicit differentiation,
\[
\boxed{d_t=\frac{R_t}{1-R_d}>0.}
\]
Therefore, for each fixed angular parameter m, the ground-state d is strictly increasing in \(t=\rho^2\) on \(0<t<1/4\), and thus strictly increasing in \(\rho\) for fixed angle. At the origin the continuous branch has d=4 and the radial increase is consistent with the coupling expansion.

## Angular parameter derivative
At fixed d,t,
\[
R_m=-\frac{256t^2}{d(d^2-16t)}<0,
\qquad
\boxed{d_m=\frac{R_m}{1-R_d}<0}.
\]
Thus d strictly decreases as m increases, for fixed t>0. Since \(m=\cos^2(2\theta)\), this is not itself a universal monotonicity statement in theta; the angular behavior follows by composing with m(theta) and its changing derivative.

## Scope / caveats
- These results are conditional on the stated matrix and ground branch, not reconciled with the original source proposition.
- Strict radial monotonicity is proved for fixed angle (fixed m) inside the open disk.
- No Lean proof or independent audit is claimed.
- At t=0 angular parameter is undefined; d(0)=4 is angle-independent.
