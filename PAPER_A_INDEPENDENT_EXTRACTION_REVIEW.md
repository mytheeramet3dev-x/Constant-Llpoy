# Paper A Independent Extraction Review — Pass 1

- **Document ID:** CL-REVIEW-A-001
- **Version:** 0.1.0
- **Reviewed source revision:** `mytheeramet3dev-x/Absolute_Sym` / `paper-a-interval-audit-2026-11-14`
- **Frozen upstream commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Scope:** All 14 Paper A Claim Records in Constant Llapoy, checked against the six pinned revised sections
- **Review type:** Independent extraction/provenance/statement-boundary review; not a proof verification
- **Overall result:** REVIEWED_WITH_ISSUES
- **Constant Llapoy VERIFIED claims:** 0

## 1. Method and review limits

The reviewer re-fetched the six source files from the pinned upstream branch and re-fetched all 14 Paper A claim records from Constant Llapoy. The source blob SHAs were checked against the frozen source manifest. For each claim, the source path, source line range, and verbatim excerpt were compared with the actual source text. The mathematical statements were also inspected for obvious hypothesis omissions, duplicate registration, and source-level proof gaps.

This pass is independent of the original extraction operation in the sense that the source and each stored claim record were fetched afresh and compared. It is **not** an independent full proof derivation, formal proof, numerical reproduction, or referee-level verification of every theorem.

## 2. Claim-by-claim extraction review

| Claim ID | Source / locator check | Review result | Finding |
|---|---|---|---|
| AS-ALPHA-A-DEF-0001 | Exact excerpt; Section 3, lines 26–44 | PASS | Definition correctly separated from theorem claims |
| AS-ALPHA-A-PROP-0001 | Exact excerpt; Section 2, lines 159–206 | PASS WITH OVERLAP | Contains threshold definition, interior-attainment scaling, tangent condition, and subcritical exclusion |
| AS-ALPHA-A-PROP-0002 | Exact excerpt; Section 3, lines 46–66 | PASS | Tangent identity is correctly transcribed |
| AS-ALPHA-A-THM-0001 | Exact excerpt; Section 3, lines 96–165 | PASS WITH MATHEMATICAL ISSUE | Taylor remainder is stated as cubic while only (C^2) regularity is assumed; see §3.2 |
| AS-ALPHA-A-PROP-0003 | Exact excerpt; Section 3, lines 192–225 | PASS | Full Picard multiplier criterion retained; descending-branch condition is not confused with full stability |
| AS-ALPHA-A-PROP-0004 | Exact excerpt; Section 4, lines 20–34 | PASS | Root-by-root scope and non-uniqueness qualification retained |
| AS-ALPHA-A-PROP-0005 | Exact excerpt; Section 5, lines 42–93 | PASS WITH DOMAIN QUALIFICATION | Decomposition/eigenvalue formulas transcribed; explicit lower bound on (N) is absent from source statement |
| AS-ALPHA-A-THM-0002 | Exact excerpt; Section 2, lines 3–17 | PASS WITH SOURCE PROOF ERROR | Perron–Frobenius shift has the wrong sign as written; see §3.1 |
| AS-ALPHA-A-PROP-0006 | Exact excerpt; Section 2, lines 71–111 | PASS | Positive scalar energy rescaling and dimensionless dependence accurately distinguished from a unitary transformation |
| AS-ALPHA-A-PROP-0007 | Exact excerpt; Section 2, lines 148–155 | PASS | Zero-coupling product state and trivial root correctly transcribed |
| AS-ALPHA-A-PROP-0008 | Exact excerpt; Section 2, lines 197–206 | DUPLICATE / OVERLAPPING | This is already included verbatim as the subcritical-exclusion assertion in PROP-0001; preserve as a traceable duplicate until registry consolidation |
| AS-ALPHA-A-PROP-0009 | Exact excerpt; Section 4, lines 105–120 | PASS WITH CONTEXT/PROOF GAP | The record excerpt omits the immediately preceding (N\ge4) scope sentence; Lemma 5.1 is unresolved and derivative asymptotics require separate remainder control |
| AS-ALPHA-A-PROP-0010 | Exact excerpt; Section 5, lines 17–24 | PASS | Correct upper bound and explicit rejection of the false sign implication retained |
| AS-ALPHA-A-PROP-0011 | Source lines 127–131 identified; stored excerpt omits the numbered-item prefix | MINOR TRANSCRIPTION BOUNDARY FIX | Add the source prefix “3. Scale covariance of perturbations.” to make the excerpt a contiguous verbatim passage |

**Summary:** 13 records have exact source excerpts and locators; PROP-0011 has the correct source location but its excerpt begins mid-item; PROP-0008 is an exact but duplicate/overlapping registration. All 14 source records remain candidates; no mathematical proof status is upgraded.

## 3. Findings requiring mathematical or source correction

### A-REVIEW-001 — Perron–Frobenius matrix shift has the wrong sign

Section 2.1 states that shifting the Hamiltonian by a sufficiently large multiple of the identity makes the resulting matrix nonnegative. But the Hamiltonian has off-diagonal entries (-h) for single-spin flips, with (h>0). Adding (cI) changes only diagonal entries and leaves those off-diagonal entries negative.

The standard Perron–Frobenius route is to apply the theorem to (cI-H) (equivalently, to (-H+cI)), choosing (c) large enough to make its diagonal entries nonnegative. Its off-diagonal single-spin-flip entries are then (+h), and the hypercube configuration graph is connected, giving irreducibility. For finite (N) and finite real couplings, this can establish simplicity of the lowest eigenvalue of (H).

**Disposition:** The conclusion may be correct, but the proof sentence in the source is incorrect as written. Keep THM-0002 CANDIDATE / NOT_VERIFIED until the source proof is corrected or a separate rigorous proof record is supplied. Do not silently repair the source excerpt.

### A-REVIEW-002 — (C^2) regularity does not justify the stated cubic Taylor remainder

Section 3.2 assumes only that (mathcal G_N) is at least (C^2), but writes a remainder of order
[
O(delta g^2+|delta g,delta x|+|delta x|^3).
]
A (C^2) hypothesis generally gives a Peano remainder (o(|delta x|^2)), not an (O(|delta x|^3)) bound. A cubic bound needs stronger control, such as a locally bounded third derivative (or an appropriate Lipschitz condition on the second derivative). The displayed (O(g-g_c)) error in the square-root branch expansion also needs enough regularity to support that order.

**Disposition:** THM-0001 is accurately transcribed but its stated regularity hypotheses do not justify the displayed remainder orders. The theorem must be audited with corrected hypotheses or weaker remainder notation; do not change the theorem in Constant Llapoy by guessing the intended regularity.

### A-REVIEW-003 — Subcritical exclusion is registered twice

PROP-0001 includes the exact subcritical statement
[
eta<alpha_Nimplies f(x;eta)<0
]
under the stated positivity condition on (mathcal G_N). PROP-0008 registers the same source passage as a separate proposition. This is not two independent results.

**Disposition:** Keep both records for audit history, mark PROP-0008 as DUPLICATE_OF PROP-0001 (or merge it into a subclaim after an explicit registry migration). Do not count it as an additional distinct mathematical result.

### A-REVIEW-004 — Strong-coupling derivative asymptotic needs its own proof obligation

Section 4.4.2 gives an asymptotic expansion for (mathcal G_N(x)), then states a derivative expansion for (mathcal G_N'(x)). Differentiating a big-(O) remainder is not justified merely by the function-level asymptotic expansion. The manuscript asserts additional analytic control of the entropy remainder, but the proof is not present in the six revised sections and the cited Lemma 5.1 is absent from the authoritative Section 5.

The source's (N\ge4) condition appears immediately before the asymptotic paragraph and must be included in the claim's assumptions. The stored PROP-0009 excerpt begins at line 105 and currently omits that contextual condition at line 103.

**Disposition:** Keep PROP-0009 CANDIDATE / NOT_VERIFIED. Add the (N\ge4) context and create separate obligations for (i) the function expansion and (ii) the differentiated remainder estimate. Resolve the missing Lemma 5.1 source.

### A-REVIEW-005 — Edge representation decomposition needs an explicit domain

The stated dimensions
[
1,quad N-1,quad rac{N(N-3)}2
]
sum to (inom N2), and the decomposition is the standard edge-permutation representation decomposition for (N\ge3). The formula for the residual sector is not a valid nonnegative dimension at (N=2). The Section 5.2 statement does not explicitly state the minimum (N).

**Disposition:** Add an explicit domain condition (at least (N\ge3)) to the claim's proof obligations; verify whether the paper's intended global model domain is narrower. Do not assume an unstated domain silently.

### A-REVIEW-006 — Lemma references unresolved

Section 4.4.2 refers to Lemma 5.1 and Section 4.4.3 refers to Lemma 5.2. Neither lemma appears in the pinned Section 5. The current authoritative six-section source set therefore does not provide the cited proof dependencies.

**Disposition:** OPEN SOURCE DEPENDENCY. Locate the intended source or correct the upstream cross-references.

### A-REVIEW-007 — Threshold (min) versus (inf) wording

Section 2 defines (alpha_N) by an infimum and only identifies an attained critical point if the infimum is attained in the interior. Section 6 writes a minimum formula and then generalizes to an infimum. The threshold as an infimum of admissible feedback parameters must be distinguished from an attained tangent/fixed-point solution.

**Disposition:** CLARIFICATION REQUIRED; no hidden attainment assumption may be introduced.

## 4. Duplicate and dependency relationships

- `AS-ALPHA-A-PROP-0008` is an exact duplicate/subclaim of the subcritical-exclusion passage already present in `AS-ALPHA-A-PROP-0001`.
- `AS-ALPHA-A-PROP-0002` is the tangent identity obtained from the critical-point equations and is closely dependent on `AS-ALPHA-A-DEF-0001` plus the definitions of (F) and (f).
- `AS-ALPHA-A-THM-0001` depends on the critical-point/tangent setup and on regularity/nondegeneracy assumptions; its displayed remainder requires stronger hypotheses than currently stated.
- `AS-ALPHA-A-PROP-0009` depends on the missing strong-coupling perturbation/entropy-remainder proof source.
- `AS-ALPHA-A-PROP-0011` depends on the dimensionless ground-state scaling recorded in `AS-ALPHA-A-PROP-0006` plus differentiability of the response map.
- `AS-ALPHA-A-PROP-0005` is algebraically distinct from the conjectural sign claim (B-C>0); the latter remains a conjecture and is not promoted into the exact identity record.

These are preliminary dependency observations, not a completed dependency graph.

## 5. Final review disposition

- Claim records freshly fetched and compared: **14/14**.
- Exact source excerpt and line locator confirmed: **13/14**.
- Minor excerpt-boundary correction required: **1** (PROP-0011).
- Duplicate/overlapping registration: **1** (PROP-0008 versus PROP-0001).
- Source-level mathematical/proof issues identified: **Perron–Frobenius sign; Taylor remainder regularity; derivative asymptotic proof dependency; representation domain; missing Lemmas; min/inf distinction**.
- Independent extraction review: **COMPLETED WITH ISSUES** for this 14-record set.
- Proof re-derivation: **NOT COMPLETED**.
- Formal verification / Lean correspondence: **NOT RUN**.
- Constant Llapoy VERIFIED claims: **0**.

No claim is upgraded to VERIFIED. The next step is to correct extraction metadata and record-level review annotations, then create the first explicit dependency/obligation graph without modifying the upstream manuscript.
