# Paper A — Claim-by-Claim Proof Obligation Matrix

- **Document ID:** CL-PA-VO-001
- **Version:** 0.1.0
- **Prepared against Constant Llpoy main:** `73171b0f540f3373cf35f88c4b6226f6d73d95ef`
- **Authoritative Paper A source:** `mytheeramet3dev-x/Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source policy:** The six revised Section files at the frozen source commit govern. This matrix does not edit or supersede them.
- **Status:** INITIAL CLAIM-BY-CLAIM OBLIGATION MAPPING COMPLETE; MATHEMATICAL VERIFICATION OPEN; INDEPENDENT MATRIX REVIEW REQUIRED.

## 1. Purpose and status semantics

This matrix expands the 15 Paper A source-linked records into claim-specific proof obligations. It is an execution plan and audit map, not a proof certificate.

Statuses used here:

- **FORMALIZED-PARTIAL:** Some relevant Lean declarations exist, but the full manuscript claim is not shown equivalent to them or its hypotheses are not discharged.
- **ANALYTIC-VERIFIED (algebraic scope only):** A direct hand-checkable algebraic derivation passes under explicit hypotheses, but Lean formalization and source correspondence remain open.
- **ANALYTIC-PARTIAL:** An independent mathematical derivation/review supports a stated restricted result, but formalization, source correspondence, or remaining conditions are open.
- **SOURCE-CONFLICT:** A manuscript assertion or supporting proof conflicts with a corrected derivation; do not use the disputed assertion as established.
- **NOT-FORMALIZED:** No direct Lean theorem for the manuscript claim was identified in the current semantic audit.
- **DEFINITION:** A definition, not a theorem to count as a proved result.
- **DUPLICATE:** Retained for traceability but not a distinct mathematical result.
- **NOT-ASSESSED:** The relevant proof obligation has not been independently settled.

A successful Lean build proves that the declarations compile under the configured environment. It does not, by itself, prove that a declaration is the same statement as a manuscript claim.

## 2. Source and artifact baseline

### 2.1 Frozen manuscript sources

| Section | Authoritative source | Frozen blob SHA |
|---|---|---|
| §2 | `Arxiv/paper_01_section_02_revised.md` | `541382fa7ab4b9e254c8e7e5158f202c1a975e0d` |
| §3 | `Arxiv/paper_01_section_03_revised.md` | `9ac164ac67cc121af212c4fb7268b809d9234bd6` |
| §4 | `Arxiv/paper_01_section_04_revised.md` | `a7570431eac62dd4555194df283edb5a9c87a28d` |
| §5 | `Arxiv/paper_01_section_05_revised.md` | `671c97fa68fa48c929760bf9956d197b358c4904` |

The full six-section inventory and source hashes remain in `MANUSCRIPT_SOURCE_MANIFEST.md`.

### 2.2 Current relevant Lean modules

- `formalization/lean/ConstantLlapoy/PaperA/HamiltonianEncoding.lean`
- `formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean`
- `formalization/lean/ConstantLlapoy/PaperA/ZeroEigenvalueEntropy.lean`
- `formalization/lean/ConstantLlapoy/PaperA/StrongCoupling.lean`
- `formalization/lean/ConstantLlapoy/PaperA/WeakCoupling.lean`

The declaration names below are candidate evidence links. Their existence is not a semantic-equivalence assertion.

## 3. Claim-by-claim matrix

### A. Threshold, critical point, and local dynamics

| Claim | Source statement and mathematical content | Required hypotheses / domain | Proof obligations | Existing evidence and formal correspondence | Disposition / next action |
|---|---|---|---|---|---|
| **AS-ALPHA-A-PROP-0001** — conditional exact threshold scaling (§2.5, §2 lines 159–206) | Define \(\alpha_N=\inf_{x>0}x/\mathcal G_N(x)\). If the infimum is attained at an interior \(x_c\), identify \(\eta_c=\alpha_N\), \(g_c(h)=\alpha_Nh\), and derive tangent relation. Subcritical exclusion \(\eta<\alpha_N\Rightarrow f(x;\eta)<0\) for all \(x>0\). | \(\mathcal G_N(x)>0\) on the domain; nonempty domain and finite infimum; interior attainment and differentiability for tangent condition; definitions of parameters fixed. | (1) Infimum pointwise bound. (2) Strict subcritical exclusion by multiplying with positive \(\mathcal G_N\). (3) At attained interior differentiable minimum, quotient derivative gives tangent equality. (4) Link \(\eta=g/h\) to \(g_c(h)=\alpha_Nh\). (5) Do not infer supercritical roots, two global roots, or nondegenerate saddle-node without further assumptions. | Independent audit **PASS** for infimum inequality, subcritical exclusion, and conditional interior tangent/scaling. Audit: `audits/paper-a/AS-ALPHA-A-PROP-0001_THRESHOLD_INFIMUM_AUDIT.md`. No matching full Lean declaration. | **ANALYTIC-VERIFIED (conditional scope only); NOT-LEAN-VERIFIED.** Model-specific attainment, positivity/finiteness, supercritical existence, and global root count remain open. |
| **AS-ALPHA-A-DEF-0001** — interior critical point definition (§3 lines 26–44) | Defines interior critical point by \(F=0,F_x=0\), equivalent to \(f=0,f_x=0\) with \(\eta=g/h\). | Explicit domains; \(x_c>0\), \(h>0\); differentiability for derivative expressions; definitions \(F=gf-hx\) via \(F=g\mathcal G_N(x)-hx\) and \(f=\eta\mathcal G_N(x)-x\). | (1) Record as definition. (2) Use \(F=hf\) for fixed positive \(h\). (3) Differentiate to get \(F_x=hf_x\). (4) Since \(h>0\), both zero-equivalences follow. (5) Do not claim critical point existence. | Independent consistency audit **PASS**. Audit file: `audits/paper-a/AS-ALPHA-A-DEF-0001_INTERIOR_CRITICAL_POINT_DEFINITION_AUDIT.md`. No dedicated Lean predicate/theorem was established. | **DEFINITION-CONSISTENT; NOT-LEAN-FORMALIZED.** This is a definition check, not a theorem proof or result count. |
| **AS-ALPHA-A-PROP-0002** — tangent constraint (§3 lines 46–66) | At an interior critical point, \(\mathcal G_N'(x_c)=\mathcal G_N(x_c)/x_c=h/g_c\); with exact scaling, both equal \(1/\alpha_N\). | \(x_c>0\), \(h>0\), \(g_c>0\); differentiability of \(\mathcal G_N\); fixed-point and critical-point equations exactly as defined in §2–3. | (1) Substitute \(F=0\) to obtain \(g_c\mathcal G_N(x_c)=hx_c\). (2) Substitute \(F_x=0\) to obtain \(g_c\mathcal G_N'(x_c)=h\). (3) Divide only after proving denominators are nonzero. (4) Derive the \(1/\alpha_N\) form only when exact threshold scaling is independently established. | Semantic audit: **NO_DIRECT_FORMALIZATION**. The generic local-minimum lemmas do not prove this model-specific algebraic implication. | **NOT-FORMALIZED.** A short algebraic Lean theorem should follow after definitions and positivity assumptions are formalized. |
| AS-ALPHA-A-THM-0001 | Local saddle-node expansion | PARTIAL: leading square-root splitting conditional; C2 does not justify claimed cubic remainder or O(delta g) correction. Needs C3/C2,1 or weakened remainder and branch-existence proof. Global exactly-two-roots not implied. No Lean formalization. Audit: audits/paper-a/AS-ALPHA-A-THM-0001_LOCAL_SADDLE_NODE_REGULARITY_AUDIT.md |
| **AS-ALPHA-A-PROP-0003** — exact Picard local-attractivity criterion (§3.3 lines 192–225) | For \(T(x)=\frac gh\mathcal G_N(x)\), the multiplier is \(T'(x_*)=1+F_x/h\). Linear stability is \(|T'(x_*)|<1\), equivalently \(-2h<F_x<0\). | Fixed point \(T(x_*)=x_*\); \(h>0\); differentiability of \(\mathcal G_N\) near \(x_*\); scalar one-dimensional iteration. | (1) Differentiate \(T\). (2) Use the exact definition of \(F_x\) to derive the multiplier identity. (3) Prove equivalence of inequalities using \(h>0\). (4) Distinguish linear contraction/attraction from nonlinear cases where \(|T'|=1\). (5) Do not infer stability from \(F_x<0\) alone away from the saddle-node. | Semantic audit: **NO_DIRECT_FORMALIZATION**. No direct Lean theorem for the Picard map or exact multiplier criterion. | **NOT-FORMALIZED.** Formalize the elementary scalar calculus result, then separately prove that the physical model's map meets its hypotheses. |
| **AS-ALPHA-A-PROP-0004** — root independence along dimensionless scaling ray (§4.2 lines 20–34) | Along \(g=\gamma\alpha_Nh\), the root equation becomes \(x=\gamma\alpha_N\mathcal G_N(x)\), independent of absolute scale \(h\); claim is root-by-root, not global uniqueness. | \(h>0\), \(\alpha_N\) independent of \(h\), fixed \(\gamma\), well-defined \(\mathcal G_N\); if using derivative notation \(\partial x_*/\partial h\), a differentiable selected root branch must exist. | (1) Substitute the scaling ray into the fixed-point equation. (2) Prove the root set is identical for all \(h>0\). (3) If asserting derivative zero, state a branch-selection/regularity condition or derive it from an implicit-function theorem with nonzero derivative. (4) Do not infer uniqueness or branch selection. | Semantic audit: **NO_DIRECT_FORMALIZATION**. No direct Lean theorem for the fixed-point root-set invariance. | **NOT-FORMALIZED.** Prove set-level invariance first; treat differentiable branch notation as a separate conditional corollary. |

### B. Hamiltonian, scaling, and zero-coupling claims

| Claim | Source statement and mathematical content | Required hypotheses / domain | Proof obligations | Existing evidence and formal correspondence | Disposition / next action |
|---|---|---|---|---|---|
| **AS-ALPHA-A-THM-0002** — Perron–Frobenius ground-state nondegeneracy (§2.1 lines 3–17) | For finite \(N\), \(h>0\), the TFIM ground state is nondegenerate. Correct PF route uses \(K=cI-H\), whose entries are nonnegative and whose positive-entry graph is the connected Boolean hypercube. | Finite \(N\ge1\), finite real edge couplings, \(h>0\); computational basis; choose \(c\) strictly above all diagonal energies. The result is finite-dimensional. | (1) Prove the encoded Hamiltonian equals the manuscript Hamiltonian in the computational basis. (2) Prove \(K=cI-H\) entrywise nonnegative. (3) Prove positive off-diagonal support is exactly single-spin flips and the hypercube is connected. (4) Establish existence of a nonzero nonnegative eigenvector at the largest eigenvalue of \(K\), or invoke a correctly scoped PF theorem that supplies it. (5) Prove strict positivity and algebraic simplicity. (6) Transfer the top eigenvalue of \(K\) to the ground eigenvalue of \(H\). | Independent finite-dimensional mathematical proof review: **PASS** for corrected \(cI-H\) argument. Current Lean modules encode Hamiltonian entries, shift, nonnegativity, connectivity, eigenvector correspondence, and conditional simplicity given a supplied nonzero nonnegative eigenvector. The declaration `shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive` propagates positivity but explicitly does **not** construct the eigenvector. Existence at the relevant top eigenvalue and final transfer remain open. | **ANALYTIC-PARTIAL / FORMALIZATION-PENDING.** Important source defect: the manuscript says shifting \(H\) by a sufficiently large positive multiple of identity makes it nonnegative; that is not the PF construction for this sign convention. The correct operator is \(cI-H\). Preserve the source verbatim in the audit, but prepare an explicit manuscript correction. |
| **AS-ALPHA-A-PROP-0006** — positive energy rescaling and dimensionless mutual information (§2.3 lines 71–111) | At the symmetric point \(H(J,h)=h\widetilde H(J/h,1)\), so for \(h>0\) the ground-state spectral projector is unchanged and \(I_{12}(J,h)=\mathcal G_N(J/h)\). | \(h>0\); symmetric coupling parameterization \(J\); finite-dimensional self-adjoint Hamiltonian; a well-defined ground spectral subspace. The vector/phase statement additionally assumes a nondegenerate ground state. | (1) Prove the operator identity. (2) Prove positive scalar multiplication preserves eigenvalue ordering and spectral eigenspaces/projectors. (3) Establish the reduced-state and mutual-information equality. (4) Keep the vector-phase statement distinct from the projector statement. (5) Do not extend to \(h=0\) by division by \(h\). | Independent audit: **PASS** for exact factorization, positive spectral scaling/projector invariance, and mutual-information identity. Audit file: `audits/paper-a/AS-ALPHA-A-PROP-0006_POSITIVE_RESCALE_MUTUAL_INFORMATION_AUDIT.md`. No matching full Lean declaration was established. | **ANALYTIC-VERIFIED (spectral/algebraic scope only); NOT-LEAN-VERIFIED.** Differentiability, entropy regularity, and \(h=0\) remain excluded. |
| **AS-ALPHA-A-PROP-0007** — zero-coupling product state and trivial fixed point (§2.4 lines 148–155) | At \(x=0\), the ground state is \(\bigotimes_i|+x\rangle_i\), hence \(\mathcal G_N(0)=0\) and \(x=0\) is the trivial fixed point. | Finite \(N\); transverse field coefficient positive; zero interaction; definitions of \(\mathcal G_N\) and fixed-point equation. | (1) Diagonalize \(-h\sum_i\sigma_i^x\) and prove the product ground state. (2) Compute its one- and two-site reduced states. (3) Prove mutual information is zero for the product state. (4) Substitute into the fixed-point equation. (5) Keep entropy differentiability at this rank-deficient endpoint separate. | Independent analytic audit: **PASS** for product ground state, zero reduced entropies/MI, and trivial fixed point. Audit file: `audits/paper-a/AS-ALPHA-A-PROP-0007_ZERO_COUPLING_PRODUCT_STATE_AUDIT.md`. Full Lean correspondence not established. | **ANALYTIC-VERIFIED (endpoint identity only); NOT-LEAN-VERIFIED.** Entropy differentiability, stability, and nontrivial-root claims remain open. |
| **AS-ALPHA-A-PROP-0008** — subcritical exclusion of nontrivial roots (§2.5 lines 197–206) | Same implication as the subcritical part of PROP-0001: \(\eta<\alpha_N\Rightarrow f(x;\eta)<0\) for all \(x>0\), assuming \(\mathcal G_N(x)>0\). | Same positivity/domain assumptions as PROP-0001; \(\alpha_N\) defined as the infimum in PROP-0001. | The proof obligation is identical to the subcritical-exclusion sub-obligation of PROP-0001. No separate theorem is needed. | No direct Lean formalization. Independent extraction review identifies this as an exact duplicate of PROP-0001. | **DUPLICATE.** Preserve record and audit trail; mark `DUPLICATE_OF AS-ALPHA-A-PROP-0001` through a controlled registry migration. Do not count as a distinct theorem or duplicate proof effort. |

### C. Asymptotic, response, and representation claims

| Claim | Source statement and mathematical content | Required hypotheses / domain | Proof obligations | Existing evidence and formal correspondence | Disposition / next action |
|---|---|---|---|---|---|
| AS-ALPHA-A-PROP-0005 | Edge-response decomposition and exact chi identity | PARTIAL: conditional S_N/J(N,2) matrix algebra checked; dimension sum and chi formulas/subtraction consistent. Differentiability of model MI map and Lean formalization remain open. Sector V2 has dimension 0 at N=3; interpret nontrivially for N>=4. B-C sign remains conjectural. Audit: audits/paper-a/AS-ALPHA-A-PROP-0005_EDGE_RESPONSE_REPRESENTATION_ALGEBRA_AUDIT.md |
| **AS-ALPHA-A-PROP-0009** — strong-coupling asymptotics of \(\mathcal G_N\) and derivative (§4.4.2 lines 103–120) | Fixed finite \(N\ge4\): \(\mathcal G_N(x)=\ln2-[(N-1)^2x^2]^{-1}+O_N(\ln x/x^4)\), and \(\mathcal G_N'(x)=2[(N-1)^2x^3]^{-1}+O_N(\ln x/x^5)\). | Fixed finite \(N\ge4\); \(x\to\infty\); even-sector perturbation and reduced-state eigenvalue/entropy remainder control. Not uniform in \(N\). | (1) Derive reduced-state eigenvalue branches. (2) Prove the small-eigenvalue coefficient, including exceptional \(N=4\). (3) Control entropy and differentiated remainder independently. (4) Resolve frozen citation to Lemma 5.1 (which concerns \(B-C\)). (5) Independently reproduce coefficient diagnostics and formalize uniform-path result. | Follow-up analytic derivation supplies separate function and derivative expansions using small eigenvalue \(\lambda_s=c_N\varepsilon^4+O_N(\varepsilon^6)\), two-sided scale bounds, and entropy derivative control. Internal consistency review PASS; recurrence and exact-rational diagnostics were **not independently rerun** in this review. Report: audits/paper-a/AS-ALPHA-A-PROP-0009_UNIFORM_ASYMPTOTIC_FOLLOWUP_REVIEW.md. Earlier audit identifies source mismatch and conditional gaps. | **PARTIALLY VERIFIED (uniform path, derivation review); NOT-LEAN-VERIFIED.** Source citation mismatch, independent reproduction, and source-to-Lean correspondence remain open. Does not prove \(B-C\). |
| AS-ALPHA-A-PROP-0010 | Uniform-response upper bound and non-implication | ANALYTIC PASS conditionally: F_J<0 iff uniform response <1/g for g>0; counterexample confirms it does not imply negative response. Picard attraction requires -2<F_J<0. Differentiability and coordinate convention required; no Lean formalization. Audit: audits/paper-a/AS-ALPHA-A-PROP-0010_UNIFORM_RESPONSE_BOUND_AUDIT.md |
| **AS-ALPHA-A-PROP-0011** — scale covariance of edge-response eigenvalues (§5.4 lines 127–131) | Claims \(\chi_k(J,h)=h^{-1}\widetilde\chi_k(J/h)\), so sector ordering is scale-independent while dimensional eigenvalues scale as \(h^{-1}\); feedback eigenvalues depend on \(g/h\). | \(h>0\); response derivatives exist; dimensionless dependence on edge ratios and consistent edge-coordinate normalization. | (1) Establish dimensionless dependence for independent edge couplings. (2) Apply chain rule to dimensional edge derivatives. (3) Confirm sector eigenvalues inherit the scalar factor. (4) Verify feedback spectrum scaling. | Audit **PASS (conditional chain-rule scope)**: audits/paper-a/AS-ALPHA-A-PROP-0011_SCALE_COVARIANCE_EDGE_RESPONSE_AUDIT.md. No full Lean theorem; model-specific entropy differentiability and coordinate conventions remain assumptions. | **ANALYTIC-VERIFIED (conditional); NOT-LEAN-VERIFIED.** No sector-ordering claim follows. |
| **AS-ALPHA-A-PROP-0012** — weak-coupling opposite-sign response assertion (§4.4.3 line 134) | Source says the lower branch has “distinct scaling and opposite-sign response characteristics” and points to Lemma 5.2. Supporting Lemma 5.2 originally asserted \(B-C<0\). Corrected fixed-\(N\) weak-coupling derivation gives \(B-C=\frac{J}{8h^2}\ln\!\frac{2(N-2)}{N-1}+O_N(\frac{J^2}{h^3}[1+|\ln(J/h)|])\), positive for sufficiently small \(J/h>0\), for each fixed \(N\ge4\). | Fixed finite \(N\ge4\); weak-coupling \(r=J/h\to0^+\); uniform reference point with independent real edge perturbations; full order-\(r^2\) coherence retained; model-specific differentiated entropy remainder control. | (1) Specify exactly which response quantity and branch comparison “opposite-sign” denotes. (2) Re-derive the weak-coupling reduced-state blocks including the omitted order-\(r^2\) coherence. (3) Prove the entropy derivative remainder. (4) Check the asymptotic against high-precision full-Hilbert-space calculations. (5) Decide whether the source sentence must be withdrawn or rewritten. (6) Do not infer global \(B-C>0\) from the local endpoint result. | Internal analytic review of the corrected fixed-\(N\) derivation: **PASS** in the local weak-coupling regime; full-Hilbert-space numerical checks for \(N=4,5,6\) are consistent. Lean has `weakCouplingCoefficient_pos` and `weakCoupling_response_positive_of_remainder`, but the latter is conditional on an assumed remainder bound; the model-specific differentiated remainder is not yet formalized. The original negative-sign derivation is superseded by its own audit due to omitted coherence. | **SOURCE-CONFLICT / NOT-VERIFIED.** The negative-sign supporting derivation is invalid, and the corrected local asymptotic gives the opposite leading sign. The manuscript's prose is less precise than the supporting \(B-C\) claim, so exact semantic reconciliation is still required. This is a substantive source issue, not merely missing Lean code. |

## 4. Provisional dependency map

These are proof-planning dependencies, not yet a verified dependency graph.

| Downstream claim | Candidate dependency | Why |
|---|---|---|
| PROP-0002 | DEF-0001; definitions of \(F,f,\eta\) | Tangent identities require the critical-point equations and parameter scaling. |
| THM-0001 | DEF-0001; PROP-0002; local regularity/nondegeneracy assumptions | Saddle-node expansion is centered at the critical point. |
| PROP-0003 | DEF-0001; fixed-point definition; derivative convention | Multiplier identity uses \(F_x\) at a fixed point. |
| PROP-0004 | PROP-0001; PROP-0006 | Threshold scaling and dimensionless dependence are used in the ray substitution. |
| PROP-0008 | PROP-0001 | Exact duplicate of the subcritical-exclusion subclaim. |
| PROP-0007 | TFIM Hamiltonian definition; zero-coupling spectral calculation | Product ground state and zero mutual information. |
| PROP-0009 | TFIM spectral perturbation; reduced-state eigenvalue branches; entropy derivative control | Function and derivative asymptotics depend on these estimates. |
| PROP-0005 | Differentiability of mutual information; \(S_N\) representation decomposition | Response matrix and sector eigenvalues require both. |
| PROP-0010 | Definitions of \(F\), uniform response, and \(g\) | Algebraic response bound depends on consistent normalization. |
| PROP-0011 | PROP-0006; differentiability of reduced-state response | Chain-rule scale covariance. |
| PROP-0012 | PROP-0005 plus weak-coupling derivative asymptotic | Sign comparison concerns the edge-response contrast. |

## 5. Cross-cutting proof obligations

1. **Definition lock:** Freeze exact definitions of \(F\), \(f\), \(\eta\), \(\alpha_N\), \(\mathcal G_N\), \(A,B,C\), \(\chi_k\), and the uniform/independent edge derivatives before writing dependent Lean theorems.
2. **Domain lock:** Record \(N\)-ranges claim by claim. In particular, PROP-0005 and endpoint asymptotics require \(N\ge4\) or \(N\ge3\) as specified; do not silently use a common domain.
3. **Entropy regularity:** Ground-state projector analyticity does not by itself imply differentiability of von Neumann entropy when reduced-state eigenvalues vanish. Each entropy derivative requires eigenvalue branch and remainder control.
4. **Asymptotic honesty:** A fixed-\(N\) remainder is not uniform in \(N\). Numerical finite-size agreement is not a proof of a uniform asymptotic.
5. **Source corrections:** Preserve verbatim source snapshots. Corrections belong in a separately versioned working manuscript and must be linked to the affected claim IDs.
6. **Proof-to-source correspondence:** For every formal theorem, record exact Lean declaration, full type, assumptions, imported axioms, source lines, and a reviewed argument that the Lean statement is equivalent to or sufficient for the manuscript claim.
7. **Counterexamples:** Search for counterexamples only within the exact stated domain. A failed search is not a proof.
8. **Independent review:** Internal derivations are not external referee review. Record reviewer independence and scope explicitly.

## 6. Priority order

1. **Resolve PROP-0012 source conflict**: specify the exact sign claim and decide the manuscript correction after a fresh independent check of the fixed-\(N\) weak-coupling derivation.
2. **Correct THM-0002 source argument**: change the mathematical exposition to the \(cI-H\) construction in a working copy; complete Lean existence of a nonnegative eigenvector at the top eigenvalue and transfer to the ground eigenspace.
3. **Close THM-0001 regularity gap**: choose and justify sufficient regularity for the stated remainder and branch expansion.
4. **Complete PROP-0009 source-citation and independent diagnostic review**: resolve the Lemma 5.1 mismatch and formalize the analytic eigenvalue/entropy estimates as feasible.
5. **Formalize the elementary claims**: PROP-0001/0002/0003/0004/0006/0007/0010/0011 after definitions and domains are locked.
6. **Formalize PROP-0005 in two independent parts**: finite permutation-representation algebra first; model-specific entropy differentiability and response derivatives second.
7. **Retire PROP-0008 as a duplicate through a registry migration**, preserving the audit trail.

## 7. Initial 14-layer routing

| Layer | Claims / obligations principally routed here |
|---|---|
| L-01 | All 15 records; prior-art search per distinct mathematical statement; duplicate and source-conflict classification |
| L-02 | All claims; exact statement/hypothesis/declaration correspondence; highest priority for every Lean-linked result |
| L-03 | PROP-0001, DEF-0001, PROP-0002, THM-0001, PROP-0003, PROP-0004, PROP-0005, PROP-0009, PROP-0011, PROP-0012 |
| L-04 | All formalizable claims; current partial modules listed in §2.2 |
| L-05 | THM-0002, THM-0001, PROP-0009, PROP-0012, and any central theorem whose independent proof route materially reduces shared-assumption risk |
| L-06 | PROP-0005 algebraic identities; PROP-0009/0012 exact finite-N diagnostics; other exact finite-dimensional spectral identities |
| L-07 | PROP-0009 and PROP-0012 independent implementations; cross-checks must have meaningfully distinct constructions |
| L-08 | Formal proof certificates and independent checking for L-04/L-05 outputs; provenance attestations alone do not satisfy mathematical certificate checking |
| L-09 | THM-0001 curvature and branch diagnostics; PROP-0009/0012 asymptotic regimes and conditioning |
| L-10 | Every claim's exact source lines, manuscript revision, Lean declaration, analytic proof, and evidence artifact |
| L-11 | All Lean axioms/imports, dependencies, toolchain, workflow, and trust boundary |
| L-12 | Reproducible builds, complete evidence packages, independent review; internal review must not be labelled external |
| L-13 | Joint satisfiability/non-vacuity of assumptions for conditional claims, especially THM-0001 and asymptotic claims |
| L-14 | Conditional on Paper A's intended target: assess TFIM idealizations and model-to-target claims; mark N/A only with an explicit scope justification |

## 8. Current overall assessment

- Paper A source-linked records: **15**.
- Latest claim-level audit updates (2026-11-21): **PROP-0002 tangent identities; PROP-0003 Picard multiplier/strict-inequality equivalence; and PROP-0004 dimensionless root-set invariance PASS by direct algebra under stated assumptions. PROP-0004's branch derivative remains conditional. Lean formalization remains open for all three.**
- Distinct theorem/proposition candidates after excluding one definition and one duplicate: **13 records**, with PROP-0012 retained as a source-conflict candidate.
- Claims with direct full manuscript-to-Lean correspondence established: **0**.
- Formalized partial support: **THM-0002 and limited auxiliary lemmas for PROP-0005/0009/0012; none yet establishes the full associated manuscript claim**.
- Analytic progress: **THM-0002 corrected PF proof reviewed PASS within finite-\(N\), \(h>0\) scope; PROP-0009 fixed-\(N\) strong-coupling derivation partially verified; PROP-0012 corrected local weak-coupling derivation internally reviewed PASS but source conflict remains**.
- Known source/math issues: **(i)** THM-0002 source uses the wrong shift direction; **(ii)** THM-0001 regularity is insufficient for the stated remainder; **(iii)** PROP-0005 omits explicit \(N\ge3\) domain; **(iv)** PROP-0008 duplicates PROP-0001; **(v)** PROP-0009 Lemma 5.1 citation is mismatched/unresolved; **(vi)** PROP-0012 supporting negative-sign derivation is superseded and its source assertion conflicts with corrected local asymptotics.
- **No conclusion is made that every Paper A claim is false.** Some are conditionally valid or analytically supported; several remain unproved or under-specified. The known issues above require correction or explicit qualification before the manuscript can be represented as fully verified.

**Final status:** `MATRIX_POPULATED_INITIAL_REVIEW_REQUIRED`; `PAPER_A_OVERALL_NOT_VERIFIED`.

---
