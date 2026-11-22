# IV-181 — Normalized probability derivative bounds (quotient audit)

Status: conditional estimates using IV-180 ceilings. This is not a proof of the upstream implicit-root assumptions.

## 1. Definitions
For each squared component, normalized quantities are \(Q_i=P_i/D\), with \(D=1+tS\), \(D\ge1\), and \(S=P_u+P_z+P_w\). Quotient rule:
\[
(Q_i)_q=(P_i)_q/D-P_iD_q/D^2,
\]
so the conservative ceiling is \(|(Q_i)_q|\le |(P_i)_q|+P_i|D_q|\), for \(q\in\{t,p\}\).

Inputs from IV-180: component amplitude ceilings \(P_u,P_z<1.132633\), \(P_w<0.016125\); derivative ceilings for u/z are 16.348319 (t), 2.345220 (p); for w are 1.134552 (t), 0.064566 (p); \(|D_t|<2.810002\), \(|D_p|<0.074297\).

## 2. Normalized component ceilings
- \(|(Q_u)_t|, |(Q_z)_t| < 19.531020\).
- \(|(Q_u)_p|, |(Q_z)_p| < 2.429372\).
- \(|(Q_w)_t| < 1.179864\).
- \(|(Q_w)_p| < 0.065765\).

These use the quotient estimate above and round upward.

## 3. Corrected Q3 (from IV-173)
\[
Q_3=(P_z+P_w)/D.
\]
Amplitude ceiling: \(Q_3\le P_z+P_w<1.148758\), since \(D\ge1\).
Derivative ceilings:
- \(|(Q_3)_t|<20.710884\).
- \(|(Q_3)_p|<2.495136\).

## 4. Limitations
All results here inherit IV-180 assumptions and ceilings. The bounds are coarse and are not certified by interval arithmetic or an independent formal checker. This note only records quotient-rule arithmetic, not a proposition-level proof.
