# C01-L1.2 — Lean Implementation Blueprint

- **Document ID:** CL-PA-C01-L1.2-LIB-001
- **Version:** 0.1.0
- **Branch:** `paper-a-mcr01-pf-redline`
- **Status:** SOURCE-INSPECTED; IMPLEMENTATION NOT YET COMPILED
- **Purpose:** Turn C01-L1.1 into a concrete, ordered scratch-module implementation plan without adding uncompiled proof code to production.

## 1. Exact project source inspected

- `formalization/lean/ConstantLlapoy/PaperA/HamiltonianEncoding.lean`
  - Blob SHA: `c168ac95bdd0bd971a6f4a1568c8b6391e780664f`
  - Defines `SpinConfig N := Fin N → Bool`.
  - Defines `shiftedTFIMHamiltonian`, its entrywise nonnegativity theorem, its Hermitian theorem, and the coordinate eigenvector propagation theorem.
- `formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean`
  - Blob SHA: `d1553a8dbcf60aaec449a98d59e92ab91c1812ea`
  - Already contains `quadratic_form_le_abs_quadratic_form` with exact statement:
    [
    \sum_i\sum_j A_{ij}x_i x_j
    \leq
    \sum_i\sum_j A_{ij}|x_i||x_j|
    ]
    assuming `∀ i j, 0 ≤ A i j`.
  - This theorem is source-present; the remaining task is to connect it to the Euclidean Rayleigh operator.

## 2. Exact Mathlib source identities

Pinned Mathlib commit: `96f6b8b8e029545577421f198a89fb174a4d62e6`.

- `Mathlib/Analysis/Normed/Lp/Matrix.lean`, blob `bbe4769e298c51c4f3c7047c0ab97dcebe78c435`:
  `Matrix.toLpLin_apply` states
  `toLpLin p q M v = toLp _ (M *ᵥ ofLp v)`.
- `Mathlib/Analysis/Matrix/Hermitian.lean`, blob `5b2cfb936a1abf866172d167127361f83d957d41`:
  `Matrix.isSymmetric_toEuclideanLin_iff` states
  `A.toEuclideanLin.IsSymmetric ↔ A.IsHermitian`.
- `Mathlib/Analysis/InnerProductSpace/LinearMap.lean`, blob `597c0a46783b4caec8c356bbfdb9448bbc717b0d`:
  `ContinuousLinearMap.reApplyInnerSelf_apply` unfolds to
  `re ⟪T x, x⟫`.
- `Mathlib/Analysis/InnerProductSpace/PiL2.lean`, blob `6085a51fa11c76443db1c56e46d5fde654e7deaf`:
  `EuclideanSpace.inner_eq_star_dotProduct` and
  `EuclideanSpace.real_norm_sq_eq` supply the coordinate identities.

All four files were fetched at the pinned commit. This is source inspection, not compilation.

## 3. Exact quadratic-form bridge

For `κ := SpinConfig N`, `A : Matrix κ κ ℝ`, and
`x : EuclideanSpace ℝ κ`, the chosen matrix operator is
`A.toEuclideanLin`.

The operator action is coordinatewise matrix multiplication:
[
\operatorname{ofLp}(A.toEuclideanLin(x))=A *ᵥ \operatorname{ofLp}(x).
]

The inner product order is important. Mathlib defines the real-coordinate identity through
`EuclideanSpace.inner_eq_star_dotProduct`; with `u = A x` and `v = x`,
[
\langle A x,x\rangle
=x\cdotᵥ(A*ᵥx)
=\sum_i x_i\left(\sum_j A_{ij}x_j\right)
=\sum_i\sum_j A_{ij}x_i x_j.
]
The final equality uses distributivity and commutativity in `ℝ`. It does **not** require assuming entrywise symmetry. Hermitian/symmetric structure is a separate input for the Rayleigh theorem.

Consequently the already-present inequality theorem applies to
`A := shiftedTFIMHamiltonian J h`, once the real Euclidean inner product has been rewritten into the double finite sum.

## 4. Scratch module declarations and dependencies

Create a separate module under `formalization/lean/ConstantLlapoy/PaperA/Scratch/`; do not modify `HamiltonianEncoding.lean` or `PerronFrobeniusCore.lean` during this stage.

Recommended declarations:

1. `absCoord`: lift `fun s => |x s|` into `EuclideanSpace ℝ κ`.
2. `absCoord_apply`: prove the coordinate of the lift is exactly `|x s|`.
3. `absCoord_nonneg`: `0 ≤ absCoord x s`.
4. `absCoord_norm_sq`: expand the squared norm as a finite sum and use `sq_abs`.
5. `absCoord_norm`: infer norm equality from equality of squared norms and norm nonnegativity.
6. `toEuclideanLin_inner_eq_double_sum`: rewrite `(A.toEuclideanLin).reApplyInnerSelf x` as the exact double sum in the existing theorem.
7. `quadratic_le_absCoord_quadratic`: invoke `quadratic_form_le_abs_quadratic_form` and rewrite both sides.
8. `absCoord_isRayleighMaximizer`: after a Rayleigh maximizing vector exists, use the same norm and quadratic comparison to prove the absolute-value vector also maximizes on the same-radius sphere.
9. `absCoord_nonzero`: derive from norm preservation and the original nonzero vector.

The exact namespace and implicit scalar parameters should be aligned with the project files at implementation time. No declaration above is claimed to exist yet.

## 5. Why the construction is mathematically sufficient

Suppose `x ≠ 0` attains the global Rayleigh supremum `M`, and set `y = absCoord x`.

- Norm preservation gives `‖y‖ = ‖x‖ > 0`, so `y ≠ 0`.
- The quadratic-form inequality gives `Q(x) ≤ Q(y)`.
- Since `x` attains the global Rayleigh supremum, every nonzero vector, including `y`, has Rayleigh quotient at most `M`.
- Since `x` and `y` have the same norm, these two facts force equality of the quadratic forms and show that `y` also attains `M).
- The maximizer-to-eigenvector theorem can then be applied to `y).

This argument must be formalized with explicit denominator positivity and the exact definition of Rayleigh quotient. No division by a possibly zero norm is permitted.

## 6. Remaining independent obligations after the bridge

Even after the scratch bridge compiles, the following remain distinct:

- Obtain the Rayleigh supremum/eigenvalue pair using the pinned finite-dimensional symmetric-operator theorem.
- Show the returned eigenvalue is the top eigenvalue of the matrix's ordered eigenvalue list (if the manuscript theorem is stated in that language).
- Translate the Euclidean continuous-linear-map eigenvector equation into the coordinate equation expected by
  `shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive`.
- Audit all axioms and theorem dependencies.
- Prove correspondence between the exact formal theorem and the manuscript's THM-0002 statement.

Do not conflate eigenvalue existence with simplicity. The nonnegative eigenvector construction plus existing graph propagation gives strict positivity; the characteristic-root multiplicity-one theorem remains a separate final step.

## 7. CI and verification route

The branch's existing `.github/workflows/constant-llpoy-lean.yml` was inspected (blob SHA
`592de198ac37aae08eb1a2021af1131b5682d5a8`). It runs the pinned Lean build and axiom audit on:
- pushes to `main` affecting `formalization/lean/**`; and
- pull requests affecting `formalization/lean/**`.

It also supports `workflow_dispatch`, but no workflow-dispatch action is exposed by the available GitHub integration in this session. The latest documentation-only commit `43244a323bf692ca174cfdc0409e20746cb43bb7` has zero check-runs and zero statuses; no CI run is being claimed.

A real Lean verification requires adding the scratch module under `formalization/lean/**` and having the repository's configured GitHub Actions workflow execute on a PR or main-branch push. Until then, compilation status is **NOT RUN**.

## 8. Disposition

- Coordinate identities: source-inspected.
- Existing absolute-value inequality: confirmed source-present.
- Scratch implementation: not yet created.
- Lean compile: not run.
- Axiom audit: not run for this bridge.
- C01-L1: **IN PROGRESS — NOT VERIFIED**.
- THM-0002: **NOT VERIFIED**.
- Paper A: **NOT VERIFIED**.

No upstream `Absolute_Sym` files were modified.
