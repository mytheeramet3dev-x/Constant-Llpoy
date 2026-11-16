# Initial Extraction Ledger
**Project:** Constant Llapoy  
**Document ID:** CL-EL-001  
**Version:** 0.4.2  
**Status:** Paper A six-section structural scan and independent extraction review completed with issues; mathematical proof review remains open

---

## 1. Summary

The initial extraction pass has inspected the upstream Absolute Symmetry repository and pinned separate branch revisions for Paper A, Paper D, and Paper A1.

| Paper | Source material inspected | Initial Constant Llapoy records | Extraction state |
|---|---|---:|---|
| A | Six revised sections plus supplementary/supporting-source reconciliation | 15 | 14 candidates + 1 SOURCE_CONFLICT; 15/15 extraction-reviewed with issues |
| D | Nine structured theorem/proposition source files | 9 | Candidate/source records; no integrated manuscript |
| A1 | Stage A1-1 theorem statement file plus 17-entry epistemic ledger | 22 | TRANSCRIBED; independent review pending |
| **Total** | — | **46** | **NOT COMPLETE** |

The fifteen Paper A records include one definition, two theorem candidates, eleven initial proposition/claim candidates, and one additional source-conflict claim. PROP-0008 is a duplicate/overlap of a subclaim in PROP-0001. The nine Paper D records include two theorem-source records and seven proposition/theorem-source records. The five Paper A1 records correspond to the five formal theorem statements in Stage A1-1.

## 2. Paper A extraction findings

Source: `Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`.

The integrated Paper A manuscript explicitly says the six revised section files are authoritative. Initial records were created from:
- Section 2.5: conditional exact threshold scaling.
- Section 3.1: interior critical point definition and tangent constraint.
- Section 3.2: conditional local saddle-node normal form.
- Section 3.3: exact Picard local-attractivity criterion.
- Section 4.2: root-by-root scale independence along the dimensionless ray.
- Section 5.2: edge-response sector decomposition and exact `chi_1-chi_2=(N-2)(B-C)` identity.

Records:
- `AS-ALPHA-A-PROP-0001`
- `AS-ALPHA-A-DEF-0001`
- `AS-ALPHA-A-PROP-0002`
- `AS-ALPHA-A-THM-0001`
- `AS-ALPHA-A-PROP-0003`
- `AS-ALPHA-A-PROP-0004`
- `AS-ALPHA-A-PROP-0005`

Important source limitations preserved:
- The local fold result is conditional on regularity and nondegeneracy; model-specific negative curvature is marked open in the source.
- The exact threshold scaling is conditional on interior attainment of the infimum.
- Root scale-independence is root-by-root; it does not prove global uniqueness or branch selection.
- `B-C>0` is explicitly a numerically supported conjecture, not an analytic theorem.
- The upstream Paper A claims ledger contains many additional mixed-scope entries (including project-level Lean source theorems, open proof obligations, numerical claims, retractions, and historical stages). It has not been treated as a complete manuscript claim list.

**Completeness:** STRUCTURAL SCAN COMPLETED FOR PASS 1; overall extraction review remains OPEN. A separate audit report records 14 candidates, additional sub-obligations, five structural/source issues, and reconciliation of the secondary claims ledger. Independent transcription review, appendix/supplement review, proof/dependency extraction, and resolution of open scope issues remain outstanding.


### 2.1 Paper A full extraction audit — Pass 1

Audit report: `PAPER_A_FULL_EXTRACTION_AUDIT.md`.

The second Paper A pass fetched all six authoritative revised section files from the frozen upstream commit and matched their blob SHAs against the source manifest. It added seven source-linked candidate records:

- `AS-ALPHA-A-THM-0002` — finite-`N`, `h>0` Perron–Frobenius ground-state nondegeneracy.
- `AS-ALPHA-A-PROP-0006` — positive energy rescaling and dimensionless mutual-information dependence.
- `AS-ALPHA-A-PROP-0007` — zero-coupling product state and trivial fixed point.
- `AS-ALPHA-A-PROP-0008` — conditional subcritical exclusion.
- `AS-ALPHA-A-PROP-0009` — strong-coupling asymptotic expansion of `G_N` and its derivative.
- `AS-ALPHA-A-PROP-0010` — uniform-response upper bound and correction of a false sign inference.
- `AS-ALPHA-A-PROP-0011` — scale covariance of response eigenvalues.

The report also identifies unresolved cross-references to Lemma 5.1 and Lemma 5.2 in Section 4, a threshold `min`/`inf` wording clarification, ground-state nondegeneracy domain obligations, and the difference between the upstream ledger's `N>=3` endpoint-limit scope and the Section 4 asymptotic expansion's `N>=4` scope.

The upstream ledger was reconciled item-by-item at the level of scope and epistemic classification. Project-level Lean-source claims and historical Stage V claims were not imported as Paper A manuscript theorems. The retracted inference `F'<0 => dI/dJ<0` remains explicitly rejected; the manuscript's correct upper bound is preserved. The sign of `B-C` remains a numerical conjecture, not a theorem.

**Pass 1 result:** 14 initial Paper A records; independent extraction review completed for 14/14 with issues; one duplicate record identified; zero Constant Llapoy VERIFIED claims. Six-section structural extraction and record-level review are complete for this initial set, but proof completeness and mathematical verification remain open.


### 2.2 Paper A independent extraction review — Pass 1

Review report: `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`.\n\nPreliminary dependency/obligation map: `PAPER_A_DEPENDENCY_OBLIGATION_MAP.md`. It records provisional dependency edges and nine verification-obligation groups. No dependency closure or circularity check is claimed.

All 14 initial Paper A claim records were freshly fetched and compared against the six pinned revised sections. A further source-conflict record, PROP-0012, was extracted from Section 4.4.3 after reconciling supporting files in the upstream repository. The source excerpts and line locators were confirmed for 13/14 records. PROP-0011's source locator was correct but its excerpt initially omitted the numbered-item prefix; the excerpt boundary has now been corrected. PROP-0008 is an exact duplicate/overlap of the subcritical-exclusion assertion already included in PROP-0001 and is retained only for audit traceability pending explicit registry consolidation.

The initial review identified source/proof obligations that must remain visible:

1. The Perron–Frobenius argument in Section 2.1 uses the wrong shift sign as written: adding (cI) to (H) does not change its negative off-diagonal entries; the standard route applies PF to (cI-H).
2. Section 3.2 assumes only (C^2) regularity but claims a cubic Taylor remainder and an (O(g-g_c)) branch remainder. Those orders need stronger regularity than stated.
3. Section 4.4.2's derivative asymptotic does not follow merely by differentiating a function-level big-(O) expansion; it needs a separate derivative remainder estimate. Lemma 5.1 is cited but absent from the pinned Section 5; the located `docs/lemma_5_1_proof.md` concerns B-C rather than the G_N expansion, so the citation appears mismatched.
4. Section 5.2's edge-representation dimensions require an explicit domain, at least (N\ge3).
5. Lemma 5.2 is cited by Section 4.4.3 but absent from the pinned Section 5; the original proof file is superseded by an audit correcting its leading sign and leaving the derivative remainder open.
6. The threshold's infimum and attainment/minimum language still needs clarification.

**Review disposition:** Independent extraction review COMPLETED WITH ISSUES for the initial 14-record set; after supporting-source reconciliation, the current Paper A set is 15/15 reviewed, including PROP-0012 marked SOURCE_CONFLICT. A preliminary dependency/obligation map has been created; all edges remain provisional. Proof re-derivation, appendix review, Lean correspondence, dependency closure, circularity analysis, and mathematical verification remain open. Constant Llapoy VERIFIED claims remain zero.


### 2.3 Paper A supporting-source reconciliation

Report: `PAPER_A_SUPPORTING_SOURCE_RECONCILIATION.md`.

The pinned upstream branch contains proof/support files outside the six authoritative sections:

- `docs/tfim_ground_state_simplicity_lemma.md` provides a corrected (cI-H) Perron–Frobenius proof candidate for THM-0002; independent Constant Llapoy verification remains pending.
- `docs/lemma_5_1_proof.md` concerns asymptotic positivity of (B-C), not the (\mathcal G_N(x)) expansion cited in Section 4.4.2. The actual proof source for that expansion remains unresolved.
- `docs/lemma_5_2_proof.md` is superseded by `docs/lemma_5_2_audit.md`. The audit identifies an omitted order-(r^2) coherence, corrects the leading sign to positive, and leaves the differentiated remainder unbounded.
- `docs/entropy_schur_remainder_lemma.md` is conditional on model-specific Schur-complement bounds; it does not establish those bounds for the TFIM.
- `STRONG_COUPLING_PROOF_RECONCILIATION.md` concludes that the strong-coupling derivative-remainder proof is not closed and the global (B-C>0) claim remains a conjecture.
- `Arxiv/supplementary_material.md` adds a finite numerical table, solver checks, and an exact Johnson-scheme derivation of the sector identity.

The weak-coupling opposite-sign statement in Section 4.4.3 has been separately registered as `AS-ALPHA-A-PROP-0012` with SOURCE_CONFLICT status. No result is promoted to VERIFIED.

## 3. Paper D extraction findings

Source: `Absolute_Sym`, branch `paper-d-singularity`, commit `2678e3f581d707ac57e8a72d3f961fadbba29ade`.

Nine structured source records were found in `papers/paper-d/02-theorems/` and transcribed into Constant Llapoy:
- `AS-ALPHA-D-THM-0001` — quadratic spectral zero entropy asymptotics.
- `AS-ALPHA-D-THM-0002` — candidate local coupling-space entropy singularity at the N=4 symmetric point.
- `AS-ALPHA-D-THM-0003` — global regularity of the N=4 minus-branch zero hypersurface.
- `AS-ALPHA-D-PROP-0001` — entropy regularity hierarchy.
- `AS-ALPHA-D-PROP-0002` — evenness in transverse field for parity-block spectra.
- `AS-ALPHA-D-PROP-0003` — path-connectedness of the P-minus zero set.
- `AS-ALPHA-D-PROP-0004` — strict positivity of the plus-branch coefficient.
- `AS-ALPHA-D-PROP-0005` — exact swap-symmetry zero set.
- `AS-ALPHA-D-PROP-0006` — symmetry-breaking eigenvalue evenness and conditional entropy consequence.

Critical source boundary: the current branch README says the integrated publication-facing manuscript has not yet been consolidated. These nine records are source-level claim candidates, not a complete extraction from a final Paper D manuscript. The file for THM-0002 explicitly labels its result a candidate theorem requiring independent audit. A filename/type mismatch is preserved for THM-0003 because the filename says proposition while the internal heading says theorem.

**Completeness:** BLOCKED for manuscript-level extraction pending an integrated Paper D manuscript and explicit canonical-source designation.

## 4. Paper A1 extraction findings

Source: `Absolute_Sym`, branch `stage-a1-1-repair-review`, commit `b95f5777dfadaf5d31eef27d813ea56c33540d1c`.

Five formal Stage A1-1 theorem statements and all 17 rows of the Stage A1-1 epistemic claim ledger were transcribed:
- `AS-ALPHA-A1-THM-0001` — compact uniform C0 convergence.
- `AS-ALPHA-A1-THM-0002` — analytic regularity, inflection structure, and unique minimizer of the thermodynamic-limit function.
- `AS-ALPHA-A1-THM-0003` — three-regime uniform bounds, equicoercivity, and Gamma-convergence.
- `AS-ALPHA-A1-THM-0004` — thermodynamic critical-threshold convergence.
- `AS-ALPHA-A1-THM-0005` — separated critical-location convergence.

The upstream README says Stage A1-1 is complete (repaired) and Stage A1-2 is pending. The separate Stage A1-1 claim ledger reports 17 epistemic entries across proven, numerical, incomplete, conjectural, unverified, and incorrect categories. Those 17 entries are not all theorem statements and must not be relabelled as proved. The source's PROVEN labels have not been independently re-proved by Constant Llapoy.

**Completeness:** PARTIAL. Five formal Stage A1-1 theorem statements and all 17 Stage A1-1 ledger rows are transcribed; supporting definitions, assumptions, appendices, and later A1 stages still require reconciliation.

## 5. Record status and what has not been done

- Initial source branches and commits: recorded.
- Individual claim-source and source-ledger records created: 45.
- Independent extraction review: NOT_RUN (including Paper A Pass 1).
- Mathematical proof re-derivation: NOT_RUN.
- Lean formalization correspondence: NOT_RUN.
- Axiom/TCB audit per claim: NOT_RUN.
- Dependency closure and circularity analysis: NOT_RUN.
- Paper A six-section structural scan: COMPLETED for Pass 1; overall completeness NOT_ESTABLISHED.\n- Full manuscript completeness: NOT_ESTABLISHED.
- Any Constant Llapoy VERIFIED claim: NONE.

## 6. Next extraction operations

1. Complete the Paper A scan across all six canonical sections and reconcile every claim-bearing statement with `Arxiv/claims_ledger.md`.
2. Resolve Paper D's integrated manuscript source; until then, keep source theorem records separate from manuscript claims.
3. Expand Paper A1's 17-entry ledger into separately classified claim records, preserving negative and incorrect entries.
4. Create claim-level dependency graphs and Verification Obligation Matrix rows only after exact statement and source reconciliation.
5. Perform independent extraction review before changing any CANDIDATE/TRANSCRIBED record to REGISTERED.

---

**End of initial extraction ledger.**
