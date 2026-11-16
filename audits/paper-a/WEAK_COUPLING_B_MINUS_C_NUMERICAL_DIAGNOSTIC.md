# Full-Hilbert-Space Weak-Coupling \(B-C\) Numerical Diagnostic

**Purpose:** Check the corrected positive leading coefficient independently.  
**Method:** 50-digit or higher full-Hilbert-space diagonalization, explicit reduced states, von Neumann entropy, and central finite differences in \(J_{13}\) and \(J_{34}\).  
**Status:** Numerical consistency check only.

## 1. Predicted asymptotic

\[
(B-C)_{\rm lead}
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right).
\]

The script edge_response_weak_coupling_diagnostic.py uses the full \(2^N\)-dimensional Hamiltonian, varies \(J_{13}\) and \(J_{34}\) independently by \(10^{-4}J\), and computes the ratio of the finite-difference response to this leading term.

## 2. Results at \(h=1\)

| \(N\) | \(J/h\) | Ratio to corrected leading term |
|---:|---:|---:|
| 4 | 0.0050 | 1.21345092725 |
| 4 | 0.0010 | 1.05385408784 |
| 4 | 0.0001 | 1.00698524149 |
| 5 | 0.0050 | 1.15376760022 |
| 5 | 0.0010 | 1.03854511732 |
| 6 | 0.0200 | 1.44242300268 |
| 6 | 0.0050 | 1.13675127460 |

The ratios approach \(1\) as \(J/h\to0\). Finite-coupling corrections are visibly substantial, which is why the analytic proof retains a conservative relative remainder of order \(O_N((J/h)|\ln(J/h)|)\).

## 3. Limitations

- Finite differences are numerical approximations to derivatives.
- Rank-changing eigenvalue branches make entropy derivatives delicate; the analytic zero-eigenvalue lemma is required.
- These finite sizes do not prove the result for every fixed \(N\ge4\).
- Numerical agreement does not establish the remainder order.

**Conclusion:** The full-Hilbert-space calculations support the corrected positive weak-coupling sign and the leading coefficient. They do not replace the analytic proof.
