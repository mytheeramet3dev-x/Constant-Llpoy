# Paper B — B1 Model and Regularity Audit

**Official title:** Equivariant Bifurcation, Isotropy Classification, Representation-Resolved Stability, and Nonlinear Branch Structure in Self-Consistent Quantum Interaction Networks

**Workspace:** Constant Llpoy  
**Audit stage:** B1 — Model and Regularity Audit  
**Status:** INITIAL AUDIT RECORDED; critical-mode-specific regularity remains OPEN  
**Source policy:** The upstream `Absolute_Sym` repository is read-only. This document is a new independent audit artifact.

---

## 1. Frozen model and conventions

Fix a finite integer (N\ge 4), let (E_N=\{\{i,j\}:1\le i<j\le N\}), and let (m=\binom N2). For an edge-coupling vector (\mathbf J\in\mathbb R^{E_N}), use

\[
H_N(\mathbf J;h)
=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z
-h\sum_{i=1}^N\sigma_i^x,\qquad h>0.
\]

The reference physical coupling domain is (\mathcal C_N=[0,\infty)^{E_N}). The local analysis is centered at a fully symmetric point (\mathbf J_*=J_*\mathbf 1_E) with (J_*>0); hence a sufficiently small open ambient ball around that point is contained in the interior of (\mathcal C_N).

For the unique normalized ground state (\Psi_0(\mathbf J;h)), define
\[
I_{ij}(\mathbf J;h)=S(\rho_i)+S(\rho_j)-S(\rho_{ij}),
\qquad S(\rho)=-\operatorname{Tr}(\rho\log\rho).
\]

Use dimensionless variables (x_{ij}=J_{ij}/h), (\eta=g/h), and the fixed residual convention
\[
\mathcal F(\mathbf x,\eta)=\eta\boldsymbol{\mathcal I}_N(\mathbf x)-\mathbf x.
\]
Thus a fixed point satisfies (\mathcal F=0), and the default Picard map is
\[
T_\eta(\mathbf x)=\eta\boldsymbol{\mathcal I}_N(\mathbf x).
\]
This sign convention is now fixed for the Paper B workspace.

## 2. Ground-state simplicity: established for the stated finite model

In the simultaneous (\sigma^z)-eigenbasis, the diagonal interaction term is real and diagonal. The transverse-field term has off-diagonal matrix elements (-h<0) between computational-basis configurations that differ at exactly one spin. The configuration graph is the connected (N)-dimensional hypercube.

Choose (c\in\mathbb R) sufficiently large that (cI-H_N) is entrywise nonnegative. Its off-diagonal graph is connected, so it is irreducible. Perron–Frobenius therefore gives a simple largest eigenvalue of (cI-H_N), equivalently a simple lowest eigenvalue of (H_N). The ground-state vector can be chosen strictly positive in this basis.

**Audit conclusion B1-GS:** For every finite real coupling vector and every (h>0), the ground state is simple. In particular, simplicity holds on the local neighborhood used here; it does not require the couplings to be permutation-symmetric.

Because (H_N(\mathbf J;h)) is a finite-dimensional real-analytic matrix family and the ground eigenvalue is simple, the ground-state spectral projector is real-analytic locally in (\mathbf J). Consequently, the reduced density matrices (\rho_i(\mathbf J)) and (\rho_{ij}(\mathbf J)), obtained by partial trace of that projector, are real-analytic matrix-valued functions locally.

**Important limitation:** Analyticity of the projector and reduced density matrices does not imply analyticity, (C^2), or (C^3) regularity of their von Neumann entropies at rank-deficient density matrices.

## 3. Permutation equivariance: established

For (\pi\in S_N), let (U_\pi) be the induced permutation unitary on the (N)-spin Hilbert space and (P_\pi) the induced permutation representation on edge coordinates. The Hamiltonian satisfies
\[
H_N(P_\pi\mathbf J;h)=U_\pi H_N(\mathbf J;h)U_\pi^*.
\]
Uniqueness of the ground-state projector implies
\[
P_0(P_\pi\mathbf J)=U_\pi P_0(\mathbf J)U_\pi^*.
\]
Partial trace and von Neumann entropy are covariant/invariant under the corresponding relabeling of subsystems. Therefore
\[
\boldsymbol{\mathcal I}_N(P_\pi\mathbf x)
=P_\pi\boldsymbol{\mathcal I}_N(\mathbf x),
\qquad
\mathcal F(P_\pi\mathbf x,\eta)
=P_\pi\mathcal F(\mathbf x,\eta).
\]

**Audit conclusion B1-EQ:** The actual finite-dimensional quantum feedback map is (S_N)-equivariant wherever it is defined. The ground-state simplicity argument supplies the unambiguous projector needed for this statement.

## 4. Exact rank obstruction in the symmetric two-site reduced state

At a fully permutation-symmetric coupling vector, the Hamiltonian commutes with every vertex permutation. Since its ground state is simple, its ground-state projector is permutation-invariant. In particular, it is invariant under the transposition exchanging sites (i) and (j).

Let (W_{ij}) be the swap operator on the two selected qubits and let
\[
Q^-_{ij}=\frac{I-W_{ij}}2
\]
be the projector onto the two-qubit antisymmetric (singlet) subspace. Swap invariance of the global ground-state projector gives
\[
\operatorname{Tr}(Q^-_{ij}\rho_{ij})
=\operatorname{Tr}(Q^-_{ij}P_{0,ij})=0.
\]
Since (\rho_{ij}\) is positive semidefinite, this implies
\[
Q^-_{ij}\rho_{ij}=\rho_{ij}Q^-_{ij}=0.
\]

**Audit conclusion B1-RANK-01:** The symmetric-point two-site reduced state has an exact symmetry-enforced zero eigenvalue in the singlet direction. Thus (\rho_{ij}\) is rank-deficient at the symmetric point (rank at most three), independently of the values of its remaining triplet-sector eigenvalues.

This is a rigorous rank statement. It does not yet establish that all three triplet eigenvalues are strictly positive; that separate rank question remains OPEN.

## 5. Consequence for the entropy-regularity gate

The matrix-valued map (\mathbf x\mapsto\rho_{ij}(\mathbf x)) is analytic, but the entropy function (S(\rho)=-\operatorname{Tr}(\rho\log\rho)) is not smooth at a zero eigenvalue in the unrestricted positive-semidefinite cone.

The symmetric-point singlet kernel therefore blocks any blanket inference that the full ambient mutual-information map is (C^2) or (C^3). A perturbation that breaks the selected pair-swap symmetry may populate the singlet direction. The size and order of the resulting small eigenvalue, and hence the precise entropy modulus (for example a possible (t^2\log|t|) term), must be computed for each candidate perturbation direction.

The following distinctions are mandatory:

1. **Ambient edge space:** rank lifting in the singlet direction is possible in principle; its actual order and coefficient have not yet been established.
2. **Pair-swap-preserving subspace:** if a perturbation path preserves the transposition exchanging (i,j), the singlet weight for that pair remains exactly zero along the path. Entropy regularity on the remaining support still requires positivity/rank control of the triplet block.
3. **Critical representation and isotropy-fixed spaces:** no regularity conclusion is made until the candidate critical mode and its isotropy are identified and the reduced-state eigenvalue expansions are computed.
4. **Transverse directions:** full-space stability requires differentiability in all relevant transverse directions, not only inside a branch fixed-point subspace.

**Audit conclusion B1-REG-01:** The regularity gate is substantive and cannot be waived. The symmetric-point two-site rank defect is proved; the differentiability class of the full feedback map and of its restrictions to candidate critical/isotropy spaces is still OPEN.

## 6. Immediate next calculations

The next B1 work items are:

- **B1.1:** Compute the exact block form of (\rho_{ij}) under global spin-flip parity and pair exchange; determine whether the triplet block is strictly positive for the full finite parameter range or only on a restricted region.
- **B1.2:** For a general edge perturbation (v\in\mathbb R^{E_N}), compute the first nonzero term of the singlet weight
  \[
  p^-_{ij}(t)=\operatorname{Tr}(Q^-_{ij}\rho_{ij}(\mathbf x_*+tv)).
  \]
  Determine when its quadratic coefficient is positive, when it vanishes by symmetry, and what higher-order alternative occurs.
- **B1.3:** Repeat the rank/entropy expansion on candidate (V_1) and (V_2) directions and on their isotropy-fixed subspaces. Do not assume the critical sector before computing the response spectrum.
- **B1.4:** Only after B1.1–B1.3, classify the actual regularity ((C^1), (C^2), (C^3), analytic on a fixed-rank stratum, or a weaker modulus) needed by each proposed bifurcation theorem.
- **B1.5:** Then compute the symmetric-branch response eigenvalues and search for a nontrivial critical multiplier crossing (1), with transversality and complementary invertibility audited separately.

No normal-form theorem, Equivariant Branching Lemma, Lyapunov–Schmidt theorem requiring unverified smoothness, or Lean formalization is authorized by this initial audit alone.

## 7. Status ledger update proposed by this audit

| Obligation | Result of this audit | Status |
|---|---|---|
| B-REG-01: ground-state/equivariance foundation | Ground-state simplicity and (S_N)-equivariance derived for the stated finite model | MATHEMATICALLY ESTABLISHED IN THIS AUDIT; independent review pending |
| B-REG-02: entropy regularity | Exact singlet zero eigenvalue at the symmetric point proved; directional eigenvalue asymptotics not yet computed | PARTIAL; overall obligation OPEN |
| B-CRIT-01/02 | Not yet investigated in this stage | OPEN |
| B-ISO-01 | Not yet investigated | NOT YET INVESTIGATED |
| B-NL-01 / B-EX-01 / B-BR-01 | No nonlinear reduction attempted | OPEN |
| B-STAB-01/02 | No nonuniform branch or full-space spectrum yet | OPEN |
| B-LEAN-01 | No Lean encoding started | NOT STARTED |

## 8. Integrity rules

- No source file in `mytheeramet3dev-x/Absolute_Sym` was edited.
- The archived former Paper B manuscript is evidence of historical scope only; its old linear-response claims are not silently imported as new Paper B results.
- No numerical claim is made in this audit.
- No theorem is marked FORMALLY VERIFIED.
- Any failure of regularity, criticality, transversality, or nondegeneracy must be recorded as a mathematical result, not repaired by weakening assumptions without explicit scope approval.
