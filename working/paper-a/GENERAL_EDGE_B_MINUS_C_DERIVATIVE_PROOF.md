# General-Edge Strong-Coupling Derivation for \(B-C\)

**Target:** \(B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}\) at the permutation-symmetric point.  
**Scope:** Fixed finite \(N\ge4\), all-to-all ferromagnetic TFIM, uniform \(J>0\), \(h/J\to0^+\).  
**Status:** Candidate analytic proof for independent review. No explicit numerical threshold and no uniform-in-\(N\) bound are claimed.

## 1. Coupling neighborhood and spectral gap

Let the edge couplings vary independently in a small real neighborhood of the uniform point:

\[
J_{ij}=J(1+u_{ij}),\qquad |u_{ij}|<\delta,
\]

where \(\delta>0\) is chosen so every \(J_{ij}>0\). Put \(\varepsilon=h/J\). At \(h=0\), the two ferromagnetic configurations are the ground states. A spin-flip set \(S\subset\{1,\ldots,N\}\) has excitation energy

\[
\Delta_S(\mathbf J)
=2\sum_{i\in S,\ j\notin S}J_{ij}.
\]

For fixed finite \(N\), this is uniformly positive for every nonempty proper \(S\) on a sufficiently small closed neighborhood of the uniform positive point. The even global-bit-flip sector has the isolated simple cat ground state

\[
|C_+\rangle=\frac{|0^N\rangle+|1^N\rangle}{\sqrt2}.
\]

Kato analytic perturbation theory therefore gives a jointly real-analytic even-sector ground-state projector in \((\varepsilon,\mathbf u)\) near \((0,\mathbf0)\). For \(\varepsilon>0\), the Perron–Frobenius ground state is unique and agrees with this even-sector branch.

All constants below may depend on fixed \(N\) and on the chosen coupling neighborhood.

## 2. First-order state for nonuniform edge couplings

For a single spin flip at site \(i\), the excitation gap is

\[
\Delta_i=2\sum_{j\ne i}J_{ij}.
\]

Define

\[
b_i(\mathbf J,h)=\frac{h}{\Delta_i}
=\frac{h}{2\sum_{j\ne i}J_{ij}}.
\]

In the even-parity sector, the normalized ground state has the first-order expansion

\[
|\Psi_0\rangle
=|C_+\rangle
+\sum_{i=1}^{N}b_i|\phi_i^+\rangle
+O_N(\varepsilon^2),
\]

where \(|\phi_i^+\rangle\) is the normalized even-parity pair of configurations with spin \(i\) flipped. Joint analyticity makes the remainder and its first derivatives in every \(u_e\) uniformly controlled on a smaller compact neighborhood.

The global parity symmetry implies that every one-site reduced state has the form

\[
\rho_i=\frac12(I+m_i\sigma_i^x),
\qquad
m_i=2b_i+O_N(\varepsilon^3).
\]

Thus

\[
S(\rho_i)
=\ln2-2b_i^2+O_N(\varepsilon^4),
\]

where the \(O_N(\varepsilon^4)\) remainder is jointly analytic in the edge variables and has edge derivatives \(O_N(\varepsilon^4/J)\).

## 3. Two-site parity blocks and the order-\(\varepsilon^2\) cancellation

Global bit-flip parity gives

\[
[\rho_{12},\sigma_1^x\sigma_2^x]=0.
\]

Use the local parity-adapted basis

\[
|+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\quad
|-\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2},
\]

\[
|\psi_+\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},
\quad
|\psi_-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}.
\]

The reduced state splits into two real symmetric \(2\times2\) blocks,

\[
M_\pm=
\begin{pmatrix}
L_\pm&X_\pm\\
X_\pm&S_\pm
\end{pmatrix},
\]

on \((|+\rangle,|\psi_+\rangle)\) and \((|-\rangle,|\psi_-\rangle)\), respectively. Directly tracing the first-order state gives

\[
L_\pm=\frac12+O_N(\varepsilon^2),
\]

\[
X_\pm=\frac12(b_1\pm b_2)+O_N(\varepsilon^3),
\]

\[
S_\pm=\frac12(b_1\pm b_2)^2+O_N(\varepsilon^4).
\]

The estimates hold jointly and differentiably in the edge variables. Since \(L_\pm\ge c>0\) near the base point, define the Schur complements

\[
Q_\pm=S_\pm-\frac{X_\pm^2}{L_\pm}.
\]

The leading terms cancel exactly:

\[
\frac12(b_1\pm b_2)^2
-\frac{\left[\frac12(b_1\pm b_2)\right]^2}{1/2}
=0.
\]

Consequently,

\[
Q_\pm(\varepsilon,\mathbf u)=O_N(\varepsilon^4)
\]

as jointly analytic functions, and their edge derivatives are also \(O_N(\varepsilon^4)\) in dimensionless \(u_e\) coordinates.

Each block has one eigenvalue near \(1/2\) and one small eigenvalue \(\lambda_\pm\) near zero. The large/small eigenvalue separation at \(\varepsilon=0\) is nonzero, so both eigenvalue branches are jointly analytic. The exact \(2\times2\) eigenvalue formula, or the identity \(\lambda_-\lambda_+=\det M_\pm\), shows

\[
\lambda_\pm(\varepsilon,\mathbf u)
=\varepsilon^4a_\pm(\mathbf u)+O_N(\varepsilon^6),
\]

with analytic coefficient functions \(a_\pm\). In particular,

\[
\partial_{u_e}\lambda_\pm(\varepsilon,\mathbf0)
=O_N(\varepsilon^4).
\]

The absence of odd powers follows from the unitary equivalence \(H(\varepsilon,\mathbf u)\sim H(-\varepsilon,\mathbf u)\), implemented by \(\prod_i\sigma_i^z\).

## 4. Treating both small eigenvalue branches in the entropy derivative

At the uniform point, permutation symmetry gives:

- One small branch is strictly positive to fourth order:
  \[
  \lambda_+(\varepsilon,\mathbf0)
  =c_N\varepsilon^4+O_N(\varepsilon^6),
  \qquad c_N>0,
  \]
  where \(c_4=1/648\), and \(c_N=1/[8(N-2)(N-1)^4]\) for \(N\ge5\).
- The other branch is exactly zero for every \(\varepsilon\) on the uniform path, because the two-site reduced state has no antisymmetric singlet support:
  \[
  \lambda_-(\varepsilon,\mathbf0)=0.
  \]

For the positive branch, continuity of \(a_+\) gives a neighborhood in which \(a_+(\mathbf u)\ge c_N/2\). Hence, for sufficiently small \(\varepsilon>0\),

\[
c'_N\varepsilon^4
\le\lambda_+(\varepsilon,\mathbf u)
\le C_N\varepsilon^4,
\qquad
\partial_{u_e}\lambda_+(\varepsilon,\mathbf0)
=O_N(\varepsilon^4).
\]

Therefore

\[
\left.
\partial_{u_e}\bigl[-\lambda_+\ln\lambda_+\bigr]
\right|_{\mathbf u=0}
=O_N\!\left(\varepsilon^4(1+|\ln\varepsilon|)\right).
\]

The zero branch requires a different argument; the positive-branch lower bound must not be applied to it. Apply the reusable analytic nonnegative-eigenvalue entropy derivative lemma in audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md. For fixed \(\varepsilon>0\), \(\lambda_-(\varepsilon,\mathbf u)\) is a nonnegative analytic eigenvalue for real \(\mathbf u\), and it attains the value zero at the interior point \(\mathbf u=0\). Thus every first directional derivative vanishes there. Along any edge direction \(u=t v\), analyticity and nonnegativity imply

\[
\lambda_-(\varepsilon,tv)=O_{\varepsilon,v}(t^2).
\]

It follows that

\[
-\lambda_-(\varepsilon,tv)
\ln\lambda_-(\varepsilon,tv)
=O_{\varepsilon,v}(t^2|\ln|t||),
\]

so the directional derivative of this entropy contribution at \(t=0\) exists and equals zero.

The two large eigenvalues \(\nu_1,\nu_2\) of \(\rho_{12}\) satisfy

\[
\nu_j=\frac12+O_N(\varepsilon^2),
\qquad
\partial_{u_e}\nu_j=O_N(\varepsilon^2).
\]

Trace one gives

\[
\partial_{u_e}(\nu_1+\nu_2)
=-\partial_{u_e}(\lambda_++\lambda_-)
=O_N(\varepsilon^4)
\]

at the uniform point. Expanding \(-t\ln t\) around \(1/2\), the constant first derivative multiplies this \(O(\varepsilon^4)\) sum, and the remaining terms are also \(O(\varepsilon^4)\). Combining the large and small branches yields

\[
\left.
\partial_{u_e}S(\rho_{12})
\right|_{\mathbf u=0}
=O_N\!\left(\varepsilon^4(1+|\ln\varepsilon|)\right).
\]

Since \(\partial_{J_e}=J^{-1}\partial_{u_e}\) at the uniform point,

\[
\left.
\partial_{J_e}S(\rho_{12})
\right|_{\mathbf J=J\mathbf1}
=O_N\!\left(
\frac{\varepsilon^4}{J}(1+|\ln\varepsilon|)
\right).
\]

This is the model-specific edge-derivative estimate that the earlier entropy–Schur lemma had assumed rather than proved.

## 5. Leading one-site response

Let

\[
R_i=\sum_{j\ne i}J_{ij},
\qquad b_i=\frac{h}{2R_i}.
\]

The leading one-site entropy correction is

\[
-2b_i^2=-\frac{h^2}{2R_i^2}.
\]

Its edge derivative is

\[
\partial_{J_e}(-2b_i^2)
=
\begin{cases}
\displaystyle \frac{h^2}{R_i^3},&e\text{ is incident to }i,\\[2mm]
0,&e\text{ is disjoint from }i.
\end{cases}
\]

The derivative of the higher-order one-site entropy remainder is \(O_N(\varepsilon^4/J)\).

At the uniform point \(R_1=R_2=(N-1)J\). The edge \(J_{13}\) is incident to site 1 but not site 2; the edge \(J_{34}\) is disjoint from both observed sites. Therefore

\[
\partial_{J_{13}}\{S(\rho_1)+S(\rho_2)\}
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(\frac{\varepsilon^4}{J}\right),
\]

whereas

\[
\partial_{J_{34}}\{S(\rho_1)+S(\rho_2)\}
=O_N\!\left(\frac{\varepsilon^4}{J}\right).
\]

## 6. Full response subtraction

Recall

\[
I_{12}=S(\rho_1)+S(\rho_2)-S(\rho_{12}),
\]

\[
B=\partial_{J_{13}}I_{12},
\qquad
C=\partial_{J_{34}}I_{12}.
\]

Combining the one-site leading terms with the two-site entropy derivative estimate gives

\[
\boxed{
B-C
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(
\frac{h^4}{J^5}
\left[1+\left|\ln(h/J)\right|\right]
\right).
}
\]

Equivalently, with \(\varepsilon=h/J\),

\[
B-C
=\frac{\varepsilon^2}{J(N-1)^3}
+O_N\!\left(
\frac{\varepsilon^4}{J}(1+|\ln\varepsilon|)
\right).
\]

Since \(\varepsilon^2(1+|\ln\varepsilon|)\to0\), the positive leading term dominates. Thus for each fixed finite \(N\ge4\), there exists \(\varepsilon_N>0\) such that

\[
0<h/J<\varepsilon_N
\quad\Longrightarrow\quad B-C>0
\]

at the permutation-symmetric point.

## 7. Remaining proof-review obligations

This derivation is a candidate proof and must be independently audited before status promotion. In particular:

1. Check every coefficient and normalization factor in the first-order reduced-block entries \(L_\pm,X_\pm,S_\pm\).
2. Verify that the joint analytic remainder bounds and their first edge derivatives follow from the chosen compact positive-coupling neighborhood.
3. Verify the analytic labeling of both small eigenvalue branches in the two parity blocks.
4. Review the zero-branch entropy directional derivative carefully for arbitrary edge directions.
5. Check the exact fourth-order positive coefficient \(c_N\), including the exceptional \(N=4\) value.
6. Confirm the dimensional conversion \(\partial_{J_e}=J^{-1}\partial_{u_e}\) and all remainder powers.
7. Independently reproduce the leading response coefficient by a second derivation or exact small-N perturbation.
8. Only after the analytic audit, formalize the stable statement in Lean and audit correspondence to the source claim.

**No claim status is upgraded by this working document. No upstream Absolute Symmetry file is modified.**
