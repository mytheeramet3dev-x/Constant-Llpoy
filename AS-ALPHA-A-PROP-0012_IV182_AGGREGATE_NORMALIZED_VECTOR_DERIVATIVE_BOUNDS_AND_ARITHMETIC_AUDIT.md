# IV-182 — Aggregate normalized-vector derivative bounds and arithmetic audit

Status: conditional analytic ceilings; this record does not independently validate the upstream assumptions.

## 1. Arithmetic recheck of IV-180 and IV-181
Re-evaluation of the displayed IV-180 constants yields:
- \(P_u,P_z<1.132632151\) (the recorded ceiling 1.132633 is upward-rounded).
- \(P_w<0.016124969\) (recorded 0.016125 is upward-rounded).
- \(|(P_u)_t|,|(P_z)_t|<16.348318014\) (recorded 16.348319 is upward-rounded).
- \(|(P_u)_p|,|(P_z)_p|<2.345219540\) (recorded 2.345220 is upward-rounded).
- \(|(P_w)_t|<1.134551908\) (recorded 1.134552 is upward-rounded).
- \(|(P_w)_p|<0.064565910\) (recorded 0.064566 is upward-rounded).
- \(S<2.281389270\), \(|S_t|<33.831187934\), \(|S_p|<4.755004990\).
- \(|D_t|<2.810001582\), \(|D_p|<0.074296953\).

The previously recorded IV-181 normalized ceilings are also checked against these constants and remain conservative:
\[
|(Q_u)_t|,|(Q_z)_t|<19.531020,
\quad |(Q_w)_t|<1.179864;
\]
\[
|(Q_u)_p|,|(Q_z)_p|<2.429372,
\quad |(Q_w)_p|<0.065765.
\]
Corrected \(Q_3=(P_z+P_w)/D\) derivative ceilings remain \(|(Q_3)_t|<20.710884\), \(|(Q_3)_p|<2.495136\).

## 2. Aggregate bounds for the normalized vector
Let \(\mathbf Q=(Q_u,Q_z,Q_w)\). Componentwise derivative ceilings imply Euclidean norm ceilings:
\[
\|\partial_t\mathbf Q\|_2
<\sqrt{2(19.531020)^2+(1.179864)^2}<27.646217,
\]
\[
\|\partial_p\mathbf Q\|_2
<\sqrt{2(2.429372)^2+(0.065765)^2}<3.436279.
\]
The corresponding componentwise L1 ceilings are:
\[
\|\partial_t\mathbf Q\|_1<40.241895,
\qquad
\|\partial_p\mathbf Q\|_1<4.924506.
\]
These are derivative-vector bounds, not yet a global Lipschitz theorem unless the differentiability and domain/segment conditions are established.

## 3. Scope
The arithmetic is checked from the recorded ceilings. Bounds remain conditional on upstream domain, implicit-root, and sign assumptions (notably \(R_d\le0\)); no independent interval-arithmetic certificate or formal proof is claimed here.
