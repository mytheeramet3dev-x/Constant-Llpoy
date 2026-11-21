#!/usr/bin/env python3
"""IV-83 symbolic raw-chain vs complete E4 cross-check for six finite graphs."""
from collections import Counter, defaultdict
from itertools import product
import sympy as sp

def complete_energy(edges):
    h = sp.symbols('h', positive=True)
    J = sp.symbols(f'J0:{len(edges)}')
    masks = [(1 << u) | (1 << v) for u, v in edges]
    def apply_v(vec):
        out = defaultdict(lambda: 0)
        for mask, coeff in vec.items():
            for i, em in enumerate(masks):
                out[mask ^ em] -= coeff * J[i]
        return {m: sp.expand(c) for m, c in out.items() if c != 0}
    psi = [{0: sp.Integer(1)}]
    E = [sp.Integer(0)]
    for k in range(1, 5):
        vp = apply_v(psi[k-1])
        E.append(sp.expand(vp.get(0, 0)))
        inside = {m: c for m, c in vp.items() if m}
        for j in range(1, k):
            for m, c in psi[k-j].items():
                if m:
                    inside[m] = inside.get(m, 0) - E[j] * c
        psi.append({m: sp.cancel(-c/(2*h*m.bit_count())) for m,c in inside.items() if m and c})
    return h, J, [sp.factor(x) for x in E[1:]]

def raw_closed_chains(edges):
    h = sp.symbols('h', positive=True)
    J = sp.symbols(f'J0:{len(edges)}')
    masks = [(1 << u) | (1 << v) for u, v in edges]
    raw = 0
    count = 0
    denominator_hist = Counter()
    for seq in product(range(len(edges)), repeat=4):
        state = 0
        sizes = []
        valid = True
        for t, eid in enumerate(seq):
            state ^= masks[eid]
            if t < 3:
                if state == 0:
                    valid = False
                    break
                sizes.append(state.bit_count())
        if valid and state == 0:
            count += 1
            denominator_hist[tuple(sizes)] += 1
            raw -= sp.prod(J[i] for i in seq)/(8*h**3*sp.prod(sizes))
    return sp.factor(raw), count, denominator_hist

def main():
    examples = {
        'single_edge': [(0,1)],
        'triangle': [(0,1),(1,2),(0,2)],
        'square_c4': [(0,1),(1,2),(2,3),(3,0)],
        'path_p4': [(0,1),(1,2),(2,3)],
        'star_k13': [(0,1),(0,2),(0,3)],
        'two_disjoint_edges': [(0,1),(2,3)],
    }
    for name, edges in examples.items():
        h, J, E = complete_energy(edges)
        raw, count, hist = raw_closed_chains(edges)
        correction = sp.factor(E[3] - raw)
        predicted = sp.factor(sum(x**2 for x in J)**2/(64*h**3))
        assert sp.simplify(correction-predicted) == 0, name
        print(f'[{name}]')
        print('  raw_chain_count =', count)
        print('  raw_E4 =', raw)
        print('  complete_E4 =', E[3])
        print('  recurrence_correction =', correction)
        print('  correction_matches_square_sum = PASS')
        print('  denominator_hist =', dict(hist))

if __name__ == '__main__':
    main()
