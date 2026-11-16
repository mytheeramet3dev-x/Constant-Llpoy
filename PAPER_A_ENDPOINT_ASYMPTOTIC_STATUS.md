# Paper A — Endpoint Asymptotic Status for \(B-C\)

**Date:** 2026-11-17  
**Scope:** Fixed finite \(N\ge4\), uniform all-to-all TFIM, independent edge derivatives evaluated at the uniform point.  
**Repository:** Constant Llapoy only. No upstream source modifications.

## 1. Strong-coupling endpoint

For \(x=J/h\to\infty\), the independent general-edge derivation and internal audit give

\[
B-C
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(
\frac{h^4}{J^5}
[1+|\ln(h/J)|]
\right).
\]

Thus \(B-C>0\) for sufficiently large \(J/h\), for each fixed finite \(N\ge4\).

Evidence:
- working/paper-a/GENERAL_EDGE_B_MINUS_C_DERIVATIVE_PROOF.md
- audits/paper-a/GENERAL_EDGE_B_MINUS_C_PROOF_AUDIT.md
- audits/paper-a/EDGE_RESPONSE_FINITE_DIFFERENCE_DIAGNOSTIC.md

## 2. Weak-coupling endpoint

For \(x=J/h\to0^+\), the corrected general-edge derivation gives

\[
B-C
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)
+O_N\!\left(
\frac{J^2}{h^3}
[1+|\ln(J/h)|]
\right).
\]

For every \(N\ge4\),

\[
\frac{2(N-2)}{N-1}>1,
\]

so the leading coefficient is strictly positive. Therefore \(B-C>0\) for sufficiently small \(J/h>0\), for each fixed finite \(N\ge4\).

Evidence:
- working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md
- audits/paper-a/WEAK_COUPLING_B_MINUS_C_PROOF_AUDIT.md
- audits/paper-a/WEAK_COUPLING_B_MINUS_C_NUMERICAL_DIAGNOSTIC.md
- audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md

The weak-coupling remainder is intentionally conservative. The stronger remainder in the original Lemma 5.2 proof is not adopted.

## 3. What follows — and what does not

**Established by the current internal analytic derivations:**
- Both asymptotic endpoints have positive \(B-C\) for each fixed finite \(N\ge4\).
- The original negative weak-coupling sign calculation is invalid because it omitted the order-\(r^2\) coherence.
- The Section 4.4.3 opposite-sign response assertion is contradicted in the weak-coupling endpoint regime.

**Not established:**
- \(B-C>0\) for every intermediate \(J/h\).
- A unique sign or monotonicity theorem across the full parameter range.
- An explicit endpoint threshold for any \(N\).
- Uniformity in \(N\).
- Lean verification or exact proof-to-manuscript correspondence.

Thus the global response-sign problem remains open. Positive asymptotics at both endpoints do not rule out a sign change in the intermediate regime.

## 4. Paper A claim status

- AS-ALPHA-A-PROP-0009: PARTIALLY VERIFIED for the uniform strong-coupling function and derivative; Lean and correspondence pending.
- AS-ALPHA-A-PROP-0012: SOURCE_CONFLICT; its opposite-sign assertion is contradicted by the independent weak-coupling endpoint derivation; formalization pending.
- Supporting Lemma 5.1 fixed-\(N\) strong-coupling statement: independent Constant Llapoy derivation and internal analytic review pass; not yet a fully formalized manuscript theorem.
- Supporting Lemma 5.2 negative-sign statement: invalid; corrected positive weak-coupling asymptotic independently derived.

## 5. Upstream boundary

The frozen Absolute Symmetry sources remain unchanged. Potential upstream corrections that require prior user authorization:
1. Replace or supplement the mismatched Section 4.4.2 Lemma 5.1 citation.
2. Correct the weak-coupling sign statement and its supporting Lemma 5.2 derivation.
3. Add a local endpoint result without claiming global \(B-C>0\).

No such change has been made.
