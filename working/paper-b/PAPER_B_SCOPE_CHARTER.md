# Paper B Scope Charter

## 0. Identity and governing rule

**Official title:** Equivariant Bifurcation, Isotropy Classification, Representation-Resolved Stability, and Nonlinear Branch Structure in Self-Consistent Quantum Interaction Networks

**Research identity:** a model-specific study of nonlinear equivariant bifurcation and nonuniform self-consistent quantum interaction branches.

This is a **new research scope**. The former Paper B manuscript studied the linear response of the permutation-symmetric solution and the sign question for (B-C). That manuscript is preserved unchanged in `source_snapshots/paper-b/paper_02_manuscript_original.md`. It is not the research plan for the redesigned Paper B.

The title names four intended result families. It does not certify that any of them has been proved. The actual quantum mutual-information feedback map—not an abstract equivariant map alone—is the target object.

---

## 1. Central research question

For the finite-(N) all-to-all transverse-field Ising quantum network whose pairwise couplings are fed back from ground-state pairwise quantum mutual information:

**When, how, and in which symmetry types can the permutation-symmetric self-consistent branch bifurcate into genuinely nonuniform coupling configurations, and what are the local nonlinear structure and stability properties of those branches in the full edge-coupling space?**

The project must establish or refute the existence of at least one nonuniform branch in the actual quantum model. An abstract application of the Equivariant Branching Lemma (EBL) is not sufficient.

---

## 2. Fixed model class

For a fixed finite integer (N\ge 4), let (E_N=\{{i,j}:1\le i<j\le N\}) and (m=|E_N|=\binom N2). Let (\mathbf J=(J_{ij})_{i<j}\in\mathbb R^m). The Hamiltonian is

\[
H_N(\mathbf J;h)
=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z
-h\sum_{i=1}^N\sigma_i^x,\qquad h>0.
\]

For a normalized ground state (\Psi_0(\mathbf J;h)), define

\[
I_{ij}(\mathbf J;h)
=S(\rho_i)+S(\rho_j)-S(\rho_{ij}),
\qquad S(\rho)=-\operatorname{Tr}(\rho\ln\rho).
\]

The feedback equation is

\[
J_{ij}=g I_{ij}(\mathbf J;h),\qquad g>0.
\]

At a permutation-symmetric point, (J_{ij}=J_*>0) for all edges. Since (J_*>0), sufficiently small real perturbations of the edge variables remain in the physical nonnegative-coupling cone. The local analysis may use an open ambient neighborhood in (\mathbb R^m), but every claimed physical branch must be checked to remain in the admissible coupling domain.

Use the dimensionless variables (x_{ij}=J_{ij}/h) and (\eta=g/h) when useful. Define the residual map consistently, for example

\[
\mathcal F(\mathbf x,\eta)=\eta\,\boldsymbol{\mathcal I}_N(\mathbf x)-\mathbf x.
\]

The sign convention for the residual must remain fixed throughout every derivation and formalization.

---

## 3. Symmetry and representation framework

The permutation group (S_N) acts on vertices and induces an orthogonal permutation representation on edge space (\mathbb R^{E_N}). The Hamiltonian, ground-state projector (where the ground state is simple), reduced states, and pairwise mutual-information feedback map must be shown to transform equivariantly under this action.

At the fully symmetric point, the edge representation for (N\ge4) has the multiplicity-free decomposition

\[
\mathbb R^{E_N}=V_0\oplus V_1\oplus V_2,
\]

with dimensions

\[
\dim V_0=1,\qquad
\dim V_1=N-1,\qquad
\dim V_2=\frac{N(N-3)}2.
\]

The conventional interpretations are:
- (V_0): uniform edge perturbations;
- (V_1): degree-changing / degree-heterogeneous perturbations;
- (V_2): degree-preserving residual perturbations.

This decomposition is inherited as setup from Paper A. Paper B must not present it as its principal new theorem. Paper B must use the critical nontrivial representation(s) to derive nonlinear branches, isotropy types, and stability results.

For each candidate isotropy subgroup (H\le S_N), the relevant fixed-point space (\operatorname{Fix}(H)\cap V_k), its dimension, conjugacy class, and admissibility for a one-dimensional EBL branch must be computed explicitly. Do not claim a complete isotropy classification unless the subgroup classes and all relevant fixed-space dimensions have actually been exhausted.

---

## 4. Four principal theorem families

### B-I. Equivariant critical-mode and bifurcation criterion

Along the symmetric branch (\mathbf x_*(\eta)=x_*(\eta)\mathbf 1_E), analyze the derivative of the actual feedback residual. If the derivative exists, its nontrivial-sector eigenvalues are determined by the representation-resolved response operator.

A candidate primary nonuniform bifurcation in sector (V_k), (k\in\{1,2\}), requires a criticality condition of the form

\[
\det\left(D_{\mathbf x}\mathcal F\big|_{V_k}\right)=0,
\]

equivalently a feedback eigenvalue crossing (1) under the convention (\mathcal F=\eta\mathcal I-\mathbf x). The project must establish:
1. the critical parameter and critical symmetric state, or prove none exists in a specified parameter region;
2. the critical representation sector and its multiplicity;
3. transversality of the crossing;
4. invertibility/noncriticality on the complementary space;
5. absence of simultaneous critical sectors, or a separate treatment of the resulting mode interaction.

A response ordering such as (\chi_1>\chi_2) is not by itself a bifurcation theorem.

### B-II. Isotropy classification and nonuniform branch existence

For each verified critical representation, determine the isotropy subgroups that can support local branches. Apply equivariant Lyapunov–Schmidt reduction or an applicable equivariant branching theorem only after verifying all hypotheses for the actual quantum feedback map.

The required model-specific work is:
1. derive the reduced equivariant equation on the critical space;
2. compute the first nonzero nonlinear coefficients from the quantum mutual-information map;
3. prove the required nondegeneracy conditions (or identify their failure);
4. establish at least one actual nonuniform branch with a rigorous local existence theorem;
5. classify the branches covered by the theorem up to the (S_N)-action, without claiming an exhaustive global classification unless proved.

The EBL may identify candidate symmetry types; it does not supply the quantum coefficients, branch direction, or stability automatically.

### B-III. Nonlinear branch structure

Determine the local branch expansions and their parameter dependence near each proved primary bifurcation. At minimum, establish the correct reduced normal form to the first order at which branch existence and multiplicity are decided.

The analysis must distinguish:
- branch existence from branch uniqueness;
- local classification from global continuation;
- a branch in a fixed-point subspace from a branch in the full edge space;
- a symmetry-reduced solution from a physically admissible nonnegative-coupling solution.

Secondary bifurcations, global branch continuation, hysteresis, cycles, and chaotic dynamics are outside the initial scope unless separately authorized by a later scope revision.

### B-IV. Representation-resolved stability

Stability is meaningful only after the update dynamics are specified. The default discrete-time interpretation is the Picard feedback iteration

\[
\mathbf x_{n+1}=T_\eta(\mathbf x_n)
:=\eta\boldsymbol{\mathcal I}_N(\mathbf x_n).
\]

For every branch whose regularity permits linearization:
1. compute or rigorously bound the spectrum of (D T_\eta) at the branch;
2. decompose perturbations according to the branch isotropy subgroup, not merely the full (S_N) decomposition valid at the symmetric point;
3. include all transverse perturbation sectors in the full edge space;
4. prove local asymptotic stability when the spectral radius is strictly below (1), and instability when a multiplier lies strictly outside the unit disk, under the stated differentiability hypotheses;
5. mark unit-modulus and nonhyperbolic cases OPEN unless a higher-order nonlinear stability analysis resolves them.

Do not infer stability from the sign of a response eigenvalue alone. Do not call an algebraic fixed point dynamically stable without naming the update rule.

---

## 5. Mandatory regularity gate: quantum entropy may obstruct standard smooth bifurcation theory

The ground-state projector can be smooth while the von Neumann entropy of a reduced state fails to be (C^2) when eigenvalues reach zero. At a fully permutation-symmetric point, a two-site reduced state may have a symmetry-enforced kernel (for example, an antisymmetric two-qubit component). A symmetry-breaking perturbation may lift a zero eigenvalue, and terms of the form (-\lambda\log\lambda) can produce non-polynomial behavior.

Therefore the project must **not** assume that the mutual-information map is (C^2) or (C^3) merely because the finite-dimensional Hamiltonian has a simple ground state.

Before invoking standard smooth equivariant bifurcation theory, prove the exact regularity needed on:
- the full ambient edge space;
- each candidate critical fixed-point subspace;
- the relevant isotropy-fixed subspaces;
- transverse directions required for full-space stability.

The regularity audit must inspect the ranks and small-eigenvalue asymptotics of (\rho_i) and (\rho_{ij}), including entropy terms generated by eigenvalues emerging from zero.

If the feedback map is only (C^1), or has a term such as (t^2\log|t|), standard (C^2/C^3) normal-form arguments cannot be used without modification. The research must then either:
1. develop a justified nonsmooth/low-regularity bifurcation argument suited to the derived asymptotics; or
2. prove that the relevant branch directions lie in a fixed-rank regularity stratum and that the required derivatives exist there; or
3. establish an obstruction showing that a proposed smooth equivariant-bifurcation route is invalid for that mode.

This regularity gate is a first-class mathematical task, not a technical footnote.

---

## 6. Proof and evidence standards

- Separate exact algebraic identities, analytic theorems, numerical evidence, conjectures, and open questions.
- Numerical scans may locate candidate critical points and estimate coefficients; they do not prove branch existence or stability.
- Any numerical critical point must be accompanied by convergence, gap, conditioning, and error analysis appropriate to the observable being differentiated.
- A finite-(N) theorem must state its exact range of (N). Do not extrapolate to (N\to\infty).
- A theorem for one isotropy type or one (N) must not be presented as a complete classification.
- Every theorem must state its domain, regularity, spectral, transversality, and nondegeneracy assumptions.
- Lean formalization begins only after the mathematical statement and proof dependencies are frozen. No `sorry`, hidden axioms, or weakened theorem statements to force a build.

---

## 7. Explicit exclusions

The redesigned Paper B does **not** claim to:
1. re-prove Paper A's symmetric threshold scaling or saddle-node theorem;
2. prove the global sign (B-C>0), or make the old linear-response obstruction its central result;
3. prove that all nonuniform branches are geometric, local, lattice-like, or finite-dimensional in an emergent spatial sense;
4. prove uniqueness or global completeness of all nonuniform fixed points;
5. establish thermodynamic-limit results or arbitrary-graph generalizations;
6. analyze finite-temperature, open-system, or time-dependent quantum dynamics;
7. claim experimental/device-control applications from bifurcation results alone.

The old (B-C) analysis may be cited as historical context or reused as an independently audited auxiliary identity where relevant, but it is not a substitute for the new nonlinear theorem programme.

---

## 8. Dependency boundary with the other papers

- **Paper A inputs:** the precise Hamiltonian, symmetric branch, dimensionless scaling, and audited symmetric-point response decomposition. Every imported statement must be cited to its exact A theorem/assumption status.
- **Paper B outputs:** model-specific nonuniform branch existence, isotropy types, nonlinear local branch structure, and full-edge-space stability results.
- **Paper C boundary:** a nonuniform coupling pattern is not yet an emergent geometry. Geometry requires additional structural and obstruction analysis in C.
- **Paper D boundary:** spectral singularity geometry is not the same object as the bifurcation set of nonuniform self-consistent branches.
- **Paper E boundary:** Paper B does not perform geometric reconstruction or prove identifiability/rigidity.

---

## 9. Initial execution order

1. Freeze the exact model, residual sign convention, physical domain, and group action.
2. Audit ground-state and reduced-state regularity, especially zero eigenvalues of (\rho_{ij}).
3. Compute the symmetric-branch response spectrum and identify candidate nontrivial critical modes.
4. Prove or refute criticality and transversality in the actual quantum model.
5. Enumerate eligible isotropy subgroups for the first critical sector.
6. Derive the reduced nonlinear coefficients from the quantum feedback map.
7. Prove at least one nonuniform branch, or record a rigorous obstruction.
8. Compute full-space branch stability under the specified Picard iteration.
9. Only then expand to further (N), isotropy types, and secondary branch structure.
10. Freeze theorem statements and formalize them in Lean.

**Current status:** scope defined; all Paper B theorem families are research targets, not yet established results. The regularity gate and first model-specific critical-mode search are the immediate next tasks.
