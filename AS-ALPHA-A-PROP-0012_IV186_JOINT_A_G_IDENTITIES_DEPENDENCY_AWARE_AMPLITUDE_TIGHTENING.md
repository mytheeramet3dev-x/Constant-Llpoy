# IV-186 — Joint-Constraint Analysis of A and G

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Exact algebraic identities and conditional amplitude tightening; upstream domain/root premises remain unverified.

## 1. Definitions
Let
\[
A=d^2+16t(1-2p),\quad G=d^2+16t(2p-1).
\]
Set \(a=d^2\), \(x=2p-1\), and \(c=16tx\). Then
\[
A=a-c,\quad G=a+c.
\]
Exact identities:
\[
A+G=2d^2,\quad G-A=32t(2p-1),
\]
\[
AG=d^4-256t^2(2p-1)^2,
\]
\[
A^2+G^2=2[d^4+256t^2(2p-1)^2].
\]

## 2. Dependency-aware weighted squared sum
Since \(p=(1+x)/2\) and \(1-p=(1-x)/2\),
\[
pA^2+(1-p)G^2
=a^2+c^2-2acx
=a^2+x^2(256t^2-32at).
\]
Given \(a=d^2\ge16\), \(t\le1/64\), we have \(8t\le1/8<a\), so
\[
256t^2-32at=32t(8t-a)\le0.
\]
Consequently the rigorous dependency-preserving inequality
\[
\boxed{pA^2+(1-p)G^2\le d^4}
\]
holds under these domain assumptions. Equality occurs in this upper inequality when (t=0) or (x=0) (also algebraically if coefficient/variable conditions make the correction zero).

## 3. Improved amplitude ceiling for P_u+P_z
Using \(P_u+P_z=16H[pA^2+(1-p)G^2]\), and \(H=1/(d^2F^2)\),
\[
P_u+P_z\le16Hd^4=\frac{16d^2}{F^2}.
\]
Under inherited \(d\le256/63\) and \(F\ge63/4\), a conservative separated bound gives
\[
P_u+P_z\le\frac{16(256/63)^2}{(63/4)^2}
=1.0650198397621882\ldots
\]
Thus rounded upward:
\[
\boxed{P_u+P_z<1.065020}
\]
and, using inherited \(P_w<0.016124969\),
\[
\boxed{S<1.081145}.
\]
This improves IV-185's aggregate amplitude ceiling (S<1.148758). The improvement is only an amplitude result; derivative ceilings are not automatically improved and require differentiating the dependency-aware identity with validated joint bounds.

## 4. Scope and limitations
These identities and the inequality are algebraically verified. Numerical ceilings remain conditional on inherited domain bounds (d\ge4\), (d\le256/63\), (F\ge63/4\), (t\le1/64\), and the stated component formulas. No root existence/uniqueness, sign premise (R_d\le0\), global domain certification, interval-arithmetic certificate, or formal proof is claimed. No downstream derivative/Lipschitz bound is updated in this record.
