#!/usr/bin/env python3
"""IV-85 symbolic recurrence cross-check of the proposed general graph E4 formula."""
from collections import defaultdict
from itertools import combinations
import sympy as sp

def recurrence_e4(edges):
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
    energy = [sp.Integer(0)]
    for k in range(1, 5):
        vp = apply_v(psi[k-1])
        energy.append(sp.expand(vp.get(0, 0)))
        inside = {m: c for m, c in vp.items() if m}
        for j in range(1, k):
            for m, c in psi[k-j].items():
                if m:
                    inside[m] = inside.get(m, 0) - energy[j] * c
        psi.append({m: sp.cancel(-c/(2*h*m.bit_count())) for m,c in inside.items() if m and c})
    return h, J, sp.factor(energy[4])

def proposed_formula(edges):
    h = sp.symbols('h', positive=True)
    J = sp.symbols(f'J0:{len(edges)}')
    adjacent_pairs = [J[i]**2 * J[j]**2
        for i, j in combinations(range(len(edges)), 2)
        if set(edges[i]) & set(edges[j])
    cycle_products = []
    for ids in combinations(range(len(edges)), 4):
        chosen = [edges[i] for i in ids]
        degree = defaultdict(int)
        adjacency = defaultdict(set)
        for u, v in chosen:
            degree[u] += 1; degree[v] += 1
            adjacency[u].add(v); adjacency[v].add(u)
        if len(degree) != 4 or any(d != 2 for d in degree.values()):
            continue
        start = next(iter(degree))
        seen = {start}; stack = [start]
        while stack:
            node = stack.pop()
            for nxt in adjacency[node]:
                if nxt not in seen:
                    seen.add(nxt); stack.append(nxt)
        if len(seen) == 4:
            cycle_products.append(sp.prod(J[i] for i in ids)
    numerator = sum(x**4 for x in J) - 2*sum(adjacent_pairs) - 20*sum(cycle_products)
    return sp.factor(numerator/(64*h**3))

def check_graph(edges, label):
    _, _, e4 = recurrence_e4(edges)
    formula = proposed_formula(edges)
    assert sp.simplify(e4-formula) == 0, (label, edges, e4, formula)
    print(f'PASS: {label}; vertices={len(set(v for e in edges for v in e))}; edges={len(edges)}')

def main():
    # Exhaust all simple graphs on at most four labeled vertices.
    checked = 0
    for n in range(1, 5):
        pool = list(combinations(range(n), 2))
        for bits in range(1 << len(pool)):
            edges = [e for i, e in enumerate(pool) if (bits >> i) & 1]
            check_graph(edges, f'exhaustive_n{n}_mask{bits}')
            checked += 1
    # Additional structured graphs on five vertices.
    examples = {
        'path_p5': [(0,1),(1,2),(2,3),(3,4)],
        'cycle_c5': [(0,1),(1,2),(2,3),(3,4),(4,0)],
        'star_k14': [(0,1),(0,2),(0,3),(0,4)],
        'square_plus_tail': [(0,1),(1,2),(2,3),(3,0),(3,4)],
        'triangle_two_leaves': [(0,1),(1,2),(2,0),(0,3),(1,4)],
        'two_disjoint_paths': [(0,1),(1,2),(3,4)],
    }
    for name, edges in examples.items():
        check_graph(edges, name)
        checked += 1
    print('TOTAL VERIFIED GRAPH INSTANCES:', checked)

if __name__ == '__main__':
    main()
