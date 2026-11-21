# IV-54 — Local Quadratic Mixing Expansion Around Uniform Coupling

**Status:** TAYLOR COEFFICIENT CARRIED FROM IV-53 / MIXING-SQUARE DERIVED / DIRECT FOURTH-ORDER TERM OPEN  
**Scope:** Physical edge displacement delta in J_13 around uniform J, h fixed, retained sites 1,2, fixed N>3. Analytic algebra only; no numerical/Lean verification.

## 1. Local cubic off-diagonal coefficient

From IV-53, at the uniform point,
B_uv(0)=0 and D_(J13) B_uv = kappa_N = J^2(N-3)/(16h^3).
For a physical coupling displacement delta, Taylor expansion gives
B_uv(delta)=kappa_N delta+O(delta^2),
provided the cubic coefficient is smooth in the couplings in the neighborhood.

## 2. Mixing-square expansion

The leading large-branch coefficient is a=(N-2)/8 when r=J/h at the uniform point. Then
|B_uv(delta)|^2/a = [J^4(N-3)^2/(256h^6)] delta^2 / [(N-2)/8] + O(delta^3)
= J^4(N-3)^2 delta^2/[32 (N-2) h^6] + O(delta^3).
This is the local expansion of the cubic off-diagonal mixing square divided by the leading eigenvalue coefficient. It is NOT the complete fourth-order low eigenvalue coefficient; the direct term c_vv remains unknown.

## 3. Scaling and caveat

If delta is a physical coupling with energy units, kappa_N has inverse-energy units and B_uv(delta) remains dimensionless as a coefficient of the cubic block. The expression above is dimensionless. The Taylor remainder O(delta^2)/O(delta^3) is only local at fixed J,h,N; no uniform-in-N estimate is established.

## 4. Disposition

- Linear Taylor coefficient kappa_N: carried from IV-53, not independently recomputed.
- Quadratic mixing-square coefficient: algebra PASS.
- Direct fourth-order coefficient c_vv: OPEN.
- Complete low-branch coefficient and positivity: OPEN.
- Edge-response B-C, entropy derivative, differentiated remainder, Lean: OPEN/NOT PERFORMED.

PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
