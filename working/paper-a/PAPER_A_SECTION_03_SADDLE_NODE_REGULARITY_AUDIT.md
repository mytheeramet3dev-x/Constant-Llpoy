# Paper A — Section 3 Saddle-Node Regularity and Branch Audit

**Audit ID:** CL-PA-S3-REG-001  
**Source:** Frozen upstream Arxiv/paper_01_section_03_revised.md  
**Frozen source commit:** 8deb7de4a49cb2060720246b7101820ee7e08c91  
**Source blob:** 9ac164ac67cc121af212c4fb7268b809d9234bd6  
**Status:** MATHEMATICAL AUDIT / PROPOSED CORRECTION / NOT VERIFIED  
**Policy:** No upstream source modification.

## 1. Executive finding

Section 3 has a valid algebraic tangent calculation, but its stated C² hypothesis does not justify the displayed cubic Taylor remainder or the claimed O(g-g_c) remainder in the square-root branch expansion. The same issue propagates into the displayed O(g-g_c) expansion of F_x in §3.3.

This does not mean that a local saddle-node pair cannot be established under C². With the appropriate nondegeneracy and sign hypotheses, a local two-root conclusion and the leading square-root scaling can be proved. The generally justified branch statement under C² is

\[
x_\pm(g)-x_c=\pm C\sqrt{g-g_c}+o(\sqrt{g-g_c}),
\]

not, in general, ± C sqrt(g-g_c) + O(g-g_c). The sharper remainder requires additional regularity, for example a locally Lipschitz second derivative (C²,¹) or suitable C³ control, together with a complete quantitative argument.

The model-specific hypotheses G_N''(x_c)<0 and existence/attainment of the relevant critical point are not established by the local algebra alone.

## 2. Definitions and derivative conventions

For fixed h>0, the source defines

\[
F(x,g,h)=g\mathcal G_N(x)-hx,\qquad
f(x;\eta)=\eta\mathcal G_N(x)-x,\quad \eta=g/h,
\]

so F=h f. Derivatives in §§3.1–3.3 are with respect to dimensionless x. Do not confuse this F_x with the physical-coupling derivative F_J used in Section 4.

At a critical point (x_c,g_c),

\[
F(x_c,g_c,h)=0,\qquad F_x(x_c,g_c,h)=0.
\]

These equations imply

\[
g_c\mathcal G_N(x_c)=hx_c,\qquad
g_c\mathcal G_N'(x_c)=h,
\]

and hence

\[
\mathcal G_N'(x_c)
=\frac{\mathcal G_N(x_c)}{x_c}
=\frac{h}{g_c}.
\]

**Disposition:** the tangent identity in §3.1 is algebraically correct, conditional on existence of a differentiable G_N and an interior critical point with x_c>0, g_c>0, h>0.

## 3. Taylor remainder audit

Write u=x-x_c and v=g-g_c, holding h fixed. Using the two critical-point equations, the exact decomposition is

\[
F(x_c+u,g_c+v,h)
=v\mathcal G_N(x_c+u)
+g_c[\mathcal G_N(x_c+u)-\mathcal G_N(x_c)-\mathcal G_N'(x_c)u].
\]

If G_N is C² near x_c, then

\[
\mathcal G_N(x_c+u)
=\mathcal G_N(x_c)+\mathcal G_N'(x_c)u
+\frac12\mathcal G_N''(x_c)u^2+o(u^2).
\]

Also v[G_N(x_c+u)-G_N(x_c)]=O(|vu|). Thus the valid expansion is

\[
F=\mathcal G_N(x_c)v
+\frac12g_c\mathcal G_N''(x_c)u^2
+o(u^2)+O(|vu|).
\]

The source instead writes a remainder O(v²+|vu|+|u|³). The O(u³) term does not follow from C²; it requires stronger control of the second derivative. The O(v²) term is harmless because F is affine in g, but it does not repair the missing cubic control.

**Finding S3-01 — P0:** Replace the stated Taylor remainder under C².

## 4. What follows under C² and a nondegenerate fold

Assume additionally:
1. G_N is C² on a neighborhood of x_c;
2. F=F_x=0 at (x_c,g_c,h);
3. G_N(x_c)>0;
4. G_N''(x_c)<0.

The last inequality is a model-specific hypothesis, not a consequence of the first three. Set a=G_N(x_c)>0 and b=-g_c G_N''(x_c)>0. The local equation has the form

\[
0=av-\frac b2u^2+o(u^2)+O(|vu|).
\]

A local fold argument can then establish, for sufficiently small v>0, two nearby roots on opposite sides of x_c, with

\[
u_\pm(v)=\pm\sqrt{\frac{2a}{b}}\sqrt v+o(\sqrt v).
\]

The argument must state a neighborhood, control signs at suitable boundary points, and use local monotonicity/critical-point structure to count roots. The source formula with an O(v) remainder is sharper than this C² conclusion.

**Finding S3-02 — P0:** Retain only the leading square-root law with o(sqrt(v)) under C², unless stronger regularity is supplied and proved.

## 5. Branch derivative and orientation

The source states F_x(x_±,g,h)=g_c G_N''(x_c)(x_±-x_c)+O(g-g_c). Under C², continuity of G_N'' gives

\[
F_x(x_c+u,g_c+v,h)
=g_c\mathcal G_N''(x_c)u+o(u)+O(v).
\]

Since u_±(v)=±C sqrt(v)+o(sqrt(v)), this yields

\[
F_x(x_\pm,g_c+v,h)
=\pm g_c\mathcal G_N''(x_c)C\sqrt v+o(\sqrt v).
\]

Thus, when G_N''(x_c)<0, the signs F_x(x_-)>0 and F_x(x_+)<0 follow sufficiently close to the fold. The source's sharper O(v) remainder is not justified by C² alone.

**Finding S3-03 — P1:** Replace the O(v) derivative remainder with o(sqrt(v)) under C².

## 6. Picard multiplier check

For T(x)=(g/h)G_N(x), at a fixed point,

\[
T'(x_*)=\frac gh\mathcal G_N'(x_*)
=1+\frac1hF_x(x_*,g,h).
\]

Therefore

\[
|T'(x_*)|<1
\quad\Longleftrightarrow\quad
-2h<F_x(x_*,g,h)<0.
\]

This equivalence is exact. The conclusion is local linear stability of the scalar Picard iteration, not global convergence. Near a nondegenerate fold, F_x tends to zero on both branches, so the negative-F_x branch is locally attracting sufficiently close to the fold, while the positive-F_x branch is repelling.

**Disposition:** §3.3 multiplier algebra is correct, conditional on differentiability. Preserve the distinction between local linear attraction and global convergence.

## 7. Global statements and threshold definition

The local fold theorem does not establish exactly two roots on the entire positive axis, nor does it establish the absence of roots below threshold unless the critical parameter is tied to the global infimum alpha_N=inf_{x>0} x/G_N(x) and positivity/domain conditions are stated. An interior minimizer, its attainment, and its nondegeneracy are separate obligations. The global root count requires global information about q(x)=x/G_N(x), including endpoint behavior and all critical points.

**Finding S3-04 — P1:** Keep local fold conclusions separate from global threshold/root-count claims.

## 8. Proposed replacement text for §3.2

The following is a conservative replacement template. It does not claim that the model-specific curvature condition has been proved.

> Assume that G_N is C² on a neighborhood of x_c, that F(x_c,g_c,h)=F_x(x_c,g_c,h)=0, and that G_N(x_c)>0 and G_N''(x_c)<0. Then F_g(x_c,g_c,h)>0 and F_xx(x_c,g_c,h)<0. The C² Taylor expansion is
> \[
> F(x,g,h)=G_N(x_c)(g-g_c)
> +\frac12g_cG_N''(x_c)(x-x_c)^2
> +o((x-x_c)^2)+O(|g-g_c||x-x_c|).
> \]
> The local fold argument yields two nearby roots for g>g_c sufficiently close to g_c, with
> \[
> x_\pm-x_c
> =\pm\sqrt{\frac{2G_N(x_c)}{g_c|G_N''(x_c)|}}\sqrt{g-g_c}
> +o(\sqrt{g-g_c}).
> \]
> This is a local statement. It does not establish a global root count or global continuation of either branch.

For §3.3, replace the branch derivative estimate by

\[
F_x(x_\pm,g,h)
=g_cG_N''(x_c)(x_\pm-x_c)+o(\sqrt{g-g_c}),
\]

under the same hypotheses.

If the authors want to retain O(g-g_c) in the branch coordinate and derivative expansions, state and prove a stronger regularity hypothesis (for example G_N locally C²,¹ or C³) and provide the corresponding quantitative fold argument.

## 9. Proof obligations and acceptance matrix

| ID | Obligation | Current result |
|---|---|---|
| S3-01 | Correct C² Taylor remainder | CHANGE REQUIRED |
| S3-02 | Branch remainder under C² | CHANGE REQUIRED |
| S3-03 | Branch derivative remainder under C² | CHANGE REQUIRED |
| S3-04 | Local fold existence/count with explicit neighborhood argument | NOT FULLY DOCUMENTED |
| S3-05 | Model-specific G_N''(x_c)<0 | OPEN |
| S3-06 | Existence/attainment of interior critical point | CONDITIONAL |
| S3-07 | Global exactly-two-root claim | OPEN / NOT IMPLIED LOCALLY |
| S3-08 | Picard multiplier equivalence | ALGEBRAICALLY VALID |
| S3-09 | Lean correspondence/build | NOT RUN |
| S3-10 | Independent external mathematical review | NOT RUN |

## 10. Cross-section dependency on Section 4

Section 4.4.1 uses x_*(gamma)->x_c and corresponding limits of T' and F_J. Those limits follow for the local upper branch if the local fold existence result is established and the branch is selected consistently. The stronger O(g-g_c) branch expansion is not needed for those limits.

Section 4.4.2 is a separate strong-coupling obligation. A strong-coupling asymptotic for G_N does not prove the curvature condition at x_c or global continuation from the fold to infinity.

Section 4.4.3's global inequality x_*(gamma)>=x_c remains conditional on global continuation/no branch exchange. The weak-coupling response-sign discussion is a distinct response-sector issue and cannot be used to prove the saddle-node branch structure.

## 11. Verification boundary

- This audit is a source-level mathematical review, not a Lean proof.
- No Lean build or CI was run.
- No independent external review was run.
- No upstream manuscript file was changed.
- Paper A remains **NOT VERIFIED**.
