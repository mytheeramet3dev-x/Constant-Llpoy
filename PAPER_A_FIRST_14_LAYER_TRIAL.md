# Paper A — First 14-Layer Trial Execution Plan

Status: Execution pipeline implemented; first full evidence run pending CI observation.
Scope: Paper A only; Constant Llpoy repository only.
Frozen upstream source commit: 8deb7de4a49cb2060720246b7101820ee7e08c91.

## Purpose

Connect existing Paper A artifacts to a reproducible execution and evidence path. Do not force every layer to PASS. Execute checks with runnable implementations, preserve open obligations, and create an auditable baseline for the first full 14-layer trial.

## Five work packages

1. Component Evidence Production: run the pinned Lean build/axiom audit, two exact symbolic diagnostics, and two high-precision numerical diagnostics. Capture command, exit code, output, input hashes, and source commit.
2. End-to-End Integration: attest each evidence subject in the producer workflow; separately download the exact producer-run artifact, verify all seven attestations, bind run ID/attempt/source revision, and aggregate fail-closed.
3. Claim-to-Proof Traceability: parse all 15 Paper A claim rows; require matching claim records and frozen local source snapshots; hash records, source snapshots, Lean modules, and diagnostic scripts. Candidate links are not semantic correspondence.
4. 14-Layer Execution Plan: emit a complete 14-row assessment with applicability, result state, and rationale. Plan generation is not a layer PASS.
5. Paper A First Trial: run producer and verifier workflows on one immutable revision; inspect all seven artifacts and 14 layer outcomes before changing any claim status.

## Conservative first-pass layer assessment

| Layer | First-pass state | Reason |
|---|---|---|
| L-01 | PARTIAL | Prior-art coverage is not complete |
| L-02 | BLOCKED | Exact statement-to-formalization correspondence remains open |
| L-03 | PARTIAL | Not all claims have completed domain/quantifier audits |
| L-04 | FAILED | First observed current Lean build fails in PerronFrobeniusCore around lines 690–709; selected formalizations do not currently compile together |
| L-05 | NOT_RUN | No independent second prover route |
| L-06 | PARTIAL | Exact computations are finite-N diagnostics |
| L-07 | PARTIAL | Different formulations exist but common-mode risk remains |
| L-08 | PARTIAL | Provenance is not a proof-certificate checker |
| L-09 | PARTIAL | Numerical samples do not prove global behavior |
| L-10 | PARTIAL | Source hashes and candidate links do not prove semantic correspondence |
| L-11 | PARTIAL | External trust root is not active |
| L-12 | PARTIAL | External independent review is absent |
| L-13 | NOT_RUN | No claim-specific satisfiability/non-vacuity model checked |
| L-14 | NOT_ASSESSED | Model-to-target adequacy review not performed |

## Acceptance gate

The execution trial is operationally successful only if the producer completes all declared commands and emits exactly seven evidence subjects; every subject has a valid GitHub/Sigstore attestation for the exact revision; the verifier authenticates all seven with the exact run ID and attempt; the aggregator reports ACCEPTED; and the report still says overall_paper_status NOT_VERIFIED.

This gate concerns execution evidence and provenance only. It is not mathematical acceptance of Paper A.

## Not activated / not claimed

No external trust root, independent trusted builder, or external reviewer is active. Paper A is not fully formalized. Exact line-level manuscript-to-Lean correspondence is open. No theorem is promoted by a green workflow. L-13 does not decide general consistency. L-14 remains open.


## First observed execution issue

The first producer run, 44247984360, failed in the Lean action before evidence generation. The compiler reported RCLike (RCLike Real) synthesis errors and unresolved goals in PerronFrobeniusCore around lines 690–709. The producer now captures that failed command output and continues the remaining checks. The 14-layer assessment must show L-04 FAILED until the formalization is repaired and a fresh pinned build passes. This failure is not an issue with the verifier and must not be hidden by CI continuation settings.


## Observed first Paper A evidence run

- Producer workflow run: 44248949683 — SUCCESS, source commit 1173aba070abd89fcb5f62f14e7fd8494bdaa464.
- Separate component provenance verifier: 44249207601 — SUCCESS.
- Seven evidence subjects were emitted and each subject's GitHub/Sigstore attestation was cryptographically authenticated. The component report records true for all seven provenance-authentication flags.
- The aggregator returned REJECTED because PAPER_A_LEAN_BUILD is an authenticated FAIL. There were no missing or duplicate components, no stale fields, no evidence digest mismatches, and no unauthenticated provenance. The verified failure list contains exactly PAPER_A_LEAN_BUILD.
- The final verifier status is PAPER_A_EVIDENCE_BUNDLE_AUTHENTICATED_WITH_FAILED_CHECKS. This means the evidence bytes and origin were authenticated; it does not mean Paper A passed.
- Claim traceability completed for all 15 Paper A registry records and resolved frozen upstream source commit 8deb7de4a49cb2060720246b7101820ee7e08c91.
- Both exact symbolic diagnostics and both high-precision numerical diagnostics exited successfully. They remain finite-N / sampled diagnostics, not proofs.

### Observed 14-layer result

| Layer | Result |
|---|---|
| L-01 | PARTIAL |
| L-02 | BLOCKED |
| L-03 | PARTIAL |
| L-04 | FAILED |
| L-05 | NOT_RUN |
| L-06 | PARTIAL |
| L-07 | PARTIAL |
| L-08 | PARTIAL |
| L-09 | PARTIAL |
| L-10 | PARTIAL |
| L-11 | PARTIAL |
| L-12 | PARTIAL |
| L-13 | NOT_RUN |
| L-14 | NOT_ASSESSED |

The overall Paper A status remains NOT_VERIFIED. The Lean failure is in ConstantLlapoy.PaperA.PerronFrobeniusCore, with RCLike (RCLike Real) synthesis errors and unresolved goals around lines 690–709. No theorem was weakened or promoted to PASS.


## L-02 semantic correspondence audit — 2026-11-18

Added \`PAPER_A_LEAN_SEMANTIC_CORRESPONDENCE_AUDIT.md\` and its machine-readable companion \`meta_verification/paper_a_semantic_correspondence.json\`. All 15 registered Paper A claims are now explicitly classified against the four existing Lean modules, with exact claim-record blob SHAs, source line locators, Lean declaration names, and remaining hypothesis/model bridges.

Observed mapping:
- 0/15 claims have a complete direct Lean correspondence.
- 4 claims have only partial supporting declarations or an abstract matrix core (DEF-0001, PROP-0005, PROP-0009, THM-0002).
- 10 claims have no direct formalization in the four audited modules.
- PROP-0012 remains a source conflict; its conditional Lean lemmas do not verify the frozen opposite-sign assertion.

This is a traceability improvement, not an L-02 pass. **L-02 remains BLOCKED** pending independent semantic review and model-specific formalization. No Paper A claim status is promoted.
