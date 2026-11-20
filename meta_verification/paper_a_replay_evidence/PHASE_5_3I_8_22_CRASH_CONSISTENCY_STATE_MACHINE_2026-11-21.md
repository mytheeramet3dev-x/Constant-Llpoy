# Phase 5.3I-8.22 — Crash-Consistency Adversarial State-Machine Model

## Scope
Adds a deterministic state machine for anchor advancement and conservative interruption classification. It models STABLE → STAGING → STAGED_DURABLE → REPLACED → READBACK_VERIFIED; ABORTED is only allowed before replacement. Invalid transitions are rejected.

## Classification
- PASS: stable/readback-verified state with authenticated final anchor, live registry match, and no staging artifacts.
- INDETERMINATE: interrupted staging/durable-stage/replaced states or aborted state. No auto-recovery.
- FAIL_CLOSED: stable or verified state without the required trust/integrity conditions, or stage artifacts contradict a stable state.

## Tests
Happy path; invalid skipped transition; no transition after terminal verification; interruptions at staging, staged-durable, replaced; stage artifact blocks PASS; replaced-but-unverified stays indeterminate; aborted never PASS; missing authentication fails closed.

## Limitation
This is a protocol state-machine model, not exhaustive power-loss simulation, filesystem fault injection, or formal proof. It does not certify the underlying anchor advancement implementation.
