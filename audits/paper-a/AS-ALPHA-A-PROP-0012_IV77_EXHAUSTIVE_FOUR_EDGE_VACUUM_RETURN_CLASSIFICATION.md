# IV-77 — Exhaustive classification of four edge operations returning to vacuum

## Claim and assumptions
For a simple loopless graph (no parallel edges), a multiset of four edge operations returns an x-basis spin-flip state to vacuum exactly when every vertex has even incidence degree in the four-edge multigraph (degrees count multiplicity).

## Proof
Applying edge (u,v) toggles u and v. After four operations, each vertex is flipped iff its total incidence count is odd. The final state is vacuum iff all incidence counts are even.

Partition multiplicities of four edge occurrences:
- 4: support one edge e, yielding e^4; every vertex degree is even.
- 3+1: the odd-multiplicity support consists of two distinct edges, which cannot form an even-degree simple graph; impossible.
- 2+2: two distinct edges e,f each occur twice; all degrees are even, regardless of whether e,f are adjacent or disjoint.
- 2+1+1: odd-multiplicity support has two distinct edges; it cannot have all degrees even; impossible.
- 1+1+1+1: four distinct edges must form a simple even-degree graph. A simple graph with four edges and all degrees even must be a 4-cycle; no other support is possible.

Thus the complete multiset classification is e^4, e^2 f^2, and a four-distinct-edge simple C4. This is a classification of multisets, not of weighted denominator contributions.

## Ordered-sequence counts and intermediate vacuum
- e^4: 1 order; intermediate flip sets after steps 1–3 are nonempty.
- e^2 f^2: 6 orders total; 2 orders place identical edges first and return to vacuum at step 2, so only 4 orders have all three intermediate states nonvacuum. In the four valid orders, step 3 is nonvacuum.
- C4 with four distinct edges: 24 orders; all have nonvacuum intermediate states at steps 1,2,3.

## Limits
This parity proof does not calculate energy denominators, raw resolvent weights, normalization corrections, or coefficients. It assumes a simple loopless graph; multigraphs with parallel edges require a separate statement. It is analytic/combinatorial only. No runtime code, numerical diagonalization, or Lean proof is claimed.