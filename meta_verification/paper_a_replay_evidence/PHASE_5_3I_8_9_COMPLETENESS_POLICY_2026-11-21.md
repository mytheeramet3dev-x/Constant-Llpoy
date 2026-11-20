# Phase 5.3I-8.9 — Independent Evidence Completeness Policy (2026-11-21)

## Purpose
Prevent a replay manifest from self-declaring completeness. Constant Llpoy now contains a separate policy evaluator that compares the manifest inventory against independently maintained required inputs, artifacts, and check IDs.

## Status semantics
- PASS means policy-listed names are present in manifest inventory.
- FAIL means at least one policy-listed input, artifact, or check ID is omitted.
- Check ID presence does not prove execution or success. A manifest can be inventory-complete while a listed check reports FAIL; completeness and outcome are intentionally separate.
- Policy maintenance/approval must be independent of the producer and manifest. This code does not authenticate policy provenance.

## Files
- paper_a_evidence_completeness.py: policy validation and inventory comparison.
- paper_a_evidence_completeness.schema.json: policy structure.
- test_paper_a_evidence_completeness.py: omission, duplicate, malformed-policy, and status-separation tests.

## Limitations
No authoritative Paper A evidence inventory is embedded yet because a project-specific complete evidence list has not been independently approved. No certification is implied. CI must be observed before claiming tests pass.
