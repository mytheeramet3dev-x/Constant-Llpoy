# Paper A Audit — Uniform-response positivity evidence trace (§5.1)

**Audit ID:** AS-ALPHA-A-PROP-0016  
**Frozen source:** Section 5.1 of Paper A, source commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`.  
**Scope:** Evidence traceability for the manuscript's numerical observation that uniform response is positive on tested physical branches for \(N=4,6,8,10,20\), excluding \(N=50\) near-critical data because of a spectral-gap reliability threshold. This is distinct from PROP-0010's algebraic bound.

## Claim

The paper reports numerical positivity of
\[
\chi_0=\frac{\partial I_{12}}{\partial J_*}
\]
for the investigated physical branches at \(N=4,6,8,10,20\), and explicitly does not promote this to an analytic theorem.

## Findings

- The source wording appropriately labels positivity as a numerical observation and explicitly excludes unreliable \(N=50\) near-critical data.
- The current independent verification repository's frozen source snapshot contains the claim, but this pass did not locate a committed raw dataset, executable reproduction script, parameter grid, numerical error estimate, or machine-readable artifact tied directly to the specific positivity statement.
- This is an evidence-traceability gap, not a counterexample and not evidence that the positivity observation is false.
- The response bound in PROP-0010 is an algebraic implication conditional on \(F_J<0\); it cannot be used to establish positivity of \(\chi_0\).
- Positivity must not be conflated with \(F_J<0\), Picard stability, or global branch existence. These are logically distinct.

## Verdict

**NUMERICAL-CLAIM / NOT-INDEPENDENTLY-REPRODUCED.** Manuscript classification is appropriately cautious; evidence provenance and reproducibility remain incomplete in the frozen verification workspace. No numerical rerun, raw data validation, or Lean build was performed.
