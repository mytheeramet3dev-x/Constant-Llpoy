# IV-199 — Uniform Endpoint Sign and Implicit Root Existence/Uniqueness Audit

**Target:** AS-ALPHA-A-PROP-0012  
**Scope:** Complete the interval root argument for the equation reconstructed in IV-176 and the sign proof in IV-198, on the parameter box \(0\le t\le1/64,\ 0\le p\le1\).

## 1. Define the root function

\[
\Phi(d;t,p)=d-4-R(d,t,p),\quad
R=\frac{16t(d^2-16mt)}{d(d^2-16t)},\quad m=(2p-1)^2.
\]
The proposed interval is \(I=[4,256/63]\).

## 2. Lower endpoint

At \(d=4\),
\[
N=16-16mt=16(1-mt)>0,\quad F=16-16t>0.
\]
Therefore \(R(4,t,p)\ge0\), so
\[
\Phi(4;t,p)=-R(4,t,p)\le0.
\]
For \(t>0\), the sign is strict; at \(t=0\), \(\Phi(4;0,p)=0\).

## 3. Upper endpoint — uniform bound

Since \(m\ge0\),
\[
d^2-16mt\le d^2.
\]
For positive denominator,
\[
R(d,t,p)\le\frac{16td}{d^2-16t}.
\]
The right side is increasing in \(t\) over the admissible interval, hence at \(t\le1/64\) and \(d_*=256/63\),
\[
R(d_*,t,p)\le\frac{16(1/64)d_*}{d_*^2-16(1/64)}
=\frac{16128}{258175}.
\]
Meanwhile
\[
d_*-4=\frac4{63}.
\]
Exact rational subtraction gives
\[
\frac4{63}-\frac{16128}{258175}
=\frac{16636}{16265025}>0.
\]
Thus
\[
\boxed{\Phi(256/63;t,p)>0}
\]
uniformly for every parameter pair in the stated box.

## 4. Existence

For fixed \((t,p)\), \(\Phi\) is continuous in \(d\) on \(I\), because \(d>0\) and \(d^2-16t\ge63/4>0\). The endpoint signs from Sections 2–3 and the intermediate value theorem imply at least one root in \(I\). When \(t=0\), the root is explicitly \(d=4\).

## 5. Uniqueness

IV-198 proves \(R_d\le0\) on this box. Hence
\[
\Phi_d=1-R_d\ge1,
\]
so \(\Phi\) is strictly increasing in \(d\). It has at most one root in \(I\). Combining existence and uniqueness establishes exactly one root in the proposed interval for each \((t,p)\) in the parameter box.

## 6. Verdict and limitations

**Existence and uniqueness in \(I\): PROVED, conditional on the reconstructed equation being the exact proposition source definition and on the parameter/domain bounds.**

The root interval is now established by explicit endpoint signs rather than merely inherited. This record does not yet establish differentiability of the root map or independently verify the full original source/proposition definitions. The implicit-function theorem and downstream derivative-bound chain must still be audited for full source fidelity and uniform applicability.
