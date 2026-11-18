# Independent Trusted Builder Contract

**Status:** Normative integration contract; no external builder is provisioned or trusted yet.
**Version:** 1.0.0
**Applies to:** Constant Llpoy signed meta-verification evidence production.

## 1. Security objective

The trusted builder is a separately administered GitHub repository and reusable workflow that receives a narrowly defined evidence subject, validates its provenance inputs, and produces a signed SLSA provenance attestation. It MUST NOT treat the relying-party repository's workflow assertions as sufficient authorization.

The builder MUST be distinct from:
- relying party: `mytheeramet3dev-x/Constant-Llpoy` (repository ID `1460417275`);
- external trust-root authority (identity to be provisioned).

A builder repository name, repository ID, workflow path, and full immutable commit SHA are not yet known. No example identity in this document is an authorized identity.

## 2. Immutable identity and authorization

The trust-root-signed manifest MUST authorize all of:
- builder repository full name and numeric GitHub repository ID;
- reusable workflow path and full 40-character commit SHA;
- allowed caller repository ID and signer workflow identity;
- accepted subject schema and maximum subject size;
- OIDC issuer, SLSA predicate type, and allowed runner class;
- validity interval and monotonically increasing trust-root sequence.

The relying-party bootstrap MUST compare the manifest to protected Environment pins and query GitHub API repository metadata for the builder's actual repository ID. The caller MUST reference the reusable workflow with a literal full commit SHA. Branches, tags, mutable refs, `@main`, and dynamically supplied refs are prohibited.

## 3. Reusable workflow interface

The reusable workflow MUST expose only a minimal `workflow_call` interface:

| Input | Type | Requirement |
|---|---|---|
| `subject_path` | string | Relative path to one evidence file inside the checked-out caller workspace |
| `expected_subject_sha256` | string | 64 lowercase hexadecimal characters computed by the caller and independently recomputed by builder |
| `source_commit` | string | Full 40-character commit of the source evidence |
| `source_repository_id` | string | Exact caller repository ID; must equal the trust-root authorization |

No input may choose the signer identity, trust-root key, attestation predicate, OIDC issuer, or builder workflow revision. Those are fixed by the builder's immutable workflow and trust-root policy.

## 4. Mandatory builder behavior

The builder MUST:

1. Reject callers whose repository ID, workflow identity, ref, or source commit is not authorized by the trust-root policy.
2. Check out the authorized source commit without executing caller-controlled scripts.
3. Resolve `subject_path` beneath the checkout root; reject absolute paths, parent traversal, symlinks, non-regular files, and paths outside the checkout.
4. Recompute SHA-256 and compare it with `expected_subject_sha256`.
5. Enforce a documented maximum subject size and strict UTF-8/JSON schema for the evidence record.
6. Reject duplicate JSON keys, unknown schema versions, missing required evidence fields, stale run IDs, mismatched source revisions, and non-success upstream run states.
7. Construct provenance metadata itself; never accept caller-supplied provenance predicate JSON.
8. Use GitHub OIDC and a supported Sigstore-backed attestation mechanism to sign the exact subject digest.
9. Restrict permissions to the minimum needed; use `id-token: write`, attestation write, and read-only source access only in the signing job.
10. Deny self-hosted runners unless separately approved and pinned by the trust-root policy.
11. Emit a machine-readable report containing builder repository ID, workflow path, immutable workflow SHA, caller identity, source commit, subject digest, attestation identity, and verification result.
12. Fail closed on every missing, ambiguous, stale, malformed, or contradictory input.

The builder MUST NOT:
- run arbitrary scripts from the relying-party checkout;
- trust a digest supplied without recomputing it;
- allow the caller to override predicate type or signer identity;
- use a floating action or workflow reference;
- sign a subject when upstream evidence is rejected, skipped, cancelled, or incomplete;
- claim that signing proves the mathematical truth of the evidence payload.

## 5. Separate verifier requirements

The relying-party verifier MUST independently retrieve the attestation from GitHub's attestation service and verify:
- subject digest against the exact downloaded subject bytes;
- OIDC issuer and certificate chain;
- builder repository ID, workflow path, and immutable workflow digest;
- authorized caller/source identity and source commit;
- SLSA provenance predicate type;
- trust-root manifest signature, digest, sequence, and validity interval;
- timestamps and transparency evidence where provided.

The verifier MUST NOT trust a report generated only by the builder. It must independently evaluate the attestation and compare every identity to the externally pinned policy.

## 6. Required conformance tests

Before activation, the builder MUST demonstrate rejection of:
- unauthorized repository ID and unauthorized workflow;
- mutable workflow ref or wrong builder commit;
- caller-supplied predicate or signer override;
- subject digest mismatch and subject substitution;
- path traversal, absolute path, symlink, and non-regular file;
- duplicate JSON keys, unknown fields, malformed UTF-8, oversized subject;
- stale, failed, cancelled, skipped, or incomplete upstream run;
- replayed evidence from a different run or source commit;
- expired or wrong-sequence trust-root policy;
- untrusted runner class and missing OIDC identity.

Positive tests MUST verify one complete, independently verifiable attestation for a known-answer subject. Tests must be run from a reviewer-controlled workflow or independently reproduced; builder self-tests alone are insufficient.

## 7. Activation gate

The builder is **NOT ACTIVE** until all are true:

- [ ] A separately administered builder repository exists.
- [ ] Its immutable repository ID, workflow path, and commit SHA are known.
- [ ] A separate trust-root authority signs those exact identities.
- [ ] The relying-party Environment pins the trust-root commit and manifest/key digests.
- [ ] The builder implements this contract and passes the conformance suite.
- [ ] The caller workflow references the exact reusable workflow commit.
- [ ] A separate verifier validates a real attestation from that builder.
- [ ] An independent reviewer examines the trust boundary and evidence.

Until then, the existing in-repository producer remains the current bounded implementation. It MUST NOT be described as independently built or independently governed.


### Current local conformance implementation (not an activation substitute)

The in-repository black-box suite at `test_trusted_builder_conformance.py` provides known-answer and negative vectors for the local reference CLI. It is a reusable starting point for a future external builder's reviewer-controlled conformance adaptation, but passing it in this repository does not satisfy the independent-review requirement above. The external builder must independently authenticate caller identity and upstream run metadata, bind to the external trust-root manifest, create a real attestation, and pass separate signature verification. The current reference intentionally does none of those things.
