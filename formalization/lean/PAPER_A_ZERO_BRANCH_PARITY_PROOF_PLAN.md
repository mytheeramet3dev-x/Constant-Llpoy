# Paper A — ZF-2: Parity and Positive Leading Coefficient

**Repository:** Constant Llapoy  
**Scope:** Paper A, one-variable local branch only  
**Status:** OPEN — proof target specified; no theorem is claimed until a pinned Lean build verifies it.

## Target

Let (f,g:\mathbb R\to\mathbb R), (m\in\mathbb N), and suppose:

1. (f) is nonnegative on a two-sided neighborhood of (0);
2. (f(r)=r^m g(r)) on a neighborhood of (0);
3. (g) is continuous at (0);
4. (g(0)\ne0).

The intended conclusion is:

[
m\text{ is even},\qquad g(0)>0.
]

This is a local one-variable statement. It does not yet establish joint uniformity in an edge parameter (u).

## Proof structure

**A. Preserve the exact factorization.** Use the factorization returned by
`exists_local_power_factorization_of_analytic_nontrivial`; do not replace eventual equality with a global identity.

**B. Determine the sign of (g(0)).** Since (g(0)\ne0) and (g) is continuous at zero, its sign is constant on a sufficiently small neighborhood. If (g(0)<0), choose a sufficiently small positive (r). Then (r^m>0), so (r^m g(r)<0), contradicting (f(r)\ge0). Thus (g(0)>0).

**C. Determine the parity of (m).** Continuity and (g(0)>0) imply (g(r)>0) for all sufficiently small positive and negative (r). Choose a sufficiently small negative (r). Since
[
0\le f(r)=r^m g(r),\qquad g(r)>0,
]
we obtain (r^m\ge0). A negative real number has a nonnegative (m)-th power only when (m) is even.

## Lean decomposition

Formalize the proof as separate lemmas so each filter and sign argument is reviewable:

- **ZF-2a:** continuity plus (g(0)\ne0) gives a neighborhood on which (g) has the same strict sign as (g(0)).
- **ZF-2b:** if (f\ge0) near zero, (f(r)=r^m g(r)) near zero, and (g(0)\ne0), then (g(0)>0), using a positive witness in the neighborhood.
- **ZF-2c:** if (g>0) near zero and (f\ge0) near zero with the factorization, then (m) is even, using a negative witness.
- **ZF-2d:** combine the previous lemmas into the target theorem.

Do not hide the positive/negative witness construction inside an unproved assumption. Verify the exact pinned Mathlib filter APIs before using them. If a helper lemma is not yet formalized, record it as open rather than weakening the theorem.

## Boundaries

- The analytic factorization theorem currently in Lean supplies (g) analytic and (g(0)\ne0), but not the sign or parity conclusions.
- The nonnegative-branch derivative theorem is not a substitute for ZF-2.
- The conclusion is pointwise in the base parameter. It does not establish a common order (m), a uniform positive lower bound for (g(0,u)), or compact-neighborhood estimates in (u).
- The identically-zero analytic branch is excluded by the nontriviality assumption and must be handled separately under ZF-8.
- No entropy derivative at the zero branch is claimed by this document.
