# Constant Llapoy — Toolchain & Dependency Inventory

**Document status:** Initial inventory framework and baseline  
**Version:** 0.1.0  
**Parent documents:** `ARCHITECTURE_CHARTER.md`, `THREAT_MODEL.md`, `TRUST_BOUNDARY_TCB_INVENTORY.md`  
**Scope:** Identification, pinning, provenance, integrity, audit, and reproducibility of tools and dependencies that may affect mathematical verification  
**Normative language:** MUST and MUST NOT are mandatory requirements; SHOULD is a strong recommendation; MAY is optional.

---

## 1. Purpose

This document defines how Constant Llapoy identifies and controls the toolchains and dependencies used to produce, check, build, test, and report mathematical verification evidence.

A named tool is not an installed tool. A planned tool is not an approved tool. A successful installation is not evidence of correctness. This inventory therefore separates:

1. candidate tools under consideration;
2. tools confirmed to be present in a particular environment;
3. tools approved for a specified verification role;
4. exact versions and dependency revisions actually used for a claim;
5. tools and dependencies whose trust implications remain unknown.

**Current baseline:** This document does not claim that Lean, Python, Rust, a CAS, an independent theorem prover, or any other verification tool has been installed or configured in the repository. Exact versions remain **UNRECORDED** until captured from an actual environment and committed as evidence.

## 2. Inventory rules

Every tool or dependency used in a verification route MUST have a record containing, where applicable:

- stable inventory ID and exact package/tool name;
- role in the verification workflow;
- status: proposed, detected, approved, deprecated, blocked, or unknown;
- exact version, build identifier, and platform;
- source repository or distribution origin;
- immutable revision, package checksum, or artifact digest;
- direct and transitive dependencies;
- license and redistribution constraints;
- known vulnerabilities and advisory review date;
- configuration, plugins, extensions, and environment variables that can affect results;
- whether it is a producer, checker, trusted component, or infrastructure component;
- mathematical and computational assumptions;
- independent validation method;
- reproducible installation and execution instructions;
- evidence paths and claim IDs that rely on it;
- owner, reviewer, and last audit date.

Missing information MUST be recorded as **UNKNOWN**, not silently omitted or guessed.

### 2.1 Status meanings

| Status | Meaning |
|---|---|
| Proposed | Candidate only; not yet detected or approved |
| Detected | Version and environment were observed, but role is not approved |
| Approved | Reviewed for a clearly specified role and scope |
| Deprecated | Retained for historical reproduction but not new verification |
| Blocked | Known issue prevents use for the specified role |
| Unknown | Evidence is insufficient to determine the state |

Approval is role-specific. A tool may be approved to generate conjectures but not to certify proofs.

## 3. Candidate toolchain map

The following list is a candidate architecture inventory, not an assertion of installation or approval.

| ID | Toolchain / component | Intended role | Initial status | Approval condition |
|---|---|---|---|---|
| TC-01 | Lean 4 | Primary formal theorem proving and kernel-checked proof artifacts | Proposed / version unrecorded | Pin toolchain and packages; audit declaration assumptions and correspondence |
| TC-02 | Independent theorem prover (Isabelle/HOL or Rocq/Coq, to be decided) | Independent formalization route for selected claims | Proposed / not selected | Demonstrate meaningful semantic and implementation independence for the target claim |
| TC-03 | Python | Exact computation, orchestration, analysis, and test harnesses | Proposed / version unrecorded | Pin interpreter and packages; exact arithmetic where required; independent checking |
| TC-04 | Rust | Independently authored computational tools and small checkers where justified | Proposed / version unrecorded | Pin compiler and crates; audit unsafe code; define arithmetic and overflow semantics |
| TC-05 | SymPy or another symbolic algebra system | Symbolic exploration and exact algebraic computation | Proposed / not selected per task | Exact input semantics; output checked independently; algorithm limits documented |
| TC-06 | Computer algebra alternative (e.g. SageMath) | Cross-check selected symbolic or algebraic computations | Proposed | Identify shared libraries and common-mode risks; do not assume independence |
| TC-07 | SMT solver (e.g. Z3 or cvc5) | Satisfiability and decision-procedure assistance for suitable obligations | Proposed | Treat solver output as evidence requiring proof/certificate or independent validation |
| TC-08 | Proof/certificate checker | Small trusted validation of computational certificates | Proposed / design pending | Specify certificate language, soundness argument, negative tests, and implementation audit |
| TC-09 | Git | Source and evidence version control | Detected as repository platform dependency; local version unrecorded | Record local version and exact commit references for each run |
| TC-10 | GitHub Actions or other CI runner | Automated reproducibility and status checks | Proposed / workflow state unverified | Audit workflows, pin actions, bind results to immutable commits |
| TC-11 | Container/build environment (Docker, Podman, Nix, or equivalent) | Environment capture and reproducible execution | Proposed / selection pending | Pin image or derivation digest; disclose host dependencies |
| TC-12 | Artifact hashing tools (e.g. SHA-256 implementation) | Bind evidence to immutable content | Proposed | Record algorithm and implementation; verify hashes independently where warranted |
| TC-13 | Documentation/report generator | Produce human-readable audit records | Proposed | Ensure reports are derived from machine-readable evidence and fail closed |
| TC-14 | AI coding/research agents | Drafting, implementation assistance, and exploratory analysis | Untrusted producer | No self-certification; all outputs reviewed and reproducibly checked |

The examples above are candidates only. Inclusion does not imply endorsement, installation, or mathematical trust.

## 4. Toolchain selection principles

Tool selection MUST be driven by the mathematical obligation and threat model, not popularity or convenience.

1. **Fit to obligation:** choose tools that can represent the relevant mathematical objects and assumptions without changing the claim.
2. **Small trusted core:** prefer a small independently checkable proof or certificate kernel when practical.
3. **Independent diversity:** choose genuinely different algorithms or proof foundations when independence is required; different languages alone are insufficient.
4. **Exactness:** prefer exact arithmetic for exact claims; document numerical approximation and error bounds for numerical evidence.
5. **Transparency:** favor inspectable formats, open specifications, stable versioning, and accessible logs.
6. **Reproducibility:** require a clean, documented installation and execution path.
7. **Long-term preservation:** archive source, dependencies, checksums, and enough metadata to reproduce historical results.
8. **No convenience override:** a tool must not be selected because it makes a theorem easier to pass by weakening its formal meaning.

## 5. Version and provenance policy

### 5.1 Exact version pinning

Every accepted verification run MUST record exact versions, not broad labels such as “latest”, “Python 3”, or “Lean 4”.

Record at least:

- tool name and exact version;
- compiler/build identifier where available;
- operating system, architecture, and relevant runtime;
- package manager and lockfile version;
- exact dependency revisions;
- environment configuration that can change semantics;
- command line used;
- source commit and artifact hashes.

A version upgrade creates a new verification environment. Prior results MUST NOT automatically transfer to the upgraded environment.

### 5.2 Immutable source references

For source-controlled dependencies, record immutable commit hashes or release tags together with verified artifact hashes. A mutable branch name is not sufficient provenance.

For registry packages, record exact resolved versions and cryptographic checksums from the lockfile or equivalent package metadata. Where the ecosystem does not provide reliable checksums, record that limitation and add an independent retrieval or archival procedure.

### 5.3 Provenance record

For each downloaded or built executable that materially affects evidence, retain:

- origin and retrieval date;
- publisher or maintainer identity as represented by the source;
- release signature or checksum verification result, if available;
- build provenance or attestation, if available;
- source revision and build instructions, if built from source;
- any discrepancy between source and distributed binary.

A signature authenticates a claimed origin; it does not prove the software is mathematically correct.

## 6. Ecosystem-specific inventory requirements

### 6.1 Lean and Lake

For every Lean project or formalization:

- pin the Lean toolchain in the repository;
- commit the Lake manifest and configuration required for exact dependency resolution;
- record Lean and Lake versions;
- record every package revision and transitive dependency;
- preserve the exact build command and complete output;
- capture declaration-level axiom and dependency reports;
- identify custom axioms, admissions, unsafe declarations, external oracles, and trust extensions;
- rebuild from a clean checkout;
- bind results to the exact Git commit.

A successful build MUST NOT be treated as a proof-to-manuscript correspondence audit.

### 6.2 Python

For every Python evidence-producing or checking program:

- pin the Python implementation and exact version;
- use a committed lockfile or fully resolved environment specification;
- record package hashes and transitive dependencies;
- distinguish standard-library use from third-party packages;
- specify exact numeric types and prohibit accidental float conversion in exact calculations;
- record random seeds and nondeterministic settings where relevant;
- test boundary cases, malformed inputs, and failure behavior;
- separate exploratory notebooks from authoritative verification scripts;
- use an independently authored checker for consequential outputs.

Python environment examples such as `venv`, `uv`, Poetry, or Conda are alternatives, not mandatory choices. The project MUST choose and document one reproducible strategy per workflow rather than mix implicit environments.

### 6.3 Rust

For every Rust evidence-producing or checking program:

- pin the Rust toolchain and target triple;
- commit `Cargo.lock` for executable applications and verification tools;
- record crate versions, checksums, features, and transitive dependencies;
- audit all `unsafe` blocks and dependencies that expose unsafe behavior;
- define overflow, integer width, rounding, and serialization semantics;
- use compiler and lint settings explicitly;
- test parser rejection, invalid certificates, and boundary conditions;
- record build profile and target configuration.

Rust's type system and memory-safety guarantees do not establish algorithmic correctness or mathematical soundness.

### 6.4 Computer algebra systems

For SymPy, SageMath, or another CAS:

- record exact version and build;
- record symbolic assumptions, domains, variable declarations, and simplification settings;
- distinguish exact domains from floating-point domains;
- preserve the complete input expression and output;
- document algorithms used when known;
- identify external libraries and native backends;
- independently verify identities, factorizations, roots, or certificates where possible;
- document resource limits, timeouts, and incomplete computations.

A CAS returning an expression is not, by itself, a proof that the expression is correct.

### 6.5 SMT solvers and decision procedures

For Z3, cvc5, or another solver:

- record solver version, logic, options, and input format;
- preserve the exact problem instance;
- record whether the result is sat, unsat, unknown, timeout, or error;
- retain proof objects or certificates if supported;
- validate certificates with a separate checker where feasible;
- disclose theory-specific assumptions and unsupported fragments;
- never translate `unknown` or timeout into a passing result.

### 6.6 Independent theorem prover

The second prover MUST be selected only after an independence analysis. The evaluation MUST consider:

- logical foundations and axiom policies;
- kernel or proof-checking architecture;
- library dependencies and imported results;
- formalization effort and semantic translation;
- automation and external solver reliance;
- compiler, runtime, and build chain;
- availability of proof objects or independent checking;
- ability to audit the same claim without copying the same formalization error.

The project MUST NOT claim independence merely because two theorem provers have different names.

## 7. Dependency graph and software bill of materials

Each verification environment SHOULD produce a machine-readable dependency graph or software bill of materials (SBOM) that captures direct and transitive dependencies.

The record MUST identify:

- direct dependency;
- transitive dependency;
- exact version or revision;
- source registry or repository;
- checksum or immutable identifier;
- license;
- known security advisories at audit time;
- whether the dependency is in the mathematical TCB, build TCB, evidence producer set, or merely tooling;
- which claims and artifacts depend on it.

A vulnerability scanner or SBOM is a visibility tool. A clean scan does not prove correctness, and the absence of a known advisory does not establish safety.

## 8. Dependency risk and change management

Dependencies MUST be reviewed when:

- a version changes;
- a transitive dependency changes;
- a package is added or removed;
- a build backend or compiler changes;
- a security advisory affects an in-scope component;
- a maintainer, origin, signature, or distribution channel changes;
- an artifact cannot be reproduced;
- an upstream project becomes abandoned or compromised.

Every update MUST state:

1. why the change is needed;
2. which claims and evidence routes are affected;
3. what changed in the dependency graph;
4. what audits and tests were rerun;
5. whether prior evidence remains valid;
6. reviewer and approval record.

Automated dependency updates MUST NOT be merged into an authoritative verification environment without review and required rechecks.

## 9. Reproducible environment policy

Each authoritative verification route MUST provide a clean-checkout procedure that does not depend on undocumented local state.

The procedure SHOULD:

- use a pinned container image or reproducible environment definition;
- pin package and toolchain versions;
- avoid unpinned downloads during the verification run;
- disable or identify network-dependent behavior;
- use explicit locale, timezone, environment variables, and configuration;
- record CPU architecture and relevant hardware assumptions;
- separate build artifacts from source inputs;
- produce machine-readable logs and exit status;
- verify hashes of inputs and outputs;
- fail when required versions or hashes do not match.

Containers improve environment isolation but do not eliminate trust in the host kernel, CPU, image supply chain, or container runtime. Reproducible build claims MUST identify their limits.

## 10. Initial inventory register

The following register is intentionally conservative. It records current knowledge from repository inspection, not an assumed development machine state.

| Inventory item | Current state | Evidence required to update |
|---|---|---|
| Constant Llapoy repository | Repository and three governance documents confirmed in GitHub | Commit IDs and file references |
| Lean installation/version | UNKNOWN | Actual `lean --version`, toolchain file, clean build log |
| Lean packages | UNKNOWN | Lake manifest, package revisions, dependency graph |
| Python installation/version | UNKNOWN | Actual interpreter version and executable path |
| Python packages | UNKNOWN | Lockfile, resolved package list, hashes |
| Rust installation/version | UNKNOWN | Actual `rustc --version`, `cargo --version`, target list |
| Rust crates | UNKNOWN | `Cargo.lock`, dependency tree, checksums |
| CAS installation/version | UNKNOWN | Selected CAS, version, configuration, environment capture |
| Independent prover | NOT SELECTED | Decision record and independence assessment |
| SMT solver | NOT SELECTED | Use-case justification, version, logic, certificate strategy |
| Certificate checker | NOT IMPLEMENTED / UNKNOWN | Specification, source, test suite, independent audit |
| CI workflows | UNKNOWN | Workflow files, pinned actions, runner details, run evidence |
| Container/reproducible environment | NOT SELECTED | Environment definition, image or derivation digest |
| SBOM generation | NOT IMPLEMENTED / UNKNOWN | Tool, format, generated artifact, review procedure |
| Vulnerability/advisory process | NOT IMPLEMENTED / UNKNOWN | Scanner configuration, advisory sources, review logs |
| Artifact hash/provenance process | DESIGN REQUIRED | Hash manifest, provenance record, verification procedure |

No entry may be changed from UNKNOWN to DETECTED or APPROVED without attaching the evidence specified in the final column or an equivalent reviewed record.

## 11. Required repository artifacts

The following files are proposed for later implementation. Their absence MUST be reported accurately; this document does not claim they already exist.

| Proposed path | Purpose |
|---|---|
| `toolchain/TOOLCHAIN_MATRIX.md` | Human-readable approved tool and version matrix |
| `toolchain/lean-toolchain` | Exact Lean toolchain pin, once selected |
| `toolchain/lake-manifest.json` | Resolved Lean dependency snapshot, when generated |
| `toolchain/python/pyproject.toml` | Python project and dependency declarations, if Python is used |
| `toolchain/python/lockfile` | Exact Python environment lock, format chosen by project |
| `toolchain/rust/rust-toolchain.toml` | Rust toolchain pin, if Rust is used |
| `toolchain/rust/Cargo.toml` and `Cargo.lock` | Rust dependencies and exact resolution |
| `toolchain/containers/` | Pinned environment definitions, if selected |
| `toolchain/sbom/` | Software bill of materials and dependency snapshots |
| `toolchain/provenance/` | Download, signature, hash, and build provenance records |
| `toolchain/advisories/` | Dependency security review records |
| `toolchain/reproduction/` | Clean-checkout commands and reproduction logs |

Do not create empty lockfiles or placeholder version pins merely to make the repository look complete. A lockfile must be generated by the actual selected package manager and checked against the real environment.

## 12. Acceptance gates before a tool is used for a claim

A tool may support a claim only after the applicable gates are satisfied:

- **G0 — Role defined:** the mathematical or engineering obligation assigned to the tool is explicit.
- **G1 — Identity known:** exact tool, version, origin, and platform are recorded.
- **G2 — Dependencies known:** direct and transitive dependencies are captured to the extent supported by the ecosystem.
- **G3 — Trust role declared:** producer, checker, TCB, or infrastructure role is documented.
- **G4 — Output contract defined:** inputs, outputs, semantics, failure states, and limitations are explicit.
- **G5 — Validation available:** independent checks, test strategy, or formal assurance argument is specified.
- **G6 — Reproducible:** a clean environment can reproduce the relevant artifact or the limitation is recorded.
- **G7 — Claim binding:** exact source and toolchain are bound to the claim's evidence record.
- **G8 — Reviewed:** a reviewer has assessed the tool's role and residual risks.

A tool that fails a gate MUST NOT silently contribute to a Verified status. It may still be used for exploration if its output is clearly labeled non-authoritative.

## 13. Open decisions and required evidence

These decisions remain open:

1. Which Lean version and package baseline will be used for the first formalization?
2. Which second theorem prover offers meaningful independent checking for the actual mathematical claims?
3. Which Python environment manager best supports reproducibility and transparent lockfiles?
4. Which Rust toolchain and crate policy will be used for independent checkers?
5. Which CAS is needed for the actual exact algebraic obligations, and which outputs can be checked independently?
6. Are SMT solvers necessary for any target proof obligations, and can their outputs be certified?
7. Which CI runner and pinned action strategy will be acceptable?
8. Will the project use containers, Nix, or another reproducible environment mechanism?
9. Which SBOM format and vulnerability review process will be adopted?
10. Which artifacts must be archived independently of GitHub for long-term reproducibility?

These decisions MUST be made from actual claim requirements and threat analysis, not from a desire to maximize the number of tools.

## 14. Relationship to verification status

This inventory is not mathematical evidence and does not verify any theorem. A fully pinned toolchain only establishes which environment was used; it does not establish that the tools are correct or that the theorem is true.

A claim's status must reflect the exact tools and dependencies used in its evidence route. If a critical version, dependency, source hash, assumption, or execution environment is unknown, the limitation MUST be recorded and the status MUST NOT exceed what the available evidence justifies.

---

## Governing principle

> **No invisible tools, no floating versions, no untracked dependencies, and no claim of reproducibility without a reproducible record.**

Constant Llapoy will treat every toolchain as an auditable part of the evidence process, not as an unquestioned authority.


## 15. Meta-verification component and dependency snapshot

Use `META_VERIFICATION_COMPONENT_REGISTER.md` as the current observed inventory for the Constant Llpoy Lean workflow and its status-affecting dependencies. The snapshot records the exact workflow blob SHA, the pinned `actions/checkout` and `leanprover/lean-action` commit references, Lean 4.36.0, the Lake project configuration, Mathlib commit, and transitive Lake package revisions. It also records `ubuntu-latest` and GitHub Actions status/log infrastructure as external boundaries whose exact runtime image and retention/attestation configuration are not established by the workflow source alone. SHA pinning and a lockfile improve identity and reproducibility; neither is a substitute for source, dependency, and provenance review. Reconcile this register with this inventory after any workflow, toolchain, manifest, or dependency change.
