#!/usr/bin/env python3
"""IV-91 numerical check of leading path-3 endpoint MI asymptotics."""
import numpy as np
from numpy.linalg import eigh

def partial_trace_middle(rho):
    t=rho.reshape(2,2,2,2,2,2)
    return np.einsum('abcAbC->acAC',t).reshape(4,4)
def entropy(rho):
    ev=np.linalg.eigvalsh(rho); ev=np.clip(ev,0,1)
    return float(-sum(x*np.log(x) for x in ev if x>1e-15))
def exact(j1,j2,h=1.):
    sx=np.array([[0.,1.],[1.,0.]]); sz=np.diag([1.,-1.]); I=np.eye(2)
    H=-h*(np.kron(np.kron(sx,I),I)+np.kron(np.kron(I,sx),I)+np.kron(np.kron(I,I),sx))-j1*np.kron(np.kron(sz,sz),I)-j2*np.kron(np.kron(I,sz),sz)
    e,v=eigh(H); psi=v[:,0]; rho=np.outer(psi,psi.conj())
    r13=partial_trace_middle(rho); r=r13.reshape(2,2,2,2)
    r1=np.einsum('acAc->aA',r); r3=np.einsum('acaC->cC',r)
    mi=entropy(r1)+entropy(r3)-entropy(r13)
    traces=(np.trace(rho).real,np.trace(r13).real,np.trace(r1).real,np.trace(r3).real)
    assert all(abs(t-1)<1e-10 for t in traces)
    assert np.linalg.norm(r13-r13.conj().T)<1e-10
    assert np.linalg.eigvalsh(r13).min()>=-1e-10
    assert mi>=-1e-10
    return float(mi),float(np.linalg.eigvalsh(r13)[-2]),float(np.linalg.eigvalsh(r1)[0]),float(np.linalg.eigvalsh(r3)[0])
def leading(j1,j2,h=1.):
    x=j1*j1/(16*h*h); y=j2*j2/(16*h*h)
    return (x+y)*np.log(x+y)-x*np.log(x)-y*np.log(y)
if __name__=='__main__':
    print('J1 J2 exact_MI leading_MI ratio lambda_joint lambda_1 lambda_3')
    cases=[(1e-3,1e-3),(1e-3,2e-3),(1e-3,1e-2),(1e-2,1e-2),(1e-2,1e-1),(3e-2,1e-1)]
    for j1,j2 in cases:
        mi,lam,x1,x3=exact(j1,j2); pred=leading(j1,j2)
        print(f'{j1:.4g} {j2:.4g} {mi:.12g} {pred:.12g} {mi/pred:.9g} {lam:.12g} {x1:.12g} {x3:.12g}')
