# IV-206 — Revised Angular Quotient and Jacobian Recalculation after IV-205

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional recomputation; inherited formulas, source fidelity, and root/domain assumptions remain open.

## 1. Corrected input ceilings
IV-205 independently recomputed the angular component ceiling from the displayed IV-180 formula:
- |(P_u)_p|, |(P_z)_p| < 2.345220 (upward)
- |(P_w)_p| < 0.064566 (retained conditionally)
- amplitude bounds |P_u|,|P_z|<1.081145; |P_w|<0.016124969
- |D_p|<0.003193586765625, D>=1.

The lower angular component ceiling 2.345169494 in IV-203/204 is not justified by the retrieved derivation and is superseded.

## 2. Generic quotient derivative ceilings
Use |(Q_i)_p| <= |(P_i)_p|+|P_i||D_p|:
\[
|(Q_u)_p|,|(Q_z)_p|<2.345220+1.081145(0.003193586765625)
=2.3486727303637216.
\]
Upward ceiling at 9 decimals: 2.348672731.

For Q_w:
\[
|(Q_w)_p|<0.064566+0.016124969(0.003193586765625)
=0.06461749648759452,
\]
upward ceiling 0.064617497.

For Q_3=(P_z+P_w)/D:
\[
|(Q_3)_p|<2.345220+0.064566+(1.081145+0.016124969)(0.003193586765625)
=2.4132902268513163,
\]
upward ceiling 2.413290227.

## 3. Recomputed vector derivative norms
Using IV-204 radial generic ceilings:
\[
Q_t^*=(17.616462585,17.616462585,1.155173614),
\]
and corrected angular ceilings:
\[
Q_p^*=(2.348672731,2.348672731,0.064617497).
\]
Euclidean column ceilings:
\[
\|Q_t\|_2<\sqrt{2(17.616462585)^2+(1.155173614)^2}
<24.940207179 
\]
\[
\|Q_p\|_2<\sqrt{2(2.348672731)^2+(0.064617497)^2}
<3.322153311 
\]
Frobenius ceiling combines both column norms. Independent arithmetic gives <25.160497545, rounded upward to 9 decimals.

## 4. Recalculation caveat
IV-204's radial ceilings are generic componentwise bounds based on its recorded inputs. IV-205 audits angular bounds only; radial input bounds have not been independently revisited in this step. Do not mix historical IV-203 tighter quotient ceilings with the generic IV-204 values.

## 5. Verdict and open items
- Angular quotient ceilings: corrected, conditional.
- Radial quotient ceilings: retained from IV-204, conditional.
- Q_3: separately tracked scalar expression; not the third component of Q=(Q_u,Q_z,Q_w).
- Jacobian/Frobenius norm: recalculated from the three component ceilings and two parameter columns; conditional.
- Global Lipschitz claim: still open due domain/segment, differentiability, source-fidelity, root premises, and formal verification.

This is not proof closure or promotion of Proposition AS-ALPHA-A-PROP-0012.
