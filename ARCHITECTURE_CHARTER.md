# Constant Llapoy — Architecture Charter

**Document status:** Initial charter  
**Version:** 0.1.0  
**Scope:** Independent proof and verification infrastructure for the Absolute Symmetry research program  
**Normative language:** MUST and MUST NOT are mandatory requirements; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Mission

Constant Llapoy exists to establish, inspect, challenge, and preserve trustworthy evidence for mathematical claims made by the Absolute Symmetry research program.

Its purpose is not to make proofs pass, maximize a verification score, or validate research by accumulating tools. Its purpose is to determine—within explicitly stated assumptions, formal semantics, and trust boundaries—what has actually been established, what remains uncertain, and what has failed.

The system MUST prioritize:

1. Mathematical honesty over convenience.
2. Correctness over speed, cost, or implementation simplicity.
3. Explicit assumptions over hidden or implicit assumptions.
4. Independent scrutiny over duplicated agreement.
5. Reproducibility and auditability over opaque success reports.
6. Accurate limitation statements over exaggerated assurance.

No fixed number of verification layers is prescribed. Layers MUST be introduced, divided, combined, replaced, or removed according to an explicit threat model and documented verification obligations. A target such as 19 layers is neither a requirement nor a measure of quality.

## 2. Foundational principles

### 2.1 No weakening to obtain a pass

A mathematical claim, its domain, hypotheses, quantifiers, or conclusion MUST NOT be silently weakened, narrowed, or altered merely to make a tool accept it.

If the original claim cannot be formalized or verified, the system MUST report the limitation. Any mathematically justified revision MUST be documented, reviewed, and reflected in the research manuscript.

### 2.2 No concealed assumptions

Every assumption required by a formal proof, computation, algorithm, or certificate checker MUST be stated and traceable to the mathematical specification.

Assumptions introduced by libraries, typeclass instances, numerical representations, simplification procedures, or external solvers MUST be surfaced where they affect the result.

### 2.3 No evidence laundering

Evidence from one method MUST NOT be relabeled as evidence of a stronger kind.

In particular:

- Numerical agreement is not a proof.
- Passing tests is not a proof.
- Symbolic computation is not automatically a proof.
- A successful build is not evidence that a theorem is true.
- A proof assistant accepting a formal theorem does not by itself establish that the formal theorem faithfully represents the manuscript's claim.
- Agreement between two implementations does not establish independence if they share algorithms, libraries, specifications, generated code, or assumptions.

### 2.4 Failure is informative

A failed proof, counterexample, mismatch, timeout, unavailable dependency, or inconclusive check MUST be recorded honestly.

The system MUST NOT convert a failure or an inconclusive result into success by suppressing the check, weakening the claim, hiding the output, or changing the status label.

### 2.5 No single-tool authority

No single programming language, theorem prover, computer algebra system, compiler, test framework, or CI provider is to be treated as an unquestionable authority for every class of claim.

The trust placed in each component MUST be scoped and documented. Independence MUST be assessed technically, not inferred from different language names or different repositories.

## 3. Mathematical claim as the unit of verification

Verification MUST be organized around identifiable mathematical claims, not around file counts, module counts, test counts, or CI badges.

Each claim MUST have a stable identifier and a record containing, as applicable:

- Exact manuscript reference and version.
- Exact mathematical statement.
- Definitions and notation on which it depends.
- Domain, quantifiers, and hypotheses.
- Supporting lemmas and dependency graph.
- Formalized statement and source location.
- Computational checks and their methods.
- Certificates produced and checker results.
- Known limitations, unresolved obligations, and counterexamples.
- Verification status and review history.

A claim MUST NOT be marked fully verified if a material part of its statement, hypotheses, or proof correspondence remains unresolved.

## 4. Evidence classes

Constant Llapoy MUST distinguish at least the following evidence classes. These classes are complementary and MUST NOT be conflated.

1. **Formal proof:** A derivation accepted by a specified proof kernel under declared axioms, definitions, imports, and trust assumptions.
2. **Exact computation:** A computation over exact representations, such as rational or algebraic values, with the algorithm and its correctness basis documented.
3. **Independent implementation:** A separately developed implementation used to cross-check a result. Its actual shared dependencies and shared assumptions MUST be disclosed.
4. **Proof-certificate checking:** Verification of a result through a certificate checked by a smaller or independently implemented checker.
5. **Numerical evidence:** Floating-point or approximate calculations, with precision, conditioning, stability, and error bounds addressed where relevant.
6. **Testing and adversarial search:** Boundary tests, property-based tests, randomized tests, fuzzing, and counterexample search.
7. **Correspondence evidence:** A documented argument that the formal and computational statements match the intended manuscript claim.
8. **Reproducibility evidence:** Evidence that independent reviewers can retrieve the specified source, dependencies, toolchain, and instructions and reproduce the stated checks.

Each report MUST identify which class of evidence supports each conclusion.

## 5. Formal proof requirements

For every theorem declared formally verified, the project MUST record:

- The exact formal proposition.
- The proof source and toolchain version.
- The proof assistant and kernel identity/version.
- Imported libraries and relevant dependency versions.
- Axiom and trust-boundary audit.
- Any admitted, deferred, or external proof obligations.
- Build and checking instructions.
- The relationship between the formal proposition and the manuscript statement.

The project MUST NOT claim a theorem is fully formalized while material proof gaps remain. In Lean, for example, uses of sorry, unreviewed axioms, unsafe escape hatches, or external oracles MUST be identified and assessed. The same principle applies to other proof systems.

A clean build is necessary for reproducibility but is not, by itself, sufficient for mathematical verification.

## 6. Independent verification requirements

Multiple implementations or proof systems MUST only be described as independent to the extent that their independence has been examined.

For each important verification path, an independence record SHOULD assess:

- Shared mathematical specification and possible specification errors.
- Shared algorithms or derivation strategies.
- Shared libraries and transitive dependencies.
- Shared code generation or generated artifacts.
- Shared compilers, runtimes, kernels, and checkers.
- Shared external oracles and data sources.
- Shared human-authored assumptions and transformations.

Different languages do not automatically imply independent algorithms. Python and Rust implementations MUST be meaningfully distinct where independence is claimed. Wrapping one implementation in another language does not count as an independent implementation.

Where feasible, high-value results SHOULD be checked by methods with different failure modes—for example, a formal proof, an exact computational derivation, and a separately implemented certificate checker.

## 7. Computation, certificates, and numerical analysis

Computational tools MAY discover patterns, derive candidate identities, generate certificates, search for counterexamples, and cross-check formal results.

However, every computational result used as evidence MUST identify:

- Input data and mathematical representation.
- Algorithm and implementation version.
- Exact or approximate arithmetic model.
- Precision and error analysis, where applicable.
- Relevant assumptions and exceptional cases.
- Independent checking method, where available.

A certificate is only as trustworthy as its format, producer assumptions, and checker. Certificate checkers SHOULD be small, auditable, deterministic where practical, and isolated from unnecessary dependencies. The checker itself remains part of the documented trust boundary.

Floating-point results MUST NOT be presented as exact results. Numerical agreement MUST NOT substitute for a proof of a universal statement.

## 8. Correspondence between proof and manuscript

This is a mandatory verification obligation.

For every theorem claimed as verified, reviewers MUST be able to trace:

**Manuscript claim → mathematical specification → formal statement → proof dependencies → checked proof artifact → verification report.**

The correspondence audit MUST check that:

- Definitions have the same meaning.
- Domains and quantifiers match.
- All hypotheses are present and equivalent.
- The conclusion is not weaker than the manuscript claim.
- Side conditions and exceptional cases are preserved.
- Notation changes do not conceal semantic changes.
- The formal proof does not establish a different or easier proposition.

A successful formal proof of a proposition that does not faithfully encode the manuscript theorem MUST NOT be counted as verification of that manuscript theorem.

## 9. Threat model and layer design

The architecture MUST be derived from a maintained threat model. At minimum, the threat model MUST consider:

- Incorrect mathematical reasoning.
- Incorrect, incomplete, or ambiguous specifications.
- Formalization and translation errors.
- Unsound or misconfigured proof dependencies.
- Kernel, compiler, runtime, and toolchain defects.
- Computer algebra and algorithm implementation bugs.
- Numerical instability and representation errors.
- Incorrect certificate formats or checkers.
- Common-mode failures and false independence.
- Dependency compromise and supply-chain attacks.
- Build and CI configuration errors.
- Incomplete test coverage and unsearched edge cases.
- Manuscript-to-proof correspondence errors.
- Missing provenance or irreproducible results.
- Human review errors and misleading status reporting.

Each verification layer MUST address one or more identified threats or obligations. Its purpose, inputs, outputs, assumptions, dependencies, trust boundary, failure modes, and validation method MUST be documented.

The architecture MUST NOT add layers merely to increase their count. It MUST NOT cap the number of layers for convenience. The design is complete only to the extent that identified risks and verification obligations are addressed with justified, auditable controls; residual risks MUST remain visible.

## 10. Dependency and supply-chain integrity

The repository MUST maintain explicit, versioned dependency and toolchain records.

For material dependencies and tools, the project SHOULD record:

- Exact versions and immutable source identifiers where available.
- Lockfiles and integrity hashes.
- Transitive dependency information.
- License and security advisories.
- Build provenance and CI environment.
- Whether the dependency is inside the trusted computing base.
- The mathematical or operational role it plays.

Dependency scanning and reproducible builds reduce risk but do not prove that dependencies are correct or free of vulnerabilities. The project MUST state what was checked and what was not checked.

Changes to proof assistants, kernels, libraries, compilers, runtimes, algorithms, or lockfiles MUST trigger the relevant regression and audit procedures before previously established statuses are carried forward.

## 11. Verification status protocol

The repository MUST use explicit, claim-level statuses:

- **Verified:** All defined verification obligations for the claim have passed, correspondence has been audited, and residual assumptions and trust boundaries are disclosed.
- **Partially Verified:** Some obligations have passed, but one or more material obligations remain open.
- **Inconclusive:** Available evidence does not determine whether the claim holds.
- **Failed:** A required check failed or a contradiction/counterexample was found.
- **Not Verified:** The required verification has not been performed.

A status MUST be accompanied by a report and evidence references. A green CI result MUST NOT automatically set a mathematical claim to Verified.

Project-level completion MUST be computed from the claim registry and required obligations, not inferred from the existence of source files or successful builds.

## 12. Auditability and reproducibility

Every verification result MUST be traceable to immutable or versioned artifacts, including source revisions, toolchain versions, dependency locks, configuration, and reports.

The repository SHOULD provide clean, documented commands for reviewers to reproduce checks. CI MUST expose failures rather than suppress them. Logs and reports SHOULD preserve enough information to diagnose the result without relying on private agent state or undocumented local setup.

Where exact reproducibility is not technically achievable, the limitation and the expected variance MUST be documented.

## 13. Change control

Changes to this charter, the threat model, verification requirements, or status criteria MUST be documented with rationale and review history.

A change MUST NOT retroactively convert an unverified result into a verified result without rerunning the affected checks and auditing the change's impact.

Any relaxation of a requirement MUST be explicit, justified, scoped, and visible to reviewers. Requirements MUST NOT be silently relaxed to obtain a passing result.

## 14. Initial implementation boundary

This charter establishes governance and design principles; it does not claim that any layer has already been implemented, that any paper has passed verification, or that the repository currently provides the controls described here.

The initial implementation MUST begin with:

1. A claim registry and mathematical specification format.
2. A threat model and trust-boundary inventory.
3. A toolchain and dependency inventory.
4. A verification-obligation matrix.
5. A proof-to-manuscript correspondence process.
6. A transparent status and reporting protocol.

The detailed layer architecture MUST be designed from those artifacts rather than assumed in advance.

## 15. Governing statement

> **We do not optimize for passing proofs. We optimize for discovering whether proofs are actually correct.**

Constant Llapoy exists to expose uncertainty, detect error, preserve evidence, and make mathematical verification independently inspectable. No deadline, cost, complexity, target layer count, publication goal, or success metric takes precedence over mathematical honesty.
