# IV-208 — Radial Ceiling Independent Recalculation and IV-207 Revision

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional numerical recalculation; source/domain/root premises remain open.

## 1. Scope
Recompute the radial component and quotient ceilings from the displayed IV-202 formulas, the improved IV-201 root ceiling \(d_t<4.128\), and the dependency-aware radial pair estimate. This resolves the input-provenance discrepancy identified in IV-207.

## 2. Upstream recalculation
Use \(d_*=256/63\), \(t_*=1/64\), \(M=d_*^2+1/4\), \(H_*=1/3969\), \(F_*=63/4\), and \(d_t<4.128\). Then
\[
|A_t|,|G_t|,|F_t|<2d_* (4.128)+16=49.54819047619048.
\]
The displayed IV-202 expression for \(H_t\) yields
\[
|H_t|<0.002105274303669006.
\]
Using the IV-180 product-rule expression with these revised inputs:
\[
|(P_u)_t|,|(P_z)_t|<16.160182017857778,
\]
upward ceiling \(16.160182018\).
The IV-180 \(P_w\) expression gives
\[
|(P_w)_t|<1.133453604817533,
\]
upward ceiling \(1.133453605\).
These arithmetic inputs reproduce IV-202's individual component ceilings.

## 3. Recalculation of dependency-aware radial pair and denominator
The IV-187 absolute expression with \(d_t<4.128\) gives
\[
|B_t|<1661.0503416717656,
\]
not IV-202's stated 2197.433309674. Reusing the dependency-preserving identity and \(H_t\):
\[
|(P_u+P_z)_t|<15.879978972296358,
\]
and therefore
\[
|S_t|<17.013432577113893
\]
after adding the \(P_w\) radial ceiling. Upward ceiling: \(17.013432578\).

With \(D=1+tS\), \(S<1.081145\):
\[
|D_t|<1.081145+\frac{17.013432577113893}{64}
=1.346979884017405,
\]
upward ceiling \(1.346979885\). This confirms the IV-203 corrected denominator radial estimate, while correcting IV-202's inflated pair derivative propagation.

## 4. Generic quotient derivative recalculation
For \(Q_i=P_i/D\), \(D\ge1\), use
\[
|(Q_i)_t|\le |(P_i)_t|+P_i^*|D_t|.
\]
With component ceilings above, \(P_u,P_z<1.081145\), \(P_w<0.016124969\):
\[
|(Q_u)_t|,|(Q_z)_t|<17.616462584563774,
\]
upward ceiling \(17.616462585\);
\[
|(Q_w)_t|<1.155173613690937,
\]
upward ceiling \(1.155173614\).
For the separate scalar \(Q_3=(P_z+P_w)/D\), using \(|(P_z)_t|+|(P_w)_t|\) (not the pair derivative) gives:
\[
|(Q_3)_t|<18.771636198396934,
\]
upward ceiling \(18.771636199\).

## 5. Reconcile IV-203 / IV-204 / IV-207
- IV-203's reported radial quotient ceiling \(17.685815885\) is a larger conservative value; it does not contradict the independently reproduced \(17.616462585\) ceiling when the latter's component input is now derived from the IV-202 displayed product-rule formulas with updated root derivative.
- IV-204's input \(16.160182018\) is traceable and reproduced in §2. Its radial quotient arithmetic is also reproduced in §4. Thus IV-204's lower component quotient ceiling is accepted **conditionally**.
- IV-207 correctly flagged missing provenance at the time it was written, but this audit now supplies the missing numerical derivation. Revise its status: the provenance blocker for this specific component input is resolved; broader root/domain/source-fidelity concerns remain.

## 6. Vector/Jacobian aggregate using IV-205 angular ceilings
Angular ceilings from IV-205 remain:
\[
|(Q_u)_p|,|(Q_z)_p|<2.348672731,\quad |(Q_w)_p|<0.064617497.
\]
Combining with revised radial ceilings:
\[
\|Q_t\|_2<24.940207177656696,\quad
\|Q_p\|_2<3.322153310069321,
\]
\[
\|J_Q\|_F<25.160497544365914.
\]
Upward ceilings:
\[
\|Q_t\|_2<24.940207178,\quad
\|Q_p\|_2<3.322153311,\quad
\|J_Q\|_F<25.160497545.
\]
The operator norm is bounded by the Frobenius norm. This remains a conditional analytic ceiling, not an interval or formal certificate.

## 7. Verdict
**PASS — independent arithmetic propagation for the displayed radial formulas.** IV-204's radial component quotient ceiling is now supported by a reproduced component input; IV-203 remains a conservative higher ceiling; IV-202's dependency-aware pair radial number is corrected. IV-207 is revised by this follow-up, not erased.

**OPEN:** source fidelity, root existence/uniqueness and sign premise, domain coverage, differentiability/segment conditions, rigorous interval verification, Lean formalization, and full proposition closure.
