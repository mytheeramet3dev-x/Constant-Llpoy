# Claim Registry
**Project:** Constant Llapoy  
**Repository:** `mytheeramet3dev-x/Constant-Llpoy`  
**Document ID:** CL-CR-001  
**Version:** 0.1.0  
**Status:** Empty registry template; no mathematical claims have yet been registered  
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

One source manifest MUST be maintained per manuscript revision.

| Paper ID | Official title | Canonical source path | Commit/tag | Source digest(s) | PDF digest | Authority confirmed by | Status |
|---|---|---|---|---|---|---|---|
| A | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |
| D | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |
| A1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |

These rows are intake placeholders only. They do not establish official titles, source availability, or paper status.

## 6. Claim index

No claim records have been registered at version 0.1.0. The table below is intentionally empty until authoritative manuscript sources are designated and extracted.

| Claim ID | Paper | Original label | Claim type | Claim version | Source locator | Extraction status | Verification status | Record path |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

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

| Paper ID | Source frozen | Sections scanned | Appendices scanned | Candidates reconciled | Independent review | Completeness status |
|---|---|---|---|---|---|---|
| A | NO | NO | NO | NO | NO | NOT_STARTED |
| D | NO | NO | NO | NO | NO | NOT_STARTED |
| A1 | NO | NO | NO | NO | NO | NOT_STARTED |

Completeness status may be marked COMPLETE only after the protocol's reconciliation and independent review gates are satisfied for the exact source revision.

## 10. Change log

| Registry version | Date | Change | Affected Claim IDs | Reviewer |
|---|---|---|---|---|
| 0.1.0 | Initial creation | Empty registry schema established | None | Pending |

## 11. Current truth statement

At version 0.1.0:
- Registered mathematical claims: **0 in this registry**.
- This count means no claim records have yet been entered here; it does not mean the papers contain zero claims.
- Manuscript source revisions: **UNKNOWN**.
- Extraction completeness: **NOT_STARTED**.
- Independent extraction review: **NOT_STARTED**.
- Mathematical proof verification: **NOT ESTABLISHED**.
- Lean/Python/Rust/CAS/SMT evidence: **NOT ASSERTED**.

The next valid operation is to designate the authoritative manuscript sources, freeze their revisions, and execute the Manuscript Extraction Protocol. Do not populate this registry with guessed theorem statements or placeholder IDs presented as real claims.

## 12. Governing documents

- `MANUSCRIPT_EXTRACTION_PROTOCOL.md`
- `VERIFICATION_OBLIGATION_MATRIX.md`
- `ARCHITECTURE_CHARTER.md`
- `THREAT_MODEL.md`
- `TRUST_BOUNDARY_TCB_INVENTORY.md`
- `TOOLCHAIN_DEPENDENCY_INVENTORY.md`

---

**End of document.**  
**Status:** Registry schema committed; actual claim records await authoritative manuscript sources.
