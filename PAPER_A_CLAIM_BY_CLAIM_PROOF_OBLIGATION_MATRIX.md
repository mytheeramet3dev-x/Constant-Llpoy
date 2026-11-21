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
| AS-ALPHA-A-THM-0001 | Local saddle-node expansion | FRESH REVIEW CONFIRMS REGULARITY GAP: C2 only gives Peano o(|dx|^2), not the claimed cubic remainder; stronger O(dg) branch correction requires additional quantitative smoothness (e.g. C3 or C2,1) and branch proof. Leading square-root coefficient conditionally consistent; model curvature G''(xc)<0 remains open; global root count not implied. No Lean build. Fresh report: audits/paper-a/AS-ALPHA-A-THM-0001_FRESH_REGULARITY_GAP_REVIEW.md |
| **AS-ALPHA-A-PROP-0003** — exact Picard local-attractivity criterion (§3.3 lines 192–225) | For \(T(x)=\frac gh\mathcal G_N(x)\), the multiplier is \(T'(x_*)=1+F_x/h\). Linear stability is \(|T'(x_*)|<1\), equivalently \(-2h<F_x<0\). | Fixed point \(T(x_*)=x_*\); \(h>0\); differentiability of \(\mathcal G_N\) near \(x_*\); scalar one-dimensional iteration. | (1) Differentiate \(T\). (2) Use the exact definition of \(F_x\) to derive the multiplier identity. (3) Prove equivalence of inequalities using \(h>0\). (4) Distinguish linear contraction/attraction from nonlinear cases where \(|T'|=1\). (5) Do not infer stability from \(F_x<0\) alone away from the saddle-node. | Semantic audit: **NO_DIRECT_FORMALIZATION**. No direct Lean theorem for the Picard map or exact multiplier criterion. | **NOT-FORMALIZED.** Formalize the elementary scalar calculus result, then separately prove that the physical model's map meets its hypotheses. |
| **AS-ALPHA-A-PROP-0004** — root independence along dimensionless scaling ray (§4.2 lines 20–34) | Along \(g=\gamma\alpha_Nh\), the root equation becomes \(x=\gamma\alpha_N\mathcal G_N(x)\), independent of absolute scale \(h\); claim is root-by-root, not global uniqueness. | \(h>0\), \(\alpha_N\) independent of \(h\), fixed \(\gamma\), well-defined \(\mathcal G_N\); if using derivative notation \(\partial x_*/\partial h\), a differentiable selected root branch must exist. | (1) Substitute the scaling ray into the fixed-point equation. (2) Prove the root set is identical for all \(h>0\). (3) If asserting derivative zero, state a branch-selection/regularity condition or derive it from an implicit-function theorem with nonzero derivative. (4) Do not infer uniqueness or branch selection. | Semantic audit: **NO_DIRECT_FORMALIZATION**. No direct Lean theorem for the fixed-point root-set invariance. | **NOT-FORMALIZED.** Prove set-level invariance first; treat differentiable branch notation as a separate conditional corollary. |

### B. Hamiltonian, scaling, and zero-coupling claims

| Claim | Source statement and mathematical content | Required hypotheses / domain | Proof obligations | Existing evidence and formal correspondence | Disposition / next action |
|---|---|---|---|---|---|
| **AS-ALPHA-A-**THM-0002** — Perron–Frobenius ground-state nondegeneracy (§2.1 lines 3–17) | Finite \(N\), \(h>0\): nondegeneracy route for TFIM ground state using \(K=cI-H\), nonnegative entries and connected hypercube support. | Finite \(N\ge1\), finite real edge couplings, \(h>0\), computational basis; \(c\) above all diagonal energies. | (1) Verify encoded Hamiltonian. (2) \(K=cI-H\) nonnegative. (3) Positive support is single-spin-flip hypercube. (4) Construct nonzero nonnegative eigenvector at maximal eigenvalue (or apply scoped PF existence theorem). (5) Prove strict positivity and simplicity. (6) Transfer maximal \(K\) eigenvalue to ground eigenvalue of \(H\). | Fresh source/Lean review: structural encoding, entrywise nonnegativity, hypercube connectivity, Hermitian property, scalar-shift eigenvector equivalence, conditional strict positivity and conditional simplicity chain are present. A quadratic-form absolute-value lemma supports variational existence, but no inspected declaration constructs a nonnegative maximal eigenvector or closes final ground-state transfer. No Lean build run. Report: audits/paper-a/AS-ALPHA-A-THM-0002_PF_GROUND_STATE_NONDEGENERACY_AUDIT.md. | **ANALYTIC-PASS (corrected finite-dimensional proof route) / FORMALIZATION-INCOMPLETE.** Fresh review of the corrected working proof confirms the mathematical PF route: (K=cI-H) is entrywise nonnegative, hypercube support is connected for finite (N\ge1) and (h>0), PF gives a simple positive top eigenvector, and the top eigenvalue of (K) transfers to the ground eigenvalue of (H). Frozen manuscript §2.1 still has the shift-sign wording to correct. Lean still lacks the reviewed nonnegative top-eigenvector existence and final ground-transfer closure; no build was run. Review: `audits/paper-a/AS-ALPHA-A-THM-0002_CORRECTED_PF_PROOF_CLOSURE_REVIEW.md`. |
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
| **AS-ALPHA-A-PROP-0012** — weak-coupling response source conflict (§4.4.3) | Corrected leading asymptotic predicts positive physical \(B-C\) for sufficiently small \(r=J/h>0\), fixed \(N\ge4\); prior Lemma 5.2 sign conflicts with retained coherence. | Fixed finite \(N\ge4\); weak coupling; uniform reference; independent edge perturbations. | Leading coefficient and branch bookkeeping analytically supported at fixed \(N\), conditional; source reconciliation and formalization/build remain open. | Leading coefficient \(\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}\). IV-9 conditionally integrates even small branch \(O_N(r^4)\) and entropy derivative \(O_N(r^4(1+|\ln r|))\), via shared-amplitude closure (not the rejected parity argument). IV-10 reconciles odd positive branch \(q=r^2Q_+(u)+O_N(r^3)\), edge derivatives, and entropy contrast remainder \(O_N(r^3(1+|\ln r|))\); even branches do not worsen that remainder under IV-9 hypotheses. Report: \`audits/paper-a/AS-ALPHA-A-PROP-0012_IV10_ODD_POSITIVE_BRANCH_AND_IV9_RECONCILIATION.md\`. | **SOURCE-CONFLICT / ANALYTIC-PARTIAL; NOT-VERIFIED.** Local weak-coupling sign is supported conditionally; frozen-source conflict, Lean, and global sign remain open. |
| **AS-ALPHA-A-PROP-0013** — near-critical upper-branch limits (§4.4.1) | Along the locally selected upper saddle-node branch, \(x_*(\gamma)\to x_c\), \(T'(x_*)\to1\), and \(F_J(x_*)\to0\) as \(\gamma\to1^+\). | Local nondegenerate saddle-node assumptions; \(\mathcal G_N'\) continuous at \(x_c\); tangent identity \(\alpha_N\mathcal G_N'(x_c)=1\); upper local branch selection. | (1) Obtain the local branch from the saddle-node theorem. (2) Use \(x_*(\gamma)\to x_c\). (3) Apply continuity of \(\mathcal G_N'\) and the tangent identity to the multiplier. (4) Use \(F_J=T'-1\) to obtain the derivative limit. (5) Keep this local limit distinct from global continuation. | Fresh analytic audit: all three limits follow directly and conditionally from the local branch and tangent identity. No model-specific numerical scan or Lean declaration checked. Report: audits/paper-a/AS-ALPHA-A-PROP-0013_NEAR_CRITICAL_BRANCH_LIMITS_AUDIT.md. | **ANALYTIC-VERIFIED (conditional local implication); NOT-LEAN-VERIFIED.** Does not establish existence/uniqueness for all \(\gamma>1\), branch continuation, or absence of branch exchanges. |

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

| **AS-ALPHA-A-PROP-0014** — strong-coupling upper-branch limits (§4.4.2) | Conditional on fixed-​N asymptotics and selected positive branch, \(x_*(\gamma)\sim\gamma\alpha_N\ln2\), \(T'(x_*)\to0\), and \(F_J(x_*)\to-1\). | Fixed finite \(N\ge4\); \(\alpha_N>0\); fixed-point equation on selected branch; \(\mathcal G_N(x)\to\ln2>0\); derivative asymptotic \(\mathcal G_N'(x)=2/((N-1)^2x^3)+O_N(\ln x/x^5)\); branch bounded away from zero; branch continuation/selection conditions. | (1) Establish global branch selection/continuation. (2) Prove mutual-information asymptotic and differentiated remainder. (3) Infer \(x_*\to\infty\) and asymptotic linear growth from fixed point. (4) Substitute derivative asymptotic into multiplier. (5) Deduce \(F_J=T'-1\to-1\). (6) Check source Lemma 5.1 citation and avoid thermodynamic-limit inference. | Fresh audit verified the limit implications algebraically conditional on the fixed-\(N\) asymptotics and branch assumptions. The asymptotic expansions were not independently fully reproduced; earlier PROP-0009 follow-up remains partial; Lemma 5.1 citation mismatch unresolved; no Lean build. Report: audits/paper-a/AS-ALPHA-A-PROP-0014_STRONG_COUPLING_BRANCH_LIMITS_AUDIT.md. | **ANALYTIC-PARTIAL.** Conditional consequences are sound; complete source asymptotics, derivative remainder, and global branch prerequisites remain unverified. |
| **AS-ALPHA-A-PROP-0015** — branch-domain qualification (§4.4.3) | Upper local branch has \(x_+>x_c\) near threshold; global \(x_*(\gamma)\ge x_c\) for all \(\gamma\ge1\) is explicitly conditional on global continuation; lower local root repelling. | Local saddle-node regularity/nondegeneracy and parameter proximity; global continuation/no reversing turning points or branch exchanges for global extension; response-sign claim depends on PROP-0012. | (1) Derive local branch inequalities from square-root normal form. (2) Check lower-branch \(F_x>0\) and \(T'>1\) locally. (3) Separate local from global continuation. (4) Evaluate response-sign evidence against corrected weak-coupling audit. | Audit confirms local implications conditionally; manuscript correctly qualifies global extension, which remains unproved. Response-sign statement remains in source conflict after PROP-0012. No global numerical continuation or Lean build. Report: audits/paper-a/AS-ALPHA-A-PROP-0015_GLOBAL_BRANCH_DOMAIN_QUALIFICATION_AUDIT.md. | **PARTIAL.** Local results conditionally sound; global continuation unproved; response-sign assertion open/conflicted. |
| **AS-ALPHA-A-PROP-0016** — uniform-response positivity numerical evidence trace (§5.1) | Manuscript reports numerical \(\chi_0=\partial I_{12}/\partial J_*>0\) on investigated physical branches for \(N=4,6,8,10,20\), and excludes \(N=50\) near-critical values below the spectral-gap reliability threshold. | Raw data, parameter grid, reproduction script, numerical error/reliability bounds, and provenance directly linked to this claim; distinguish positivity from branch slope and iteration stability. | (1) Locate original data/script. (2) Reproduce \(\chi_0\) across the stated parameter points. (3) Verify gap/reliability cutoff. (4) Record convergence/error controls. (5) Keep numerical observation separate from analytic theorem and PROP-0010's conditional bound. | Source labels this as numerical observation, not theorem. Frozen verification workspace did not locate linked raw data/script/grid/error estimates for this specific claim. No rerun was performed. Report: audits/paper-a/AS-ALPHA-A-PROP-0016_UNIFORM_RESPONSE_POSITIVITY_EVIDENCE_TRACE_AUDIT.md. | **NUMERICAL-CLAIM / NOT-INDEPENDENTLY-REPRODUCED.** Traceability gap, not counterexample. |
| **AS-ALPHA-A-PROP-0017** — \(B-C>0\) evidence consistency (§5.3) | Existing CSV gives positive values and dense/reduced cross-checks for \(N=4,6,8,10\); source still labels sign conjectural. Weak-coupling corrected conditional sign is consistent with table but not global proof. | Reproduction provenance (coupling/branch points, scan coverage, finite-difference details, uncertainties, command/script); global sector-ordering lemma; resolve old Lemma 5.2 source conflict. | (1) Validate CSV values and solver cross-check columns. (2) Recover missing parameter provenance. (3) Compare with PROP-0012 corrected weak-coupling sign. (4) Keep exact sector identity separate from conjectured ordering. (5) Do not infer global sign, stability, or locality. | Four tabulated N values positive with dense/reduced discrepancies at roughly \(10^{-11}\) or smaller. CSV lacks point/grid provenance needed for independent reproduction. Global sign theorem remains open. Report: audits/paper-a/AS-ALPHA-A-PROP-0017_B_MINUS_C_SIGN_EVIDENCE_CONSISTENCY_AUDIT.md. | **NUMERICAL EVIDENCE / GLOBAL SIGN OPEN.** |

## Supplemental audit update — PROP-0012 odd positive branch (2026-11-21)

A new independent audit closes the differentiated remainder for the **odd positive eigenbranch and leading entropy contrast only**, within fixed finite N >= 4 and weak coupling. Report: `audits/paper-a/AS-ALPHA-A-PROP-0012_ODD_POSITIVE_BRANCH_DIFFERENTIATED_REMAINDER_AUDIT.md`. Report commit: `0c3b68ae6deea8a9c9c747c92e303e2016fcf800`.

The positive odd branch is constructed after factoring the analytic block by r^2; its leading positive eigenvalue is simple at the uniform point, allowing a local analytic branch and differentiated expansion. The zero branch is handled separately by nonnegativity/interior-minimum and is not assigned a uniform O(r^3) estimate in edge variables. The one-site and positive odd-branch terms yield the corrected physical-coupling leading contrast

\[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}+O_N\!\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right),
\]
conditional on closure of the even-block small eigenbranch contribution.

**Do not promote full PROP-0012 to PASS.** The even-block small eigenbranch is retained at conservative O_N(r^3) in the checked working proof. A conversational O_N(r^4) claim has not yet been supported by an independently committed derivation and is not accepted in this matrix update. Full entropy remainder/source reconciliation, global sign, and Lean formalization/build remain open.


## Supplemental audit update — PROP-0012 even-block shared-amplitude Schur cancellation (2026-11-21)

A new environment-resolved even-block review is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_EVEN_BLOCK_SHARED_AMPLITUDE_SCHUR_CANCELLATION_REVIEW.md`, commit `34c3dfbcddb2f2c199248db4f191da7e47461a4b`. It derives exact reduced-block entry sums and identifies a candidate stronger cancellation: the empty-environment contribution to X and S shares the exact ground-state amplitude c_12, while nonempty environments first contribute at higher perturbation orders. Conditional fixed-N analytic order bounds then suggest Schur remainder and small even eigenbranch O_N(r^4), including first edge derivatives.

This is **ANALYTIC-PARTIAL / candidate stronger bound**, not upgraded to full pass. The pair-flip perturbation-order lemma for all amplitudes and edge derivatives still needs a fully closed proof. No Lean formalization/build, source reconciliation, or global B-C sign theorem is claimed.


## Supplemental audit update — PROP-0012 pair-flip amplitude-order lemma (2026-11-21)

The previously outstanding fixed-N pair-flip amplitude-order argument has now been recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_PAIR-FLIP_AMPLITUDE_ORDER_LEMMA_AUDIT.md`. Report commit: `df748501e02fa1a7d18d88b8a1a8ca082953406d`; fetched report blob SHA: `c288692fd8ea208d7fe6747f70138d031533a3cb`.

The paper-level induction uses the analytic eigenvector Taylor recursion and pair-flip support: order n can reach only sets produced by at most n pair flips, so amplitudes for even flip sets E have no Taylor terms below |E|/2. Differentiating edge variables changes coefficients but does not lower r powers. This closes the specific order-lemma gap at analytic argument level for fixed finite N, with no uniform-in-N constants claimed.

**Status remains ANALYTIC-PARTIAL, NOT FORMALLY VERIFIED.** The recursion/support induction has not been mechanically checked; exact source Hamiltonian/convention reconciliation is still required. No Lean formalization/build, full entropy remainder integration, or global B-C sign theorem is claimed. The new lemma alone does not upgrade PROP-0012 to PASS.


## Supplemental audit update — PROP-0012 even-block O(r^4) integration (2026-11-21)

The pair-flip amplitude-order argument has now been integrated with the exact environment-summed even-block entries, Schur cancellation, determinant identity for the small eigenvalue, and first edge derivatives. Report: `audits/paper-a/AS-ALPHA-A-PROP-0012_EVEN_BLOCK_R4_INTEGRATION_REVIEW.md`; commit `38d4498ba0aa287ad4f4518d83be7a27e77d169d`; fetched report blob SHA `68f34f61e0c3ad1bff2ba1333868c1aa4db2a50e`.

The paper-level argument closes the even-block small eigenbranch and first edge derivatives at O_N(r^4). The entropy derivative is O_N(r^4(1+|ln r|)) subject to the explicit positive-branch scale check or zero-branch treatment. This is an analytic integration result, **conditional on exact source/Hamiltonian convention and branch reconciliation**; it is not a source-wide or formal pass.

Full PROP-0012 remains OPEN: source reconciliation, branch-scale verification against the source, all entropy branches/remainder integration, and Lean formalization/build remain outstanding. No global B-C sign theorem is claimed.


## Supplemental audit update — PROP-0012 source reconciliation access/definitions (2026-11-21)

A source-access/definition audit was recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_SOURCE_RECONCILIATION_ACCESS_AND_DEFINITION_AUDIT.md`, commit `18e829bd2962c0b5a1af7b9aa10d4ea77c031b66`. The accessible current-main manuscript Section 5.2 confirms the definitions (B=\partial_{J_{13}}I_{12}) (adjacent edge) and (C=\partial_{J_{34}}I_{12}) (disjoint edge), and Section 5.3 labels the sign (B-C>0) a numerically supported conjecture. The current-main Hamiltonian/sign convention is structurally consistent with the working TFIM derivation.

**Frozen-source reconciliation BLOCKED:** fetch attempts for the audit branch and frozen commit returned 404/NOT FOUND; the current-main manuscript is not treated as a substitute for the frozen source. Therefore no source-wide reconciliation or status promotion is claimed. PROP-0012 remains OPEN; no Lean formalization/build or global sign theorem is claimed.


## Supplemental audit update — PROP-0012 complete entropy-branch bookkeeping (2026-11-21)

A branch-by-branch entropy derivative audit is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_COMPLETE_ENTROPY_BRANCH_BOOKKEEPING_AUDIT.md`, commit `e3425299d481e291ba4ed653d2246f4f6ad4c9c7`. It explicitly uses trace normalization to cancel the constant `-1` terms in entropy derivatives, then checks the even-block large eigenbranch: `lambda_L=1-O_N(r^2)`, `lambda_L'=O_N(r^2)`, so the trace-cancelled contribution `-(ln lambda_L)lambda_L'` is `O_N(r^4)`. The even small branch remains conditional on the pair-flip/Schur estimates and positive-scale or zero-branch treatment; the odd positive branch, odd zero branch, and one-site branches are accounted for by the existing reports.

**Status:** complete entropy branch bookkeeping at the claimed fixed-N orders, **conditional analytic closure only**. The report does not upgrade PROP-0012 to PASS. Frozen-source access/reconciliation, verifying the branch-scale hypotheses against the frozen source, independent verification of the amplitude recursion, Lean formalization/build, and any global `B-C>0` theorem remain open.


## Supplemental audit update — PROP-0012 leading logarithmic coefficient / constant cancellation (2026-11-21)

A separate algebraic cross-check is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_LEADING_LOG_COEFFICIENT_AND_CONSTANT_CANCELLATION_CHECK.md`, commit `5aa3f21d48e0644315b457114d3865ea52dc6954`. It explicitly verifies that the `+1` constants in derivatives of `-lambda ln lambda` cancel by trace normalization `sum(lambda')=0`; after this cancellation the leading two-site entropy contrast is `-(r^2/8)ln(q)`, not a term retaining an isolated constant. Combining with one-site entropy gives `(r^2/8)ln(q/p)`, where `q/p=2(N-2)/(N-1)>1`, and physical-coupling conversion reproduces the corrected leading formula.

**Disposition:** algebraic cross-check PASS conditional on the previously audited branch expansions and derivative estimates. This is not an independent source reconciliation, formal verification, or global sign proof; PROP-0012 remains OPEN.


## Supplemental audit update — PROP-0012 independent leading-coefficient re-derivation (2026-11-21)

A separate leading-order re-derivation is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_INDEPENDENT_LEADING_COEFFICIENT_REDERIVATION.md`, commit `023e389a7d0461efed0690e5c8105842e2ec3b80`. It recomputes the pair amplitude from the TFIM matrix element/energy gap, the one-site small eigenvalue, the odd-block positive eigenvalue and its adjacent-edge derivative via the eigenvector formula, the logarithmic ratio, and the physical-coupling conversion. It agrees with the leading coefficient previously obtained.

**Disposition:** independent leading-coefficient algebra PASS. This is not a full independent eigenbranch/remainder/source proof. Even-block and all-branch remainder estimates remain conditional, source reconciliation and Lean formalization/build remain open, and PROP-0012 remains OPEN.


## Supplemental audit update — PROP-0012 independent Hamiltonian/leading-coefficient checks IV-1 to IV-6 (2026-11-21)

A consolidated report was added at `audits/paper-a/AS-ALPHA-A-PROP-0012_IV1-IV6_INDEPENDENT_HAMILTONIAN_AND_N4_CHECK.md`, report commit `96b3a02f03b4f4b234132f85e0dfc721b173d8f8`, fetch-back blob SHA `7dd89a90d44331d277989e871e770445d0431e21`. It independently rebuilds the Hamiltonian normalization and pair-flip amplitude, the odd two-site block and positive eigenvalue, adjacent-edge eigenvalue derivative, leading entropy contrast, physical coupling conversion, and the N=4 specialization (ratio q/p=4/3).

**Disposition:** IV-1 through IV-6 PASS for the specified leading-order algebraic reconstruction. The N=4 specialization is not a separate remainder proof. Full higher-order entropy remainder closure, frozen-source reconciliation, Lean formalization/build, and global `B-C>0` remain OPEN. PROP-0012 stays ANALYTIC-PARTIAL / OPEN; no status promotion is made.


## Supplemental audit update — PROP-0012 IV-7 working-proof remainder-status reconciliation (2026-11-21)

Audit report `audits/paper-a/AS-ALPHA-A-PROP-0012_IV7_WORKING_PROOF_REMAINDER_STATUS_RECONCILIATION.md`, commit `819b5c116ff4ef55f910c0646b83545d6b286fc5`. This found a documentation/provenance mismatch: the current working derivation states the even-block Schur branch at conservative (O_N(r^3)), while the later environment-resolved integration report claims conditional (O_N(r^4)) closure. These are not contradictory by themselves; the stronger estimate has not yet been integrated into the working proof and is conditional on entry/amplitude-order/derivative checks.

**Disposition:** mismatch FOUND; mathematical contradiction NOT ESTABLISHED. Keep the conservative working-proof order unless the stronger environment-resolved entry derivation is explicitly reconciled and independently checked. PROP-0012 remains OPEN / ANALYTIC-PARTIAL.


## Supplemental audit update — PROP-0012 IV-8 direct environment-sum reconstruction (2026-11-21)

A fresh derivation reconstructs the even-block entries directly from exact environment sums, isolates the empty-environment shared amplitude, and independently checks the nonempty-environment tail orders and Schur cancellation. Report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV8_DIRECT_ENVIRONMENT_SUM_RECONSTRUCTION.md`; report commit `87c85cf01f3167575921d53431cf9ef15350bd03`; fetch-back blob SHA `ae65288901ee26fbebb2abd535998f056ae232ba`.

**IV-8 disposition:** PASS for the algebraic reconstruction, conditional on the pair-flip Taylor-support and first-edge-derivative order lemma, fixed finite N, local analyticity, and source/convention agreement. The shared-amplitude argument gives Schur remainder and small eigenbranch O_N(r^4), with entropy derivative O_N(r^4(1+|ln r|)) under the positive-scale check or separate zero-branch treatment. This addresses the earlier derivation-provenance gap, but does not independently mechanize the amplitude recursion or source reconciliation. The working proof's conservative O_N(r^3) even-branch bound is now ready for an explicit provenance/integration update, but has not yet been edited in this IV-8 step. Full PROP-0012 remains OPEN / ANALYTIC-PARTIAL; no Lean formalization/build, source-wide pass, uniform-in-N bound, or global B-C sign theorem is claimed.


## IV-11 status correction — Full differentiated entropy contrast

**IV-11: FAIL-TO-CLOSE / REOPENED.** Independent scalar entropy derivative checking identified an additive constant discrepancy in the IV-10 claim that chain-rule constants cancel. The one-site binary entropy derivative is exactly \(H'(p)=\ln((1-p)/p)\), with no standalone \(-1\), while the positive eigenbranch derivative of \(-q\ln q\) is \(-(1+\ln q)q'\), containing an explicit \(+1\). With the currently reported edge-direction coefficients, a candidate combination retains an additive \(+1\) inside the leading bracket; this is not accepted as a corrected theorem because the full source-convention and both-site derivative reconstruction is still incomplete.

- Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV11_FULL_ENTROPY_CONTRAST_CLOSURE_REOPENED.md`
- Frozen manuscript source retrieval/reconciliation remains blocked.
- Do not cite the IV-10 leading coefficient as confirmed until the complete contrast is recomputed.
- PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**. No Lean formalization/build was performed.


## IV-12 status — site-by-site and branch-by-branch reconstruction

**IV-12 PASS for reconstruction from the current working derivative ledger, conditional on its analytic expansions and source convention.** The one-site binary entropy derivative is \(H'(p)=\ln((1-p)/p)\) (no standalone \(-1\)); the odd positive branch derivative of \(-q\ln q\) contains \(-(1+\ln q)q'\). The combined candidate therefore retains an additive \(+1\) in the leading bracket:
\[
B-C=\frac{J}{8h^2}\left[1+\ln\frac{2(N-2)}{N-1}\right]+O_N\left(\frac{J^2}{h^3}|\ln(J/h)|\right).
\]
For fixed \(N\ge4\), the bracket is positive. This is only a local weak-coupling candidate under current expansions; frozen-source convention reconciliation, complete proof of analytic remainder lemmas, Lean formalization/build, and global positivity remain open. Do not claim PROP-0012 verified.

- Report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV12_SITE_BRANCH_DERIVATIVE_RECONSTRUCTION.md`


## IV-13 status — adversarial check of corrected coefficient

**IV-13 PASS only as an adversarial consistency check against the current working ledger; no internal counterexample found.** The $1/8$ derivative normalization is consistent with the pair-flip gap $4h$ under the stated Hamiltonian convention; leading $(N-1)$ and $(N-2)$ counts match the current ledger; logarithmic combination is algebraically correct and retains the additive $+1$; dimensional remainder conversion is correct conditional on the joint differentiated expansion; and the candidate bracket is positive for fixed $N\ge4$. This is not an independent full reduced-matrix derivation. Frozen-source convention reconciliation, analytic lemma proof, Lean formalization/build, and global positivity remain open.

- Report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV13_ADVERSARIAL_COEFFICIENT_CHECK.md`


## Supplemental audit update — PROP-0012 IV-14 direct reduced-matrix reconstruction (2026-11-21)

A direct reconstruction of the leading one-site and two-site reduced-matrix entries from perturbative ground-state amplitudes is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_IV14_DIRECT_REDUCED_MATRIX_RECONSTRUCTION.md`. Report commit: `6034f734cd02050edf69ac45ea18ec9115f71be9`; fetched report blob SHA: `5c9dd2637a5bc042f400159665dd287df01b563c`.

**IV-14 disposition:** PASS for leading-order direct reconstruction: one-site small eigenvalue coefficient `(N-1)/16`, odd-block positive eigenvalue `(N-2)/8`, and adjacent-edge derivative coefficient `1/8` are reproduced from direct environmental tracing/Gram matrix entries. The even-block shared-amplitude rank-one empty-environment cancellation is confirmed structurally, but this pass does not independently mechanize the amplitude recursion, prove all higher-order branch remainders, or verify the small branch logarithmic scale.

**Status remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.** Frozen-source reconciliation, full higher-order remainder closure, Lean formalization/build, and global `B-C` sign remain open.


## Supplemental audit update — PROP-0012 IV-15 independent higher-order even-block reconstruction (2026-11-21)

The adversarial higher-order environment-tail and shared-amplitude Schur cancellation review is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_IV15_INDEPENDENT_HIGHER_ORDER_EVEN_BLOCK_RECONSTRUCTION.md`. Report commit: `b3fe6ca71279863e3bf26a0d2eb56a6a82fa39ad`; fetched report blob SHA: `ab41e569e0ec56cbef3c2a7227ad786b859e2db0`.

**IV-15 disposition:** Conditional analytic order-counting PASS. The empty-environment rank-one term uses the exact shared amplitude `c_12 so second-order overlapping paths modifying `c_12=a_12+O_N(r^2)` do not spoil its cancellation. Nonempty environment tails have conditional orders `R_L=O_N(r^2)`, `R_X=O_N(r^3)`, `R_S=O_N(r^4)`; their Schur residual and first edge derivatives are therefore `O_N(r^4)`. No O(r^2) or O(r^3) counterexample was found under the pair-flip Taylor-support/derivative lemma.

This is not mechanized; the amplitude support induction, entropy logarithmic-scale closure, frozen-source reconciliation, Lean formalization/build, and global `B-C` sign remain open. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.


## Supplemental audit update — PROP-0012 IV-16 pair-flip Taylor-support induction (2026-11-21)

The fixed-finite-N pair-flip Taylor-support induction, including first edge derivatives, is recorded at `audits/paper-a/AS-ALPHA-A-PROP-0012_IV16_PAIR_FLIP_TAYLOR_SUPPORT_INDUCTION.md`. Report commit: `4f605a3926ede9b89f1176339d63aa0aa28fa087`.

The support argument uses the fact that each interaction insertion flips exactly two sites: after n insertions, the flip set is a symmetric difference of n pairs and therefore contains at most 2n sites. Scalar eigenvalue/normalization recursion terms multiply prior amplitudes and do not introduce new sites. Differentiating edge variables changes path weights but not flip-set transitions or r-order. This supports the conditional orders `c_E=O_N(r^{|E|/2})` and `c_{E∪{1,2}}=O_N(r^{(|E|+2)/2})), and hence IV-15 environment-tail orders.

**IV-16 disposition:** analytic argument-level support/order PASS under the locally analytic eigenvector Taylor setup; not mechanically checked and not Lean-formalized. No uniform-in-N bounds. Frozen-source reconciliation, complete entropy-branch closure, formalization/build, and global `B-C` sign remain open. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-17 adversarial Taylor recursion audit (2026-11-21)

The scalar eigenvalue corrections, normalization/gauge terms, excited-space degeneracy, edge differentiation, and pair-flip transition support were adversarially reviewed at `audits/paper-a/AS-ALPHA-A-PROP-0012_IV17_ADVERSARIAL_RECURSION_AUDIT.md`. Report commit: `a21bfbf7c2456ed8beb5bb4d72b7caddffada8be`.

No support/order counterexample was found under the locally analytic finite-dimensional ground-state setup. Scalar energy coefficients and normalization factors cannot introduce flip sites; excited-state degeneracy does not obstruct the simple isolated ground-state projector; edge differentiation preserves pair-transition support and the r-order of insertions. This remains an argument-level PASS—not a mechanically checked normalized recurrence or Lean proof. No uniform-in-N estimates or status promotion are made. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-18 entropy branch logarithmic remainder (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV18_ENTROPY_BRANCH_LOG_REMAINDER_AUDIT.md`. IV-18 identifies a crucial distinction: an eigenvalue bound \(\lambda=O_N(r^4)\) alone does **not** imply the edge derivative \(\lambda_u=O_N(r^4)\), nor does it alone control \(\lambda_u\ln\lambda\). With a joint branch factorization \(\lambda=r^4a(u,r)\), bounded \(a_u\), and a positive lower bound on \(a\), the entropy derivative is \(O_N(r^4(1+|\ln r|))\). If the leading coefficient vanishes, pointwise nonnegativity forces the derivative to vanish at that interior point, but a uniform neighborhood estimate still requires analytic factorization/vanishing-order control. The complete trace-normalized entropy derivative cancels additive constants using \(\sum_i\lambda_i'=0\); this cancellation must not be applied branch-by-branch in isolation.

**IV-18 disposition:** conditional pass for the positive-scale branch; zero-leading-coefficient neighborhood control remains a gap until its actual branch factorization is checked. This audit does not claim frozen-source reconciliation, a mechanically checked recursion, Lean formalization/build, or global \(B-C>0\). PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.


## Supplemental audit update — PROP-0012 IV-19 zero-branch factorization & uniform-neighborhood audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV19_ZERO_BRANCH_FACTOR_UNIFORM_NEIGHBORHOOD_AUDIT.md`. IV-19 tests whether the positive-scale entropy derivative estimate can be extended across a zero-leading-coefficient branch. The bound \(0\le\lambda\le Cr^4\) alone is insufficient to infer derivative or logarithmic control. For \(\lambda=r^4a(u,r)\), bounded \(a_u\) and a positive lower bound on \(a\) give the conditional \(O(r^4(1+|\ln r|)\) estimate. At a zero of the leading coefficient, the factor's vanishing order and neighborhood behavior must be proved; pointwise derivative vanishing at an interior minimum does not close a uniform neighborhood estimate. Trace normalization is not a substitute for branch-local or aggregate cluster control.

**IV-19 disposition:** positive-scale estimate conditional; zero-leading-coefficient uniform neighborhood remains OPEN; no counterexample to the exact target formula established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-20 aggregate small-spectral-cluster entropy derivative audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV20_AGGREGATE_SMALL_CLUSTER_ENTROPY_DERIVATIVE_AUDIT.md`. IV-20 evaluates aggregating a small spectral cluster to avoid branch-label issues. Decomposition \(S_I=-q\ln q+qH(\mu)\), where \(q\) is cluster mass and \(\mu\) is the normalized cluster spectrum, separates the mass term from internal entropy. Bounds \(q=O(r^4)\), or \(H(\mu)\le\ln m\), alone do not control derivatives: \(q_u\) and internal \(H_u\) need separate estimates. Aggregation removes dependence on eigenvalue labels for the entropy value, but does not close the uniform derivative estimate near internal zero eigenvalues. A smooth isolated cluster projector remains conditional on a proven spectral gap and derivative bounds.

**IV-20 disposition:** cluster mass/value bounds are valid but insufficient for the derivative; uniform cluster entropy derivative remains OPEN; no counterexample to the exact target proposition established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-21 spectral projector gap & cluster boundary audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV21_SPECTRAL_PROJECTOR_GAP_CLUSTER_BOUNDARY_AUDIT.md`. IV-21 examines the cluster-projection route. For an isolated spectral cluster, a Riesz contour formula for the projector derivative yields resolvent estimates whose constants depend on contour separation/gap. Uniform control therefore requires a demonstrated uniform gap and controlled contour. Gap collapse can invalidate differentiability of a fixed-rank cluster projector or make its derivative bounds diverge; crossing the chosen cluster boundary is distinct from internal eigenvalue relabeling. No uniform gap/projector derivative has been established for the target derivation, and this is a proof-route obstruction, not a counterexample to the proposition.

**IV-21 disposition:** local isolated-cluster differentiability conditional; uniform gap and projector derivative OPEN; cluster boundary crossings must be controlled or avoided; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-22 gap-free full-spectrum entropy derivative audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV22_FULL_SPECTRUM_ENTROPY_DERIVATIVE_AUDIT.md`. IV-22 reviews the label-free full-matrix derivative. For positive-definite normalized \(\rho\), the identity \(S_u=-\operatorname{Tr}(\rho_u\ln\rho)\) follows after the normalization trace cancels the additive identity term. This avoids branch labels and cluster projector gaps but does not eliminate logarithmic weights: \(\ln\rho\) is unbounded as eigenvalues approach zero, and \(\|\rho_u\|\) alone does not imply a uniform entropy derivative bound. Boundary/rank-deficient cases require limiting justification and additional low-spectrum matrix-element control or verified cancellation.

**IV-22 disposition:** full-spectrum derivative identity PASS on positive-definite states; gap-free route identity-level PASS; uniform low-spectrum logarithmic estimate OPEN; target remainder not closed; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-23 low-spectrum matrix-element suppression audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV23_LOW_SPECTRUM_MATRIX_ELEMENT_SUPPRESSION_AUDIT.md`. In the instantaneous eigenbasis for positive-definite \(\rho\), the entropy derivative reads \(S_u=-\sum_i(\rho_u)_{ii}\ln\lambda_i\), with the normalization identity \(\sum_i(\rho_u)_{ii}=0\). This reveals that low-spectrum diagonal derivative suppression or a verified weighted cancellation is needed to offset logarithmic weights. The eigenvalue size alone, a generic norm bound on \(\rho_u\), or trace normalization alone does not establish the needed rate. Pair-flip support/order results have not been bridged to the exact low-spectrum diagonal response in this basis; that connection remains OPEN.

**IV-23 disposition:** identity-level PASS; low-spectrum diagonal response suppression and uniform logarithmic remainder OPEN; no counterexample to exact proposition established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-24 kernel/tangent-cone & rank-deficient boundary audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV24_KERNEL_TANGENT_CONE_RANK_DEFICIENT_AUDIT.md`. IV-24 checks whether PSD tangent constraints alone imply low-spectrum response suppression. For a two-sided differentiable PSD path at a rank-deficient base point, the kernel-to-kernel block of the first derivative must vanish; one-sided tangent paths impose positivity on that block. However cross-block derivatives need not vanish: the PSD rank-one path \(\rho(t)=\begin{pmatrix}1&t\\t&t^2\end{pmatrix}\) has nonzero cross-block derivative at \(t=0\). These local positivity facts do not supply a uniform weak-coupling order for the low-spectrum diagonal response or entropy derivative.

**IV-24 disposition:** tangent-cone facts PASS; shortcut from positivity to quantitative response suppression FAILS (not implied); uniform rank-deficient entropy derivative remains OPEN; no counterexample to exact proposition established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-25 model-specific selection-rule bridge audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV25_SELECTION_RULE_BRIDGE_AUDIT.md`. IV-16/17 pair-flip Taylor support/order is a conditional fixed-finite-N analytic result in the computational configuration basis. It does not itself bound the transformation into the instantaneous low-spectrum eigenbasis: eigenvector/projector mixing and near-degeneracy require spectral separation or basis-invariant cluster estimates. The audited records do not derive a bridge from support/order to the low-spectrum diagonal response entering the entropy derivative.

**IV-25 disposition:** prior pair-flip support/order premise PASS within scope; bridge to low-spectrum response NOT ESTABLISHED; eigenbasis mixing and log-weighted remainder OPEN; no proposition counterexample established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-26 reduced-density construction/partial-trace audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV26_REDUCED_DENSITY_PARTIAL_TRACE_AUDIT.md`. Rechecked the exact Gram partial-trace identity, one-site leading probability/edge derivative, odd-block environment parity and leading index convention, and even-block shared-amplitude rank-one cancellation. The displayed IV-14 leading formulas are internally consistent under the stated basis convention. The exact even-block residual Schur quantity is nonnegative for \(L>0\); its claimed \(O_N(r^4)\) size and differentiated size still depend on amplitude/tail estimates and were not re-proved here. Normalization corrections and higher-order derivative remainders remain open for independent closure.

**IV-26 disposition:** exact Gram partial trace PASS; leading one-site and odd-block reconstruction PASS within perturbative scope; shared-amplitude cancellation PASS algebraically; higher-order normalization/tail/remainder closure OPEN; no counterexample to exact proposition; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-27 normalization/truncation-remainder audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV27_NORMALIZATION_TRUNCATION_REMAINDER_AUDIT.md`. Exact normalized amplitudes satisfy the norm identity, but a truncated perturbative vector is not exactly normalized; scalar normalization preserves support while changing amplitude coefficients and potentially differentiated remainders. Joint analyticity permits edge differentiation of controlled Taylor remainders only with uniform neighborhood/differentiability bookkeeping. The current derivation's edge-differentiated amplitude/tail estimates remain conditional and are not mechanized. Low-branch size alone does not close its entropy derivative.

**IV-27 disposition:** normalization identity PASS; support preservation under scalar normalization PASS; differentiated truncation remainders and normalization-to-log-entropy closure OPEN; no target counterexample established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-28 edge-derivative remainder uniformity audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV28_EDGE_DERIVATIVE_REMAINDER_UNIFORMITY_AUDIT.md`. Cauchy's estimate confirms that a holomorphic remainder uniformly bounded by \(C_N|r|^k\) on a common complex edge-variable disk yields a first edge derivative of the same \(r\)-order, with constant scaled by disk radius. Pointwise real \(O(r^k)\) alone does not imply same-order derivative. The working derivation states joint finite-N analyticity and differentiated expansions, but the complete quantitative neighborhood, common-radius constants, and every amplitude-recursion remainder were not independently certified in IV-28.

**IV-28 disposition:** Cauchy derivative principle PASS conditionally; pointwise-to-derivative shortcut FAILS; complete uniform remainder ledger OPEN; spectral/logarithmic remainder OPEN; no target counterexample established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-29 ground-state projector/gap-neighborhood audit (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV29_GROUND_STATE_PROJECTOR_GAP_NEIGHBORHOOD_AUDIT.md`. The uncoupled \(H_0=-h\sum_i\sigma_i^x\), \(h>0\), has a unique ground state and gap \(2h\). Standard finite-dimensional perturbation theory gives persistence of an isolated ground eigenvalue and analyticity of its Riesz projector in a sufficiently small parameter neighborhood; the working derivation states this fixed-finite-N analytic setup. Explicit perturbation norm/radius, quantitative gap lower bound across the common remainder neighborhood, and uniform-in-N control are not supplied/independently audited. This validates the projector principle but not every downstream remainder.

**IV-29 disposition:** unperturbed unique ground/gap PASS; analytic projector principle and local gap persistence PASS conditional on small finite-N neighborhood; explicit common neighborhood for all remainders OPEN; no counterexample established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-30 remainder ledger cross-audit/dependency graph (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV30_REMAINDER_LEDGER_CROSS_AUDIT_DEPENDENCY_GRAPH.md`. The dependency chain is ground-state analytic projector → amplitude support/order → partial-trace blocks → small eigenvalues → entropy derivatives → final edge-response difference. No explicit circular equality was identified in the inspected working derivation; however, pair-flip order and uniform C1/holomorphic remainder bounds are upstream premises, not independently validated by downstream uses. Schur cancellation is algebraically valid but order bounds depend on amplitude orders. Low-spectrum entropy derivative closure and independent leading-coefficient reconstruction remain open.

**IV-30 disposition:** structural dependency map PASS; no explicit circularity identified in inspected source; full amplitude recursion, common remainder neighborhood, small-spectrum entropy derivative closure, and independent leading coefficient remain OPEN. No target counterexample and no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.


## Supplemental audit update — PROP-0012 IV-31 independent leading-coefficient reconstruction (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV31_LEADING_COEFFICIENT_INDEPENDENT_RECONSTRUCTION_AUDIT.md`. From the displayed leading branches \(p=(N-1)r^2/16\), \(q=(N-2)r^2/8\), and leading edge-13 derivatives \(p_{1,u}=q_u=r^2/8\), the leading logarithmic mutual-information derivative difference gives \(\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}\), after conversion from dimensionless edge \(u\) to physical \(J_e\). The regular entropy \(-1\) terms cancel if these derivative coefficients match. This differs from the previous candidate bracket containing an additional \(+1\); that extra term is not supported by this leading-branch calculation and requires full block bookkeeping/reconciliation. This is a material coefficient discrepancy, not a theorem or counterexample.

**IV-31 disposition:** coefficient reconciliation OPEN; higher/zero branches, complete regular terms, and uniform remainder closure OPEN; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**. Do not use either coefficient as proven.


## Supplemental audit update — PROP-0012 IV-32 exact edge-direction entropy bookkeeping (2026-11-21)

Audit report: `audits/paper-a/AS-ALPHA-A-PROP-0012_IV32_EXACT_EDGE_DIRECTION_ENTROPY_BOOKKEEPING_AUDIT.md`. Using the displayed leading branches, edge 13 contributes \(r^2/8(-\ln p-1)\) from site 1 and subtracts \(r^2/8(-\ln q-1)\) from the positive odd two-site branch; site 2 is higher order at this direction. The regular \(-1\) pieces cancel, giving \(r^2/8\ln(q/p)\), with \(q/p=2(N-2)/(N-1)\). Edge 34 has no displayed order-\(r^2\) contribution (one-site and odd-branch derivatives are stated \(O_N(r^3)\)); other branches remain conditional. After physical derivative conversion, the corrected leading candidate is \(\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}\), without the prior extra \(+1\).

**IV-32 disposition:** displayed-branch bookkeeping PASS; extra \(+1\) not supported and cancels at this level; full low-spectrum and remainder closure OPEN; no counterexample established; no Lean verification. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
