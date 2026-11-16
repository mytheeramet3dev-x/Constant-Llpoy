#!/usr/bin/env python3
"""Independent reduced-Dicke-basis perturbation diagnostic for the uniform TFIM.

Requires SymPy. This uses the fully permutation-symmetric spin sector rather
than the computational complement-orbit basis used by the companion script.
"""
from __future__ import annotations
import argparse
import sympy as sp

def dicke_even_small_eigenvalue_coefficient(n: int, order: int = 4):
    eps=sp.symbols("eps", positive=True)
    columns=[]
    labels=[]
    for k in range(n//2+1):
        if n%2==0 and k==n//2:
            vec=sp.zeros(n+1,1)
            vec[k]=1
        else:
            vec=sp.zeros(n+1,1)
            vec[k]=1/sp.sqrt(2)
            vec[n-k]=1/sp.sqrt(2)
        columns.append(vec)
        labels.append(k)
    transform=sp.Matrix.hstack(*columns)
    h0_full=sp.diag(*[
        -(((n-2*k)**2-n)//2) for k in range(n+1)
    ])
    v_full=sp.zeros(n+1)
    for k in range(n):
        value=-sp.sqrt((k+1)*(n-k))
        v_full[k,k+1]=value
        v_full[k+1,k]=value

    h0=transform.T*h0_full*transform
    v=transform.T*v_full*transform
    dim=h0.rows
    e0=-n*(n-1)//2
    coeff=[sp.zeros(dim,1) for _ in range(order+1)]
    coeff[0][0]=1
    energy=[sp.Integer(0)]*(order+1)
    gaps=[sp.simplify(h0[i,i]-e0) for i in range(dim)]

    for degree in range(1,order+1):
        energy[degree]=sp.simplify((v*coeff[degree-1])[0])
        rhs=v*coeff[degree-1]
        for k in range(1,degree+1):
            rhs-=energy[k]*coeff[degree-k]
        for i in range(1,dim):
            coeff[degree][i]=sp.simplify(-rhs[i]/gaps[i])

    dicke=[sp.Integer(0)]*(n+1)
    for j,k in enumerate(labels):
        amplitude=sum(coeff[p][j]*eps**p for p in range(order+1))
        if n%2==0 and k==n//2:
            dicke[k]=amplitude
        else:
            dicke[k]=amplitude/sp.sqrt(2)
            dicke[n-k]=amplitude/sp.sqrt(2)

    psi=[]
    for state in range(1<<n):
        weight=state.bit_count()
        psi.append(dicke[weight]/sp.sqrt(sp.binomial(n,weight)))
    norm2=sp.series(sum(z*z for z in psi),eps,0,order+1).removeO()
    norm_factor=sp.series(1/sp.sqrt(norm2),eps,0,order+1).removeO()
    psi=[sp.series(z*norm_factor,eps,0,order+1).removeO() for z in psi]

    rho=sp.zeros(4)
    for a in range(1<<n):
        ia=((a>>0)&1)*2+((a>>1)&1)
        for b in range(1<<n):
            if (a>>2)==(b>>2):
                ib=((b>>0)&1)*2+((b>>1)&1)
                rho[ia,ib]+=psi[a]*psi[b]
    rho=rho.applyfunc(
        lambda z:sp.series(z,eps,0,order+1).removeO().expand()
    )

    aa,bb,qq,cc=rho[0,0],rho[0,1],rho[0,3],rho[1,1]
    upper=aa+qq
    offdiag=2*bb
    lower=2*cc
    disc=sp.sqrt((upper-lower)**2+4*offdiag**2)
    small=sp.series(
        (upper+lower-disc)/2,eps,0,order+1
    ).removeO().expand()
    return sp.factor(small.coeff(eps,4))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n",nargs="+",type=int,default=[4,5,6,7,8,9,10])
    args=parser.parse_args()
    for n in args.n:
        coefficient=dicke_even_small_eigenvalue_coefficient(n)
        print(f"N={n}: [epsilon^4] lambda_small = {coefficient}")

if __name__=="__main__":
    main()
