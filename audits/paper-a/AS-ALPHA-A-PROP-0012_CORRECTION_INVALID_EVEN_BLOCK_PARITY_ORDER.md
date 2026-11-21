# CORRECTION — PROP-0012 Even-Block Parity Order Refinement Was Invalid

This correction supersedes the stronger order claim in `AS-ALPHA-A-PROP-0012_EVEN_BLOCK_PARITY_ENTRY_ORDER_REFINEMENT.md`.

## Error

The previous report claimed that two-flip amplitudes have only odd perturbation orders (r, r^3, ...) and that four-flip amplitudes start at r^2. This is not a valid selection rule for a Hamiltonian composed of pair-flip operators: pair flips act by symmetric difference, and overlapping edges can change the target flip set in ways that invalidate parity-of-order claims.

Counterexample: applying pair flips on edges (1,3) and (2,3) gives
[
{1,3}	riangle{2,3}={1,2}.
]
Thus a two-flip configuration {1,2} can be reached at second perturbative order (r^2), so c_12 may contain an O_N(r^2) correction. The previously asserted c_12=a_12+O_N(r^3) is not established and may be false.

## Consequences

- Do not use X=a_12+O_N(r^3) or S=a_12^2+O_N(r^4) based on this parity argument.
- The conservative entries X=a_12+O_N(r^2), S=a_12^2+O_N(r^3) remain the appropriate working orders, subject to explicit amplitude derivation.
- The Schur estimate D=O_N(r^3) and lambda_s=O_N(r^3) from the earlier even-block Schur audit remains conditional on those conservative entry expansions.
- No O_N(r^4) even-block eigenvalue or entropy improvement is accepted.

## Status

**INVALIDATED refinement; correction recorded.** The earlier refinement report remains in the audit trail but must not be treated as a valid result. No source manuscript was changed. No Lean formalization/build was performed.
