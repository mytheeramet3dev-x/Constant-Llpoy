# IV-188 — Dependency-Aware Angular Derivative of P_u + P_z

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional analytic estimate; inherited bounds remain unverified.

## 1. Exact identity
With \(a=d^2\), \(x=2p-1\), and
\[
B=a^2+x^2(256t^2-32at),\qquad P_u+P_z=16HB,
\]
holding \(a,t,H\) fixed with respect to the angular variable \(p\) except for the inherited \(H_p\) term, differentiation gives
\[
B_p=4x(256t^2-32at).
\]
Under \(a\ge16\) and \(t\le1/64\), the coefficient is nonpositive, and
\[
|B_p|=4|x|(32at-256t^2)\le128at\le128a_*t_*<33.023936.
\]

## 2. Bound on the pair derivative
Use \(B\le a_*^2\), \(H\le1/3969\), and \(|H_p|<1.535\times10^{-6}\):
\[
|(P_u+P_z)_p|\le16(|H_p|B+H|B_p|)<0.139823644.
\]
Rounded upward:
\[
\boxed{|(P_u+P_z)_p|<0.139824}.
\]

## 3. Aggregate angular derivative
Using the inherited \(|(P_w)_p|<0.064566\),
\[
|S_p|<0.139823644+0.064566=0.204389644,
\]
so upward-rounded
\[
\boxed{|S_p|<0.204390}.
\]
This is tighter than IV-185's dependency-aware aggregate angular bound \(2.408660592\). It is conditional and uses a conservative bound on \(B_p\); no sharpness claim is made.

## 4. Scope
The calculation does not yet propagate the new \(S_p\) bound through \(D_p\), normalized \(Q\)-derivatives, or a new Lipschitz constant. It assumes the inherited domain and bounds (including \(a\ge16\), \(a\le(256/63)^2\), \(t\le1/64\), and \(|H_p|<1.535\times10^{-6}\)).
