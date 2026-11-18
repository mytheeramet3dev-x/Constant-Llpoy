# Paper A — Finite-N TFIM Perron–Frobenius Existence and Spectral-Shift Plan

**Status:** proof plan only; the positive top-eigenvector existence theorem and the spectral-shift transfer are not implemented.

## 1. Exact target

For the finite computational-basis configuration type \`SpinConfig N = Fin N → Bool\`, let

\[
K := cI-H,\qquad c>\max_s H_{ss},
\]

where \`H\` is the explicit real-symmetric computational-basis matrix for the finite-\(N\) transverse-field Ising Hamiltonian and \(h>0\).

The next theorem target is an actual model-level statement:

- \(K_{st}\ge 0\) for all configurations;
- the positive-support quiver of \(K\) is strongly connected;
- there exist \(\lambda>0\) and \(v\) with \(v_s>0\) for every configuration and \(Kv=\lambda v\);
- \(\lambda\) is the spectral radius / largest real eigenvalue of \(K\).

The final Paper A target then transfers this to \(H\): its ground-state eigenvalue is \(c-\lambda\), and its characteristic-root multiplicity is one.

## 2. Current formalized prerequisites

The existing modules already contain:
- explicit computational-basis TFIM matrix entries;
- real-symmetry proof for \(H\);
- explicit scalar shift and a proof that the shifted entries are nonnegative;
- exact positive off-diagonal support iff two configurations differ by one spin flip;
- a finite Boolean-hypercube path construction;
- shifted-matrix Hermiticity;
- a conditional characteristic-root multiplicity-one theorem for \(K\), assuming a strictly positive eigenvector and a positive eigenvalue.

The new path-to-quiver bridge is being tested. It must compile before its status is upgraded. A reachability proposition in \`Prop\` cannot be eliminated into quiver-path data in \`Type\`; the implementation therefore uses a separate data-carrying \`PFPath\` inductive and only then forgets it to the proposition-valued relation.

## 3. Remaining proof obligations

### PA-LEAN-027 — existence and strict positivity

Prove a Perron eigenvector existence theorem for the actual finite nonnegative irreducible matrix \(K\), without assuming the eigenvector.

Required subclaims:
1. Establish the finite-dimensional Perron root and its positivity.
2. Construct a nonzero nonnegative eigenvector at the Perron root.
3. Use irreducibility / positive-support connectivity to prove that no coordinate can vanish.
4. Normalize the vector if a simplex-based proof is used.
5. Prove that the resulting eigenvalue equals the spectral radius, not merely that it is some positive eigenvalue.

A possible proof architecture is a Collatz–Wielandt extremal construction on the finite standard simplex, followed by an irreducibility argument that upgrades nonnegativity to strict positivity. The proof must expose compactness, non-emptiness, boundedness, attainment, and every continuity/order argument.

### PA-LEAN-028 — spectral shift and multiplicity transfer

Prove in Lean:
1. \(K=cI-H\) is real symmetric;
2. \(Kv=\lambda v\) iff \(Hv=(c-\lambda)v\);
3. the largest eigenvalue of \(K\) corresponds to the smallest eigenvalue of \(H\);
4. the characteristic-polynomial root multiplicity is preserved under the affine transformation \(x\mapsto c-x\).

The conditional matrix-level simplicity theorem does not itself establish the ground-state correspondence.

### PA-LEAN-029 — final theorem assembly

Combine the model encoding, nonnegativity, irreducibility, positive Perron eigenvector existence, and spectral-shift transfer into the exact finite-\(N\) ground-state nondegeneracy claim in the frozen Paper A source. No hidden positivity, connectivity, or eigenvector-existence assumptions may remain.

## 4. Formalization prior art and compatibility review

A public formalization reference exists in \`or4nge19/MCMC\`, commit \`254beeb\`:
- \`MCMC/PF/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean\`, blob \`98da7b1f0e079a97bb8c8c1d11d03d44e03c3382\`, contains \`Matrix.pft_irreducible\`, an irreducible nonnegative-matrix existence/positivity/uniqueness theorem.
- Supporting modules include \`Lemmas.lean\`, \`Uniqueness.lean\`, \`Primitive.lean\`, and the Collatz–Wielandt development.
- The source carries an Apache-2.0 header.
- That repository uses Lean \`v4.27.0-rc1\` and Mathlib revision \`bf3d6ee6a12e79b7a727df8e1df032ba3819b077\`; Constant Llpoy uses Lean \`v4.36.0\` and Mathlib \`96f6b8b8e029545577421f198a89fb174a4d62e6\`.

This is prior-art and proof-strategy evidence only. It is not imported, not treated as a theorem available in the pinned Mathlib version, and not counted as verification of Paper A. Any adaptation must be reviewed for theorem-statement equivalence, dependency closure, license compliance, and compatibility with the current pinned toolchain.

## 5. Acceptance gates

A result may be marked implemented only when:
- all definitions and theorem statements are source-linked;
- every model-specific hypothesis is proved from the finite-\(N\) TFIM definitions;
- no \`sorry\`, new axiom, oracle, or unreviewed external theorem is introduced;
- the pinned Lean build and axiom audit pass;
- the theorem is checked against the frozen source claim and its quantifiers;
- independent review is recorded separately from CI;
- the Paper A evidence producer and separate provenance verifier authenticate the exact source-bound artifact.

A successful build of the conditional theorem is not a pass for the full ground-state claim.


## 6. Pinned-toolchain theorem-route audit (2026-11-19)

The exact pinned Mathlib revision `96f6b8b8e029545577421f198a89fb174a4d62e6` was inspected. Relevant source blobs:

- `Mathlib/Analysis/InnerProductSpace/Rayleigh.lean`, blob `78845bef9a7cc7a3712f4cdd83c0d8ecadd639b6`:
  - `LinearMap.IsSymmetric.hasEigenvalue_iSup_of_finiteDimensional` proves that the supremum of the Rayleigh quotient of a symmetric operator on a nontrivial finite-dimensional space is an eigenvalue.
  - `IsSelfAdjoint.hasEigenvector_of_isMaxOn` turns a maximizer of the quadratic form on a sphere into an eigenvector.
  - These results provide a possible finite-dimensional extremal route, but do not themselves construct a nonnegative or strictly positive eigenvector.
- `Mathlib/Analysis/Matrix/Spectrum.lean`, blob `5af1845164c4a1c7d7a360bf9086191fac1d52f3`:
  - Hermitian matrices have an orthonormal eigenvector basis; `eigenvalues₀_antitone` orders the real eigenvalues antitonically.
  - This supports the largest-eigenvalue / Rayleigh bridge.
- `Mathlib/LinearAlgebra/Matrix/Irreducible/Defs.lean`, blob `cbd71a13fa7931c20abc99ab01e154578029dad9`:
  - `Matrix.IsIrreducible` packages entrywise nonnegativity and strong connectivity of the positive-entry quiver.
  - `IsIrreducible.exists_pos` supplies a positive entry in every row for a nontrivial index type.

### Preferred route to prototype

Because the Paper A shifted TFIM matrix is real symmetric, use a symmetry-specific Rayleigh-maximization proof before importing a general nonsymmetric Perron development:

1. Obtain a nonzero maximizing vector for the Rayleigh quotient of the real-symmetric shifted matrix.
2. Replace its coordinates by absolute values. Prove norm preservation and that the quadratic form does not decrease, term-by-term from entrywise nonnegativity.
3. Since the original vector already maximizes the Rayleigh quotient, show the absolute-value vector is also a maximizer; invoke the pinned Rayleigh extremum theorem to obtain a nonnegative eigenvector at the largest eigenvalue.
4. Show the largest eigenvalue is strictly positive using the model's strictly positive diagonal (the existing shift bound gives this).
5. Use positive-support connectivity to propagate positivity from one nonzero coordinate to every coordinate. This must be proved explicitly; do not assume strict positivity.
6. Prove the largest real eigenvalue is the spectral radius for this real-symmetric matrix, then feed the resulting positive eigenpair into the existing characteristic-root multiplicity-one theorem.

This route is a **proof strategy only**. The absolute-value quadratic-form inequality, extremizer transfer, strict positivity propagation, and spectral-radius identification have not yet been formalized.

### External formalization prior-art compatibility

The exact source `or4nge19/MCMC` commit `254beeb` was inspected:
- `MCMC/PF/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean`, blob `98da7b1f0e079a97bb8c8c1d11d03d44e03c3382`, contains `Matrix.exists_positive_eigenvector_of_irreducible`.
- It obtains the irreducible case through `1 + A), primitive-matrix Perron theory, and supporting Collatz–Wielandt modules.
- Its declared Lean toolchain is `leanprover/lean4:v4.27.0-rc1`, unlike this repository's Lean `v4.36.0`; the inspected code imports a substantial MCMC-specific support tree. The theorem is therefore not a drop-in dependency for the pinned project.
- The source carries an Apache-2.0 license. No source code has been copied or imported into Constant Llpoy.

**Decision:** prototype the symmetry-specific Rayleigh route first. Reconsider a port of the general irreducible theorem only if the tailored route proves materially harder, and then require a complete dependency, license, theorem-statement, and axiom audit.

## 7. Current status after route audit

- PA-LEAN-027: `NOT_IMPLEMENTED`; existence of a strictly positive top eigenvector remains the principal mathematical gap.
- PA-LEAN-028: `PARTIAL`; the algebraic eigenvector correspondence for `K = cI - H` is formalized, but the extremal spectral transfer and characteristic-root affine-multiplicity bridge are not complete.
- PA-LEAN-029: `NOT_IMPLEMENTED`; no final model-level ground-state nondegeneracy theorem is claimed.
