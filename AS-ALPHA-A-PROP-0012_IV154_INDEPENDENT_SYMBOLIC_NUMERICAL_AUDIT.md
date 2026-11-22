# IV-154 — Independent Symbolic–Numerical Audit of the Implicit Ground-State Branch

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC AUDIT / NUMERICAL CHECK; not exhaustive and not Lean-verified

## 1. Audit scope and reproducibility

This audit independently compares the scalar implicit equation for the ground-state parameter against direct eigensolutions of the 4-by-4 matrix model, checks the implicit derivative formulas against central finite differences, checks the stated IV-150 radial derivative bounds at sampled interior points, and tests the expected symmetry identities on sampled points and symmetry axes.

All numerical checks are finite-sample diagnostics. They are not substitutes for exact proof, and they do not independently validate the matrix model against the original Paper A manuscript.

## 2. Scalar branch versus direct eigenvalue

For the matrix model M(x,y), let lambda_min denote the lowest eigenvalue and define d=1-lambda_min. The scalar equation audited is

\[
d-4=R(d,t,m),\qquad
R=\frac{16t(d^2-16mt)}{d(d^2-16t)},
\]
with t=x^2+y^2 and m=(x^2-y^2)^2/t^2 for t>0.

Direct diagonalization and scalar root-solving were compared at representative points:
- (x,y)=(0.1,0.05): d_direct=4.049775641458633; d_scalar=4.049775641458636.
- (0.2,0.1): d_direct=4.196443999369126; d_scalar=4.196443999369126.
- (0.1,0.2): d_direct=4.1964439993691265; d_scalar=4.196443999369126.
- (0.25,0): d_direct=4.23606797749979; d_scalar=4.23606797749979.
- (0,0.25): d_direct=4.23606797749979; d_scalar=4.23606797749979.
- (0.3,0.2): d_direct=4.506439378966283; d_scalar=4.506439378966006.

Observed discrepancies are at floating-point/root-solver scale (up to about 3e-13 in this listed set).

## 3. Corrected Cartesian derivative of m

An initial derivative expression used during the audit was incorrect and was discarded before recording the final result. The correct derivatives of

\[
m=\frac{(x^2-y^2)^2}{(x^2+y^2)^2}
\]
are

\[
m_x=\frac{8xy^2(x^2-y^2)}{(x^2+y^2)^3},\qquad
m_y=-\frac{8x^2y(x^2-y^2)}{(x^2+y^2)^3}.
\]

The implicit derivatives are

\[
d_x=\frac{2xR_t+m_xR_m}{1-R_d},\qquad
d_y=\frac{2yR_t+m_yR_m}{1-R_d},
\]
where partial derivatives of R hold the other independent variables fixed.

This correction matters: using the earlier erroneous m_x,m_y expressions produced discrepancies of order 10^-2 against finite differences. After correction, the analytic derivatives agreed with central finite differences (epsilon=10^-6) at five representative points to roughly 4e-10 or better:
- (0.1,0.05): dx 0.78820651605655, dy 0.40566459063268.
- (0.2,0.1): dx 1.51029703972226, dy 0.83811996135316.
- (0.1,0.2): dx 0.83811996135316, dy 1.51029703972226.
- (0.3,0.2): dx 2.16214260149774, dy 1.66117682453558.
- (0.2,-0.15): dx 1.53894195647419, dy -1.22392964130590.

This audit also cross-checks the Cartesian derivative route, rather than relying only on polar-coordinate expressions.

## 4. Radial derivative bounds (IV-150) sample check

Using the recorded IV-150 candidate bounds

\[
L_t=\frac{16(d^4-8d^2+16)}{d^5}
\]
and
\[
U_t=\frac{16(d^4+16)}{d(d^2-4)^2},
\]
together with
\[
B=\frac{16t}{(d-4\rho)^2},\qquad
\frac{L_t}{1+B}\le d_t\le U_t,
\]
a seeded random sample of 1,000 points with radii uniformly sampled in (0.001,0.499) and angles in [0,2pi) produced zero bound violations. This is only a numerical stress check, not proof of the inequalities for all points.

## 5. Symmetry and axes

Direct eigenvalue/scalar comparisons confirm the expected coordinate-swap symmetry d(x,y)=d(y,x) at representative exchanged points. The x- and y-axis samples (0.25,0) and (0,0.25) agree. The scalar branch depends on t and m, both invariant under sign changes and coordinate interchange, supporting the stated branch symmetries.

At the origin, the angular variable m is undefined, so the scalar polar representation must be interpreted by a limit. The original matrix is well-defined there, has lambda_min=-3, hence d(0,0)=4. Symmetry and differentiability of the nondegenerate eigenvalue branch imply zero first derivative at the origin; the polar formulas are not to be evaluated directly at rho=0.

## 6. Audit findings

**Passed in the checks performed**
- Scalar implicit root agrees with direct lowest-eigenvalue computation at listed test points.
- Corrected Cartesian implicit derivatives agree with central finite differences at listed points.
- 1,000 sampled interior points showed no IV-150 radial-bound violations.
- Coordinate swap and axis symmetry checks agree with the model.

**Correction recorded**
- The Cartesian derivative of m was corrected in this audit. Any prior derivative calculation using the discarded expression must not be reused.

**Not established**
- Exhaustive symbolic proof of all IV-150 inequalities.
- Independent verification of all prior IV-146/147 probability and entropy identities.
- Lean formalization, independent human review, or reconciliation with the original manuscript.
- Uniform boundary behavior as rho approaches 1/2.

## 7. Next action

Prioritize exact symbolic derivation of the Cartesian gradient and a review of radial-bound inequalities before deriving additional global geometry or entropy monotonicity claims.
