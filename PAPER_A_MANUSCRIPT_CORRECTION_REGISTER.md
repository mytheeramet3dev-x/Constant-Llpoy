# Paper A — Manuscript Correction Register

- **Document ID:** CL-PA-MCR-001
- **Version:** 0.1.0
- **Purpose:** A manuscript-facing list of corrections, qualifications, and source checks required before Paper A can be represented as publication-ready.
- **Authoritative frozen source:** `mytheeramet3dev-x/Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`.
- **Canonical manuscript:** the six revised section files listed in `MANUSCRIPT_SOURCE_MANIFEST.md`.
- **Related verification record:** `PAPER_A_CLAIM_BY_CLAIM_PROOF_OBLIGATION_MATRIX.md`.
- **Status:** CORRECTION REGISTER CREATED; NO UPSTREAM MANUSCRIPT FILES MODIFIED.

## 1. How to interpret this register

This document is about what the manuscript text may need to change. It is not a list of Lean tasks or CI tasks.

Priority labels:

- **P0 — Correct before relying on the claim:** the present wording/proof route contains a demonstrated mathematical or logical defect, or a material source conflict.
- **P1 — Required clarification or missing hypothesis:** the result may be correct, but the present statement is under-specified, overstates what follows, or cites the wrong support.
- **P2 — Editorial/structural cleanup:** duplication, notation, scope, or exposition that must be cleaned up for an accurate paper.

Disposition labels:

- **CHANGE REQUIRED:** the source as currently recorded should not be retained unchanged.
- **REVISE OR QUALIFY:** choose the corrected statement only after the specified proof check.
- **VERIFY BEFORE EDITING:** evidence is not yet sufficient to prescribe a mathematical change.
- **EDITORIAL:** no new mathematical theorem is implied.

Do not edit the frozen upstream source snapshot. Proposed changes must first be made in a separate, versioned manuscript working copy. Every accepted change must record affected section, claim ID, old statement, new statement, proof supporting the change, and reviewer.

## 2. P0 — Corrections required before relying on the current statement

### MCR-01 — Correct the Perron–Frobenius shift construction

- **Affected claim:** AS-ALPHA-A-THM-0002
- **Location:** §2.1, lines 3–17 in the frozen source.
- **Current issue:** The manuscript describes shifting the Hamiltonian by adding a sufficiently large positive multiple of the identity to make the matrix nonnegative. For the stated transverse-field Ising sign convention, adding (cI) does not reverse the negative off-diagonal spin-flip entries. That is not the nonnegative matrix needed for the Perron–Frobenius argument.
- **Required manuscript correction:** Replace the construction with (K=cI-H), with (c) chosen large enough that all diagonal entries of (K) are nonnegative. Since the off-diagonal spin-flip entries of (H) are nonpositive for (h>0), the corresponding off-diagonal entries of (K) are nonnegative. State that the positive off-diagonal support graph is the connected Boolean hypercube.
- **Required proof checks:** Prove entrywise nonnegativity; irreducibility/connectedness; existence of a nonzero nonnegative eigenvector for the spectral-radius eigenvalue; strict positivity and simplicity; and transfer from the largest eigenvalue of (K) to the ground eigenvalue of (H).
- **Do not overstate:** A proof that positivity propagates from an already supplied nonnegative eigenvector does not establish existence of that eigenvector.
- **Disposition:** **CHANGE REQUIRED.** The corrected (cI-H) route has an independent finite-dimensional proof review, but the complete Lean proof is still open.

### MCR-02 — Repair the regularity assumptions in the saddle-node theorem

- **Affected claim:** AS-ALPHA-A-THM-0001
- **Location:** §3.2, lines 96–165 in the frozen source.
- **Current issue:** The theorem states (C^2)-type regularity while using a cubic Taylor remainder (O(|delta x|^3)) and deriving a branch remainder (O(g-g_c)). In general, (C^2) regularity alone gives a second-order Peano remainder (o(|delta x|^2)), not a cubic (O(|delta x|^3)) bound.
- **Required manuscript correction:** Either (a) strengthen and justify the regularity assumption sufficiently to support the stated remainder (for example, a locally Lipschitz second derivative / suitable (C^{2,1}) condition, or (C^3) with an appropriate local bound), or (b) weaken the Taylor and branch remainder conclusions to the strongest statements actually proved under the existing assumptions.
- **Required proof checks:** Prove local branch existence and the stated expansion, not only a formal Taylor balance. Verify the sign of the curvature, the side of the bifurcation, and the coefficient in the square-root term.
- **Do not overstate:** The conditional abstract saddle-node theorem does not establish that the particular TFIM function satisfies its nondegeneracy and regularity hypotheses.
- **Disposition:** **CHANGE REQUIRED** to either the hypotheses or the conclusion, based on a complete proof.

### MCR-03 — Resolve the weak-coupling response sign conflict

- **Affected claim:** AS-ALPHA-A-PROP-0012 and the supporting Lemma 5.2 discussion
- **Location:** §4.4.3, line 134, and the cross-reference to §5 / Lemma 5.2.
- **Current issue:** The original supporting Lemma 5.2 negative-sign derivation was superseded by its audit after an order-(r^2) coherence contribution was omitted. The corrected fixed-finite-(N) weak-coupling derivation gives
  [
  B-C=\frac{J}{8h^2}\ln\!\frac{2(N-2)}{N-1}
  +O_N\!\left(\frac{J^2}{h^3}[1+|\ln(J/h)|]\right),
  ]
  which has a positive leading coefficient for fixed (N\ge4) and sufficiently small (J/h>0), provided the model-specific differentiated remainder is established.
- **Required manuscript correction:** Do not retain the negative-sign Lemma 5.2 conclusion as established. Reconcile the phrase “distinct scaling and opposite-sign response characteristics” with the exact response quantity it is intended to describe. If it refers to (B-C), revise/remove the negative-sign assertion and update the cross-reference. If it refers to another response quantity, define that quantity and prove its sign separately.
- **Required proof checks:** Re-derive the weak-coupling reduced-state blocks with the coherence term included; prove the differentiated entropy remainder for the actual model; compare with full-Hilbert-space high-precision calculations; and limit the conclusion to fixed finite (N\ge4) and sufficiently small positive (J/h) unless a uniform result is proved.
- **Do not overstate:** A positive local weak-coupling leading coefficient does not prove (B-C>0) globally for all couplings or all system sizes.
- **Disposition:** **CHANGE REQUIRED for the superseded negative-sign proof; REVISE OR QUALIFY the §4.4.3 prose after the response quantity is made explicit.** The corrected local asymptotic is internally reviewed, but its model-specific differentiated remainder is not yet fully closed.

## 3. P1 — Statements requiring qualification, missing hypotheses, or citation repair

### MCR-04 — State the domain of the edge-space decomposition

- **Affected claim:** AS-ALPHA-A-PROP-0005
- **Location:** §5.2, lines 42–93.
- **Current issue:** The stated dimensions (1), (N-1), and (N(N-3)/2) for the three edge-space sectors require an explicit size range. The standard three-sector decomposition as stated requires (N\ge3); for smaller (N), the decomposition/dimensions need separate treatment.
- **Required manuscript correction:** Add the exact condition (N\ge3) to the proposition and all dependent statements, or state and prove separate low-(N) cases.
- **Required proof checks:** Verify the sector decomposition, dimensions, response eigenvalues, and (chi_1-chi_2=(N-2)(B-C)) under the stated domain. Keep the exact algebraic identity distinct from any conjectured sign of (B-C).
- **Disposition:** **REVISE OR QUALIFY.**

### MCR-05 — Repair the strong-coupling cross-reference

- **Affected claim:** AS-ALPHA-A-PROP-0009
- **Location:** §4.4.2, lines 103–120.
- **Current issue:** The section's citation to Lemma 5.1 is not supported by the located source: the inventoried Lemma 5.1 concerns the (B-C) response sign, not the stated (mathcal G_N(x)) strong-coupling function and derivative expansion.
- **Required manuscript correction:** Replace the citation with the actual derivation/source for the (mathcal G_N) asymptotics, or add a correctly numbered lemma that proves precisely the function and derivative expansions cited in §4.4.2.
- **Required proof checks:** Reconcile the fixed-(N\ge4) expansion and derivative remainder; do not infer a uniform-in-(N) result from fixed-(N) estimates. The derivative remainder must be proved, not obtained by informally differentiating a big-O term.
- **Disposition:** **CHANGE REQUIRED** for the citation; the asymptotic conclusion remains **ANALYTIC-PARTIAL**, not fully verified.

### MCR-06 — Make the threshold proposition explicitly conditional

- **Affected claims:** AS-ALPHA-A-PROP-0001 and AS-ALPHA-A-PROP-0008
- **Location:** §2.5, lines 159–206.
- **Current issue:** The infimum definition and interior-attainment argument support a conditional threshold/tangency result. They do not, without additional assumptions on (mathcal G_N), prove existence of roots above threshold, exactly two roots, or a global bifurcation diagram.
- **Required manuscript correction:** State separately: (i) the pointwise subcritical exclusion under (mathcal G_N(x)>0); (ii) equality/tangency if the infimum is attained at an interior point and the required differentiability holds; and (iii) any supercritical root-existence/count statement only under separately stated global shape, continuity, endpoint, and nondegeneracy hypotheses.
- **Required proof checks:** Verify the definitions of (F,f,eta,g,h), positivity and nonzero denominators, and the exact domain of (x).
- **Disposition:** **REVISE OR QUALIFY** wherever the prose suggests stronger global conclusions than the conditional argument proves.

### MCR-07 — Separate root-set invariance from differentiable branch claims

- **Affected claim:** AS-ALPHA-A-PROP-0004
- **Location:** §4.2, lines 20–34.
- **Current issue:** Substitution along (g=\gamma\alpha_N h) can establish that the fixed-point root equation is independent of (h), assuming the dimensionless function and threshold are independent of (h). It does not by itself establish a differentiable selected root branch or justify (partial x_*/\partial h=0) without branch regularity/selection assumptions.
- **Required manuscript correction:** State the root-set invariance as the primary result. Present the derivative-zero statement only as a conditional corollary under a well-defined differentiable branch (or a suitable implicit-function theorem hypothesis).
- **Disposition:** **REVISE OR QUALIFY** if the derivative statement is currently unconditional.

### MCR-08 — Clarify the scope of the Picard stability criterion

- **Affected claim:** AS-ALPHA-A-PROP-0003
- **Location:** §3.3, lines 192–225.
- **Current issue:** The equivalence (|T'(x_*)|<1\iff -2h<F_x<0) is a linear multiplier criterion under the stated fixed-point and differentiability assumptions. It should not be presented as a global convergence theorem, and (F_x<0) alone is insufficient for the full criterion.
- **Required manuscript correction:** Explicitly label it as a local linear stability criterion. State the fixed-point condition, (h>0), differentiability, and the full two-sided inequality. Explain that the borderline cases (|T'|=1) need higher-order analysis.
- **Disposition:** **REVISE OR QUALIFY** if broader convergence language is used.

### MCR-09 — State the positive-field restriction for scale covariance

- **Affected claims:** AS-ALPHA-A-PROP-0006 and AS-ALPHA-A-PROP-0011
- **Location:** §2.3, lines 71–111; §5.4, lines 127–131.
- **Current issue:** The rescaling (H(J,h)=h\widetilde H(J/h,1)) and the (h^{-1}) derivative scaling require (h>0). At (h=0), (J/h) is undefined and the positive-rescaling spectral argument does not apply.
- **Required manuscript correction:** State (h>0) explicitly in each proposition and corollary. Distinguish spectral-projector invariance from a phase-dependent eigenvector statement; the latter requires a nondegenerate ground state or an explicit phase convention.
- **Required proof checks:** Derive the reduced-state/mutual-information identity and the edge-response chain-rule factor from the precise dimensionless dependence.
- **Disposition:** **REVISE OR QUALIFY** wherever the domain or eigenvector qualification is omitted.

### MCR-10 — State the zero-coupling endpoint and entropy regularity separately

- **Affected claim:** AS-ALPHA-A-PROP-0007
- **Location:** §2.4, lines 148–155.
- **Current issue:** The product ground state at zero interaction supports zero mutual information and the trivial fixed point. It does not automatically establish differentiability of entropy at that endpoint, where reduced-state eigenvalues may vanish.
- **Required manuscript correction:** Keep the exact endpoint statement separate from any derivative/analytic-continuation claim at (x=0). Add a one-sided regularity statement only if supported by an entropy eigenvalue/remainder proof.
- **Disposition:** **VERIFY BEFORE EDITING**, unless the current prose explicitly infers endpoint differentiability from the product-state identity.

### MCR-11 — Make the uniform-response normalization explicit

- **Affected claim:** AS-ALPHA-A-PROP-0010
- **Location:** §5.1, lines 17–24.
- **Current issue:** The derivative with respect to a uniform change of all edge couplings must not be confused with the derivative with respect to one independent edge coordinate. The inequality depends on the exact definition and normalization of (F_J), (g), and (I_{12}).
- **Required manuscript correction:** Define the uniform coupling path and its derivative convention explicitly. State the algebraic bound and its non-implication separately; do not infer a negative response from (F_J<0) alone.
- **Disposition:** **VERIFY BEFORE EDITING** until the exact derivative convention is reconciled with the definitions in §§3–5.

## 4. P2 — Structural and editorial cleanup

### MCR-12 — Mark PROP-0008 as duplicate or merge it with PROP-0001

- **Affected claim:** AS-ALPHA-A-PROP-0008
- **Location:** §2.5, lines 197–206; compare PROP-0001.
- **Current issue:** The subcritical exclusion statement repeats the subcritical portion of PROP-0001.
- **Required manuscript correction:** Either remove the duplicate proposition and retain the statement once under PROP-0001, or explicitly make it a named corollary with a reference to PROP-0001 and no repeated independent proof.
- **Disposition:** **EDITORIAL.** Preserve claim-ID traceability in the audit registry even if the publication-facing numbering changes.

### MCR-13 — Lock notation and parameter definitions across §§2–5

- **Affected claims:** DEF-0001, PROP-0001–0004, PROP-0010–0011.
- **Current issue:** Dependent results require consistent definitions of (F), (f), (eta), (alpha_N), (mathcal G_N), (g), (h), and the distinction between uniform and edgewise derivatives.
- **Required manuscript correction:** Add or consolidate a notation/definitions paragraph. State all domains and positivity assumptions once, then reference them precisely. Check every use of (x_c), (g_c), (eta_c), and (h) for consistent parameter substitution.
- **Disposition:** **EDITORIAL / MATHEMATICAL CLARIFICATION.**

## 5. Correction order

The manuscript should be revised in this order:

1. **MCR-01 / THM-0002:** correct the Perron–Frobenius operator shift.
2. **MCR-02 / THM-0001:** resolve the regularity-versus-remainder mismatch.
3. **MCR-03 / PROP-0012:** remove the superseded negative-sign proof and settle the exact meaning of the “opposite-sign” prose.
4. **MCR-05 / PROP-0009:** repair the strong-coupling citation and derivative-remainder support.
5. **MCR-06 through MCR-11:** clarify hypotheses, domains, and scope of conditional statements.
6. **MCR-04:** make the edge-space dimension range explicit.
7. **MCR-12 and MCR-13:** remove duplication and harmonize notation.

The ordering is a work priority, not a claim that later items are mathematically less important.

## 6. Manuscript change-control protocol

For each proposed correction:

1. Copy the frozen six-section manuscript into a separate working directory/repository or branch. Do not edit the immutable source snapshot.
2. Create a correction record with: MCR ID, claim ID, source section and lines, old text, proposed new text, mathematical rationale, proof artifact, and reviewer.
3. Prove the revised statement under its explicitly stated assumptions before marking it accepted.
4. Update the Claim-by-Claim Proof Obligation Matrix and the manuscript-to-artifact traceability record.
5. Run the relevant formal and computational checks on the revised source revision.
6. Re-run the affected 14-layer obligations; a manuscript change invalidates prior correspondence evidence for the changed claim.
7. Preserve a redline/diff and a new source manifest with commit and blob hashes.
8. Only after review should a correction be proposed upstream. This register itself does not authorize changes to `Absolute_Sym`.

## 7. What this register does not claim

- It does not claim that all Paper A results are false.
- It does not claim that all listed corrections have already been applied.
- It does not turn an internal derivation or numerical check into an external peer review.
- It does not treat a passing Lean build or provenance workflow as proof of manuscript correctness.
- It does not assert uniform-in-(N) asymptotics from fixed-(N) results.
- It does not assert that all 14 verification layers can or should have a PASS status when a layer is genuinely not applicable; any N/A disposition requires a documented scope justification.

**Overall disposition:** Paper A needs a controlled manuscript revision before it can be described as fully verified. The highest-priority source corrections are the Perron–Frobenius shift, the saddle-node regularity/remainder mismatch, and the weak-coupling sign/source conflict.
