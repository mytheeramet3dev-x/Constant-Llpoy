# Component Provenance Receipt Authentication

**Status:** Implemented prototype; production activation is NOT ACTIVE  
**Version:** 0.1.0  
**Scope:** Authentication of exact component evidence bytes and their provenance receipts before bundle aggregation

## 1. Assurance claim and boundary

A component receipt is not trusted because its JSON says `VERIFIED`, because its SHA-256 field is self-consistent, or because a run ID is present. The production CLI MUST verify a GitHub/Sigstore SLSA provenance attestation for the exact bytes embedded in each required component.

The verifier MUST bind:
- exact component evidence bytes and their SHA-256 digest;
- exact source commit;
- repository numeric identity and repository name;
- signer workflow identity and source ref;
- GitHub Actions OIDC issuer and SLSA provenance v1 predicate;
- verified transparency-log/timestamp evidence;
- the unique attestation subject digest; and
- the GitHub workflow invocation ID, including both run ID and run attempt.

This is provenance authentication, not proof that the evidence content is mathematically correct, complete, relevant, or sound.

## 2. Receipt schema 2.0

Each component's `provenance` object has exactly these fields:

| Field | Meaning |
|---|---|
| `receipt_schema_version` | Exact value `2.0` |
| `subject_sha256` | SHA-256 of the exact decoded `evidence_base64` bytes |
| `source_commit` | Expected source Git commit |
| `attestation_run_id` | Positive integer GitHub Actions run ID that produced the attestation |
| `attestation_run_attempt` | Positive integer run attempt; prevents confusing reruns with the original attempt |
| `attestation_workflow_revision` | Immutable 40-character source/workflow commit SHA |

Legacy fields such as a caller-provided `status: VERIFIED`, `verifier_run_id`, or `verifier_revision` are not part of schema 2.0 and MUST be rejected as unknown fields. Run ID and attempt are bound to SLSA `predicate.runDetails.metadata.invocationId`, expected in GitHub's form:

`https://github.com/OWNER/REPOSITORY/actions/runs/RUN_ID/attempts/RUN_ATTEMPT`

The invocation identifier is checked against the receipt; it is not inferred from a caller's status field.

## 3. Direct authentication procedure

`component_provenance_authenticator.py`:
1. validates the exact aggregation policy and complete, unique required component set;
2. verifies the raw provenance-policy bytes against a separately supplied SHA-256 pin;
3. verifies that the parsed provenance-policy object equals the exact pinned bytes;
4. validates each receipt's schema, source commit, workflow revision, run ID and attempt;
5. decodes each component's exact evidence bytes and recomputes SHA-256;
6. invokes the pinned-version GitHub CLI `gh attestation verify` on those exact bytes, with explicit repository, signer-workflow, OIDC issuer, predicate type, source ref, source digest, signer digest, and self-hosted-runner denial constraints;
7. independently checks the returned certificate identity, verified timestamps, SLSA predicate type, unique subject digest, and exact SLSA invocation ID; and
8. returns an in-memory authenticated record for each component.

The authenticated map is not read from JSON, an uploaded report, or a caller-supplied `VERIFIED` value. The CLI builds it directly from the verifier's result and immediately passes it to the existing aggregator.

## 4. Aggregation semantics

- `status_aggregator.py`'s standalone CLI supplies no authenticated map; it therefore cannot return `ACCEPTED` from structural JSON alone.
- Missing authentication, a missing attestation, invalid signature/certificate, wrong signer, wrong source, wrong subject, wrong invocation ID, stale run attempt, or a provenance-policy pin mismatch fails closed.
- The production path is `policy_activation_gate.py`, which requires the authority-set pin, active-policy pin, provenance-policy pin, and trusted epoch time, authenticates every required component, and only then invokes aggregation.
- The success status is `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`. It is not theorem acceptance and does not claim the evidence itself is mathematically valid.
- The in-memory map is an internal API convention, not a Python sandbox. Arbitrary code importing the function can fabricate Python objects. The supported trust boundary is the production CLI path, not arbitrary direct invocation of the Python function.

## 5. Tests and mutation adequacy

The tests use controlled fake GitHub CLI output to test parsing, policy enforcement, exact subject binding, certificate identity, run-attempt binding, and fail-closed behavior. These fixtures are not real signatures and do not establish that a component artifact has a live GitHub attestation.

The selected mutation suite deliberately weakens policy-pin checking, evidence digest checking, run ID/attempt validation, workflow revision binding, GitHub CLI failure handling, SLSA invocation-ID binding, subject-digest matching, and the aggregator's authentication requirement. The mutation score is limited to the exact selected mutants and is not exhaustive.

## 6. Non-activation and residual trust

The following remain explicitly NOT ACTIVE / NOT ESTABLISHED:
- No current component-evidence producer workflow emits a separate attestation for every component artifact. The existing evidence producer attests `github-run-evidence.json`; that does not automatically attest arbitrary component subjects.
- One real one-component smoke bundle for the collector's `github-run-evidence.json` has been authenticated end to end (see Section 9). No Paper A, Lean-module, numerical-diagnostic, or other mathematical component artifact has yet been authenticated.
- The provenance-policy SHA-256 pin must be supplied from a separately administered protected source; the relying repository does not provide an independent pin merely by storing a JSON policy file.
- The external authority/activation pins and trusted-time source remain unprovisioned.
- GitHub CLI is version-pinned, but its binary/runtime is runner-provided and not independently installed from a pinned binary digest.
- Repository administrators who can alter the relying repository's workflows and policies remain inside the trust boundary.

A green test suite proves only that the declared tests ran and passed on the named revision. The live smoke test below validates one real collector-evidence attestation path; it does not activate external trust, authenticate every mathematical component, or prove mathematical claims.


## 7. Observed CI validation

On commit `e8da7e8923440716a1b1dbf85c6f2c7b0408c9dc`, full harness run [44238894962](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238894962) passed 263 tests in 28.235 seconds. Selected mutation results: component provenance 10/10, aggregator 12/12, policy activation 9/9. Producer [44238972702](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238972702) and separate verifier [44239010485](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44239010485) succeeded; the verified attestation is for `github-run-evidence.json`, not for individual component evidence. This is bounded CI evidence, not live per-component attestation validation.


## 8. Live GitHub attestation integration smoke test

A separate workflow, `.github/workflows/component-provenance-live-smoke.yml`, exercises the authenticator against a real GitHub/Sigstore attestation rather than a fake CLI fixture. It runs only after the existing evidence-collection producer workflow completes successfully. It downloads the exact evidence artifact from that producer run, checks out the producer's exact source revision, and invokes the direct authenticator through `component_provenance_live_smoke.py`.

The smoke adapter constructs a one-component bundle for the exact downloaded `github-run-evidence.json` bytes. Its receipt binds the producer workflow run ID, run attempt, and source revision. The direct authenticator must verify the actual attestation and its SLSA invocation ID; the normal aggregator must then accept the one-component smoke bundle. The workflow uploads a report only after that sequence succeeds.

**Interpretation boundary:** this demonstrates that the current GitHub CLI / Sigstore integration can authenticate one real subject emitted by the existing producer. It does not create attestations for Paper A, Lean modules, numerical diagnostics, or every future component. It also does not activate the external authority, active-policy, or provenance-policy trust roots. The smoke workflow computes the policy digest from the checked-out policy file; this is deliberately a local integration-test pin, not an independently governed production pin. Its final status is `LIVE_COMPONENT_PROVENANCE_SMOKE_VERIFIED`, never a theorem status.


## 9. Observed live attestation integration result

On signer source commit `7d5f778e9cd05cd1ef1095dd23f139d83aba8248`:
- Harness run [44240363793](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240363793) passed 267 tests in 22.096 seconds.
- The selected component-provenance, aggregator, and activation mutation suites killed 10/10, 12/12, and 9/9 mutants, respectively.
- Evidence producer run [44240436570](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240436570) succeeded and signed the exact collector evidence subject.
- Separate provenance verifier run [44240468328](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240468328) succeeded and reported `VERIFIED` for subject SHA-256 `b2cbc1a74afc06e47ba9b0cba2feee31aca9fb59f459562338329ce5964119aa`.
- Live component-provenance smoke run [44240468560](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44240468560) succeeded. It downloaded the exact artifact from producer run `44240436570`, passed the actual GitHub/Sigstore attestation through the component authenticator, checked run ID `44240436570` / attempt `1`, and obtained aggregator status `ACCEPTED`. The smoke report states `production_activation=NOT_ACTIVE` and `mathematical_correctness=NOT_ASSESSED`.

This is the first observed real-signature end-to-end exercise of the component authenticator. It is limited to one collector evidence subject and a locally computed smoke-test policy digest. It is not independent external policy governance, a production component producer, or a theorem-verification result.
