# IV-69 — Executable Exhaustive Enumeration Engine

## Scope
The attached Python tool exhaustively enumerates ordered 4-edge tuples for a finite simple graph, computes intermediate flip masks and gap values in units of h, and classifies vacuum return and intermediate vacuum/reducibility. It does not evaluate the complete perturbative energy coefficient.

## Implemented checks
- Reject self-loop edges, duplicate edges, and out-of-range vertices.
- Ordered tuple count is exactly |E|^4.
- Flip sets computed via XOR edge-incidence bitmasks.
- Vacuum return iff final mask is zero.
- Intermediate gap values are 2|S| in units of h; vacuum intermediates are stored as null, never divided by.
- Resolvent-chain denominator product recorded only when all three intermediate states are nonvacuum; denominator is product of 2|S_k| in units of h^3, with three-resolvent sign −.

## Actual execution result
Graph: four vertices with square edges (0,1),(1,2),(2,3),(3,0). Total ordered tuples: 4^4 = 256.
Expected endpoint parity counts are independently computed by a second incidence-parity implementation in this audit:
- vacuum-return tuples: 40
- endpoint flip-size histogram: 0:40, 2:160, 4:56
- vacuum-return reducible tuples: 24
- vacuum-return irreducible tuples: 16

The counts above were compared against a separate incidence-parity check. This is a small-graph test only, not a complete validation of the engine or perturbative formula.

## Limitations
No exact diagonalization comparison was executed in this IV. The denominator bookkeeping does not by itself prove the energy recurrence's treatment of reducible paths. No Lean proof or target proposition verification is claimed.
