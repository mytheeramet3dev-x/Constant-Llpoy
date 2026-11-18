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


## Updated Paper A trial — commit d772706992a2e5e86d3205dbcae0fd8428e91923

- Lean workflow run \`44334091727\`: SUCCESS; 18,266 build jobs; axiom audit covered 109 declarations, all within \`propext\`, \`Classical.choice\`, and \`Quot.sound\`.
- Paper A evidence producer run \`44334091894\`: SUCCESS; Lean build and all four finite-N / high-precision diagnostic commands returned PASS.
- The evidence manifest includes all five Paper A Lean modules, the root \`ConstantLlapoy.lean\`, and the exact source hashes.
- Claim traceability: 15/15 records located and hashed. Semantic correspondence remains NOT_ESTABLISHED.
- Separate Paper A provenance verifier run \`44334708201\`: SUCCESS; the exact producer evidence bundle was authenticated.
- The 14-layer assessment remains: L-01 PARTIAL; L-02 BLOCKED; L-03 PARTIAL; L-04 PARTIAL; L-05 NOT_RUN; L-06 PARTIAL; L-07 PARTIAL; L-08 PARTIAL; L-09 PARTIAL; L-10 PARTIAL; L-11 PARTIAL; L-12 PARTIAL; L-13 NOT_RUN; L-14 NOT_ASSESSED.
- External trust root NOT_ACTIVE; independent external review NOT_COMPLETED; overall Paper A NOT_VERIFIED.

The new shifted-matrix Hermitian and conditional Perron multiplicity declarations compile, but the positive top-eigenvector existence theorem and the spectral-shift transfer to the ground eigenvalue remain open.


## Mathlib irreducibility bridge — commit 5e8475fe7a90bc4e27158ba983c752900bd6e2df

- Lean workflow run \`44338374338\`: SUCCESS; 18,266 build jobs; axiom audit covered 154 declarations, all within \`propext\`, \`Classical.choice\`, and \`Quot.sound\`.
- Paper A evidence producer run \`44338374152\`: SUCCESS; Lean build and all four exact / high-precision diagnostic commands returned PASS.
- The Lean evidence manifest includes all five Paper A modules and the root \`ConstantLlapoy.lean\`.
- Claim traceability: 15/15 registry records located and hashed; semantic correspondence remains NOT_ESTABLISHED.
- Separate component provenance verifier run \`44339038580\`: SUCCESS for the exact producer artifact.
- 14-layer assessment: L-01 PARTIAL; L-02 BLOCKED; L-03 PARTIAL; L-04 PARTIAL; L-05 NOT_RUN; L-06 PARTIAL; L-07 PARTIAL; L-08 PARTIAL; L-09 PARTIAL; L-10 PARTIAL; L-11 PARTIAL; L-12 PARTIAL; L-13 NOT_RUN; L-14 NOT_ASSESSED.
- External trust root NOT_ACTIVE; independent external review NOT_COMPLETED; overall Paper A NOT_VERIFIED.

The new Mathlib irreducibility theorem closes the model-specific positive-support connectivity obligation. The strictly positive top-eigenvector existence theorem and spectral-shift transfer to the ground eigenvalue remain open.


## First full executable 14-layer Paper A trial — 2026-11-19

Exact mathematical/source revision under test: \`d58bcc55f156418959df11b6e36ccf2f9d3f988e\`.

### Execution and provenance evidence

- Lean workflow run \`44385358280\`: SUCCESS; \`lake build\` completed 18,266 jobs. The configured axiom audit covered 156 declarations and found only \`propext\`, \`Classical.choice\`, and \`Quot.sound\` within the configured allowlist.
- Paper A component producer run \`44385358261\`: SUCCESS. All seven required evidence components were generated and signed: Lean build, exact Dicke diagnostic, exact strong-coupling diagnostic, finite-difference diagnostic, weak-coupling numerical diagnostic, claim traceability, and the 14-layer trial plan.
- Separate Paper A component verifier run \`44385979037\`, final retried job \`135092142327\`: SUCCESS; final status \`PAPER_A_COMPONENT_EVIDENCE_PIPELINE_VERIFIED\` for the exact source revision. The first verifier attempt hit a transient GitHub API DNS timeout; the retry completed successfully.
- Meta-verification harness run \`44386128336\`: SUCCESS; 289 tests passed. The Paper A semantic-audit validator returned \`STRUCTURALLY_VALID_NOT_SEMANTICALLY_VERIFIED\`, with 15 claim records checked, 28 declaration references checked, and all five Lean module source bindings checked.
- Claim traceability: 15/15 registry records located and hashed. This does not establish semantic equivalence between manuscript claims and Lean declarations.

### Exact and numerical diagnostic observations

- Dicke-basis and independent finite-\(N\) strong-coupling diagnostics agree on the fourth-order coefficients for \(N=4,5,6\): \(1/648\), \(1/6144\), and \(1/20000\), respectively.
- The strong-coupling diagnostic's comparison rule was corrected to use the separate \(N=4\) endpoint coefficient rather than incorrectly applying the \(N\ge5\) expression at \(N=4\). A regression test now checks all three exact values and fails on mismatch.
- Finite-difference checks for \(N=4,5\) approach the displayed leading coefficients as \(h\) decreases over the tested values.
- Weak-coupling numerical checks for \(N=4,5\) approach the displayed leading coefficients as \(J/h\) decreases over the tested values.
- These are finite-\(N\), finite-sample execution results. They do not prove uniform-in-\(N\) asymptotics, global error bounds, or the full manuscript claims.

### Actual 14-layer assessment

| Layer | Result | Trial finding |
|---|---|---|
| L-01 | PARTIAL | Source records and preliminary prior-art screening exist; no exhaustive claim-specific novelty review. |
| L-02 | BLOCKED | No full direct manuscript-to-Lean semantic correspondence; 0/15 claims fully verified. |
| L-03 | PARTIAL | Claim obligations and known domain/scope issues are catalogued, but the complete claim-by-claim quantifier and boundary audit is not closed. |
| L-04 | PARTIAL | The selected Lean development builds and passes the configured axiom audit; 10 claims still lack direct formalization and THM-0002 still has open proof obligations. |
| L-05 | NOT_RUN | No independent second-prover proof route for Paper A. |
| L-06 | PARTIAL | Exact symbolic checks cover selected finite \(N\), not the general or asymptotic statements. |
| L-07 | PARTIAL | Two separately structured finite-\(N\) calculations agree on the tested coefficients; shared specification/runtime risks remain. |
| L-08 | PARTIAL | Signed attestations authenticate evidence bytes and origin, not theorem proof certificates or their mathematical meaning. |
| L-09 | PARTIAL | High-precision checks cover a small set of parameter values; no complete conditioning, error, or adversarial parameter analysis. |
| L-10 | PARTIAL | 15/15 source-linked claim records and exact artifact hashes are present; line-level semantic correspondence is unresolved. |
| L-11 | PARTIAL | Axiom and GitHub/Sigstore provenance checks pass; external trust-root activation and independent administration are absent. |
| L-12 | PARTIAL | Exact CI artifacts are reproducible for this run; independent external review is not completed. |
| L-13 | NOT_RUN | No claim-wide executable satisfiability/non-vacuity audit. A simple non-vacuity example for THM-0002 alone is not sufficient to pass this layer. |
| L-14 | NOT_ASSESSED | No concrete target system, measurement map, or empirical adequacy analysis has been established for the TFIM model. |

### Mathematical boundary and overall result

The new Hamiltonian encoding, shifted-matrix positivity, Boolean-hypercube connectivity, Mathlib irreducibility bridge, exact matrix-action identity, and eigenvector correspondence strengthen the formal model bridge for THM-0002. The following remain open:

1. Construct a strictly positive eigenvector at the top eigenvalue of the shifted matrix without assuming that eigenvector exists.
2. Complete the spectral/algebraic-multiplicity transfer from \(K=cI-H\) to the ground eigenvalue of \(H\).
3. Complete direct formalization and semantic correspondence for the other manuscript claims.

**Overall Paper A status: \`NOT_VERIFIED\`.** All seven evidence components are authenticated, but that is an evidence-integrity result, not a mathematical-proof verdict. External trust root remains \`NOT_ACTIVE\`; independent external review remains \`NOT_COMPLETED\`.


## Structural semantic-audit integrity is now part of the evidence bundle

The producer now executes `paper_a_semantic_audit_validator.py` against the 15 frozen claim records and five pinned Lean modules, records the command result and input hashes, attests the resulting evidence subject, and includes it in the separate verifier's eight-component authenticated bundle. The 14-layer plan records this structural result explicitly. A structural PASS does not change L-02: semantic equivalence, exact hypothesis correspondence, and claim-level mathematical proof remain BLOCKED / unverified.


## Follow-up execution: structural claim-to-Lean audit included in authenticated bundle

- Producer workflow run: `44401847581`, source commit `5d0d11f5685f96c673991e8f0b681dd8234eed6b` — SUCCESS.
- Separate component verifier run: `44402341599` — SUCCESS; final report `PAPER_A_COMPONENT_EVIDENCE_PIPELINE_VERIFIED`.
- Eight component subjects were produced, each separately attested and cryptographically authenticated by the verifier:
  1. `PAPER_A_LEAN_BUILD`
  2. `PAPER_A_DICKE_EXACT_DIAGNOSTIC`
  3. `PAPER_A_STRONG_COUPLING_EXACT_DIAGNOSTIC`
  4. `PAPER_A_FINITE_DIFFERENCE_DIAGNOSTIC`
  5. `PAPER_A_WEAK_COUPLING_NUMERICAL_DIAGNOSTIC`
  6. `PAPER_A_CLAIM_TRACEABILITY`
  7. `PAPER_A_SEMANTIC_AUDIT_INTEGRITY`
  8. `PAPER_A_14_LAYER_TRIAL_PLAN`
- The component aggregator returned `ACCEPTED`: no missing or duplicate components, digest mismatches, stale fields, pending/unverified evidence, unauthenticated provenance, or verified execution failures.
- The Lean project build returned exit code 0; the log records 18,266 build jobs and an axiom audit of 156 declarations, all within `[propext, Classical.choice, Quot.sound]`. This establishes the selected project build and configured axiom-audit result, not whole-paper formalization.
- All four configured finite-N / high-precision diagnostic commands returned exit code 0. They remain diagnostics, not proofs of asymptotic or uniform-in-`N` claims.
- Structural semantic-audit check: `STRUCTURALLY_VALID_NOT_SEMANTICALLY_VERIFIED`; 15 claim records and five Lean module blob bindings checked; 28 declaration references found; classifications recomputed as 10 `NO_DIRECT_FORMALIZATION`, 4 `PARTIAL_SUPPORT_ONLY`, and 1 `SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY`.
- **L-02 remains BLOCKED.** The structural checker confirms source hashes, claim registry completeness, declaration-name presence and classification counts only. It does not prove mathematical equivalence or exact hypothesis correspondence.
- The observed 14-layer statuses remain: L-01 PARTIAL; L-02 BLOCKED; L-03 PARTIAL; L-04 PARTIAL; L-05 NOT_RUN; L-06 PARTIAL; L-07 PARTIAL; L-08 PARTIAL; L-09 PARTIAL; L-10 PARTIAL; L-11 PARTIAL; L-12 PARTIAL; L-13 NOT_RUN; L-14 NOT_ASSESSED.
- Overall Paper A status remains `NOT_VERIFIED`. External trust root is `NOT_ACTIVE`; independent external review is `NOT_COMPLETED`. The current provenance-policy pin is checked out from the same repository and is not an independent trust anchor.

The separate meta-verification workflow policy's pinned workflow blob was also refreshed after a workflow-file revision mismatch. On commit `a3f1c7b4ac7f9e7059824270fec7f2d0a3707a59`, the harness and evidence-collection runs succeeded, the signed evidence verifier reported `VERIFIED`, and the live component-provenance smoke test reported `ACCEPTED`. This verifies that bounded meta-verification pipeline path on that commit; it does not activate external trust or prove Paper A.


## Verified eight-component Paper A evidence bundle — 2026-11-18

- Source commit: `1dbb5a282b1d62c2a2928585f6d08af1af42acb9`.
- Lean workflow run: `44414931670` — SUCCESS.
- Component evidence producer run: `44414931668` — SUCCESS.
- Separate component provenance verifier run: `44415434432` — SUCCESS.
- Verifier report artifact: `paper-a-component-verification-44414931668`, artifact ID `14480105102`.
- Producer evidence artifact: `paper-a-component-evidence-44414931668`, artifact ID `14478178116`.

The producer executed all eight required components successfully:
1. `PAPER_A_LEAN_BUILD`
2. `PAPER_A_DICKE_EXACT_DIAGNOSTIC`
3. `PAPER_A_STRONG_COUPLING_EXACT_DIAGNOSTIC`
4. `PAPER_A_FINITE_DIFFERENCE_DIAGNOSTIC`
5. `PAPER_A_WEAK_COUPLING_NUMERICAL_DIAGNOSTIC`
6. `PAPER_A_CLAIM_TRACEABILITY`
7. `PAPER_A_SEMANTIC_AUDIT_INTEGRITY`
8. `PAPER_A_14_LAYER_TRIAL_PLAN`

The separate verifier returned `PAPER_A_COMPONENT_EVIDENCE_PIPELINE_VERIFIED`; the component aggregation was `ACCEPTED`, with all eight subjects individually provenance-authenticated and no missing/duplicate components, digest mismatches, stale fields, unauthenticated receipts, or verified execution failures.

The Lean build completed 18,266 build jobs. The configured axiom audit checked 158 declarations and reported only the allowlisted axioms `propext`, `Classical.choice`, and `Quot.sound`. The structural semantic-audit integrity checker validated 15 frozen claim records, five Lean module blob bindings, and 28 declaration references; classifications were 10 `NO_DIRECT_FORMALIZATION`, 4 `PARTIAL_SUPPORT_ONLY`, and 1 `SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY`.

### 14-layer result for this exact source commit

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

**Overall Paper A status remains `NOT_VERIFIED`.** The `ACCEPTED` result is strictly about bundle policy, byte digests, and GitHub/Sigstore provenance. It does not verify any manuscript claim. L-02 remains blocked because source/hash/declaration-reference integrity is not semantic equivalence; L-04 remains partial because the current Lean development formalizes selected obligations rather than the full paper. External trust root remains `NOT_ACTIVE`, and independent external review remains `NOT_COMPLETED`.
