# IV-225 — Uniform Odd-Block Normalization Reconciliation and kappa=0

**Date:** 2026-11-23
**Target:** AS-ALPHA-A-PROP-0012; retained subsystem {1,2}, finite N>=4
**Status:** UNIFORM AMPLITUDE MAPPING RECONCILED / EXACT SYMMETRY CHECK / KAPPA ZERO AT UNIFORM POINT / EDGE DERIVATIVES OPEN / NOT VERIFIED
**Scope:** Reconcile the global normalized amplitudes in IV-220–224 with the environment Gram coefficients in IV-222, and evaluate the uniform-point small-eigenvalue quartic coefficient. This does not establish the requested edge-response sign.

## 1. Coefficient mapping at uniform coupling

For each environment single-flip k>=3, the retained-odd basis amplitudes are global pair-flip coefficients:
A_ik = a_ik^(1), B_ik = a_ik^(2), C_ik = a_ik^(3) (normalized global-state coefficients).
At uniform g=1, symmetry gives for both i=1,2:
A=1/4, B=(N-2)/8, C=(19N^2-91N+100)/256 from IV-224.
For environment triple T, the amplitude is a four-global-flip coefficient D_iT=3/16 from IV-223.
These are global normalized state coefficients; they enter the reduced Gram construction once, with no extra global normalization multiplier.

## 2. Uniform Gram coefficient checks

Let n=N-2. By the IV-222 coefficient identities:
M2_ij=n A_i A_j=n/16.
M3_ij=n(A_i B_j+B_i A_j)=n(N-2)/16.
M4_ij=n(A_i C_j+C_i A_j+B_i B_j)+binom(n,3)D_iT D_jT
       =n( C/2 + B^2 ) + binom(n,3) 9/256.
Every entry is equal at the uniform point because retained indices 1 and 2 are exchange-symmetric.

Thus in u=(1,1)/sqrt(2), v=(1,-1)/sqrt(2):
a_+=(M2)_uu=2n/16=n/8>0, (M3)_uv=0, and (M4)_vv=0.
Consequently the formal quartic Schur coefficient is
kappa=(M4)_vv-| (M3)_uv |^2/a_+ = 0.

This zero is also required by exact exchange symmetry: at the uniform point the two Gram rows coincide, so the odd-block small eigenvalue is exactly zero (not merely zero through quartic order). The uniform-point result is therefore a symmetry check, not evidence for strict quartic positivity.

## 3. Independent arithmetic checks

Exact rational arithmetic checked the diagonal common-entry M4 values for N=4,...,8:
N=4: 9/32; N=5: 297/256; N=6: 3; N=7: 1575/256; N=8: 351/32.
These are common entries of M4, not eigenvalues; the v eigenvalue is zero.

## 4. Disposition

- Mapping global normalized amplitudes into IV-222 Gram sectors at the uniform point: **RECONCILED**.
- Uniform coefficients A, B, C, D: **CARRIED FROM IV-220/223/224; convention consistency checked**.
- Uniform M2, M3, M4 arithmetic: **EXACT RATIONAL CHECKS**.
- Uniform kappa: **ZERO**, forced by retained-site exchange symmetry.
- Nonuniform coefficients and derivatives wrt u13/u34: **OPEN**.
- First nonzero expansion of small eigenvalue away from uniform symmetry point: **OPEN**.
- Remainder/entropy derivative closure, global B-C sign, and Lean: **OPEN / NOT VERIFIED**.

## 5. Next obligation (IV-226)

Compute explicit first edge derivatives of A, B, D, C for perturbations u13 and u34, respecting the symmetry relations and normalized-state corrections. Assemble derivative-level Gram coefficients and identify the first nonzero symmetry-breaking contribution to the small eigenvalue. Do not infer positivity without calculation.
