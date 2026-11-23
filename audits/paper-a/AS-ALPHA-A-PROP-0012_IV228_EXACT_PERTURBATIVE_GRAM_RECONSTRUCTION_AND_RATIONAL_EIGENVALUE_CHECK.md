# IV-228 — Exact Perturbative Gram Reconstruction and Rational Eigenvalue Check

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, first-order retained-odd amplitude Gram under a single edge perturbation  
**Status:** EXACT MATRIX RECONSTRUCTION AND QUADRATIC COEFFICIENT DERIVED / HIGHER-ORDER PHYSICAL BLOCK OPEN / NOT LEAN-FORMALIZED  
**Scope:** Reconstruct the finite-dimensional first-order Gram matrix exactly for edge (u_{13}), derive its smallest eigenvalue expansion without relying only on a projection heuristic, and identify the precise limits.

## 1. Setup

Let (n=N-2ge2) be the number of environment coordinates. At uniform coupling, the two retained-site first-order amplitude rows are
[
a_2=\frac14\mathbf1_n,qquad a_1=\frac14\mathbf1_n+\frac u4e_3,
]
where (u=u_{13}) and the perturbed coordinate is one of the environment coordinates. This is the first-order amplitude-row model from IV-226, not the complete normalized ground-state amplitude vector.

The Gram entries are exactly
[
x=\langle a_1,a_1\rangle=\frac n{16}+\frac u8+\frac{u^2}{16},quad
y=\langle a_2,a_2\rangle=\frac n{16},quad
z=\langle a_1,a_2\rangle=\frac n{16}+\frac u{16}.
]
Thus
[
M_2(u)=\begin{pmatrix}x&z\\z&y\end{pmatrix}.
]

## 2. Exact eigenvalue expression

For this real symmetric (2\times2) Gram matrix,
[
\lambda_-(u)=\frac{x+y-\sqrt{(x-y)^2+4z^2}}2.
]
At (u=0), (M_2(0)=(n/16)\begin{pmatrix}1&1\\1&1\end{pmatrix}) has eigenvalues (n/8) and (0).

Expanding the exact expression at (u=0) gives
[
\lambda_-(u)=\frac{n-1}{32n}u^2+O(u^3)
=\frac1{32}\left(1-\frac1n\right)u^2+O(u^3).
]
Equivalently, substituting (n=N-2):
[
\boxed{\lambda_-(u)=\frac{N-3}{32(N-2)}u^2+O(u^3).}
]
The constant and linear terms are exactly zero.

## 3. Exact rational spot-checks

The coefficient \((n-1)/(32n)\) is rational for every integer (n\ge2). Values:
- (n=2) (N=4): (1/64).
- (n=3) (N=5): (1/48).
- (n=4) (N=6): (3/128).
- (n=6) (N=8): (5/192).
- (n=8) (N=10): (7/256).

These are substitutions into the exact derived coefficient, not floating-point fits. No numerical diagonalization is being claimed.

## 4. Geometric derivation cross-check

Let (d=(u/4)e_3) and let (a=(1/4)\mathbf1_n). Orthogonally project the row difference onto the complement of the common row:
[
d_\perp=\frac u4\left(e_3-\frac1n\mathbf1_n\right).
]
Then
[
\|d_\perp\|^2=\frac{u^2}{16}\left(1-\frac1n\right).
]
The small Gram eigenvalue at quadratic order is one-half of this quantity, yielding the same coefficient. The exact eigenvalue expansion and geometric projection therefore agree algebraically.

## 5. Disposition

- Exact (M_2(u)) entries: **DERIVED** under the stated row perturbation.
- Smallest-eigenvalue expansion and rational quadratic coefficient: **DERIVED**.
- Positive quadratic coefficient for all finite (N\ge4): **DERIVED**.
- Independent numerical diagonalization: **NOT PERFORMED**; no floating-point evidence is claimed.
- Physical odd-block higher-order terms, normalized subsystem reconstruction, full finite-r response, manuscript parameter mapping, global (B-C) sign, and Lean formalization: **OPEN**.

This record verifies the first-order Gram calculation only. It does not upgrade AS-ALPHA-A-PROP-0012 to VERIFIED.
