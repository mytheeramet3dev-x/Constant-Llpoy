#!/usr/bin/env python3
"""High-precision full-Hilbert-space finite-difference check of B-C.

Requires mpmath. This is numerical diagnostic evidence only, not a proof.
"""
from __future__ import annotations
import argparse
import mpmath as mp

def mutual_information(n: int, h, edge_changes=None):
    edge_changes=edge_changes or {}
    dim=1<<n
    couplings={}
    for i in range(n):
        for j in range(i+1,n):
            couplings[(i,j)]=mp.mpf(1)+edge_changes.get((i,j),mp.mpf(0))
    H=mp.matrix(dim)
    for state in range(dim):
        z=[1 if ((state>>i)&1)==0 else -1 for i in range(n)]
        diagonal=mp.mpf(0)
        for i in range(n):
            for j in range(i+1,n):
                diagonal-=couplings[(i,j)]*z[i]*z[j]
        H[state,state]=diagonal
        for i in range(n):
            H[state,state^(1<<i)] += -h

    eigenvalues,eigenvectors=mp.eigsy(H)
    psi=[eigenvectors[i,0] for i in range(dim)]

    def reduced_state(sites):
        rho=mp.matrix(1<<len(sites))
        environment=[i for i in range(n) if i not in sites]
        def local_index(state):
            value=0
            for bit,site in enumerate(sites):
                value|=((state>>site)&1)<<bit
            return value
        for a in range(dim):
            ia=local_index(a)
            for b in range(dim):
                if all(((a>>site)&1)==((b>>site)&1) for site in environment):
                    rho[ia,local_index(b)]+=psi[a]*psi[b]
        return rho

    def entropy(rho):
        vals=mp.eigsy(rho,eigvals_only=True)
        total=mp.mpf(0)
        for value in vals:
            if value>mp.mpf("1e-40"):
                total-=value*mp.log(value)
        return total

    return (
        entropy(reduced_state([0]))
        +entropy(reduced_state([1]))
        -entropy(reduced_state([0,1]))
    )

def estimate_b_minus_c(n: int, h, step):
    shared=(0,2)   # J_13
    disjoint=(2,3) # J_34
    def derivative(edge):
        plus=mutual_information(n,h,{edge:step})
        minus=mutual_information(n,h,{edge:-step})
        return (plus-minus)/(2*step)
    b=derivative(shared)
    c=derivative(disjoint)
    return b-c,b,c

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n",nargs="+",type=int,default=[4,5,6])
    parser.add_argument("--h",nargs="+",default=["0.2","0.1","0.05"])
    parser.add_argument("--step",default="1e-4")
    parser.add_argument("--dps",type=int,default=50)
    args=parser.parse_args()
    mp.mp.dps=args.dps
    step=mp.mpf(args.step)
    for n in args.n:
        for h_text in args.h:
            h=mp.mpf(h_text)
            difference,b,c=estimate_b_minus_c(n,h,step)
            leading=h**2/(n-1)**3
            print(
                f"N={n} h={h_text} B-C={mp.nstr(difference,18)} "
                f"leading={mp.nstr(leading,18)} "
                f"ratio={mp.nstr(difference/leading,14)}"
            )

if __name__=="__main__":
    main()
