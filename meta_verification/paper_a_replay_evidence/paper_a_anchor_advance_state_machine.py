"""Adversarial anchor-advance state machine model (Phase 5.3I-8.22).

This is a conservative protocol model, not an implementation-level crash injector.
It enumerates allowed transitions and classifies interrupted states without
promoting any state to trusted recovery.
"""
from enum import Enum

class State(str, Enum):
    STABLE = "STABLE"
    STAGING = "STAGING"
    STAGED_DURABLE = "STAGED_DURABLE"
    REPLACED = "REPLACED"
    READBACK_VERIFIED = "READBACK_VERIFIED"
    ABORTED = "ABORTED"

_ALLOWED = {
    State.STABLE: {State.STAGING},
    State.STAGING: {State.STAGED_DURABLE, State.ABORTED},
    State.STAGED_DURABLE: {State.REPLACED, State.ABORTED},
    State.REPLACED: {State.READBACK_VERIFIED},
    State.READBACK_VERIFIED: set(),
    State.ABORTED: set(),
}

def transition(state, next_state):
    state, next_state = State(state), State(next_state)
    if next_state not in _ALLOWED[state]:
        raise ValueError(f"illegal transition: {state.value} -> {next_state.value}")
    return next_state

def classify_interruption(state, *, final_anchor_authenticated=False,
                          live_registry_matches=False, stage_present=False):
    """Never treat an interrupted state as recovered PASS."""
    state = State(state)
    if state == State.READBACK_VERIFIED:
        if final_anchor_authenticated and live_registry_matches and not stage_present:
            return "PASS"
        return "FAIL_CLOSED"
    if state == State.STABLE:
        if final_anchor_authenticated and live_registry_matches and not stage_present:
            return "PASS"
        return "FAIL_CLOSED"
    if state == State.ABORTED:
        return "INDETERMINATE"
    # A crash during staging or replacement is ambiguous by design.
    return "INDETERMINATE"
