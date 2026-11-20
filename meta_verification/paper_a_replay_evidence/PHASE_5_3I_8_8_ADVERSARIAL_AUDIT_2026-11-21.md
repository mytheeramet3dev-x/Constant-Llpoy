# Phase 5.3I-8.8 — Independent Intake Adversarial Audit (2026-11-21)

## Scope
Audit of Constant Llpoy's Paper A replay-evidence intake adapter. This is an integrity review of intake, not mathematical certification.

## Findings and mitigations
- **Empty evidence bundle:** schema allowed empty inputs/artifacts, previously risking a vacuous PASS. Intake now requires at least one input and artifact.
- **Duplicate path across sections:** same path could be represented as both input/output. Canonical duplicates are rejected across the bundle.
- **Noncanonical paths:** backslashes, absolute paths, trailing slash, empty components, dot components, and traversal are rejected before descriptor-relative opens.
- **Metadata race detection:** hashing and manifest reading compare descriptor fingerprints before/after (device, inode, size, mtime_ns, ctime_ns). This mitigates but does not eliminate mutation races.
- **Producer status trust:** producer check labels are explicitly untrusted assertions; their PASS does not imply certification.
- **Hashes:** establish byte equality against the manifest, not manifest authenticity, provenance, numerical correctness, or theorem truth.

## Residual limitations
1. Workspace root and parent chain are trusted at setup; privileged mount/filesystem manipulation is outside scope.
2. Fingerprints cannot rule out all concurrent in-place writes or adversarial filesystem behavior.
3. No detached-signature verification or external custody anchoring is implemented.
4. Intake is not a sandbox and does not invoke claim-specific numerical or mathematical evaluators.
5. Non-empty input/artifact is only a minimal completeness policy. Claim-specific completeness needs an independently maintained inventory.

## Verification
Adversarial tests were added. They are **not claimed passing** until an actual GitHub Actions result is inspected. Certification remains NOT PERFORMED.
