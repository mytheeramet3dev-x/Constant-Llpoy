# Independent Regularity Audit — AS-ALPHA-A-THM-0001

- Audit ID: CL-A-AUDIT-SN-0001
- Date: 2026-11-17
- Target: `AS-ALPHA-A-THM-0001`
- Frozen source: `Arxiv/paper_01_section_03_revised.md`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Source blob: `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- Constant Llapoy snapshot: `source_snapshots/paper-a/Arxiv/paper_01_section_03_revised.md`
- Review type: local Taylor-remainder and bifurcation-asymptotic audit
- Lean status: NOT_RUN
- Model-specific curvature status: OPEN / NOT_ESTABLISHED

## 1. Executive finding

The stated (C^2) hypothesis is sufficient for the quadratic Peano expansion
[
\mathcal G_N(x_c+y)=G_c+G'_c y+\tfrac12G''_c y^2+o(y^2),
]
but is **not sufficient in general** for the cubic remainder (O(|y|^3)) asserted in Section 3.2. It is also not sufficient in general for the stronger branch-location error (O(g-g_c)) displayed after solving the normal form.

A locally Lipschitz second derivative (equivalently (C^{2,1}) locally) is a convenient sufficient condition for the cubic Taylor remainder. A locally bounded third derivative, for example (C^3) on a neighborhood, is another sufficient condition. These are sufficient, not claimed to be necessary.

Under only (C^2) plus the nondegeneracy and transversality assumptions, the natural general conclusion is the leading square-root law with an (o(\sqrt{g-g_c})) error, not automatically an (O(g-g_c)) error.

**Disposition:** the local saddle-node mechanism is mathematically supportable, but the source overstates the remainder under its stated regularity. Keep the Constant Llapoy claim NOT_VERIFIED until the exact intended theorem and hypotheses are settled and formally checked.

## 2. Exact structure of this model

At fixed (h),
[
F(x,g,h)=gG(x)-hx,qquad G=\mathcal G_N.
]
Write (y=x-x_c), (mu=g-g_c). At the critical point:
[
F(x_c,g_c,h)=0,qquad F_x(x_c,g_c,h)=0.
]
Since (F) is affine in (g), there is no independent (mu^2) term. Exactly,
[
F(x_c+y,g_c+mu,h)
= g_c\bigl(G(x_c+y)-G_c-G'_c y\bigr)
+\mu G(x_c+y)
]
after using the two critical-point identities. If (G\in C^2), this gives
[
F=\mu G_c+\tfrac12g_cG''_c y^2
+O(|\mu y|)+o(y^2),
]
locally. The (O(|\mu y|)) follows from local boundedness of (G'); the (o(y^2)) is the Peano remainder. This is the generally justified (C^2) statement.

If (G'') is locally Lipschitz, then
[
G(x_c+y)=G_c+G'_c y+\tfrac12G''_c y^2+O(|y|^3),
]
and the model-specific exact affine dependence on (g) yields
[
F=\mu G_c+\tfrac12g_cG''_c y^2
+O(|\mu y|+|y|^3).
]
The source's larger remainder (O(\mu^2+|\mu y|+|y|^3)) is then also valid, though the (mu^2) term is unnecessary for this exact (F).

## 3. Why (C^2) does not imply the cubic bound

Fix (0<\alpha<1) and consider locally
[
G(x_c+y)=G_c+m y+b y^2+|y|^{2+\alpha},
]
with (G_c>0), (x_c>0), (m=G_c/x_c), and (b\ne0). This function is (C^2) near (x_c), and its second derivative is continuous, but the Taylor remainder after the quadratic term is (|y|^{2+\alpha}), which is not (O(|y|^3)) as (y\to0). The chosen (m) also satisfies the tangent relation (G'_c=G_c/x_c); choosing (g_c=h/m>0) makes the two critical-point equations hold. The coefficient (b) can be chosen negative to realize (G''_c<0).

Thus the defect persists even in a local example satisfying the saddle-node tangency and nonzero-curvature conditions. (C^2) alone cannot justify the cubic remainder.

## 4. Branch-location error

Let (\mu=g-g_c>0), (G_c>0), and (g_cG''_c<0). Under a cubic remainder, the leading balance gives
[
y_\pm=\pm A\sqrt\mu+O(\mu),qquad
A=\sqrt{\frac{2G_c}{g_c|G''_c|}}.
]
This is justified by the usual rescaling (y=\sqrt\mu z) and a regular perturbation/implicit-function argument around the two nonzero simple roots in the rescaled variable.

With only (C^2), the remainder may instead be (O(|y|^{2+\alpha})) for (0<\alpha<1). Substituting (y\asymp\sqrt\mu) produces a correction of order (\mu^{(1+\alpha)/2}), which is larger than (\mu). Therefore the claimed (O(\mu)) branch error is not guaranteed by (C^2).

Under (C^2), the generally safe statement is
[
y_\pm=\pm A\sqrt\mu+o(\sqrt\mu),
]
with local existence of the two branches on the appropriate side under the nondegenerate fold hypotheses. If a stronger error term is desired, the regularity must be strengthened accordingly.

## 5. Additional sign and scope checks

1. The coefficient (G_c) must be strictly positive for the parameter transversality condition (F_g=G_c>0).
2. The fold condition requires (g_cG''_c\ne0); for the stated supercritical side (g>g_c), one needs (g_c>0) and (G''_c<0).
3. At an interior critical point of (q(x)=x/G(x)), the tangent relation gives
   [
   q''(x_c)=-\frac{x_cG''(x_c)}{G(x_c)^2}.
   ]
   Thus (G''(x_c)<0) is equivalent to (q''(x_c)>0), i.e. a nondegenerate local minimum, assuming (G(x_c)>0). It is not equivalent to strict global minimality.
4. The local fold theorem does not establish global root count or global threshold attainment.
5. The source's displayed branch formula is conditional on negative curvature; the model-specific sign (G''(x_c)<0) remains unproved by this audit.

## 6. Recommended theorem formulations

### Option A — retain (C^2), weaken the remainders

State the local expansion as
[
F=G_c\mu+\tfrac12g_cG''_c y^2+O(|\mu y|)+o(y^2),
]
and the branch law as
[
y_\pm=\pm A\sqrt\mu+o(\sqrt\mu).
]
This is the conservative formulation supported by (C^2), subject to the nondegenerate fold and transversality assumptions.

### Option B — retain the current cubic and branch error terms

Strengthen the hypothesis to (G\in C^{2,1}) locally (or another explicit condition guaranteeing a cubic Taylor remainder, such as a locally bounded third derivative). Then the cubic expansion and (O(\mu)) branch correction are supportable. The exact assumptions should be stated on a neighborhood of (x_c), not just informally as “at least (C^2).”

## 7. Disposition matrix

| Obligation | Result |
|---|---|
| (C^2\Rightarrow o(y^2)) Peano remainder | PASS |
| (C^2\Rightarrow O(y^3)) | FAIL (counterexample) |
| (C^{2,1}\Rightarrow O(y^3)) | PASS (sufficient condition) |
| Cubic local normal form under strengthened regularity | PASS, conditional |
| (O(\mu)) branch correction under cubic remainder | PASS, conditional |
| (O(\mu)) branch correction from (C^2) alone | FAIL (not guaranteed) |
| Leading square-root law under (C^2) fold hypotheses | PASS, with (o(\sqrt\mu)) error |
| Model-specific (G''(x_c)<0) | OPEN |
| Global root count | NOT_ESTABLISHED |
| Lean verification | NOT_RUN |
| Constant Llapoy claim status | NOT_VERIFIED |

No manuscript source was modified. No claim status was upgraded.
