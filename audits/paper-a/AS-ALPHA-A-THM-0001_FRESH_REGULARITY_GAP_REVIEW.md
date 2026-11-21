# THM-0001 — Local Saddle-Node Regularity Gap Audit (Fresh Source Review)

**Frozen source:** Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`, Paper A §3.2–3.4.  
**Audit type:** Fresh mathematical regularity check against the exact frozen source; no Lean build and no model-specific curvature computation.

## Verdict

**REGULARITY-GAP CONFIRMED / LEADING-ORDER RESULT CONDITIONAL.**

The manuscript's stated (C^2) hypothesis does not justify its cubic Taylor remainder or the (O(g-g_c)) correction in the square-root branch expansion. The leading square-root scaling remains consistent under the local nondegeneracy assumptions, but the remainder must be weakened or regularity strengthened.

## 1. Taylor expansion

For a (C^2) function, the second-order Taylor expansion at (x_c) has Peano remainder (o(|delta x|^2)). The source claims a cubic bound (O(|delta x|^3)), which does not follow from (C^2) alone. A local (C^3) bound, or suitable Lipschitz control on the second derivative ((C^{2,1})), is sufficient for cubic remainder control.

Parameter terms likewise need regularity for the claimed mixed and pure-(delta g) bounds; the source is affine in (g), so (F_{gg}=0), but the mixed term still depends on the regularity of (mathcal G_N).

## 2. Branch expansion

The leading coefficient
[
A=sqrt{\frac{2\mathcal G_N(x_c)}{g_c|\mathcal G_N''(x_c)|}}
]
is consistent with solving the local quadratic normal form when (mathcal G_N(x_c)>0), (g_c>0), and (mathcal G_N''(x_c)<0).

Under (C^2) and a nondegenerate fold, the leading splitting can be justified with a weaker asymptotic remainder (typically (o(\sqrt{g-g_c})) absent further quantitative smoothness). The stronger
[
x_\pm-x_c=\pm A\sqrt{g-g_c}+O(g-g_c)
]
requires additional control, e.g. (C^3) or (C^{2,1}) in the neighborhood, plus a branch-existence argument. Do not treat this stronger remainder as proved from (C^2).

## 3. What remains valid / open

- Tangent constraint: exact algebra under critical equations.
- Leading square-root coefficient: conditionally consistent under fold nondegeneracy.
- Local two-branch existence: requires the local fold hypotheses; no model-specific curvature proof.
- Claimed cubic Taylor remainder and (O(g-g_c)) branch correction: **not justified by stated (C^2)**.
- (mathcal G_N''(x_c)<0): remains model-specific OPEN.
- Exactly two roots globally: not implied by local normal form.
- Picard stability: exact criterion remains (|1+F_x/h|<1); (F_x<0) alone is insufficient globally.
- Lean: no formalization/build was inspected or run in this fresh pass.

## 4. Correction options to record

Either:
1. strengthen the regularity hypothesis to (C^3) (or a suitably stated (C^{2,1}) condition) and prove the quantitative remainder; or
2. retain (C^2), weaken the Taylor and branch remainder statements, and state the precise local fold conclusion supported by the proof.

The frozen source is unchanged.

**Disposition:** `REGULARITY-GAP-CONFIRMED / CONDITIONAL-LEADING-ORDER / MODEL-CURVATURE-OPEN`.
