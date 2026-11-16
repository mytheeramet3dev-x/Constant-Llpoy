#!/usr/bin/env python3
"""High-precision full-Hilbert-space weak-coupling check of B-C.

Requires mpmath. Numerical diagnostic only; not a proof.
"""
from __future__ import annotations
import argparse
import mpmath as mp

def mutual_information(n: int, J, h, edge_changes=None):
    edge_changes=edge_changes or {}
    dim=1<<n
    couplings={(i,j):J+edge_changes.get((i,j),mp.mpf(0))
               for i in range(n) for j in range(i+1,n)}
    H=mp.matrix(dim)
    for state in range(dim):
        z=[1 if ((state>>i)&1)==0 else -1 for i in range(n)]
        diagonal=mp.mpf(0)
        for i in range(n):
            for j in range(i+1,n):
                diagonal-=couplings[(i,j)]*z[i]*z[j]
        H[state,state]=diagonal
        for i in range(n):
            H[state,state^(1<<i)]-=h
    values,vectors=mp.eigsy(H)
    psi=[vectors[i,0] for i in range(dim)]

    def reduced_state(sites):
        rho=mp.matrix(1<<len(sites))
        environment=[i for i in range(n) if i not in sites]
        def local_index(state):
            value=0
            for bit,site in enumerate(sites):
                value|=((state>>site)&1)<<bit
            return value
        for a in range(dim):
            for b in range(dim):
                if all(((a>>site)&1)==((b>>site)&1) for site in environment):
                    rho[local_index(a),local_index(b)]+=psi[a]*psi[b]
        return rho

    def entropy(rho):
        eigs=mp.eigsy(rho,eigvals_only=True)
        total=mp.mpf(0)
        for value in eigs:
            if value>mp.mpf("1e-45"):
                total-=value*mp.log(value)
        return total

    return (
        entropy(reduced_state([0]))
        +entropy(reduced_state([1]))
        -entropy(reduced_state([0,1]))
    )

def estimate(n: int, J, h, step):
    shared=(0,2)   # J_13
    disjoint=(2,3) # J_34
    def derivative(edge):
        plus=mutual_information(n,J,h,{edge:step})
        minus=mutual_information(n,J,h,{edge:-step})
        return (plus-minus)/(2*step)
    return derivative(shared)-derivative(disjoint)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n",nargs="+",type=int,default=[4,5,6])
    parser.add_argument("--J",nargs="+",default=["0.005","0.001"])
    parser.add_argument("--h",default="1")
    parser.add_argument("--relative-step",default="1e-4")
    parser.add_argument("--dps",type=int,default=60)
    args=parser.parse_args()
    mp.mp.dps=args.dps
    h=mp.mpf(args.h)
    for n in args.n:
        coefficient=mp.log(mp.mpf(2)*(n-2)/(n-1))/8
        for J_text in args.J:
            J=mp.mpf(J_text)
            value=estimate(n,J,h,J*mp.mpf(args.relative_step))
            leading=J/(h*h)*coefficient
            print(
                f"N={n} J/h={mp.nstr(J/h,10)} "
                f"B-C={mp.nstr(value,18)} "
                f"leading={mp.nstr(leading,18)} "
                f"ratio={mp.nstr(value/leading,14)}"
            )

if __name__=="__main__":
    main()
