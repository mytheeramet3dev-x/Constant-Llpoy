# IV-91 — Leading weak-coupling endpoint MI on the three-spin path

**Status:** analytic leading-order derivation with numerical cross-check; higher-order remainder not fully quantified.

## Model and notation
\[
H=-h(X_1+X_2+X_3)-J_{12}Z_1Z_2-J_{23}Z_2Z_3,\quad h>0,\quad J_{13}=0.
\]
Set \(x=J_{12}^2/(16h^2)\) and \(y=J_{23}^2/(16h^2)\).

## Perturbative leading weights
In the \(X\)-eigenbasis, the first-order ground-state corrections from the two edges create distinct two-spin-flip states, with amplitudes \(J_{12}/(4h)\) and \(J_{23}/(4h)\). The endpoint marginals therefore have small eigenvalues \(x+o(x)\) and \(y+o(y)\); the endpoint joint state has small eigenvalue \(x+y+o(x+y)\) in the weak-coupling regime. This additive leading weight is also numerically cross-checked below. These leading-weight statements are the perturbative input to the entropy calculation.

## Leading MI
For small \(z\), binary entropy obeys \(H(z)=z(1-\ln z)+O(z^2)\). Substituting the three leading small eigenvalues into \(I=S(\rho_1)+S(\rho_3)-S(\rho_{13})\), the linear and logarithmic scale terms cancel, giving
\[
\boxed{I(1:3)=(x+y)\ln(x+y)-x\ln x-y\ln y+o(x+y).}
\]
The displayed leading expression is homogeneous of degree two in the couplings, with a ratio-dependent coefficient, and does not reduce to one fixed coefficient times \(J_{12}^2J_{23}^2\). At equal couplings, it becomes \(2x\ln2=J^2\ln2/(8h^2)\).

## Numerical cross-check
The script `tools/paper-a/iv91_path3_mi_leading_asymptotic.py` diagonalizes the 8x8 Hamiltonian and checks trace, Hermiticity, positivity, and MI nonnegativity, then compares exact MI with the leading formula.

| J12 | J23 | exact MI | leading estimate | ratio |
|---:|---:|---:|---:|---:|
| 0.001 | 0.001 | 8.66439089206e-8 | 8.664339757e-8 | 1.00000590 |
| 0.001 | 0.002 | 1.56377726558e-7 | 1.56375757356e-7 | 1.00001259 |
| 0.001 | 0.01 | 3.50680220403e-7 | 3.50634600135e-7 | 1.00013011 |
| 0.01 | 0.01 | 8.66801503403e-6 | 8.664339757e-6 | 1.00042418 |
| 0.01 | 0.1 | 3.53751377944e-5 | 3.50634600135e-5 | 1.00888896 |
| 0.03 | 0.1 | 1.96565121472e-4 | 1.94155496051e-4 | 1.01241080 |

The ratio approaches 1 as the tested couplings shrink. This is numerical corroboration, not an independent proof of the remainder bound or a result for general graphs.

## Consequence
This is an indirect endpoint MI result for a path graph. It does not establish the response identity \((N-2)(B-C)\), the general-graph proposition, or Paper A Proposition 0012.

## Reproduction
Run `python3 tools/paper-a/iv91_path3_mi_leading_asymptotic.py`. No Lean formalization was performed.
