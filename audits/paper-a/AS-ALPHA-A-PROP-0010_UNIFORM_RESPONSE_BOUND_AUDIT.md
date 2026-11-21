# Paper A PROP-0010 — Uniform-response upper bound and non-implication audit

- Date: 2026-11-21
- Frozen source: Paper A Section 5.1, commit 8deb7de4a49cb2060720246b7101820ee7e08c91
- Verdict: **ANALYTIC PASS for the stated algebra, conditional on g>0 and differentiability; no Lean formalization.**

## Definition
At the uniform coupling fixed point,
[
F(J;g,h)=gI_{12}(J,h)-J,quad g>0,quad F(J_*)=0.
]
Assuming (I_{12}) differentiable in the same uniform-coupling coordinate (J),
[
F_J(J_*)=g,partial_J I_{12}(J_*,h)-1.
]

## Upper bound
(F_J(J_*)<0) is equivalent, by rearrangement and (g>0), to
[
partial_J I_{12}(J_*,h)<1/g.
]
The derivative here is the response under uniform variation of all edge couplings according to the source's scalar coordinate, not a single-edge derivative.

## Non-implication counterexample
Let (g=2) and (partial_J I_{12}=1/4). Then (F_J=2(1/4)-1=-1/2<0), but the response derivative is positive. Thus (F_J<0) does not imply (partial_J I_{12}<0). Conversely, (partial_J I_{12}<0) gives (F_J<-1), a stronger condition than merely negative (F_J).

## Picard stability distinction
For (T(J)=gI_{12}(J,h)), (T'=1+F_J). Local linear attraction requires (|T'|<1), equivalent to (-2<F_J<0). Hence (F_J<0) alone is not sufficient for discrete Picard stability. The paper's distinction is algebraically correct.

## Scope / caveats
- The calculation is exact algebra, not a model-specific numerical or analytic proof of response sign.
- Differentiability and the matching uniform-coordinate convention are prerequisites.
- No direct Lean formalization for PROP-0010 was established in this audit.
