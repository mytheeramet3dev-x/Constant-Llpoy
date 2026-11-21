#!/usr/bin/env python3
"""IV-89: validation-only exact diagonalization for unequal-coupling 3-spin path MI.

The implementation uses an 8x8 Hamiltonian, constructs rho_13 by tracing spin 2,
then validates trace, Hermiticity, positivity, marginal traces, and MI >= 0.
This is exploratory numerical evidence, not an asymptotic proof.
"""
import numpy as np
from numpy.linalg import eigh

def partial_trace_middle(rho):
    r = rho.reshape(2, 2, 2, 2, 2, 2)
    return np.einsum('abcAbC->acAC', r).reshape(4, 4)

def entropy(r):
    vals = np.linalg.eigvalsh(r)
    if vals.min() < -1e-10:
        raise ValueError(f"non-PSD eigenvalue: {vals.min()}")
    vals = np.clip(vals, 0, 1)
    vals = vals[vals > 1e-15]
    return float(-np.sum(vals * np.log(vals)))

def evaluate(j12, j23, h=1.0):
    sx = np.array([[0., 1.], [1., 0.]])
    sz = np.diag([1., -1.])
    I = np.eye(2)
    H = (-j12*np.kron(np.kron(sz, sz), I)
         -j23*np.kron(np.kron(I, sz), sz)
         -h*(np.kron(np.kron(sx, I), I)
              +np.kron(np.kron(I, sx), I)
              +np.kron(np.kron(I, I), sx)))
    eigvals, eigvecs = eigh(H)
    psi = eigvecs[:, 0]
    rho = np.outer(psi, psi.conj())
    rho13 = partial_trace_middle(rho)
    r = rho13.reshape(2, 2, 2, 2)
    rho1 = np.einsum('acAc->aA', r)
    rho3 = np.einsum('acaC->cC', r)
    mi = entropy(rho1) + entropy(rho3) - entropy(rho13)
    checks = {
        "trace_full": float(np.trace(rho).real),
        "trace_rho13": float(np.trace(rho13).real),
        "trace_rho1": float(np.trace(rho1).real),
        "trace_rho3": float(np.trace(rho3).real),
        "hermiticity_error": float(np.linalg.norm(rho13-rho13.conj().T)),
        "min_eigen_rho13": float(np.linalg.eigvalsh(rho13).min()),
        "mi": float(mi),
    }
    assert all(abs(checks[k]-1.0) < 1e-10 for k in
               ("trace_full", "trace_rho13", "trace_rho1", "trace_rho3"))
    assert checks["hermiticity_error"] < 1e-10
    assert checks["min_eigen_rho13"] >= -1e-10
    assert checks["mi"] >= -1e-10
    return checks

if __name__ == "__main__":
    pairs = [(0.01,0.10),(0.03,0.10),(0.10,0.03),(0.10,0.20),
             (0.20,0.10),(0.01,0.01),(0.01,0.03),(0.03,0.01)]
    for a,b in pairs:
        out = evaluate(a,b)
        print(f"{a:.3f} {b:.3f} MI={out['mi']:.15g} "
              f"MI/(a^2 b^2)={out['mi']/(a*a*b*b):.10g} "
              f"tr(rho13)={out['trace_rho13']:.12g} "
              f"minEig={out['min_eigen_rho13']:.3e}")
