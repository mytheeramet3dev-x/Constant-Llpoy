# Paper A DEF-0001 — Interior critical point definition consistency audit

- Claim/record: AS-ALPHA-A-DEF-0001
- Date: 2026-11-21
- Frozen source: Section 3, Paper A frozen commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Status: DEFINITION-CONSISTENT (not a theorem proof; not Lean formalized)

## Definition being audited

For fixed (h>0), the source calls ((x_c,g_c)) an interior critical point when (x_c>0) and
[
F(x_c,g_c,h)=0,quad partial_xF(x_c,g_c,h)=0.
]
The dimensionless equivalent form is
[
f(x_c;eta_c)=0,quad partial_xf(x_c;eta_c)=0,quad eta_c=g_c/h.
]

Section 2 defines (x=J/h), (eta=g/h), and (f(x;eta)=etamathcal G_N(x)-x). Section 3 defines (F(x,g,h)=gmathcal G_N(x)-hx).

## Consistency derivation

For fixed (h>0), substitute (eta=g/h):
[
F(x,g,h)=gmathcal G_N(x)-hx
=hleft((g/h)mathcal G_N(x)-xight)
=h f(x;eta).
]
Therefore (F=0iff f=0), because (h>0).

If (mathcal G_N) is differentiable in (x), then
[
F_x=gmathcal G_N'(x)-h
=hleft((g/h)mathcal G_N'(x)-1ight)
=h f_x.
]
Again, (h>0) gives (F_x=0iff f_x=0). Thus the two critical-point formulations are exactly equivalent under the source definitions and fixed positive (h).

## Verdict

- **PASS (definition consistency):** the two formulations are equivalent by the positive factor (h).
- **Scope:** requires (h>0), (x_c>0), and differentiability of (mathcal G_N) at (x_c) for derivative notation. Parameter (eta_c) is defined as (g_c/h).
- **Not a theorem result:** this record is definitional and does not establish the existence of any critical point.
- **Formal status:** no dedicated Lean predicate or theorem correspondence checked/created in this audit.

## Follow-up

A formal definition can be introduced once the paper's core functions and domains are locked. Avoid duplicate definitions or implicit domain coercions.