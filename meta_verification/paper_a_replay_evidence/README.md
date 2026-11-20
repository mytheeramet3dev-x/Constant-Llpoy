# Paper A Replay Evidence Intake — Independent Verification Boundary

Status: imported utilities; **not yet integrated into certification workflows**.

## Boundary

- `Absolute_Sym/Alphabet/paper_a/verification` remains the evidence producer: it creates replay manifests, inputs, numerical outputs, and metadata.
- Constant Llpoy is the independent verifier and evidence-review authority. Producer-side PASS labels are claims to inspect, not accepted certification results.
- The imported validator and path-safety utilities are auxiliary intake checks. They are not the existing Constant Llpoy meta-verification pipeline and are not a mathematical certification by themselves.

## Imported components

- `paper_a_replay_manifest.schema.json`: manifest shape.
- `paper_a_replay_manifest_validate.py`: schema-like structural and semantic checks, with optional raw file hash checking.
- `paper_a_replay_manifest_path_safety.py`: workspace-contained file resolution and hash helper.
- Three test modules: validator behavior, path-safety behavior, and schema/validator consistency.
- Threat-model, signature-design, and evidence-retention policy documents.

## Known integration blockers (do not silently treat as resolved)

1. The manifest validator's `--verify-files` path hashes ordinary paths without workspace containment. Use the path-safety helper as a separate gate or design a safe adapter before accepting evidence.
2. The path-safety `verify_record` requires exactly `path` and `sha256`; input records with `exact_values` need an explicit adapter that strips/validates that extra field without discarding its semantic content.
3. The current helper performs path preflight and hashing, not race-free descriptor-relative verification; TOCTOU remains documented.
4. The detached-signature design is a proposal only. No cryptographic signature verification is implemented here.
5. The retention/custody policy is design only. No WORM storage, external anchoring, or retention infrastructure is claimed to exist.
6. Tests have been copied, but have **not been executed** in this repository or in CI during this import.

## Suggested intake order

1. Preserve the producer bundle as received; record source/run identity and bundle digest.
2. Verify path containment and recompute hashes for each retained input and artifact with a workspace root policy.
3. Validate the manifest's structure and semantics. Treat claimed statuses as untrusted data.
4. Verify provenance/attestation independently using existing Constant Llpoy mechanisms where applicable.
5. Route mathematical and numerical claims to their claim-specific independent checks; no evidence-manifest PASS promotes theorem truth.
6. Emit a distinct verifier report with explicit scope, findings, and limitations; fail closed for missing/ambiguous evidence.

## Copy provenance

Imported from `mytheeramet3dev-x/Absolute_Sym`, branch
`paper-a-numerical-evidence-framework-2026-11-20`, under
`Alphabet/paper_a/verification`. Producer generator `paper_a_replay_manifest.py`
was intentionally not copied: it belongs in the producer repository.


## Secure intake adapter (initial implementation)

- `paper_a_replay_evidence_intake.py` validates manifest structure then independently hashes every input/artifact with workspace containment and default symlink rejection.
- `test_paper_a_replay_evidence_intake.py` covers success, hash mismatch, path escape, symlink rejection, and missing artifact.
- Output distinguishes intake checks from producer checks and always reports `certification: NOT_PERFORMED`.
- **Not yet workflow-integrated; tests not executed in CI.** TOCTOU limitations remain.


## Race-reduced intake hardening (8.7)
- Intake paths are workspace-relative; absolute paths and `..` traversal are rejected.
- Manifest and evidence are opened via directory descriptors and `O_NOFOLLOW` (when supported), and targets are checked as regular files. Hashing occurs on opened descriptors.
- Dedicated workflow `.github/workflows/paper-a-replay-evidence-intake-tests.yml` runs this package's tests on changes, PRs, or manual dispatch. The first actual run must still be inspected before reporting tests as passing.
- Residual risks: platform/filesystem semantics, trusted workspace-root setup, mount/privileged adversaries; not a sandbox or mathematical certification.


## Adversarial audit 8.8
- Empty input or artifact sections fail closed.
- Duplicate normalized paths across inputs/artifacts are rejected.
- Paths must be canonical relative POSIX paths (no backslashes, empty/dot/traversal components).
- Descriptor metadata fingerprints are checked before/after manifest read and evidence hashing (race mitigation, not full snapshot protection).
- Producer check statuses remain untrusted claims; intake does not certify mathematics.
- See `PHASE_5_3I_8_8_ADVERSARIAL_AUDIT_2026-11-21.md`.


## Phase 5.3I-8.9 — independent evidence completeness policy
- `paper_a_evidence_completeness.py` compares manifest inventories against a separately maintained policy.
- Policy requires non-empty required input and artifact lists, rejects duplicates and noncanonical paths.
- Completeness status only means names are present; it does not imply checks passed or policy authenticity.
- No authoritative Paper A inventory is adopted yet; this remains an interface/tooling component pending independent inventory approval.
- See `PHASE_5_3I_8_9_COMPLETENESS_POLICY_2026-11-21.md`.
