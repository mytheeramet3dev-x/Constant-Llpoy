# Section 3 — Saddle-Node Bifurcation Theorem (Revised)

## 3.1 Critical point and tangent constraint

For fixed \(h>0\), define the dimensional fixed-point function

\[
F(x,g,h)=g\mathcal G_N(x)-hx,
\qquad x=J/h.
\]

It is convenient to divide by the positive scale \(h\) and work with

\[
f(x;\eta)=\eta\mathcal G_N(x)-x,
\qquad
\eta=\frac gh.
\]

The two functions have the same roots and

\[
F=h f.
\]

### Definition 1 — Interior critical point

For a fixed \(h>0\), an interior critical point \((x_c,g_c)\), with \(x_c>0\), satisfies

\[
F(x_c,g_c,h)=0,
\qquad
\partial_xF(x_c,g_c,h)=0.
\]

Equivalently,

\[
f(x_c;\eta_c)=0,
\qquad
\partial_xf(x_c;\eta_c)=0,
\qquad
\eta_c=\frac{g_c}{h}.
\]

### Proposition 1 — Tangent constraint

At an interior critical point,

\[
\boxed{
\mathcal G_N'(x_c)
=\frac{\mathcal G_N(x_c)}{x_c}
=\frac{h}{g_c}
}
\]

If the threshold has the exact scaling \(g_c(h)=\alpha_Nh\), then

\[
\boxed{
\mathcal G_N'(x_c)
=\frac{\mathcal G_N(x_c)}{x_c}
=\frac1{\alpha_N}
}
\]

### Proof

The derivative condition gives

\[
\partial_xF=g_c\mathcal G_N'(x_c)-h=0,
\]

so

\[
\mathcal G_N'(x_c)=\frac h{g_c}.
\]

The fixed-point condition gives

\[
g_c\mathcal G_N(x_c)=hx_c,
\]

and hence

\[
\frac{\mathcal G_N(x_c)}{x_c}=\frac h{g_c}.
\]

Combining the two equations proves the result

## 3.2 Local normal form

Assume that \(\mathcal G_N\) is at least \(C^2\) near \(x_c\). Let

\[
\delta x=x-x_c,
\qquad
\delta g=g-g_c.
\]

Taylor expansion at fixed \(h\) gives

\[
F(x,g,h)
=F_c+F_g\delta g+F_x\delta x
+\frac12F_{xx}\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

At the critical point,

\[
F_c=0,
\qquad F_x=0,
\qquad F_g=\mathcal G_N(x_c)>0,
\qquad F_{xx}=g_c\mathcal G_N''(x_c).
\]

Therefore,

\[
F(x,g,h)
=\mathcal G_N(x_c)\delta g
+\frac12g_c\mathcal G_N''(x_c)\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

### Assumption 1 — Generic nondegeneracy

Assume

\[
\mathcal G_N''(x_c)\neq0.
\]

If \(x_c\) is an interior minimizer of \(x/\mathcal G_N(x)\), then

\[
\mathcal G_N''(x_c)<0
\]

is equivalent to strict nondegeneracy of that minimum

Solving the leading normal form gives

\[
\boxed{
x_\pm-x_c
=\pm
\sqrt{
\frac{2\mathcal G_N(x_c)}{g_c|\mathcal G_N''(x_c)|}
}
\sqrt{g-g_c}
+O(g-g_c)
}
\]

on the side \(g>g_c\) when \(\mathcal G_N''(x_c)<0\)

This is a **local conditional saddle-node theorem**. The condition \(\mathcal G_N''(x_c)<0\) is not established by the numerical scans currently documented and must not be labelled numerically verified without a dedicated curvature audit

## 3.3 Local branch orientation and iteration stability

The derivative with respect to \(x\) is

\[
F_x(x,g,h)=g\mathcal G_N'(x)-h.
\]

Near the two branches:

\[
F_x(x_\pm,g,h)
=g_c\mathcal G_N''(x_c)(x_\pm-x_c)+O(g-g_c).
\]

If \(\mathcal G_N''(x_c)<0\), then

\[
F_x(x_-)>0,
\qquad
F_x(x_+)<0.
\]

This determines the local orientation of the two branches

### Picard iteration

The dimensionless fixed-point iteration is

\[
x^{(k+1)}=T(x^{(k)}),
\qquad
T(x)=\frac gh\mathcal G_N(x).
\]

At a fixed point,

\[
T'(x_*)=\frac gh\mathcal G_N'(x_*)
=1+\frac1hF_x(x_*,g,h).
\]

The exact linear stability condition for this iteration is

\[
\boxed{|T'(x_*)|<1}
\]

or equivalently

\[
\boxed{-2h<F_x(x_*,g,h)<0.}
\]

Near a generic saddle-node, \(F_x\) is small, so the branch with \(F_x<0\) has \(0<T'<1\) and is locally attracting, while the branch with \(F_x>0\) has \(T'>1\) and is locally repelling

Away from the bifurcation, the condition \(F_x<0\) alone is not sufficient: if \(F_x\le-2h\), the Picard multiplier has magnitude at least one

The term “physical branch” will therefore mean the branch selected by the documented continuation/iteration prescription, while “Picard stable” requires the full inequality \(|T'|<1\)

## 3.4 Local versus global statements

The local normal form establishes two nearby roots on the supercritical side under Assumption 1. It does not by itself prove that:

- there are exactly two roots globally
- no additional roots exist outside the local neighborhood
- the subcritical regime has no nontrivial root unless \(g_c\) is defined as the global infimum threshold

Those global claims require a separate analysis of

\[
q(x)=\frac{x}{\mathcal G_N(x)}
\]

including its endpoint behavior and all interior extrema

## 3.5 Status

- Tangent constraint: exact
- Local square-root normal form: exact under \(C^2\) and nondegeneracy assumptions
- \(F_g>0\) at a nontrivial point: exact
- \(\mathcal G_N''(x_c)<0\): open model-specific condition
- Two roots globally: not established by this local theorem
- \(F_x<0\) as a universal stability criterion: false; the exact Picard condition is \(|1+F_x/h|<1\)
