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
