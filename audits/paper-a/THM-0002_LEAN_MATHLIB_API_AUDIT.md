# THM-0002 Lean / Mathlib API audit

- **Claim:** `AS-ALPHA-A-THM-0002`
- **Repository:** `mytheeramet3dev-x/Constant-Llpoy`
- **Audit date:** 2026-11-17
- **Mathlib revision:** `96f6b8b8e029545577421f198a89fb174a4d62e6` (the revision pinned in `formalization/lean/lakefile.lean`)
- **Status:** API reconnaissance only; no theorem formalized and no claim status promoted.

## 1. Question

Can the finite-N transverse-field Ising ground-state simplicity proof be formalized by directly invoking a Perron–Frobenius theorem already present in the pinned Mathlib revision?

## 2. Findings

The pinned source contains:

- `Mathlib/LinearAlgebra/Matrix/Irreducible/Defs.lean`
  - `Matrix.toQuiver`
  - `Matrix.IsIrreducible`
  - `Matrix.pow_apply_pos_iff_nonempty_path`
  - `Matrix.isIrreducible_iff_exists_pow_pos`
  - `Matrix.IsPrimitive.isIrreducible`

These declarations provide a graph-theoretic interface for nonnegative matrices and connect strong connectivity to positivity of some matrix powers. They do **not**, in this file, assert existence of a positive eigenvector, identify the spectral radius as an eigenvalue, or establish algebraic/geometric simplicity of the Perron eigenvalue.

Searches of the pinned Mathlib repository for `Perron Frobenius`, `spectralRadius`, `eigenvector positive matrix`, `IsIrreducible eigenvalues`, and `exists_eigenvalue nonnegative matrix` located general spectral/eigenvalue infrastructure and the irreducibility file above, but no ready-made irreducible-nonnegative-matrix Perron–Frobenius simplicity theorem.

This is a bounded API search, not a proof that no relevant theorem exists anywhere under a different name. Before implementing a custom theorem, perform a declaration-level search over the pinned source tree and inspect related matrix spectrum/eigenvalue files.

## 3. Mathematical route that the formalization must preserve

For the computational `Fin N → Bool` basis (or an explicitly equivalent finite type), define the real symmetric Hamiltonian matrix H:

- diagonal interaction term: `-∑_{i<j} Jᵢⱼ zᵢ zⱼ`;
- off-diagonal term: `-h` exactly when two bitstrings differ at one site;
- zero off-diagonal term when Hamming distance is not one.

Choose `c = 1 + max_s H[s,s]` and define `K = c • 1 - H`.

Required obligations:

1. Prove every entry of K is nonnegative.
2. Prove a positive K-entry exists for every single-spin flip, using h>0.
3. Prove the positive-entry graph of K is strongly connected by constructing a path that flips exactly the differing coordinates between any two bitstrings.
4. Prove K is real symmetric.
5. Establish a Perron–Frobenius result for this finite irreducible nonnegative matrix, including simplicity of the maximal eigenvalue and a strictly positive eigenvector.
6. Transfer simplicity from K to the lowest eigenvalue of H using the affine spectral relation.

The couplings Jᵢⱼ may be arbitrary finite real numbers: they affect only the diagonal. The hypothesis h>0 is essential for the hypercube edges.

## 4. Formalization options and trust boundary

A valid implementation may:

- prove the needed finite-dimensional Perron–Frobenius theorem inside Constant Llapoy from already verified Mathlib foundations; or
- use a suitable theorem if a deeper pinned-source audit finds one and document its exact declaration and assumptions.

It may **not**:

- introduce an axiom, `sorry`, or `admit`;
- state Perron–Frobenius simplicity as an unproved hypothesis and count the Hamiltonian claim as verified;
- formalize only the hypercube connectivity while omitting the spectral simplicity step;
- infer strict positivity or simplicity from irreducibility without the required theorem;
- weaken h>0 or conceal the finite-dimensional assumptions.

## 5. Current disposition

- Independent mathematical proof review: PASS (see `THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md`).
- Lean Hamiltonian/matrix construction: NOT_STARTED.
- Hypercube irreducibility formalization: NOT_STARTED.
- Perron–Frobenius spectral theorem dependency: NOT_RESOLVED.
- Lean theorem for THM-0002: NOT_FORMALIZED.
- Full claim status: NOT_VERIFIED.

## 6. Next bounded task

Complete a declaration-level audit of the pinned Mathlib matrix and finite-dimensional spectral files, recording exact candidate declarations and assumptions. If no applicable PF simplicity theorem exists, design a separate, reviewable finite-dimensional PF development before connecting it to the TFIM matrix. Keep this work inside Constant Llapoy.


## 7. Deeper spectral API inspection

A second pass inspected these pinned files:

- `Mathlib/Analysis/Matrix/Spectrum.lean`
  - For Hermitian matrices: `Matrix.IsHermitian.eigenvalues`, `eigenvectorBasis`, `mulVec_eigenvectorBasis`, `eigenvalues_mem_spectrum_real`, and `spectral_theorem`.
  - The eigenvalue indexing is ordered antitonically through `eigenvalues₀_antitone`.
- `Mathlib/Analysis/InnerProductSpace/Spectrum.lean`
  - General finite-dimensional self-adjoint spectral decomposition and eigenspace orthogonality.
- `Mathlib/LinearAlgebra/Eigenspace/Matrix.lean`
  - Matrix/linear-map spectrum equivalences and diagonal matrix eigenvalue facts.
- `Mathlib/LinearAlgebra/Matrix/PosDef.lean`
  - Positive-semidefinite and positive-definite quadratic-form interfaces.
- `Mathlib/LinearAlgebra/Matrix/Irreducible/Defs.lean`
  - Positive-entry quiver and strong-connectivity interface.

These results provide the real-symmetric spectral foundation and matrix irreducibility interface, but the inspected declarations still do not give the PF conclusion (a strictly positive top eigenvector and one-dimensional top eigenspace) for a general irreducible entrywise-nonnegative symmetric matrix.

## 8. Candidate self-contained symmetric PF proof (not yet formalized)

For a finite index type and a real symmetric matrix A with nonnegative entries and connected positive-entry graph:

1. By the symmetric spectral theorem, the largest eigenvalue λ exists and is the maximum Rayleigh quotient.
2. For a maximizing unit vector x, the coordinatewise absolute-value vector |x| has the same norm and satisfies
   `⟪|x|, A |x|⟫ ≥ ⟪x, A x⟫`,
   because every A_ij is nonnegative and `|x_i||x_j| ≥ x_i x_j`.
3. Maximality forces |x| to be a maximizer too, hence an eigenvector for λ.
4. The eigen-equation and graph connectivity imply every coordinate of this nonnegative eigenvector is strictly positive: if one coordinate were zero, the eigen-equation forces all positive-neighbors to be zero; connectivity propagates this to every coordinate, contradicting unit norm.
5. For any other top eigenvector y, equality in the Rayleigh absolute-value inequality forces no positive edge to join coordinates of opposite nonzero signs. Since the positive-entry graph is connected and the strictly positive top eigenvector exists, the top eigenspace must be one-dimensional. A formal proof must handle zero coordinates and the equality condition carefully; this step is not accepted as complete merely from the outline.

This is a candidate proof architecture, not a Lean proof and not a claim that all required inequalities/API lemmas have been located. In particular, the equality case in step 5 must be formalized rigorously.

## 9. Updated disposition

- Symmetric spectral decomposition API: LOCATED.
- Positive-entry irreducibility API: LOCATED.
- Ready-made symmetric Perron–Frobenius simplicity theorem: NOT LOCATED in inspected files.
- Candidate elementary proof route: IDENTIFIED; equality-case proof still open.
- TFIM Hamiltonian encoding and correspondence: NOT_STARTED.
- THM-0002 Lean formalization: NOT_STARTED.
- Full claim: NOT_VERIFIED.


## 10. Refined uniqueness argument via a stochastic edge kernel

The equality-case step in the preceding candidate proof can be replaced by a cleaner ratio argument, once a strictly positive top eigenvector v and positivity of the top eigenvalue λ have been established.

Let A be symmetric, entrywise nonnegative, with connected positive-entry graph. Assume λ>0 and v_i>0 for every i, with Av=λv. For any other real eigenvector y with Ay=λy, define t_i=y_i/v_i and
`P(i,j)=A_{ij}v_j/(λv_i)`.

Then:

- P(i,j)≥0.
- `∑_j P(i,j)=1`, by Av=λv.
- `t_i=∑_j P(i,j)t_j`, by Ay=λy.
- Since the finite index set has a maximum M=max_i t_i, at an index i attaining M, the weighted-average identity forces t_j=M for every j with A_ij>0.
- Connectivity propagates t_j=M to all vertices, hence y=Mv.

Thus every real eigenvector for λ is proportional to v. Since A is symmetric, the spectral theorem identifies algebraic multiplicity with eigenspace dimension, so λ is simple.

The proof still requires formalizing:
1. λ>0 from a positive off-diagonal entry (e.g. a positive Rayleigh quotient on the all-ones vector);
2. the existence of a nonnegative maximizing eigenvector using the absolute-value Rayleigh inequality;
3. strict positivity of that eigenvector by zero-propagation along connected positive edges;
4. finite maximum and weighted-average propagation;
5. translation from one-dimensional eigenspace to simplicity in the exact matrix/eigenvalue API used.

This ratio argument avoids a delicate equality characterization in the absolute-value inequality. It is still only a proof plan; no Lean theorem has been committed.
