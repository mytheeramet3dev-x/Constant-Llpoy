# Paper A PROP-0004 — Dimensionless root-set invariance audit

- Claim ID: AS-ALPHA-A-PROP-0004
- Audit date: 2026-11-21
- Frozen source: Section 4.2 at Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Scope: root-set invariance and conditional branch derivative; does not prove existence, uniqueness, or global branch selection.

## Source statement

The manuscript uses
`f(x; eta) = eta G_N(x) - x = 0`
and the ray
`g(gamma,h)=gamma alpha_N h`,
with fixed `gamma` and `alpha_N`, hence `eta=g/h=gamma alpha_N`.

## Proof: root-set invariance

Fix `gamma` and `alpha_N`, and let `h>0`. On the ray,
`eta(h)=g(gamma,h)/h=gamma alpha_N h/h=gamma alpha_N`.
Thus the fixed-point function for every value of `h` on the ray is exactly the same function:
`f_h(x)=gamma alpha_N G_N(x)-x`.
For any `x>0`, the equation `f_h(x)=0` is independent of `h`. Therefore the root sets are identical for all positive `h`:
`{x>0 | f_h(x)=0} = {x>0 | gamma alpha_N G_N(x)-x=0}`.
This is set-level invariance; it does not require a root to exist or be unique.

## Conditional derivative statement

If a selected root `x_*(h)` is differentiable and satisfies the implicit equation `Q(x,h)=gamma alpha_N G_N(x)-x=0`, then `Q` has no explicit `h` dependence and `Q_x=gamma alpha_N G_N'(x_*)-1`. If `Q_x != 0`, implicit differentiation yields `Q_x x_*'(h)+Q_h=0`, with `Q_h=0`, so `x_*'(h)=0`. The manuscript's derivative notation therefore requires branch differentiability and a nonzero implicit derivative; root-set invariance alone is the unconditional statement.

## Verdict

- Root-set invariance: **PASS**, directly from exact substitution and cancellation, assuming `h>0` and fixed `gamma, alpha_N, G_N`.
- Existence of a root: **not proved by this claim**.
- Global uniqueness: **not asserted and not proved**.
- Branch selection/continuation: **not supplied**.
- Derivative `dx_*/dh=0`: **CONDITIONAL PASS** only for a differentiable simple selected branch; the root-set statement is stronger in scope and avoids branch-selection assumptions.
- Lean: not formalized; source correspondence audit remains open.

## Checklist

- [x] Substitute the ray into `eta=g/h`.
- [x] Show the fixed-point function has no `h` dependence.
- [x] State root-set invariance without uniqueness assumptions.
- [x] Identify extra conditions for the derivative claim.
- [ ] Formalize set-level identity and conditional branch derivative in Lean.
- [ ] Compile and review correspondence against the frozen source.
