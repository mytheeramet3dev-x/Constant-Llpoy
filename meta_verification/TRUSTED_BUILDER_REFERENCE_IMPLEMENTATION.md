# Local Trusted-Builder Reference Implementation

**Status: IMPLEMENTED AS A NON-TRUSTED TEST REFERENCE ONLY. NOT AN EXTERNAL BUILDER.**

## Purpose

`trusted_builder_reference.py` implements a deterministic, fail-closed subset of the
Trusted Builder Contract so that path handling, subject integrity, caller metadata,
upstream-run metadata, and evidence-record validation can be adversarially tested
before an independently administered builder repository exists.

It is intentionally incapable of signing. It does not request GitHub OIDC tokens,
use Sigstore, create SLSA attestations, contact GitHub, or establish trust.

## Accepted evidence

The reference accepts only the exact schema-v1 normalized record emitted by
`github_run_collector.py`. It checks:
- exact field set and schema version;
- repository, run ID, and source commit binding;
- `ACCEPTED` status, successful workflow conclusion, empty failure list;
- full Git object IDs and the collector record's canonical SHA-256;
- strict UTF-8 JSON with duplicate-key rejection;
- exact subject byte digest and configured size limit;
- relative canonical path, no traversal, no symlink components, regular file only;
- caller repository ID, workflow identity, and ref against explicit expected values;
- upstream run ID, completion/conclusion, repository ID, workflow, ref, and source commit.

The caller and upstream metadata are passed as arguments in this local harness. They are
not independently authenticated. The reference therefore tests validation logic only;
it does not establish the authenticity of those metadata.

## Run tests

```sh
python -m unittest discover -s meta_verification -p 'test_trusted_builder_reference.py' -v
```

Run the full suite with:

```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```

## Output semantics

A successful validation returns `VALIDATED_LOCAL_UNTRUSTED` with
`signing_performed=false`, `attestation_created=false`, and
`trust_established=false`. This is deliberately incompatible with a signed-builder
success claim. It must never be translated into `SIGNED` or used as an attestation.

## Not implemented

- external repository or separate administration;
- independent authentication of caller/upstream metadata;
- trusted-root manifest retrieval and enforcement inside an external builder;
- OIDC identity issuance or validation;
- provenance predicate construction;
- Sigstore attestation production;
- independent attestation verification;
- replay protection backed by durable external state;
- independently governed conformance execution.

The external activation gate in `TRUSTED_BUILDER_CONTRACT.md` remains unchanged.
