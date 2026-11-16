# Constant Llapoy Working Formulation — Conditional Local Saddle-Node

> This is a proposed Constant Llapoy formulation, not an edit to the Absolute Symmetry manuscript. It records the conservative (C^2) version and the stronger-regularity alternative.

Let
[
F(x,g,h)=gG(x)-hx
]
and suppose (x_c>0), (g_c>0), (h>0), (G(x_c)>0), and
[
F(x_c,g_c,h)=0,qquad F_x(x_c,g_c,h)=0,qquad G''(x_c)<0.
]
Write (y=x-x_c), (mu=g-g_c), (G_c=G(x_c)).

## Version A: only (G\in C^2)

Taylor's theorem with Peano remainder gives
[
G(x_c+y)=G_c+G'_c y+\tfrac12G''_c y^2+o(y^2).
]
Using the critical-point identities and the exact affine dependence of (F) on (g),
[
F(x_c+y,g_c+mu,h)
=G_c\mu+\tfrac12g_cG''_c y^2+O(|\mu y|)+o(y^2).
]
The nondegenerate fold has two local branches for sufficiently small (mu>0), with leading asymptotic
[
x_\pm-x_c
=\pm\sqrt{\frac{2G_c}{g_c|G''_c|}}\sqrt{\mu}
+o(\sqrt{\mu}).
]
Do not claim a cubic remainder or an (O(\mu)) branch correction from (C^2) alone.

## Version B: stronger regularity

If (G'') is locally Lipschitz near (x_c) (in particular, if (G\in C^3) on a neighborhood with bounded third derivative), then
[
G(x_c+y)=G_c+G'_c y+\tfrac12G''_c y^2+O(|y|^3),
]
and
[
F(x_c+y,g_c+\mu,h)
=G_c\mu+\tfrac12g_cG''_c y^2
+O(|\mu y|+|y|^3).
]
The two branches then satisfy
[
x_\pm-x_c
=\pm\sqrt{\frac{2G_c}{g_c|G''_c|}}\sqrt{\mu}
+O(\mu).
]

## Scope

This is local and conditional. It does not prove that the model-specific curvature is negative, that the critical point exists, that it is globally minimizing, or that there are exactly two roots globally. Those are separate obligations.
