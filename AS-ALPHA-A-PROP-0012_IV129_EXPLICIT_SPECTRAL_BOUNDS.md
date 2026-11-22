# IV-129 — Explicit Spectral and Eigenvector Bounds (Initial Quantitative Step)

**Status:** VALIDATED OPERATOR-NORM ESTIMATES; FACTORIZATION COEFFICIENT BOUNDS NOT YET CLOSED.  
**Proposition:** AS-ALPHA-A-PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.

## 1. Choose a concrete absolute-coupling box
Set \(\rho=10^{-3}\) and assume \(|x|,|y|\le\rho\), where \(x=\varepsilon A\), \(y=\varepsilon B\).

The symmetric perturbation from the uncoupled matrix consists of four edge entries (and their transposes), each of magnitude \(4|x|\) or \(4|y|\). Its Frobenius norm obeys
\[
\|E\|_2\le\|E\|_F=4\sqrt{2x^2+2y^2}\le8\rho=0.008.
\]
By Weyl's eigenvalue inequality, the lowest eigenvalue shifts by at most 0.008 from -3. The unperturbed gap is 4, so this box preserves a separated lowest eigenvalue; the distance from the lowest eigenvalue to the upper cluster is at least \(4-2(0.008)=3.984\).

## 2. Bound the lower-block resolvent
Write the lower block as \(N=I+K\). The matrix \(K\) has four symmetric off-diagonal entries with magnitudes \(4|x|,4|y|\), so
\[
\|K\|_2\le\|K\|_F\le8\rho=0.008.
\]
Writing \(\lambda=-3+\delta\), Weyl gives \(|\delta|\le0.008\). Hence
\[
N-\lambda I=4I+(K-\delta I),
\quad \|K-\delta I\|_2\le0.016.
\]
The Neumann/resolvent bound therefore yields
\[
\|(N-\lambda I)^{-1}\|_2
\le\frac{1}{4-0.016}=\frac1{3.984}.
\]

## 3. Bound the eigenvector coordinates (absolute bound)
The lower equations are \((N-\lambda I)v=-c\), with \(v=(u,w,z)^T\) and \(\|c\|_2=4\sqrt{x^2+y^2}\). Therefore
\[
\|v\|_2\le\frac{4\sqrt{x^2+y^2}}{3.984}
\le\frac{4\sqrt2\rho}{3.984}<0.001422.
\]
Thus each of \(|u|,|w|,|z|\) is below 0.001422 on this box. Consequently \(D=1+u^2+w^2+z^2\ge1\), and the recorded probabilities are small (in particular \(q,q_3<1/2\)).

## 4. Important limitation
These norm bounds do **not** yet give finite explicit bounds for \(U=u/x\), \(W=w/(xy)\), or \(Z=z/y\) at the axes. Componentwise eigenvector bounds alone cannot divide by small couplings. To close IV-127, exploit the analytic parity factorization and the equations to derive quotient bounds separately. No positivity proof is claimed in this file.

## 5. Audit status
- Spectral perturbation bound in the box: established by Frobenius norm + Weyl.
- Resolvent bound: established with the stated constants.
- Absolute eigenvector coordinate bound: established.
- Quotient/factor bounds \(U,W,Z\): OPEN.
- Local entropy positivity proof: not completed.
- Lean verification: not completed.
