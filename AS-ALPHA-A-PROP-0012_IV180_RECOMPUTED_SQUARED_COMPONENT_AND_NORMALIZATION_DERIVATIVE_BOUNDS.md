# IV-180 — Recomputed squared-component derivative and normalization bounds

Status: conditional analytic bounds; this record does not certify the underlying implicit-root assumptions.

## 1. Inputs inherited from IV-175–IV-179
Use the stated domain bounds (t\le 1/64), (d\ge4), (d\le256/63), (F=d^2-16t\ge63/4), and conditional (R_d\le0). The inherited derivative bounds are:
- \(|d_t|<4.194\), \(|d_p|\le1/252\).
- \(|A_t|,|G_t|<50.084572\); \(|A_p|,|G_p|<0.532250\).
- \(H\le1/3969\), \(|H_t|<0.002131\), \(|H_p|<1.535\times10^{-6}\).
- \(|F_t|<50.084572\), \(|F_p|\le0.032249938\).

Let \(M=(256/63)^2+1/4=16.7619677501\), so \(|A|,|G|\le M\).

## 2. Component definitions and derivative formulas
\[
P_u=16pA^2H,\quad P_z=16(1-p)G^2H,\quad
P_w=1024tp(1-p)F^{-2}.
\]
By product rule:
\[
|(P_u)_t|,|(P_z)_t|\le16(2M(50.084572)H+M^2(0.002131)).
\]
The angular bounds use \(p,1-p\le1\):
\[
|(P_u)_p|,|(P_z)_p|\le16(M^2H+2M^2(0.532250)H+M^2(1.535\times10^{-6})).
\]
For \(P_w\):
\[
|(P_w)_t|\le1024(1/4)(F^{-2}+2t|F_t|F^{-3}),
\]
\[
|(P_w)_p|\le1024tF^{-2}+2048t(1/4)|F_p|F^{-3}.
\]

## 3. Numerically evaluated conservative bounds (rounded upward)
- \(P_u,P_z<1.132633\); \(P_w<0.016125\).
- \(|(P_u)_t|,|(P_z)_t|<16.348319\).
- \(|(P_u)_p|,|(P_z)_p|<2.345220\).
- \(|(P_w)_t|<1.134552\).
- \(|(P_w)_p|<0.064566\).

Thus, for \(S=P_u+P_z+P_w\):
- \(S<2.281390\).
- \(|S_t|<33.831188\).
- \(|S_p|<4.755005\).

With \(D=1+tS\), it follows:
- \(D\ge1\).
- \(|D_t|=|S+tS_t|<2.810002\).
- \(|D_p|=t|S_p|<0.074297\).

## 4. Audit note / scope
These estimates improve the earlier IV-165 component derivative numbers, which used older, looser radial bounds. They are conditional on the assumptions and upstream constants listed in §1 and on the displayed component formulas. They are not a global proof of the proposition, nor do they validate the implicit-root existence/uniqueness or the condition \(R_d\le0\). The Q3 expression remains the corrected one from IV-173: \((P_z+P_w)/D\).

## 5. Reproducibility
All numerical ceilings above are intentionally rounded upward. This record is a standalone calculation audit; independent machine verification is still pending.
