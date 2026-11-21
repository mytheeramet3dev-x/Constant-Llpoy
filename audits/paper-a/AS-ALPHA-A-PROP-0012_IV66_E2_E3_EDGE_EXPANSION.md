# IV-66 — Explicit Second- and Third-Order Energy Corrections

**Status:** ANALYTIC DERIVATION; not Lean verified.

## Definitions
For each undirected edge \(e=(i,j)\), let \(W_e=\sigma_i^z\sigma_j^z\), and \(V=-\sum_e J_eW_e\). The unperturbed x-polarized state is \(|0\rangle\). A flip set \(S\) has gap \(2h|S|\); hence an edge-flip state has gap \(4h\), and a four-site flip state has gap \(8h\).

## Second order
\[
\psi_1=R_0V|0\rangle=\frac{1}{4h}\sum_eJ_e|e\rangle.
\]
Orthogonality of distinct edge-flip states yields
\[
\boxed{E_2=-\frac{1}{4h}\sum_eJ_e^2.}
\]
Only identical-edge pairing contributes at order two.

## Third order: edge-set symmetric difference
The two-operator action on vacuum corresponds to the symmetric difference of the two edge endpoint sets:
- same edge: vacuum; excluded from Q resolvent;
- distinct edges sharing one vertex: the symmetric difference is another two-vertex flip, i.e. the third edge of a triangle;
- disjoint edges: four-vertex flip, which cannot be returned to vacuum by one pair edge.

Vacuum return at third order requires \(e\triangle f\triangle g=\varnothing\). For a simple undirected graph with loop-free edges, the only nonzero third-order closed edge-operation supports are triangles.

Each triangle contributes six ordered operation sequences. Each has two edge-state denominators \(4h\), and the three V factors carry an overall negative sign. Thus
\[
\boxed{E_3=-\frac{3}{8h^2}\sum_{\triangle(i,j,k)}J_{ij}J_{jk}J_{ki}.}
\]
Each triangle is counted once in the sum.

## Scope and caveats
This is a perturbative energy coefficient for the stated pairwise transverse-field Ising model under intermediate normalization. It does not by itself prove the target response proposition. Graphs with no triangles have \(E_3=0\). No fourth-order observable expansion or independent computational cross-check has been completed in this audit.