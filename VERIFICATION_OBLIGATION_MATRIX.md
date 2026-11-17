# Verification Obligation Matrix
**Project:** Constant Llapoy  
**Repository:** `mytheeramet3dev-x/Constant-Llpoy`  
**Document ID:** CL-VM-001  
**Version:** 0.1.0  
**Status:** Governance specification; not yet populated with audited Absolute Symmetry claims  
**Normative language:** MUST, MUST NOT, SHOULD, and MAY are used as requirements.

---

## 1. Purpose

This document defines the claim-level matrix that determines what evidence is required before any mathematical claim in the Absolute Symmetry research program may be reported as verified.

The matrix connects each precise manuscript claim to its mathematical assumptions, dependencies, proof obligations, computational evidence (where applicable), trust boundaries, threats, reproducibility record, and manuscript correspondence audit.

It is an obligation register, not a proof system. Creating this matrix does not prove any theorem, validate any manuscript, or establish that a toolchain is installed.

## 2. Governing rules

1. **Claim-level scope.** Every theorem, lemma, proposition, corollary, definition with substantive properties, and other assertion requiring mathematical support MUST have a stable claim ID.
2. **Exact statement first.** Verification applies to a frozen, precisely transcribed statement—not to a title, informal summary, or intended result.
3. **No invented claims.** Actual claim IDs, statements, assumptions, and manuscript locations MUST be extracted from the authoritative source. Until then they remain explicitly unpopulated.
4. **Applicability is not a result.** Whether an obligation applies MUST be recorded separately from whether it passed.
5. **Fail closed.** Missing, ambiguous, stale, or unreviewed required cells prevent a Verified status.
6. **No universal tool mandate.** Lean, another proof assistant, CAS, SMT, Python, Rust, numerical analysis, and certificate checking are selected only when justified by the claim and its threat model.
7. **No independence by branding.** Different languages, packages, teams, or executables do not by themselves establish independent verification.
8. **No hidden assumptions.** Every assumption, axiom, imported theorem, domain restriction, and trusted component relevant to the result MUST be disclosed.
9. **Evidence is immutable by reference.** Evidence records MUST identify exact content by commit, digest, version, or another reproducible identifier.
10. **Uncertainty remains visible.** Unknown, inconclusive, and not-run states MUST NOT be silently converted into pass.

## 3. Claim identity and granularity

Each claim MUST receive an ID that remains stable across manuscript edits. Suggested format:

`AS-[SERIES]-[DOCUMENT]-[CLAIM]-[SEQUENCE]`

Example only: `AS-ALPHA-PAPER-X-THM-0001`.

The ID is illustrative and MUST NOT be treated as an actual Absolute Symmetry claim.

A claim MUST be split into separately tracked subclaims when:
- its conclusion contains logically separable results;
- different parts rely on materially different assumptions or proof routes;
- a single pass/fail status would conceal a failed component;
- a computational result is being used to support a distinct mathematical inference.

A claim MAY reference shared definitions or lemmas, but dependency edges MUST be explicit. A parent claim cannot be Verified if a required dependency is unresolved.

## 4. Two-dimensional status model

### 4.1 Applicability status

Every obligation row MUST use exactly one applicability value:

| Value | Meaning |
|---|---|
| REQUIRED | This obligation is necessary for this claim and verification route. |
| NOT_REQUIRED | The obligation was considered and a documented rationale shows it is unnecessary. |
| NOT_APPLICABLE | The obligation does not make mathematical or technical sense for this claim. |
| UNKNOWN | Applicability has not yet been determined. |

A blank applicability cell is invalid and treated as UNKNOWN.

### 4.2 Execution/result status

For every applicable obligation, record exactly one result value:

| Value | Meaning |
|---|---|
| NOT_RUN | No execution or review has been completed. |
| PASS | The defined check completed and met its acceptance criteria. |
| FAIL | The check produced a counterexample, contradiction, mismatch, or unmet criterion. |
| INCONCLUSIVE | The check ran but did not establish pass or fail. |
| BLOCKED | The check could not run because a prerequisite was missing. |
| STALE | Evidence exists but no longer corresponds to the current claim, code, environment, or manuscript revision. |

For NOT_REQUIRED or NOT_APPLICABLE rows, result MUST be recorded as `N/A` with a rationale. UNKNOWN applicability MUST have result `NOT_RUN` or `BLOCKED`, never PASS.

### 4.3 Overall claim status

| Overall status | Minimum meaning |
|---|---|
| UNREGISTERED | Claim has not been entered into the matrix. |
| DRAFT | Claim identity or exact statement is still being established. |
| OBLIGATIONS_OPEN | One or more applicability decisions or required evidence items remain unresolved. |
| IN_PROGRESS | Required checks are being performed. |
| BLOCKED | A required prerequisite, artifact, or environment is unavailable. |
| FAILED | At least one required obligation failed. |
| INCONCLUSIVE | Required checks completed but the result is not decisive. |
| VERIFIED | Every required obligation passed, all correspondence and review gates passed, and no unresolved blocker remains. |
| SUPERSEDED | Claim version was replaced; its historical record is retained. |

A Verified label is scoped to the exact claim version, evidence set, and manuscript revision recorded. It is not a permanent guarantee against later discoveries.

## 5. Mandatory claim record

Every claim record MUST contain the following fields:

| Field | Required content |
|---|---|
| Claim ID | Stable unique identifier |
| Claim version | Version or revision of the statement |
| Claim type | Theorem, lemma, proposition, corollary, definition, conjecture, etc. |
| Series/document | Authoritative paper or project document |
| Manuscript revision | Commit SHA or immutable document digest |
| Location | Section, page, theorem number, and source path |
| Exact statement | Full mathematical statement, including notation |
| Definitions | Definitions needed to interpret the statement |
| Domain | Sets, spaces, structures, topology, fields, dimensions, and other domains |
| Quantifiers | Explicit order and scope of all quantifiers |
| Hypotheses | Every premise and side condition |
| Conclusion | Exact proposition being established |
| Dependencies | Claim IDs and external results used |
| Informal proof | Source location or explicit absence |
| Formal proof | Artifact path, prover, version, and status, if applicable |
| Evidence owner | Responsible person or agent |
| Independent reviewer | Reviewer distinct from the evidence producer where required |
| Overall status | Status from Section 4.3 |
| Last reviewed | Timestamp and reviewer |
| Evidence index | Links/paths and immutable identifiers for all artifacts |

No statement may be reconstructed from memory or inferred from a paper title when the authoritative source is unavailable.

## 6. Obligation catalogue

The following catalogue defines the rows to instantiate for each claim. Applicability MUST be decided claim by claim.

### A. Statement and mathematical specification

- **A01 — Statement fidelity:** Is the exact claim transcribed without strengthening, weakening, or omission?
- **A02 — Definitions:** Are all symbols and terms defined unambiguously?
- **A03 — Domain and typing:** Are domains, codomains, dimensions, structures, and type constraints explicit?
- **A04 — Quantifier scope:** Are universal/existential quantifiers and their order correct?
- **A05 — Hypothesis completeness:** Are all premises, regularity conditions, non-degeneracy conditions, and side assumptions stated?
- **A06 — Edge cases:** Are boundary, empty, zero, singular, degenerate, and exceptional cases addressed where relevant?
- **A07 — Logical form:** Is the conclusion exactly the intended implication/equivalence/existence/uniqueness statement?
- **A08 — Counterexample review:** Have plausible counterexamples and failure modes been actively sought?

### B. Dependency and proof structure

- **B01 — Dependency closure:** Are all internal lemmas and definitions identified?
- **B02 — Dependency status:** Are all required dependencies verified at compatible versions?
- **B03 — External theorem provenance:** Are external results precisely cited, with assumptions checked?
- **B04 — Circularity:** Has circular reasoning and hidden dependence on the target claim been excluded?
- **B05 — Proof completeness:** Does every inference follow from stated premises and accepted rules?
- **B06 — Case coverage:** Are all cases exhaustive and mutually handled as claimed?
- **B07 — Existence/uniqueness:** Where asserted, are existence and uniqueness separately established?

### C. Formal proof obligations

- **C01 — Formalization fidelity:** Does the formal statement match the frozen manuscript statement?
- **C02 — Kernel/checker result:** Does the proof assistant's trusted checking process accept the proof?
- **C03 — Axioms and assumptions:** Are all axioms, admitted results, sorry/admit placeholders, and imported assumptions enumerated?
- **C04 — Dependency audit:** Are imported libraries and theorem dependencies identified and version-pinned?
- **C05 — Trust configuration:** Are unsafe extensions, custom axioms, plugins, external oracles, and relevant kernel options disclosed?
- **C06 — Proof artifact reproducibility:** Can the exact proof be rebuilt and checked from recorded sources and environment?
- **C07 — Independent formalization:** Is a second formalization/prover required by the threat model? If so, is it genuinely independent enough for the stated purpose?

A successful formal proof establishes the formalized proposition under the formal system's axioms and trusted base. It does not by itself establish that the formalization faithfully represents the intended manuscript claim.

### D. Exact symbolic/computational evidence

- **D01 — Computational necessity:** Is computation needed for this claim, or is a direct mathematical proof sufficient?
- **D02 — Exactness:** If computation is used, are arithmetic and symbolic operations exact rather than floating-point approximations?
- **D03 — Independent derivation:** Is the computational result derived independently from the proof route where required?
- **D04 — Certificate production:** If a large computation is used, does it produce a compact, checkable certificate where feasible?
- **D05 — Certificate checker:** Is the certificate checked by a smaller, separately assessed checker?
- **D06 — Algorithm validity:** Are algorithm preconditions, termination, completeness, and soundness justified?
- **D07 — Resource limits:** Are timeouts, memory limits, truncation, and incomplete search recorded?
- **D08 — Reproducibility:** Are input, source, parameters, software versions, and exact output preserved?

A CAS output or successful script execution is evidence only for the computation actually performed. It is not automatically a proof of the mathematical theorem.

### E. Software implementation and independent checks

- **E01 — Python role:** Is Python used? If yes, state whether it is a producer, checker, test harness, or orchestration layer.
- **E02 — Rust role:** Is Rust used? If yes, state the same role and the exact property it checks.
- **E03 — Implementation correspondence:** Is the implementation shown to encode the intended mathematical object and algorithm?
- **E04 — Differential testing:** Are independently implemented routes compared where useful?
- **E05 — Common-mode analysis:** Do implementations share algorithms, libraries, specifications, generated code, or assumptions that undermine independence?
- **E06 — Defect controls:** Are tests, static analysis, dependency audits, and review appropriate to the risk?
- **E07 — Failure behavior:** Are errors, overflow, panic, undefined behavior, precision loss, and invalid inputs handled?
- **E08 — Independent checker scope:** Is the checker materially simpler than the producer and does it validate the relevant certificate/property rather than repeat the same computation?

Using Python and Rust does not automatically constitute two independent proofs. Independence must be argued at the level of specification, algorithm, implementation, dependencies, and checking logic.

### F. Numerical evidence

- **F01 — Numerical necessity:** Does the claim genuinely require numerical evidence?
- **F02 — Error bounds:** Are rounding, truncation, discretization, and conditioning errors bounded?
- **F03 — Stability:** Is the computation stable over the relevant parameter range?
- **F04 — Precision sensitivity:** Are results checked under justified precision changes?
- **F05 — Certified numerics:** If a rigorous numerical conclusion is needed, are interval/arbitrary-precision or other certified methods used?
- **F06 — Scope limitation:** Is numerical evidence clearly distinguished from exact proof?

Numerical agreement, plots, and finite sampling cannot establish a universal theorem unless a separate rigorous argument justifies that inference.

### G. Assumptions, trust, and security

- **G01 — Assumption ledger:** Are all mathematical and environmental assumptions recorded?
- **G02 — TCB declaration:** Is the claim-specific trusted computing base identified?
- **G03 — Trust-boundary mapping:** Are relevant TB identifiers from the TCB inventory linked?
- **G04 — Threat mapping:** Are relevant threat IDs from the threat model linked?
- **G05 — Dependency integrity:** Are dependencies pinned and their provenance/integrity assessed?
- **G06 — Build integrity:** Is the build environment and toolchain recorded sufficiently to reproduce the check?
- **G07 — Agent/human review:** Are AI-agent contributions and human decisions traceable and reviewed?
- **G08 — Residual risk:** Are risks that remain after checks explicitly stated?

### H. Manuscript correspondence and release

- **H01 — Statement correspondence:** Does the formal/computational claim match the manuscript statement exactly?
- **H02 — Proof correspondence:** Does the manuscript proof explain the same argument as the evidence artifacts?
- **H03 — Citation correspondence:** Are external citations accurate and sufficient?
- **H04 — Revision synchronization:** Are manuscript and evidence revisions synchronized?
- **H05 — Reproducibility package:** Can a reviewer obtain and run the necessary artifacts?
- **H06 — Independent review:** Has an appropriate reviewer examined the claim and its evidence?
- **H07 — Status approval:** Has the required reviewer approved the exact claim version?
- **H08 — Change impact:** Have changes since the last verified revision triggered re-evaluation of affected obligations?


### I. Foundations, satisfiability, and non-vacuity (L-13)

For each claim, record the foundations, axioms, transitive assumptions, and joint hypotheses. Assess whether the hypotheses can hold simultaneously and whether the intended domain contains admissible instances. Distinguish consistency of a logic, relative consistency of a theory, satisfiability of a hypothesis set, and realizability in an intended model. Record witnesses/models or relative-consistency evidence where available. Do not treat a failed search as proof of inconsistency, or kernel acceptance as a consistency proof. Unknown or undecidable questions remain open.

### J. Model adequacy and applicability (L-14)

For claims about physical, empirical, computational, or other external targets, record the target-to-model mapping, omitted mechanisms, idealizations, parameter interpretation, boundary conditions, and applicability regime. Assess whether the theorem's conclusion stays within that regime and whether finite/discrete-to-continuum or thermodynamic extrapolations have a justified bridge. Separate mathematical correctness from model adequacy, empirical fit, explanatory relevance, and predictive validity. For pure mathematical claims, record a reasoned non-applicability decision.

### K. Verification-system assurance / meta-verification (L-08, L-10, L-11, L-12)

For each verification route, apply `META_VERIFICATION_SPECIFICATION.md` as the normative design. Inventory every status-affecting validator, parser, certificate checker, workflow, evidence schema, report generator, and status aggregator; assign stable component IDs, owners, trust classifications, exact revisions, dependencies, and claim impact. Define checker input/output contracts and distinguish ACCEPTED, REJECTED, ERROR, TIMEOUT, INCONCLUSIVE, and NOT_RUN. Execute positive, negative, malformed-input, boundary, mutation, fault-injection, regression, and differential tests as applicable; preserve surviving mutations and shared dependencies. Bind each result to the exact claim, source, checker, schema, workflow, dependency, and artifact revisions. Test fail-closed aggregation against missing, skipped, stale, failed, timed-out, inconclusive, contradictory, and partial evidence. Require independent review for high-impact acceptance logic or explicitly record that it is absent. Self-tests are not a proof of verifier correctness; residual trust and limitations must remain explicit.
## 7. Tool selection and applicability rationale

For each tool family below, the matrix MUST record one of REQUIRED, NOT_REQUIRED, NOT_APPLICABLE, or UNKNOWN, plus a rationale.

| Tool/evidence family | When it may be required | What it cannot establish by itself |
|---|---|---|
| Lean 4 | Formal proof route selected for the claim | Manuscript/formalization fidelity |
| Isabelle/HOL or Rocq/Coq | Independent or alternative formal route justified by risk | Independence merely from using a different prover |
| Python | Exact computation, orchestration, testing, or data processing | Correctness merely because tests pass |
| Rust | Implementation, independent checker, or systems-level validation | Mathematical correctness of its specification |
| SymPy/SageMath | Symbolic/exact algebraic computation | Soundness of an unreviewed algorithm or theorem inference |
| Z3/cvc5 | Decision procedures or bounded/SMT obligations within justified scope | General theorem truth outside encoded logic and assumptions |
| Certificate checker | Independent validation of a producer's result | Correctness of the theorem-to-certificate translation |
| Numerical tools | Approximation, exploration, or certified numerical analysis | Exact universal conclusions from finite samples |
| CI/container/Nix | Reproducible execution and environment control | Correctness of the mathematical argument |

The rationale MUST explain why a tool is or is not needed for this particular claim. Cost, convenience, or a desire to achieve a fixed number of layers is not sufficient justification.

## 8. Independence assessment

Where independent evidence is required, record:

1. The precise proposition/property independently checked.
2. Whether the specification was independently derived or merely copied.
3. Whether the algorithm is distinct.
4. Whether the implementation is distinct.
5. Shared libraries, dependencies, compilers, runtimes, hardware, and generated artifacts.
6. Shared human or AI reasoning and review.
7. The checker’s trusted base and complexity.
8. Remaining common-mode failure scenarios.

Use one independence classification:

- **I0 — Same route:** No meaningful independence.
- **I1 — Implementation diversity:** Different implementation, substantial shared specification/algorithm.
- **I2 — Algorithmic diversity:** Distinct algorithmic route, but notable shared assumptions or infrastructure.
- **I3 — Strongly separated route:** Independently derived specification/argument and materially distinct algorithm/checking path; residual common modes documented.
- **I4 — Independently reviewed formal route:** A separate formalization or proof route with independently assessed assumptions and trust base.

These labels describe the evidence relationship, not an absolute guarantee. A claim MUST NOT be called independently verified solely because two programming languages or tools were used.

## 9. Threat and trust-boundary mapping

Every claim MUST link applicable identifiers from:
- `THREAT_MODEL.md` (T01–T21);
- `TRUST_BOUNDARY_TCB_INVENTORY.md` (TB-01–TB-24);
- `TOOLCHAIN_DEPENDENCY_INVENTORY.md` (relevant tool/dependency entries).

The identifiers above are catalogue ranges, not a statement that every threat or boundary applies to every claim. If none apply, the reviewer MUST document why. If a new threat or boundary is discovered, update the governing inventory and link it; do not force it into an inaccurate existing category.

## 10. Evidence record schema

Each executed obligation MUST reference an evidence record containing, as applicable:

- Evidence ID and obligation ID.
- Claim ID and exact claim version.
- Artifact path and immutable commit/digest.
- Source code, input data, certificate, and output.
- Tool name, exact version, build identifier, and configuration.
- Operating system, architecture, runtime, and relevant environment details.
- Reproduction command and expected result.
- Actual result, exit code, logs, and limitations.
- Producer and reviewer identities/roles.
- Timestamp in an unambiguous timezone.
- Dependency and provenance record.
- Related threat and trust-boundary IDs.

Evidence MUST be retained when a claim is superseded. A new revision MUST create a new evidence association; it MUST NOT silently overwrite historical evidence.

## 11. Required matrix template

Copy this template for every claim. Add or split rows whenever the claim's mathematical structure or threat model requires it.

| Obligation ID | Applicability | Rationale | Result | Evidence ID/path + digest | Reviewer | Threat IDs | TB IDs |
|---|---|---|---|---|---|---|---|
| A01 | UNKNOWN | Pending source inspection | NOT_RUN | — | — | — | — |
| A02 | UNKNOWN | Pending source inspection | NOT_RUN | — | — | — | — |
| A03 | UNKNOWN | Pending source inspection | NOT_RUN | — | — | — | — |
| A04 | UNKNOWN | Pending source inspection | NOT_RUN | — | — | — | — |
| A05 | UNKNOWN | Pending source inspection | NOT_RUN | — | — | — | — |
| B01 | UNKNOWN | Pending dependency analysis | NOT_RUN | — | — | — | — |
| B02 | UNKNOWN | Pending dependency analysis | NOT_RUN | — | — | — | — |
| C01 | UNKNOWN | Formalization route not selected | NOT_RUN | — | — | — | — |
| C02 | UNKNOWN | Formalization route not selected | NOT_RUN | — | — | — | — |
| C03 | UNKNOWN | Axiom audit not performed | NOT_RUN | — | — | — | — |
| D01 | UNKNOWN | Computational necessity not assessed | NOT_RUN | — | — | — | — |
| E01 | UNKNOWN | Implementation role not assessed | NOT_RUN | — | — | — | — |
| E02 | UNKNOWN | Implementation role not assessed | NOT_RUN | — | — | — | — |
| F01 | UNKNOWN | Numerical necessity not assessed | NOT_RUN | — | — | — | — |
| G01 | UNKNOWN | Assumption ledger not populated | NOT_RUN | — | — | — | — |
| G02 | UNKNOWN | Claim-specific TCB not declared | NOT_RUN | — | — | — | — |
| H01 | UNKNOWN | Correspondence audit not performed | NOT_RUN | — | — | — | — |
| H06 | UNKNOWN | Independent review not recorded | NOT_RUN | — | — | — | — |

This compact template is a starting set, not an exhaustive fixed list. The full catalogue in Section 6 MUST be considered. Rows may be added; none may be removed without a recorded applicability decision and rationale.

## 12. Illustrative example (not an Absolute Symmetry result)

The following is a deliberately simple, fictional example to demonstrate how applicability decisions work. It is not a theorem from any Absolute Symmetry paper and MUST NOT be copied into the project claim register as an actual result.

**Example claim:** For every integer (n), (n+n=2n).

| Obligation | Applicability | Rationale | Result |
|---|---|---|---|
| A01 exact statement | REQUIRED | The quantified integer statement must be fixed | PASS only after statement review |
| A03 domain | REQUIRED | Integer domain is material | PASS only after type/domain review |
| B05 proof completeness | REQUIRED | A mathematical derivation is needed | NOT_RUN in this illustration |
| C01 formalization fidelity | REQUIRED if Lean route is selected | Formal statement must match the claim | NOT_RUN |
| D01 computational necessity | NOT_REQUIRED | A direct algebraic proof suffices for this elementary example | N/A |
| E01 Python | NOT_REQUIRED | Python adds no necessary evidence here | N/A |
| E02 Rust | NOT_REQUIRED | Rust adds no necessary evidence here | N/A |
| F01 numerical evidence | NOT_APPLICABLE | The claim is exact over integers, not numerical approximation | N/A |
| G02 TCB declaration | REQUIRED for any formal/computational evidence route | Trust assumptions must be explicit | NOT_RUN |
| H01 correspondence | REQUIRED | Evidence and manuscript must agree | NOT_RUN |

Even in this example, the overall claim cannot be called Verified while required proof and review obligations remain NOT_RUN. The PASS wording in the first two rows describes the acceptance condition, not a claim that this example has actually been audited.

## 13. Verification decision gate

A claim may transition to VERIFIED only when all conditions below hold:

1. Claim identity, exact statement, version, and manuscript location are frozen.
2. Every catalogue obligation has an explicit applicability decision.
3. Every REQUIRED obligation has result PASS and traceable evidence.
4. Every NOT_REQUIRED or NOT_APPLICABLE decision has a specific, reviewed rationale.
5. No UNKNOWN, NOT_RUN, FAIL, INCONCLUSIVE, BLOCKED, or STALE required item remains.
6. All dependencies are resolved and version-compatible.
7. Assumptions, axioms, imported results, and claim-specific TCB are disclosed.
8. Formalization and manuscript correspondence audits pass where applicable.
9. Required independent review is complete.
10. Evidence can be reproduced or any justified reproducibility limitation is explicitly accepted under a documented policy that does not overstate the result.
11. The final status is approved for the exact claim and manuscript revision.

A failed required obligation makes the claim FAILED until the issue is resolved and re-reviewed. A changed statement, dependency, proof artifact, checker, or relevant environment may invalidate affected evidence and require re-verification.

## 14. Change control and invalidation

The following changes MUST trigger impact analysis and may invalidate evidence:
- Any change to hypotheses, domains, quantifiers, definitions, or conclusion.
- Any change to a dependency lemma or external theorem version.
- Any change to formal source, axioms, imports, or proof assistant configuration.
- Any change to computation code, algorithm, input, certificate format, or checker.
- Any change to dependency versions, compiler, runtime, build image, or relevant hardware.
- Any manuscript edit that changes claim meaning or proof correspondence.
- Any newly discovered counterexample, vulnerability, or common-mode dependency.

Impact analysis MUST identify affected claim IDs and obligation rows. Historical evidence remains preserved and marked STALE or SUPERSEDED as appropriate.

## 15. Reviewer checklist

A reviewer should be able to answer YES to all applicable questions:

- Is the exact claim identifiable and stable?
- Are definitions, domains, quantifiers, hypotheses, and conclusion explicit?
- Are dependencies complete and non-circular?
- Is the proof valid for the exact statement?
- Are all formal axioms and trusted components disclosed?
- Are computational algorithms and certificates justified?
- Are Python/Rust roles and independence claims accurately characterized?
- Are numerical results bounded and correctly limited?
- Are threat and trust-boundary mappings complete?
- Can evidence be reproduced and independently inspected?
- Does the manuscript say no more than the evidence establishes?
- Are unresolved risks and limitations visible?
- Have L-13 consistency, joint satisfiability, and non-vacuity obligations been assessed where material?
- Has L-14 model adequacy and applicability been assessed for external/applied claims?
- Are countermodel searches distinguished from proofs of independence or necessity?
- Are structural robustness checks distinguished from numerical stability checks?
- Are validators, parsers, certificate checkers, CI orchestration, report generation, and status aggregation covered by meta-verification obligations (T21)?

A NO or UNKNOWN answer blocks VERIFIED status.

## 16. Current population status

At version 0.1.0, this matrix is a governance specification only.

- Actual Absolute Symmetry claim records: **not yet populated in this document**.
- Exact theorem statements: **not asserted here**.
- Claim-level applicability decisions: **not yet performed**.
- Lean/Rocq/Isabelle proof results: **not asserted here**.
- Python/Rust implementation results: **not asserted here**.
- CAS/SMT/certificate results: **not asserted here**.
- Claim-level independent reviews: **not asserted here**.
- Any paper's verified status: **not established by this document**.

The next population task is to inspect authoritative manuscript and source revisions, enumerate claims without omission, assign stable IDs, and fill each claim record with exact text and source locations. Only after that should claim-specific verification routes and tool layers be designed.

## 17. Relationship to governing documents

This matrix MUST be read together with:
- `ARCHITECTURE_CHARTER.md` — governing mission, principles, evidence policy, and verification architecture.
- `14_LAYER_VERIFICATION_STANDARD.md` — provisional 14-layer candidate standard.
- `THREAT_MODEL.md` — threat catalogue and adversarial failure scenarios.
- `TRUST_BOUNDARY_TCB_INVENTORY.md` — trust boundaries and trusted computing base inventory.
- `TOOLCHAIN_DEPENDENCY_INVENTORY.md` — candidate tools, dependency controls, and environment acceptance gates.

If these documents conflict, do not silently choose the more permissive interpretation. Record the conflict, preserve the stricter safety posture temporarily, and resolve it through documented change control.

---

**End of document.**  
**Document status:** Specification committed; claim population and actual verification remain outstanding.
