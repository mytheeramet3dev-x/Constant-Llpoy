"""Retry decision gate for ambiguous anchor commits (Phase 5.3I-8.25).

This is read-only policy logic. It does not retry, mutate registry/anchor files,
or provide atomicity. Caller must freshly re-run recovery classification immediately
before any retry attempt.
"""
from __future__ import annotations


def authorize_ambiguous_anchor_retry(
    recovery_result,
    *,
    expected_previous_sequence,
    expected_previous_digest,
    intended_sequence,
    externally_held_minimum_sequence,
    caller_freshly_revalidated=False,
):
    """Return a fail-closed retry decision; never performs a retry.

    A retry is considered only for NOT_COMMITTED with explicit caller revalidation,
    an exact one-step sequence transition, and a previous sequence not below the
    external floor. COMMITTED and all ambiguous/failed states deny retry.
    """
    deny = {"decision": "DENY_RETRY", "retry": False}
    if not isinstance(recovery_result, dict):
        return {**deny, "reason": "recovery result must be a mapping"}
    if type(expected_previous_sequence) is not int or expected_previous_sequence < 1:
        return {**deny, "reason": "expected previous sequence invalid"}
    if type(intended_sequence) is not int or intended_sequence != expected_previous_sequence + 1:
        return {**deny, "reason": "retry must target exactly the next sequence"}
    if type(externally_held_minimum_sequence) is not int or externally_held_minimum_sequence < 1:
        return {**deny, "reason": "external minimum sequence invalid"}
    if expected_previous_sequence < externally_held_minimum_sequence:
        return {**deny, "reason": "previous sequence is below external rollback floor"}
    if not isinstance(expected_previous_digest, str) or len(expected_previous_digest) != 64:
        return {**deny, "reason": "expected previous digest malformed"}
    status = recovery_result.get("status")
    if status == "COMMITTED":
        return {**deny, "reason": "intended commit already verified; duplicate retry prohibited"}
    if status != "NOT_COMMITTED":
        return {**deny, "reason": "recovery state is not retry-eligible"}
    if recovery_result.get("anchor_sequence") != expected_previous_sequence:
        return {**deny, "reason": "recovery sequence does not match caller expectation"}
    if recovery_result.get("snapshot_sha256") != expected_previous_digest:
        return {**deny, "reason": "recovery digest does not match caller expectation"}
    if not caller_freshly_revalidated:
        return {**deny, "reason": "caller must freshly revalidate recovery state"}
    return {
        "decision": "RETRY_CANDIDATE",
        "retry": False,
        "reason": "policy gate permits caller to consider a single next-sequence retry after fresh revalidation",
        "target_sequence": intended_sequence,
        "requires_writer_cas": True,
        "execution_performed": False,
    }
