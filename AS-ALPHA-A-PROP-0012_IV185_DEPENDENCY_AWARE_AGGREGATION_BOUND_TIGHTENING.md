# IV-185 — Dependency-Aware Aggregation Tightening

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional analytic bound tightening; upstream implicit-root premises remain unverified.

## 1. Purpose and dependency retained

Previous componentwise estimates bounded the radial derivatives of \(P_u\) and \(P_z\) separately, then added them. That is valid but loses the known prefactor dependency \(p+(1-p)=1\) in the sum.

Definitions retained from IV-180:
\[
P_u=16pA^2H,\quad P_z=16(1-p)G^2H,\quad
P_w=1024tp(1-p)F^{-2}.
\]
Use the inherited ceilings \(M=16.7619677501\), \(H\le1/3969\), \(|A|,|G|\le M\), \(|A_t|,|G_t|<50.084572\), \(|A_p|,|G_p|<0.532250\), \(|H_t|<0.002131\), \(|H_p|<1.535\times10^{-6}\), \(F\ge63/4\), \(|F_t|<50.084572\), \(|F_p|\le0.032249938\), and \(t\le1/64\). These premises are conditional and are not re-proved here.

## 2. Joint amplitude bound

Because \(p+(1-p)=1\),
\[
P_u+P_z=16H[pA^2+(1-p)G^2]
\le16M^2H<1.132632151.
\]
Also \(P_w<0.016124969\). Thus
\[
S=P_u+P_z+P_w<1.148757119,
\]
rounded upward, \(\boxed{S<1.148758}\). This improves the old independent sum ceiling 2.281390 without changing the component definitions.

## 3. Joint radial derivative bound

The product-rule estimates retain the weights:
\[
|(P_u)_t+(P_z)_t|
\le16[p+(1-p)](2M(50.084572)H+M^2(0.002131)).
\]
Numerically, the pair ceiling is 16.348318014. Adding the existing conservative \(|(P_w)_t|<1.134551908\) yields
\[
\boxed{|S_t|<17.482869921}
\]
(rounded upward).

## 4. Joint angular derivative bound

The leading angular terms are \(16(A^2-G^2)H\). Without a proven relation that forces cancellation, retain the safe estimate \(|A^2-G^2|\le2M^2\). The weighted chain-rule terms use \(p+(1-p)=1\):
\[
|(P_u)_p+(P_z)_p|
\le16(2M^2H+2M(0.532250)H+M^2(1.535\times10^{-6})).
\]
This gives 2.344094682. Adding \(|(P_w)_p|<0.064565910\) gives
\[
\boxed{|S_p|<2.408660592}.
\]

## 5. Tightened normalization derivatives

With \(D=1+tS\), \(D\ge1\):
\[
|D_t|=|S+tS_t|<S_*+t_*S_{t,*}<1.421926962,
\]
\[
|D_p|=t|S_p|<0.037635322.
\]
These replace the previous looser ceilings 2.810002 and 0.074297 for downstream quotient estimates, under the same assumptions.

## 6. Updated normalized derivative ceilings

Using IV-180 individual component derivative ceilings and the tightened \(D_t,D_p\), the quotient estimate gives:
- \(|(Q_u)_t|, |(Q_z)_t|<17.958840401\).
- \(|(Q_w)_t|<1.157480573\).
- \(|(Q_u)_p|, |(Q_z)_p|<2.387847008\).
- \(|(Q_w)_p|<0.065172870\).

For corrected \(Q_3=(P_z+P_w)/D\), the corresponding ceilings are:
- \(|(Q_3)_t|<19.116320973\).
- \(|(Q_3)_p|<2.453019877\).

## 7. Audit and scope

This is a dependency-aware improvement, not an optimal/sharp bound. It preserves the prefactor relation but still uses coarse independent ceilings for \(A,G,H\) and their derivatives. The calculations remain conditional on inherited domain, branch, implicit-root, and sign premises, including \(R_d\le0\). No independent interval-arithmetic certificate or formal proof is claimed in this record.
