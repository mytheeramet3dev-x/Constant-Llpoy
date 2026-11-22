# IV-166 — Quotient Derivative Bounds for Q and Q3

## Domain and inherited estimates
On \(0\le t\le1/64\), \(0\le p\le1\), inherit IV-165 constants:
\(d\le256/63\), \(F\ge63/4\), \(|d_t|\le7.455139\),
\(|d_p|\le0.003968254\), \(D\le1.035647\),
\(|D_t|\le3.099578\), and \(|D_p|\le0.038362\).
These inherited values are assumed for this note and remain subject to audit.

Use \(H=(d^2F^2)^{-1}\), \(M=(256/63)^2+1/4\), and the IV-165 derivative estimates for the unweighted factors:
\[
R_u=16A^2H,\quad R_z=16G^2H,\quad R_w=1024t/F^2.
\]
Then \(Q=[pR_u+(1-p)R_z]/D\), and \(Q_3=[R_z+R_w]/D\). This representation is endpoint-regular and avoids division by \(1-p\).

## Numerator bounds
Conservative upper bounds obtained by product rule from inherited constants:
\[
R_u,R_z<1.132633,\quad |(R_u)_t|,|(R_z)_t|<25.587618,
\]
\[
|(R_u)_p|,|(R_z)_p|<0.078815583,
\]
\[
R_w<0.064499875,\quad |(R_w)_t|<4.755281235,
\quad |(R_w)_p|<0.064499875.
\]
Consequently:
\[
N_Q<2.265264302,\quad |(N_Q)_t|<51.175234190,
\]
\[
|(N_Q)_p|<2.422895466,
\]
where \(N_Q=pR_u+(1-p)R_z\).
For \(N_3=R_z+R_w\):
\[
N_3<1.197132025,\quad |(N_3)_t|<30.342898330,
\quad |(N_3)_p|<0.143315457.
\]

## Quotient rule
For \(Q=N_Q/D\) and \(Q_3=N_3/D\), use \(D\ge1\) and the inherited denominator bounds. Explicit conservative results, rounded upward:
\[
|Q_t|<58.196598,\quad |Q_p|<2.509796,
\]
\[
|(Q_3)_t|<34.053503,\quad |(Q_3)_p|<0.189240.
\]
Also \(Q<2.265265\) and \(Q_3<1.197133\).

## Caveat
This note depends on IV-165 component and spectral derivative constants. It is a quotient-rule propagation, not an independent validation of those constants. The bounds are coarse and do not certify an entropy remainder. In particular, IV-165 inherited estimates must be audited before downstream constants can be treated as certified.

## Conclusion
IV-166 supplies finite uniform first-derivative bounds for normalized probability factors, conditional on the inherited bounds. Further entropy derivatives and Taylor remainder estimates remain open.
