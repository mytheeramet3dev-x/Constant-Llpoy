#!/usr/bin/env python3
"""IV-90 reduced-state spectral validation for a 3-spin open path."""
import numpy as np
from numpy.linalg import eigh

def partial_trace_middle(rho):
    tensor = rho.reshape(2,2,2,2,2,2)
    return np.einsum('abcAbC->acAC', tensor).reshape(4,4)

def entropy(rho):
    eig = np.linalg.eigvalsh(rho)
    if eig.min() < -1e-10:
        raise ValueError(f"negative eigenvalue {eig.min()}")
    eig = np.clip(eig, 0, 1)
    eig = eig[eig > 1e-15]
    return float(-np.sum(eig*np.log(eig)))

def calculate(J12,J23,h=1.0):
    sx=np.array([[0.,1.],[1.,0.]])
    sz=np.diag([1.,-1.]); I=np.eye(2)
    H=(-J12*np.kron(np.kron(sz,sz),I)
       -J23*np.kron(np.kron(I,sz),sz)
       -h*(np.kron(np.kron(sx,I),I)+np.kron(np.kron(I,sx),I)
             +np.kron(np.kron(I,I),sx)))
    vals,vecs=eigh(H); psi=vecs[:,0]; rho=np.outer(psi,psi.conj())
    rho13=partial_trace_middle(rho)
    r=rho13.reshape(2,2,2,2)
    rho1=np.einsum('acAc->aA',r)
    rho3=np.einsum('acaC->cC',r)
    mi=entropy(rho1)+entropy(rho3)-entropy(rho13)
    metrics=(np.trace(rho).real,np.trace(rho13).real,
             np.linalg.norm(rho13-rho13.conj().T),
             np.linalg.eigvalsh(rho13).min(),mi)
    assert abs(metrics[0]-1)<1e-10 and abs(metrics[1]-1)<1e-10
    assert metrics[2]<1e-10 and metrics[3]>=-1e-10 and metrics[4]>=-1e-10
    return vals[0],np.linalg.eigvalsh(rho13),metrics

if __name__=='__main__':
    print('J12 J23 ground_energy rho13_eigs MI')
    for a,b in [(0.01,0.01),(0.01,0.03),(0.03,0.01),(0.01,0.10),(0.03,0.10),(0.10,0.10)]:
        E,eigs,m=calculate(a,b)
        print(f'{a:.4g} {b:.4g} {E:.12g} {eigs} {m[-1]:.12g}')
