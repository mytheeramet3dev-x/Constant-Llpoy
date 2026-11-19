# Paper A — Consolidated Manuscript Correction and Execution Plan

- **Document ID:** CL-PA-CCEP-001
- **Version:** 0.1.0
- **Repository:** `mytheeramet3dev-x/Constant-Llpoy`
- **Working branch:** `paper-a-mcr01-pf-redline`
- **Frozen upstream repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Frozen upstream branch:** `paper-a-interval-audit-2026-11-14`
- **Frozen upstream commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Status:** CONSOLIDATED EXECUTION PLAN / NO UPSTREAM EDITS / NOT A VERIFICATION CERTIFICATE
- **Related records:**
  - `PAPER_A_MANUSCRIPT_CORRECTION_REGISTER.md` (MCR-01–MCR-13)
  - `working/paper-a/PAPER_A_CROSS_SECTION_AUDIT_SECTIONS_02_TO_05.md` (XSEC-01–XSEC-14)
  - `working/paper-a/PAPER_A_FULL_MANUSCRIPT_INTEGRATION_AUDIT.md`
  - `working/paper-a/PAPER_A_SOURCE_AUTHORITY_RECONCILIATION.md`
  - `working/paper-a/PAPER_A_TECHNICAL_AUDIT_CORRECTION_ADDENDUM.md`
  - `PAPER_A_CLAIM_BY_CLAIM_PROOF_OBLIGATION_MATRIX.md`

## 1. Purpose and governing rule

This document consolidates manuscript corrections and cross-section dependencies into one controlled execution plan. It does not replace the frozen source, the claim matrix, or the individual technical audits. It resolves duplicate tracking and assigns each issue a single execution key.

**No manuscript statement is to be changed merely to make it agree with an audit note.** Each mathematical change must be supported by a checked derivation or proof under explicit hypotheses. If the evidence is incomplete, the item remains open and the manuscript must not overstate it.

The six revised section files at the frozen upstream commit remain the audit baseline. The upstream repository is immutable for this workflow. All proposed edits must first be made in a separate working manuscript copy on Constant Llpoy.

## 2. Consolidation rules: duplicates and scope

The following records overlap and must not be counted as independent defects:

| Consolidated key | Existing records | Consolidation |
|---|---|---|
| C-01 | MCR-01; XSEC-03; Technical Addendum §3 | One Perron–Frobenius sign/operator correction |
| C-02 | MCR-02; XSEC-06; Technical Addendum §2; Section 3 audit | One regularity/remainder issue, plus separate model-specific fold hypotheses |
| C-03 | MCR-03; XSEC-11; Section 5 audit; Technical Addendum §4 | One weak-coupling sign/source conflict |
| C-04 | MCR-04; XSEC-10; Technical Addendum §5(3) | One representation-domain clarification; distinguish existence of a zero-dimensional sector from nonzero-sector range |
| C-05 | MCR-05; XSEC-12; Section 4 audit | One strong-coupling citation and derivative-proof issue |
| C-06 | MCR-06; XSEC-05; XSEC-04 | Threshold definition, positivity, attainment, and global root count are related but separate proof obligations |
| C-07 | MCR-07 | Root-set invariance versus differentiable branch selection |
| C-08 | MCR-08 | Picard local multiplier criterion versus global convergence |
| C-09 | MCR-09 | Positive-field domain and scale covariance |
| C-10 | MCR-10 | Zero-coupling endpoint versus entropy regularity |
| C-11 | MCR-11; XSEC-01; XSEC-02; XSEC-09 | Derivative notation and uniform-path/edgewise chain rule |
| C-12 | MCR-12 | Duplicate claim/proposition cleanup |
| C-13 | MCR-13 | Global notation and parameter dictionary |
| C-14 | XSEC-07; XSEC-08 | Local branch inheritance versus global continuation |
| C-15 | XSEC-13; Section 4 and Section 5 audits | Do not infer edge-response sign from uniform-path strong-coupling asymptotics |
| C-16 | XSEC-14; Source Authority Reconciliation | Manifest authority versus actual TeX build input |

XSEC-04, XSEC-05, and the global root-count part of MCR-06 are not interchangeable: positivity permits the ratio argument; attainment permits a critical point; global shape and endpoint information are needed for root counts.

## 3. Master correction register

Priority meanings:
- **P0:** do not rely on the current claim/proof route until corrected or explicitly withdrawn.
- **P1:** required hypothesis, derivation, notation, domain, citation, or scope clarification.
- **P2:** editorial/traceability cleanup.

Evidence classes:
- **Demonstrated defect:** a concrete mathematical, logical, or source mismatch has been identified.
- **Missing proof/hypothesis:** claim may be true, but present evidence does not establish it.
- **Scope/notation:** ambiguity or overstatement requiring precise formulation.
- **Editorial/source governance:** document/build consistency, not itself a mathematical theorem.

| Key | Priority / class | Affected area | Required action | Acceptance gate |
|---|---|---|---|---|
| C-01 | P0 / demonstrated defect | §2.1, PF ground-state simplicity | Replace the invalid (H+cI) nonnegative-matrix construction by (K=cI-H); prove entrywise nonnegativity, hypercube connectivity/irreducibility, PF eigenvector existence and simplicity, and transfer to the ground eigenvalue | Written finite-dimensional proof reviewed; Lean correspondence checked separately |
| C-02 | P0 / demonstrated defect + missing proof | §3.2 and dependent §4 limits | Under (C^2), use a Peano (o(|u|^2)) remainder and prove the local fold/branch conclusion at that regularity; alternatively prove stronger model regularity before retaining cubic or (O(g-g_c)) remainders | Correct theorem statement, proof of branch existence and coefficient, and model-specific regularity evidence |
| C-03 | P0 / demonstrated source conflict + open analysis | §4.4.3, Lemma 5.2, §5 response sign | Remove the superseded negative-sign argument and unsupported “opposite-sign” wording unless another precisely defined quantity is proved; retain corrected weak-coupling coefficient only as a candidate until differentiated remainder is controlled | Re-derivation includes missing coherence; differentiated remainder proved; scope fixed in finite (N); independent numerical comparison recorded |
| C-04 | P1 / scope | §5.2 representation decomposition | State decomposition domain (Nge3); explicitly note (dim V_2=0) at (N=3); use (Nge4) if all three sectors are required to be nonzero | Representation statement and eigenvalue formulas checked for stated range |
| C-05 | P1 / source and proof | §4.4.2 strong-coupling asymptotics | Replace mismatched Lemma 5.1 citation; prove function and derivative expansions separately; keep fixed-finite-(N) scope; never differentiate a big-O estimate without a derivative theorem | Correct source/lemma, derivation, and derivative remainder proof |
| C-06 | P0 / missing hypotheses | §§2.5–3 threshold/fold | Separate pointwise subcritical exclusion, infimum attainment, interior tangency, nondegeneracy, supercritical root existence, and exactly-two-root claims | Each proposition states only what follows from its explicit hypotheses; global root count separately proved or withdrawn |
| C-07 | P1 / scope | §4.2 scale invariance | State root-set invariance separately from a differentiable selected-root branch and any (partial x_*/partial h=0) conclusion | Branch-selection and differentiability hypotheses supplied for derivative statement |
| C-08 | P1 / scope | §3.3 Picard stability | Present (|T'(x_*)|<1iff -2h<F_x<0) as a local linear multiplier criterion; do not infer global convergence | Exact derivative convention and local hypotheses stated |
| C-09 | P1 / domain | §§2.3, 5.4 scale covariance | State (h>0); distinguish projector invariance from eigenvector phase convention | All scaling identities carry explicit positive-field domain |
| C-10 | P1 / endpoint regularity | §2.4 | Keep product-state endpoint and (mathcal G_N(0)=0) separate from differentiability/analyticity at rank-changing endpoint | Entropy eigenvalue/remainder analysis supports any one-sided regularity claim |
| C-11 | P1 / notation and chain rule | §§3–5 | Define (F^{(x)}), (F^{(J)}); state (F^{(x)}_x=hF^{(J)}_J); state (mathcal G_N'(x)=hchi_0) where differentiability and symmetry apply; distinguish (chi_0) from a single edge partial | One notation dictionary and a checked chain-rule derivation used consistently |
| C-12 | P2 / editorial | §2.5 claim numbering | Merge or cross-reference duplicate PROP-0008 / PROP-0001 without losing claim traceability | Claim ledger maps old IDs to final publication numbering |
| C-13 | P1/P2 / notation governance | §§2–5 | Lock (N,h,J,J_{ij},x,g,eta,mathcal G_N,f,F,alpha_N,x_c,g_c,A,B,C,chi_k) and derivative conventions | Notation table and all dependent statements reconciled |
| C-14 | P1 / dependency | §§3–4 | Make near-critical limits depend only on the valid local branch theorem; prove global continuation and (x_*(gamma)	oinfty) separately | Local and global statements have separate hypotheses and proofs |
| C-15 | P1 / non-implication | §§4–5 | Do not use uniform-path strong-coupling asymptotics to infer the sign of (B-C) or independent-edge response sectors | Each response claim has its own derivative calculation and evidence |
| C-16 | P0 / release governance | Manifest, integrated Markdown, TeX generator | Resolve whether six revised sections or integrated Markdown are canonical; update assembly/build policy only after explicit owner decision | Deterministic build consumes the declared canonical source; manifest, source hashes, generated TeX and provenance agree |

## 4. Canonical derivative and parameter conventions

The working manuscript must use the following convention unless a mathematically justified alternative is approved:

[
x=J/h,qquad eta=g/h,qquad h>0,
]
[
f(x;eta)=etamathcal G_N(x)-x,
]
[
F^{(x)}(x,g,h)=gmathcal G_N(x)-hx=h f(x;eta),
]
[
F^{(J)}(J,g,h)=gI_{12}(J,h)-J.
]

At (J=hx),

[
F^{(x)}_x=hF^{(J)}_J.
]

For the symmetric edge-response map, if it is differentiable and permutation-equivariant,

[
mathcal G_N'(x)=hchi_0,
]
[
chi_0=A+2(N-2)B+rac{(N-2)(N-3)}2C,
]
[
F^{(J)}_J=gchi_0-1,qquad T'(x)=gchi_0.
]

The inequality (F^{(J)}_J<0) implies (chi_0<1/g), not (chi_0<0). The identity
[
chi_1-chi_2=(N-2)(B-C)
]
orders two response eigenvalues when the sign of (B-C) is known; it does not itself establish stability or a sign theorem.

## 5. Execution sequence and decision gates

### Phase 0 — Freeze and provenance (no manuscript edits)

1. Preserve the frozen source commit and section blob hashes.
2. Preserve all current audit files and their hashes.
3. Confirm the Constant Llpoy working branch is the only edit target.
4. Keep the source-authority decision open until the owner explicitly selects a canonical policy.

**Gate 0:** all proposed work traces to the frozen source and no upstream files are changed.

### Phase 1 — Resolve demonstrated mathematical defects

1. C-01 Perron–Frobenius operator correction.
2. C-02 saddle-node regularity/remainder correction.
3. C-03 weak-coupling sign conflict and removal/qualification of unsupported prose.

For each item, produce:
- source excerpt and claim ID;
- corrected statement;
- derivation/proof artifact;
- assumptions and exact domain;
- counterchecks or numerical comparison where relevant;
- independent review status.

**Gate 1:** no corrected statement is accepted merely because it is plausible or compiles.

### Phase 2 — Close threshold and local-branch logic

1. C-06 positivity, threshold infimum, attainment, interior minimizer, curvature, and global root-count obligations.
2. C-14 local branch versus global continuation.
3. C-10 endpoint entropy regularity.
4. C-07 scale-invariant root set versus selected differentiable branch.

**Gate 2:** every global statement is either proved under explicit hypotheses or weakened/removed. Do not infer exactly two roots from the threshold definition alone.

### Phase 3 — Reconcile response-sector mathematics

1. C-04 representation domain.
2. C-11 derivative conventions and uniform-path chain rule.
3. C-05 strong-coupling function and derivative proof/citation.
4. C-15 separation of uniform-path and independent-edge asymptotics.
5. Reassess the global (B-C) sign claim without converting numerical evidence or a local asymptotic into a theorem.

**Gate 3:** response-sector claims have explicit differentiability, equivariance, and dimension assumptions; each sign claim has its own proof.

### Phase 4 — Formalization and independent verification mapping

1. Update the claim-by-claim matrix to point to the exact corrected statement and proof artifact.
2. Formalize definitions and elementary identities only after the mathematical statement is stable.
3. For each Lean theorem, record exact correspondence to the manuscript statement, all assumptions, and any admitted axioms.
4. Run targeted Lean checks and the full project build only when the relevant working source is ready.
5. Record independent builder/reviewer identity and environment; if not provisioned, label that layer NOT ACTIVE / NOT VERIFIED.
6. Re-evaluate the 14-layer obligations individually. N/A requires a scope justification; PASS must never be forced.

**Gate 4:** Lean compilation, mathematical proof review, manuscript correspondence, and independent reproducibility remain separate statuses.

### Phase 5 — Manuscript working copy and release build

1. Create a new versioned working manuscript from the frozen six-section source.
2. Apply only corrections that passed the preceding gates.
3. Maintain a redline, change log, claim mapping, and new source manifest.
4. Resolve C-16 before generating release TeX.
5. Rebuild from the declared canonical source and verify byte/source provenance.
6. Only then prepare an upstream change proposal for explicit authorization.

**Gate 5:** no release or upstream update while canonical source and build input disagree.

## 6. Required status vocabulary

Use only precise statuses:
- **OPEN:** obligation identified, not yet resolved.
- **PROPOSED:** correction text exists but is not accepted.
- **PROVED-ANALYTIC:** mathematical proof reviewed for the stated assumptions and domain.
- **FORMALIZED-PARTIAL:** some formal declarations exist but correspondence or assumptions remain incomplete.
- **LEAN-CHECKED:** exact target builds in a recorded environment; not by itself a mathematical verification claim.
- **INDEPENDENTLY-REVIEWED:** a reviewer independent of the derivation has checked the stated artifact.
- **VERIFIED:** use only when the relevant mathematical, formal, correspondence, provenance, and independent-review obligations are all satisfied for that claim.
- **NOT APPLICABLE:** accompanied by a written scope justification.
- **NOT VERIFIED:** default overall paper status until all required obligations are satisfied.

Do not use a single green CI badge as shorthand for all verification dimensions.

## 7. Current disposition

- The correction register and cross-section audit are consolidated; they are not all resolved.
- C-01, C-02, and C-03 are the first mathematical correction gates.
- C-06 is a central theorem-scope gate: the threshold infimum does not automatically yield an attained fold or global two-root theorem.
- C-11 is the main cross-section notation/derivative bridge.
- C-16 blocks release TeX generation until source authority and build input are reconciled.
- The frozen upstream manuscript remains unchanged.
- No Lean build, CI pass, or new independent external review is claimed by this plan.

**Overall status: PAPER A — NOT VERIFIED.**
