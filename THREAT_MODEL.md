# Constant Llapoy — Threat Model

**Document status:** Initial threat model  
**Version:** 0.1.0  
**Parent document:** `ARCHITECTURE_CHARTER.md`  
**Scope:** Threats to the correctness, soundness, correspondence, integrity, and reproducibility of mathematical verification evidence  
**Normative language:** MUST and MUST NOT are mandatory requirements; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Purpose

This document identifies ways in which Constant Llapoy could produce, preserve, or communicate a false impression that a mathematical claim has been verified.

The central security property is not merely that software executes successfully. It is that every published verification conclusion is justified by evidence that:

1. addresses the exact mathematical claim under review;
2. has explicit assumptions and known trust boundaries;
3. has not silently omitted a material obligation;
4. can be independently inspected and, where feasible, reproduced; and
5. is reported at no stronger level than the evidence warrants.

The threat model is a living engineering and research document. It is not a claim that every listed control has already been implemented. Each control must later be mapped to an implementation, an owner, a test or audit procedure, and retained evidence.

## 2. Security objectives and protected assets

The following assets require protection.

| Asset | Required property | Example failure |
|---|---|---|
| Mathematical claim | Exact meaning preserved | A universal theorem is checked only for sampled inputs |
| Specification | Complete and faithful | A hypothesis is omitted or a domain is narrowed |
| Formal proof | Kernel-accepted derivation under disclosed assumptions | A theorem depends on an unreviewed axiom or admitted gap |
| Proof dependencies | Integrity and understood semantics | A library theorem or instance introduces an unexpected assumption |
| Computational result | Correct method and representation | A CAS simplification bug produces a false identity |
| Certificate | Valid, unambiguous, correctly checked | A malformed certificate is accepted by a buggy parser |
| Correspondence record | Manuscript and formal statement match | Lean proves a nearby but weaker proposition |
| Source and history | Integrity and provenance | A verification artifact is silently replaced |
| Toolchain and dependencies | Known versions and trust boundaries | A compromised package or compiler changes the result |
| Verification report | Honest, accurate status | A timeout or skipped test is shown as a pass |
| Reproduction procedure | Independently executable | Results depend on undocumented local state |
| Reviewer access | Sufficient transparency | Critical assumptions or logs are withheld |

### 2.1 Primary security properties

- **Soundness:** Accepted evidence does not rely on invalid inference within the declared formal system and trust boundary.
- **Faithfulness:** The checked proposition represents the intended manuscript claim.
- **Completeness of obligations:** Material hypotheses, cases, side conditions, and dependencies are not omitted.
- **Integrity:** Source, proof artifacts, certificates, reports, and provenance are not silently altered.
- **Independence:** Cross-checks do not share an undisclosed failure source while being presented as independent.
- **Reproducibility:** Reviewers can reconstruct the stated verification environment and procedure.
- **Transparency:** Failures, uncertainty, residual risks, and assumptions remain visible.
- **Availability of evidence:** Relevant artifacts and logs remain accessible for review.

Availability is important for auditability, but it must never be confused with correctness. A system that is temporarily unavailable has not disproved a theorem; equally, a system that is available and green has not automatically proved one.

## 3. Adversaries, error sources, and trust assumptions

The model considers both intentional attacks and non-malicious failures.

### 3.1 Sources of threat

1. **Research reasoning error:** An incorrect lemma, hidden assumption, invalid inference, or overlooked exceptional case.
2. **Specification author error:** A faithful-looking formal statement encodes a different or weaker claim.
3. **Formalization author error:** Definitions, coercions, typeclass instances, or translations alter intended semantics.
4. **Tool defect:** A bug in a prover, kernel, CAS, compiler, runtime, parser, or checker.
5. **Dependency defect or compromise:** A package is defective, malicious, unexpectedly changed, or no longer available.
6. **Automation defect:** CI, scripts, generated files, or orchestration report misleading results.
7. **Common-mode error:** Nominally separate checks share the same mistaken specification, algorithm, source, or dependency.
8. **Human review failure:** Reviewers overlook a mismatch, trust a badge, or misunderstand what a result establishes.
9. **Intentional manipulation:** Someone deliberately suppresses a failure, changes a theorem, alters evidence, or misrepresents status.
10. **Environmental failure:** Hardware faults, resource exhaustion, nondeterminism, or corrupted storage affect execution or evidence.

No assumption is made that all contributors are malicious. Controls must nevertheless make accidental and deliberate misrepresentation detectable where reasonably possible.

### 3.2 Trust-boundary rule

Every component that can affect a verification conclusion MUST be classified as one of:

- inside the trusted computing base (TCB) for a stated claim;
- checked by a smaller or independently justified component;
- cross-checked by an alternative method;
- assumed trustworthy for a clearly stated reason; or
- explicitly untrusted, with its output treated only as a candidate or heuristic.

The label “independent” MUST be supported by a dependency and method analysis. Different languages, teams, repositories, or vendors are not sufficient evidence on their own.

## 4. Threat analysis

Each threat below includes the failure mode, possible impact, required controls, and evidence to retain. These controls are requirements for the later design; their implementation status must be tracked separately.

### T01 — Incorrect mathematical reasoning

**Failure modes**
- An argument uses an invalid inference or circular reasoning.
- A lemma is true only under an unstated condition.
- A proof assumes a special case and generalizes without justification.
- A boundary, degenerate, singular, zero, or limiting case is overlooked.
- A theorem depends on a definition whose intended meaning was misunderstood.

**Impact:** The research claim itself may be false even if every subsequent software check faithfully verifies a derived statement.

**Required controls**
- Maintain a human-readable mathematical specification for each claim.
- Record definitions, hypotheses, domains, quantifiers, and exceptional cases explicitly.
- Maintain dependency graphs and identify circular dependencies.
- Require independent mathematical review for high-impact claims.
- Use counterexample search and adversarial review as discovery tools, never as universal proof.
- Preserve unresolved mathematical questions as open obligations.

**Evidence:** Reviewed specification, dependency graph, review record, counterexample-search scope and output, unresolved-obligation list.

### T02 — Incomplete, ambiguous, or incorrect specification

**Failure modes**
- A variable's domain is narrower than in the manuscript.
- A universal quantifier becomes an existential or bounded statement.
- A side condition is silently added or omitted.
- A definition is circular, ambiguous, or inconsistent across documents.
- A theorem is formalized using a convenient surrogate that is not equivalent.

**Impact:** A proof may be valid for the formal statement but irrelevant to the intended theorem.

**Required controls**
- Give every claim a stable identifier and versioned specification.
- Make domains, quantifiers, assumptions, and conclusions explicit.
- Require a specification review separate from proof-code review.
- Record every translation choice and nontrivial equivalence.
- Prohibit silent theorem weakening or narrowing.
- Maintain explicit links from each manuscript claim to its specification.

**Evidence:** Specification version, review checklist, translation notes, claim-to-manuscript mapping, change history.

### T03 — Formalization and encoding errors

**Failure modes**
- Coercions, implicit arguments, overloaded notation, or typeclass instances change semantics.
- A definition in Lean or another prover does not match the mathematical definition.
- A theorem is proved for an unintended structure or weaker type.
- A namespace collision or shadowed definition causes the wrong object to be used.
- Simplification or rewriting uses a lemma under inappropriate conditions.

**Impact:** The proof assistant establishes a proposition different from the intended mathematics.

**Required controls**
- Review definitions and theorem statements, not only proof terms.
- Expand or inspect critical definitions and inferred types.
- Record relevant instances, coercions, notation, and imported namespaces.
- Use explicit names and types for high-risk definitions.
- Check critical statements against the specification using independent review or a second formalization where justified.
- Add regression tests for known semantic edge cases.

**Evidence:** Formal source, elaborated theorem statement, relevant definition and instance inventory, review notes, regression results.

### T04 — Proof gaps, axioms, and hidden trust expansion

**Failure modes**
- An admitted theorem, placeholder, or incomplete proof remains in a dependency path.
- An axiom is introduced without adequate justification.
- An external oracle is trusted without disclosure.
- Unsafe features, custom axioms, or unverified extensions expand the TCB.
- A theorem appears closed while a material obligation is deferred elsewhere.

**Impact:** A theorem may be accepted only because an unverified assumption has been treated as fact.

**Required controls**
- Audit the transitive dependency path of every claim.
- Inventory axioms, admitted obligations, external oracles, unsafe escapes, and custom extensions.
- Distinguish foundational axioms of the formal system from project-introduced assumptions.
- Require explicit justification and approval for every project-introduced axiom.
- Block “Verified” status while material proof gaps or unreviewed trust expansions remain.
- Re-run the audit when dependencies or proof sources change.

**Evidence:** Axiom report, dependency closure, admitted/placeholder scan, oracle inventory, reviewed TCB statement.

### T05 — Proof assistant and kernel defects

**Failure modes**
- A kernel bug accepts an invalid proof.
- A bug in elaboration, reduction, serialization, or import handling changes the checked object.
- A version-specific defect affects a relevant inference.
- A custom kernel or extension is assumed sound without adequate review.

**Impact:** A formally accepted proof may not provide the expected assurance.

**Required controls**
- Pin and record proof assistant and kernel versions and source identities.
- Keep proof artifacts available for independent checking.
- Where feasible, use a small trusted kernel or independent checker path.
- Assess known defects and advisories relevant to the used version and features.
- Recheck critical claims after kernel or toolchain upgrades.
- Document precisely what the kernel checks and what remains outside its scope.

**Evidence:** Toolchain manifest, source hashes, build logs, kernel identity, defect/advisory review, independent checking results where available.

### T06 — Library and theorem dependency defects

**Failure modes**
- A dependency contains a false theorem, unsound axiom, or defect.
- A transitive dependency changes without an intentional project change.
- A theorem is used outside its intended assumptions.
- A package name or version resolves to unexpected content.
- A dependency's generated or compiled artifact differs from reviewed source.

**Impact:** Trust is inherited from an unexamined dependency or changed artifact.

**Required controls**
- Pin versions and immutable revisions where possible.
- Maintain lockfiles and dependency closure reports.
- Identify dependencies that contribute foundational results or critical algorithms.
- Audit axioms and trust assumptions in relevant theorem libraries.
- Review dependency diffs before upgrades.
- Keep critical dependency use minimal where feasible.
- Re-run affected proof and correspondence audits after changes.

**Evidence:** Lockfiles, package manifest, hashes, dependency graph, upgrade review, relevant axiom/dependency reports.

### T07 — Computer algebra system and exact algorithm defects

**Failure modes**
- A CAS transformation is incorrect for a corner case.
- A polynomial factorization, resultant, Gröbner basis, determinant, or simplification routine has a bug.
- An algorithm silently changes domains, assumptions, coefficient rings, or variable ordering.
- Exact-looking output is actually based on approximate arithmetic or heuristic assumptions.
- A result is copied into a proof without independently checking the derivation.

**Impact:** A false computational identity or classification may be treated as established mathematics.

**Required controls**
- State the exact input domain and representation.
- Record algorithm, software version, options, and assumptions.
- Distinguish exact rational/algebraic computation from floating-point or heuristic output.
- Where possible, emit a checkable certificate.
- Use a separate checker or mathematically distinct implementation for critical results.
- Independently verify small or structurally important cases.
- Treat CAS output as a candidate until its result is checked at the required evidence level.

**Evidence:** Input files, exact representation, scripts, logs, software versions, certificate, checker output, independent comparison.

### T08 — False independence and common-mode failure

**Failure modes**
- Python and Rust programs are ports of the same flawed algorithm.
- Two proof paths share the same incorrect specification.
- Independent-looking tools use the same library, backend, generated source, or external oracle.
- Multiple agents repeat the same mistaken assumption from a shared prompt.
- A second implementation merely calls the first implementation.

**Impact:** Agreement is mistaken for independent confirmation when all paths can fail in the same way.

**Required controls**
- Maintain an independence matrix for each important cross-check.
- Compare algorithms, specifications, libraries, code generation, compilers, and human assumptions.
- State exactly which failure modes are diversified and which remain shared.
- Use structurally different methods when practical, not merely different syntax.
- Include an independent reviewer who can challenge the specification itself.
- Never convert agreement alone into a formal proof claim.

**Evidence:** Independence matrix, implementation design notes, dependency graphs, review records, common-mode residual-risk statement.

### T09 — Numerical representation and floating-point failure

**Failure modes**
- Rounding, cancellation, overflow, underflow, or ill-conditioning changes results.
- Precision is insufficient to distinguish a true zero from a small nonzero value.
- A numerical optimizer or solver returns a local or approximate solution.
- Tolerances are selected after seeing results.
- A finite sample is presented as evidence for a universal claim.

**Impact:** Numerical artifacts are misinterpreted as exact identities, counterexamples, or proofs.

**Required controls**
- Label all approximate results as approximate.
- Record precision, rounding mode, tolerance, conditioning, and error bounds where relevant.
- Use interval arithmetic or rigorous error bounds for claims that depend on numerical enclosures.
- Separate exploratory numerical evidence from exact proof evidence.
- Test stability under increased precision and alternative formulations.
- Do not infer universal statements from finite samples.

**Evidence:** Numerical environment, precision settings, error analysis, conditioning notes, raw outputs, exact follow-up proof or explicit limitation.

### T10 — Certificate format and checker defects

**Failure modes**
- A certificate producer emits invalid or incomplete data.
- A parser accepts ambiguous, truncated, or malformed input.
- The checker has a bug or shares too much code with the producer.
- A certificate is detached from the exact input or theorem it certifies.
- The checker verifies a weaker property than the report claims.

**Impact:** A purportedly small trusted verification path may itself accept false evidence.

**Required controls**
- Specify certificate formats precisely and version them.
- Bind certificates cryptographically or immutably to their input, claim ID, and producer version.
- Keep checkers small and minimize dependencies.
- Test parsers against malformed, adversarial, and boundary inputs.
- Use independent checker implementations for high-value results where feasible.
- Review exactly what proposition the checker establishes.
- Fail closed on malformed, missing, or mismatched certificate data.

**Evidence:** Format specification, certificate hash, input binding, checker source/version, adversarial parser tests, checker logs.

### T11 — Compiler, runtime, and build-system defects

**Failure modes**
- A compiler miscompiles proof or checker code.
- A runtime or build tool changes semantics or omits required work.
- Cached artifacts are stale or do not correspond to current source.
- Build scripts skip failed stages or ignore exit codes.
- Different environments produce materially different artifacts.

**Impact:** The executed checker or proof build may not correspond to the reviewed source.

**Required controls**
- Pin compiler, runtime, build tool, and relevant environment versions.
- Preserve complete build commands and logs.
- Use clean builds and disable or validate untrusted caches for critical checks.
- Verify exit codes and fail the pipeline on missing stages.
- Where feasible, compare reproducible builds or use a second toolchain.
- Re-audit after compiler or build-system changes.

**Evidence:** Environment manifest, build scripts, clean-build logs, artifact hashes, cache policy, toolchain comparison.

### T12 — Hardware, operating system, and execution-environment faults

**Failure modes**
- Memory or storage corruption changes inputs or outputs.
- Hardware faults affect arithmetic or execution.
- Operating-system behavior, resource limits, or concurrency introduce nondeterminism.
- A virtualized or remote environment is compromised.
- Timeouts or resource exhaustion are misreported as successful completion.

**Impact:** Results may be corrupted, incomplete, or impossible to reproduce.

**Required controls**
- Preserve input and output hashes for critical runs.
- Record relevant OS, architecture, runtime, and execution environment.
- Treat crashes, timeouts, killed processes, and incomplete logs as inconclusive or failed—not passed.
- Use redundant execution or checksums for high-value artifacts where justified.
- Make resource limits and nondeterministic settings visible.
- Keep the environment's role in the TCB explicit.

**Evidence:** Environment metadata, run identifiers, exit status, resource and timeout records, artifact hashes, rerun comparisons.

### T13 — Dependency supply-chain compromise

**Failure modes**
- A package, action, binary, container, or upstream repository is compromised.
- A maintainer account or release channel is compromised.
- A dependency is replaced under a mutable tag.
- A build downloads unpinned code at execution time.
- A malicious update enters through a transitive dependency.

**Impact:** The verification environment executes unreviewed code or checks altered artifacts.

**Required controls**
- Pin dependencies and CI actions to immutable versions or commit identifiers where feasible.
- Verify hashes and provenance for downloaded artifacts.
- Minimize network access during critical verification runs.
- Review dependency and action updates.
- Generate and retain software bill of materials (SBOM) where practical.
- Separate dependency update workflows from proof verification workflows.
- Document which supply-chain risks remain unmitigated.

**Evidence:** Lockfiles, action pins, hashes, SBOM, provenance records, update review, network policy.

### T14 — CI, automation, and agent orchestration errors

**Failure modes**
- A workflow reports success after a required job was skipped.
- A script catches an exception and continues.
- An AI agent edits the theorem, test, or report to make a check pass.
- Generated files are stale or not regenerated.
- A workflow runs against a different commit than the one reported.
- Parallel jobs race or overwrite artifacts.

**Impact:** The repository presents a green result that does not correspond to the required verification process.

**Required controls**
- Define required checks explicitly and enforce their completion.
- Bind reports to exact commit SHA, claim version, workflow version, and toolchain manifest.
- Make skipped, cancelled, timed-out, and failed jobs distinct.
- Review changes to verification scripts and workflow configuration.
- Require human review for changes that alter theorem statements, assumptions, status rules, or required checks.
- Treat agent output as untrusted until reviewed and reproduced.
- Preserve raw logs and generated-artifact hashes.

**Evidence:** Workflow definitions, commit-bound reports, job outcomes, code review, agent change log, artifact hashes.

### T15 — Manuscript-to-proof correspondence failure

**Failure modes**
- The formal theorem differs from the published theorem.
- A definition or assumption changes between manuscript versions.
- A proof covers only a lemma while the report implies the full theorem.
- A statement is weakened during formalization without disclosure.
- A manuscript edit invalidates a previously audited correspondence record.

**Impact:** A valid formal proof is incorrectly represented as verification of the paper.

**Required controls**
- Maintain a claim-level correspondence record.
- Compare definitions, domains, quantifiers, hypotheses, side conditions, and conclusion strength.
- Bind each correspondence audit to exact manuscript and formal-source revisions.
- Require re-audit after either side changes.
- Keep formal proof status separate from correspondence status.
- Do not mark the manuscript claim Verified while correspondence is open.

**Evidence:** Side-by-side statement record, manuscript hash/version, formal source revision, correspondence checklist, reviewer approval.

### T16 — Provenance, history, and evidence-integrity failure

**Failure modes**
- Source files or reports are overwritten without traceable history.
- A report is copied from an earlier commit.
- A result cannot be tied to the source and dependencies that produced it.
- Logs are edited, truncated, or selectively published.
- A reviewer cannot determine which artifacts are authoritative.

**Impact:** Evidence cannot be trusted, audited, or reproduced.

**Required controls**
- Use version control and immutable commit identifiers for evidence.
- Record hashes for important inputs, outputs, certificates, and reports.
- Bind every result to a claim ID and exact source revision.
- Preserve failed and superseded reports with status history.
- Restrict write permissions and protect critical branches where available.
- Make canonical artifact locations and naming conventions explicit.

**Evidence:** Commit history, hashes, report metadata, access-control configuration, artifact index, status history.

### T17 — Human review, governance, and status manipulation

**Failure modes**
- Reviewers approve work without inspecting the relevant theorem or assumptions.
- A green badge is treated as a mathematical conclusion.
- Conflicts of interest or time pressure reduce scrutiny.
- A status is upgraded while obligations remain open.
- A failed result is omitted from the public record.
- Review criteria are relaxed after an inconvenient failure.

**Impact:** Governance fails even if individual tools behave as designed.

**Required controls**
- Separate authoring, verification, and approval roles where practical.
- Use claim-specific review checklists.
- Require explicit rationale for status transitions.
- Preserve dissent, unresolved issues, and failed checks.
- Require documented approval for changes to verification criteria.
- Never use layer count, test count, or CI green status as a proxy for correctness.
- Make residual risks visible to external reviewers.

**Evidence:** Review assignments, approvals, status-transition log, exception register, dissent and issue records.

### T18 — Availability, preservation, and reproducibility failure

**Failure modes**
- Tool versions, packages, source repositories, or external data disappear.
- A build depends on undocumented local files or private agent state.
- A long-running computation cannot be reconstructed.
- Artifacts are stored only in temporary CI output.
- Instructions omit necessary environment details.

**Impact:** Reviewers cannot verify the historical claim or reproduce the evidence.

**Required controls**
- Archive source, manifests, lockfiles, instructions, and essential outputs.
- Avoid dependence on private conversational or agent state.
- Record external data sources and retrieval dates.
- Preserve long-running job parameters, checkpoints, and logs.
- Document known limits to bit-for-bit reproducibility.
- Provide a clean reviewer path from repository checkout to reported result.

**Evidence:** Archive manifest, reproduction instructions, retained logs, external-source register, reproducibility report.


### T19 — Foundational inconsistency, unsatisfiable assumptions, and vacuity

**Threat:** A claim is accepted under contradictory foundations or mutually incompatible hypotheses, or a formally valid implication is vacuous because its hypotheses have no intended instances. A consistency assertion may also exceed what the available metatheory establishes.

**Failure modes:**
- An inconsistent axiom set permits arbitrary conclusions by explosion.
- Individually plausible assumptions cannot hold simultaneously.
- The theorem's domain or parameter constraints are empty or exclude every intended case.
- A vacuous implication is reported as a substantive mathematical or scientific result.
- Relative consistency is misreported as absolute consistency, or formal acceptance is mistaken for a consistency proof.

**Required controls:** L-13 assumption inventory; transitive axiom inspection; joint satisfiability/non-vacuity analysis; explicit witness/model or relative-consistency evidence where available; clear statement of undecidable or unresolved limits. L-04/L-05 kernel acceptance alone does not discharge this threat.

**Residual risk:** General consistency and satisfiability questions may be undecidable or inaccessible from the chosen metatheory. Unknown must remain visible.

### T20 — Mathematical model inadequacy and invalid applicability

**Threat:** A theorem or computation is correct for a mathematical model that does not adequately represent the intended target, or conclusions are extrapolated beyond the model's justified regime.

**Failure modes:**
- Unsupported mapping from a physical/empirical system to mathematical objects or parameters.
- Material mechanisms or constraints are omitted without justification.
- Idealizations, truncations, finite-size assumptions, or boundary conditions invalidate the intended interpretation.
- A finite/discrete result is presented as a continuum or thermodynamic conclusion without a valid limiting bridge.
- A mathematically correct result is presented as empirically predictive or explanatory without adequate validation.

**Required controls:** L-14 model specification, target-to-model correspondence, assumption/idealization register, applicability regime, sensitivity to reasonable modeling alternatives, and explicit distinction among mathematical validity, model adequacy, empirical fit, and predictive validity.

**Residual risk:** Model adequacy is domain-dependent and may remain partly empirical or judgment-based. A proof of the model's theorem does not eliminate this risk.

## 5. Cross-cutting attack scenarios

The following scenarios illustrate how multiple individually plausible failures can combine.

### Scenario A — A weaker theorem is proved and reported as the original theorem

1. A manuscript claim contains a universal quantifier over a broad domain.
2. During formalization, the domain is restricted to a convenient subtype.
3. Lean proves the restricted proposition.
4. CI succeeds.
5. The report links the proof file but does not compare the statements.

**Required detection:** T02, T03, T15, and T17 controls. The correspondence audit must fail or remain open. The original claim cannot be marked Verified.

### Scenario B — Two implementations agree because they share the same bug

1. A Python implementation produces a classification.
2. A Rust implementation is ported line-for-line from the Python algorithm.
3. Both use the same generated test cases and mathematical assumptions.
4. Their outputs agree.
5. The agreement is described as independent confirmation.

**Required detection:** T08 controls. The independence matrix must expose shared algorithmic and specification risk. Agreement may be reported as replication, not independent verification.

### Scenario C — A proof is accepted through an unreviewed axiom

1. A convenient helper theorem is introduced with an axiom.
2. A downstream theorem imports the helper.
3. The final theorem compiles.
4. The report records only a successful build.

**Required detection:** T04 and T06 controls. The transitive axiom audit must identify the assumption. The theorem remains unverified until the axiom is justified or discharged.

### Scenario D — A CAS result is exact-looking but not independently checked

1. A symbolic package returns a determinant identity.
2. The output is copied into the manuscript.
3. A script compares the two sides on sample values.
4. No proof or certificate checks the identity in the claimed domain.

**Required detection:** T07 and T09 controls. The result remains computational or exploratory evidence; sample agreement is not a universal proof.

### Scenario E — CI reports green after a required job is skipped

1. A workflow condition prevents the formal audit from running.
2. A wrapper script ignores the skipped state.
3. The aggregate job exits successfully.
4. The report displays a green badge.

**Required detection:** T14 controls. Required-job enforcement and explicit skipped-state handling must prevent a pass classification.

### Scenario F — A dependency update changes the trusted environment

1. A transitive package or action is updated through a mutable reference.
2. The verification job uses the new code.
3. No lockfile or provenance review is performed.
4. Existing status is carried forward without rerunning affected checks.

**Required detection:** T06 and T13 controls. Dependency changes must be pinned, reviewed, and followed by the required regression and audit process.

## 6. Risk assessment method

Risk ratings MUST not be used as a substitute for mathematical judgment. A low estimated likelihood does not justify hiding a catastrophic failure mode.

For each threat, the implementation register SHOULD record:

- **Impact:** What false conclusion or loss could result?
- **Likelihood rationale:** What evidence supports the estimate?
- **Detectability:** How likely is the failure to be detected before a claim is marked Verified?
- **Exposure:** Which claims, tools, and artifacts are affected?
- **Control strength:** Preventive, detective, corrective, or merely documentary.
- **Residual risk:** What remains possible after controls?
- **Owner and review date:** Who is responsible for the next assessment?

Use qualitative categories (Critical, High, Moderate, Low, Unknown) with written rationale. Unknown MUST NOT be silently treated as Low. Critical mathematical or correspondence threats MUST block Verified status until adequately addressed or explicitly resolved by a documented governance decision consistent with the charter.

## 7. Required threat-to-control traceability

Every threat ID in this document MUST map to one or more concrete controls in the implementation plan. Every control MUST map back to at least one threat or verification obligation.

The initial traceability set is:

| Threat ID | Area | Minimum control family |
|---|---|---|
| T01 | Mathematical reasoning | Specification review, dependency analysis, adversarial review |
| T02 | Specification | Versioned claim schema, quantifier/domain audit |
| T03 | Formalization | Elaborated-statement and definition review |
| T04 | Proof gaps and axioms | Transitive axiom/admission/escape audit |
| T05 | Kernel and prover | Pinned toolchain, kernel identity, independent checking where feasible |
| T06 | Libraries | Locked dependency closure and trust audit |
| T07 | CAS and exact algorithms | Exact-input record, certificate or independent check |
| T08 | Independence | Independence matrix and common-mode analysis |
| T09 | Numerics | Precision/error disclosure and exact follow-up |
| T10 | Certificates | Versioned format, bound inputs, independent checker testing |
| T11 | Compiler/build | Pinned toolchain, clean build, artifact identity |
| T12 | Hardware/environment | Run metadata, exit-state integrity, hashes |
| T13 | Supply chain | Immutable pins, provenance, SBOM, update review |
| T14 | CI and agents | Required-job enforcement, commit-bound reports, human review |
| T15 | Correspondence | Claim-to-manuscript audit and version binding |
| T16 | Evidence integrity | Immutable history, hashes, canonical artifact index |
| T17 | Human governance | Role separation, status approvals, exception history |
| T18 | Reproducibility | Archived artifacts, clean reviewer instructions |

This table is a minimum traceability baseline, not a fixed architecture or a claim that one control is sufficient for a threat.

## 8. Rules for declaring a threat controlled

A threat MUST NOT be marked “controlled” merely because a document mentions it or a tool exists.

A threat may be classified as:

- **Open:** No adequate control is implemented or evidenced.
- **Partially Mitigated:** Some controls exist, but important gaps remain.
- **Mitigated with Residual Risk:** Controls are implemented and evidenced; remaining risk is explicitly documented.
- **Accepted Exception:** A specific residual risk is consciously accepted with rationale, scope, approver, and review date. This label does not automatically permit a mathematical claim to be Verified.
- **Not Applicable:** A documented analysis shows why the threat does not apply to the specified claim or workflow.

Each classification MUST cite concrete implementation artifacts and test/audit evidence. This document alone does not close any threat.

## 9. Minimum implementation gates

Before a claim can receive **Verified** status, its verification record MUST demonstrate, as applicable:

1. Exact claim and specification are versioned.
2. Domain, quantifiers, assumptions, and conclusion have been reviewed.
3. Formal statement has been inspected and matched to the specification.
4. Transitive axioms, admitted obligations, oracles, and trust escapes have been audited.
5. Toolchain and relevant dependencies are identified and pinned.
6. Required proof and computational checks completed with interpretable results.
7. Independent checks are described honestly, including common-mode limitations.
8. Numerical evidence is not represented as exact proof.
9. Certificates are checked against the exact claim and input.
10. Manuscript-to-proof correspondence is approved against exact revisions.
11. Failed, skipped, timed-out, and inconclusive checks are visible.
12. Evidence is tied to immutable source revisions and can be reviewed.
13. Residual risks and assumptions are disclosed.

The applicable gates must be selected from the claim's threat profile. A generic checklist cannot replace claim-specific reasoning. If a gate is genuinely inapplicable, the record must explain why.

## 10. Residual risks and limitations

No practical verification architecture can prove that every tool, human, physical component, and assumption is infallible. Formal proof reduces important classes of mathematical reasoning risk but does not eliminate specification error, foundational assumptions, kernel risk, or correspondence error.

Independent implementations reduce some implementation risks but can preserve shared specification errors. Reproducible builds improve provenance but do not establish semantic correctness. Security scanning can identify known dependency risks but cannot guarantee the absence of malicious or defective code.

Constant Llapoy MUST therefore report assurance as bounded by explicit claims, assumptions, evidence classes, and trust boundaries. It MUST NOT claim absolute security, absolute correctness, or complete elimination of risk.

## 11. Maintenance and change triggers

This threat model MUST be reviewed when any of the following occurs:

- A new proof assistant, CAS, language, compiler, checker, or major dependency is introduced.
- A new verification layer or external oracle is added.
- A foundational inconsistency, vacuous theorem, unsatisfiable hypothesis set, or model-to-target mismatch is discovered.
- A theorem's statement, definitions, or assumptions change.
- A manuscript revision affects an audited claim.
- A vulnerability, soundness issue, or relevant tool defect is disclosed.
- A workflow, CI provider, agent, or build environment changes.
- A failure reveals a previously unmodeled threat.
- A reviewer identifies a common-mode or correspondence weakness.

Every revision MUST preserve history and state which threats, controls, and claims are affected.

## 12. Current implementation status

This is the initial threat model, not an implementation report.

At the time this document is created:
- The threat categories and required control families are specified here.
- No threat is considered mitigated solely by this document.
- No verification layer is declared operational by this document.
- No paper or theorem is declared verified by this document.
- The 14-layer candidate standard maps threats to candidate controls; claim-specific verification obligations, implementation evidence, and residual-risk assessments remain to be populated.

## 13. Governing rule

> **A threat is not controlled because we have named it. It is controlled only when a concrete control has been implemented, tested or audited, and its residual risk has been made visible.**

The threat model exists to challenge the verification system itself with the same rigor that the system is expected to apply to mathematical claims.
