# Constant Llapoy — Lean Formalization

**Project:** Paper A only  
**Status:** Initial formalization scaffold; first source module submitted to CI, not yet build-verified.  
**Boundary:** This directory is inside Constant Llapoy. No Absolute Symmetry source is edited.

## Pinned toolchain

- Lean: `leanprover/lean4:v4.36.0`
- Mathlib repository: `leanprover-community/mathlib4`
- Mathlib commit: `96f6b8b8e029545577421f198a89fb174a4d62e6`
- Transitive Lake dependencies: locked by exact revisions in `lake-manifest.json`.
- CI action revisions are pinned by commit SHA in `.github/workflows/constant-llapoy-lean.yml`.

The Mathlib commit's own `lean-toolchain` file was checked and matches the pinned Lean version. The manifest was assembled from that exact Mathlib commit's dependency manifest, with the Mathlib package added as the root dependency and its transitive packages locked.

## First formalized obligations

Module: `ConstantLlapoy/PaperA/WeakCoupling.lean`

1. Positivity of
   [
   \alpha_N=\frac18\ln\left(\frac{2(N-2)}{N-1}\right)
   \]
   for every natural (N\ge4).
2. The elementary sign implication when the absolute remainder is at most half the positive leading term.
3. The weak-coupling endpoint sign conditional on that explicit remainder bound.
4. The chain-rule derivative of the positive-eigenvalue entropy contribution ( -f\ln f ), when (f(x)>0).

## Explicitly not formalized yet

The following are separate obligations and MUST NOT be inferred from the initial module:

- The joint real-analytic eigenvalue factorization used at rank-changing / zero eigenvalues.
- The zero-eigenvalue entropy directional-derivative lemma.
- The reduced-density-matrix perturbation expansions and edge derivatives.
- The differentiated (O_N(r^3(1+|\ln r|))) remainder.
- The eventual small-coupling threshold implied by the asymptotic remainder.
- The full strong-coupling differentiated remainder and endpoint threshold proof.
- Exact correspondence between the Lean declarations and the frozen Paper A manuscript.

The current endpoint theorem is deliberately conditional on an explicit remainder inequality. It does not turn a big-O assertion into a verified estimate.

## Build and verification

From this directory, run:

```sh
lake exe cache get
lake build
```

The repository CI runs the pinned Lean/Mathlib build and an axiom audit. A green build will establish only that the declarations in this module type-check under the pinned Lean/Mathlib environment; it will not establish the unformalized analytic remainder or manuscript correspondence.

Do not run `lake update` as part of an ordinary verification run: it can move dependency revisions and rewrite the lockfile. If a dependency update is intentionally proposed, review and commit the complete manifest diff as a separate change.

Until a successful CI run is observed, the module status remains **NOT BUILD-VERIFIED**.
