# IV-93 — Uniform Remainder and Ratio-Regime Stress Test

**Status:** ANALYTIC-PARTIAL / NUMERICAL EXPLORATION; not a proof of Proposition 0012.

## Question
For the three-vertex path with endpoint mutual information I(1:3), can the proposed leading term
\[
F(x,y)=(x+y)\log_2(x+y)-x\log_2x-y\log_2y,
\quad x=J_{12}^2/(16h^2),\ y=J_{23}^2/(16h^2)
\]
be justified with a remainder uniformly controlled as x/y varies, including boundary regimes?

## Structural leading-order rationale
In the transverse-field product ground-state basis, the first-order wavefunction contains single-spin-flip amplitudes on the two edges. After tracing out the middle vertex, the endpoint sector retains a coherence between the two edge-generated configurations. At leading order the candidate small eigenvalue scales are x and y for the endpoint marginals, and x+y for the joint endpoint state. Their entropy combination gives F. This is a leading-order heuristic/perturbative derivation; it does not itself prove uniform eigenvalue expansions or a remainder bound.

## Numerical exploratory check (local eigensolver)
We diagonalized the 8x8 path Hamiltonian locally with h=1, formed the endpoint reduced density matrix by tracing the middle spin, and computed entropy from its eigenvalues. Values are exploratory; entropy subtraction and very small eigenvalues are numerically delicate. In particular, an extreme-ratio row must not be read as a reliable asymptotic counterexample without higher precision.

| J12 | J23 | Exact diagonalization MI (bits) | F (bits) | MI/F |
|---:|---:|---:|---:|---:|
| 0.01 | 0.01 | 1.2505302303750232e-5 | 1.2499999999999985e-5 | 1.0004241843 |
| 0.0001 | 0.01 | 9.20733396671963e-9 | 9.20654972048301e-9 | 1.0000851835 |
| 0.000001 | 0.01 | 1.7468260318049753e-12 | 1.7511324707777006e-12 | 0.9975407692 |
| 0.01 | 0.0001 | 9.207331965038475e-9 | 9.206549720483478e-9 | 1.0000849661 |
| 0.001 | 0.1 | 9.264527059066677e-7 | 9.206549720497087e-7 | 1.0062974013 |
| 0.0001 | 0.1 | 1.3429845928045192e-8 | 1.3358915207485416e-8 | 1.0053096168 |

## Interpretation / limitations
- The moderate-ratio points are consistent with the proposed leading term.
- The extreme-ratio point (1e-6, 1e-2) shows a small discrepancy that is likely dominated by numerical conditioning at this precision; it is not evidence of failure.
- No claim is made that the remainder is O((x+y)^2), or that such a bound is uniform in x/y. Entropy's derivative diverges at zero, so additive eigenvalue perturbation bounds alone do not automatically control entropy remainders near a boundary.
- The equal-coupling case, one-coupling-zero boundary, and unequal-coupling asymptotics need a proof with ratio-aware eigenvalue/entropy estimates (or high-precision validation supplemented by analysis).

## Next proof obligation
Derive the reduced density matrices' small eigenvalues with estimates that retain relative information when x or y is much smaller than the other. Establish a remainder bound for the entropy combination, preferably expressed in terms of t=x+y and r=x/t, with explicit dependence on r near 0 and 1. Until this is completed, IV-91's leading formula remains proposed, and Paper A / Proposition 0012 remains OPEN, ANALYTIC-PARTIAL, NOT VERIFIED.
