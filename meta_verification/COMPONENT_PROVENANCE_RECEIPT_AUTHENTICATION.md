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
- No real component-evidence bundle with per-component attestations has been authenticated end to end.
- The provenance-policy SHA-256 pin must be supplied from a separately administered protected source; the relying repository does not provide an independent pin merely by storing a JSON policy file.
- The external authority/activation pins and trusted-time source remain unprovisioned.
- GitHub CLI is version-pinned, but its binary/runtime is runner-provided and not independently installed from a pinned binary digest.
- Repository administrators who can alter the relying repository's workflows and policies remain inside the trust boundary.

A green test suite proves only that the declared tests ran and passed on the named revision. It does not activate external trust, verify real component attestations, or prove mathematical claims.
