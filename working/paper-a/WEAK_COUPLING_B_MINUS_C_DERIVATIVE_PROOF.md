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

The following elementary analytic-positivity observation controls its entropy derivative. If a nonnegative real-analytic eigenvalue branch is \(O(r^3)\) jointly in \(r\) and the edge variables, then at the uniform point either:
- its first nonzero coefficient in \(r\) is positive, giving a lower bound \(c r^m\) and an entropy derivative \(O(r^m|\ln r|)\), with \(m\ge3\); or
- that coefficient vanishes at the uniform point, in which case nonnegativity makes its first edge derivative vanish, and one proceeds to the next coefficient; or
- the branch is identically zero on the uniform path, in which case its entropy directional derivative is zero.

In every case, the first directional derivative of this branch's entropy at the uniform point is

\[
O_N\!\left(r^3(1+|\ln r|)\right).
\]

The same minimum argument handles the zero branch of \(M_{\rm odd}\).

Let \(\nu\) be the large eigenvalue of the \((++ , --)\) block. Trace one gives

\[
\nu+q+\lambda_0+\lambda_s=1,
\]

where \(\lambda_0\) is the small branch of \(M_{\rm odd}\). Therefore

\[
S(\rho_{12})=H(q)+R_{12},
\]

where, at the uniform point, the first edge derivatives satisfy

\[
\partial_{u_e}R_{12}
=O_N\!\left(r^3(1+|\ln r|)\right).
\]

This estimate includes the entropy of \(\lambda_s\), the zero branch \(\lambda_0\), and the correction from replacing \(\nu\) by \(1-q\). It does not assume a logarithmic bound from an upper eigenvalue estimate alone.

## 5. Leading derivative of the positive odd-block eigenvalue

At the uniform point,

\[
p=\frac{N-1}{16}r^2+O_N(r^3),
\qquad
q=\frac{N-2}{8}r^2+O_N(r^3).
\]

The shared-edge derivatives satisfy

\[
\partial_{u_{13}}p_1
=\frac{r^2}{8}+O_N(r^3),
\qquad
\partial_{u_{13}}q
=\frac{r^2}{8}+O_N(r^3).
\]

The other site marginal and the disjoint-edge derivatives have no order-\(r^2\) term:

\[
\partial_{u_{13}}p_2=O_N(r^3),
\quad
\partial_{u_{34}}p_i=O_N(r^3),
\quad
\partial_{u_{34}}q=O_N(r^3).
\]

Since \(I_{12}=H(p_1)+H(p_2)-H(q)-R_{12}\) with the sign convention \(R_{12}\) absorbed into the remainder, and

\[
H'(t)=\ln\frac{1-t}{t},
\]

we obtain

\[
B-C
=\frac1J\frac{r^2}{8}
\left[H'(p)-H'(q)\right]
+O_N\!\left(\frac{r^3}{J}(1+|\ln r|)\right).
\]

Now

\[
H'(p)-H'(q)
=\ln\frac{q}{p}
+\ln\frac{1-p}{1-q}
=\ln\!\left(\frac{2(N-2)}{N-1}\right)+O_N(r).
\]

Consequently,

\[
\boxed{
B-C
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)
+O_N\!\left(
\frac{J^2}{h^3}
\left[1+\left|\ln(J/h)\right|\right]
\right).
}
\]

For every \(N\ge4\),

\[
\frac{2(N-2)}{N-1}>1,
\]

so the leading coefficient is strictly positive. Since \(r|\ln r|\to0\), it follows that for each fixed finite \(N\ge4\) there exists \(\delta_N>0\) such that

\[
0<J/h<\delta_N
\quad\Longrightarrow\quad B-C>0
\]

at the uniform point.

## 6. Scope and open checks

- This proves only a local weak-coupling endpoint asymptotic, not global positivity for every \(J/h\).
- The conservative \(O(J^2h^{-3}|\ln(J/h)|)\) remainder is used; the stronger \(O(J^3h^{-4})\) source remainder is not claimed.
- The first-order coherence in the odd block must be retained; omitting it reverses the leading sign.
- The proof relies on joint analyticity and positivity of the reduced-state eigenvalue branches; the detailed analytic-positivity lemma should be formalized separately.
- No Lean proof or manuscript correspondence audit has been completed.
- No Absolute Symmetry file has been modified.

**Conclusion:** The corrected weak-coupling leading sign is positive, not negative. The analytic route supplies a conservative derivative remainder sufficient to establish local positivity for each fixed finite \(N\ge4\), subject to the proof-review obligations above.
