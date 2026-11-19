# C01-L1.11 — ECB-10 Simplicity of the Top Eigenvalue

**Status:** PROPOSED / MATHEMATICAL ARGUMENT; NOT LEAN-COMPILED  
**Scope:** Prove the top eigenspace is one-dimensional using strict positivity and the absolute-value quadratic-form comparison, without invoking the Perron–Frobenius simplicity theorem as a black box.

## 1. Hypotheses

Let K be a real symmetric matrix on a finite index set V. Assume K_ij≥0 for i≠j and the graph of strictly positive off-diagonal entries is connected. Let λ_max be the maximal Rayleigh value. By the preceding ECB-01–08, there exists a unit top eigenvector y with y_i>0 for every i.

## 2. Assume a second top eigenvector exists

Suppose the top eigenspace has dimension at least two. Then choose a nonzero top eigenvector z orthogonal to y (orthogonalize within the eigenspace). Since y_i>0 for all i and ⟨z,y⟩=0, z must have at least one positive and at least one negative coordinate. Otherwise its inner product with y would have strict one-sided sign.

Normalize z to unit norm if convenient. It remains a top Rayleigh maximizer.

## 3. Apply absolute coordinates to z

Set w_i=|z_i|. Norm preservation gives ‖w‖=‖z‖, and quadratic-form comparison gives Q_K(w)≥Q_K(z). Since z is a top maximizer, w cannot have a larger Rayleigh quotient; hence w is also a top maximizer. ECB-08 strict positivity applies to w, so w_i>0 for every i. Thus z_i≠0 for every i.

## 4. Connected graph forces a sign-changing positive edge

Because z has both positive and negative coordinates and no zero coordinates, connectedness implies there is an edge {i,j} with z_i z_j<0. (Along a path from a positive-coordinate vertex to a negative-coordinate vertex, the sign must change across an adjacent pair.) On that edge K_ij>0.

In the quadratic-form comparison, diagonal terms cancel, while the off-diagonal contribution for this edge is strictly larger after taking absolute values:
\[
K_{ij}(|z_i||z_j|-z_i z_j)>0.
\]
The full ordered-pair sum includes both (i,j) and (j,i); every other off-diagonal difference is nonnegative. Hence Q_K(w)>Q_K(z), contradicting that z is a top Rayleigh maximizer.

## 5. Conclusion

The top eigenspace cannot have dimension at least two. Therefore λ_max is simple (algebraic multiplicity one for a real symmetric matrix) and its eigenvector is unique up to scalar. The positive normalized eigenvector is uniquely determined.

## 6. Lean obligations

- ECB-10a: construct a nonzero top eigenvector z orthogonal to y if the eigenspace is assumed nontrivial beyond span(y).
- ECB-10b: orthogonality to y>0 forces z to have positive and negative coordinates.
- ECB-10c: absolute-value vector w remains a top maximizer using ECB-02/04/05.
- ECB-10d: apply strict positivity ECB-08 to w to rule out zero coordinates of z.
- ECB-10e: derive a sign-changing edge from connectedness and nonzero coordinates.
- ECB-10f: show the quadratic-form comparison is strict on that edge and non-strict elsewhere.
- ECB-10g: contradiction to maximality, establishing one-dimensionality.

## 7. Caveats

This proof uses the strict positivity lemma and the strict-edge graph assumptions. It must not claim simplicity from connectivity without a proof. It establishes simplicity of the top eigenvalue for the stated real symmetric nonnegative-off-diagonal irreducible matrix. It does not by itself show that all eigenvalues are simple.

**Disposition:** Mathematical argument is sound under the stated hypotheses. Concrete Lean proof, theorem/API mapping, compilation, and axiom audit remain pending. **NOT FORMALLY VERIFIED.**
