# Paper A PROP-0002 — Independent algebraic proof audit

- Claim: `AS-ALPHA-A-PROP-0002` (Tangent constraint at an interior critical point)
- Audit date: 2026-11-21
- Source: frozen Paper A Section 3.1, source blob `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- Scope: direct algebraic derivation only; not Lean formalization or independent external review.

## Statement and hypotheses

Let
`F(x,g,h)=g G_N(x)-h x`.
Assume `x_c>0`, `g_c>0`, `h>0`, and `G_N` is differentiable at `x_c`. Assume the critical-point equations:
`F(x_c,g_c,h)=0` and `partial_x F(x_c,g_c,h)=0`.

## Proof

The first critical equation is
`g_c G_N(x_c)-h x_c=0`.
Because `g_c>0` and `x_c>0`, rearrangement/division gives
`G_N(x_c)/x_c=h/g_c`.

Differentiating the definition of `F` in its `x` coordinate gives
`partial_x F(x,g,h)=g G_N'(x)-h`.
At the critical point, the second critical equation therefore gives
`g_c G_N'(x_c)-h=0`, hence
`G_N'(x_c)=h/g_c`.

Combining the two identities yields
`G_N'(x_c)=G_N(x_c)/x_c=h/g_c`.

If, additionally, the exact threshold scaling `g_c(h)=alpha_N h` holds with `alpha_N>0`, then `h/g_c=1/alpha_N`. Substitution yields the scaled identity
`G_N'(x_c)=G_N(x_c)/x_c=1/alpha_N`.

## Result

- **Algebraic derivation:** PASS, conditional on the hypotheses and definitions above.
- **Existence of an interior critical point:** not proved here.
- **Threshold scaling `g_c(h)=alpha_N h`:** an additional premise, not derived by this proposition.
- **Uniqueness/global criticality:** not claimed.
- **Lean proof:** not yet implemented.
- **Paper-source correspondence:** the derivation matches the extracted Proposition 1 and the frozen Section 3.1 equations.
- **Overall claim status:** do not promote to fully VERIFIED until a Lean theorem with the exact hypotheses is compiled and its statement-to-source correspondence is audited.

## Proof-obligation checklist

- [x] Substitute the fixed-point equation and rearrange.
- [x] Differentiate `F` and use the stationarity equation.
- [x] Combine the equalities.
- [x] Derive the `alpha_N` form only under exact threshold scaling.
- [ ] Formalize the algebraic identity in Lean.
- [ ] Compile in the repository's pinned Lean toolchain.
- [ ] Audit the Lean declaration against the source statement.

