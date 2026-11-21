# PROP-0009 Follow-up Review — Strong-Coupling Uniform Function and Derivative

**Claim:** AS-ALPHA-A-PROP-0009  
**Frozen Paper A commit:** 8deb7de4a49cb2060720246b7101820ee7e08c91  
**Reviewed evidence:** Constant Llpoy's `UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md`, `SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md`, and canonical working derivation.  
**Review type:** Internal mathematical consistency review. No Lean run; no independent code execution in this pass.

## Verdict

**PARTIAL — the new uniform-path derivation addresses the prior differentiation-of-big-O gap, and its displayed entropy/chain-rule algebra is internally consistent. The claim is not promoted to fully verified.**

## Checks

1. **Parameter conversion:** With \\varepsilon=h/J=1/x, the identity (d/dx=-\\varepsilon^2 d/d\\varepsilon) is correct.
2. **One-site entropy:** From (b=\\varepsilon/[2(N-1)]+O_N(\\varepsilon^3)), binary entropy gives (S(\\rho_i)=\\ln2-\\varepsilon^2/[2(N-1)^2]+O_N(\\varepsilon^4)), consistent with the claimed coefficient.
3. **Two-site small eigenvalue:** If the branch is analytic and the coefficient (c_N>0) is established, then (lambda_s=c_N\\varepsilon^4+O_N(\\varepsilon^6)) gives (lambda_s'=4c_N\\varepsilon^3+O_N(\\varepsilon^5)) and the two-sided scale bound for sufficiently small positive epsilon.
4. **Entropy derivative:** The two-sided scale bound controls (|\\ln lambda_s|); hence (-(1+\\lnlambda_s)lambda_s'=O_N(\\varepsilon^3(1+|\\ln\\varepsilon|))). The large eigenvalue derivative sum uses trace normalization and the small-branch derivative. This is a legitimate route that does not differentiate an unqualified big-O remainder.
5. **Mutual-information combination:** Combining (2S(\\rho_i)-S(\\rho_{12})) yields the stated (\\varepsilon^2) coefficient and separately controlled derivative order, conditional on the detailed reduced-state branch expansions.
6. **Domain:** Results are fixed finite (N\\ge4), (arepsilon\\to0^+). They do not imply uniform-in-(N) estimates or any independent-edge response result (B-C).

## Evidence not independently reproduced in this review

- Symbolic recurrence calculation for all (N\\ge9).
- Exact-rational recurrence/certificates for (N=5,6,7,8).
- High-precision (N=4) coefficient verification and the exceptional coefficient (1/648).
- Complete normalized-state and reduced-block coefficient collection from executable source.

These derivations and diagnostics are recorded in Constant Llpoy, but were not independently rerun or line-by-line re-derived here. Their existence is not equivalent to external replication.

## Frozen-source issue

The frozen Section 4.4.2 cites Lemma 5.1, whose located source concerns (B-C), not the uniform (mathcal G_N) expansion. The new Constant Llpoy derivation is an independent proof route, but the frozen citation mismatch remains uncorrected. Upstream manuscript must not be changed as part of this audit.

## Scope separation

This review supports only the uniform coupling path:
- (mathcal G_N(x)) function asymptotic;
- its separately derived (x)-derivative asymptotic and endpoint limits, conditional on the reviewed coefficient/remainder evidence.

It does **not** close the independent edge-derivative expansion (B-C), entropy mixed-derivative remainders, global branch continuation, or Lean/source correspondence.

## Disposition

**ANALYTIC-PARTIAL / DERIVATION REVIEWED; NOT-LEAN-VERIFIED; SOURCE-CITATION MISMATCH OPEN.** Keep PROP-0009 as PARTIALLY VERIFIED. Next work should reproduce the coefficient recurrence and diagnostics, then resolve the source citation and formalize the uniform-path statements.
