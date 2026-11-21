# IV-70 — Independent Parity Graph Suite

## Scope
Run two structurally different endpoint/intermediate parity implementations across seven small graphs: single edge, two disjoint edges, path of 3 vertices, triangle, square, star with 3 leaves, and path of 4 vertices. Each implementation exhaustively enumerates all ordered 4-edge tuples.

## Results
Both methods agree for every graph. Exact totals and classifications are recorded in the accompanying JSON. This validates tuple counts, flip-set parity, endpoint flip-size histograms, and reducible/irreducible vacuum-return classification for this suite.

## Limitations
This is combinatorial verification only. It does not validate perturbative signs, energy denominators, vacuum subtraction, energy coefficients, mutual information, or Proposition 0012. No Lean proof is claimed.
