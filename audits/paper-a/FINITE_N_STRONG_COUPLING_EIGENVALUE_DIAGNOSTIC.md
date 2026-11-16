# Finite-N Exact-Rational Diagnostic — Strong-Coupling Pair Eigenvalue

**Scope:** Uniform all-to-all TFIM, fixed finite \(N=4,\ldots,8\), \(\varepsilon=h/J\to0^+\).  
**Method:** Exact-rational Rayleigh–Schrödinger recurrence in the even-parity complement-orbit basis, normalized state reconstruction, partial trace, and symbolic eigenvalue expansion.  
**Role:** Diagnostic evidence only. It is not a proof of a formula for all \(N\), nor does it establish any coupling-derivative estimate.

## 1. Reproducible method

The script finite_n_strong_coupling_exact_diagnostic.py constructs the full even-parity Hilbert space by complement orbits. It uses

\[
H/J=K_0+\varepsilon V,\qquad
K_0=-\sum_{i<j}\sigma_i^z\sigma_j^z,\qquad
V=-\sum_i\sigma_i^x.
\]

Intermediate-normalized perturbation coefficients are obtained recursively from

\[
(K_0-E_0)c_n
+Vc_{n-1}
-\sum_{k=1}^{n}E_kc_{n-k}=0.
\]

The resulting state is normalized as a formal series, the two-site reduced density matrix is computed by an exact partial trace, and the smaller eigenvalue in the symmetric parity block is expanded through order \(\varepsilon^4\). All arithmetic is rational until the square-root series for the eigenvalue is formed.

## 2. Exact-rational outputs

| \(N\) | Coefficient of \(\varepsilon^4\) in the small eigenvalue | Candidate \(1/[8(N-2)(N-1)^4]\) | Match |
|---:|---:|---:|---|
| 4 | \(1/648\) | \(1/1296\) | **No — factor 2** |
| 5 | \(1/6144\) | \(1/6144\) | Yes |
| 6 | \(1/20000\) | \(1/20000\) | Yes |
| 7 | \(1/51840\) | \(1/51840\) | Yes |
| 8 | \(1/115248\) | \(1/115248\) | Yes |

For \(N=4\), the discrepancy was additionally checked against direct high-precision diagonalization of the full \(2^N\)-dimensional Hamiltonian at \(\varepsilon=0.01\) and \(0.005\). The ratio \(\lambda_{\rm small}/\varepsilon^4\) approaches \(1/648\), not \(1/1296\).

## 3. Mathematical interpretation

1. The candidate coefficient used in prior proof materials is **not valid uniformly for every \(N\ge4\)** as written.
2. The exact finite-\(N\) recurrence and independent direct diagonalization agree on the exceptional \(N=4\) coefficient.
3. For \(N=5,6,7,8\), the exact-rational recurrence agrees with the proposed expression. A separate symbolic low-Hamming-weight recurrence now derives the same coefficient for every fixed \(N\ge9\); see SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md.
4. This discrepancy concerns a fourth-order small eigenvalue coefficient. It does not change the leading \(O(\varepsilon^2)\) one-site entropy coefficient or, by itself, disprove the proposed leading \(x^{-2}\) coefficient of \(\mathcal G_N(x)\).
5. This computation is only at the permutation-symmetric uniform point. It does not establish derivatives with respect to \(J_{13}\) or \(J_{34}\), and therefore does not close the \(B-C\) theorem.

## 4. Required follow-up

- Preserve the closed symbolic derivation for \(N\ge9\) and the exact finite calculations for \(N=5,6,7,8\); retain the exceptional \(N=4\) value explicitly.
- Independently verify the recurrence against full-space perturbation theory for additional \(N\).
- Extend the calculation to independent edge variables before taking the uniform limit.
- Establish derivative and lower-bound estimates for every small eigenvalue branch before differentiating the entropy.
- Keep the theorem status NOT_VERIFIED until the analytic remainder chain is complete.

**Verdict:** A concrete finite-size discrepancy has been detected in the inherited fourth-order coefficient. The coefficient must be corrected or qualified before it can be used in a general \(N\ge4\) proof.
