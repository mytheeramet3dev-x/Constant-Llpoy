# IV-53 — Cubic Off-Diagonal Mixing and Edge Derivatives

**Status:** UNIFORM CUBIC OFF-DIAGONAL ZERO / B-DIRECTION DERIVATIVE RE-DERIVED / SCHUR MIXING TERM OPEN AS FUNCTION OF EDGE PERTURBATION  
**Scope:** Two-site odd block, retained sites 1,2, uniform all-to-all coupling J, derivatives B=J13 and C=J34. Analytic calculation only; no Lean/numerical validation.

## 1. Cubic entry formulas

Use a_ik=J_ik/(4h), b_ik=sum_{m != i,k} J_im J_km/(8h^2), and
O11^(3)=2 sum_{k=3}^N a_1k b_1k,
O22^(3)=2 sum_{k=3}^N a_2k b_2k,
O12^(3)=sum_{k=3}^N(a_1k b_2k+b_1k a_2k).
At uniform J, all three entries equal, so B_uv=(O11-O22)/2=0, and B_vv=0.

## 2. Derivative in B=J13, recomputed term-by-term

Let M=N-2 environment indices.

For O11: k=3 contributes through derivative of a_13, while k=4,...,N contribute through m=3 in b_1k. Hence
D_B O11^(3)=J^2[(N-2)+(N-3)]/(16h^3)=J^2(2N-5)/(16h^3).

For O22: only k=3, m=1 in b_23 depends on J_13; hence
D_B O22^(3)=J^2/(16h^3).

For O12: derivative contributions are (i) k=3 through a_13 and b_23, and (ii) k=4,...,N through b_1k. Combining gives
D_B O12^(3)=J^2(N-2)/(16h^3).

Therefore
D_B B_vv=(D_B O11+D_B O22-2D_B O12)/2=0,
but
D_B B_uv=(D_B O11-D_B O22)/2=J^2(N-3)/(16h^3).
So the cubic null coefficient derivative cancels, while the cubic off-diagonal mixing derivative generally does NOT (for N>3).

## 3. Derivative in C=J34

Recounting terms in the cubic sums: for O11, C appears in b_13 and b_14 through shared vertex 4 or 3; O22 likewise in b_23 and b_24; O12 has matching terms. At uniform point:
D_C O11=D_C O22=D_C O12=J^2/(8h^3).
Thus D_C B_vv=0 and D_C B_uv=0.

## 4. Mixing term implication

At the uniform point B_uv=0, so |B_uv|^2/a=0. Its first derivative also vanishes at that point because the derivative of |B_uv|^2 is 2 Re(B_uv* D B_uv), and B_uv=0. However, the directional derivative D_B B_uv above is nonzero for N>3, so the mixing correction begins quadratically in a B-edge displacement around the uniform point (unless additional cancellations). This is a local statement about the cubic block and not an evaluated fourth-order eigenvalue coefficient.

## 5. Disposition

- Uniform cubic odd block is rank-one all-ones: **PASS algebraically**.
- B_vv and its B/C derivatives vanish at uniform point: **PASS at cubic order from the formulas**.
- B_uv at uniform point: **ZERO**.
- D_B B_uv: **J^2(N-3)/(16h^3), nonzero for N>3**.
- D_C B_uv: **ZERO at uniform point**.
- Schur mixing term's local variation: structurally identified, not a full fourth-order coefficient.
- Fourth-order direct term c_vv, low eigenvalue coefficient, entropy derivative, B-C response, uniform differentiated remainder, Lean: **OPEN / NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
