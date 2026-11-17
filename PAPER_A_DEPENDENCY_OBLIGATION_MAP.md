# Paper A Preliminary Dependency and Verification-Obligation Map

- **Document ID:** CL-DEP-A-001
- **Version:** 0.2.1
- **Source revision:** `Absolute_Sym` / `paper-a-interval-audit-2026-11-14` / `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Inputs:** `PAPER_A_FULL_EXTRACTION_AUDIT.md`, `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`, 15 Paper A claim records, and the 2026-11-17 strong-coupling follow-up audits
- **Status:** PRELIMINARY_MAP; dependencies and proof obligations not yet independently closed
- **Verified claims:** 0

## 1. Purpose and interpretation

This map records likely logical prerequisites and explicit verification obligations for Paper A. It is a planning/audit artifact, not a proof and not a claim that every listed edge is formally necessary. Edges are labelled:

- **D — definitional:** a claim uses a definition or convention.
- **L — logical:** the conclusion is derived from another claim or equation.
- **A — analytic:** regularity, limit, perturbation, or spectral assumptions are needed.
- **S — symmetry/representation:** group action or invariant-sector structure is needed.
- **U — unresolved:** likely dependency or proof source is missing and must be confirmed.

A dependency edge must not be treated as a proof. If a claim's proof uses an assumption not established elsewhere, that assumption remains an open obligation.

## 2. Claim nodes

| Node | Claim | Current extraction/review status |
|---|---|---|
| A-DEF-0001 | Interior critical point | Source-faithful; definition only |
| A-PROP-0001 | Threshold infimum, interior attainment scaling, tangent minimizer relation, subcritical exclusion | Source-faithful; attainment and domain conditions remain |
| A-PROP-0002 | Tangent constraint | Source-faithful; follows from critical-point equations |
| A-THM-0001 | Conditional local saddle-node normal form | Reviewed with regularity/remainder issue |
| A-PROP-0003 | Exact scalar Picard local-attractivity criterion | Source-faithful; scalar iteration only |
| A-PROP-0004 | Root-by-root dimensionless scale independence | Source-faithful; root existence/branch selection not proved |
| A-PROP-0005 | Edge-space representation decomposition and exact `chi_1-chi_2` identity | Source-faithful; explicit (N\ge3) domain obligation |
| A-THM-0002 | Finite-(N), (h>0) ground-state nondegeneracy | Independent finite-dimensional Perron–Frobenius proof review PASS for all finite real couplings; Lean formalization and exact Hamiltonian correspondence remain OPEN |
| A-PROP-0006 | Positive energy rescaling and (I_{12}=\mathcal G_N(J/h)) | Source-faithful; requires ground-state projector uniqueness or a carefully stated spectral-subspace version |
| A-PROP-0007 | Zero-coupling product state and trivial root | Source-faithful |
| A-PROP-0008 | Subcritical exclusion | Duplicate/overlap of a subclaim in A-PROP-0001; preserve as trace record |
| A-PROP-0009 | Strong-coupling expansion of (\mathcal G_N) and its derivative | PARTIALLY VERIFIED by independent fixed-N derivation; Lean/correspondence pending; upstream Lemma 5.1 citation remains mismatched |
| A-PROP-0010 | Uniform-response upper bound and non-implication of response negativity | Source-faithful algebraic bound |
| A-PROP-0011 | Scale covariance of response eigenvalues | Source excerpt boundary corrected; differentiability remains an obligation |
| A-PROP-0012 | Weak-coupling lower-branch opposite-sign response assertion | SOURCE_CONFLICT; original negative-sign proof invalid; independent Constant Llapoy endpoint derivation gives positive sign, formalization/correspondence pending |
| A-SUPP-LEMMA-5-1 | Supporting fixed-N strong-coupling positivity statement for (B-C) | Independent Constant Llapoy analytic derivation and internal review pass; not an authoritative manuscript theorem; Lean/correspondence pending |

## 3. Preliminary dependency edges

| From (claim) | Depends on | Edge | Reason / open condition |
|---|---|---|---|
| A-PROP-0001 | A-PROP-0006 | D/A | Requires a well-defined dimensionless (\mathcal G_N(x)), positivity on the domain, and a precise domain for (x/\mathcal G_N(x)) |
| A-DEF-0001 | Model definitions in Sections 2–3 | D | Uses (F), (f), (x), (g), (h), and (eta=g/h) |
| A-PROP-0002 | A-DEF-0001 | L | Combines (F=0) and (F_x=0) at an interior critical point |
| A-THM-0001 | A-DEF-0001, A-PROP-0001, A-PROP-0002 | L/A | Needs a nontrivial tangent point, (\mathcal G_N(x_c)>0), and a nondegenerate curvature condition; current (C^2) hypothesis does not justify stated cubic remainder |
| A-PROP-0003 | Model definition of scalar Picard map (T(x)=\eta\mathcal G_N(x)) | D/L | Derives (|T'(x_*)|<1\iff -2h<F_x<0); applies only to the scalar iteration |
| A-PROP-0004 | A-PROP-0001, A-PROP-0006 | D/L | Along (g=\gamma\alpha_Nh), the root equation is independent of (h); does not establish existence or branch uniqueness |
| A-THM-0002 | Hamiltonian definition in Section 2.1 | A | Apply PF to (cI-H), not (H+cI); verify irreducibility and allowed coupling domain |
| A-PROP-0006 | A-THM-0002 | A/L | Positive multiplication by (h) preserves the ground eigenspace; uniqueness is needed for a single ground-state projector |
| A-PROP-0007 | Hamiltonian at (x=0), Section 2.4 | L | At zero coupling the ground state is the product (|+x\rangle^{\otimes N}), giving zero pairwise mutual information |
| A-PROP-0008 | A-PROP-0001 | DUPLICATE | Same subcritical-exclusion statement; not an independent theorem |
| A-PROP-0009 | Independent uniform function/derivative proof and small-eigenvalue coefficient derivation in Constant Llapoy | A/S | Function and differentiated remainder derived for fixed finite N >= 4; the source citation remains mismatched and formalization/correspondence are pending |
| A-PROP-0010 | Section 5.1 definition of (F_J) | D/L | (F_J=g\,\partial_J I_{12}-1); (F_J<0\) gives only the upper bound (\partial_JI_{12}<1/g) |
| A-PROP-0011 | A-PROP-0006 | D/A | Differentiate the dimensionless dependence with respect to each edge coupling; requires differentiability of the ground-state response map |
| A-PROP-0012 | Frozen Lemma 5.2 proof/audit plus Constant Llapoy weak-coupling proof and audit | A/S | Corrected positive leading sign and conservative differentiated remainder derived for fixed finite N >= 4; source assertion contradicted locally; Lean/correspondence pending |
| A-SUPP-LEMMA-5-1 | General-edge joint-analyticity, parity-block Schur cancellation, positive/zero small-eigenvalue entropy treatment | A/S | Fixed-N strong-coupling asymptotic derived locally; formalization and manuscript correspondence remain open |
| A-PROP-0005 | (S_N)-invariance of the symmetric Hamiltonian and response map | S/A | Need differentiability, orbit classification of edge pairs, and (N\ge3); algebraic eigenvalue identity is separate from the conjectural sign of (B-C) |

## 4. Open verification obligations

### VO-A-001 — Ground-state nondegeneracy

- **Mathematical review completed:** corrected the shift to (K=cI-H), proved entrywise nonnegativity and hypercube irreducibility, and identified the Perron eigenvalue with the ground eigenvalue. See `audits/paper-a/THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md`.
- Use (cI-H) with explicit (c); prove entrywise nonnegativity.
- Prove irreducibility via connectedness of the single-spin-flip hypercube graph.
- State whether the result covers all finite real (J_{ij}) or only the source's reference domain (J_{ij}\ge0).
- **Mathematical conclusion:** the lowest eigenvalue of (H) is simple for finite (N≥1), (h>0), and arbitrary finite real (J_ij). **Still open:** Lean formalization and exact correspondence to the formal Hamiltonian definition.

### VO-A-002 — Threshold definition and attainment

- Specify the domain where (\mathcal G_N(x)>0).
- Distinguish (inf) threshold from an attained minimizer.
- Establish whether (\alpha_N) is finite and positive.
- State the exact conditions under which (g_c(h)=\alpha_Nh) corresponds to an actual tangent solution rather than only an infimum threshold.
- Keep the subcritical exclusion separate from any supercritical existence or global root-count claim.

### VO-A-003 — Saddle-node regularity and curvature

- Establish differentiability through the required order near (x_c).
- Replace the unsupported cubic remainder or supply stronger regularity hypotheses.
- Verify (\mathcal G_N''(x_c)<0) for the model if the supercritical square-root branch is claimed.
- Distinguish local existence of two roots from global root counts and global continuation.
- Verify the claimed (O(g-g_c)) correction order under explicit hypotheses.

### VO-A-004 — Scalar iteration stability

- Keep the exact multiplier (T'(x_*)) distinct from the fixed-point slope (f_x) or (F_x).
- State that (|T'|<1) is local stability for the scalar Picard iteration only.
- Do not infer full edge-space stability from scalar stability.

### VO-A-005 — Uniform strong-coupling asymptotics

- The function expansion and its differentiated remainder are independently derived in Constant Llapoy for each fixed finite N >= 4.
- Preserve the corrected fourth-order small-eigenvalue coefficient: c_4=1/648; c_N=1/[8(N-2)(N-1)^4] for N >= 5.
- Complete Lean formalization and proof-to-manuscript correspondence for A-PROP-0009.
- Keep the frozen manuscript's Lemma 5.1 citation mismatch visible; do not edit upstream without prior authorization.
- Trace large-parameter branch-limit conclusions to a separate valid global-continuation hypothesis.

### VO-A-006 — Response representation and sector eigenvalues

- State the minimum allowed (N), at least (N\ge3) for the displayed decomposition.
- Derive the three orbit classes for pairs of edges under (S_N).
- Derive the eigenvalues and multiplicities from the response operator.
- Verify the uniform eigenvalue normalization against the convention for changing every edge simultaneously.
- Keep global (B-C>0) as a conjecture. A separate fixed-N local strong-coupling asymptotic is now derived in Constant Llapoy, but is not yet a fully formalized manuscript theorem.

### VO-A-007 — Response scaling and sign bound

- Verify differentiability of (I_{12}) with respect to all edge couplings in the domain used.
- Derive the (h^{-1}) response scaling by the chain rule.
- Keep the dimensional eigenvalues distinct from the dimensionless (widetilde\chi_k).
- Preserve the exact implication (F_J<0\Rightarrow \partial_JI_{12}<1/g), not the false implication that the response is negative.

### VO-A-008 — Supporting-lemma scope and source reconciliation

- Lemma 5.1 and Lemma 5.2 files have been located outside the six authoritative sections, but their subject/status must be reconciled with the manuscript references.
- The located Lemma 5.1 file concerns (B-C), not the (\mathcal G_N(x)) expansion cited by Section 4.4.2. The uniform (\mathcal G_N) expansion now has an independent Constant Llapoy derivation; the source citation itself remains mismatched.
- A separate Constant Llapoy derivation now closes the fixed-N strong-coupling (B-C) asymptotic locally; this does not prove global positivity.
- The original Lemma 5.2 negative-sign proof is superseded by its audit; do not rely on it.
- Keep source correspondence and formalization obligations OPEN; the independent Constant Llapoy derivations do not repair the frozen upstream citation.
- Do not synthesize missing lemmas from surrounding prose.

### VO-A-010 — General-edge fixed-N strong-coupling response asymptotic

- Internal analytic review: PASS for fixed finite N >= 4 and the local strong-coupling regime.
- Full-Hilbert-space finite-difference diagnostic: consistent with the leading coefficient for N=4,5,6.
- Remaining: independent external review, Lean formalization, and exact correspondence to the supporting Lemma 5.1 statement.
- Do not infer global B-C positivity, uniformity in N, or an explicit epsilon_N.

## 5. Circularity and dependency closure

No complete dependency closure or circularity analysis has been performed. The edges above are provisional and must be checked against actual proof scripts and source derivations. A claim must not be used to discharge an obligation that ultimately depends on that same claim. Any shared lemma, definition, numerical routine, or formal axiom must be tracked in the trust-boundary inventory.

## 6. Explicit non-claims

This map does **not** establish:

- exactly two global nontrivial roots for every supercritical parameter;
- global continuation of the selected upper branch;
- model-specific negative curvature at the threshold;
- positivity of (B-C) for all parameters or uniformly in (N);
- full edge-space dynamical stability from scalar Picard stability;
- a formal Lean proof of the supporting Lemma 5.1 statement or a repair to its upstream source citation;
- correctness of any proof merely because a source claim is indexed.

## 7. Next actions

1. Formalize the independently derived A-PROP-0009 uniform asymptotic result and the supporting fixed-N B-C asymptotic in Lean.
2. Independently review the joint-analyticity and zero-eigenvalue entropy-direction argument for both endpoints.
3. Audit the exact correspondence between the Constant Llapoy statements and the frozen Paper A / supporting Lemma 5.1 statements.
4. Keep all proposed Absolute Symmetry source corrections separate and request authorization before any upstream edit.
5. Produce a formal dependency graph only after the remaining provisional edges are independently confirmed.

---

**End of preliminary Paper A dependency and verification-obligation map.**


## 8. Newly located supporting-source obligations

- **A-THM-0002:** candidate proof source `docs/tfim_ground_state_simplicity_lemma.md` (blob `472328b596ccdcc82ece65faf5ef65a9dab63e50`) supplies the (cI-H) Perron–Frobenius argument. It is not yet independently verified by Constant Llapoy.
- **A-PROP-0009:** `docs/lemma_5_1_proof.md` is not the proof of the (\mathcal G_N(x)) expansion cited in Section 4.4.2; it concerns (B-C). The uniform asymptotic has an independent Constant Llapoy derivation; the frozen upstream citation remains mismatched.
- **A-PROP-0012:** the original negative-sign derivation omitted an order-(r^2) coherence. The corrected positive leading sign now has a Constant Llapoy differentiated-remainder derivation; it contradicts the source assertion locally as J/h -> 0. Lean and manuscript correspondence remain pending.
- **Entropy–Schur remainder lemma:** `docs/entropy_schur_remainder_lemma.md` is conditional on model-specific Schur-complement and derivative bounds; it does not itself establish those hypotheses.
- **Supplementary material:** `Arxiv/supplementary_material.md` supplies an exact Johnson-scheme derivation of the sector identity and finite numerical validation data; these must be separated into exact algebraic support and finite empirical evidence.

### VO-A-009 — Weak-coupling response conflict

- The original Lemma 5.2 negative-sign proof is invalid because it omits the order-r^2 coherence.
- The corrected positive leading sign and a conservative differentiated remainder are independently derived in Constant Llapoy for fixed finite N >= 4.
- The Section 4.4.3 opposite-sign assertion is contradicted in the weak-coupling endpoint regime.
- Lean formalization and exact manuscript correspondence remain pending.
- Keep global B-C positivity open; local endpoint positivity is not a global theorem.

### VO-A-011 — Weak-coupling entropy derivative remainder

- Preserve the full odd-block Gram coherence and its positive eigenvalue branch.
- Formalize the analytic nonnegative-eigenvalue entropy derivative lemma for the zero and rank-changing branches.
- Verify the conservative O(r^3 |ln r|) derivative remainder in dimensionless edge coordinates.
- Check the leading derivative identity ∂u13 p1 = ∂u13 q = r^2/8 + O(r^3), with all disjoint-edge leading derivatives zero.
- Formalize the fixed-N result in Lean and audit correspondence before any upstream change.
