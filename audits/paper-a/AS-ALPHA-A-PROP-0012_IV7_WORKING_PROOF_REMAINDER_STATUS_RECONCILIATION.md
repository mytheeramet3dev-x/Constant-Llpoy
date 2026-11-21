# Paper A — PROP-0012 IV-7: Working-proof remainder-status reconciliation

Date: 2026-11-21

## Scope
This audit checks consistency of the current working derivation and prior committed even-block remainder audits. It is a documentation/provenance reconciliation, not a new eigenvalue proof.

## Observation
The current working file `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md` states in its even-parity block section that the Schur small eigenvalue is only (O_N(r^3)), with first edge derivatives of the same order, and consequently gives an entropy derivative (O_N(r^3(1+|\ln r|))).

Two committed audits separately provide:
1. `AS-ALPHA-A-PROP-0012_EVEN_BLOCK_SMALL_BRANCH_SCHUR_AUDIT.md`: the same (O_N(r^3)) closure conditional on entry expansions, explicitly leaves their provenance open.
2. `AS-ALPHA-A-PROP-0012_EVEN_BLOCK_R4_INTEGRATION_REVIEW.md`: a stronger environment-resolved argument uses (X=c_\emptyset\overline{c_{12}}+R_X), (R_X=O_N(r^3)), (S=|c_{12}|^2+R_S), (R_S=O_N(r^4)), and (L=|c_\emptyset|^2+O_N(r^2)). It concludes (D=S-|X|^2/L=O_N(r^4)), with first edge derivatives, and (lambda_s=O_N(r^4)), conditional on the pair-flip order lemma and exact entry formulas.

These are not necessarily contradictory: the working file retains a conservative (O_N(r^3)) statement, while the later audit claims a strengthened (O_N(r^4)) cancellation. However, the working proof has not been updated to integrate or explicitly reference the stronger conditional argument, and its section does not reproduce the environment-resolved derivation.

## IV-7 disposition
- Documentation status mismatch: **FOUND**.
- Mathematical contradiction: **NOT ESTABLISHED**.
- Stronger even-block (O_N(r^4)) integration: **CONDITIONAL ANALYTIC REVIEW**, not formal proof.
- The current working derivation's conservative (O_N(r^3)) estimate remains safe as stated if its entry-expansion hypotheses are accepted.
- Do not use the stronger (O_N(r^4)) estimate as unconditional in the working proof until the environment-resolved entry formulas, pair-flip-order lemma, edge-derivative estimates, and source convention are integrated and independently checked.

## Next proof obligation
Explicitly reconcile the working proof and the newer (O_N(r^4)) report. Reconstruct the even-block entries from the exact amplitude sums and verify the empty-environment and nonempty-environment contributions with first edge derivatives, then choose the supported remainder order. This reconciliation is bookkeeping/provenance, not a promotion of PROP-0012.
