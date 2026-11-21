#!/usr/bin/env python3
"""IV-82: exhaustive raw fourth-order closed-chain enumeration on K8."""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter

N = 8
EDGES = list(combinations(range(N), 2))
MASKS = [(1 << u) | (1 << v) for u, v in EDGES]
MULTISETS = list(combinations_with_replacement(range(len(EDGES)), 4))

def classify(ms):
    occ = Counter(ms)
    if len(occ) == 2 and sorted(occ.values()) == [2, 2]:
        e1, e2 = occ.keys()
        return "adjacent_2plus2" if set(EDGES[e1]) & set(EDGES[e2]) else "disjoint_2plus2"
    if len(occ) == 4 and all(c == 1 for c in occ.values()):
        return "four_distinct_cycle"
    if len(occ) == 1:
        return "one_edge_fourfold"
    return "other_closed_pattern"

multiset_counts = Counter()
raw_valid_sequences = Counter()
raw_denominator_hist = Counter()
for ms in MULTISETS:
    endpoint = 0
    for eidx in ms:
        endpoint ^= MASKS[eidx]
    if endpoint:
        continue
    typ = classify(ms)
    multiset_counts[typ] += 1
    for seq in set(permutations(ms)):
        state = 0
        sizes = []
        valid = True
        for k, eidx in enumerate(seq):
            state ^= MASKS[eidx]
            if k < 3:
                if state == 0:
                    valid = False
                    break
                sizes.append(state.bit_count())
        if valid and state == 0:
            raw_valid_sequences[typ] += 1
            raw_denominator_hist[(typ, tuple(sizes))] += 1

assert len(EDGES) == 28
assert len(MULTISETS) == 31465
assert multiset_counts == Counter({
    "adjacent_2plus2": 168,
    "disjoint_2plus2": 210,
    "four_distinct_cycle": 210,
    "one_edge_fourfold": 28,
})
assert raw_valid_sequences == Counter({
    "adjacent_2plus2": 672,
    "disjoint_2plus2": 840,
    "four_distinct_cycle": 5040,
})
assert raw_denominator_hist[("adjacent_2plus2", (2, 2, 2))] == 672
assert raw_denominator_hist[("disjoint_2plus2", (2, 4, 2))] == 840
assert raw_denominator_hist[("four_distinct_cycle", (2, 2, 2))] == 3360
assert raw_denominator_hist[("four_distinct_cycle", (2, 4, 2))] == 1680

print("K8 edge pool:", len(EDGES))
print("4-edge multisets:", len(MULTISETS))
print("closed multiset counts:", dict(multiset_counts))
print("valid raw non-vacuum sequences:", dict(raw_valid_sequences))
print("denominator-size histogram:", dict(raw_denominator_hist))
