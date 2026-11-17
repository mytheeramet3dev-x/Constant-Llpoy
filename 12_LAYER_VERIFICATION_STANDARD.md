# Constant Llapoy — 12-Layer Verification Standard

**Document status:** Approved architecture baseline; implementation and validation remain layer- and claim-specific  
**Version:** 1.0.0  
**Effective date:** 2026-11-18  
**Parent documents:** `ARCHITECTURE_CHARTER.md`, `THREAT_MODEL.md`  
**Catalog:** `LAYER_CATALOG.md`  
**Scope:** Independent, claim-centered verification infrastructure for the Absolute Symmetry research program  
**Normative language:** MUST and MUST NOT are mandatory; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Decision and governing scope

The project adopts **12 named verification layers** as its current architecture baseline. This is a consolidation and refinement of the prior ten-function conceptual catalog, with three additional functions incorporated through a deliberate merge:

- Literature and prior-art positioning is integrated with mathematical claim specification in Layer 1.
- Boundary, domain, and scope-quantifier auditing is a dedicated Layer 3.
- Manuscript-to-artifact traceability and synchronization is a dedicated Layer 10.

The prior ten functions are preserved in substance and mapped to the new architecture in Section 5. No original verification obligation is silently discarded.

The number twelve is the approved organization of the current catalog, **not a permanent cap on the architecture**. The Architecture Charter remains controlling: a layer may be split, merged, replaced, or supplemented when a documented threat or verification obligation requires it. Any such change requires versioned rationale and migration analysis. Twelve is not a quality score, completion target, or guarantee that all possible failure modes have been eliminated.

This document specifies architecture and acceptance requirements. It does not certify that all twelve layers have been implemented, that every layer applies to every claim, or that any paper is thereby verified.

## 2. Foundational rules

1. **The claim is the unit of verification.** Every result must identify the exact claim, source revision, definitions, assumptions, domain, quantifiers, and conclusion.
2. **No weakening to obtain a pass.** A failed or difficult proof must not be made to pass by silently narrowing a domain, changing quantifiers, adding unapproved assumptions, or weakening the conclusion.
3. **No evidence laundering.** A build, test, numerical match, symbolic output, literature citation, or green CI job is not automatically a mathematical proof.
4. **Correspondence is mandatory.** A correct proof of the wrong formal proposition does not verify the manuscript claim.
5. **Independence must be demonstrated.** Different languages, vendors, repositories, or tools do not establish independence by themselves.
6. **Failure and uncertainty remain visible.** Failed, stale, unavailable, skipped, and inconclusive checks must be reported accurately.
7. **Applicability is claim-specific.** A layer may be marked not applicable only with a written mathematical and threat-based justification.
8. **Residual risk is never hidden.** Passing every currently required check does not imply the absence of unknown threats or unmodeled failure modes.

## 3. Architecture map

| ID | Layer | Primary function |
|---|---|---|
| L-01 | Literature, Prior-Art, and Mathematical Claim Specification | Position the claim in existing knowledge and freeze its exact mathematical meaning |
| L-02 | Semantic Correspondence and Formalization Audit | Check that translations and formal statements preserve meaning |
| L-03 | Boundary, Domain, and Scope-Quantifier Audit | Audit domains, boundary cases, quantifier order, parameter dependence, and uniformity |
| L-04 | Primary Kernel-Checked Formal Verification (Lean 4) | Establish formal derivations checked by the designated Lean kernel |
| L-05 | Independent Formal-Proof Route | Recheck selected claims through a technically independent formal route |
| L-06 | Exact Computational Verification | Check exact finite/algebraic consequences with justified algorithms |
| L-07 | Independent Implementation Cross-Checks | Detect implementation defects using separately developed implementations |
| L-08 | Proof-Certificate Production and Independent Checking | Separate complex result production from auditable certificate checking |
| L-09 | Numerical Analysis and Adversarial Testing | Search for counterexamples and assess numerical behavior and edge cases |
| L-10 | Manuscript-to-Artifact Traceability and Synchronization | Maintain end-to-end links and detect drift among manuscripts, specifications, proofs, code, and reports |
| L-11 | Trust, Axiom, Dependency, and Supply-Chain Audit | Expose and assess trusted components, assumptions, dependencies, and provenance |
| L-12 | Reproducibility, Independent Review, and Evidence Governance | Make evidence reproducible, reviewable, and honestly reported |

The identifiers are stable references for the current architecture version. They do not prescribe a rigid execution order. Some checks must occur early and recur after changes; others are conditional on the claim and its threat model.

## 4. Layer specifications

Every layer below defines its purpose, threat coverage, required inputs, required outputs, and acceptance conditions. A layer is not operational merely because this specification names it.

### L-01 — Literature, Prior-Art, and Mathematical Claim Specification

**Purpose:** Establish both what is being claimed and how that claim relates to existing mathematical and scientific knowledge.

**Threats addressed:** Ambiguous or unstable claims; omitted definitions; mistaken novelty assertions; rediscovery presented as novelty; failure to identify equivalent or stronger prior results; incorrect attribution; hidden dependence on external results.

**Required inputs:**
- The exact manuscript and version under review.
- Source references, definitions, notation, cited theorems, and supporting materials.
- A literature-search protocol appropriate to the claim and field.
- The proposed novelty statement, if novelty is asserted.

**Required responsibilities:**
- Freeze each claim under a stable identifier and preserve its source location.
- Record the exact statement, mathematical objects, definitions, hypotheses, domains, quantifiers, side conditions, and conclusion.
- Identify dependencies on prior definitions, lemmas, theorems, conventions, and external results.
- Search and record relevant prior art, including equivalent formulations, stronger/weaker results, known special cases, counterexamples, and adjacent results.
- Distinguish established background, adaptation/application, new proof, new method, new theorem, conjecture, and unresolved question.
- State the novelty boundary precisely; do not infer novelty from an unsuccessful search.
- Record search scope, databases or sources consulted, query terms, dates, inclusion/exclusion criteria, and unresolved literature uncertainty.

**Required outputs:** Versioned claim record; exact mathematical specification; dependency and citation map; literature/prior-art review record; novelty classification and limitations; unresolved-ambiguity list.

**Acceptance conditions:**
- The claim is unambiguous enough for independent mathematical review.
- All material definitions and assumptions are recorded.
- Prior-art conclusions are supported by traceable sources and a disclosed search method.
- Novelty statements are no stronger than the evidence.
- Any unresolved ambiguity or literature uncertainty is explicit.

**Failure conditions:** Missing source provenance; materially ambiguous statement; unrecorded assumptions; unsupported novelty claim; or a known relevant prior result omitted without explanation.

**Important boundary:** A literature review does not prove a theorem. A claim may be mathematically true but not novel; it may be novel but false. These judgments must remain separate.

### L-02 — Semantic Correspondence and Formalization Audit

**Purpose:** Establish that each formal or computational representation means the same thing as the intended mathematical claim.

**Threats addressed:** Translation errors, formalization drift, changed definitions, omitted hypotheses, mismatched objects, and proof of a nearby but easier proposition.

**Required inputs:** The frozen L-01 claim; manuscript definitions; formal propositions; notation maps; dependency declarations; relevant code or symbolic representations.

**Required responsibilities:**
- Trace manuscript statement → mathematical specification → formal statement or computational predicate.
- Compare definitions, types, structures, domains, quantifiers, hypotheses, side conditions, exceptional cases, and conclusions.
- Identify every added, removed, strengthened, weakened, or transformed assumption.
- Review coercions, encodings, quotient constructions, finite representations, and library abstractions where they affect semantics.
- Require mathematical justification for each equivalence or translation step.
- Separate exact equivalence from one-way implication, approximation, special-case formalization, or conjectural correspondence.

**Required outputs:** Claim-to-artifact correspondence record; explicit translation rationale; discrepancy log; reviewer decision; unresolved correspondence obligations.

**Acceptance conditions:** Every material semantic transformation is justified, and the formal proposition is equivalent to the intended claim or its precisely declared sub-obligation. Any weaker or partial result is labeled as such and is not counted as verification of the full claim.

**Failure conditions:** Silent semantic change; missing hypothesis; wrong object or domain; unexplained strengthening/weakening; or unresolved material mismatch.

### L-03 — Boundary, Domain, and Scope-Quantifier Audit

**Purpose:** Challenge the exact scope of a claim, especially where boundary behavior, quantifier order, parameter dependence, or hidden regularity assumptions can invalidate an apparently plausible result.

**Threats addressed:** Wrong domains; omitted endpoints; singular or degenerate cases; quantifier reversal; non-uniform estimates presented as uniform; constants with hidden parameter dependence; unjustified exchanges of limits, derivatives, sums, or integrals.

**Required inputs:** Frozen claim and definitions from L-01; semantic map from L-02; parameter ranges; proof dependencies; theorem statements and estimates.

**Required responsibilities:**
- Audit open, closed, half-open, finite, infinite, empty, and degenerate domains as applicable.
- Check endpoints, boundary cases, zero values, singularities, limiting regimes, and excluded parameter values.
- Parse quantifier order explicitly, including statements such as ∀ε ∃δ, ∃C ∀N, and parameter-dependent existence.
- Check whether constants depend on parameters, dimension, system size, discretization, or other variables.
- Distinguish pointwise, local, compact-uniform, and global-uniform claims.
- Audit asymptotic notation and remainder terms for their exact limiting regime and dependence on fixed or varying parameters.
- Check regularity requirements for differentiation, Taylor expansions, implicit-function arguments, eigenvalue branches, and limit exchanges.
- Check whether hypotheses are sufficient and whether apparently stronger assumptions are actually used.
- Identify counterexamples at excluded boundaries and test whether exclusions are justified by the mathematics.

**Required outputs:** Domain and quantifier audit table; boundary-case inventory; parameter-dependence map; uniformity/regularity checklist; counterexample or justification record; unresolved scope obligations.

**Acceptance conditions:** The stated scope is explicit; every relevant boundary and quantifier obligation is discharged or transparently marked open; all constants and uniformity claims have justified dependence; and no unapproved scope change has occurred.

**Failure conditions:** A universal claim supported only pointwise; a hidden parameter dependence; an omitted boundary case; a quantifier mismatch; or an unsupported regularity/uniformity step.

### L-04 — Primary Kernel-Checked Formal Verification (Lean 4)

**Purpose:** Construct formal derivations whose proof terms are checked by the designated Lean kernel.

**Threats addressed:** Invalid deductive steps within the formal system; informal gaps; untracked axioms or admissions; errors in formal proof construction, subject to the declared kernel and trusted computing base.

**Required inputs:** Approved formal statement and correspondence record; pinned Lean toolchain and Mathlib revision; explicit assumptions; dependency and trust-boundary records.

**Required responsibilities:**
- Formalize the approved proposition without silently changing its meaning.
- Construct proof terms accepted by the Lean kernel.
- Record theorem declarations, source revision, imports, toolchain, dependency lock, and build instructions.
- Inspect axioms, admissions, unsafe declarations, external oracles, and trust extensions.
- Keep helper lemmas and conditional results distinguishable from the target theorem.
- Preserve failing builds and proof gaps; do not suppress errors or weaken the theorem to force acceptance.

**Required outputs:** Lean source revision; theorem declaration; reproducible build log; axiom/trust report; dependency snapshot; L-02 correspondence link.

**Acceptance conditions:** The exact intended formal proposition builds under the pinned environment; no prohibited or undisclosed proof escape is present; dependencies and axioms are disclosed; and correspondence is independently reviewed.

**Failure conditions:** Build failure; unresolved proof obligation; prohibited admission; undisclosed axiom/oracle; stale or unpinned dependencies; or a theorem that does not correspond to the target claim.

**Important boundary:** A Lean build pass proves only that the formal declarations are accepted under the stated Lean environment and assumptions. It does not by itself prove that the manuscript claim was faithfully formalized or that the theorem is novel.

### L-05 — Independent Formal-Proof Route

**Purpose:** Recheck selected high-value claims through a genuinely distinct formal proof system or independently trusted proof-checking route.

**Threats addressed:** Common-mode errors specific to one prover, kernel, library, formalization, or proof-development path.

**Required inputs:** Frozen mathematical claim; L-02 correspondence record; independence requirements; candidate proof systems and dependency inventories.

**Required responsibilities:**
- Select claims for independent formalization based on mathematical importance and risk.
- Encode the statement independently rather than mechanically translating generated proof code.
- Compare definitions, assumptions, theorem strength, and conclusions across routes.
- Analyze shared libraries, algorithms, specifications, kernels, compilers, code generators, external oracles, and human assumptions.
- Document where independence is partial rather than absolute.

**Required outputs:** Independent formal artifact; separate toolchain/dependency record; cross-route statement comparison; independence matrix; common-mode failure analysis.

**Acceptance conditions:** The route is technically distinct in the failure modes it is intended to challenge, the exact proposition is compared, and residual shared assumptions are disclosed.

**Failure conditions:** A wrapper around the primary proof; copied/generated proof with no independent reasoning; materially different propositions; or unsupported claims of independence.

**Applicability:** Not every claim requires a second prover. Non-applicability requires a written risk-based rationale; it must not be inferred from cost or inconvenience alone.

### L-06 — Exact Computational Verification

**Purpose:** Check finite, algebraic, combinatorial, or otherwise exactly representable consequences with explicit algorithmic correctness.

**Threats addressed:** Hand-calculation errors; incorrect finite enumeration; implementation defects in exact arithmetic; invalid symbolic transformations; and false confidence from approximate computation.

**Required inputs:** Exact mathematical subproblem; exact input encoding; algorithm specification; correctness argument; independent-checking plan.

**Required responsibilities:**
- Prefer exact integer, rational, algebraic, or other rigorously specified representations where feasible.
- State the algorithm and its mathematical correctness basis.
- Record exceptional cases, complexity constraints, and representation limits.
- Distinguish theorem-backed symbolic transformations from heuristic simplification.
- Make finite exhaustive checks explicit about the exact finite universe enumerated.
- Provide independently checkable outputs or proofs of algorithm correctness.

**Required outputs:** Exact input data; algorithm and version; result; correctness basis; reproducible execution record; independent check or explicit limitation.

**Acceptance conditions:** Arithmetic and representation semantics are exact and specified; algorithm correctness is justified for the declared domain; and the conclusion does not exceed the finite or algebraic scope actually checked.

**Failure conditions:** Floating-point substitution presented as exact; heuristic output presented as proof; incomplete enumeration presented as exhaustive; or an algorithm used outside its proved domain.

### L-07 — Independent Implementation Cross-Checks

**Purpose:** Detect implementation defects by comparing separately authored implementations whose independence has been technically assessed.

**Threats addressed:** Bugs in one implementation; accidental dependence on a single library or algorithm; shared implementation assumptions mistaken for independent confirmation.

**Required inputs:** Exact or operational specification; reference test vectors; candidate implementations; dependency and toolchain records.

**Required responsibilities:**
- Develop separate implementations where a second implementation provides meaningful assurance.
- Prefer distinct algorithms for high-value checks when feasible.
- Compare exact outputs where possible and explain tolerances where not.
- Audit shared algorithms, libraries, specifications, generated code, compilers, runtimes, data sources, and test oracles.
- Preserve disagreements as first-class findings; do not choose the preferred output without investigation.

**Required outputs:** Source revisions; build/environment locks; test vectors; comparison report; independence assessment; discrepancy and resolution records.

**Acceptance conditions:** Each implementation is reproducible; comparison inputs and semantics match; independence claims are bounded by evidence; and every discrepancy is resolved or remains visibly open.

**Failure conditions:** Merely wrapping one implementation; comparing different mathematical objects; shared hidden dependencies; or discarding disagreement without analysis.

### L-08 — Proof-Certificate Production and Independent Checking

**Purpose:** Separate potentially complex result production from a smaller, auditable checker that validates a well-defined certificate.

**Threats addressed:** Producer bugs; malformed or ambiguous certificates; overlarge checker trust bases; shared producer-checker defects; and acceptance of invalid evidence.

**Required inputs:** Certificate semantics; producer and checker specifications; target mathematical claim; adversarial certificate cases; TCB declaration.

**Required responsibilities:**
- Define canonical certificate syntax and mathematical meaning.
- Treat producers as untrusted unless separately justified.
- Keep checkers small and auditable where feasible.
- Test valid, invalid, malformed, truncated, duplicated, boundary, and adversarial certificates.
- Analyze whether producer and checker share code, libraries, parsers, algorithms, or assumptions.
- Bind every accepted certificate to its exact claim and source revision.

**Required outputs:** Certificate specification; producer provenance; checker source/version; positive and negative test results; checker TCB; claim-to-certificate binding.

**Acceptance conditions:** The checker validates the declared certificate semantics; invalid certificates are rejected in the required test suite; and the checker trust boundary and producer/checker independence are disclosed.

**Failure conditions:** Ambiguous format; untested malformed inputs; checker accepts invalid certificates; or certificate is not bound to the target claim.

### L-09 — Numerical Analysis and Adversarial Testing

**Purpose:** Challenge conjectures, algorithms, and analytic estimates through edge-case search and quantitative numerical analysis without confusing such evidence with proof.

**Threats addressed:** Numerical instability; conditioning and precision errors; unsearched counterexamples; false patterns; implementation defects; hidden edge cases.

**Required inputs:** Mathematical scope and parameter ranges; numerical model; algorithms; test strategy; expected error and stability requirements.

**Required responsibilities:**
- Use boundary, property-based, randomized, fuzz, and adversarial tests where appropriate.
- Record precision, rounding mode, conditioning, stability, convergence, and error estimates.
- Preserve random seeds, inputs, environments, and minimal reproducible counterexamples.
- Test near singularities, degeneracies, phase boundaries, and parameter extremes where relevant.
- Separate empirical observations from proved statements.
- Investigate every mismatch between theory, exact computation, independent implementation, and numerical results.

**Required outputs:** Test protocol; datasets and seeds; numerical error/stability analysis; logs; counterexamples; limitations; discrepancy reports.

**Acceptance conditions:** Tests are reproducible; numerical uncertainty is quantified to the extent required by the claim; edge-case coverage is justified; and no numerical result is mislabeled as a proof.

**Failure conditions:** Unreported precision limitations; irreproducible failures; known counterexample ignored; or numerical agreement used as the sole basis for a universal theorem.

### L-10 — Manuscript-to-Artifact Traceability and Synchronization

**Purpose:** Maintain a verifiable chain between manuscript statements and the exact specifications, formal proofs, programs, certificates, generated data, and reports that support them; detect drift after any revision.

**Threats addressed:** Stale proofs; manuscript/code version mismatch; broken references; copied constants or equations drifting apart; incorrect generated artifacts; a claim appearing verified after its source has changed.

**Required inputs:** Manuscript source and revision; claim registry; formal and computational artifact manifests; generated artifact metadata; commit identifiers and report references.

**Required responsibilities:**
- Maintain bidirectional traceability: each manuscript claim links to its specification and evidence, and each evidence artifact links back to the claim it supports.
- Record exact file paths, declaration names, line or section references where stable, commit hashes, and artifact versions.
- Synchronize equation/claim registries, generated constants, notation tables, references, and other derived artifacts where applicable.
- Use structured parsing or AST-aware checks where appropriate; plain-text search alone must not be treated as sufficient for semantic synchronization.
- Detect deleted, renamed, duplicated, stale, or orphaned artifacts and broken references.
- Revalidate affected claims when manuscript text, definitions, assumptions, proof code, dependencies, or generated files change.
- Preserve a change-impact report showing which claims and verification layers require reruns.
- Verify generated artifacts against their source and generator; generation itself is not validation.

**Required outputs:** Traceability graph or registry; artifact manifest; synchronization report; stale/orphan/broken-link report; change-impact report; regeneration and validation evidence.

**Acceptance conditions:** Every verified claim has a complete trace to the exact source and evidence revisions; no material drift is unresolved; generated artifacts are reproducible and checked; and changes trigger the required re-audits.

**Failure conditions:** Orphan proof or manuscript claim; stale evidence; mismatched revisions; unvalidated generated constants/equations; broken links; or status carried forward after a material change without impact review.

### L-11 — Trust, Axiom, Dependency, and Supply-Chain Audit

**Purpose:** Identify, bound, and assess every material trusted component, assumption, dependency, external service, and artifact-provenance path.

**Threats addressed:** Hidden axioms; unsound or compromised dependencies; unsafe escape hatches; toolchain defects; CI misconfiguration; dependency confusion or tampering; false independence; compromised build artifacts.

**Required inputs:** Claim-specific proof and computation artifacts; toolchain locks; dependency manifests; CI configuration; source provenance; external-service inventory.

**Required responsibilities:**
- Enumerate claim-specific trusted computing base components and trust boundaries.
- Audit axioms, admissions, unsafe features, external oracles, kernel extensions, and proof-checking assumptions.
- Pin tools, libraries, transitive dependencies, and immutable revisions.
- Record hashes, provenance, build environments, and relevant security advisories.
- Inspect CI workflows and artifact-generation paths.
- Analyze common-mode failures and supply-chain exposure.
- Reassess affected claims when a kernel, compiler, runtime, library, dependency, or workflow changes.

**Required outputs:** Claim-level TCB declaration; axiom/trust report; dependency and toolchain inventory; provenance records; CI configuration review; residual-risk register.

**Acceptance conditions:** Material trust assumptions and dependencies are disclosed and versioned; relevant audits pass; and residual risks are explicit.

**Failure conditions:** Undisclosed axiom/oracle; mutable or unknown critical dependency; unreviewed unsafe feature; unverifiable artifact provenance; or a material trust change without reassessment.

### L-12 — Reproducibility, Independent Review, and Evidence Governance

**Purpose:** Ensure that an appropriately independent reviewer can inspect and reproduce the stated evidence and that project reports never claim more than the evidence establishes.

**Threats addressed:** Irreproducibility; hidden local state; selective reporting; status inflation; incomplete review; lost failure evidence; misleading project-level completion metrics.

**Required inputs:** Immutable source and artifact revisions; environment locks; commands and configurations; logs; layer reports; claim registry; review requirements.

**Required responsibilities:**
- Provide clean reproduction instructions and environment manifests.
- Rebuild and rerun required checks from clean environments where feasible.
- Preserve logs, reports, failed attempts, inconclusive outcomes, and reviewer rationale.
- Require independent review proportionate to claim importance and risk.
- Separate implementation status, validation status, and claim-level verification status.
- Prevent green CI, source-file existence, or layer count from becoming a proxy for mathematical correctness.
- Maintain status history and change-control records.

**Required outputs:** Reproduction protocol; run manifests; immutable evidence references; independent review records; claim-level status decisions; residual-risk and exception reports.

**Acceptance conditions:** Required evidence is reproducible or its limitations are stated; review is documented; statuses follow the repository protocol; and all material failures and uncertainties remain visible.

**Failure conditions:** Missing critical provenance; unreproducible result without explanation; suppressed failure; unsupported status upgrade; or review presented as independent without evidence of independence.

## 5. Preservation and migration from the previous ten-function catalog

The earlier catalog contained ten conceptual functions. Their substance is preserved through the following mapping:

| Previous function | New location | Treatment |
|---|---|---|
| Mathematical Claim Specification | L-01 | Merged with literature/prior-art positioning; exact claim specification remains mandatory |
| Semantic Correspondence and Formalization Audit | L-02 | Retained as a dedicated layer |
| Primary Kernel-Checked Formal Verification (Lean 4) | L-04 | Retained; identifier changes from L-03 to L-04 |
| Independent Formal-Proof Route | L-05 | Retained |
| Exact Computational Verification | L-06 | Retained |
| Independent Implementation Cross-Checks | L-07 | Retained |
| Proof-Certificate Production and Independent Checking | L-08 | Retained |
| Numerical Analysis and Adversarial Testing | L-09 | Retained |
| Trust, Axiom, Dependency, and Supply-Chain Audit | L-11 | Retained |
| Reproducibility, Independent Review, and Evidence Governance | L-12 | Retained |
| New: Literature and Prior-Art Positioning | L-01 | Added and integrated with claim specification |
| New: Boundary, Domain, and Scope-Quantifier Audit | L-03 | Added as a dedicated layer |
| New: Manuscript-to-Artifact Traceability and Synchronization | L-10 | Added as a dedicated layer |

**Identifier migration warning:** Previous references to L-03 as Lean 4 refer to the old catalog. Under this standard Lean 4 is L-04. Historical records and commits must not be rewritten as though they originally used the new identifiers. New records should use the current IDs and, when referring to historical material, state the old ID and catalog version.

## 6. Cross-layer obligations

The following controls apply across all relevant layers; they are not additional numbered layers:

- Stable claim identity and exact source version.
- Explicit mathematical assumptions, domains, quantifiers, and side conditions.
- Semantic correspondence between representations.
- Claim-specific trust-boundary declaration.
- Independence analysis wherever independence is claimed.
- Provenance and version pinning for evidence and dependencies.
- Failure preservation and discrepancy investigation.
- Change-impact analysis after material revisions.
- Honest status reporting and visible residual risk.

A layer report must include at least:

1. Claim IDs and source revision covered.
2. Threats and obligations addressed.
3. Applicability decision and rationale.
4. Inputs and exact versions.
5. Methods and assumptions.
6. Outputs and immutable evidence references.
7. Dependencies and TCB.
8. Independence assessment, where applicable.
9. Acceptance criteria and results.
10. Failures, open obligations, limitations, and residual risks.
11. Reviewer and review date, where review is required.
12. Revalidation triggers.

## 7. Layer applicability and dependency rules

Not every claim must pass through every layer. The claim-specific Verification Obligation Matrix determines which layers are required.

For each layer and claim, record one of:
- **Required:** A material obligation or threat makes the layer necessary.
- **Conditional:** The layer is required if a specified mathematical or technical condition applies.
- **Not applicable:** A written justification demonstrates why the layer adds no relevant assurance for this claim.
- **Not assessed:** Applicability has not yet been determined.

“Not applicable” must never be used as a synonym for “not implemented,” “too expensive,” “not yet attempted,” or “failed.” If a required layer is not implemented, the claim remains open or not verified as dictated by the claim-level status protocol.

The dependency structure is not a simple linear pipeline. L-01, L-02, and L-03 establish and challenge the meaning and scope of the claim; L-04 through L-09 provide different evidence routes; L-10 binds all artifacts and detects drift; L-11 audits trust and dependencies across routes; L-12 governs reproducibility, review, and status. L-10 through L-12 are not merely final paperwork and may identify defects that require earlier layers to be rerun.

## 8. Status protocol

Layer status and claim status must be kept separate.

**Layer design/implementation status:**
- **Specified:** Requirements are documented.
- **Implemented:** A concrete control or tool exists.
- **Validated:** The implementation has passed its defined validation.
- **Partially Implemented:** Some controls exist but material requirements remain open.
- **Not Implemented:** No operational control is established.
- **Inconclusive:** Available evidence cannot determine the result.
- **Failed:** A required validation failed.

**Claim-level verification status** remains governed by the Architecture Charter:
- **Verified**
- **Partially Verified**
- **Inconclusive**
- **Failed**
- **Not Verified**

A layer being Specified does not mean Implemented. Implemented does not mean Validated. A Validated layer does not automatically make a claim Verified. Claim verification requires all applicable obligations, correspondence, and evidence to pass with assumptions and residual risks disclosed.

## 9. Change control and review triggers

A layer or this standard must be reviewed when:
- A new threat, counterexample, or common-mode failure is discovered.
- A claim's statement, domain, quantifiers, assumptions, or manuscript source changes.
- A formal prover, kernel, compiler, library, runtime, CAS, checker, or external oracle changes.
- A new verification route or layer is proposed.
- A dependency, CI workflow, artifact generator, or evidence format changes.
- A reviewer finds a correspondence, reproducibility, independence, or trust-boundary defect.

Every material change must record rationale, affected layers and claims, migration impact, validation requirements, and approval history. No status is retroactively upgraded merely because the standard changes; affected evidence must be reassessed.

## 10. Initial implementation boundary

This standard establishes the approved 12-layer architecture and its requirements. It does **not** claim that:
- all twelve layers have been implemented;
- all layers are validated or independently reviewed;
- every Paper A claim has passed all applicable layers;
- Lean 4 is the only verification route or a complete substitute for the other layers;
- the architecture eliminates every possible blind spot.

The current active Lean 4 work belongs to **L-04** under this standard. Other layers must be assessed against their actual artifacts and validation evidence. The project must not infer completion from the existence of this document.

## 11. Governing statement

> **Twelve layers organize the current verification obligations; they do not limit scrutiny, guarantee correctness, or replace evidence.**

The system is successful only to the extent that it detects errors, exposes uncertainty, preserves provenance, and supports independent examination of the exact mathematical claims.
