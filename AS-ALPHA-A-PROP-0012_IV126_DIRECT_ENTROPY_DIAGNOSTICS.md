# IV-126 — Direct Entropy-Difference Diagnostics in Shrinking Coupling Regimes

**Status:** NUMERICAL DIAGNOSTIC / NOT A PROOF.  
**Proposition:** AS-ALPHA-A-PROP-0012 remains OPEN, ANALYTIC-PARTIAL, NOT VERIFIED.

## Scope
Evaluate the actual quantity \(\Delta S=2[h(q)-h(q_3)]\) numerically using the lowest eigenvector of the stated 4-by-4 even-parity matrix, with binary entropy defined continuously at endpoints by \(h(0)=h(1)=0\). This is a diagnostic, not a replacement for uniform analytic remainder estimates.

## Numerical method
For each point, form the symmetric matrix
\[
M=\begin{pmatrix}-3&-4a&0&-4b\\-4a&1&-4b&0\\0&-4b&1&-4a\\-4b&0&-4a&1\end{pmatrix},
\quad a=\varepsilon A,\ b=\varepsilon B,
\]
diagonalize it numerically, choose the lowest-eigenvalue eigenvector with positive first component, and compute normalized probabilities
\[
q=(u^2+z^2)/D,\quad q_3=(z^2+w^2)/D,\quad D=1+u^2+w^2+z^2.
\]
Then evaluate entropy directly, not through a truncated entropy series.

## Shrinking ratio tests (A=1, B=eps^alpha)
For \(\alpha\in\{1/4,1/2,1,2\}\) and \(\varepsilon\in\{10^{-2},10^{-3},10^{-4}\}\), the observed \(\Delta S/(2\varepsilon^2)\) is positive and approaches the leading coefficient \(C_2\). Sample data:

| alpha | eps | Direct Delta S/(2 eps^2) | C2 | difference |
|---:|---:|---:|---:|---:|
| 1/4 | 1e-2 | 9.8720609318 | 9.8752406649 | -3.1797e-3 |
| 1/4 | 1e-3 | 14.6741280362 | 14.6741717690 | -4.3733e-5 |
| 1/4 | 1e-4 | 19.3645786447 | 19.3645792079 | -5.6322e-7 |
| 1/2 | 1e-2 | 10.1513780890 | 10.1542388360 | -2.8607e-3 |
| 1/2 | 1e-3 | 14.8075602825 | 14.8076023029 | -4.2020e-5 |
| 1/2 | 1e-4 | 19.4196591489 | 19.4196597049 | -5.5600e-7 |
| 1 | 1e-2 | 10.2065064182 | 10.2093193329 | -2.8129e-3 |
| 1 | 1e-3 | 14.8154537959 | 14.8154957425 | -4.1947e-5 |
| 1 | 1e-4 | 19.4206799938 | 19.4206805497 | -5.5590e-7 |
| 2 | 1e-2 | 10.2075279796 | 10.2103401778 | -2.8122e-3 |
| 2 | 1e-3 | 14.8154686115 | 14.8155105579 | -4.1946e-5 |
| 2 | 1e-4 | 19.4206801881 | 19.4206807440 | -5.5590e-7 |

These tests support the expected asymptotic behavior on these selected paths only; they do not prove positivity uniformly in parameters.

## Exact-axis observations
- At **A=0**, the computed probabilities satisfy \(q=q_3\) and direct entropy difference is exactly zero in floating-point evaluation at the tested points. This is consistent with the previously recorded exact axis reduction; the interior strict-positivity claim cannot extend to this axis without qualification.
- At **B=0**, \(q_3=0\), so \(h(q_3)=0\). The entropy function must be evaluated with its endpoint convention rather than a naive \(0\log 0\) calculation. Direct \(\Delta S=2h(q)\) is positive for nonzero coupling and sufficiently small tested \(\varepsilon\).

## Interpretation / outstanding work
1. Direct calculations on these shrinking-ratio paths are consistent with the positive leading coefficient established in IV-123.
2. The small discrepancy between direct \(\Delta S/(2\varepsilon^2)\) and \(C_2\) decreases with \(\varepsilon\), but the finite samples are not a uniform bound.
3. Establish a rigorous direct-entropy asymptotic with explicit parameter-dependent remainders, especially for shrinking neighborhoods of \(A=0\) and \(B=0\), before asserting a global sign.
4. No Lean formalization, no uniform remainder theorem, and no proof of the full proposition are produced here.

## Reproducibility note
These numerical checks were run with double-precision symmetric eigendecomposition and direct endpoint-aware binary entropy. They should be rerun at higher precision and cross-checked with independent perturbation expansions before being treated as certified numerics.
