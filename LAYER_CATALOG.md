# Constant Llapoy — Verification Layer Catalog

**Document status:** Preliminary architecture catalog; not an implementation claim  
**Version:** 0.1.0  
**Scope:** Conceptual inventory of verification functions and assurance controls for Constant Llapoy  
**Parent documents:** `ARCHITECTURE_CHARTER.md`, `THREAT_MODEL.md`, `TRUST_BOUNDARY_TCB_INVENTORY.md`, `VERIFICATION_OBLIGATION_MATRIX.md`  
**Normative language:** MUST and MUST NOT are mandatory requirements; SHOULD is a strong recommendation.

---

## 1. Purpose and status

This catalog records the verification functions currently contemplated for Constant Llapoy. It gives the project a common architecture map before additional verification systems are implemented.

This is a **preliminary catalog**, not a declaration that every listed layer has been fully designed, implemented, independently validated, or applied to every paper. The catalog is intentionally revisable as the threat model, claim obligations, and trust-boundary analysis mature.

The architecture has no predetermined layer count. Layer identifiers are stable references for discussion and traceability, not a commitment to a fixed number or a mandatory linear pipeline. Layers MAY be split, combined, replaced, reordered, or retired when justified by documented threat and obligation analysis.

A layer MUST exist because it addresses a real verification obligation or threat. It MUST NOT exist merely to increase the layer count or create an appearance of assurance.

## 2. Architecture principles

1. **Claim-driven:** The mathematical claim and its exact hypotheses, domains, quantifiers, and conclusion determine which checks are required.
2. **Evidence-class aware:** Formal proof, exact computation, independent implementation, certificate checking, numerical evidence, testing, correspondence, and reproducibility are distinct evidence classes.
3. **Producer-checker separation:** A tool that generates a result is not automatically qualified to validate its own result.
4. **Independence must be demonstrated:** Different languages, tools, repositories, or vendors do not by themselves establish independent verification.
5. **Cross-cutting controls remain visible:** Correspondence, trust-boundary, dependency, provenance, and reporting controls apply across evidence-producing layers; they are not optional decorations.
6. **Fail closed:** Missing, stale, ambiguous, or failed evidence MUST NOT be converted into a pass.
7. **No evidence laundering:** Numerical agreement, tests, successful builds, and green CI MUST NOT be described as formal proof.
8. **No implementation overclaim:** A catalog entry describes an intended function until its implementation and validation evidence are recorded.

## 3. Conceptual layer inventory

The following entries are the current architecture baseline. Their order is for reference and does not imply that every claim must traverse them in a single sequence.

### L-01 — Mathematical Claim Specification

**Purpose:** Establish the exact mathematical object being checked.

**Responsibilities:**
- Freeze the claim statement and manuscript revision.
- Record definitions, notation, domains, quantifiers, hypotheses, side conditions, and conclusion.
- Identify dependencies on prior definitions, lemmas, and external results.
- Preserve source provenance and stable claim identifiers.

**Required outputs:** Claim record, machine-readable or otherwise unambiguous mathematical specification, source reference, dependency links, and unresolved-ambiguity record.

**Primary threats addressed:** Incorrect or ambiguous statements, omitted assumptions, wrong domains, claim drift, and specification errors.

**Status:** Foundational artifacts exist (including the Claim Registry and manuscript extraction records); completeness is claim-specific and must not be presumed.

### L-02 — Semantic Correspondence and Formalization Audit

**Purpose:** Check that every translated or formalized statement means what the intended manuscript claim says.

**Responsibilities:**
- Compare manuscript claim → mathematical specification → formal proposition.
- Check definitions, domains, quantifiers, hypotheses, exceptional cases, and conclusion.
- Detect silent weakening, strengthening, narrowing, or semantic drift.
- Review proof dependencies for hidden assumptions and mismatched objects.

**Required outputs:** Claim-to-formalization correspondence record, reviewer rationale, discrepancy list, and approval or unresolved status.

**Primary threats addressed:** Formalization errors, translation errors, and proof of the wrong theorem.

**Status:** Governance requirements are defined in the Architecture Charter; claim-by-claim correspondence remains an outstanding obligation unless an explicit audit record says otherwise.

### L-03 — Primary Kernel-Checked Formal Verification

**Purpose:** Prove formal propositions in a proof assistant and have the designated kernel check the resulting proof terms.

**Current primary route:** Lean 4 with pinned toolchain and Mathlib dependency revisions.

**Responsibilities:**
- Formalize definitions and theorem statements.
- Construct proofs accepted by the Lean kernel.
- Record declaration names, imports, toolchain, dependency revisions, and build commands.
- Audit transitive axioms, admissions, unsafe features, and other trust extensions.

**Required outputs:** Source revision, theorem declaration, reproducible build result, axiom/trust audit, and dependency snapshot.

**Primary threats addressed:** Invalid deductive steps within the formal system and untracked formal assumptions, subject to the declared kernel and TCB.

**Status:** **Implemented and actively developed for selected Paper A obligations.** This does not mean Paper A or the repository's claims are fully verified. A successful build alone does not establish manuscript correspondence or mathematical completeness.

### L-04 — Independent Formal-Proof Route

**Purpose:** Recheck selected high-value claims through a genuinely distinct proof system or independently trusted proof-checking route.

**Candidate approaches:** Rocq/Coq, Isabelle/HOL, or another system selected after a claim-specific independence and feasibility analysis.

**Responsibilities:**
- Independently encode the relevant mathematical statement.
- Avoid merely translating generated Lean code or reusing the same proof-producing implementation.
- Document shared specifications, algorithms, libraries, kernels, compilers, and human assumptions.
- Compare the actual proposition and assumptions, not only theorem names or final outputs.

**Required outputs:** Independent formal artifact, toolchain and dependency record, correspondence audit, and common-mode failure analysis.

**Primary threats addressed:** Correlated defects or mistaken assumptions specific to a single formalization route.

**Status:** Conceptual; no independent prover is designated as an implemented project-wide route.

### L-05 — Exact Computational Verification

**Purpose:** Derive or check finite and algebraic consequences using exact representations and algorithms.

**Possible methods:** Integer and rational arithmetic, exact linear algebra, algebraic-number computation, symbolic identities with independently checkable derivations, and finite exhaustive computation where mathematically appropriate.

**Responsibilities:**
- Specify exact input encodings and arithmetic semantics.
- Distinguish exact algorithms from heuristic or approximate procedures.
- Record algorithm correctness basis and exceptional cases.
- Provide independently checkable outputs where possible.

**Required outputs:** Exact input data, algorithm/version, result, correctness basis, and independent check or explicit limitation.

**Primary threats addressed:** Hand-calculation errors and implementation errors in finite or exact computational subproblems.

**Status:** Conceptual / claim-dependent. The existence of scripts or symbolic calculations does not establish a general exact-verification layer.

### L-06 — Independent Implementation Cross-Checks

**Purpose:** Detect implementation defects through separately developed implementations with analyzed independence.

**Possible implementation technologies:** Python, Rust, or other suitable languages. These are implementation choices, not separate layers merely because the languages differ.

**Responsibilities:**
- Use independently authored implementations where independence is claimed.
- Prefer meaningfully different algorithms for critical cross-checks.
- Compare exact outputs where possible.
- Record shared libraries, algorithms, specifications, generated code, compilers, runtimes, and test oracles.

**Required outputs:** Source revisions, environment locks, test vectors, comparison reports, and independence assessment.

**Primary threats addressed:** Defects in a single implementation and some classes of common implementation errors.

**Status:** Conceptual / not established as an independent route until specific implementations and independence evidence are reviewed.

### L-07 — Proof-Certificate Production and Independent Checking

**Purpose:** Separate potentially complex evidence generation from a smaller, auditable checker.

**Responsibilities:**
- Define canonical certificate formats and semantics.
- Treat certificate producers as untrusted evidence producers unless separately justified.
- Build or select small checkers with explicit assumptions.
- Test valid, invalid, malformed, incomplete, and boundary certificates.
- Document checker TCB and producer-checker common dependencies.

**Required outputs:** Certificate specification, producer provenance, checker source and version, positive/negative test results, and checker trust declaration.

**Primary threats addressed:** Incorrect outputs from complex producers and defects that can be caught by a distinct checker.

**Status:** Conceptual; certificate formats and checkers remain claim- and domain-dependent.

### L-08 — Numerical Analysis and Adversarial Testing

**Purpose:** Find counterexamples, expose edge cases, assess numerical behavior, and challenge conjectures or implementations.

**Responsibilities:**
- Use boundary, property-based, randomized, fuzz, and adversarial tests where appropriate.
- Record precision, rounding, conditioning, stability, convergence, and error bounds for numerical work.
- Preserve seeds, inputs, environments, and reproducible failure cases.
- Keep numerical evidence and testing explicitly separate from proof.

**Required outputs:** Test protocol, datasets/seeds, numerical error analysis, logs, counterexamples, and limitations.

**Primary threats addressed:** Unsearched edge cases, numerical instability, implementation defects, and false conjectures.

**Status:** Existing project-specific computations and scripts may support individual claims; coverage and rigor must be audited claim by claim. This entry does not assert comprehensive implementation.

### L-09 — Trust, Axiom, Dependency, and Supply-Chain Audit

**Purpose:** Make every material trust assumption and dependency visible and assess whether the verification route relies on acceptable components.

**Responsibilities:**
- Enumerate claim-specific TCB components and trust boundaries.
- Audit formal axioms, admissions, unsafe features, and external oracles.
- Pin toolchains, packages, transitive dependencies, and immutable revisions.
- Inspect CI configuration, build provenance, artifact integrity, and dependency changes.
- Analyze common-mode failures and false independence.

**Required outputs:** Claim-level TCB declaration, axiom report, dependency inventory, provenance records, and residual-risk register.

**Primary threats addressed:** Hidden assumptions, unsound dependencies, compromised supply chains, CI misconfiguration, and correlated failures.

**Status:** Foundational inventories and Lean/CI audit mechanisms exist; complete claim-specific and system-wide coverage is not established.

### L-10 — Reproducibility, Independent Review, and Evidence Governance

**Purpose:** Ensure that verification evidence can be reproduced, inspected, challenged, and reported without overstating its meaning.

**Responsibilities:**
- Bind every result to immutable source, toolchain, configuration, dependencies, and logs.
- Rebuild from clean environments where feasible.
- Obtain independent review proportionate to claim importance.
- Preserve failures, inconclusive results, reviewer rationale, and residual risks.
- Apply claim-level status rules and prevent CI success from automatically becoming mathematical verification.

**Required outputs:** Reproduction instructions, run manifests, immutable evidence references, review records, and claim-level status decisions.

**Primary threats addressed:** Irreproducibility, misleading status aggregation, hidden failures, provenance gaps, and human review errors.

**Status:** Governance and CI infrastructure exist in part; end-to-end evidence governance and independent review are not complete for all claims.

## 4. Cross-layer obligations

The following are not optional extra layers. They are obligations that attach to every applicable layer and claim:

| Obligation | Applies to | Minimum requirement |
|---|---|---|
| Claim identity and versioning | All | Stable claim ID and exact statement revision |
| Manuscript correspondence | All evidence routes | Traceable semantic comparison |
| Assumption disclosure | All | Explicit mathematical and environmental assumptions |
| TCB declaration | All relied-upon routes | Claim-specific trusted components and residual risk |
| Independence analysis | Any claimed independent route | Shared-failure analysis, not language-name diversity |
| Provenance and reproducibility | All accepted evidence | Immutable source, dependency, toolchain, and run references |
| Failure preservation | All | Failed and inconclusive checks remain visible |
| Status discipline | All | Status cannot exceed the evidence obtained |

## 5. Layer applicability is claim-specific

Not every theorem requires every layer.

For each claim, the Verification Obligation Matrix MUST determine:
- which layers are applicable;
- why each applicable layer is required;
- which layers are not applicable and why;
- which evidence artifacts are required;
- the dependencies and independence constraints;
- the acceptance criteria;
- the remaining risks and unresolved obligations.

An omitted layer is not automatically a defect if it is explicitly justified as not applicable. Conversely, a layer listed in this catalog does not count as completed evidence merely because it exists in the document.

## 6. Current implementation snapshot

This section is a status snapshot, not a completion score.

| Area | Current assessment |
|---|---|
| Claim registry and extraction records | Implemented as repository artifacts; claim review remains claim-specific |
| Threat model and architecture governance | Initial documents exist |
| Lean 4 formal verification | Active implementation and CI testing for selected Paper A obligations |
| Lean axiom / trust audit | CI mechanism exists; each theorem still requires interpretation and correspondence |
| Independent formal prover | Not established |
| Exact computational verification framework | Not established as a general layer |
| Independent Python/Rust implementations | Not established as independent verification routes |
| Certificate checker framework | Not established |
| Numerical/adversarial verification | Partial, claim-specific evidence only |
| Claim-specific TCB and independence coverage | Incomplete |
| End-to-end reproducibility and independent review | Incomplete |

No project-wide percentage or “number of completed layers” should be inferred from this table. Implementation, validation, and claim-level applicability are separate dimensions.

## 7. Design and implementation sequence

The following is a provisional order of work, subject to the obligation matrix and threat model:

1. Maintain exact claim specifications and claim identifiers.
2. Complete and trial the correspondence and claim-level TCB templates on real Paper A claims.
3. Continue the Lean 4 route as the first active formalization path, without treating it as the sole authority.
4. Select a small number of high-value claims for independent-route feasibility studies.
5. Define exact-computation and certificate-checking formats only where real claims justify them.
6. Establish implementation-independence criteria before treating Python/Rust cross-checks as independent.
7. Expand numerical and adversarial testing according to identified failure modes.
8. Integrate clean reproducibility, review, and status governance across all evidence routes.

This sequence is not permission to skip required obligations. The Verification Obligation Matrix controls what must be completed before a particular claim can be accepted.

## 8. Change control

Every material addition, split, merge, or retirement of a layer MUST record:
- the threat or verification obligation motivating the change;
- the intended scope and affected claims;
- inputs, outputs, assumptions, and dependencies;
- trust boundary and failure modes;
- independence rationale, if applicable;
- validation and acceptance criteria;
- migration impact on existing claim records;
- reviewer and decision rationale.

Layer count MUST NOT be used as a quality metric.

## 9. Governing statement

> **The architecture is defined by the verification obligations we must satisfy—not by a predetermined number of tools, languages, or layers.**

A layer is complete only when its design, implementation, validation, evidence outputs, trust assumptions, and claim-specific applicability have been demonstrated and recorded. A passing job or a catalog entry alone is never sufficient.
