# IV-60 — Executable Graph Enumeration and Canonicalization

**Status:** COMPUTATIONAL ENUMERATION EXECUTED / AMPLITUDE AUDIT OPEN  
**Scope:** Four pair-edge operations on an 8-vertex pool; exact combinatorial enumeration only.

## 1. Reproducible implementation

The pure-Python script `tools/paper-a/iv60_four_pair_edge_multigraph_enumeration.py` enumerates edge multisets and distinct ordered sequences. Weighted support graph classes are canonicalized component-wise by brute-force vertex permutations; multiplicities are retained. Summary JSON is at `audits/paper-a/IV60_ENUMERATION_SUMMARY.json`.

Run:
```bash
python tools/paper-a/iv60_four_pair_edge_multigraph_enumeration.py --output iv60_summary.json
```

## 2. Executed results

- Vertex pool: 8.
- Available pair edges: \(\binom82=28\).
- Edge multisets: \(\binom{28+4-1}{4}=31{,}465\).
- Unique ordered sequences: \(28^4=614{,}656\).
- Canonical weighted support classes: **23**.
- Ordered sequences with a vacuum intermediate at step 2 or 3: **31,360**.
- Endpoint flipped-count distribution over multisets: 0: 616; 2: 9,464; 4: 17,080; 6: 4,200; 8: 105.

Vacuum flag checks only steps 2 and 3. It is bookkeeping, not a perturbative correction.

## 3. Canonicalization

For four edge occurrences, each connected support component has at most five vertices. The script minimizes the weighted edge encoding over all permutations of each component, then sorts component encodings. This handles disconnected support graphs and preserves multiplicity.

The 23-class count is a computational result from this script. It does **not** provide perturbative denominators, path aggregation, normalization, reduced-density entries, or a proof of \(c_{vv}\).

## 4. Check identities

The script results satisfy:
- \(31{,}465=\binom{31}{4}\);
- \(614{,}656=28^4\);
- endpoint flip counts are even and at most 8.

## 5. Status

- Multiset enumeration: **EXECUTED**.
- Ordered sequence count: **EXECUTED**.
- Weighted-support canonicalization: **EXECUTED**.
- 23 classes: **COMPUTATIONAL RESULT**.
- Vacuum-intermediate flag: **EXECUTED**.
- Per-path denominator ledger: **NOT GENERATED**.
- Reducible-path corrections, normalized amplitudes, fourth-order reduced density, and \(c_{vv}\): **OPEN**.
- Lean verification: **NOT PERFORMED**.

This enumeration is combinatorial bookkeeping only; no physical proof claim is inferred.
