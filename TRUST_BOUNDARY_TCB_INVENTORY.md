# Constant Llapoy — Trust Boundary & Trusted Computing Base Inventory

**Document status:** Initial trust inventory and design baseline  
**Version:** 0.1.0  
**Parent documents:** `ARCHITECTURE_CHARTER.md`, `THREAT_MODEL.md`  
**Scope:** Identification, classification, reduction, and explicit disclosure of components whose behavior is relied upon when producing or accepting mathematical verification evidence  
**Normative language:** MUST and MUST NOT are mandatory requirements; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Purpose

This document identifies the boundaries across which Constant Llapoy transfers mathematical meaning, proof obligations, executable artifacts, and verification conclusions.

The **Trusted Computing Base (TCB)** is the set of components, assumptions, people, and processes whose failure could cause the system to accept an incorrect mathematical claim as verified, or could cause the system to report a stronger conclusion than its evidence supports.

The TCB is claim- and workflow-dependent. There is no single universal TCB size for every paper or every verification route. A component may be inside the TCB for one route and outside it for another, depending on the evidence actually relied upon.

This inventory is a design artifact. It does not assert that the listed tools are installed, that any verification route is implemented, or that any paper has been verified.

## 2. Definitions and trust vocabulary

### 2.1 Trust boundary

A trust boundary is a point where data, meaning, authority, or execution crosses from one component or responsibility domain to another. Examples include:

- manuscript statement to machine-readable specification;
- specification to Lean theorem statement;
- source code to compiler output;
- proof term to kernel checking;
- computation to certificate;
- certificate producer to independent certificate checker;
- repository commit to CI execution;
- verification evidence to a human status decision.

Every material boundary MUST have a documented input contract, output contract, assumptions, failure modes, and validation procedure.

### 2.2 Trust classifications

| Classification | Meaning | Required treatment |
|---|---|---|
| TCB — relied upon | Failure can invalidate the accepted conclusion | Explicitly enumerate, version, audit, and minimize |
| Independently checked | Its output is checked by a separate mechanism with a documented contract | Record checker, assumptions, and independence limits |
| Evidence producer | Generates evidence but is not authoritative by itself | Never treat successful execution as proof |
| Untrusted input | May be malformed, incomplete, adversarial, or wrong | Validate; do not execute or accept blindly |
| Human-controlled assumption | Depends on mathematical judgment or review | State explicitly; obtain independent review where material |
| Out of scope | Not relied upon for the current claim or route | Explain why; do not imply it was audited |

“Independently checked” does not mean infallible. It means a distinct check reduces reliance on the producer, subject to the checker’s own TCB.

### 2.3 TCB is not the same as the whole software stack

A tool may be present in the workflow without being trusted for correctness. For example, a CAS can propose a factorization while a small exact checker verifies the returned factors and identity. In that route, the CAS is an evidence producer; the checker and its arithmetic foundation remain in the relevant TCB.

Conversely, a tool cannot be called “outside the TCB” merely because another programming language was used. Shared algorithms, specifications, libraries, generated code, compilers, hardware, or human assumptions can create common-mode failure.

## 3. TCB inventory by boundary

The following is the initial inventory. “Conditional” means inclusion depends on whether the claim’s accepted evidence route relies on that component.

| ID | Component / boundary | Initial classification | What can go wrong | Required treatment |
|---|---|---|---|---|
| TB-01 | Mathematical statement and definitions | Human-controlled assumption; TCB | Ambiguous terms, wrong domains, missing quantifiers | Freeze a claim-level specification; record author and reviewer decisions |
| TB-02 | Manuscript-to-specification translation | TCB unless independently audited | A theorem is silently weakened or changed | Bidirectional correspondence audit with exact statement comparison |
| TB-03 | Specification schema and parser | Conditional TCB | Fields dropped, defaults alter meaning, malformed data accepted | Version schema; validate strictly; test malformed and boundary cases |
| TB-04 | Lean theorem statement and imports | TCB for Lean route | Formal statement differs from intended theorem; hidden assumptions | Inspect elaborated declaration, dependencies, namespaces, and assumptions |
| TB-05 | Lean kernel / trusted proof checker | TCB for Lean route | Kernel defect or unsound trust escape | Pin toolchain; disclose trust boundary; seek independent routes for critical claims |
| TB-06 | Lean elaborator, compiler, tactics, automation | Evidence producer or conditional TCB | Incorrect elaboration, tactic bug, generated invalid object | Distinguish proof-term production from kernel checking; minimize opaque/external trust |
| TB-07 | Lean axioms, constants, admitted obligations, unsafe features | TCB / explicit assumption | Unproved premise enters theorem dependency graph | Enumerate transitively; classify each; prohibit undisclosed admissions |
| TB-08 | Imported Lean libraries and package graph | Conditional TCB | Incorrect theorem, hidden axiom, version drift | Pin revisions; inspect relevant declarations and transitive axioms |
| TB-09 | CAS / symbolic algebra system | Evidence producer by default | Incorrect simplification, algorithm bug, convention mismatch | Use exact arithmetic where possible; independently check outputs |
| TB-10 | Python and its runtime / packages | Evidence producer by default | Runtime, library, precision, or implementation defects | Pin environment; isolate logic; use exact types; independent checking |
| TB-11 | Rust and its compiler / crates | Evidence producer by default | Compiler, unsafe code, crate, overflow, or logic defects | Pin toolchain and crates; audit unsafe blocks; cross-check outputs |
| TB-12 | Certificate format and producer | Producer; format parser may be TCB | Incomplete or ambiguous certificate | Specify canonical format; reject unknown or missing fields |
| TB-13 | Certificate checker | TCB for certificate route | Checker accepts invalid certificate | Keep small; independent implementation; test negative cases and malformed inputs |
| TB-14 | Numerical libraries / floating-point hardware | Conditional TCB for numerical claims | Rounding, instability, overflow, platform variation | State error bounds and arithmetic model; never relabel numerical evidence as exact proof |
| TB-15 | Compiler, linker, interpreter, build system | Conditional TCB | Different executable than source implies; stale artifacts | Pin versions; record hashes; clean builds; independent reproduction |
| TB-16 | Operating system, CPU, memory, storage | Conditional TCB | Hardware faults, nondeterminism, corruption | Record environment; repeat critical checks; use independent machines when warranted |
| TB-17 | Dependency registry and supply chain | Conditional TCB | Compromised or replaced dependency | Lock versions and hashes; provenance; minimize and review dependencies |
| TB-18 | CI runner, workflow, action dependencies | Conditional TCB | Checks skipped, stale cache, wrong branch, forged status | Pin actions; inspect workflow; bind reports to commit and artifact hashes |
| TB-19 | Git hosting, access control, branch protection | Integrity TCB | Unauthorized changes, lost history, misleading branch state | Protect main; review changes; preserve immutable commit references |
| TB-20 | AI agents and generated code | Untrusted evidence producer | Fabricated results, silent edits, incorrect assumptions | Require reproducible artifacts; no agent self-certification |
| TB-21 | Human reviewers and status approvers | Human-controlled assumption | Oversight, conflict of interest, confirmation bias | Separate author and reviewer where possible; retain rationale and dissent |
| TB-22 | Report generator and status aggregation | Conditional TCB | Incorrectly converts partial evidence into “Verified” | Status rules as code plus human audit; fail closed on missing evidence |
| TB-23 | Time, locale, environment variables, configuration | Conditional TCB | Different behavior or hidden configuration | Capture relevant configuration; eliminate implicit defaults |
| TB-24 | Artifact storage, backups, and provenance records | Integrity TCB | Evidence mismatch, deletion, substitution | Content hashes, commit binding, backup/restore tests |

This table is not a claim that every component is currently in use. Each project-specific verification route MUST mark each row as **in use**, **not used**, or **unknown**, and provide evidence.

## 4. Minimal-trust design principles

Constant Llapoy MUST reduce unnecessary trust rather than merely list a large TCB.

1. **Kernel-check proof objects where possible.** Tactics and automation may search for proofs, but acceptance should depend on the designated proof checker and the declared axioms.
2. **Separate producers from checkers.** A complex CAS, Python script, Rust program, or AI agent should not be the sole judge of its own output.
3. **Prefer small checkers over large trusted producers.** A certificate may be generated by a sophisticated system and verified by a much smaller, simpler checker.
4. **Use exact representations for exact claims.** Rational, integer, algebraic, or other mathematically exact representations should be used when appropriate. Floating-point evidence must remain explicitly numerical.
5. **Make assumptions visible.** A theorem relying on classical choice, extensionality, excluded middle, custom axioms, or external assumptions must disclose them at the claim level.
6. **Pin dependencies and bind evidence to immutable revisions.** A passing result must identify the exact source, dependency graph, toolchain, configuration, and artifacts checked.
7. **Avoid single points of authority.** For high-consequence claims, seek genuinely distinct proof or checking routes.
8. **Fail closed.** Missing logs, unknown dependencies, unrecognized assumptions, failed correspondence, or stale artifacts must not produce a Verified status.
9. **Keep the mathematical claim authoritative.** No implementation convenience may redefine the theorem being checked.
10. **Do not confuse diversity with independence.** Different languages or vendors do not establish independence without a common-mode analysis.

## 5. Lean-specific trust boundary

For a Lean-based route, the system MUST distinguish at least these layers:

- the intended mathematical claim;
- the written Lean proposition;
- elaboration and generated proof term;
- the kernel’s checking of that term;
- imported declarations and their transitive dependencies;
- axioms and constants on which the declaration depends;
- compiler, runtime, package manager, and build environment used to produce the checked artifact.

A successful Lean build establishes that the configured Lean process accepted the source under its actual environment. It does **not**, by itself, establish that the proposition faithfully represents the manuscript theorem, that its assumptions are acceptable, or that all relevant dependencies are trustworthy.

For each theorem, the evidence record MUST include:

- fully qualified declaration name;
- exact source revision and file path;
- Lean version and toolchain identifier;
- dependency lock information and package revisions;
- transitive axiom/dependency report, including any admissions or unsafe trust escapes;
- build command and result;
- correspondence audit identifier;
- reviewer and review date;
- known limitations.

Any use of `sorry`, custom axioms, `admit`, unsafe declarations, external oracles, or other trust extensions MUST be detected and reported. Whether a particular axiom is mathematically legitimate is a claim-specific judgment, not a blanket ban or blanket approval.

## 6. Independent computation and certificate trust

### 6.1 Producer-checker separation

For every computational result used as evidence, record:

- producer name, version, source revision, and configuration;
- mathematical problem and exact input encoding;
- output format and its semantics;
- checker name, version, source revision, and configuration;
- whether producer and checker share libraries, algorithms, code, specifications, or authorship;
- negative tests demonstrating that invalid outputs are rejected.

A producer’s own “success” flag is not an independent check.

### 6.2 Python and Rust

Python and Rust MAY provide useful implementation diversity, but they MUST NOT be described as independent verification merely because they are different languages.

An independence assessment MUST consider:

- whether both implementations copied the same pseudocode or specification error;
- shared external libraries and algorithms;
- common generated source or code-generation tools;
- compiler/runtime and hardware dependencies;
- arithmetic semantics, overflow behavior, and precision;
- test data and oracle provenance;
- whether one implementation checks the other or both merely reproduce the same result.

Where feasible, use different algorithms and independently authored implementations, then compare exact outputs or check a certificate using a smaller trusted checker.

### 6.3 Exactness and numerical evidence

A numerical result MUST identify precision, rounding mode, error analysis, convergence criteria, conditioning, and exceptional cases as relevant. Numerical agreement can support confidence or falsify a conjecture; it cannot establish a universal theorem without a mathematically valid bridge such as a rigorous interval enclosure or a separately checked certificate.

## 7. Common-mode and correlated failure analysis

Each claimed independent route MUST have a written independence argument. At minimum, evaluate these shared dependencies:

| Shared factor | Possible correlated failure | Required question |
|---|---|---|
| Same mathematical specification | Both routes prove the wrong statement | Was the statement independently derived from the manuscript? |
| Same pseudocode | Same algorithmic defect | Are algorithms genuinely distinct? |
| Same library | Shared defect | Which library routines are relied upon? |
| Same compiler family | Common compiler defect | Is a different compiler or proof checker practical? |
| Same hardware / OS | Shared platform fault | Should critical checks run on another platform? |
| Same test oracle | Incorrect expected answer | How was the oracle established? |
| Same author / AI agent | Shared conceptual blind spot | Is there an independent reviewer? |
| Same generated source | Shared generation defect | Is generation itself checked? |
| Same dependency registry | Supply-chain compromise | Are artifacts pinned and verified by hashes? |

A diversity claim without this analysis MUST be labeled **independence not established**.

## 8. Claim-level TCB declaration

Every claim admitted to the verification registry MUST have a TCB declaration with at least the following fields:

| Field | Required content |
|---|---|
| Claim ID | Stable identifier |
| Claim revision | Exact revision of the mathematical statement |
| Evidence route | Lean, certificate, exact computation, numerical, or combination |
| In-scope components | Components actually relied upon |
| Out-of-scope components | Tools present but not relied upon, with rationale |
| Assumptions | Mathematical, environmental, and procedural assumptions |
| Axioms / trust extensions | Complete relevant list and judgment |
| Dependency snapshot | Immutable versions and hashes |
| Checker boundary | What checks the output and what the checker itself relies upon |
| Independence assessment | Common-mode risks and unresolved dependencies |
| Correspondence record | Link between manuscript and formal statement |
| Residual risk | Known unmitigated risks |
| Reviewer | Person responsible for independent assessment |
| Status | Not assessed, assessed with limitations, or approved for the stated route |

A generic repository-wide TCB list is not a substitute for a claim-specific declaration.

## 9. Trust-boundary validation requirements

Before a verification route can be used to support a Verified claim, the following checks MUST be completed as applicable:

1. **Input integrity:** verify source files, theorem statements, configuration, and dependencies against immutable revisions or hashes.
2. **Semantic correspondence:** independently compare manuscript definitions, domains, quantifiers, hypotheses, and conclusions with the formal specification.
3. **Assumption audit:** inspect transitive axioms, admitted declarations, unsafe features, external oracles, and hidden premises.
4. **Checker validation:** test the checker with valid, invalid, malformed, incomplete, and boundary certificates.
5. **Reproducibility:** rebuild from a clean environment and record the exact commands and outputs.
6. **Independence analysis:** document shared code, algorithms, libraries, tools, people, and infrastructure.
7. **Failure-path validation:** show that missing evidence, corrupted artifacts, version mismatches, and failed checks prevent approval.
8. **Status audit:** verify that the final status does not exceed the evidence actually obtained.

These are design requirements; implementation and evidence must be recorded separately.

## 10. Residual risk and limits of assurance

No finite software stack can prove its own complete correctness merely by reporting success. A small checker can reduce the amount of software trusted, but its specification, implementation, compiler, execution environment, and mathematical interface still require consideration.

Independent implementations can share conceptual mistakes. Formal proof can formalize the wrong theorem. Exact computation can solve the wrong problem. A valid proof can rely on unacceptable assumptions. Reproducible builds can reproducibly build incorrect software.

Accordingly:

- TCB reduction is risk reduction, not a declaration of absolute infallibility.
- Every assurance statement MUST name the route and assumptions to which it applies.
- Unknown or unaudited components MUST remain visible as residual risk.
- A claim MUST NOT be called Verified solely because all configured jobs passed.
- The status MUST be downgraded when a newly discovered trust failure invalidates prior evidence.

## 11. Required artifacts before layer architecture

The following artifacts are prerequisites for designing the detailed verification-layer architecture:

| Artifact | Purpose | Completion condition |
|---|---|---|
| Claim-level TCB template | Make trust explicit for each theorem | Fields defined and trialed on a real claim |
| Toolchain inventory | Identify exact tools and versions | All tools in an evidence route listed |
| Dependency inventory | Expose transitive dependencies | Lockfiles, revisions, hashes, and provenance recorded |
| Axiom / assumption report | Reveal formal trust extensions | Transitive assumptions captured per declaration |
| Producer-checker map | Separate generation from acceptance | Each evidence type has a named checker or limitation |
| Independence matrix | Prevent false diversity claims | Shared dependencies and common-mode risks documented |
| Correspondence protocol | Preserve theorem meaning | Manuscript-to-formal mapping is reviewable |
| Residual-risk register | Track unresolved trust | Each risk has severity, rationale, owner, and status |

The architecture MUST be derived from these artifacts and the Threat Model. It MUST NOT begin by assigning arbitrary names or counts to layers.

## 12. Initial unresolved decisions

These decisions remain open until the actual paper claims and toolchains are inventoried:

1. Which independent theorem prover, if any, will provide a genuinely distinct formal route alongside Lean.
2. Whether certificate checking can be standardized across exact algebra, combinatorics, and numerical proof obligations.
3. Which Python and Rust components will be evidence producers, independent implementations, or checkers.
4. Which claims require cross-platform or cross-compiler reproduction.
5. What minimum reviewer separation is practical for high-impact claims.
6. Which external assumptions are acceptable for each mathematical domain.
7. Which artifacts require long-term archival beyond the Git repository.

No decision should be made solely to make the architecture appear more comprehensive.

## 13. Relationship to the status protocol

This inventory does not itself verify any theorem. A completed TCB declaration is evidence about the transparency of a verification route, not proof of the mathematical claim.

A claim can be marked Verified only when its mathematical obligations, formal or exact evidence, correspondence, dependency and assumption audits, and claim-specific residual-risk assessment satisfy the governing status criteria. Where the trust boundary is unknown or materially unreviewed, the result MUST remain Not Verified, Inconclusive, or Partially Verified as appropriate.

---

## Governing principle

> **Trust as little as necessary; disclose everything that is trusted; independently check what can be checked; never report more certainty than the evidence warrants.**

Constant Llapoy does not seek a mythical zero-trust proof system. It seeks a transparent, minimized, claim-specific, and independently inspectable trust base.


## 14. Meta-verification component register

The current observed verification-system components and trust boundaries are catalogued in `META_VERIFICATION_COMPONENT_REGISTER.md`. That register is an initial partial snapshot, not a complete TCB audit. In particular, it records the single observed Lean GitHub Actions workflow, its pinned action references, the `ubuntu-latest` runner boundary, the Lean/Lake toolchain and dependency lock, and the fact that a dedicated repository-owned meta-verification test harness, certificate checker, and status aggregator were not observed in the inspected tracked-tree snapshot. Treat unobserved components as unknown rather than proving their nonexistence. Update this inventory when new status-affecting components are introduced.
