# Policy Authority and Change Control

## Status

Implemented as a verification prototype; NOT ACTIVATED as the production policy authority. No independent authority set, reviewer keys, external digest pin, protected Environment, or external policy repository has been provisioned or independently confirmed.

## Separation of duties

- Policy Author: proposes changes and supplies rationale; cannot self-authorize.
- Independent Reviewers: inspect the policy diff, threat model, compatibility, tests and mutation evidence; sign the exact proposal metadata.
- Policy Authority: governs the reviewer roster, threshold, key revocation, sequence and external policy pin. It must be outside the relying repository's sole administrative control.
- Policy Evaluator: verifies the externally pinned authority-set digest, signatures, parent chain, sequence and expiry; cannot edit policy.
- Status Aggregator: evaluates evidence under an authorized policy; cannot change the policy or upgrade component states.

## Approval and change rules

- Default approval threshold is 2-of-3 distinct Ed25519 reviewers.
- The reviewer roster and threshold are themselves trust-root material. Their exact canonical bytes must be pinned out-of-band; an in-repository copy cannot authorize itself.
- Each proposal binds policy ID, monotonically increasing sequence, parent policy SHA-256, exact new policy SHA-256, issue/expiry times and detached reviewer signatures.
- Signatures cover canonical proposal metadata including the exact policy digest. Duplicate, unknown, unauthorized or invalid signatures fail closed.
- The next sequence and exact parent digest are required. This rejects rollback, fork and replay.
- A valid signature threshold does not activate a policy. The external authority must separately update the protected policy pin and reviewer controls.
- Reviewer rotation/revocation requires a new externally authorized authority-set digest. Repository-local edits cannot remove or add trusted reviewers.
- Editorial changes require one independent review; schema/required-evidence changes and status-semantic changes require two-of-three approval plus adversarial tests; trust-root, reviewer, signer, builder or cryptographic changes require a separate external authority ceremony.
- Any reduction in required evidence, weakening of rejection, broader signer identity, or acceptance of INCONCLUSIVE/NOT_RUN is security-sensitive.

## Activation lifecycle

1. Author proposes exact policy bytes and digest.
2. Proposal names current parent digest and next sequence.
3. Reviewers inspect the change and sign the canonical proposal metadata.
4. The verifier checks signatures against an externally pinned authority set.
5. Policy authority independently approves and publishes the new digest/sequence pin using protected controls.
6. The evaluator confirms policy change authorization.
7. Activation occurs only after external pin update and protected reviewer approval.
8. Historical evidence remains bound to the policy digest under which it was evaluated. Re-evaluation creates a new result; no silent retroactive reinterpretation.

## Revocation and rollback

Revocation is forward-only: issue a new authority-set revision and increment sequence. Emergency suspension may disable acceptance but cannot convert failed or incomplete evidence into acceptance. Rollback to old policy bytes requires a new forward sequence referencing the currently active parent and explicit re-authorization. Expired proposals and authority manifests cannot authorize changes. Suspected key compromise requires a new externally pinned reviewer set.

## Verifier implementation and limitations

- policy_change_control.py validates the external authority-set SHA-256 pin supplied to the invocation, strict JSON, distinct reviewer IDs, Ed25519 key type, threshold, exact policy digest, policy ID, parent digest, next sequence, validity interval and cryptographic signatures.
- It uses the OpenSSL CLI; the executable/runtime remains part of the trust boundary and is not independently pinned by this prototype.
- test_policy_change_control.py generates ephemeral keys and tests positive 2-of-3 authorization and negative threshold, unauthorized/duplicate reviewer, bad signature, altered policy, authority pin mismatch, wrong parent/sequence, expiry, malformed JSON and unknown fields.
- The authority-set digest is an external argument. The tool does not establish its own trust root. A caller controlling both authority bytes and expected digest can defeat the boundary.
- No real human reviewer identity or organizational independence has been established.
- No external policy repository/private key custody or protected Environment/ruleset has been provisioned or independently inspected.
- No production workflow consumes this verifier.
- This does not establish mathematical correctness or theorem acceptance.


## Validation record

The full meta-verification harness run [44233157563](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233157563) passed 219 tests. The policy-change mutation suite killed all 8/8 selected mutants through assertion-driven failures. Evidence producer run [44233215756](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233215756) succeeded, and separate verifier run [44233252327](https://github.com/mytheeramet3dev-x/Constant-Llpoy/actions/runs/44233252327) reported VERIFIED for source commit 56f4ac5678ab5dc1225075fa242e442f2601da57 and one attestation. This authenticates the evidence artifact's origin/integrity within the configured GitHub/Sigstore trust model; it does not establish an independent policy authority or validate the truth of every assertion in the artifact.
