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


## Phase 5.3I-8.10 — verifier-side policy integrity pin gate
- `paper_a_policy_trust.py` canonicalizes policy JSON and checks its SHA-256 against a verifier-side pin record, including policy identity/version and explicit approved status.
- `test_paper_a_policy_trust.py` includes tampering, pending approval, malformed pin, identity mismatch and canonicalization cases.
- Pin PASS means integrity relative to the provided pin only; approval provenance and pin custody are not cryptographically authenticated.
- **No production policy has been approved or pinned.** The unit tests use test fixtures only. See `PHASE_5_3I_8_10_POLICY_TRUST_PIN_2026-11-21.md`.


## Phase 5.3I-8.11 — trust-gated completeness pipeline
- `paper_a_trust_gated_completeness.py` verifies the policy pin before invoking the completeness evaluator.
- Untrusted policy returns `FAIL_CLOSED` with completeness `NOT_EVALUATED`; trusted policy proceeds to inventory comparison.
- `test_paper_a_trust_gated_completeness.py` exercises fail-closed, trusted, missing-evidence, pending-pin and non-certification boundaries.
- Pipeline status remains evidence-intake/completeness only. No production inventory/pin is approved; no math certification is claimed.
- See `PHASE_5_3I_8_11_TRUST_GATED_PIPELINE_2026-11-21.md`.


## Phase 5.3I-8.12 — independent evidence status semantics
- `paper_a_evidence_status_semantics.py` validates status-specific obligations, evidence/policy digest format, reasons, and FAIL_CLOSED downstream state.
- Same evaluation ID cannot mutate status, scope, evidence, or context digests; re-evaluation requires a new ID.
- PASS is limited to the explicit scope and evidence IDs; it is not certification. This validator does not provide persistent uniqueness or authenticated custody.
- See `PHASE_5_3I_8_12_STATUS_SEMANTICS_2026-11-21.md`.


## Phase 5.3I-8.13 — provenance identity binding
- `paper_a_evidence_provenance_binding.py` validates declared evaluation, evidence bundle, policy, verifier/version, environment and result record identifiers and compares them field-wise.
- Tests cover invalid or missing identity/digest and mismatched binding fields.
- This checks metadata consistency only; no identity authentication, signature verification, immutable custody, or certification is claimed.
- See `PHASE_5_3I_8_13_PROVENANCE_BINDING_2026-11-21.md`.


## Phase 5.3I-8.14 — authenticated provenance record

- `paper_a_provenance_hmac.py` authenticates the entire record using HMAC-SHA256 over deterministic JSON bytes; required identity/digest fields are validated and MAC comparison is constant-time.
- `test_paper_a_provenance_hmac.py` exercises valid records and tampering (status, bundle digest, certification), wrong key, short key, malformed values and missing fields.
- HMAC uses a shared secret. No production secret provisioning, custody, rotation, revocation, or trust-root setup exists. CI secrets are test-only. This is integrity/authentication of the record only, not numerical or mathematical certification.
- See `PHASE_5_3I_8_14_HMAC_AUTHENTICATION_2026-11-21.md`.


## Phase 5.3I-8.15 — independent trust policy and replay guard

- `paper_a_provenance_trust.py` applies verifier-supplied key allowlisting, key revocation, record freshness, nonce validation, HMAC verification, and replay checks.
- `InMemoryReplayGuard` is process-local and not restart/distributed safe; production requires persistent atomic replay state. Caller-provided trusted key registry is not secure key custody. The result explicitly remains `certification: NOT_PERFORMED`.
- `test_paper_a_provenance_trust.py` covers valid/unknown/revoked key, tampering, freshness, future timestamp, replay, nonce, missing metadata and bool timestamp.
- See `PHASE_5_3I_8_15_TRUST_POLICY_REPLAY_GUARD_2026-11-21.md`.


## Phase 5.3I-8.16 — persistent atomic replay registry

- `paper_a_persistent_replay_guard.py` provides a file-backed SQLite registry with atomic nonce consumption and a unique key on `(key_id, nonce)`, protecting nonce reuse across different evaluation IDs for the same key.
- The guard uses transactional insertion, survives process restart, and fails closed on storage errors. `test_paper_a_persistent_replay_guard.py` exercises restart persistence, cross-evaluation replay, key scoping, concurrent race, and failure cases.
- This is local persistent state, not distributed replay coordination. Backup rollback, filesystem durability, deployment permissions and cross-host concurrency remain residual risks; certification is not performed.
- See `PHASE_5_3I_8_16_PERSISTENT_ATOMIC_REPLAY_REGISTRY_2026-11-21.md`.


## Phase 5.3I-8.17 — replay registry integrity and rollback audit

- `paper_a_replay_registry_audit.py` checks SQLite integrity, expected schema presence, and computes a deterministic logical snapshot digest from registry rows.
- `verify_snapshot` detects changes when compared to an independently retained expected digest. Tests cover clean state, digest drift after insertion, missing DB/table, and malformed anchor.
- The digest is not a secure anchor by itself: if both database and expected digest can be altered or rolled back, changes/rollback may go undetected. No external transparency log, hardware anchor, or automatic recovery is implemented.
- See `PHASE_5_3I_8_17_REPLAY_REGISTRY_INTEGRITY_ROLLBACK_AUDIT_2026-11-21.md`.


## Phase 5.3I-8.18 — external replay-registry anchor verification
- `paper_a_external_registry_anchor.py` compares the current logical registry snapshot digest and entry count against an externally supplied anchor record.
- Missing or malformed anchors are rejected; drift returns `FAIL`; missing/corrupt registry fails closed.
- Anchor custody is outside this repository/module: it is not authenticated, advanced, stored, or protected here. If both registry and anchor are replaced/rolled back, detection may be defeated.
- Tests: `test_paper_a_external_registry_anchor.py`; this remains an audit component, not certification.
- Report: `PHASE_5_3I_8_18_EXTERNAL_REGISTRY_ANCHOR_2026-11-21.md`.


## Phase 5.3I-8.19 — authenticated anchor and anti-rollback
- `paper_a_authenticated_registry_anchor.py` authenticates a canonical anchor with HMAC-SHA256, checks a verifier-supplied trusted-key map and explicit minimum sequence floor, then compares live registry digest and count.
- `test_paper_a_authenticated_registry_anchor.py` exercises valid authentication, tampering, unknown key, sequence rollback, live state drift, malformed sequence, and missing DB.
- The key registry and minimum sequence floor must be retained independently. No secure key custody, key rotation/revocation, hardware monotonic counter, anchor advancement protocol, or certification is provided.
- Report: `PHASE_5_3I_8_19_AUTHENTICATED_ANCHOR_ANTI_ROLLBACK_2026-11-21.md`.


## Phase 5.3I-8.20 — atomic anchor advancement and crash-safe transition
- `paper_a_atomic_anchor_advance.py` serializes cooperating local writers using an advisory lock, verifies the currently signed anchor and live registry, applies caller-supplied sequence/digest compare-and-swap expectations, and requires a strictly increasing sequence.
- Writes the next anchor via same-directory staging, file fsync, atomic replacement, and directory fsync; performs read-back equality.
- `test_paper_a_atomic_anchor_advance.py` covers success, stale writers, non-increasing sequence, malformed anchor, untrusted key, simulated replace failure, and registry drift.
- The minimum sequence floor must remain independently held. This local file protocol cannot resist coordinated rollback of the anchor and external floor, does not provide distributed locking, and is not certification.
- Report: `PHASE_5_3I_8_20_ATOMIC_ANCHOR_ADVANCEMENT_2026-11-21.md.


## Phase 5.3I-8.22 — crash-consistency adversarial state-machine model

- `paper_a_anchor_advance_state_machine.py` models STABLE → STAGING → STAGED_DURABLE → REPLACED → READBACK_VERIFIED, with ABORTED only before replacement.
- Invalid state transitions are rejected. Interrupted states remain INDETERMINATE; they are never automatically recovered or promoted.
- `test_paper_a_anchor_advance_state_machine.py` covers valid path, skipped/terminal transitions, interrupted stages, orphan stage contradictions, and trust/integrity failure.
- This is a protocol model, not exhaustive power-loss simulation, filesystem fault injection, or formal proof.


## Phase 5.3I-8.23 — filesystem fault injection at anchor commit boundaries
- `test_paper_a_anchor_filesystem_fault_injection.py` injects Python-level exceptions at staging write, staged-file fsync, `os.replace`, parent-directory fsync, and read-back.
- Pre-replacement failures are tested to preserve the original anchor; failures after replacement explicitly assert that the new anchor may already be visible. Raised exceptions after replace therefore mean commit outcome uncertain, not rollback.
- This is not power-loss, kernel crash, storage hardware, or reboot durability simulation. No durability guarantees or certification are claimed.
- Report: `PHASE_5_3I_8_23_FILESYSTEM_FAULT_INJECTION_2026-11-21.md`.


## Phase 5.3I-8.24 — recovery semantics after ambiguous commit
- `paper_a_ambiguous_anchor_commit_recovery.py` classifies an authenticated live anchor after ambiguous write errors as `COMMITTED`, `NOT_COMMITTED`, `INDETERMINATE`, or `FAIL_CLOSED`.
- `NOT_COMMITTED` is only a retry candidate when previous sequence/digest match, registry verification passes, and no stage files exist; caller revalidation is required. Missing/unexpected state or stage files block retry.
- The classifier is read-only; no automatic retry, repair, or stage promotion. It does not prove post-power-loss durability or certification.
- Tests: `test_paper_a_ambiguous_anchor_commit_recovery.py`; report `PHASE_5_3I_8_24_AMBIGUOUS_COMMIT_RECOVERY_2026-11-21.md`.
