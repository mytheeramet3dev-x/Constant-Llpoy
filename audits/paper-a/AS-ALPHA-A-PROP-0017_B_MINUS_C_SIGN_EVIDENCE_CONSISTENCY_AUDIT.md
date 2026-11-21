# Paper A Audit — Section 5.3 B−C sign evidence and source consistency

**Audit ID:** AS-ALPHA-A-PROP-0017  
**Frozen source:** Paper A Sections 5.2–5.3, commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`.  
**Scope:** Evidence consistency for the numerical/conjectural \(B-C>0\) statement, including comparison with the existing weak-coupling audit PROP-0012. This does not re-prove the representation algebra in PROP-0005.

## Claim

The manuscript reports \(B-C>0\) as numerical evidence and a strong conjecture, not an exact theorem. The sign would imply \(\chi_1>\chi_2\) via the exact identity \(\chi_1-\chi_2=(N-2)(B-C)\), for \(N\ge4\).

## Evidence found

- The current paper data CSV contains four rows, \(N=4,6,8,10\), and reports positive \(B-C\) values (approximately 0.01291, 0.01434, 0.01645, 0.01799).
- Each row reports dense and reduced solver values. The absolute cross-check errors are 0, \(1.61\times10^{-11}\), \(3.89\times10^{-12}\), and \(5.55\times10^{-13}\), respectively.
- The CSV does not identify the coupling/branch point for each row, provide a full scan/grid, finite-difference step or derivative extraction details, uncertainty bounds, or executable reproduction command in this file. Solver agreement is evidence of implementation cross-check at the listed points, not a proof of the sign globally.
- The separate weak-coupling audit PROP-0012 reports a source conflict: the prior Lemma 5.2 sign derivation omitted an order-\(r^2\) coherence contribution, and the corrected conditional leading coefficient is positive for \(B-C\). This weak-coupling correction is consistent with the positive tabulated values but does not establish the global conjecture.
- The existing theorem target correctly identifies an unresolved sector-ordering lemma; symmetry, PF positivity, endpoint asymptotics, and the exact eigenvalue identity do not alone establish \(B-C>0\).

## Verdict

**NUMERICAL EVIDENCE / GLOBAL SIGN OPEN.** Positive tabulated values and dense-versus-reduced cross-checks are present for four finite sizes, but evidence provenance and parameter coverage are incomplete for independent reproduction. The weak-coupling source conflict remains a manuscript-correction obligation. Do not claim a global theorem or use this sign to infer stability/locality without separate conditions.
