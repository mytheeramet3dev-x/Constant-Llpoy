# IV-88 — Validated numerical path-3 endpoint MI (exploratory)

## Model
Three spins on path 1--2--3, with h=1 and equal couplings J12=J23=J:
H=-J sigma1^z sigma2^z-J sigma2^z sigma3^z-sum_i sigma_i^x.
No direct edge 1--3. Ground state from exact dense Hermitian diagonalization (8x8).

## Correct reduced-state construction
For rho=|psi><psi|, rho_13[a,c;b,d]=sum_m rho[a,m,c;b,m]. Independent one-spin partial trace is used to compute rho_1 and rho_3. Validation checks trace one, Hermiticity, eigenvalue positivity within numerical tolerance, and MI nonnegativity.

## Tested values
J=0.01: MI=8.66801503536391e-6
J=0.03: MI=7.82210623589592e-5
J=0.10: MI=8.887053598602338e-4
J=0.20: MI=3.749426605262347e-3
For all values trace(rho13) was 1 within floating precision; smallest eigenvalues were approximately zero with deviations around 1e-16, and MI was nonnegative.

## Exploratory scaling
MI/J^2 values: approximately 0.08668015, 0.08690236, 0.08887054, 0.09373567 for the four couplings. This suggests an order-J^2 leading behavior in the equal-coupling path test, but this is numerical evidence only. No analytic asymptotic coefficient, uniform limit, or general graph theorem is claimed.

## Limitations
Equal couplings only, h fixed at 1, finite numerical sample, no error bound or analytic expansion. This does not prove general path behavior, B-C, or Proposition 0012. No Lean verification.
