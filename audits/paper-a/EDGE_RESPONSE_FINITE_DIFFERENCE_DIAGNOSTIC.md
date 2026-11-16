# Full-Hilbert-Space Numerical Diagnostic for the Strong-Coupling \(B-C\) Coefficient

**Purpose:** Independently check the predicted leading coefficient in the general-edge proof.  
**Method:** High-precision full-Hilbert-space diagonalization, explicit reduced states, von Neumann entropies, and central finite differences in \(J_{13}\) and \(J_{34}\).  
**Status:** Numerical diagnostic only; not a proof.

## 1. Reproducibility

The script edge_response_finite_difference_diagnostic.py uses mpmath at 50 decimal digits. It sets the uniform coupling \(J=1\), varies \(J_{13}\) and \(J_{34}\) separately by \(\pm10^{-4}\), and estimates

\[
B-C=
\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}.
\]

The predicted leading term is

\[
(B-C)_{\rm lead}=\frac{h^2}{(N-1)^3}.
\]

The full \(2^N\times2^N\) Hamiltonian is diagonalized; no permutation-symmetric reduced Hamiltonian is used for this diagnostic.

## 2. Results

| \(N\) | \(h\) | Finite-difference \(B-C\) | Leading term | Ratio |
|---:|---:|---:|---:|---:|
| 4 | 0.20 | 0.00144942969140041 | 0.00148148148148148 | 0.978365041695 |
| 4 | 0.10 | 0.000368033693677248 | 0.000370370370370370 | 0.993690972929 |
| 4 | 0.05 | 0.0000924261954435451 | 0.0000925925925925926 | 0.998202910790 |
| 5 | 0.20 | 0.000620177914103482 | 0.000625000000000000 | 0.992284662566 |
| 5 | 0.10 | 0.000155935934292247 | 0.000156250000000000 | 0.997989979470 |
| 5 | 0.05 | 0.0000390420911053355 | 0.0000390625000000000 | 0.999477532297 |
| 6 | 0.10 | 0.0000799184985029714 | 0.0000800000000000000 | 0.998981231287 |
| 6 | 0.05 | 0.0000199947778620255 | 0.0000200000000000000 | 0.999738893101 |

The ratios approach \(1\) as \(h/J\to0\), consistent with the proposed leading coefficient.

## 3. Limitations

- Finite differences approximate derivatives and are sensitive to the chosen step.
- The zero eigenvalue of the uniform two-site state opens under edge perturbation; entropy derivatives near this rank-changing point require the analytic argument in GENERAL_EDGE_B_MINUS_C_DERIVATIVE_PROOF.md.
- The tested sizes and field values do not prove the asymptotic statement for all fixed \(N\ge4\).
- Numerical agreement cannot replace the joint-analyticity, Schur-complement, and entropy-derivative proof obligations.

**Conclusion:** The independent full-Hilbert-space numerical check supports the leading coefficient \(h^2/[J^3(N-1)^3]\). It does not, by itself, establish \(B-C>0\).
