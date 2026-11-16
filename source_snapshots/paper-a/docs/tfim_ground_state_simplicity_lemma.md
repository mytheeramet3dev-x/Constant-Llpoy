# Ground-state simplicity lemma for finite all-to-all TFIM

**Status:** [EXACT]

## Statement

For finite \(N\ge1\), \(h>0\), and real couplings \(J_{ij}\), consider
\[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^x.
\]
If the transverse-field graph is connected (in particular, for \(h>0\) on
all sites), the ground-state eigenvalue is simple. In the computational
\(\sigma^z\) basis, a ground-state vector can be chosen strictly positive.

## Proof

In the computational basis, the Ising term is diagonal. The transverse-field
term connects two basis configurations exactly when they differ at one spin,
with off-diagonal matrix element \(-h<0\). The resulting configuration graph
is the \(N\)-dimensional hypercube and is connected.

Choose \(c\) large enough that \(K=cI-H\) is entrywise nonnegative. Because
the off-diagonal configuration graph is connected, \(K\) is irreducible.
The Perron–Frobenius theorem gives a simple largest eigenvalue of \(K\) with
a strictly positive eigenvector. Since the eigenvalues of \(K\) are
\(c-E\), its largest eigenvalue corresponds to the smallest eigenvalue of
\(H\). Therefore the ground state of \(H\) is simple and strictly positive
in this basis.

## Consequences

For the dimensionless symmetric Hamiltonian
\[
\widetilde H_N(x)
=-x\sum_{i<j}\sigma_i^z\sigma_j^z-\sum_i\sigma_i^x,
\qquad x\ge0,
\]
the ground state is simple for every finite \(x\ge0\). For \(x\) in the
interior \(x>0\), the ground-state spectral projector is locally real-analytic
in \(x\), by the finite-dimensional resolvent formula.

This closes the ground-state-simplicity hypothesis used in
docs/curvature_analyticity_lemma.md. It does not prove positive definiteness
of \(\rho_1\) or \(\rho_{12}\), and therefore does not by itself prove
analyticity of the entropy or \(\mathcal G_N''(x_c)\ne0\).
