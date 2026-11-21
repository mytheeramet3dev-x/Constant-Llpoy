# IV-90 — Path-3 reduced-state spectral validation

**Status:** numerical validation only. No analytic asymptotic expansion has been established.

## Model
\[
H=-J_{12}Z_1Z_2-J_{23}Z_2Z_3-h(X_1+X_2+X_3),\quad J_{13}=0.
\]
The ground state is obtained from an 8x8 exact diagonalization. Spin 2 is traced out. MI is evaluated using natural-log entropy.

## Implementation checks
The executable checks full-state trace, reduced trace, Hermiticity, PSD (within tolerance), and nonnegative MI for tested points. The partial trace contracts the second and fifth tensor indices (spin 2 bra/ket).

## Samples at h=1
| J12 | J23 | ground energy | MI(1:3) |
|---:|---:|---:|---:|
| 0.01 | 0.01 | -3.00005 | 8.66801503403e-6 |
| 0.01 | 0.03 | -3.00024999 | 2.03482201651e-5 |
| 0.03 | 0.01 | -3.00024999 | 2.03482201636e-5 |
| 0.01 | 0.10 | -3.00252347048 | 3.53751377944e-5 |
| 0.03 | 0.10 | -3.00272370747 | 1.96565121472e-4 |
| 0.10 | 0.10 | -3.00499999221 | 8.88705359861e-4 |

The endpoint-swap pairs give matching MI within numerical precision, consistent with path reflection symmetry.

## Important correction / interpretation
Earlier IV-89 scaling ratios were computed but do not establish a leading-order monomial. IV-90 deliberately makes no asymptotic claim. This report only records a reproducible reduced-state numerical baseline. The next proof obligation is an analytic expansion of \(\rho_{13}\), followed by controlled eigenvalue/entropy asymptotics.

## Reproduction
Run `python3 tools/paper-a/iv90_path3_reduced_state_validation.py`. No Lean proof was performed.
