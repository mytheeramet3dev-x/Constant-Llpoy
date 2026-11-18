# External Trust Root and Trusted Builder Bootstrap

## Status

The external trust-root verifier and a manually dispatched bootstrap workflow are implemented. **External trust-root activation is not complete.** No independent trust-root repository, signing key, protected GitHub Environment, or external trusted-builder repository has been provisioned or independently inspected in this repository.

The workflow deliberately fails closed until all required protected Environment variables are configured. Do not replace missing values with placeholders or repository-local defaults.

## Separation model

Three distinct repositories are required:

1. **Relying party:** `mytheeramet3dev-x/Constant-Llpoy` (repository ID `1460417275`).
2. **Trust-root authority:** an independently administered repository holding a signed policy manifest and public Ed25519 key. It must not be the relying-party repository.
3. **Trusted builder:** a separately administered repository holding the reusable build/signing workflow. It must be distinct from both the relying party and trust-root authority.

The trust-root private key MUST be held outside Git (preferably offline or in an HSM). Only the public key, signed manifest, and detached signature belong in the trust-root repository. The public-key SHA-256 fingerprint and exact trust-root commit are pinned in a protected Environment in the relying-party repository.

The trust-root authority must independently review and authorize:
- exact relying-party repository ID;
- exact signer workflow identity, source ref, and source commit;
- exact trusted-builder repository ID, workflow path, and immutable commit;
- OIDC issuer and SLSA predicate type;
- manifest validity interval and monotonically increasing sequence.

The manifest sequence is informational unless a protected Environment update advances the pinned manifest digest and trust-root commit. The bootstrap workflow does not silently accept a newer root revision.

## Required GitHub Environment

Create an Environment named `meta-trust-root` in the relying-party repository. Configure required reviewers who are independent of the producer/workflow authors, and prevent self-review where the platform permits. Environment protection is an operational prerequisite; this code cannot create or attest to that setting.

Configure these Environment **variables** (not values committed to this repository):

| Variable | Required value |
|---|---|
| `TRUST_ROOT_REPOSITORY` | External trust-root repository in `owner/name` form |
| `TRUST_ROOT_REPOSITORY_ID` | Numeric immutable GitHub repository ID |
| `TRUST_ROOT_COMMIT` | Full 40-character commit SHA containing the root package |
| `TRUST_ROOT_MANIFEST_PATH` | Relative path to signed JSON manifest |
| `TRUST_ROOT_SIGNATURE_PATH` | Relative path to detached Ed25519 signature |
| `TRUST_ROOT_PUBLIC_KEY_PATH` | Relative path to PEM public key |
| `TRUST_ROOT_MANIFEST_SHA256` | SHA-256 of the exact manifest bytes |
| `TRUST_ROOT_PUBLIC_KEY_SHA256` | SHA-256 fingerprint of the exact PEM public-key bytes |
| `AUTHORIZED_SIGNER_COMMIT` | Full commit SHA authorized to sign for the current relying-party signer workflow |
| `TRUSTED_BUILDER_REPOSITORY` | Separate external builder repository |
| `TRUSTED_BUILDER_REPOSITORY_ID` | Numeric builder repository ID |
| `TRUSTED_BUILDER_WORKFLOW` | Exact reusable workflow identity/path |
| `TRUSTED_BUILDER_COMMIT` | Full immutable commit SHA of the builder workflow |

For a private trust-root repository, add an environment secret `TRUST_ROOT_READ_TOKEN` with read-only access to the trust-root repository and, if private, the trusted-builder repository as well. The same token is used for the checkout and GitHub API repository-ID checks. Public repositories can be read through the workflow token.

The Environment's required reviewers and variable values are part of the trust boundary. A repository administrator who can change the workflow, Environment protection, and pins remains privileged; protect workflow changes with independently administered branch/ruleset controls.

## Manifest schema

The signed UTF-8 JSON manifest has exactly these fields:

```json
{
  "schema_version": "1.0",
  "trust_root_id": "organization-defined-stable-id",
  "sequence": 1,
  "issued_at": "2026-11-17T00:00:00Z",
  "expires_at": "2027-11-17T00:00:00Z",
  "relying_party": {
    "repository": "mytheeramet3dev-x/Constant-Llpoy",
    "repository_id": 1460417275
  },
  "authorized_signer": {
    "workflow": "mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml",
    "source_ref": "refs/heads/main",
    "oidc_issuer": "https://token.actions.githubusercontent.com",
    "predicate_type": "https://slsa.dev/provenance/v1",
    "commit": "FULL_40_CHARACTER_COMMIT_SHA"
  },
  "trusted_builder": {
    "repository": "independent-build/constant-llpoy-builder",
    "repository_id": 2880000002,
    "workflow": "independent-build/constant-llpoy-builder/.github/workflows/trusted-builder.yml",
    "commit": "FULL_40_CHARACTER_BUILDER_COMMIT"
  }
}
```

The example builder identity is illustrative only and MUST NOT be copied as if it were real. The external authority must substitute actual independently governed repository IDs and commits.

## Signing the root manifest

Generate an Ed25519 keypair in a controlled environment, not in GitHub Actions and not inside either application repository:

```sh
openssl genpkey -algorithm ED25519 -out trust-root-private.pem
openssl pkey -in trust-root-private.pem -pubout -out trust-root.pub
openssl pkeyutl -sign -inkey trust-root-private.pem -rawin \
  -in trust-root.json -out trust-root.sig
sha256sum trust-root.json trust-root.pub
```

The private key MUST NOT be uploaded. The detached signature is verified over the exact manifest bytes. The public-key fingerprint and manifest digest must be provisioned independently in the protected Environment. Do not obtain the expected fingerprint from the same trust-root checkout being verified.

## Running the bootstrap

After the external trust-root repository and builder exist, the manifest is signed, and the protected Environment is configured, dispatch:

`Actions → External trust-root bootstrap verification → Run workflow`

The workflow checks:
- exact external repository remote and immutable checkout commit;
- exact manifest and public-key SHA-256 pins;
- Ed25519 signature using OpenSSL;
- duplicate JSON keys and strict manifest schema;
- relying-party repository name and numeric ID;
- authorized signer workflow, source ref, issuer, predicate, and exact commit;
- trusted-builder repository identity, workflow, and immutable commit;
- manifest validity window.

A successful result is only `TRUST_ROOT_POLICY_VALID`. It proves that the checked manifest was signed by the key whose fingerprint was pinned through the protected Environment and that its policy matches the declared identities. It does **not** prove the builder is already used by the current evidence producer.

## Trusted-builder activation remains a separate gate

The current evidence producer still invokes `actions/attest` in the relying-party repository. The manifest's trusted-builder identity is currently an authorization contract, not an active signing route. Do not report the system as using an independent trusted builder until:
1. the external builder repository exists and is independently administered;
2. its reusable workflow is pinned by full commit SHA;
3. the producer delegates the attestation/build operation to that reusable workflow;
4. the resulting certificate identifies the authorized builder workflow;
5. the relying-party verifier checks the builder identity against the external trust-root manifest;
6. positive, wrong-builder, stale-builder, modified-subject, and replay tests pass end-to-end.

No independent trust root or trusted builder is considered active before these gates pass.


## Normative trusted-builder contract

The builder interface, mandatory validation behavior, separate-verifier requirements, conformance tests, and activation gates are defined in [`TRUSTED_BUILDER_CONTRACT.md`](TRUSTED_BUILDER_CONTRACT.md). The machine-readable report shape is [`trusted_builder_report.schema.json`](trusted_builder_report.schema.json).

The contract is intentionally not implemented as a local reusable workflow: a workflow in this relying-party repository would remain under the same repository administration boundary and would not establish an independent builder. GitHub reusable workflow references must be committed with the real external repository and full immutable workflow commit after that identity is provisioned and authorized by the signed trust-root manifest.


## Local reference implementation status

A non-signing reference validator is implemented at `meta_verification/trusted_builder_reference.py`. It is deliberately confined to the relying-party repository and therefore provides no administrative or cryptographic independence. It checks safe subject path resolution, no symlink components, regular-file and size requirements, strict UTF-8 JSON with duplicate-key rejection, subject SHA-256, collector-record schema/digest, caller identity fields, and completed successful upstream run metadata. The local test harness supplies caller/upstream metadata, so these checks validate logic but do not authenticate the metadata source.

The only success state is `VALIDATED_LOCAL_UNTRUSTED`; signing, attestation, and trust flags remain false. See [the implementation note](TRUSTED_BUILDER_REFERENCE_IMPLEMENTATION.md). External trust-root and trusted-builder activation gates remain unchanged and unsatisfied.
