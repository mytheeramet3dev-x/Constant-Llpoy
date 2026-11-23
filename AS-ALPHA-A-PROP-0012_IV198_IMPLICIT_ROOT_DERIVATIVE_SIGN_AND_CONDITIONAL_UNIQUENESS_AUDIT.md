# IV-198 — Implicit Root Derivative Sign Audit

**Target:** AS-ALPHA-A-PROP-0012  
**Scope:** Algebraic verification of \(R_d\) for the implicit equation recorded in IV-176, conditional only on the stated box bounds \(d\ge4\), \(0\le t\le1/64\), and \(m=(2p-1)^2\in[0,1]\). Root existence/uniqueness is treated separately.

## 1. Reconstructed equation

\[
R(d,t,p)=\frac{16t(d^2-16mt)}{d(d^2-16t)},\quad
m=(2p-1)^2,\quad F=d^2-16t.
\]

Differentiate with respect to \(d\), holding \(t,p\) fixed. Symbolic differentiation and simplification give

\[
R_d=-\frac{16t\left[d^4+d^2t(16-48m)+256mt^2\right]}
{d^2(d^2-16t)^2}.
\]

## 2. Sign proof

The denominator is strictly positive because \(d\ge4\) and \(0\le t\le1/64\), so
\[
d^2-16t\ge16-\frac14=\frac{63}{4}>0.
\]

For the bracket, since \(m\in[0,1]\), we have \(16-48m\ge-32\). Also \(256mt^2\ge0\). Therefore
\[
\begin{aligned}
d^4+d^2t(16-48m)+256mt^2
&\ge d^4-32d^2t\\
&=d^2(d^2-32t)\\
&\ge d^2\left(16-\frac12\right)\\
&=\frac{31}{2}d^2>0.
\end{aligned}
\]
Thus the bracket is strictly positive. Since \(t\ge0\), it follows that
\[
\boxed{R_d\le0}
\]
throughout the stated box (with equality at \(t=0\)); for \(t>0\), \(R_d<0\).

This closes the sign inequality itself, **provided** the implicit variable \(d\) lies in the stated box and the equation/formula is the correct source definition.

## 3. Consequence for uniqueness (conditional domain statement)

Define \(\Phi(d;t,p)=d-4-R(d,t,p)\). Then
\[
\Phi_d=1-R_d\ge1.
\]
Consequently, for fixed \((t,p)\), \(\Phi\) is strictly increasing in \(d\) on any interval where the stated box and denominator conditions hold. There can be at most one root on that interval.

This proves interval uniqueness, but not existence. Existence still requires a sign change or another valid existence argument at the endpoints of a specified admissible interval. The claimed interval \([4,256/63]\) and endpoint sign checks must be independently sourced/verified before existence can be declared.

## 4. Status

- Algebraic derivative formula: **verified by symbolic differentiation and manual sign argument**.
- \(R_d\le0\) on stated box: **proved conditional on the box/source equation**.
- Strict monotonicity of \(\Phi\) on that interval: **proved conditional on interval validity**.
- Root uniqueness within that interval: **proved conditional**.
- Root existence in the interval: **OPEN** (endpoint sign check/source premise not established in this audit).
- Correct source equation and root interval provenance: **not fully independently verified**.

## 5. Next obligation

Retrieve the exact upstream source for the admissible interval and perform endpoint evaluations \(\Phi(4;t,p)\), \(\Phi(256/63;t,p)\) uniformly in \((t,p)\). If these signs cannot be established, root existence remains open and downstream derivative bounds remain conditional on existence.
