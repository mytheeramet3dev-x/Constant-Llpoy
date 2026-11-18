# Paper A — Lean Semantic Correspondence Audit

**Audit ID:** `PAPER_A_LEAN_SEMANTIC_CORRESPONDENCE_AUDIT`  
**Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Audited Constant Llapoy revision:** `4f6efbe9a1140007d73250940ed7c0ee97411842`  
**Lean:** `leanprover/lean4:v4.36.0`; **Mathlib:** `96f6b8b8e029545577421f198a89fb174a4d62e6`

## Purpose and standard

This audit asks whether each of the 15 registered Paper A claims has a Lean declaration whose mathematical statement and hypotheses correspond to that exact frozen source claim. Merely finding a related lemma, a similarly named declaration, a source hash, or a green build is not correspondence.

Classifications:
- **ABSTRACT_MATRIX_CORE_ONLY:** formalizes a generic mathematical core under supplied hypotheses, without proving the Paper A model-specific bridge.
- **PARTIAL_SUPPORT_ONLY:** a generic or leading-order lemma supports only a sub-obligation.
- **NO_DIRECT_FORMALIZATION:** no declaration in the four audited Paper A modules formalizes the claim.
- **SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY:** the frozen source assertion conflicts with the local corrected endpoint analysis; Lean contains conditional supporting lemmas but does not prove the physical-model remainder.

## Claim-to-Lean matrix

| Frozen claim | Current Lean relationship | Exact remaining gap |
|---|---|---|
| DEF-0001 — Interior critical point | PARTIAL_SUPPORT_ONLY: `hasDerivAt_local_min_branch_eq_zero`, `hasDerivAt_nonnegative_branch_eq_zero` | Generic Fermat/local-minimum facts only; no formalization of the paper's specific objective, domain, or hypotheses. |
| PROP-0001 — Conditional exact threshold scaling | NO_DIRECT_FORMALIZATION | No exact threshold-scaling theorem. |
| PROP-0002 — Tangent constraint at an interior critical point | NO_DIRECT_FORMALIZATION | No paper-specific tangent constraint theorem. |
| PROP-0003 — Exact Picard local-attractivity criterion | NO_DIRECT_FORMALIZATION | No Picard map, derivative, or local-attractivity criterion. |
| PROP-0004 — Root independence along the dimensionless scaling ray | NO_DIRECT_FORMALIZATION | No root-independence theorem. |
| PROP-0005 — Edge-response sector decomposition and exact `chi` identity | PARTIAL_SUPPORT_ONLY: `hasDerivAt_one_site_leading_entropy_incident`, `..._disjoint`, `..._edge_contrast` | These differentiate only a leading one-site entropy correction; they do not prove the (S_N) decomposition, the three sector eigenvalues, or (chi_1-chi_2=(N-2)(B-C)). |
| PROP-0006 — Positive energy rescaling and dimensionless mutual information | NO_DIRECT_FORMALIZATION | No projector-preservation or dimensionless mutual-information theorem. |
| PROP-0007 — Symmetric zero-coupling trivial fixed point | NO_DIRECT_FORMALIZATION | No source-level fixed-point theorem. |
| PROP-0008 — Subcritical exclusion of nontrivial roots | NO_DIRECT_FORMALIZATION | No root-exclusion theorem. |
| PROP-0009 — Strong-coupling asymptotics of mutual information | PARTIAL_SUPPORT_ONLY | `strongCouplingCoefficient_pos` and `strongCoupling_response_positive_of_remainder` concern a (B-C) sign step and assume the remainder bound; they do not formalize the mutual-information expansion or derive its differentiated remainder. |
| PROP-0010 — Uniform-response upper bound | NO_DIRECT_FORMALIZATION | No uniform-response bound or non-implication theorem. |
| PROP-0011 — Scale covariance of edge-response eigenvalues | NO_DIRECT_FORMALIZATION | No scale-covariance theorem. |
| PROP-0012 — Weak-coupling opposite-sign response | SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY | `weakCouplingCoefficient_pos` and `weakCoupling_response_positive_of_remainder` prove a positive coefficient and a conditional final sign step only. They do not prove the model-specific differentiated remainder; this is not verification of the frozen opposite-sign assertion. |
| THM-0001 — Conditional local saddle-node normal form | NO_DIRECT_FORMALIZATION | No formal Taylor/branch theorem or corresponding regularity bridge. |
| THM-0002 — Finite-(N) ground-state Perron–Frobenius nondegeneracy | PARTIAL_SUPPORT_ONLY | The TFIM computational-basis matrix, Hermitian property, scalar shift, nonnegative entries, exact single-spin-flip support, and Boolean-hypercube connectivity are formalized. Still missing: shifted-matrix Hermiticity, spectral-shift transfer, and existence of a strictly positive top eigenvector. |

## Audited Lean modules

| Module | Main declarations | Correspondence boundary |
|---|---|---|
| `PerronFrobeniusCore.lean` | Positive-eigenvector ratio/harmonic arguments; one-dimensional Perron eigenspace; unique real-symmetric spectral index; characteristic-root multiplicity one | Abstract matrix theorem only; physical Hamiltonian encoding remains open. |
| `StrongCoupling.lean` | Positive leading coefficient; conditional sign under explicit remainder bound | Does not prove the asymptotic expansion or its remainder. |
| `WeakCoupling.lean` | Positive logarithmic coefficient; conditional sign; positive-branch entropy derivative | Does not derive the model-specific differentiated remainder or verify the source's opposite-sign statement. |
| `HamiltonianEncoding.lean` | Computational-basis TFIM matrix, Hermitian proof, explicit `cI-H` shift, entrywise nonnegativity, single-spin-flip support, and Boolean-hypercube connectivity | Does not prove shifted-matrix Hermiticity, positive eigenvector existence, or spectral transfer to the ground state. |
| `ZeroEigenvalueEntropy.lean` | Parity/Schur algebra, scalar analytic factorization and bounds, generic entropy derivative estimates, leading one-site edge derivative | Generic and leading-order tools; their hypotheses are not yet derived from the complete TFIM reduced-state model. |

## Result

- Registered claims reviewed: **15/15**.
- Fully corresponding Lean claim statements: **0/15**.
- Partial support / abstract or model-specific core: **4 claims** (DEF-0001, PROP-0005, PROP-0009, THM-0002). For THM-0002, the model matrix and shifted nonnegative support are now formalized, but the full Perron application remains open.
- No direct formalization: **10 claims**.
- Source conflict retained: **PROP-0012**.
- No claim status is upgraded by this audit.

**L-02 remains BLOCKED.** This matrix improves traceability and makes the gaps explicit; it does not discharge the semantic-correspondence layer. It requires independent mathematical review and subsequent model-specific Lean formalization. For THM-0002, the remaining obligations are shifted-matrix Hermiticity, spectral transfer from `K=cI-H`, and construction of a strictly positive top eigenvector.

## Reproducibility

The machine-readable companion `meta_verification/paper_a_semantic_correspondence.json` binds the 15 claim-record blob SHAs, frozen source commit, audited repository revision, Lean toolchain, Mathlib revision, and exact module blob SHAs.

The audit is intentionally conservative. It does not infer equivalence from names, comments, nearby formulas, compilation, or numerical diagnostics.


## 2026-11-18 model-encoding update

The audit now binds five Lean modules, including \`HamiltonianEncoding.lean\`, at the exact module blob SHA. THM-0002 remains **PARTIAL_SUPPORT_ONLY**. The formalization now includes the Boolean-hypercube path theorem \`singleSpinFlip_pf_connected\` and its transfer to positive support of the shifted TFIM matrix, \`shiftedTFIMHamiltonian_pf_connected\`.

Still not established: Hermiticity of the shifted matrix as a separate Lean theorem, the algebraic transfer from \(K=cI-H\) to the ground eigenvalue of \(H\), and existence of a strictly positive eigenvector at the top eigenvalue. This update does not promote THM-0002 to verified.
