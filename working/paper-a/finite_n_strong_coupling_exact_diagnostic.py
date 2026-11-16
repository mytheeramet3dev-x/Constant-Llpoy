#!/usr/bin/env python3
"""Exact-rational finite-N perturbation diagnostic for the uniform TFIM pair state.

Requires SymPy. This is a reproducibility diagnostic, not a proof of a
uniform-in-N theorem and not a replacement for general-edge derivative bounds.
"""
from __future__ import annotations
import argparse
import sympy as sp

def even_parity_orbits(n: int):
    full = (1 << n) - 1
    return sorted({min(s, full ^ s) for s in range(1 << n)})

def perturbative_ground_state(n: int, order: int = 4):
    eps = sp.symbols("eps", positive=True)
    reps = even_parity_orbits(n)
    index = {s: i for i, s in enumerate(reps)}
    dim = len(reps)
    e0 = -n * (n - 1) // 2
    h0 = sp.diag(*[
        -(((n - 2 * s.bit_count()) ** 2 - n) // 2)
        for s in reps
    ])
    v = sp.zeros(dim)
    full = (1 << n) - 1
    for row, state in enumerate(reps):
        for bit in range(n):
            target = state ^ (1 << bit)
            orbit = min(target, full ^ target)
            v[row, index[orbit]] -= 1

    coeff = [sp.zeros(dim, 1) for _ in range(order + 1)]
    coeff[0][0] = 1
    energy = [sp.Integer(0)] * (order + 1)
    gaps = [h0[i, i] - e0 for i in range(dim)]
    for degree in range(1, order + 1):
        energy[degree] = (v * coeff[degree - 1])[0]
        rhs = v * coeff[degree - 1]
        for k in range(1, degree + 1):
            rhs -= energy[k] * coeff[degree - k]
        for i in range(1, dim):
            coeff[degree][i] = sp.cancel(-rhs[i] / gaps[i])

    raw = []
    for state in range(1 << n):
        orbit = min(state, full ^ state)
        idx = index[orbit]
        raw.append(sum(
            coeff[k][idx] * eps**k for k in range(order + 1)
        ) / sp.sqrt(2))
    norm2 = sp.series(sum(a * a for a in raw), eps, 0, order + 1).removeO()
    norm_factor = sp.series(1 / sp.sqrt(norm2), eps, 0, order + 1).removeO()
    psi = [
        sp.series(a * norm_factor, eps, 0, order + 1).removeO()
        for a in raw
    ]
    return eps, psi

def reduced_pair(n: int, eps, psi, order: int = 4):
    rho = sp.zeros(4)
    for a in range(1 << n):
        pair_a = ((a >> 0) & 1) * 2 + ((a >> 1) & 1)
        for b in range(1 << n):
            if (a >> 2) == (b >> 2):
                pair_b = ((b >> 0) & 1) * 2 + ((b >> 1) & 1)
                rho[pair_a, pair_b] += psi[a] * psi[b]
    return rho.applyfunc(
        lambda value: sp.series(value, eps, 0, order + 1).removeO().expand()
    )

def small_eigenvalue_coefficient(n: int, order: int = 4):
    eps, psi = perturbative_ground_state(n, order)
    rho = reduced_pair(n, eps, psi, order)
    a, b, q, c = rho[0, 0], rho[0, 1], rho[0, 3], rho[1, 1]
    upper, offdiag, lower = a + q, 2 * b, 2 * c
    disc = sp.sqrt((upper - lower) ** 2 + 4 * offdiag**2)
    small = sp.series(
        (upper + lower - disc) / 2, eps, 0, order + 1
    ).removeO().expand()
    return sp.factor(small.coeff(eps, 4)), small

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[4, 5, 6, 7, 8])
    parser.add_argument("--order", type=int, default=4)
    args = parser.parse_args()
    for n in args.n:
        if n < 4:
            raise SystemExit("This diagnostic is configured for N >= 4.")
        coefficient, expansion = small_eigenvalue_coefficient(n, args.order)
        proposed = sp.Rational(1, 8 * (n - 2) * (n - 1) ** 4)
        print(f"N={n}")
        print(f"  lambda_small = {expansion}")
        print(f"  [epsilon^4]  = {coefficient}")
        print(f"  proposed     = {proposed}")
        print(f"  exact_match  = {coefficient == proposed}")

if __name__ == "__main__":
    main()
