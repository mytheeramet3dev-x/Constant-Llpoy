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
