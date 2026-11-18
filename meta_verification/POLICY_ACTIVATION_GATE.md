# Policy activation gate — end-to-end integration

**Status:** Implemented prototype; external activation is not provisioned or operational.
**Scope:** Bind the existing structural component aggregator to an independently pinned active-policy record.

## Why this exists

The existing `status_aggregator.py` is a structural bundle evaluator. Its `ACCEPTED` result means only that a supplied bundle matches the supplied structural policy. The existing `policy_change_control.py` verifies threshold signatures on a proposed policy change, but correctly reports that authorization is not activation.

This integration adds `policy_activation_gate.py`. It requires both:
1. an authority-set SHA-256 supplied as an external pin; and
2. an active-policy record SHA-256 supplied as a separate external pin.

The record must bind the exact policy bytes, policy ID, monotonic sequence, authority-set digest, ACTIVE state, validity interval, and threshold signatures from distinct Ed25519 reviewers. Only after this check does the gate invoke the existing structural aggregator.

## Status semantics

- `POLICY_CHANGE_AUTHORIZED`: proposal signatures are valid. This is not activation.
- `POLICY_ACTIVE`: the active record matches both external pins and its signatures, sequence, policy digest, and validity interval verify.
- `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`: active-policy gate passed and every required component's exact evidence bytes passed direct GitHub/Sigstore attestation verification before aggregation. This still does not prove mathematical correctness.
- `REJECTED`, `INCONCLUSIVE`, or `ERROR`: underlying non-acceptance is preserved; activation cannot upgrade component evidence.

The integration deliberately does not emit the bare status `ACCEPTED` as its final result. It is not a theorem-verification decision and must not be described as one.

## Trust and activation boundary

The expected authority-set digest and active-record digest are parameters intended to be supplied by a protected, separately administered source (for example, a protected deployment environment backed by an external policy repository). If the relying repository controls both the bytes and their expected digests, the boundary collapses. Therefore this prototype does not claim independent trust.

No external authority repository, private reviewer key custody, protected Environment reviewers, active-policy pin, or external builder is provisioned or verified. No production workflow currently invokes this gate. The module is a tested integration component, not an activated production gate.

The current implementation checks the active record's Ed25519 threshold against the pinned authority set. Revocation is represented by publishing a new authority-set revision with revoked keys removed and advancing the externally pinned authority digest. Rollback resistance depends on the external source advancing the expected sequence and active-record digest; a caller that can roll back both external pins defeats this property.

The gate CLI now requires a third external pin for the exact provenance-policy bytes and calls `component_provenance_authenticator.py` for every required component before aggregation. It checks repository identity, source ref/commit, signer commit, timestamp evidence, SLSA predicate, unique subject digest, and the signed invocation ID bound to the receipt run ID/attempt. The external OpenSSL executable/runtime for policy activation remains in the verifier trust boundary and is not independently pinned here.

## Test coverage

`test_policy_activation_gate.py` covers valid active policy, authorized-but-not-active rejection, missing/mismatched external pins, policy digest tampering, wrong policy identity, sequence rollback/replay, expiry, authority binding, insufficient/invalid signatures, preservation of non-accepted component results, existing policy-revision/commit binding, order invariance, and duplicate component handling.

Run with:

```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```

Passing these tests demonstrates only the listed local test cases. It does not establish independent administration, production activation, complete mutation adequacy, or mathematical correctness.


## Mutation adequacy (selected set)

`test_policy_activation_mutations.py` applies nine controlled weakenings to the activation gate in isolated temporary copies and requires the adversarial gate suite to fail through assertions. The selected mutants cover authority pin, activation pin, ACTIVE-state distinction, sequence binding, policy digest, exact policy-object/bytes binding, expiry, threshold, and Ed25519 signature verification. The score is bounded to these nine authored mutants and is not complete mutation coverage or evidence of independent external governance.


## Observed validation record

On commit `b09293fc018144d43829c3a1b6b2dbbed93beef8`, the full harness run [44235070461](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235070461) passed 239 tests in 16.004 seconds. The activation-gate mutation suite killed all 9/9 selected mutants through assertion-driven failures. Evidence producer run [44235147267](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235147267) succeeded; separate provenance verifier run [44235183026](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44235183026) reported `VERIFIED` for that exact source commit and one attestation (subject SHA-256 `1735f3a778ebf7f7fe16ca1980fbcdd01f46d4c028a8c63232d6a7c86ed71902`). These are repository CI observations for the named revision, not independent governance or mathematical proof validation.


## Executable CLI contract

The gate now has a fail-closed CLI entry point. It requires explicit paths for the exact policy, authority-set, active-record, and component-bundle bytes, plus explicit expected commit, authority digest, active-record digest, provenance-policy digest, policy ID, sequence, and epoch time. There are no default pins and no fallback to repository-local policy values. Input files must be regular non-symlink files and are size-bounded; policy, authority, activation, and bundle JSON are parsed with duplicate-key rejection. A missing/malformed external pin or invalid activation returns `ERROR` and a nonzero exit. A structurally non-accepted bundle is not upgraded by activation.

The CLI does not itself establish that command-line pins or time are trustworthy. A production caller must inject them from protected, separately administered controls and a trusted time source. Supplying these values from the same mutable checkout or an unprotected workflow input does not satisfy the external trust requirement. The repository workflow runs adversarial tests only; it intentionally does not invoke the gate as a production decision.


## Component provenance authentication integration

The gate CLI now requires `--provenance-policy` and `--expected-provenance-policy-sha256` in addition to the authority and activation pins. It calls `component_provenance_authenticator.py` on every required component's exact evidence bytes before invoking the aggregator. The authenticator verifies the GitHub/Sigstore attestation, repository ID, source ref/commit, signer workflow/commit, verified timestamps, SLSA v1 predicate, exact subject digest, and `runDetails.metadata.invocationId` against the receipt's attestation run ID and attempt.

Receipt schema 2.0 contains no caller-supplied `status: VERIFIED`. It contains only subject digest, source commit, attestation run ID/attempt, and attestation workflow revision. The final status is `POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED`; it is not theorem acceptance.

The authenticator's tests use fake GitHub CLI output. No live component artifact has been authenticated, and the current evidence producer signs only `github-run-evidence.json`, not every component artifact. The external provenance-policy pin and the external authority pins remain unprovisioned. Therefore the integration is implemented and testable but NOT ACTIVE for production decisions.


## Validation for the component-provenance integration

Commit `e8da7e8923440716a1b1dbf85c6f2c7b0408c9dc` passed 263 tests in harness run [44238894962](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238894962). Selected mutation suites killed 10/10 component-provenance, 12/12 aggregator, and 9/9 activation mutants. Producer [44238972702](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44238972702) and verifier [44239010485](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44239010485) succeeded. The verified provenance subject remains the collector evidence JSON; no real per-component artifact attestation has been produced or verified. Production activation remains NOT ACTIVE.
