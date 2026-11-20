# Paper A THM-0001 — Local saddle-node regularity and remainder audit

- Claim: AS-ALPHA-A-THM-0001
- Date: 2026-11-21
- Frozen source: Paper A Section 3.2, frozen source commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Verdict: **PARTIAL / STATEMENT NEEDS REPAIR**; no direct Lean formalization.

## Exact source setup

[
F(x,g,h)=gmathcal G_N(x)-hx
]
At ((x_c,g_c)), source assumes (F=0), (F_x=0), and states (mathcal G_N(x_c)>0), (g_c>0), with (mathcal G_N''(x_c)<0) for the supercritical branch. Section 3.2 assumes (mathcal G_Nin C^2), but writes the Taylor remainder as
[
O(delta g^2+|delta gdelta x|+|delta x|^3)
]
and later claims a square-root branch expansion with an (O(g-g_c)) correction.

## Correct local expansion and issue

The function is affine in (g), so the (delta g^2) term is actually zero. Under (C^2) alone, Taylor expansion in (x) yields
[
mathcal G_N(x_c+delta x)=mathcal G_N(x_c)+mathcal G_N'(x_c)delta x+	frac12mathcal G_N''(x_c)delta x^2+o(delta x^2),
]
not generally a cubic (O(|delta x|^3)) remainder. Thus the source's asserted remainder is not justified by its stated (C^2) regularity.

At the critical point, the exact identities (F_c=0) and (F_x=0) remove constant and linear terms. For (C^2) and (mathcal G_N''(x_c)<0), a local saddle-node existence/splitting result can be established by a suitable standard theorem or reduction, but the source's specific (O(g-g_c)) correction requires stronger regularity/control than the bare (C^2) condition. A sufficient repair is locally Lipschitz second derivative ((C^{2,1})) or (C^3), alongside explicit nondegeneracy and parameter transversality (here (F_g=mathcal G_N(x_c)>0) already supplies it).

## Conditional algebra that is supported

With (mathcal G_N(x_c)>0), (g_c>0), and (mathcal G_N''(x_c)<0), the leading equation is
[
mathcal G_N(x_c)delta g+	frac12 g_cmathcal G_N''(x_c)delta x^2=0.
]
It gives the leading real branch splitting for (delta g>0):
[
delta xsimpmsqrt{rac{2mathcal G_N(x_c)}{g_c|mathcal G_N''(x_c)|}}sqrt{delta g}.
]
This leading balance is not, by itself, a proof of branch existence or of the stated remainder.

## Classification

- **PARTIAL:** leading square-root coefficient/side is consistent with the critical expansion under the stated sign hypotheses.
- **NOT PASS as written:** the (C^2)-to-cubic-remainder claim and the precise (O(delta g)) branch correction are not justified by the stated regularity.
- **Repair path:** strengthen regularity (or weaken the remainder to a justified little-o statement), state all local hypotheses explicitly, prove the parameter-dependent saddle-node theorem, and keep the model-specific curvature condition as a separate unverified obligation.
- **Global:** this local result does not imply exactly two roots globally.
- **Lean:** no direct theorem formalization was found/created in this audit; analytic reasoning is not Lean verification.

