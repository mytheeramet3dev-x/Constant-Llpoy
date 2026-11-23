# IV-205 — Independent Angular Component Ceiling Audit and IV-204 Correction

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional formula/arithmetic audit. Inherited root, domain, and component assumptions remain unverified.

## 1. Scope
Audit IV-180's componentwise angular estimates for P_u and P_z and the P_w angular derivative; compare with IV-203/IV-204 input ceilings. This is a direct recalculation of the displayed IV-180 formulas, not a source-fidelity proof.

## 2. Angular derivative of P_u/P_z
Definitions:
\[
P_u=16pA^2H,\quad P_z=16(1-p)G^2H.
\]
The IV-180 componentwise absolute-value estimate is
\[
|(P_u)_p|,|(P_z)_p|
\le16\left(M^2H+2M^2(0.532250)H+M^2(1.535\times10^{-6})\right),
\]
with M=(256/63)^2+1/4=16.761967750062986 and H<=1/3969.
Independent arithmetic gives 2.3452195399836016. Rounded upward to 6 decimals:
\[
\boxed{|(P_u)_p|,|(P_z)_p|<2.345220}.
\]

**Discrepancy:** IV-203/IV-204 used 2.345169494, which is lower than this independently recalculated ceiling. The retrieved IV-180 formula and inputs do not justify that lower number. Unless another tighter, fully documented dependency-aware derivation is supplied, replace it with 2.345220.

## 3. Angular derivative of P_w
From IV-180:
\[
|(P_w)_p|\le1024tF^{-2}+2048t(1/4)|F_p|F^{-3},
\]
using t<=1/64, F>=63/4, and |F_p|<=0.032249938. Recalculation yields a value below 0.064566 when rounded upward to 6 decimals. Thus IV-180's ceiling 0.064566 is retained (conditional).

## 4. Corrected generic quotient ceilings from IV-204
Use IV-204's generic estimates with the corrected angular input:
- Q_u,Q_z: 2.345220 + 1.081145(0.003193586765625) = 2.3486727303637216; upward ceiling **2.348672731**.
- Q_w: retained ceiling **0.064617497**.
- Q_3: 2.345220 + 0.064566 + (1.081145+0.016124969)(0.003193586765625) = 2.4132902268513163; upward ceiling **2.413290227**.

The IV-204 angular ceilings 2.348622225 and 2.413239721 are **superseded** by these corrected ceilings. Its radial generic ceilings are unaffected by this audit.

## 5. Verdict
- IV-180 displayed angular estimate for P_u/P_z: arithmetic PASS; ceiling 2.345220.
- IV-203/IV-204 lower input 2.345169494: **not supported by the retrieved derivation**, corrected conservatively.
- P_w angular ceiling 0.064566: retained conditionally.
- Quotient angular ceilings: corrected as above, using D>=1 and inherited component-amplitude ceilings.

All remain conditional. No source fidelity, interval verification, or Lean proof is claimed. Root/domain closure and inherited derivative premises remain open.
