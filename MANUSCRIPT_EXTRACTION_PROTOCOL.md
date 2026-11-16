# Manuscript Extraction Protocol
**Project:** Constant Llapoy  
**Repository:** `mytheeramet3dev-x/Constant-Llpoy`  
**Document ID:** CL-MEP-001  
**Version:** 0.1.0  
**Status:** Protocol specification; manuscript extraction has not yet been performed  
**Normative language:** MUST, MUST NOT, SHOULD, and MAY are requirements.

---

## 1. Purpose

This protocol defines a controlled, auditable process for discovering and transcribing every mathematical claim in an authoritative Absolute Symmetry manuscript into the project Claim Registry.

The objective is completeness and fidelity—not speed, favorable results, or a predetermined claim count. Extraction is a source-accounting activity. It does not prove a claim, endorse its correctness, or establish that a paper is complete.

## 2. Scope

The initial intended manuscript set includes Paper A, Paper D, and Paper A1, subject to confirmation of their authoritative source locations and revisions. Other papers or project-level documents MUST be added only after their scope and source are explicitly confirmed.

Paper 1–2, older concepts, and other materials MUST NOT be silently merged into the Alphabet series. Project-level stages or concepts MUST NOT be assigned to an individual paper unless the source and project structure explicitly support that assignment.

This protocol does not prescribe the number of verification layers or require every claim to use every tool.

## 3. Source authority and source freeze

### 3.1 Source hierarchy

For each manuscript, the extraction lead MUST identify and record the authoritative source. Candidate source types include:

1. A designated canonical Git repository revision and exact file path.
2. A release/tag or immutable commit explicitly designated by the project owner.
3. A source archive (for example, LaTeX sources) with a recorded digest.
4. A rendered PDF generated from the designated source, with its own digest.
5. Other copies, exports, screenshots, OCR text, or agent summaries as secondary aids only.

A secondary copy MUST NOT silently override the designated canonical source. If two sources conflict, stop extraction for the affected material and open a source discrepancy record.

### 3.2 Freeze record

Before extraction, record:

- Paper/document identifier and official title.
- Canonical repository and path, if applicable.
- Branch/tag/commit SHA or immutable source version.
- File names and SHA-256 digests for all source files used.
- PDF digest and page count, if a PDF is used.
- Extraction date and responsible operator.
- Any submodules, bibliography files, macros, generated files, or included source files needed to interpret the manuscript.

A mutable branch name alone is not a sufficient source identity. Record its resolved commit.

### 3.3 Missing source

If the canonical source cannot be located or its authority cannot be established:
- record the manuscript as SOURCE_NOT_LOCATED or SOURCE_AUTHORITY_UNKNOWN;
- do not invent a replacement source;
- do not claim extraction completeness;
- request the exact source or authoritative repository location.

## 4. What counts as a claim

The extractor MUST inspect the complete manuscript, not only theorem environments.

Potential claim-bearing items include:

- Theorem
- Lemma
- Proposition
- Corollary
- Conjecture
- Definition that asserts a substantive property or characterization
- Equation or identity asserted as a result
- Explicitly stated existence, uniqueness, classification, equivalence, or impossibility result
- Main-text mathematical assertion that is relied upon in later reasoning
- Appendix result or supplementary proposition

Definitions that only introduce notation may be registered as definitions/dependencies when needed, but MUST NOT be misclassified as proved theorems.

Examples, motivations, informal conjectures, numerical observations, and heuristic statements MUST be distinguished from proved claims. Their evidentiary status MUST be recorded accurately.

## 5. Extraction workflow

### Phase 0 — Manuscript inventory

1. List all candidate manuscripts and source locations.
2. Confirm official paper title and series membership.
3. Resolve canonical source revision with the project owner or designated maintainer.
4. Record all source files and digests.
5. Identify included files, macros, appendices, supplements, and generated content.
6. Mark missing or ambiguous sources as blockers.

**Output:** Manuscript Source Manifest.

### Phase 1 — Structural scan

Inspect every section, subsection, appendix, theorem-like environment, displayed equation, and mathematical assertion.

Record a structural inventory containing:
- source file and line range, where available;
- PDF page and section, where applicable;
- environment type and displayed number;
- heading/text that introduces the result;
- whether the item appears to be a theorem, supporting claim, definition, conjecture, example, or other assertion.

The structural scan is a discovery aid, not a correctness judgment.

### Phase 2 — Candidate claim enumeration

Assign a temporary extraction key to every candidate before final Claim IDs are issued. This prevents early numbering decisions from hiding omissions.

For each candidate:
1. Capture its complete statement.
2. Include all conditions in surrounding prose that are part of the statement.
3. Capture relevant definitions and notation.
4. Record the proof location or state that no proof is supplied.
5. Record dependencies explicitly stated or apparently used.
6. Flag ambiguous boundaries between statement and surrounding prose.
7. Flag any missing, malformed, or unresolved notation.

Do not silently repair typos, add assumptions, or normalize a statement in a way that changes meaning.

### Phase 3 — Exact transcription

- Preserve mathematical notation and quantifier order.
- Preserve all hypotheses, side conditions, domain restrictions, and exceptional cases.
- Preserve the original numbering as a source locator, not as the stable Claim ID.
- Record the source file and line range, and PDF page/section where available.
- Where OCR or PDF extraction is uncertain, inspect the original page image or source code.
- Mark unreadable or ambiguous text as TRANSCRIPTION_UNRESOLVED; do not guess.
- Store a verbatim transcription separately from any normalized machine-readable representation.
- Any normalization MUST be recorded as a separate derivative with a link to the verbatim source.

### Phase 4 — Completeness reconciliation

Reconcile at least these independent inventories:
1. Theorem-like environments found in source code.
2. Numbered theorem-like results visible in the rendered manuscript.
3. Appendix and supplementary results.
4. Results referenced by name or number elsewhere in the manuscript.
5. Main-text assertions that carry proof obligations despite lacking a formal environment.

Every discovered item MUST be accounted for as:
- registered claim;
- registered non-claim item with rationale;
- duplicate/reference to an existing claim;
- excluded item with a documented reason;
- unresolved candidate requiring further review.

No candidate may disappear from the reconciliation list without a disposition.

### Phase 5 — Claim identity and dependency mapping

After candidate enumeration and initial reconciliation:
1. Assign stable Claim IDs according to the Claim Registry policy.
2. Record original manuscript numbering independently.
3. Link definitions, lemmas, propositions, external theorems, and assumptions.
4. Distinguish explicit dependencies from dependencies inferred by reviewers.
5. Mark uncertain dependency edges as UNCONFIRMED.
6. Detect possible circular dependency paths for later mathematical review.

Claim numbering in the manuscript MUST NOT be used as the sole stable identifier because manuscript edits can renumber results.

### Phase 6 — Independent extraction review

A reviewer who did not perform the initial extraction SHOULD:
- compare the registry against the complete source;
- inspect all theorem-like environments and appendices;
- sample or fully compare verbatim transcriptions according to the risk policy;
- verify source paths, line ranges, pages, and original numbering;
- inspect all unresolved candidates and exclusions;
- sign off completeness separately from mathematical correctness.

For high-assurance release, complete second-person reconciliation is preferred over sampling. Any sampling policy MUST state its limitations and cannot be described as exhaustive review.

### Phase 7 — Freeze and handoff

Freeze the extracted registry against the exact manuscript revision. Record:
- extraction commit;
- source manifest digest;
- registry revision;
- reviewer and date;
- unresolved items;
- completeness status.

Only after this handoff should claim-specific Verification Obligation Matrix rows and verification routes be populated.

## 6. Stable Claim ID policy

Use the following format:

`AS-[SERIES]-[PAPER]-[TYPE]-[SEQUENCE]`

Examples below are format illustrations only:
- `AS-ALPHA-A-THM-0001`
- `AS-ALPHA-D-LEM-0001`
- `AS-ALPHA-A1-PROP-0001`

These are NOT actual registered claims.

Rules:
1. Claim IDs are immutable once assigned.
2. A change in wording does not automatically create a new ID; use a new claim version if the logical identity remains the same.
3. A materially different proposition MUST receive a new ID and be linked to the superseded claim.
4. Splitting a claim creates new IDs and a relation to the original.
5. Merging claims creates a new ID with explicit links to all predecessors.
6. Renumbering in a paper does not change Claim ID.
7. Never recycle an ID.
8. Type labels describe the source/result classification and do not imply proof status.

Suggested type tokens: THM, LEM, PROP, COR, DEF, CONJ, ID, EQ, OTHER. The registry MUST document any additional token.

## 7. Claim record minimum fields

Each claim record MUST contain:

- Stable Claim ID.
- Claim version and lifecycle status.
- Paper/document ID and official title.
- Source revision, path, and digest.
- Original manuscript label/number.
- Section, subsection, source line range, and PDF page if available.
- Verbatim statement.
- Normalized statement, if prepared, clearly separated.
- Definitions and notation dependencies.
- Domain and type information.
- Quantifiers.
- Hypotheses and side conditions.
- Conclusion.
- Proof location and proof availability.
- Explicit dependency links.
- Inferred dependency links with reviewer and rationale.
- Extraction operator and independent reviewer.
- Extraction status and unresolved issues.
- Verification Obligation Matrix link/status.

No field may be populated by assumption when the source is silent. Use UNKNOWN, NOT_STATED, or UNRESOLVED as appropriate and explain the distinction.

## 8. Extraction status vocabulary

| Status | Meaning |
|---|---|
| CANDIDATE | Discovered but not fully transcribed or classified |
| TRANSCRIBED | Verbatim statement captured with source locator |
| NEEDS_REVIEW | Awaiting independent extraction review |
| TRANSCRIPTION_UNRESOLVED | Source text or notation cannot yet be read reliably |
| SOURCE_CONFLICT | Two candidate authoritative sources disagree |
| REGISTERED | Identity and minimum record are accepted into the registry |
| SUPERSEDED | Replaced by a new claim identity/version; history retained |
| EXCLUDED | Determined not to be a claim; rationale required |

Extraction status is separate from mathematical verification status. REGISTERED does not mean proved, correct, formalized, or verified.

## 9. Dependency representation

Represent dependencies as directed edges from a dependent claim to the item it relies on.

Each edge MUST record:
- source Claim ID or external reference;
- edge type: EXPLICIT, INFERRED, DEFINITIONAL, AXIOMATIC, or EXTERNAL;
- exact source location;
- rationale;
- confidence/review state;
- version of the dependency.

Do not convert an inferred dependency into an explicit one. Unresolved edges remain visible and block dependency closure.

## 10. Exclusions and non-claim items

An exclusion record MUST include:
- source locator;
- quoted or summarized item sufficient to identify it;
- reason for exclusion;
- reviewer;
- date;
- whether the item is instead tracked as a definition, assumption, conjecture, example, or informal assertion.

Examples are not proofs. Conjectures are not theorems. A statement that is merely called a theorem is not thereby established.

## 11. Quality controls and failure conditions

Extraction MUST stop or mark the affected record unresolved when:
- canonical source authority is unknown;
- the source revision changes during extraction;
- text, formula, quantifier, or hypothesis is ambiguous;
- a referenced included file is missing;
- OCR is the only available basis for a critical formula and cannot be checked;
- manuscript numbering or references cannot be reconciled;
- a candidate result is omitted from the reconciliation ledger;
- the registry text differs from the source without a recorded normalization.

A completeness claim MUST be withheld if any source section, appendix, supplement, or candidate item remains unaccounted for.

## 12. Relationship to verification

Extraction and verification are separate stages:

1. **Extraction:** What does the manuscript actually claim?
2. **Specification review:** Is the claim unambiguous and well-formed?
3. **Proof review:** Does the argument establish that exact claim?
4. **Formal/computational verification:** Do selected tools establish their defined obligations?
5. **Correspondence audit:** Do the evidence artifacts match the manuscript?
6. **Release decision:** Is the evidence sufficient for the stated verification status?

A registered claim MUST NOT inherit a Verified status from a neighboring claim, a paper-level label, a previous manuscript revision, or an AI-generated summary.

## 13. Initial manuscript intake register

The following are intake targets, not confirmation that source files are currently available in this repository.

| Intake ID | Manuscript | Source authority | Revision/digest | Intake status |
|---|---|---|---|---|
| MI-A | Paper A | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |
| MI-D | Paper D | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |
| MI-A1 | Paper A1 | UNKNOWN | UNKNOWN | SOURCE_NOT_LOCATED |

The intake targets MUST be corrected if the project owner designates a different official manuscript set. No theorem content is inferred from these labels.

## 14. Current execution status

At version 0.1.0:
- Protocol: specified.
- Canonical manuscript sources: not yet designated in this repository.
- Source manifest: not yet created.
- Structural scan: not run.
- Candidate claim enumeration: not run.
- Verbatim transcription: not run.
- Completeness reconciliation: not run.
- Independent extraction review: not run.
- Claim-level verification: not performed by this protocol.

The repository root was inspected during preparation and contained the five governance documents, but no Paper A, D, or A1 manuscript source files. This observation is limited to the inspected repository root and does not establish that the manuscripts do not exist elsewhere.

## 15. Governing documents

Read together with:
- `ARCHITECTURE_CHARTER.md`
- `THREAT_MODEL.md`
- `TRUST_BOUNDARY_TCB_INVENTORY.md`
- `TOOLCHAIN_DEPENDENCY_INVENTORY.md`
- `VERIFICATION_OBLIGATION_MATRIX.md`
- `CLAIM_REGISTRY.md`

If a source or protocol conflict appears, preserve the source evidence, record the discrepancy, and resolve it through documented review. Do not silently edit source statements to make them easier to formalize.

---

**End of document.**  
**Status:** Protocol committed; manuscript extraction and claim verification remain outstanding.
