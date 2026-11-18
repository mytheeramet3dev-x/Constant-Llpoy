# Constant Llapoy — Verification Layer Catalog (14-Layer Candidate)

**Document status:** Current 14-layer candidate catalog; architecture remains provisional  
**Version:** 0.2.0  
**Effective date:** 2026-11-18  
**Normative specification:** `14_LAYER_VERIFICATION_STANDARD.md`  
**Parent documents:** `ARCHITECTURE_CHARTER.md`, `THREAT_MODEL.md`  
**Scope:** Conceptual inventory and implementation-status index for Constant Llapoy

---

## 1. Purpose and authority

This file is the concise catalog and navigation index for the current **14-layer candidate verification architecture**. The normative purpose, threat model, inputs, outputs, acceptance/failure conditions, applicability rules, and status protocol are specified in `14_LAYER_VERIFICATION_STANDARD.md`.

The 14-layer architecture is a provisional organization of current verification functions, not a final approval or completeness claim. It is not a permanent upper bound: the Architecture Charter continues to permit layers to be split, merged, replaced, or supplemented when documented threats and obligations justify doing so.

This catalog does not claim that all layers are implemented, validated, or applicable to every mathematical claim.

## 2. Current 14-layer candidate catalog

| ID | Layer | Core responsibility | Initial implementation posture |
|---|---|---|---|
| L-01 | Literature, Prior-Art, and Mathematical Claim Specification | Freeze exact claims and position them against prior knowledge | Claim registry and extraction artifacts exist; a complete literature/prior-art audit is claim-specific and not presumed |
| L-02 | Semantic Correspondence and Formalization Audit | Verify that formal and computational statements preserve manuscript meaning | Governance requirements exist; claim-level audits remain necessary |
| L-03 | Boundary, Domain, and Scope-Quantifier Audit | Audit domains, endpoints, quantifier order, parameter dependence, uniformity, and regularity | Newly specified; operational controls and claim-level audits remain to be established |
| L-04 | Primary Kernel-Checked Formal Verification (Lean 4) | Construct Lean proofs checked by the designated kernel | Active implementation for selected Paper A obligations; this is not whole-paper verification |
| L-05 | Independent Formal-Proof Route | Recheck selected claims through a genuinely distinct formal route | Conceptual; no project-wide independent prover route is established |
| L-06 | Exact Computational Verification | Verify exact finite and algebraic consequences with justified algorithms | Claim-dependent; no general project-wide framework is presumed |
| L-07 | Independent Implementation Cross-Checks | Compare separately developed implementations with assessed independence | No general independent route is presumed without implementation-specific evidence |
| L-08 | Proof-Certificate Production and Independent Checking | Separate result production from certificate validation | Conceptual; certificate formats and checkers remain claim-dependent |
| L-09 | Numerical Analysis and Adversarial Testing | Search edge cases and assess numerical behavior without treating it as proof | Partial, claim-specific evidence only; coverage must be audited |
| L-10 | Manuscript-to-Artifact Traceability and Synchronization | Bind claims to exact manuscripts, specifications, proofs, code, certificates, and reports; detect drift | Newly specified as a dedicated layer; end-to-end synchronization controls remain to be established |
| L-11 | Trust, Axiom, Dependency, and Supply-Chain Audit | Audit TCB, axioms, dependencies, provenance, and common-mode risks | Foundational inventories and some audit mechanisms exist; claim-specific coverage remains incomplete |
| L-12 | Reproducibility, Independent Review, and Evidence Governance | Reproduce, review, preserve, and honestly report verification evidence | Governance and CI infrastructure exist in part; end-to-end coverage remains incomplete |
| L-13 | Foundational Consistency, Assumption Satisfiability, and Non-Vacuity Audit | Assess foundational assumptions, joint satisfiability, realizability, and vacuity | Newly specified candidate; no general consistency or satisfiability decision procedure is claimed |
| L-14 | Mathematical Model Adequacy and Applicability Audit | Assess whether the model supports the intended interpretation and application | Newly specified candidate; claim-specific model maps and adequacy evidence remain to be established |

**Important identifier change:** Lean 4 is **L-04** in version 0.2.0. In the previous ten-function catalog (version 0.1.0), Lean 4 was L-03. Historical references must retain their original context; do not silently rewrite historical records.

## 3. Preservation of prior catalogs and identifier stability

All ten functions in catalog version 0.1.0 are preserved in substance. The previous Mathematical Claim Specification function is integrated with Literature and Prior-Art in L-01. The previous L-02 function remains L-02. Previous L-03 through L-10 functions are retained with new identifiers L-04 through L-12, respectively. The three additions are Literature/Prior-Art (integrated into L-01), Boundary/Domain/Scope-Quantifier Audit (L-03), and Manuscript-to-Artifact Traceability/Synchronization (L-10).

The exact migration table and rationale are maintained in Section 5 of `14_LAYER_VERIFICATION_STANDARD.md`. Earlier catalogs remain available in repository history; historical identifiers MUST NOT be silently rewritten.

## 4. Cross-layer obligations

The following controls apply across all relevant layers and are not additional numbered layers:

- Stable claim identity and exact source revision.
- Countermodel search versus proof of independence/necessity (L-03, L-06, L-09).
- Proof-dependency graph and circularity audit (L-02, L-11).
- Structural robustness and perturbation analysis, distinct from numerical stability (L-03, L-09).
- Foundational consistency, joint satisfiability, and non-vacuity (L-13).
- Model adequacy and applicability, when an external/applied target is claimed (L-14).
- Explicit assumptions, domains, quantifiers, and side conditions.
- Semantic correspondence between manuscript and formal/computational representations.
- Claim-specific trust-boundary declaration.
- Independence analysis wherever independence is claimed.
- Provenance, version pinning, and reproducibility.
- Failure preservation and discrepancy investigation.
- Change-impact analysis after material revisions.
- Honest status reporting and visible residual risk.

Every layer must be evaluated against the exact claim and the threat model. A layer entry in this catalog is not evidence that the layer has passed.

## 5. Applicability and status

Layer applicability is claim-specific and must be recorded in the Verification Obligation Matrix as Required, Conditional, Not applicable (with written justification), or Not assessed.

Layer status and claim status must not be conflated. The normative layer statuses are Specified, Implemented, Validated, Partially Implemented, Not Implemented, Inconclusive, and Failed. Claim statuses remain Verified, Partially Verified, Inconclusive, Failed, and Not Verified, as defined by the Architecture Charter and the 14-layer candidate standard.

A green CI result, a source file, a catalog entry, or a completed layer design does not automatically verify a mathematical claim.

## 6. Meta-verification specification

The cross-layer assurance requirements for checkers, parsers, CI/workflow orchestration, evidence revision binding, mutation testing, independent review, and fail-closed status aggregation are specified in `META_VERIFICATION_SPECIFICATION.md`. The component snapshot is maintained in `META_VERIFICATION_COMPONENT_REGISTER.md`. A policy evaluator, GitHub API collector, Sigstore-signed evidence producer, and separate provenance verifier are implemented; the bounded 52-test and end-to-end provenance results are recorded in those documents. These results do not establish mathematical proof correctness, a defect-free verification system, or an independently governed external trust root. Current provisional ownership is L-08, L-10, L-11, and L-12; no dedicated L-15 has been approved.

## 7. Governing statement

> **The catalog names the current verification functions; only claim-specific, auditable evidence can establish that an obligation has been met.**
