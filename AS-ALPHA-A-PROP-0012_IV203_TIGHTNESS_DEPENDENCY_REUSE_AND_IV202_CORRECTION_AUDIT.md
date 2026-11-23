# IV-203 — Tightness, Dependency Reuse, and Correction Audit of IV-202

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional recalculation; source formulas/domain and root premises remain open.

## 1. Critical audit finding
IV-202 contains an arithmetic propagation error in its dependency-aware radial pair bound and an invalid substitution in the radial bound for \(Q_3\). This audit corrects them rather than treating IV-202's ceilings as certified.

With \(d_*=256/63\), \(t_*=1/64\), and the improved \(d_t<4.128\):
\[
a_*=d_*^2=16.511967750062986,
\quad a_{t,*}=2d_*\cdot4.128=33.54819047619048.
\]
Re-evaluating IV-187's displayed absolute expression gives
\[
|B_t|<1661.0503416717656,
\]
not IV-202's reported 2197.433309674. With updated \(|H_t|<0.002105274303669006\), the pair radial derivative becomes
\[
|(P_u+P_z)_t|<15.879978972296358,
\]
rather than 18.042268589. Add \(|(P_w)_t|<1.133453604817533\):
\[
|S_t|<17.013432577113893.
\]
Upward ceilings to 9 decimal places: \(|B_t|<1661.050341672\), pair \(<15.879978973\), and \(|S_t|<17.013432578\).

## 2. Corrected denominator derivatives
Retain the dependency-aware amplitude \(S<1.081145\), \(|S_p|<0.204389553\), and \(D=1+tS\):
\[
D<1.016892890625,
\]
\[
|D_t|<1.346979884017405,
\quad |D_p|<0.003193586765625.
\]
The displayed rounded ceilings \(|D_t|<1.346979885\), \(|D_p|<0.003193587\) are upward.

## 3. Correct quotient derivative estimates
Use the IV-202 component bounds and the conservative quotient estimate \(|(Q_i)_v|\le |(P_i)_v|+P_i^*|D_v|\), with \(D\ge1\):
\[
|(Q_u)_t|,|(Q_z)_t|<17.685815884832063,
\]
\[
|(Q_u)_p|,|(Q_z)_p|<2.348786655759110,
\]
\[
|(Q_w)_t|<1.155173613690937,
\quad |(Q_w)_p|<0.064617406487595.
\]
Upward ceilings at 9 decimal places:
- radial pair components: 17.685815885
- angular pair components: 2.348786656
- \(Q_w\) radial: 1.155173614
- \(Q_w\) angular: 0.064617407

### Correction to \(Q_3\)
\(Q_3=(P_z+P_w)/D\), not \((P_u+P_z+P_w)/D\) and not a numerator to which the \((P_u+P_z)_t\) pair bound may be substituted. Therefore its radial numerator derivative must use the individual \((P_z)_t\) ceiling plus \((P_w)_t\):
\[
|(Q_3)_t|<18.840989498523,
\quad |(Q_3)_p|<2.413404062246705.
\]
Upward ceilings: \(18.840989499\), \(2.413404063\). This corrects IV-202's \(20.761886575\) radial ceiling; the earlier estimate was not justified by the stated numerator.

## 4. Corrected vector and Jacobian aggregate
For \(Q=(Q_u,Q_z,Q_w)\):
\[
\|Q_t\|_2<25.0381827036653,
\quad\|Q_p\|_2<3.322314391770489,
\]
\[
\|J_Q\|_F<25.257639755525247.
\]
Upward ceilings:
\[
\|Q_t\|_2<25.038182704,\quad
\|Q_p\|_2<3.322314392,\quad
\|J_Q\|_F<25.257639756.
\]
Thus the corrected arithmetic ceiling is lower than IV-196's 25.525810, but **not** the IV-202 claimed 25.311254311; IV-202's propagated values are superseded.

## 5. Dependency/tightness notes
- The weighted pair identity is useful for \(S\)'s radial derivative, but cannot be repurposed for \(P_z+P_w\), which is the numerator of \(Q_3\).
- Component-wise absolute-value quotient estimates still lose dependency/cancellation between numerator and denominator. This audit does not assert optimality/tightness.
- The next tightening effort should derive quotient derivatives directly from \(Q_i=P_i/(1+tS)\), preserve shared variables, and avoid independently maximizing each factor where joint constraints can be proved.
- These remain conditional ceilings; no interval-arithmetic or Lean proof is supplied. Root existence/uniqueness, source fidelity, full domain and segment conditions, and upstream assumptions remain unresolved.

## 6. Verdict
**PASS — correction/recalculation for displayed formulas.** IV-202's radial pair arithmetic and \(Q_3\) radial substitution are identified and corrected. Corrected aggregate is \(25.257639756\) (upward ceiling), conditional. IV-202 is superseded for its affected radial derivative and aggregate values. This is not theorem-level closure.
