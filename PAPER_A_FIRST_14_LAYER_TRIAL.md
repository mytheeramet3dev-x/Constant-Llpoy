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


## Confirmed current Paper A run — 2026-11-18

Exact source revision: \`1aff68f49d95c2d186576362cd1d392ae474269b\`.

| Stage | Run | Result |
|---|---:|---|
| Meta-verification harness | 44323177645 | SUCCESS — 275 tests passed in 31.865s |
| Pinned Lean build + axiom audit | 44323177442 | SUCCESS — 79 declarations audited; only \`propext\`, \`Classical.choice\`, \`Quot.sound\` |
| Paper A evidence producer | 44323177446 | SUCCESS — all 7 evidence subjects produced and individually attested |
| Separate Paper A provenance verifier | 44323720798 | SUCCESS — all 7 component attestations authenticated; aggregator ACCEPTED |

The authenticated component bundle reports:
- 7/7 required evidence components present and authenticated;
- no missing or duplicate components;
- no stale fields, evidence digest mismatches, pending/unverified components, unauthenticated provenance, or verified failures;
- producer run ID 44323177446, attempt 1;
- exact source commit bound to the evidence: \`1aff68f49d95c2d186576362cd1d392ae474269b\`.

The producer's 14-layer plan remains:
| Layer | Result |
|---|---|
| L-01 | PARTIAL |
| L-02 | BLOCKED |
| L-03 | PARTIAL |
| L-04 | PARTIAL |
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

**Overall Paper A remains NOT_VERIFIED.** The bundle acceptance is limited to execution-artifact completeness and GitHub/Sigstore provenance. The report explicitly records \`paper_a_claims_verified=false\`, \`external_trust_root=NOT_ACTIVE\`, and \`independent_external_review=NOT_COMPLETED\`. The Lean build passing does not close the 10 absent direct claim formalizations, the four partial/abstract correspondences, or the model-specific Hamiltonian bridge.


## TFIM encoding and shifted-matrix formalization — 2026-11-18

Exact source revision: \`4f6efbe9a1140007d73250940ed7c0ee97411842\`.

- Lean workflow run 44326403470: SUCCESS; \`lake build\` completed 18,266 jobs.
- Configured axiom audit: 103 declarations; all within \`[propext, Classical.choice, Quot.sound]\`.
- Paper A producer run 44326401521: SUCCESS; exact build transcript and four diagnostic outputs plus traceability and 14-layer plan were emitted and attested.
- Separate component provenance verifier run 44327033995: SUCCESS; final status \`PAPER_A_COMPONENT_EVIDENCE_PIPELINE_VERIFIED\`.

New formalized results in \`HamiltonianEncoding.lean\`:
1. Boolean computational-basis spin configurations and unordered interaction edges.
2. Exact diagonal ZZ interaction and off-diagonal \(-h\) single-spin-flip matrix entries.
3. Hermitian/symmetric property of the encoded Hamiltonian.
4. Explicit finite shift \(c=1+\sum_s |H_{ss}|\), with \(c>H_{ss}\) for every configuration.
5. Shifted matrix \(K=cI-H\) is entrywise nonnegative for \(h\ge0\).
6. For \(h>0\), a distinct off-diagonal entry of \(K\) is positive exactly when the configurations differ at one spin.

This advances THM-0002's model-to-matrix bridge, but it does **not** yet prove hypercube connectivity in \`PFReachable\`, Hermitian/spectral transfer for the shifted matrix, or existence of a strictly positive eigenvector for its top eigenvalue. Thus L-04 remains PARTIAL and THM-0002 remains not formally verified. L-02 remains BLOCKED.


## Updated verified Paper A trial — commit 232686de6761b63ebcce6073d5de0867ef320405

- Lean workflow run \`44330440325\`: SUCCESS; build completed 18,266 jobs; axiom audit covered 107 declarations, all within \`propext\`, \`Classical.choice\`, and \`Quot.sound\`.
- Component producer run \`44330440437\`: SUCCESS; all five execution components returned PASS: Lean build, exact Dicke diagnostic, exact strong-coupling diagnostic, finite-difference diagnostic, and weak-coupling numerical diagnostic.
- Claim traceability: 15/15 registry records located and hashed; semantic correspondence remains NOT_ESTABLISHED.
- Four diagnostic commands exited 0. These are finite-N / sampled execution results, not theorem proofs.
- The 14-row assessment was: L-01 PARTIAL; L-02 BLOCKED; L-03 PARTIAL; L-04 PARTIAL; L-05 NOT_RUN; L-06 PARTIAL; L-07 PARTIAL; L-08 PARTIAL; L-09 PARTIAL; L-10 PARTIAL; L-11 PARTIAL; L-12 PARTIAL; L-13 NOT_RUN; L-14 NOT_ASSESSED.
- External trust root: NOT_ACTIVE. Independent external review: NOT_COMPLETED. Overall Paper A: NOT_VERIFIED.
- Separate provenance verifier run \`44330971751\` succeeded for the exact source commit and evidence artifact.

The successful Lean build verifies compilation of the current formalized declarations only. It does not complete the manuscript's full 14-layer verification or prove the ground-state Perron–Frobenius claim.


## Updated evidence run — commit 5eed2081099023631f41e31da9533a3741670b16

- Lean workflow \`44331504425\`: SUCCESS; 18,266 build jobs; axiom audit covered 107 declarations, all within the configured allowlist.
- Paper A evidence producer \`44331504302\`: SUCCESS; all five execution components PASS.
- The Lean evidence manifest includes all five Paper A Lean modules and the root \`ConstantLlapoy.lean\`, including the new \`HamiltonianEncoding.lean\` module.
- Claim traceability: 15/15 records located and hashed; semantic correspondence remains NOT_ESTABLISHED.
- Four computational diagnostics executed successfully, but remain finite-N / sampled diagnostics rather than theorem proofs.
- Separate component provenance verifier \`44332051326\`: SUCCESS for the exact producer artifact.
- 14-layer assessment unchanged: L-01 PARTIAL; L-02 BLOCKED; L-03 PARTIAL; L-04 PARTIAL; L-05 NOT_RUN; L-06 PARTIAL; L-07 PARTIAL; L-08 PARTIAL; L-09 PARTIAL; L-10 PARTIAL; L-11 PARTIAL; L-12 PARTIAL; L-13 NOT_RUN; L-14 NOT_ASSESSED.
- External trust root NOT_ACTIVE; independent external review NOT_COMPLETED; overall Paper A NOT_VERIFIED.
