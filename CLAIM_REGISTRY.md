# Claim Registry
**Project:** Constant Llapoy  
**Repository:** `mytheeramet3dev-x/Constant-Llpoy`  
**Document ID:** CL-CR-001  
**Version:** 0.4.2  
**Status:** 45 source-linked records indexed; Paper A independent extraction review completed with issues; mathematical verification remains open  
**Normative language:** MUST, MUST NOT, SHOULD, and MAY are requirements.

---

## 1. Purpose

This file is the canonical index of mathematical claims admitted to the Constant Llapoy verification workflow.

It records claim identity, exact manuscript provenance, statement versions, dependencies, extraction review, and links to claim-specific verification obligations and evidence.

This registry is not a list of proven theorems. Registration is an administrative and source-fidelity milestone only.

## 2. Registry invariants

1. Every registered claim MUST have a stable, unique Claim ID.
2. Every claim MUST point to an immutable manuscript revision and exact source locator.
3. The verbatim statement MUST be preserved independently from any normalized representation.
4. No claim may be inferred from memory, a paper title, an AI summary, or an unverified secondary copy.
5. Unknown information MUST be marked UNKNOWN, NOT_STATED, or UNRESOLVED—not guessed.
6. Original manuscript numbering and stable Claim ID MUST remain separate.
7. Dependencies MUST be explicit records; uncertain dependencies remain unconfirmed.
8. Extraction status MUST remain separate from mathematical verification status.
9. Claim edits and supersession MUST preserve history.
10. A missing or incomplete record MUST NOT be treated as a Verified claim.

## 3. Stable ID format

`AS-[SERIES]-[PAPER]-[TYPE]-[SEQUENCE]`

Illustrative formats only:
- `AS-ALPHA-A-THM-0001`
- `AS-ALPHA-D-LEM-0001`
- `AS-ALPHA-A1-PROP-0001`

These IDs are examples of syntax only. They are not actual claims and are not reserved.

## 4. Status dimensions

### 4.1 Extraction lifecycle

CANDIDATE, TRANSCRIBED, NEEDS_REVIEW, TRANSCRIPTION_UNRESOLVED, SOURCE_CONFLICT, REGISTERED, SUPERSEDED, EXCLUDED.

### 4.2 Verification status

UNREGISTERED, DRAFT, OBLIGATIONS_OPEN, IN_PROGRESS, BLOCKED, FAILED, INCONCLUSIVE, VERIFIED, SUPERSEDED.

A claim may be REGISTERED for extraction while its verification status remains UNREGISTERED or DRAFT. Never conflate the two.

## 5. Manuscript source manifest

The canonical source pins and file digests are maintained in `MANUSCRIPT_SOURCE_MANIFEST.md`. The registry MUST NOT duplicate stale intake placeholders in place of that manifest.

| Paper ID | Frozen source | Current scope | Manifest |
|---|---|---|---|
| A | `Absolute_Sym` / `paper-a-interval-audit-2026-11-14` / `8deb7de4a49cb2060720246b7101820ee7e08c91` | Six revised sections are authoritative for this extraction pass | [Source manifest](MANUSCRIPT_SOURCE_MANIFEST.md) |
| D | `Absolute_Sym` / `paper-d-singularity` / `2678e3f581d707ac57e8a72d3f961fadbba29ade` | Nine structured theorem sources only; integrated manuscript not consolidated | [Source manifest](MANUSCRIPT_SOURCE_MANIFEST.md) |
| A1 | `Absolute_Sym` / `stage-a1-1-repair-review` / `b95f5777dfadaf5d31eef27d813ea56c33540d1c` | Stage A1-1 theorem statements and ledger only | [Source manifest](MANUSCRIPT_SOURCE_MANIFEST.md) |

## 6. Claim index

The registry now contains 46 source-linked records (29 theorem/proposition/definition source records and 17 Stage A1-1 epistemic-ledger transcriptions). Paper A has 15 source-linked records: 14 initial candidates plus one SOURCE_CONFLICT record (PROP-0012) extracted from Section 4.4.3 after supporting-source reconciliation. All 15 have undergone extraction review; one record (PROP-0008) duplicates a subclaim in PROP-0001. No record has been mathematically verified.

### Paper A — 15 records; extraction review completed with issues

| Claim ID | Original label | Type | Source locator | Extraction | Verification | Record |
|---|---|---|---|---|---|---|
| AS-ALPHA-A-PROP-0001 | §2.5 threshold scaling | Proposition/claim | `Arxiv/paper_01_section_02_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0001.md) |
| AS-ALPHA-A-DEF-0001 | Definition 1 | Definition | `Arxiv/paper_01_section_03_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-DEF-0001.md) |
| AS-ALPHA-A-PROP-0002 | Proposition 1 | Proposition | `Arxiv/paper_01_section_03_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0002.md) |
| AS-ALPHA-A-THM-0001 | §3.2 local normal form | Conditional theorem | `Arxiv/paper_01_section_03_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-THM-0001.md) |
| AS-ALPHA-A-PROP-0003 | §3.3 Picard criterion | Proposition/claim | `Arxiv/paper_01_section_03_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0003.md) |
| AS-ALPHA-A-PROP-0004 | §4.2 scale independence | Proposition/claim | `Arxiv/paper_01_section_04_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0004.md) |
| AS-ALPHA-A-PROP-0005 | §5.2 response-sector identity | Proposition/claim | `Arxiv/paper_01_section_05_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0005.md) |

| AS-ALPHA-A-THM-0002 | §2.1 Perron–Frobenius ground-state nondegeneracy | Theorem candidate | `Arxiv/paper_01_section_02_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-THM-0002.md) |
| AS-ALPHA-A-PROP-0006 | §2.3 positive energy rescaling / dimensionless mutual information | Proposition candidate | `Arxiv/paper_01_section_02_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0006.md) |
| AS-ALPHA-A-PROP-0007 | §2.4 zero-coupling product state and trivial root | Proposition candidate | `Arxiv/paper_01_section_02_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0007.md) |
| AS-ALPHA-A-PROP-0008 | §2.5 subcritical exclusion | Proposition candidate | `Arxiv/paper_01_section_02_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0008.md) |
| AS-ALPHA-A-PROP-0009 | §4.4.2 strong-coupling asymptotic expansion | Proposition candidate | `Arxiv/paper_01_section_04_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0009.md) |
| AS-ALPHA-A-PROP-0010 | §5.1 uniform-response upper bound and non-implication | Proposition candidate | `Arxiv/paper_01_section_05_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0010.md) |
| AS-ALPHA-A-PROP-0011 | §5.4 response-eigenvalue scale covariance | Proposition candidate | `Arxiv/paper_01_section_05_revised.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0011.md) |
| AS-ALPHA-A-PROP-0012 | §4.4.3 weak-coupling opposite-sign response assertion | Source-conflict claim | `Arxiv/paper_01_section_04_revised.md` | SOURCE_CONFLICT | NOT_ASSESSED | [Record](claims/A/AS-ALPHA-A-PROP-0012.md) |

### Paper D — structured source records, not a final-manuscript extraction

| Claim ID | Original label | Type | Source locator | Extraction | Verification | Record |
|---|---|---|---|---|---|---|
| AS-ALPHA-D-THM-0001 | Theorem 1 | Theorem | `papers/paper-d/02-theorems/theorem_1_quadratic_spectral_zero.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-THM-0001.md) |
| AS-ALPHA-D-THM-0002 | Candidate Theorem 2 | Candidate theorem | `papers/paper-d/02-theorems/theorem_2_coupling_space_singularity.md` | CANDIDATE | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-THM-0002.md) |
| AS-ALPHA-D-THM-0003 | Internal heading: Theorem | Theorem (filename says proposition) | `papers/paper-d/02-theorems/proposition_global_regular_zero_hypersurface.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-THM-0003.md) |
| AS-ALPHA-D-PROP-0001 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_entropy_regularity_hierarchy.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0001.md) |
| AS-ALPHA-D-PROP-0002 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_even_field_parity_spectrum.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0002.md) |
| AS-ALPHA-D-PROP-0003 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_pminus_zero_set_path_connected.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0003.md) |
| AS-ALPHA-D-PROP-0004 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_pplus_strict_positivity.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0004.md) |
| AS-ALPHA-D-PROP-0005 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_swap_symmetry_exact_zero.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0005.md) |
| AS-ALPHA-D-PROP-0006 | Proposition | Proposition | `papers/paper-d/02-theorems/proposition_symmetry_breaking_even_eigenvalue.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/D/AS-ALPHA-D-PROP-0006.md) |

### Paper A1 — Stage A1-1 formal theorem statements

| Claim ID | Original label | Type | Source locator | Extraction | Verification | Record |
|---|---|---|---|---|---|---|
| AS-ALPHA-A1-THM-0001 | Theorem 1 / OP-2 | Theorem | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/A1/AS-ALPHA-A1-THM-0001.md) |
| AS-ALPHA-A1-THM-0002 | Theorem 2 | Theorem | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/A1/AS-ALPHA-A1-THM-0002.md) |
| AS-ALPHA-A1-THM-0003 | Theorem 3 / OP-3 | Theorem | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/A1/AS-ALPHA-A1-THM-0003.md) |
| AS-ALPHA-A1-THM-0004 | Theorem 4 | Theorem | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/A1/AS-ALPHA-A1-THM-0004.md) |
| AS-ALPHA-A1-THM-0005 | Theorem 5 | Theorem | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md` | TRANSCRIBED | NOT_ASSESSED | [Record](claims/A1/AS-ALPHA-A1-THM-0005.md) |

### Paper A1 — Stage A1-1 epistemic ledger entries

These 17 records preserve the source ledger's mixed epistemic classifications. They are not 17 additional theorems; some overlap with Theorems 1–5, while others are corrections, counterexamples, conjectures, numerical claims, or unresolved items.

| Claim ID | Upstream ID | Source-reported classification | Record |
|---|---|---|---|
| AS-ALPHA-A1-CLM-0001 | C1 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0001.md) |
| AS-ALPHA-A1-CLM-0002 | C2 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0002.md) |
| AS-ALPHA-A1-CLM-0003 | C3 | INCORRECT | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0003.md) |
| AS-ALPHA-A1-CLM-0004 | C4 | INCORRECT | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0004.md) |
| AS-ALPHA-A1-CLM-0005 | C5a | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0005.md) |
| AS-ALPHA-A1-CLM-0006 | C5b | UNVERIFIED / CONJECTURAL; endpoint claim INCORRECT | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0006.md) |
| AS-ALPHA-A1-CLM-0007 | C6 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0007.md) |
| AS-ALPHA-A1-CLM-0008 | C7 | INCORRECT for N=2; UNVERIFIED for small N≥4 | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0008.md) |
| AS-ALPHA-A1-CLM-0009 | C8 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0009.md) |
| AS-ALPHA-A1-CLM-0010 | C9 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0010.md) |
| AS-ALPHA-A1-CLM-0011 | C10 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0011.md) |
| AS-ALPHA-A1-CLM-0012 | C11 | PROVEN | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0012.md) |
| AS-ALPHA-A1-CLM-0013 | C12 | SUPPORTED_BUT_INCOMPLETE | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0013.md) |
| AS-ALPHA-A1-CLM-0014 | C13 | CONJECTURAL | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0014.md) |
| AS-ALPHA-A1-CLM-0015 | C14 | CONJECTURAL | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0015.md) |
| AS-ALPHA-A1-CLM-0016 | C15 | INCORRECT for clustering limit; UNVERIFIED for open dynamics | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0016.md) |
| AS-ALPHA-A1-CLM-0017 | C16 | NUMERICALLY_REPRODUCED | [Record](claims/A1/ledger/AS-ALPHA-A1-CLM-0017.md) |

## 7. Canonical claim record template

Create one record per claim, preferably as an individual file under `claims/<PAPER_ID>/<CLAIM_ID>.md`. The index in this file MUST link to each record.

### Claim identity
- Claim ID:
- Claim version:
- Lifecycle status:
- Paper/document ID:
- Official paper title:
- Claim type:
- Original manuscript number/label:
- Supersedes / superseded by:

### Source provenance
- Canonical repository:
- Source path:
- Source commit/tag:
- Source file digest:
- PDF path and digest:
- Section/subsection:
- Source line range:
- PDF page:
- Extraction date:
- Extractor:
- Independent extraction reviewer:

### Verbatim statement
> Paste the exact statement from the authoritative source. Preserve all mathematical notation and hypotheses. If transcription is uncertain, do not complete this field by guessing; mark TRANSCRIPTION_UNRESOLVED and identify the ambiguity.

### Normalized representation (optional)
- Normalized statement:
- Normalization rules:
- Differences from verbatim text:
- Reviewer approval:

### Mathematical structure
- Definitions and notation:
- Domain and codomain:
- Structures/spaces:
- Quantifiers:
- Hypotheses:
- Side conditions:
- Conclusion:
- Edge cases:
- Proof location:
- Proof supplied: YES / NO / PARTIAL / UNKNOWN

### Dependencies
| Dependency ID/reference | Edge type | Source location | Rationale | Version | Review state |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

### Extraction review
- Structural scan reconciled: YES / NO / UNKNOWN
- Verbatim transcription checked: YES / NO / UNKNOWN
- Appendix/supplement checked: YES / NO / UNKNOWN
- Cross-references checked: YES / NO / UNKNOWN
- Exclusions reconciled: YES / NO / UNKNOWN
- Unresolved issues:
- Reviewer decision:
- Review date:

### Verification linkage
- Verification Obligation Matrix record:
- Formal proof artifact:
- Exact computation/certificate:
- Independent checker:
- Numerical evidence:
- Claim-specific TCB declaration:
- Threat IDs:
- Trust-boundary IDs:
- Evidence index:
- Verification reviewer:
- Verification status:
- Residual risks:

## 8. Non-claim and exclusion ledger

Every candidate found during extraction that is not registered as a mathematical claim MUST be accounted for here or in a linked extraction ledger.

| Candidate key | Manuscript/source locator | Item classification | Disposition | Rationale | Reviewer |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

Valid dispositions include DEFINITION_ONLY, NOT_A_CLAIM, EXAMPLE, CONJECTURE, DUPLICATE_REFERENCE, OUT_OF_SCOPE, and UNRESOLVED. An unresolved candidate cannot be silently excluded.

## 9. Completeness ledger

| Paper ID | Source frozen | Sections scanned | Appendices / supplementary | Candidates reconciled | Independent review | Completeness status |
|---|---|---|---|---|---|---|
| A | YES | YES (six revised sections) | Supplementary material inspected; other appendices UNKNOWN | PARTIAL (secondary ledger reconciled; duplicate and source conflict recorded) | YES — WITH ISSUES (15/15 records) | EXTRACTION_REVIEW_COMPLETE_WITH_ISSUES; PROOF_AND_APPENDIX_REVIEW_OPEN |
| D | YES | PARTIAL (nine structured theorem sources; no integrated manuscript) | UNKNOWN | NO (manuscript scope blocked) | NO | BLOCKED_PENDING_INTEGRATED_MANUSCRIPT |
| A1 | YES (Stage A1-1 snapshot) | PARTIAL (five theorem statements and 17 ledger rows) | UNKNOWN | PARTIAL | NO | PARTIAL_STAGE_SCOPE; REVIEW_OPEN |

Completeness status may be marked COMPLETE only after the protocol's reconciliation and independent review gates are satisfied for the exact source revision.

## 10. Change log

| Registry version | Change | Affected scope | Review state |
|---|---|---|---|
| 0.1.0 | Initial registry schema | Registry architecture | Pending |
| 0.2.0 | Initial source-linked extraction; 38 records | Paper A, D, A1 | Independent review pending |
| 0.3.0 | Added seven Paper A candidates; indexed 45 source-linked records | Paper A | Independent review pending |
| 0.4.0 | Completed independent extraction review of the initial 14 Paper A records; recorded source proof issues and one duplicate | Paper A | Review complete with issues; proof review open |
| 0.4.1 | Added preliminary Paper A dependency and verification-obligation map | Paper A | Edges provisional; proof review open |
| 0.4.2 | Added source-conflict claim PROP-0012 and supporting-source inventory | Paper A | Extraction review complete with issues; proof review open |

## 11. Current truth statement

At version 0.4.2:

- Source-linked claim records: **46** (29 formal/proposition/definition records and 17 A1 ledger records).
- Paper A: **15** records (14 initial candidates and one SOURCE_CONFLICT record); all extraction-reviewed, none mathematically verified.
- Paper A six-section structural scan: **COMPLETED for Pass 1**.
- Paper A independent extraction review: **COMPLETED WITH ISSUES (15/15 records)**; one duplicate and one source conflict identified; no proof verified.
- Paper D manuscript-level extraction: **BLOCKED** pending an integrated manuscript.
- Paper A1 extraction: **PARTIAL**, limited to Stage A1-1.
- Constant Llapoy VERIFIED claims: **0**.
- Preliminary Paper A dependency/obligation map: **CREATED; EDGES PROVISIONAL**. Proof re-derivation, Lean correspondence, axiom/TCB audit, dependency closure, and circularity analysis: **NOT_RUN / NOT_ESTABLISHED**.

A record's presence is not evidence of correctness. Do not promote a claim to REGISTERED or VERIFIED solely because it has been transcribed.

## 12. Governing documents

- `MANUSCRIPT_EXTRACTION_PROTOCOL.md`\n- `MANUSCRIPT_SOURCE_MANIFEST.md`\n- `EXTRACTION_LEDGER.md`\n- `PAPER_A_FULL_EXTRACTION_AUDIT.md`\n- `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`\n- `PAPER_A_DEPENDENCY_OBLIGATION_MAP.md`\n- `PAPER_A_SUPPORTING_SOURCE_RECONCILIATION.md`
- `VERIFICATION_OBLIGATION_MATRIX.md`
- `ARCHITECTURE_CHARTER.md`
- `THREAT_MODEL.md`
- `TRUST_BOUNDARY_TCB_INVENTORY.md`
- `TOOLCHAIN_DEPENDENCY_INVENTORY.md`

---

**End of document.**  
**Status:** Source-linked records populated; independent extraction review and mathematical verification remain open.
