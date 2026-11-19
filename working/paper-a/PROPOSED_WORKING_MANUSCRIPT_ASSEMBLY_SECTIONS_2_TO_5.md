# Paper A — Proposed Working Manuscript Assembly (Sections 2–5)

**Status: PROPOSED / SOURCE-PRESERVING ASSEMBLY / NOT VERIFIED / NOT FOR SUBMISSION**

Frozen upstream: `mytheeramet3dev-x/Absolute_Sym`  
Frozen branch: `paper-a-interval-audit-2026-11-14`  
Frozen commit: `8deb7de4a49cb2060720246b7101820ee7e08c91`

## Reading rule

The four source sections below are reproduced verbatim from the frozen commit to preserve exact provenance. They are followed by an **authoritative proposed correction overlay**. Where the overlay conflicts with frozen prose, the overlay records the proposed disposition; the old prose is retained only as immutable source history and must not be read as simultaneously accepted. This is a working/audit artifact, not a clean publication-ready manuscript. No upstream file is modified.

## Frozen source: Arxiv/paper_01_section_02_revised.md

- Blob SHA: `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`

# Section 2 — Model and Self-Consistency Formulation (Revised)

## 2.1 The all-to-all transverse-field Ising model

We consider an \(N\)-qubit quantum many-body system with pairwise interactions represented initially by the complete graph \(K_N\). The Hamiltonian is

\[
H[\mathbf J]
=-
\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z
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


---

## Frozen source: Arxiv/paper_01_section_03_revised.md

- Blob SHA: `9ac164ac67cc121af212c4fb7268b809d9234bd6`

# Section 3 — Saddle-Node Bifurcation Theorem (Revised)

## 3.1 Critical point and tangent constraint

For fixed \(h>0\), define the dimensional fixed-point function

\[
F(x,g,h)=g\mathcal G_N(x)-hx,
\qquad x=J/h.
\]

It is convenient to divide by the positive scale \(h\) and work with

\[
f(x;\eta)=\eta\mathcal G_N(x)-x,
\qquad
\eta=\frac gh.
\]

The two functions have the same roots and

\[
F=h f.
\]

### Definition 1 — Interior critical point

For a fixed \(h>0\), an interior critical point \((x_c,g_c)\), with \(x_c>0\), satisfies

\[
F(x_c,g_c,h)=0,
\qquad
\partial_xF(x_c,g_c,h)=0.
\]

Equivalently,

\[
f(x_c;\eta_c)=0,
\qquad
\partial_xf(x_c;\eta_c)=0,
\qquad
\eta_c=\frac{g_c}{h}.
\]

### Proposition 1 — Tangent constraint

At an interior critical point,

\[
\boxed{
\mathcal G_N'(x_c)
=\frac{\mathcal G_N(x_c)}{x_c}
=\frac{h}{g_c}
}
\]

If the threshold has the exact scaling \(g_c(h)=\alpha_Nh\), then

\[
\boxed{
\mathcal G_N'(x_c)
=\frac{\mathcal G_N(x_c)}{x_c}
=\frac1{\alpha_N}
}
\]

### Proof

The derivative condition gives

\[
\partial_xF=g_c\mathcal G_N'(x_c)-h=0,
\]

so

\[
\mathcal G_N'(x_c)=\frac h{g_c}.
\]

The fixed-point condition gives

\[
g_c\mathcal G_N(x_c)=hx_c,
\]

and hence

\[
\frac{\mathcal G_N(x_c)}{x_c}=\frac h{g_c}.
\]

Combining the two equations proves the result

## 3.2 Local normal form

Assume that \(\mathcal G_N\) is at least \(C^2\) near \(x_c\). Let

\[
\delta x=x-x_c,
\qquad
\delta g=g-g_c.
\]

Taylor expansion at fixed \(h\) gives

\[
F(x,g,h)
=F_c+F_g\delta g+F_x\delta x
+\frac12F_{xx}\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

At the critical point,

\[
F_c=0,
\qquad F_x=0,
\qquad F_g=\mathcal G_N(x_c)>0,
\qquad F_{xx}=g_c\mathcal G_N''(x_c).
\]

Therefore,

\[
F(x,g,h)
=\mathcal G_N(x_c)\delta g
+\frac12g_c\mathcal G_N''(x_c)\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

### Assumption 1 — Generic nondegeneracy

Assume

\[
\mathcal G_N''(x_c)\neq0.
\]

If \(x_c\) is an interior minimizer of \(x/\mathcal G_N(x)\), then

\[
\mathcal G_N''(x_c)<0
\]

is equivalent to strict nondegeneracy of that minimum

Solving the leading normal form gives

\[
\boxed{
x_\pm-x_c
=\pm
\sqrt{
\frac{2\mathcal G_N(x_c)}{g_c|\mathcal G_N''(x_c)|}
}
\sqrt{g-g_c}
+O(g-g_c)
}
\]

on the side \(g>g_c\) when \(\mathcal G_N''(x_c)<0\)

This is a **local conditional saddle-node theorem**. The condition \(\mathcal G_N''(x_c)<0\) is not established by the numerical scans currently documented and must not be labelled numerically verified without a dedicated curvature audit

## 3.3 Local branch orientation and iteration stability

The derivative with respect to \(x\) is

\[
F_x(x,g,h)=g\mathcal G_N'(x)-h.
\]

Near the two branches:

\[
F_x(x_\pm,g,h)
=g_c\mathcal G_N''(x_c)(x_\pm-x_c)+O(g-g_c).
\]

If \(\mathcal G_N''(x_c)<0\), then

\[
F_x(x_-)>0,
\qquad
F_x(x_+)<0.
\]

This determines the local orientation of the two branches

### Picard iteration

The dimensionless fixed-point iteration is

\[
x^{(k+1)}=T(x^{(k)}),
\qquad
T(x)=\frac gh\mathcal G_N(x).
\]

At a fixed point,

\[
T'(x_*)=\frac gh\mathcal G_N'(x_*)
=1+\frac1hF_x(x_*,g,h).
\]

The exact linear stability condition for this iteration is

\[
\boxed{|T'(x_*)|<1}
\]

or equivalently

\[
\boxed{-2h<F_x(x_*,g,h)<0.}
\]

Near a generic saddle-node, \(F_x\) is small, so the branch with \(F_x<0\) has \(0<T'<1\) and is locally attracting, while the branch with \(F_x>0\) has \(T'>1\) and is locally repelling

Away from the bifurcation, the condition \(F_x<0\) alone is not sufficient: if \(F_x\le-2h\), the Picard multiplier has magnitude at least one

The term “physical branch” will therefore mean the branch selected by the documented continuation/iteration prescription, while “Picard stable” requires the full inequality \(|T'|<1\)

## 3.4 Local versus global statements

The local normal form establishes two nearby roots on the supercritical side under Assumption 1. It does not by itself prove that:

- there are exactly two roots globally
- no additional roots exist outside the local neighborhood
- the subcritical regime has no nontrivial root unless \(g_c\) is defined as the global infimum threshold

Those global claims require a separate analysis of

\[
q(x)=\frac{x}{\mathcal G_N(x)}
\]

including its endpoint behavior and all interior extrema

## 3.5 Status

- Tangent constraint: exact
- Local square-root normal form: exact under \(C^2\) and nondegeneracy assumptions
- \(F_g>0\) at a nontrivial point: exact
- \(\mathcal G_N''(x_c)<0\): open model-specific condition
- Two roots globally: not established by this local theorem
- \(F_x<0\) as a universal stability criterion: false; the exact Picard condition is \(|1+F_x/h|<1\)


---

## Frozen source: Arxiv/paper_01_section_04_revised.md

- Blob SHA: `a7570431eac62dd4555194df283edb5a9c87a28d`

# Section 4 — Dynamic Scaling from Hamiltonian Homogeneity

## 4.1 Dynamic scaling parameterization

The positive energy-rescaling structure of the all-to-all TFIM implies that the natural dimensionless control parameter is
\[
\eta = \frac{g}{h}.
\]
When the threshold is attained at an interior point and obeys
\[
g_c(h) = \alpha_N h,
\]
we may parameterize a corresponding supercritical ray by
\[
g(\gamma,h) = \gamma g_c(h) = \gamma \alpha_N h,
\qquad \gamma > 1.
\]
This keeps \(\eta = \gamma \alpha_N\) fixed while \(h\) varies. It is a scaling-homogeneity construction, not a unitary invariance, and not, by itself, evidence for a thermodynamic phase transition.

## 4.2 Independence of dimensionless fixed points

The nontrivial fixed-point equation is
\[
f(x; \eta) = \eta \mathcal G_N(x) - x = 0.
\]
Along the ray \(g = \gamma \alpha_N h\), it becomes
\[
x = \gamma \alpha_N \mathcal G_N(x).
\]
Therefore, every corresponding root \(x_*(\gamma)\), whenever it exists, is independent of the absolute scale \(h\):
\[
\frac{\partial x_*}{\partial h} = 0.
\]
This statement holds root-by-root. It does not assert global uniqueness, nor does it select a branch without an explicit continuation or iteration prescription.

## 4.3 Picard multiplier and fixed-point derivatives

Let
\[
T(x) = \eta \mathcal G_N(x)
\]
be the dimensionless Picard map. Its multiplier is
\[
T'(x_*) = \eta \mathcal G_N'(x_*).
\]
The derivative of the dimensionless fixed-point function is
\[
\partial_x f(x_*; \eta) = \eta \mathcal G_N'(x_*) - 1 = T'(x_*) - 1.
\]

In dimensional variables, with the fixed-point function
\[
F(J, g, h) = g \mathcal G_N(J/h) - J,
\]
its derivative with respect to the physical coupling \(J\) is denoted by \(F_J\):
\[
F_J \equiv \frac{\partial F}{\partial J} = \frac{g}{h} \mathcal G_N'(J/h) - 1 = \eta \mathcal G_N'(x) - 1.
\]

Thus, under \(g = \gamma \alpha_N h\), we obtain the scale-invariant relations:
\[
\boxed{ F_J\big|_{J_*} = \gamma \alpha_N \mathcal G_N'(x_*) - 1 }
\]
and
\[
\boxed{ T'(x_*) = \gamma \alpha_N \mathcal G_N'(x_*) = F_J\big|_{J_*} + 1 }.
\]
Both quantities depend on \(h\) only through the dimensionless branch coordinate \(x_*(\gamma)\). At a tangent point \(x_c\):
\[
T'(x_c) = 1,
\qquad
F_J\big|_{J_c} = 0.
\]
The exact scalar Picard-attractivity condition for the iteration \(x_{k+1} = T(x_k)\) is:
\[
|T'(x_*)| < 1
\quad \Longleftrightarrow \quad
-2 < F_J\big|_{J_*} < 0.
\]

## 4.4 Asymptotic regimes

### 4.4.1 Near-critical regime

For the upper local branch supplied by the nondegenerate saddle-node theorem,
\[
\lim_{\gamma \to 1^+} x_*(\gamma) = x_c.
\]
Consequently,
\[
\lim_{\gamma \to 1^+} T'(x_*) = 1,
\qquad
\lim_{\gamma \to 1^+} F_J\big|_{J_*} = 0.
\]
The first limit corresponds to the marginality of the Picard map; the second is the tangent condition for the fixed-point function.

### 4.4.2 Large-\(\gamma\) regime (Strong coupling)

Assuming the selected upper branch admits a global continuation devoid of turning points or branch exchanges, \(\mathcal G_N(x)\) approaches a positive finite limit as \(x \to \infty\). The equation
\[
x = \gamma \alpha_N \mathcal G_N(x)
\]
then implies \(x_*(\gamma) \to \infty\) as \(\gamma \to \infty\). For \(N \ge 4\) and \(h > 0\), the unperturbed limiting Ising Hamiltonian has a two-dimensional ferromagnetic ground space. The transverse field selects the unique, parity-even cat state.

By applying Schrieffer–Wolff degenerate perturbation theory to the parity-even sector (see Lemma 5.1), we obtain the rigorous asymptotic expansion for the dimensionless mutual information:
\[
\mathcal G_N(x) = \ln 2 - \frac{1}{(N-1)^2 x^2} + O\left(\frac{\ln x}{x^4}\right) \qquad (x \to \infty).
\]
This proves that the endpoint limit is attained as:
\[
\lim_{x \to \infty} \mathcal G_N(x) = \ln 2.
\]
Furthermore, the analytic control of the entropy remainder near the degenerate subspace guarantees that the derivative follows the leading algebraic order:
\[
\mathcal G_N'(x) = \frac{2}{(N-1)^2 x^3} + O\left(\frac{\ln x}{x^5}\right).
\]
This rigorously establishes that
\[
\lim_{x \to \infty} \mathcal G_N'(x) = 0.
\]
Consequently, on the physical stable branch at large \(\gamma\), the multiplier and the fixed-point derivative satisfy:
\[
\lim_{\gamma \to \infty} T'(x_*(\gamma)) = 0,
\qquad
\lim_{\gamma \to \infty} F_J\big|_{J_*(\gamma)} = -1.
\]

### 4.4.3 Branch-domain qualification

The inequality
\[
x_*(\gamma) \ge x_c
\]
holds for the upper local branch near \(\gamma = 1\). Extending it to every \(\gamma \ge 1\) requires a **global continuation assumption** asserting the absence of intermediate reversing turning points or branch exchanges. In contrast, the lower interval \(0 < x < x_c\) forms the locally unstable branch near the saddle-node. A weak-coupling perturbative expansion (\(x \to 0\), Lemma 5.2) further confirms that this lower branch possesses distinct scaling and opposite-sign response characteristics compared to the physical stable branch.

---

## Frozen source: Arxiv/paper_01_section_05_revised.md

- Blob SHA: `671c97fa68fa48c929760bf9956d197b358c4904`

# Section 5: Physical Discussion and Connection to Paper 2

## 5.1 Mathematical meaning of the branch condition

For the scalar self-consistency equation

\[
F(J;g,h)=gI_{12}(J,h)-J,
\]

the derivative at a fixed point is

\[
F_J(J_*)=g\left.\frac{\partial I_{12}}{\partial J}\right|_{J_*}-1.
\]

Therefore, the branch condition (F_J(J_*)<0) is equivalent to

\[
\left.\frac{\partial I_{12}}{\partial J}\right|_{J_*}<\frac1g.
\]

This is an exact upper bound on the response to a uniform change of all edge couplings. It does **not** determine the sign of that response. In particular, (F_J<0) does not imply
\(\partial I_{12}/\partial J<0\); negativity would require the stronger condition (F_J<-1).

Let
\[
T(J)=gI_{12}(J,h)
\]
be the scalar Picard map. Since (T'(J_*)=1+F_J(J_*)), the exact local Picard-attractivity condition is

\[
|T'(J_*)|<1
\quad\Longleftrightarrow\quad
-2<F_J(J_*)<0.
\]

Thus (F_J<0) identifies the descending side of the fixed-point curve and is sufficient for the usual saddle-node branch classification, but by itself is not the complete discrete-iteration stability criterion.

For the present model, positivity of the uniform response has been observed numerically on the investigated physical branches for (N=4,6,8,10,20). This remains a numerical observation, not an analytic theorem. The (N=50) data near (x_c) are excluded from this statement because the computed spectral gap is below the reliability threshold.

## 5.2 Representation-theoretic decomposition of edge perturbations

At the permutation-symmetric point (J_{ij}=J_*), an infinitesimal edge perturbation belongs to
\[
\mathcal V_{\mathrm{edge}}\cong\mathbb R^{\binom N2}.
\]
As an (S_N)-representation, this space decomposes as

\[
\mathcal V_{\mathrm{edge}}=\mathcal V_0\oplus\mathcal V_1\oplus\mathcal V_2,
\]

with
\[
\dim\mathcal V_0=1,\qquad
\dim\mathcal V_1=N-1,\qquad
\dim\mathcal V_2=\frac{N(N-3)}2.
\]

Here (mathcal V_0) is the uniform edge direction, (mathcal V_1) is the degree-heterogeneous (standard-representation) sector, and (mathcal V_2) is the residual degree-preserving sector. The last sector is a natural place to look for distributed, geometry-like perturbations, although representation labels alone do not establish the emergence of a lattice or finite-dimensional geometry.

Define the three derivatives

\[
A=\frac{\partial I_{12}}{\partial J_{12}},\qquad
B=\frac{\partial I_{12}}{\partial J_{13}},\qquad
C=\frac{\partial I_{12}}{\partial J_{34}},
\]

where (J_{13}) shares one endpoint with the observed edge and (J_{34}) is disjoint from it. (S_N) symmetry implies that the response matrix is determined by these three numbers. Its sector eigenvalues are

\[
\chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C,
\]
\[
\chi_1=A+(N-4)B-(N-3)C,
\]
\[
\chi_2=A-2B+C.
\]

The uniform eigenvalue, obtained by varying every edge simultaneously, satisfies
\[
\chi_0=\frac{\partial I_{12}}{\partial J_*},
\]
and direct subtraction gives the exact identity

\[
\boxed{\chi_1-\chi_2=(N-2)(B-C)}.
\]

This identity is exact at the symmetric point and does not require a numerical approximation.

## 5.3 Status of the (B-C) statement

The sign of (B-C) determines the ordering of the two nontrivial response sectors:

\[
B-C>0\iff\chi_1>\chi_2.
\]

For the feedback map (mathbf J\mapsto g\mathbf I(\mathbf J)), the corresponding linearized eigenvalues are (g\chi_k). Consequently, the statement that one sector is more strongly amplified than another requires comparison of (g\chi_1) and (g\chi_2), together with their signs and the chosen stability convention. The inequality (B-C>0) alone is a response-ordering statement; it is not by itself a proof that a hub mode is dynamically unstable or that a geometric mode is dynamically suppressed.

The current evidence is:

- reduced-solver validation agrees with dense exact diagonalization at small (N);
- near-(x_c) scans give (B-C>0) for (N=4,6,8,10);
- finite-size data are positive for (N=4,6,8,10,20);
- the (h)-scan at (N=8) is positive over the tested range (h=0.5,1.0,\ldots,3.5);
- (N=50) near (x_c) is excluded because the spectral gap is below the reliability threshold.

Accordingly, (B-C>0) should be labelled a **strong numerically supported conjecture**, not an exact theorem. The algebraic proof remains open. The principal barrier is that the perturbations associated with the different edge sectors couple to different excited-state/resolvent channels, while the von Neumann entropy derivative contains noncommuting Fréchet terms. Permutation symmetry fixes the sector decomposition but does not impose an ordering between the resulting reduced matrix elements.

## 5.4 Connection to Paper 2

The results of this paper provide constraints and definitions for the symmetry-breaking analysis in Paper 2.

1. **Branch restriction.** The locally relevant physical branch is the branch emerging on the (x>x_c) side of the nondegenerate tangent point. Statements extending this branch to all (gamma\ge1) require a separate global-continuation argument and should not be inferred from the local saddle-node theorem alone.

2. **Uniform-response bound.** On any fixed point satisfying (F_J<0),
\[
\chi_0=\left.\frac{\partial I_{12}}{\partial J_*}\right|_{J_*}<\frac1g.
\]
Under (g=\gamma\alpha_Nh), this bound scales as (1/h), while the dimensionless response (h\chi_0) depends only on (x).

3. **Scale covariance of perturbations.** Since the ground state depends on (J,h) through (x=J/h), response eigenvalues have the dimensional scaling
\[
\chi_k(J,h)=h^{-1}\,\widetilde\chi_k(x).
\]
Thus the ordering of the sectors is independent of the overall energy scale (h), but the dimensional eigenvalues themselves are not strictly invariant under changing (h). The same qualification applies to the feedback eigenvalues (g\chi_k), which depend on the dimensionless ratio (g/h).

These results establish the precise interface between Paper 1 and Paper 2: Paper 1 supplies the symmetric branch, its local bifurcation structure, and the exact sector identity; Paper 2 must determine whether the unresolved ordering (\chi_1\gtreqless\chi_2) can be proved or whether additional model structure is required.



---

# Proposed Correction Overlay — Read with the Source Sections

## O-01 / MCR-01 — Perron–Frobenius shift

Replace the §2.1 claim that adding a large multiple of the identity to (H) makes it nonnegative. With the stated sign convention define (K=cI-H), choosing (c) so (c-H_{ss}\ge0) for every computational basis state. Single-spin-flip off-diagonal entries of (K) are (+h>0); its positive-entry graph is the connected Boolean hypercube. Thus (K) is nonnegative and irreducible, and its simple largest eigenvalue corresponds to the smallest eigenvalue of (H). This is a finite-(N), (h>0) argument only. Lean correspondence, exact declaration matching, and independent review remain open.

## O-02 / MCR-02 — Saddle-node regularity

Withdraw the frozen §3.2 cubic Taylor remainder (O(|\delta x|^3)) and branch remainder (O(g-g_c)) under the stated (C^2) hypothesis. A general (C^2) function only gives a Peano remainder (o(|\delta x|^2)) after the quadratic Taylor polynomial. Do not assert the quantitative branch formula as proved. The local root-count theorem remains open until a complete proof supplies neighborhood quantifiers, critical-value control, endpoint signs, local root counting, and sufficient regularity. The model-specific conditions (F_g>0) and (F_{xx}<0) also remain to be verified.

## O-03 / MCR-03 — Weak-coupling response sign

The original negative-sign derivation for (B-C) is superseded: it omitted the order-(r^2) coherence (\rho_{-+,+-}=\sum_{k\ge3}a_{1k}a_{2k}). The corrected candidate asymptotic recorded in the internal audit is
\[
B-C=\frac{J}{8h^2}\ln\!\left(\frac{2(N-2)}{N-1}\right)
+O_N\!\left(\frac{J^2}{h^3}[1+|\ln(J/h)|]\right),
\qquad J/h\to0^+,
\]
for each fixed finite (N\ge4). Its leading coefficient is positive. However, the model-specific differentiated remainder is not fully Lean-proved and the derivation has not received independent external review. Treat the result as provisional local analytic evidence only. It does not prove global positivity, intermediate-coupling behavior, uniform-in-(N) behavior, or a global branch theorem. Remove “opposite-sign response characteristics” if it refers to (B-C).

## O-04 / MCR-04 — Edge-space domain

The dimensions (1,N-1,N(N-3)/2) apply for (N\ge3); at (N=3) the residual sector is zero-dimensional. If all three sectors are intended to be nonzero, state (N\ge4). The §5.2 source passage still needs this explicit qualification.

## O-05 / MCR-05 — Strong-coupling citation and estimates

The frozen §4.4.2 citation to Lemma 5.1 is incorrect for the stated (\mathcal G_N(x)) strong-coupling expansion. Remove that citation. Candidate fixed-finite-(N) estimates recorded in separate Constant Llpoy artifacts are
\[
\mathcal G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}+O_N(\ln x/x^4),
\]
and
\[
\mathcal G_N'(x)=\frac{2}{(N-1)^2x^3}+O_N(\ln x/x^5).
\]
The derivative estimate is a separate proof obligation and must not be inferred by differentiating a function-level big-O estimate. Until the derivation is placed in a manuscript appendix and independently reviewed, retain both estimates as provisional audit-backed claims, not accepted manuscript theorems. No uniform-in-(N) result is asserted.

## O-06 / MCR-06 — Threshold and root counts

Keep (\alpha_N=\inf_{x>0}x/\mathcal G_N(x)) distinct from an attained minimum. Subcritical exclusion follows from the infimum definition when (\mathcal G_N(x)>0). An interior tangent point exists only if the infimum is attained at an interior point and the required differentiability holds. A nondegenerate tangent point requires additional curvature. Existence of roots for every supercritical parameter and exactly two global roots require continuity, endpoint behavior, and global shape hypotheses; they are not consequences of the infimum definition alone.

## O-07 / MCR-07 — Root-set invariance versus branch derivative

Along a fixed dimensionless ray (\eta=g/h), the dimensionless root set is independent of (h). A derivative (\partial_hx_*(h)=0) for a selected root branch additionally requires a differentiable branch selection (for example, a simple root and the implicit-function theorem). At a fold, this argument does not apply.

## O-08 / MCR-08 — Picard stability

For (T(x)=(g/h)\mathcal G_N(x)), (T'=1+F_x/h), so (|T'|<1) iff (-2h<F_x<0). This is a local linear stability condition. (F_x<0) alone is not a global convergence theorem and is not the complete multiplier condition away from the local saddle-node regime.

## O-09 / MCR-09 — Positive scaling

State (h>0) wherever (H(J,h)=h\widetilde H(J/h,1)) is used. The ground-state spectral projector is the phase-independent invariant. Normalized eigenvectors agree only up to phase. Response scaling (\chi=h^{-1}\widetilde\chi) requires differentiability of the reduced-state mutual information in the relevant coordinates; rank-deficient entropy points need separate regularity analysis.

## O-10 / MCR-10 — Zero-coupling endpoint

At (J=0,h>0), the ground state is (\bigotimes_i|+x\rangle_i), and the two-site mutual information is exactly zero. This establishes the trivial endpoint only. It does not establish differentiability or analyticity of entropy at the rank-deficient reduced state, nor any derivative obtained by termwise differentiation.

## O-11 / MCR-11 — Uniform-path derivative

Define the uniform path by varying every edge coupling together. At the symmetric point,
\[
\chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C.
\]
Then (F_J=g\chi_0-1), where (F_J) is the derivative along that uniform path. For (g>0), (F_J<0) gives (\chi_0<1/g), not (\chi_0<0); the latter requires (F_J<-1). Do not confuse this directional derivative with one independent-edge partial.

## O-12 / MCR-12 — Duplicate claim

PROP-0008 duplicates the subcritical exclusion in PROP-0001. Preferred publication disposition: retire the duplicate or relabel it as a corollary, while preserving its claim-registry record and audit traceability. This limited assembly does not renumber it.

## O-13 / MCR-13 — Notation/domain lock

Use (J) for the uniform common coupling and (J_{ij}) for independent edge coordinates; (x=J/h) and (\eta=g/h) only for (h>0); distinguish (F_x) from (F_J); define (A,B,C) before using the sector identity; use (O_N) when constants may depend on fixed (N); state (N)-domains per theorem; and do not infer derivative remainders by differentiating function-level big-O bounds. This is a consistency checklist, not proof that all assumptions hold.

---

## Acceptance and verification gate

- This is a partial assembly of §§2–5 only; the rest of the manuscript, bibliography, appendices, figures, tables, and all cross-references remain unassembled.
- The correction overlay is proposed text/disposition, not an accepted revision.
- Lean build: not run in this assembly step.
- CI: not run in this assembly step.
- Independent review: not run.
- Paper A overall status remains **NOT VERIFIED**.
