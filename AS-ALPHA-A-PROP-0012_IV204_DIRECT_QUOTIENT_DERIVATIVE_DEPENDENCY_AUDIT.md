# IV-204 — Direct Quotient Derivative Audit with Dependency Preservation

## Scope
Independently re-check the quotient derivative formulas and the conditional numerical ceilings recorded in IV-203, with focus on dependency preservation, sign structure, and avoiding unsupported tightening. This is an arithmetic/analytic audit of the displayed reconstruction, not a source-fidelity or formal proof.

## Definitions inherited conditionally
For components i, let Q_i=P_i/D, S=P_u+P_z+P_w, D=1+tS, and Q_3=(P_z+P_w)/D. On the stated box, inherited bounds are P_i>=0, S>=0, D>=1, and the IV-203 conditional ceilings:
- S<1.081145 (amplitude bound)
- S_t<17.013432578
- S_p<0.204389644
- D<1.016892890625
- |D_t|<1.346979884017405
- |D_p|<0.003193586765625
- |P_u|,|P_z|<1.081145; |P_w|<0.016124969
- |(P_u)_t|,|(P_z)_t|<16.160182018; |(P_u)_p|,|(P_z)_p|<2.345169494
- |(P_w)_t|<1.133453605; |(P_w)_p|<0.064566 (inherited angular ceiling).

## Quotient rule
For v in {t,p},
\[
(Q_i)_v=\frac{(P_i)_v}{D}-\frac{P_iD_v}{D^2}.
\]
This identity is valid where D is differentiable and nonzero. Because D>=1, division is safe.

For Q_3, use its numerator N_3=P_z+P_w:
\[
(Q_3)_v=\frac{(P_z)_v+(P_w)_v}{D}-\frac{(P_z+P_w)D_v}{D^2}.
\]
Important dependency correction: the numerator radial derivative is (P_z)_t+(P_w)_t, not (P_u+P_z)_t. IV-203 used this distinction.

## Conservative recalculation using componentwise ceilings
Using |1/D|<=1 and 1/D^2<=1 (since D>=1), the safe generic estimate is
\[
|(Q_i)_v|\le |(P_i)_v|+|P_i||D_v|.
\]
For Q_3:
\[
|(Q_3)_v|\le |(P_z)_v|+|(P_w)_v|+(|P_z|+|P_w|)|D_v|.
\]
These are conservative, dependency-agnostic bounds; they do not exploit exact correlation between numerator and denominator.

### Radial (t) ceilings
Using the displayed upward-rounded ceilings:
- For Q_u,Q_z: 16.160182018 + 1.081145×1.346979884017405 < 17.616462585.
- For Q_w: 1.133453605 + 0.016124969×1.346979884017405 < 1.155173614.
- For Q_3: 16.160182018 + 1.133453605 + (1.081145+0.016124969)×1.346979884017405 < 18.771636199.

### Angular (p) ceilings
Using the displayed ceilings:
- Q_u,Q_z: 2.345169494 + 1.081145×0.003193586765625 < 2.348622225.
- Q_w: 0.064566 + 0.016124969×0.003193586765625 < 0.064617497.
- Q_3: 2.345169494 + 0.064566 + (1.081145+0.016124969)×0.003193586765625 < 2.413239721.

## Audit conclusion
1. Quotient derivative identities: PASS, conditional on component differentiability and D=1+tS.
2. Dependency selection for Q_3: PASS in IV-203's corrected form; the numerator must be P_z+P_w.
3. IV-203 quotient ceilings: this audit does **not** certify the earlier IV-203 values as optimal/tight. They may be valid sharper bounds if their derivation correctly retained D and numerator dependency; however this generic D>=1 component estimate is the independently transparent baseline.
4. The bounds above remain conditional on reconstructed formulas and prior component ceilings. Source-equation fidelity, root/domain closure, interval verification, and Lean formalization remain OPEN.

## Next proof obligations
- Compute and compare the exact generic ceilings from the component ceilings above.
- Independently audit inherited angular component bounds (especially P_w,p) and formulas for P_u/P_z derivatives.
- Do not promote the proposition or claim complete proof closure based on this audit alone.
