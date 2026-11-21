# IV-82 — Executable raw fourth-order chain enumeration on K8

## Purpose
Reproduce the IV-79 closed multiset counts and valid non-vacuum raw ordered-sequence counts, and verify denominator-size patterns with an executable Python script.

## Method
The script enumerates all 28 edges of K8 and all 31,465 multisets of four edge occurrences. Endpoint closure is checked via vertex-bitmask XOR. Each unique ordered permutation is tested for vacuum avoidance at prefix lengths 1, 2, and 3. Valid closed sequences are classified by edge multiplicities and pair adjacency. Assertions verify all expected totals and denominator-size histograms.

## Runtime results
- K8 edge pool: 28
- Four-edge multisets: 31,465
- Closed multiset counts: one edge fourfold = 28; adjacent 2+2 = 168; disjoint 2+2 = 210; four distinct cycle = 210.
- Valid raw non-vacuum sequences: adjacent 2+2 = 672; disjoint 2+2 = 840; C4 = 5,040.
- Denominator size histogram: adjacent 2+2 (2,2,2) = 672; disjoint 2+2 (2,4,2) = 840; C4 (2,2,2) = 3,360; C4 (2,4,2) = 1,680.

This independently reproduces IV-79's multiset counts (588 valid closed classes, excluding the 28 e^4 endpoint-closed but raw-invalid classes) and expands it to sequence counts. Note 588 is a count of multiset classes, not ordered walks.

## Limitations
This confirms combinatorial endpoint and raw-chain classification only. It does not calculate symbolic energy coefficients, full recurrence corrections, numerical diagonalization, B-C response, Proposition 0012, or Lean proof.
