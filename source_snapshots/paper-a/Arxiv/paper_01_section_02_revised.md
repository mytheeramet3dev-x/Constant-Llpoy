# Section 2 — Model and Self-Consistency Formulation (Revised)

## 2.1 The all-to-all transverse-field Ising model

We consider an \(N\)-qubit quantum many-body system with pairwise interactions represented initially by the complete graph \(K_N\). The Hamiltonian is

\[
H[\mathbf J]
=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z
-h\sum_{i=1}^{N}\sigma_i^x,
\qquad h>0,
\]

where \(\sigma_i^\alpha\) are Pauli operators acting on site \(i\), and \(\mathbf J=\{J_{ij}\}_{i<j}\) is the edge-coupling configuration. The reference model takes \(J_{ij}\ge0\), although response derivatives are evaluated in the ambient real edge space around a symmetric point.

For finite \(N\) and \(h>0\), the ground state is nondegenerate. This follows from Perron–Frobenius theory after shifting the Hamiltonian by a sufficiently large multiple of the identity: the resulting matrix is nonnegative and irreducible in the computational \(\sigma^z\) basis.

## 2.2 Self-consistency and the symmetric fixed point

The interaction weights are generated from the ground-state quantum mutual information:

\[
J_{ij}=g\,I_{ij}[\Psi_0(\mathbf J)],
\qquad g>0,
\]

where \(\Psi_0(\mathbf J)\) is the ground state of \(H[\mathbf J]\), and

\[
I_{ij}=S(\rho_i)+S(\rho_j)-S(\rho_{ij}).
\]

We use natural logarithms throughout:

\[
S(\rho)=-\operatorname{Tr}(\rho\ln\rho).
\]

Using \(\log_2\) instead would only rescale all mutual informations and the corresponding feedback parameter \(g\); the convention must remain fixed between the analysis and numerical implementation.

The reduced density matrices are

\[
\rho_i=\operatorname{Tr}_{\{1,\ldots,N\}\setminus\{i\}}
|\Psi_0\rangle\langle\Psi_0|,
\]

and

\[
\rho_{ij}=\operatorname{Tr}_{\{1,\ldots,N\}\setminus\{i,j\}}
|\Psi_0\rangle\langle\Psi_0|.
\]

The complete graph and the Hamiltonian are invariant under the permutation group \(S_N\). At a permutation-symmetric configuration,

\[
J_{ij}=J,
\qquad i<j,
\]

all one-site reduced states are equivalent and all distinct two-site reduced states are equivalent. The matrix self-consistency equation therefore reduces to

\[
J=gI_{12}(J,h).
\]

We reserve \(J_*\) for a particular fixed-point solution and use \(J\) as the variable when discussing the full solution curve.

## 2.3 Dimensional scaling

Define the dimensionless coupling

\[
x=\frac Jh,
\qquad h>0.
\]

At the symmetric point,

\[
H(J,h)
=h\left[
-x\sum_{i<j}\sigma_i^z\sigma_j^z
-\sum_i\sigma_i^x
\right]
\equiv h\widetilde H(x,1).
\]

This is a positive energy rescaling, not a unitary scale transformation. Multiplication by the positive scalar \(h\) leaves the spectral projectors unchanged. Thus, for a nondegenerate ground state,

\[
|\Psi_0(J,h)\rangle
=e^{i\theta(J,h)}|\widetilde\Psi_0(x)\rangle,
\]

for some irrelevant phase \(\theta\). Equivalently, the ground-state projectors are identical:

\[
|\Psi_0(J,h)\rangle\langle\Psi_0(J,h)|
=|\widetilde\Psi_0(x)\rangle\langle\widetilde\Psi_0(x)|.
\]

Consequently,

\[
I_{12}(J,h)=\mathcal G_N(x),
\]

where \(\mathcal G_N\) is dimensionless. For \(x>0\), smoothness or analyticity additionally requires the relevant reduced density matrices to remain in a fixed-rank regularity region. At \(x=0\), the function is continuous with \(\mathcal G_N(0)=0\), but entropy derivatives require separate care because the product-state reduced density matrices have zero eigenvalues.

## 2.4 Dimensionless fixed-point equation

Substituting \(J=hx\) and \(I_{12}=\mathcal G_N(x)\) into the self-consistency equation gives

\[
hx=g\mathcal G_N(x).
\]

Introduce the dimensionless feedback parameter

\[
\eta=\frac gh.
\]

The dimensionless fixed-point function is

\[
f(x;\eta)=\eta\mathcal G_N(x)-x.
\]

Nontrivial fixed points satisfy

\[
f(x;\eta)=0,
\qquad x>0,
\]

or equivalently

\[
\frac{x}{\mathcal G_N(x)}=\eta,
\]

where \(\mathcal G_N(x)>0\).

At \(x=0\), the ground state is the separable transverse-field product state

\[
|\widetilde\Psi_0(0)\rangle
=\bigotimes_{i=1}^{N}|+x\rangle_i,
\]

and therefore \(\mathcal G_N(0)=0\). Hence \(x=0\) is the trivial fixed point for every \(g,h>0\).

Nontrivial roots correspond to self-consistent configurations with nonzero edge weights. Their existence and number are determined by the intersections of \(\mathcal G_N(x)\) with the line \(x/\eta\), subject to the global shape of \(\mathcal G_N\).

## 2.5 Critical threshold

Define the system-size-dependent threshold scaling coefficient by

\[
\alpha_N
\equiv
\inf_{x>0}\frac{x}{\mathcal G_N(x)}.
\]

If the infimum is attained at an interior point \(x_c>0\), then

\[
\eta_c=\alpha_N,
\qquad
g_c(h)=\alpha_Nh.
\]

At an interior differentiable minimizer,

\[
\frac{d}{dx}\left(\frac{x}{\mathcal G_N(x)}\right)_{x=x_c}=0,
\]

which is equivalent to

\[
\mathcal G_N(x_c)=x_c\mathcal G_N'(x_c).
\]

Equivalently, the tangent conditions for \(f\) are

\[
f(x_c;\alpha_N)=0,
\qquad
\partial_xf(x_c;\alpha_N)=0.
\]

The statement that subcritical parameters have no nontrivial roots follows directly from the definition of the infimum:

\[
\eta<\alpha_N
\quad\Longrightarrow\quad
f(x;\eta)<0
\quad\text{for all }x>0,
\]

provided \(\mathcal G_N(x)>0\) on the domain considered. The existence of roots for every \(\eta>\alpha_N\), and the claim that there are exactly two roots globally, require additional assumptions on continuity, endpoint behavior, and the global shape of \(x/\mathcal G_N(x)\). The saddle-node theorem used later is local and requires a nondegenerate interior minimum.
