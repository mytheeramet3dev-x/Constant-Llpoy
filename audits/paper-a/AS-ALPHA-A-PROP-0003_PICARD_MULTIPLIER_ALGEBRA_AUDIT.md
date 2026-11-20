# Paper A PROP-0003 — Picard multiplier algebra audit

- Claim: `AS-ALPHA-A-PROP-0003`
- Audit date: 2026-11-21
- Source: frozen Paper A Section 3.3, source blob `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- Scope: direct differentiation and inequality equivalence; no Lean proof or nonlinear convergence theorem.

## Definitions and hypotheses

Let `h>0`, and let `G_N` be differentiable at `x_*`. Define
`T(x)=(g/h)G_N(x)` and `F(x,g,h)=gG_N(x)-hx`, with finite real parameters.

## Multiplier identity

Differentiation gives
`T'(x_*)=(g/h)G_N'(x_*)`.

Also
`F_x(x_*,g,h)=gG_N'(x_*)-h`.
Dividing by `h>0` and rearranging:
`(g/h)G_N'(x_*)=1+F_x(x_*,g,h)/h`.
Thus
`T'(x_*)=1+F_x/h`.

## Exact linear-stability inequality

For real `T'(x_*)`, the condition `|T'|<1` is equivalent to
`-1<T'<1`.
Substitute `T'=1+F_x/h`:
`-1<1+F_x/h<1`.
Subtract 1:
`-2<F_x/h<0`.
Since `h>0`, multiplication by h preserves strict order, giving
`-2h<F_x<0`.

This establishes the exact scalar linear-attraction criterion stated in the claim.

## Limits of this audit

- **Algebra:** PASS.
- **Local convergence of the nonlinear Picard iteration:** not independently proved here. The usual derivative test gives local attraction when the map is differentiable and the multiplier has modulus strictly below 1; the source's term “exact linear stability” is appropriately narrower than a global convergence claim.
- **At `|T'|=1`:** linear test is inconclusive.
- **Lean formalization:** not yet implemented.
- **Full claim status:** not formally VERIFIED until the theorem is encoded, compiled, and matched to the source.

## Checklist

- [x] Differentiate the map.
- [x] Derive the multiplier in terms of `F_x`.
- [x] Establish equivalence of the two strict inequalities using `h>0`.
- [ ] Formalize the exact algebra in Lean.
- [ ] Compile in the pinned Lean toolchain and audit correspondence.
