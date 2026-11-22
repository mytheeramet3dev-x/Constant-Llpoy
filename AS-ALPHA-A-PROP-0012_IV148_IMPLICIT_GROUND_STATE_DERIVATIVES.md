# IV-148 — Implicit Ground-State Derivative Analysis

**Status:** ANALYTICAL DERIVATION / MODEL-CONDITIONAL; not Lean-verified; source-model reconciliation remains open.

## Model
Let
\[
M=\begin{pmatrix}-3&b^T\\b&N\end{pmatrix},\quad
b=(-4x,0,-4y)^T,\quad N=I+K,
\]
\[
K=\begin{pmatrix}0&-4y&0\\-4y&0&-4x\\0&-4x&0\end{pmatrix}.
\]
For the ground eigenvalue \(\lambda\le -3\), set \(d=1-\lambda\ge4\), \(A=N-\lambda I=dI+K\), and \(F=d^2-16(x^2+y^2)\). On \(\rho=\sqrt{x^2+y^2}<1/2\), \(F>0\) and \(A\) is positive definite.

## Schur equation
The Schur complement gives
\[
d-4=b^TA^{-1}b=:R(d,x,y).
\]
Direct symbolic simplification gives the explicit rational form
\[
R(d,x,y)=\frac{16\left[d^2(x^2+y^2)-16(x^2-y^2)^2\right]}{d\left[d^2-16(x^2+y^2)\right]}.
\]
The formula is positive for \(0<\rho<1/2\), consistent with \(d>4\); at the origin, \(d=4\).

## Implicit derivatives
Define \(G(d,x,y)=d-4-R(d,x,y)\). Since
\[
\partial_d R=-b^TA^{-2}b<0
\]
for nonzero coupling (and equals zero at the origin), we have
\[
\partial_dG=1+b^TA^{-2}b>0.
\]
Consequently the implicit branch is locally differentiable (indeed analytic where the eigenvalue remains simple), and
\[
\boxed{d_x=\frac{R_x}{1+b^TA^{-2}b}},\qquad
\boxed{d_y=\frac{R_y}{1+b^TA^{-2}b}},
\]
where \(R_x,R_y\) are partial derivatives with \(d\) held fixed. In radial–angular coordinates,
\[
\boxed{d_\rho=\frac{R_\rho}{1+b^TA^{-2}b}},\qquad
\boxed{d_\theta=\frac{R_\theta}{1+b^TA^{-2}b}},
\]
with the corresponding partial derivatives of \(R(d,\rho,\theta)\) taken at fixed \(d\).

These formulas give a derivative framework but do **not** by themselves establish the sign of \(d_\rho\) or \(d_\theta\). Monotonicity remains open and must be determined by sign analysis of the numerators.

## Proof obligations / limitations
- The Schur equation and rational expression are for the stated matrix model; the original manuscript/source proposition is not yet reconciled.
- Differentiability follows from the simple isolated ground branch and the nonzero implicit derivative.
- No radial/angular monotonicity claim is made here.
- No formal Lean proof or independent audit is claimed.

## Record
IV-148 derives an explicit Schur scalar and implicit derivative identities. This record is not a verified theorem about an unreconciled source model.
