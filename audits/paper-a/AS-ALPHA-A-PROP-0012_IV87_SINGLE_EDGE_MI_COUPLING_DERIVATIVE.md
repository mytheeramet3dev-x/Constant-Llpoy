# IV-87 — Single-edge MI coupling derivative

## Setup
Reuse IV-86 exact two-spin model and natural-log mutual information. Let q=2h/sqrt(4h^2+J^2), p=(1-q)/2, and I(J)=2[-p ln p-(1-p)ln(1-p)].

## Exact derivative
dp/dJ = J h/(4h^2+J^2)^(3/2).
dI/dJ = 2 ln((1-p)/p) dp/dJ
= 2 J h/(4h^2+J^2)^(3/2) ln((1+q)/(1-q)).
Equivalent exact expression is finite for J≠0; at J=0 define the continuous limit derivative 0.

## Weak-coupling asymptotic
From IV-86:
I(J)=J^2/(8h^2)[1-ln(J^2/(16h^2))]+O(J^4/h^4 ln(h/|J|)).
Differentiating the leading term:
dI/dJ= -J/(4h^2) ln(J^2/(16h^2)) + O(J^3/h^4 ln(h/|J|)).
This tends to 0 as J→0 but carries a logarithmic factor. The derivative is not represented by a regular power-series coefficient at zero.

## Limitations
This derivative is for the directly coupled two-spin model only. It is not the B or C response on a general graph, does not establish B-C, and does not prove Proposition 0012. No Lean verification claimed.
