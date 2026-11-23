# IV-190 — Source Reconstruction, Normalization Correction, and Recomputed Quotient Bounds

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional arithmetic audit; inherited premises remain unverified.

## 1. Source files recovered
Repository tree confirms the exact IV-180 and IV-185 files:
- IV-180: `AS-ALPHA-A-PROP-0012_IV180_RECOMPUTED_SQUARED_COMPONENT_AND_NORMALIZATION_DERIVATIVE_BOUNDS.md`
- IV-185: `AS-ALPHA-A-PROP-0012_IV185_DEPENDENCY_AWARE_AGGREGATION_BOUND_TIGHTENING.md
IV-180 defines
\[
P_u=16pA^2H,\quad P_z=16(1-p)G^2H,\quad P_w=1024tp(1-p)F^{-2},
\]
and the normalization **\(D=1+tS\)**, not \(D=1+S\).

## 2. Correction to IV-189
IV-189 incorrectly wrote \(D=1+S\). Correct this to
\[
\boxed{D=1+tS}.
\]
The previous IV-189 bounds \(1\le D<2.081145\), \(|D_t|<17.199243\), and \(|D_p|<0.204390\) were consequently not the proper normalization bounds.

From IV-186/187/188:
\[
S<1.081145,\quad |S_t|<17.199242818,\quad |S_p|<0.204389644.
\]
For \(0\le t\le1/64\):
\[
1\le D=1+tS<1+\frac{1.081145}{64}=1.016892890625,
\]
\[
|D_t|=|S+tS_t|<1.081145+\frac{17.199242818}{64}
<1.349883169026,
\]
\[
|D_p|=t|S_p|<\frac{0.204389644}{64}
<0.003193588188.
\]
These are upward-rounded ceilings.

## 3. Recompute normalized derivative ceilings
For \(Q_i=P_i/D\), use \(D\ge1\), \(Q_i\le P_i\), and
\[
|(Q_i)_t|\le |(P_i)_t|+P_i^*|D_t|,\quad
|(Q_i)_p|\le |(P_i)_p|+P_i^*|D_p|.
\]
With the IV-180 component ceilings:
\[
P_u,P_z<1.132633;\quad P_w<0.016124969,
\]
\[
|(P_u)_t|,|(P_z)_t|<16.348319;\quad
|(P_u)_p|,|(P_z)_p|<2.345220,
\]
\[
|(P_w)_t|<1.134552;\quad |(P_w)_p|<0.064566,
\]
the recomputed normalized ceilings are:
- \(|(Q_u)_t|,|(Q_z)_t|<17.877241224\).
- \(|(Q_u)_p|,|(Q_z)_p|<2.348837164\).
- \(|(Q_w)_t|<1.156318825\).
- \(|(Q_w)_p|<0.064617497\).

For the corrected \(Q_3=(P_z+P_w)/D\), use numerator ceilings \(|(P_z+P_w)_t|<17.482870918\), \(|(P_z+P_w)_p|<2.409786\) (componentwise IV-180 sum), and amplitude \(P_z+P_w<1.148758\):
- \(|(Q_3)_t|<19.033560048\).
- \(|(Q_3)_p|<2.413454660\).

These quotient estimates are conservative and conditional.

## 4. Scope
This audit corrects IV-189's normalization mistake and recomputes quotient bounds using the retrieved source records. It does not independently prove the implicit root exists uniquely, \(R_d\le0\), the upstream domain, or the component ceilings. No sharpness or formal verification claim is made.
