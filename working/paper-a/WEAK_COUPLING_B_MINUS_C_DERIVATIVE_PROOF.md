# Weak-Coupling General-Edge Derivation for \(B-C\)

**Target:** Corrected weak-coupling asymptotic of \(B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}\).  
**Scope:** Fixed finite \(N\ge4\), transverse-field-dominated TFIM, \(r=J/h\to0^+\), uniform reference \(J_{ij}=J>0\), with independent real edge perturbations near that point.  
**Status:** Candidate analytic derivation for independent review. The remainder is deliberately stated at the conservative order \(O_N(J^2h^{-3}|\ln(J/h)|)\); the stronger \(O(J^3h^{-4})\) source remainder is not assumed.

## 1. Analytic perturbation setup

Write

\[
J_{ij}=J(1+u_{ij}),\qquad |u_{ij}|<\delta,\qquad r=J/h.
\]

At \(r=0\), the Hamiltonian is

\[
H_0=-h\sum_i\sigma_i^x
\]

with unique ground state \(|+\cdots+\rangle\) and a gap \(2h\). The interaction perturbation flips pairs of \(x\)-basis spins. For fixed finite \(N\), the ground-state projector is jointly analytic in \(r\) and the independent edge variables \(\mathbf u\) in a sufficiently small neighborhood.

The first-order state is

\[
|\Psi_0\rangle
=|+\cdots+\rangle
+\sum_{i<j}a_{ij}|i,j\rangle
+O_N(r^2),
\qquad
a_{ij}=\frac{J_{ij}}{4h}
=\frac r4(1+u_{ij}).
\]

Set \(w_{ij}=a_{ij}^2\).

Unlike the strong-coupling endpoint, the perturbation here is in the edge couplings. No symmetry under simultaneous \(J_{ij}\mapsto-J_{ij}\) is assumed; odd powers of \(r\) may occur in higher-order coefficients. This is why the conservative remainder below allows an \(r^3\) term.

## 2. One-site small eigenvalues

The one-site reduced state is diagonal in the \(x\)-basis by global bit-flip parity. Its small eigenvalue is

\[
p_i(\mathbf u,r)
=\sum_{j\ne i}w_{ij}+O_N(r^3).
\]

This is a jointly analytic expansion, including first derivatives in every \(u_e\). At the uniform point,

\[
p_1=p_2=p+O_N(r^3),
\qquad
p=\frac{N-1}{16}r^2.
\]

The leading edge derivatives are

\[
\partial_{u_{13}}p_1
=\frac{r^2}{8}+O_N(r^3),
\qquad
\partial_{u_{13}}p_2=O_N(r^3),
\]

and

\[
\partial_{u_{34}}p_1=O_N(r^3),
\qquad
\partial_{u_{34}}p_2=O_N(r^3).
\]

For sufficiently small \(r>0\), \(p_i\asymp_N r^2\), so the binary entropy

\[
H(p)=-p\ln p-(1-p)\ln(1-p)
\]

has a controlled logarithm. Exactly,

\[
S(\rho_i)=H(p_i).
\]

## 3. Two-site reduced state and the order-\(r^2\) coherence

In the \(x\)-basis \((++,+-,-+,--)\), global parity splits \(\rho_{12}\) into two \(2\times2\) blocks.

The block on \((+-,-+)\) has the leading form

\[
M_{\rm odd}
=
\begin{pmatrix}
\displaystyle\sum_{k\ge3}a_{2k}^2&
\displaystyle\sum_{k\ge3}a_{1k}a_{2k}\\[2mm]
\displaystyle\sum_{k\ge3}a_{1k}a_{2k}&
\displaystyle\sum_{k\ge3}a_{1k}^2
\end{pmatrix}
+O_N(r^3).
\]

The off-diagonal coherence is essential. At the uniform point, the leading matrix is

\[
\frac{N-2}{16}r^2
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

whose eigenvalues are

\[
q=\frac{N-2}{8}r^2
\quad\text{and}\quad 0.
\]

The positive eigenvalue branch is simple after factoring out \(r^2\), so it is jointly analytic near the uniform point:

\[
q(\mathbf u,r)=r^2Q(\mathbf u)+O_N(r^3),
\qquad Q(\mathbf0)=\frac{N-2}{8}>0.
\]

The other branch is nonnegative and is exactly zero at the uniform point for every sufficiently small \(r\), because the uniform ground state is permutation symmetric and the pair singlet has zero support. Its entropy contribution has zero first directional derivative at the uniform point: for fixed \(r>0\), it is a nonnegative analytic eigenvalue attaining an interior minimum of zero, hence it opens at least quadratically in every real edge direction.

For the positive branch, the eigenvector at the uniform point is \((1,1)/\sqrt2\). Differentiating the leading matrix gives

\[
\partial_{u_{13}}q
=\frac{r^2}{8}+O_N(r^3),
\qquad
\partial_{u_{34}}q=O_N(r^3).
\]

Indeed, \(J_{13}\) changes \(a_{13}\), while \(J_{34}\) does not enter the leading Gram matrix.

## 4. The \((++ , --)\) block and its entropy remainder

The other parity block, on \((++,--)\), has entries

\[
L=1+O_N(r^2),\qquad
X=a_{12}+O_N(r^2),\qquad
S=a_{12}^2+O_N(r^3).
\]

The order-\(r^2\) Schur term cancels:

\[
S-\frac{|X|^2}{L}=O_N(r^3).
\]

Thus its small eigenvalue \(\lambda_s\) is a jointly analytic nonnegative branch of order \(O_N(r^3)\), with first edge derivatives of the same order.

Apply the reusable analytic nonnegative-eigenvalue entropy lemma in

audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md.

Its hypotheses hold for \(\lambda_s\): the block eigenvalue is jointly analytic, nonnegative, and \(O_N(r^3)\) jointly in \(r,\mathbf u\). Therefore its first edge-direction entropy derivative at the uniform point is

\[
O_N\!\left(r^3(1+|\ln r|)\right).
\]

The other small branch \(\lambda_0\) is exactly zero at the uniform point for every sufficiently small \(r\), so the same lemma's zero-branch case gives a zero first entropy directional derivative.
