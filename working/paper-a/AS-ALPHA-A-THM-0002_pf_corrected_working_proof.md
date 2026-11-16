# Constant Llapoy Working Proof — Perron–Frobenius Ground-State Simplicity

> Working correction derived for Constant Llapoy. This is not an edit to the frozen Absolute Symmetry manuscript or source snapshot.

## Statement

Let (N\ge1), (h>0), and (J_{ij}\in\mathbb R). On ((\mathbb C^2)^{\otimes N}), define
[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_{i=1}^N\sigma_i^x.
]
Then the lowest eigenvalue of (H) is simple. Its eigenvector can be chosen strictly positive in the computational (sigma^z) basis.

## Proof

In the computational basis the interaction term is diagonal and real. The only nonzero off-diagonal entries of (H) are (-h), joining basis configurations that differ at exactly one spin.

Since the matrix is finite-dimensional, choose (c\in\mathbb R) such that (c-H_{ss}\ge0) for every computational basis state (s). Set (K=cI-H). Then (K) is entrywise nonnegative: its diagonal entries are nonnegative and each single-spin-flip entry is (+h>0).

The graph of these positive off-diagonal entries is the (N)-dimensional hypercube, which is connected for every (N\ge1). Hence (K) is irreducible. By Perron–Frobenius, its spectral radius is a simple eigenvalue with a strictly positive eigenvector. As (K) is real symmetric, this spectral radius is its largest eigenvalue. Since (lambda_j(K)=c-E_j(H)), this eigenvalue corresponds to the smallest eigenvalue of (H). Thus the ground-state eigenvalue is simple and its eigenvector is strictly positive in the stated basis. \(\square\)

## Scope note

The proof uses no sign restriction on the real couplings (J_{ij}). The strict condition (h>0) is essential to the stated hypercube-connectivity argument. The result does not by itself establish reduced-density-matrix strict positivity, entropy regularity, or curvature nondegeneracy.
