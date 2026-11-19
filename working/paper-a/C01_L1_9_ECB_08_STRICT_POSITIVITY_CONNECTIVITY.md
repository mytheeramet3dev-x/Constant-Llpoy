# C01-L1.9 — ECB-08 Strict Positivity by Connectivity

**Status:** PROPOSED / MATHEMATICAL AUDIT; NOT LEAN-COMPILED  
**Scope:** Upgrade a nonzero nonnegative eigenvector to strictly positive coordinates, using a connected graph of strictly positive off-diagonal entries.

## 1. Hypotheses

Let K be a real finite matrix indexed by a finite vertex set V. Let y be a nonzero vector satisfying Ky=λy and y_i≥0 for all i. Assume K_ij≥0 for i≠j. Define an undirected graph with edge {i,j} whenever K_ij>0 (the intended application has symmetric K), and assume this graph is connected.

## 2. Zero-coordinate propagation

Suppose y_i=0. The coordinate eigenvector equation gives

Σ_{j≠i} K_ij y_j = (λ−K_ii)y_i = 0.

Every summand K_ij y_j is nonnegative. A finite sum of nonnegative real numbers equals zero only if every summand equals zero. Hence for every j with K_ij>0, K_ij y_j=0, and strict positivity of K_ij implies y_j=0.

Thus a zero at one vertex propagates to every adjacent vertex along a positive edge.

## 3. Connectivity propagation and contradiction

If the graph is connected, any vertex j can be reached from i by a finite positive-edge path. Repeated zero propagation implies y_j=0 for every j∈V. This contradicts y≠0. Therefore no coordinate is zero. Combined with y_i≥0, this gives y_i>0 for every i.

## 4. Hypercube application

For spin configurations Ω_N={−1,+1}^N, connect two configurations if they differ by a single spin flip. This graph is connected: transform one configuration into another by flipping precisely the coordinates where they differ. Under the Paper A shifted operator K=cI−H, confirm from the frozen operator definition that each single-spin-flip off-diagonal coefficient is strictly positive when h>0. Then the positive-edge graph contains the hypercube edges and is connected, so the strict-positivity lemma applies.

For N=0 the graph has one vertex; nonzero nonnegative y has its sole coordinate positive, so the conclusion is immediate.

## 5. Lean proof obligations

- ECB-08a: extract the coordinate eigen-equation.
- ECB-08b: with y_i=0, simplify the RHS to zero.
- ECB-08c: show every summand K_ij y_j is nonnegative.
- ECB-08d: infer each summand is zero from a finite sum of nonnegative terms equaling zero.
- ECB-08e: infer y_j=0 on every positive-weight edge.
- ECB-08f: propagate along a graph path (induction on path length).
- ECB-08g: use graph connectivity to force all coordinates zero and contradict nonzero y.
- ECB-08h: separately verify the frozen operator's spin-flip edge coefficient is strictly positive for h>0.

## 6. Assumption discipline

Connectivity alone is insufficient unless the edge weights used in propagation are strictly positive. Likewise, off-diagonal nonnegativity does not imply positivity on every graph edge. The Paper A application must verify the exact coefficient and sign of K=cI−H from its frozen source, not from memory or a generic model convention.

This lemma proves strict positivity for the constructed nonnegative eigenvector. It does not by itself prove simplicity of the top eigenvalue or uniqueness of the positive eigenvector.

**Disposition:** The abstract strict-positivity argument is mathematically sound under the listed assumptions. The exact source/operator correspondence, concrete Lean code, compilation, and axiom audit remain pending. **NOT FORMALLY VERIFIED.**
