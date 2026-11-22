# Paper A — IV-172: Independent Audit Attempt, Dependency Gate, and IV-171 Arithmetic Verification

## Audit disposition
This step separates arithmetic checks that can be reproduced from the present derivation context from the upstream analytic bounds that require source inspection. The prior IV-165/166 file paths could not be fetched (GitHub API returned 404), and repository code search returned no matching excerpts for the attempted filenames/phrases. Accordingly, no independent audit of IV-165/166 is claimed.

## 1. Recomputed IV-171 scalar constants
Using \(M=2.265265\), \(c_-=16(31/2)^2/[(256/63)^6(50/49)]\), and \(t_{max}=1/64\), direct scalar recomputation gives:
\[
B_{min}=\log64-\log M-M/32
=3.2704018022258876>0.
\]
\[
c_-=0.8367832138900445.
\]
\[
c_-B_{min}=2.736617330778372,
\qquad 2c_-B_{min}=5.473234661556744.
\]
These agree with IV-171's displayed rounded values. This verifies only the scalar arithmetic, not the upstream interval bounds.

## 2. Re-check of the IV-171 comparison argument
Given \(0\le b\le a\le M\) and \(M>1\), the finite term comparison
\[
\Phi(a)-\Phi(b)=\int_b^a-\log s\,ds\ge-(a-b)\log M
\]
is valid. Since \(g'(s)=\log(1-s)\) and \(-\log(1-s)\le2s\) for \(0\le s\le1/2\), if \(q,q_3\le tM\) and both remain in \([0,1/2]\), then
\[
|g(q)-g(q_3)|\le2tM|q-q_3|=2Mt^2C.
\]
The IV-171 bracket follows under these premises.

## 3. Unverified upstream dependencies
The following cannot be accepted as independently certified in this audit:
- IV-165 bounds for squared-component derivatives and normalization derivatives.
- IV-166 quotient bounds for \(Q,Q_3,Q_t,Q_p,(Q_3)_t,(Q_3)_p\).
- The exact filename/content of these records, since the attempted GitHub fetch/search calls failed.
- Any IV-171 conclusion that requires the reported bound \(Q\le M\) until its proof is independently inspected.

The exact IV-169 factorization and the displayed arithmetic were not re-derived from the full upstream source in this audit; IV-169 remains a recorded analytic claim, not newly certified here.

## 4. Correction to proof status
IV-171 should be labeled **conditional on the required probability-factor bounds and exact identities**. The recomputed numeric constants are verified, but this audit does not upgrade the entropy positivity claim to an unconditional theorem.

## 5. Next action
Recover the actual IV-165/166 source records by repository directory/content retrieval or direct GitHub API/tree access, then audit each inequality from the original formulas. Do not proceed to stronger downstream theorem claims until this dependency gate is cleared.

Repository note created as an audit-status record only; no Lean proof is claimed.
