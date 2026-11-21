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
Graph: four vertices with square edges (0,1),(1,2),(2,3),(3,0). Total ordered tuples: 4^4 = 256. The engine was executed locally, and the endpoint counts were checked with a separate incidence-parity calculation:
- vacuum-return tuples: 64
- endpoint flip-size histogram: 0:64, 2:128, 4:64
- vacuum-return reducible tuples: 16
- vacuum-return irreducible tuples: 48

Both implementations matched exactly. This is a small-graph test only, not a complete validation of the engine or perturbative formula.

## Limitations
No exact diagonalization comparison was executed in this IV. The denominator bookkeeping does not by itself prove the energy recurrence's treatment of reducible paths. No Lean proof or target proposition verification is claimed.
