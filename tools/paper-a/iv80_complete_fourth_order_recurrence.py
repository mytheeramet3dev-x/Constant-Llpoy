#!/usr/bin/env python3
"""IV-80: symbolic intermediate-normalized perturbation recurrence through E4.
Requires SymPy. Graph edges use zero-based vertex indices.
"""
import sympy as sp


def perturbation_energy(edges):
    h = sp.symbols("h", positive=True)
    J = sp.symbols(f"J0:{len(edges)}")

    def apply_V(vector):
        out = {}
        for mask, coeff in vector.items():
            for i, (u, v) in enumerate(edges):
                target = mask ^ (1 << u) ^ (1 << v)
                out[target] = out.get(target, 0) - coeff * J[i]
        return {mask: sp.expand(coeff) for mask, coeff in out.items() if coeff != 0}

    psi = [{0: sp.Integer(1)}]
    energy = [sp.Integer(0)]
    for k in range(1, 5):
        vpsi = apply_V(psi[k - 1])
        ek = sp.expand(vpsi.get(0, 0))
        energy.append(ek)
        inside = {mask: coeff for mask, coeff in vpsi.items() if mask}
        for j in range(1, k):
            for mask, coeff in psi[k - j].items():
                if mask:
                    inside[mask] = inside.get(mask, 0) - energy[j] * coeff
        psi_k = {
            mask: sp.cancel(-coeff / (2 * h * mask.bit_count()))
            for mask, coeff in inside.items()
            if mask
        }
        psi.append(psi_k)
    return [sp.factor(value) for value in energy[1:]]


def main():
    examples = {
        "single_edge": [(0, 1)],
        "triangle": [(0, 1), (1, 2), (0, 2)],
        "square_c4": [(0, 1), (1, 2), (2, 3), (3, 0)],
    }
    for name, edges in examples.items():
        print(f"[{name}] edges={edges}")
        for order, coefficient in enumerate(perturbation_energy(edges), start=1):
            print(f"E{order} = {coefficient}")


if __name__ == "__main__":
    main()
