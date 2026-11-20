# Paper A PROP-0001 — Threshold infimum and subcritical exclusion audit

- Claim ID: AS-ALPHA-A-PROP-0001
- Audit date: 2026-11-21
- Frozen source: Section 2.5 at Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Disposition: ANALYTIC-PASS for infimum-based subcritical exclusion and conditional interior tangency; the threshold is not shown attained or to be a global two-root bifurcation.

## Definitions and hypotheses

Let (D=(0,infty)), and assume (mathcal G_N(x)>0) for every (xin D). Define
[
q(x)=rac{x}{mathcal G_N(x)},qquad alpha_N=inf_{xin D}q(x).
]
Assume the infimum is finite and (D) nonempty. The dimensionless equation is
[
f(x;eta)=etamathcal G_N(x)-x.
]

## Proof 1 — pointwise infimum bound and subcritical exclusion

By the defining property of an infimum, (alpha_Nle q(x)) for every (xin D). If (eta<alpha_N), then (eta<q(x)). Since (mathcal G_N(x)>0), multiplying preserves strict inequality:
[
etamathcal G_N(x)<q(x)mathcal G_N(x)=x.
]
Thus
[
f(x;eta)=etamathcal G_N(x)-x<0
]
for every (x>0). This proves the subcritical no-positive-root statement under the stated positivity and finiteness conditions.

## Proof 2 — attained threshold and exact scaling

If (q) attains its infimum at some (x_c>0), then (q(x_c)=alpha_N). The root equation at that point is
[
alpha_Nmathcal G_N(x_c)-x_c=0,
]
so (eta_c=alpha_N) is a parameter with a positive root. Under the physical relation (eta=g/h), this parameter corresponds to (g_c(h)=alpha_Nh). This is exact dimensional scaling, not evidence that (alpha_N) is universal in (N).

## Proof 3 — conditional interior tangent equations

If (mathcal G_N) is differentiable near (x_c) and (q) has an interior differentiable minimum there, then (q'(x_c)=0). Since
[
q'(x)=rac{mathcal G_N(x)-xmathcal G_N'(x)}{mathcal G_N(x)^2},
]
we obtain (mathcal G_N(x_c)=x_cmathcal G_N'(x_c)). Combining with (q(x_c)=alpha_N) gives
[
f(x_c;alpha_N)=0,qquad
f_x(x_c;alpha_N)=alpha_Nmathcal G_N'(x_c)-1=0.
]
The tangent equivalence is conditional on interior attainment and differentiability, with nonzero denominator ensured by (mathcal G_N(x_c)>0).

## Verdict and scope

- **PASS:** Infimum pointwise inequality; strict subcritical exclusion; exact (g_c(h)=alpha_Nh) when a positive interior minimizer attains the infimum; conditional tangent equivalence.
- **Not proved:** Finiteness/positivity of the infimum from the TFIM model itself; existence or interior attainment of the minimizer; supercritical root existence for every (eta>alpha_N); exactly two global roots; nondegenerate saddle-node; numerical or model-specific properties of (mathcal G_N).
- **Duplicate:** The subcritical exclusion portion of PROP-0008 is the same argument and must not be re-audited as an independent theorem.
- **Formal status:** No matching complete Lean theorem established. This is an analytic audit only.

## Proof sketch

The proof uses only the definition of infimum, positivity of (mathcal G_N), the quotient derivative at an interior minimizer, and the substitution (eta=g/h). The global bifurcation assertions are explicitly excluded.
