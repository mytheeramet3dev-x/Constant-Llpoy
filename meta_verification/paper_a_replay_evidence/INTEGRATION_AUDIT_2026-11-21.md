# Paper A Replay Evidence Intake — Integration Audit & Boundary

Date: 2026-11-21
Status: Repository source audit and utility import completed; runtime tests NOT RUN.

## Repository boundary

Paper A (`Absolute_Sym`) is the evidence producer: replay generation, numerical outputs, manifests, input/output records, and claim-specific artifacts. Constant Llpoy is the independent verification and certification infrastructure. Producer-produced PASS labels are untrusted claims, not certification decisions.

## Source audit

Constant Llpoy already contains Paper A evidence workflows and meta-verification components:
- `meta_verification/paper_a_component_pipeline.py`
- `meta_verification/paper_a_semantic_audit_validator.py`
- `.github/workflows/paper-a-component-evidence.yml`
- `.github/workflows/paper-a-component-evidence-verify.yml`

These existing workflows produce and verify component evidence/provenance. The newly imported replay-manifest intake package is **not yet connected** to these workflows, and no workflow dispatch/test run was available in this review.

## Migration decision

Copied nine portable files, byte-for-byte (source and destination Git blob SHAs match), into `Constant-Llpoy/meta_verification/paper_a_replay_evidence/`:
1. replay manifest structural/semantic validator
2. path-safety utility
3. validator regression tests
4. path-safety adversarial tests
5. schema consistency tests
6. manifest JSON schema
7. signature design JSON
8. threat-model JSON
9. evidence-retention policy JSON

The producer-side manifest generator remains in Paper A. It was not copied, because the verifier should independently validate evidence rather than become a second evidence producer.

## Integration blockers and caution

- Validator's `--verify-files` option directly hashes paths and does not enforce workspace containment. It must not be used as the only safe file-intake gate.
- Path safety utility is a preflight/hash helper; its check-then-open flow is not race-free against concurrent filesystem mutation (TOCTOU).
- `verify_record` requires exactly `path` and `sha256`; input records with `exact_values` require a deliberate adapter preserving semantic checks.
- Detached signatures remain design-only; no signature cryptography implemented.
- Retention/custody policy remains design-only; no immutability, WORM storage, or external digest anchoring deployed.
- Copied tests have not been run in Constant Llpoy or Paper A during this audit.

## Next safe work

Design an intake adapter and test harness in Constant Llpoy only: safely extract/contain evidence, validate the manifest, verify every listed file with the workspace-root policy, preserve and validate `exact_values`, and emit an independent report with statuses distinct from producer statuses. Then add the adapter to the existing evidence verification workflow only after interface/security review. Do not promote any producer PASS to mathematical PASS.

## Integrity verification

All nine copied files were fetched from Paper A and Constant Llpoy and compared by content; all were identical. This establishes copy equality, not runtime correctness.
