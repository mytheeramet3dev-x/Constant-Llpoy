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
