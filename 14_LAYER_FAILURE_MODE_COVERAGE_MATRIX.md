# Constant Llpoy — 14-Layer Failure-Mode Coverage Matrix

**Document status:** Initial threat-to-control analysis; design evidence only, not implementation or validation evidence  
**Version:** 0.1.0  
**Date:** 2026-11-18  
**Architecture baseline:** Provisional 14-layer candidate (14_LAYER_VERIFICATION_STANDARD.md)  
**Authority:** Read with ARCHITECTURE_CHARTER.md, THREAT_MODEL.md, LAYER_CATALOG.md, VERIFICATION_OBLIGATION_MATRIX.md, and the trust/toolchain inventories.

---

## 1. Purpose and limits

This matrix challenges the candidate architecture against concrete ways that a mathematical claim or its verification evidence can be wrong. It asks whether each failure mode has an owner, whether a second meaningfully different detection route exists, whether both routes can fail through shared dependencies, and what remains unproved after checks pass.

This is a design-level coverage analysis. It does not establish that a control exists in working code, has been executed, or is effective. Risk labels are qualitative prioritization judgments, not measured probabilities.

**Coverage labels:** Mapped = explicitly assigned; Partial = relevant controls exist but are not fully operationalized or independently tested; Gap = no sufficiently explicit control; Conditional = applies only to certain claims.

Absence of a counterexample in a finite or heuristic search is never treated as proof that no counterexample exists.

## 2. Failure-mode coverage matrix

| ID | Failure mode / false-acceptance path | Primary owner | Secondary challenge | Common-mode / residual risk | Design coverage |
|---|---|---|---|---|---|
| FM-01 | Incorrect informal inference or invalid proof step | L-01, L-02 | L-04/L-05 formal routes; L-12 independent review | Same mistaken argument or hidden lemma copied into both routes | Partial |
| FM-02 | Ambiguous, incomplete, or altered theorem statement | L-01 | L-02 and L-12 source comparison | Shared reliance on one defective claim extraction | Mapped |
| FM-03 | Formalization proves a weaker, stronger, or different proposition | L-02 | L-10 traceability; L-05/L-12 independent statement review | Both reviewers may accept the same incorrect semantic map | Mapped |
| FM-04 | Wrong domain, endpoint, quantifier order, parameter dependence, or uniformity | L-03 | L-05/L-06/L-09; L-13 for vacuity | Shared omitted edge case or identical parameter assumptions | Mapped |
| FM-05 | Contradictory axioms or inconsistent assumptions permit arbitrary conclusions | L-13 | L-11 axiom/TCB audit; L-05 alternative foundation where feasible | General consistency may be undecidable or only relative | Partial |
| FM-06 | Joint hypotheses unsatisfiable, domain empty, or implication vacuous | L-13 | L-03 scope audit; witness/model search; L-14 when applicable | Failed witness search does not prove impossibility | Partial |
| FM-07 | Hidden or unapproved axiom, admission, oracle, or trust extension | L-11 | L-04/L-05 axiom reports; dependency inspection | Shared tooling may omit the same transitive declaration | Mapped |
| FM-08 | Circular proof dependency or theorem depends indirectly on itself | L-02, L-11 | Dependency graph and L-12 review | Graph may omit implicit imports or semantic dependencies | Partial |
| FM-09 | Imported theorem/library lemma false, misused, or assumption-mismatched | L-11 | L-05 independent route; L-01 source review | Both routes may reuse the same library result | Partial |
| FM-10 | Proof assistant kernel, compiler, runtime, or build defect | L-04, L-11 | L-05 different prover; L-08 certificate checker; L-12 reproduction | Routes may share hardware, algorithms, assumptions, or infrastructure | Partial |
| FM-11 | Exact algorithm or CAS returns an incorrect result | L-06 | L-07 independent implementation; L-08 certificate | Same algorithm/specification or generated code shared | Mapped |
| FM-12 | Finite enumeration or sampling incomplete but reported exhaustive | L-06 | L-02 encoding audit; L-07 independent enumeration; L-09 tests | Same truncated universe or generator reused | Partial |
| FM-13 | Two implementations agree because they share a defect | L-07 | L-05/L-08 and explicit independence analysis | Shared spec, algorithm, libraries, code generation, tests, or people | Mapped |
| FM-14 | Certificate producer/checker accepts invalid or malformed evidence | L-08 | Small independent checker; negative-input tests; L-11 TCB audit | Shared parser, schema, or assumptions | Partial |
| FM-15 | Floating-point error, ill-conditioning, cancellation, or numerical artifact | L-09 | Exact L-06 route; independent precision/algorithm comparison L-07 | Same numerical model or tolerance biases multiple implementations | Mapped |
| FM-16 | Structural perturbation invalidates theorem outside stated regime | L-03, L-09 | L-13 assumption audit; L-14 sensitivity when applicable | Perturbation family may omit destabilizing direction | Partial |
| FM-17 | Correct theorem about inadequate or misidentified applied model | L-14 | L-01 model provenance; L-12 domain-expert review | Shared model assumptions and disciplinary blind spots | Partial / Conditional |
| FM-18 | Invalid extrapolation from finite/discrete result to continuum or thermodynamic limit | L-03, L-14 | L-04/L-05 limiting proof; L-09 diagnostics | Numerics suggest convergence without proving a limit | Partial / Conditional |
| FM-19 | Novelty or prior-art claim wrong or overstated | L-01 | Independent literature review L-12 | Search-source, keyword, and access blind spots | Partial |
| FM-20 | Manuscript, proof, code, certificate, and report refer to different revisions | L-10 | L-11 provenance; L-12 clean reproduction | Shared stale manifest or mutable artifact store | Mapped |
| FM-21 | Dependency compromise, version drift, or unrecorded transitive dependency | L-11 | L-10 immutable artifact binding; L-12 clean rebuild | Registry, source host, or build infrastructure compromise | Mapped |
| FM-22 | CI skips required job, uses wrong commit, or reports stale success | L-12 | L-10 source binding; independent workflow audit; negative CI tests | CI configuration and status reporter share trust boundary | Partial |
| FM-23 | Human confirmation bias, selective reporting, or status inflation | L-12 | Independent reviewer; preserved failures; L-10 evidence trail | Reviewers may share incentives or assumptions | Partial |
| FM-24 | Evidence irreproducible, lost, or lacks provenance | L-10, L-12 | L-11 dependency provenance; independent clean rebuild | Hosting/archive failure; non-deterministic tools | Mapped |
| FM-25 | Validator, parser, report generator, or status aggregator itself defective | L-08, L-10, L-11, L-12 | Independent negative/mutation tests, alternative checker, external review | Verifier cannot fully certify itself; tests may share defects | Partial — T21 |
| FM-26 | Countermodel search finds nothing and is treated as proof | L-03, L-06, L-09 | L-05 formal proof or completeness theorem for search | Incomplete search, bounded domain, heuristics, timeout | Mapped |
| FM-27 | Independence of assumptions inferred from examples or failed search | L-03, L-05, L-13 | Formal independence construction or model-theoretic argument | Shared metatheory or encoding | Partial |
| FM-28 | Theorem holds only under impossible, irrelevant, or overly narrow assumptions | L-01, L-03, L-13, L-14 | L-02 correspondence; domain/model review L-12 | Intent may be underspecified; authors share assumptions | Partial |

## 3. Cross-layer coverage and ownership rules

- **Countermodels and independence (B):** L-03 scopes the search; L-06 checks exact finite/model instances; L-09 performs adversarial search. L-05 or a formal model-theoretic argument is needed for positive independence claims. Search failure is not proof.
- **Circularity (C):** L-02 and L-11 maintain and inspect dependency graphs across definitions, assumptions, lemmas, theorems, imports, and generated artifacts. Syntactic import acyclicity alone may not establish semantic independence.
- **Robustness (E):** L-03/L-09 distinguish structural perturbation from numerical stability. Define perturbation class, admissible range, metric/topology, quantitative bound, and failure threshold where relevant.
- **Meta-verification (T21):** L-08/L-10/L-11/L-12 cover checker contracts, evidence binding, trust inventory, negative tests, mutation tests, independent review, and explicit residual risk.
- **No status laundering:** L-10/L-12 ensure skipped, stale, failed, partial, and inconclusive results cannot be aggregated into a passing claim status.

A layer may be marked Not applicable only with a claim-specific rationale. It may not be marked Not applicable merely because implementation is absent or difficult.

## 4. Common-mode failure analysis

| Common-mode source | How multiple layers can fail together | Required mitigation | Residual limitation |
|---|---|---|---|
| Shared claim specification | All routes verify the same wrongly stated claim | Independent extraction; reviewer comparison; immutable claim version | Reviewers can share interpretive assumptions |
| Shared definitions / encoding | Formal and computational routes use the same defective encoding | Independently inspect semantic maps; alternative encodings for critical claims | Independent encodings can share mathematical misunderstanding |
| Shared mathematical assumptions | Multiple routes inherit inconsistent or impossible hypotheses | L-13 inventory, satisfiability/non-vacuity analysis, relative-consistency limits | General consistency may be undecidable |
| Shared library / theorem dependency | Different proof files rely on the same defective theorem | Transitive dependency audit; alternative derivation for critical results | Full independent re-proving may be infeasible |
| Shared algorithm or generated code | Multiple implementations repeat the same defect | Distinct algorithms, independent implementations, minimal checker, mutation tests | Specification-level bugs can remain shared |
| Shared toolchain / infrastructure | Different checks use same compiler, runner, hardware, or artifact store | Distinct toolchains where justified; clean reproduction; external archive | Independence is bounded, never absolute |
| Shared numerical assumptions | Multiple runs use same precision, tolerances, discretization, or conditioning assumptions | Exact comparisons, interval/error bounds, alternate discretizations | Some quantities lack tractable exact forms |
| Shared reviewer / incentives | Independent-looking reviews reproduce confirmation bias | Critical review prompts, preserved dissent and failures | Human judgment cannot be fully mechanized |
| Shared CI and evidence pipeline | Multiple green reports derive from one skipped or stale job | Independent workflow audit, revision-bound attestations, negative tests | Hosting-provider and credential risks remain |
| Self-testing verifier | Defective checker validates its own tests and reports | External review, independent checker, mutation and malformed-input tests | No complete self-certification guarantee |

## 5. Highest-priority gaps and design decisions

### G-01 — Meta-verification design specified; operational assurance remains open

`META_VERIFICATION_SPECIFICATION.md` now defines component inventories, checker contracts, challenge tests, mutation/fault-injection requirements, exact revision binding, fail-closed aggregation invariants, independent review, evidence packages, and operational acceptance/failure gates. Provisional ownership remains across L-08, L-10, L-11, and L-12. This closes the design-specification gap only; no implementation, executed challenge suite, independent review, or operational validation is established by the document. The cross-layer versus dedicated-layer decision remains open and must be made only after the criteria in Section 12 of the specification are assessed against populated inventories and real evidence.

### G-02 — Foundational consistency cannot be promised as a universal pass/fail test

L-13 must distinguish logical consistency, relative consistency, joint satisfiability, intended-model realizability, and non-vacuity. Unknown/Undecidable/Inconclusive outcomes must remain available. A proof accepted under axioms does not certify the consistency of those axioms.

### G-03 — Model adequacy is conditional but must not disappear

L-14 is conditional for pure mathematics, but mandatory where physical, empirical, explanatory, or predictive claims are made. A mathematical theorem does not automatically validate its model interpretation.

### G-04 — Coverage is not completeness

The matrix includes known threat families, not every conceivable failure. Unknown unknowns, novel mathematics, new tools, and domain-specific threats remain possible. Update the threat model after every material failure or reviewer finding.

## 6. Acceptance gate for the architecture review

The candidate architecture must not be frozen as final until:

1. Every high-severity failure mode has a named owner and explicit acceptance/failure criteria.
2. Each critical failure mode has a credible secondary challenge or a written reason why one is unavailable.
3. Common-mode dependencies are mapped for every route described as independent.
4. L-13 distinguishes consistency, satisfiability, realizability, and vacuity without overclaiming decidability.
5. L-14 is mandatory for applicable external/applied claims and has a justified Not-applicable path for pure mathematics.
6. T21 meta-verification has a normative specification with concrete negative, malformed-input, mutation, fault-injection, revision-binding, fail-closed aggregation, and independent-review requirements; implementation and execution evidence remain separate acceptance gates.
7. The verification obligation matrix can represent every row in this failure-mode matrix at claim level.
8. All open gaps and residual risks are explicitly accepted; no gap is silently converted to a pass.

## 7. Current assessment

**Design-level conclusion:** The 14-layer candidate architecture maps the major currently enumerated failure families, but this mapping is not operational coverage. The largest unresolved design risk is meta-verification: the system must challenge its own checkers, parsers, CI orchestration, report generation, and status logic using evidence not wholly self-generated.

**Do not freeze the architecture yet.** Determine whether T21 can be governed robustly as a cross-layer obligation or requires a dedicated layer after acceptance criteria and an independent evidence route are designed.

**Implementation status:** This matrix is a design artifact only. No control is marked implemented or validated by its existence.

---

**Governing principle:** A failure mode is covered on paper only when it has an owner, observable acceptance criterion, failure path, and explicit residual-risk statement. It is controlled in practice only after implementation and evidence have been independently examined.