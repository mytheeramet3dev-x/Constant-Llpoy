# IV-175 — First-Principles Audit: Partial Radial Derivative R_t

Starting from the implicit equation d-4=R(d,t,p), with
\[
R=\frac{16tN}{dF},\quad N=d^2-16mt,\quad F=d^2-16t,\quad m=(2p-1)^2,
\]
differentiate with d held fixed:
\[
R_t=\frac{16}{d}\left[\frac NF+t\frac{N_tF-NF_t}{F^2}\right].
\]
Since N_t=-16m and F_t=-16,
\[
N_tF-NF_t=16(N-mF)=16(1-m)d^2.
\]
Hence the exact identity
\[
\boxed{R_t=\frac{16N}{dF}+\frac{256t(1-m)d}{F^2}.}
\]

On t<=1/64, d>=4, d<=256/63, F>=63/4, and 0<=m<=1. Also N=d^2-16mt>=d^2-16t=F and N<=d^2. Thus
\[
R_t\ge16/d\ge63/16=3.9375,
\]
and
\[
R_t\le16d/F+256td/F^2
\le16(256/63)/(63/4)+4(256/63)/(63/4)^2
<4.194.
\]
This is a conservative, explicit enclosure for the partial derivative, derived from first principles and the listed domain bounds.

Implicit differentiation gives d_t=R_t/(1-R_d). Because R_d<=0 on the branch, 0<d_t<=R_t<4.194. The previously reported 7.455139 upper bound is conservative but not sharp; this calculation does not by itself audit R_d or all IV-165 bounds.

## Verification scope
This record verifies the algebra for R_t and the enclosure assuming the previously established d,F bounds. It does not certify R_d, d_p, component derivatives, or the complete IV-165 estimate set.
