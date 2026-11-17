# Independent Mathematical Review — AS-ALPHA-A-THM-0002

- **Claim:** Finite-dimensional transverse-field Ising ground-state simplicity
- **Review date:** 2026-11-17
- **Repository boundary:** Constant Llapoy only
- **Review disposition:** MATHEMATICAL_PROOF_PASS; LEAN_FORMALIZATION_PENDING
- **Source manuscript status:** The original proof sentence remains incorrect as written and is not amended here.

## 1. Reviewed statement

For finite $N\ge 1$, $h>0$, and arbitrary finite real edge couplings $J_{ij}$, let
\[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_{i=1}^N\sigma_i^x
\]
on $(\mathbb C^2)^{\otimes N}$. The lowest eigenvalue of $H$ is simple. Its eigenvector can be chosen strictly positive in the computational $\sigma^z$ basis.

The statement is valid for all real $J_{ij}$, not merely ferromagnetic couplings. The couplings affect only diagonal entries in this basis.

## 2. Correct shifted matrix

Index the computational basis by bit strings $s\in\{0,1\}^N$. The interaction term is diagonal. The transverse-field term has matrix element $-h$ exactly when two bit strings differ in one coordinate, and zero for other off-diagonal pairs.

Since the basis is finite, define
\[
c=1+\max_{s\in\{0,1\}^N} H_{ss},\qquad K=cI-H.
\]
Then $K_{ss}\ge1$, and every nonzero off-diagonal entry of $K$ equals $+h>0$. All remaining entries are zero. Thus $K$ is entrywise nonnegative and real symmetric.

This sign is essential. The alternative shift $H+cI$ leaves the off-diagonal entries equal to $-h$ and does not produce an entrywise nonnegative matrix. The source proof's shift sentence is therefore false as written.

## 3. Irreducibility

The directed graph of positive off-diagonal entries of $K$ contains an edge between every pair of bit strings differing in exactly one bit. This is the $N$-dimensional hypercube graph.

For any two bit strings, flipping the coordinates on which they differ gives a finite path between them. Hence the graph is connected. Because every edge has strictly positive weight $h$, the nonnegative matrix $K$ is irreducible.

This argument includes $N=1$. It does not require any sign restriction on $J_{ij}$.

## 4. Perron–Frobenius conclusion and spectral ordering

For an irreducible finite nonnegative matrix, Perron–Frobenius gives a strictly positive eigenvector for the spectral radius and makes that eigenvalue simple. Since $K$ is real symmetric, its spectral radius is its largest eigenvalue. Therefore $\lambda_{\max}(K)$ is simple and has a strictly positive eigenvector.

If $E_{\min}$ is the smallest eigenvalue of $H$, then the eigenvalues of $K=cI-H$ are $c-E_j(H)$, so
\[
\lambda_{\max}(K)=c-E_{\min}.
\]
Consequently $E_{\min}$ is simple, and the corresponding ground-state eigenvector is strictly positive in the computational basis.

## 5. Scope and non-implications

- **Pass:** finite-dimensional ground-state eigenvalue simplicity for every finite $N\ge1$, $h>0$, and real finite $J_{ij}$.
- **Pass:** strict positivity of a ground-state eigenvector in the computational basis.
- **Not implied:** strict positivity of reduced density matrices.
- **Not implied:** entropy differentiability, eigenvalue-branch order, or curvature nondegeneracy.
- **Not implied:** any thermodynamic-limit statement.
- **Not yet done:** Lean formalization and proof-to-manuscript correspondence.

## 6. Verification decision

The corrected Perron–Frobenius proof is mathematically complete under the stated finite-dimensional Hamiltonian definition. Promote the *independent mathematical review* to PASS, but retain the overall claim as not fully formally verified until the Lean theorem and its exact matrix/Hamiltonian correspondence are checked.

No upstream Absolute Symmetry file was modified.
