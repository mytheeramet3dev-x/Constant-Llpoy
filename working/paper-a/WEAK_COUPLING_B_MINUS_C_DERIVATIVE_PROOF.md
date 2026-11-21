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

## 4. The `(++ , --)` block: shared-amplitude Schur cancellation

Write the even block entries as exact environment sums over even environment
flip sets (Esubseteq{3,ldots,N}):
[
L=sum_E|c_E|^2,quad
X=sum_Ec_Eoverline{c_{Ecup{1,2}}},quad
S=sum_E|c_{Ecup{1,2}}|^2.
]
Separate the empty environment without truncating the shared amplitude:
[
L=|c_emptyset|^2+R_L,quad
X=c_emptysetoverline{c_{12}}+R_X,quad
S=|c_{12}|^2+R_S.
]
By the pair-flip support lemma, for fixed finite (N), nonempty even (E)
has (|E|ge2), and the corresponding amplitudes have orders
(c_E=O_N(r^{|E|/2})), (c_{Ecup{1,2}}=O_N(r^{(|E|+2)/2}));
the same orders hold for first edge derivatives. Thus
[
R_L=O_N(r^2),quad R_X=O_N(r^3),quad R_S=O_N(r^4),
]
including first edge derivatives. Also (c_emptyset=1+O_N(r^2)) and
(c_{12}=O_N(r)), with first edge derivatives (O_N(r)).

Consequently,
[
rac{|X|^2}{L}=|c_{12}|^2+O_N(r^4),qquad
D:=S-rac{|X|^2}{L}=O_N(r^4),
]
and (partial_{u_e}D=O_N(r^4)) for each first edge direction. The
cancellation is through the exact common amplitude (c_{12}); it does not
assume (c_{12}=a_{12}+O(r^3)). In fact, second-order overlapping pair-flip
paths can give (c_{12}=a_{12}+O_N(r^2)).

If (lambda_L) is the large eigenvalue of this positive block, then it
stays bounded below near the uncoupled point and
[
lambda_s=rac{det M}{lambda_L}
=rac{L}{lambda_L}D=O_N(r^4),qquad
partial_{u_e}lambda_s=O_N(r^4).
]
For a positive analytic branch with its leading logarithmic scale controlled,
the small-branch entropy directional derivative is
(O_N(r^4(1+|ln r|))). An identically-zero/nonnegative branch is handled
separately by the interior-minimum argument; no (ln 0) is evaluated.

This replaces the former conservative (O_N(r^3)) Schur/entropy bound with
the stronger (O_N(r^4)) result **conditional on the stated amplitude-order
lemma and environment-sum hypotheses**. This is fixed-(N), local weak-coupling
analysis; no uniform-in-(N) estimate is claimed.
