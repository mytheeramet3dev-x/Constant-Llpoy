# C01-L1.1 — Euclidean Coordinate Bridge

- **Document ID:** CL-PA-C01-L1.1-ECB-001
- **Version:** 0.1.0
- **Branch:** `paper-a-mcr01-pf-redline`
- **Status:** SOURCE-INSPECTED; PROOF IMPLEMENTATION OPEN
- **Scope:** Resolve the exact finite-coordinate identities needed to connect the existing absolute-value quadratic-form inequality to Mathlib's Euclidean Rayleigh construction.
- **Pinned Lean:** `leanprover/lean4:v4.36.0`
- **Pinned Mathlib:** `96f6b8b8e029545577421f198a89fb174a4d62e6`

## 1. Exact project inputs inspected

Working-branch source files:

| File | Blob SHA |
|---|---|
| `formalization/lean/ConstantLlapoy/PaperA/HamiltonianEncoding.lean` | `c168ac95bdd0bd971a6f4a1568c8b6391e780664f` |
| `formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean` | `d1553a8dbcf60aaec449a98d59e92ab91c1812ea` |
| `formalization/lean/lean-toolchain` | `00f848359b1cdaf7c12cd6b7acc5b4364752e154` |
| `formalization/lean/lakefile.lean` | `c135825a39770b3f26860aeae9983b8351d490f6` |

The model index type is `SpinConfig N := Fin N → Bool`. The shifted Hamiltonian is a real matrix on this finite type. The existing theorem `quadratic_form_le_abs_quadratic_form` is source-present in `PerronFrobeniusCore.lean`; it states the required entrywise absolute-value inequality under entrywise nonnegativity.

## 2. Pinned Mathlib source inspected

Exact files fetched at the pinned Mathlib commit:

| Mathlib file | Blob SHA | Relevant declarations |
|---|---|---|
| `Mathlib/Analysis/InnerProductSpace/Rayleigh.lean` | `78845bef9a7cc7a3712f4cdd83c0d8ecadd639b6` | `IsSelfAdjoint.hasEigenvector_of_isMaxOn`, `rayleighQuotient`, `iSup_rayleigh_eq_iSup_rayleigh_sphere` |
| `Mathlib/Analysis/InnerProductSpace/PiL2.lean` | `6085a51fa11c76443db1c56e46d5fde654e7deaf` | `EuclideanSpace.inner_eq_star_dotProduct`, `inner_toLp_toLp`, `EuclideanSpace.real_norm_sq_eq` |
| `Mathlib/Analysis/Matrix/Spectrum.lean` | `5af1845164c4a1c7d7a360bf9086191fac1d52f3` | `Matrix.isSymmetric_toEuclideanLin_iff`, `Matrix.IsHermitian.eigenvalues₀_antitone`, `Matrix.IsHermitian.mulVec_eigenvectorBasis`, `Matrix.toLpLin_apply` |

This is source inspection, not a compilation result.

## 3. Coordinate bridge: exact mathematical identities

Let `κ := SpinConfig N`, let `A : Matrix κ κ ℝ` be the shifted TFIM matrix, and let `x : EuclideanSpace ℝ κ`. Write `x_i` for its coordinate at `i`.

The pinned Mathlib source identifies the Euclidean representation with the (L^2) Pi space. In particular:

1. The coordinatewise absolute-value vector is represented by the Pi-(L^2) lift of the function `fun i => |x i|`.
2. Its coordinates are nonnegative by `abs_nonneg`.
3. The norm identity follows coordinatewise:
   [
   |,|x|_{mathrm{coord}},|^2
   = \sum_i |x_i|^2
   = \sum_i x_i^2
   = \|x\|^2.
   ]
   The final equality is exactly the real-coordinate norm formula exposed by `EuclideanSpace.real_norm_sq_eq`. The middle equality is `sq_abs`.

For the operator represented by `A.toLpLin 2 2`, Mathlib's `EuclideanSpace.inner_eq_star_dotProduct` and `Matrix.toLpLin_apply` reduce the real quadratic form to:
[
\langle A x,x\rangle
=\sum_i x_i\,(A x)_i
=\sum_i\sum_j A_{ij}x_i x_j.
]
The last equality requires only the finite matrix-vector expansion, finite-sum rearrangement, and commutativity of real multiplication. It is not an additional analytic assumption.

Applying the already-present theorem
`quadratic_form_le_abs_quadratic_form A x hA_nonneg`
then gives:
[
\langle A x,x\rangle
\leq
\langle A |x|_{\mathrm{coord}},|x|_{\mathrm{coord}}\rangle.
]

These formulas identify the exact proof bridge; they do not yet constitute Lean declarations.

## 4. Lean implementation obligations isolated

The next scratch module should prove these separately, without editing production modules first:

- **ECB-01 — coordinate representation:** establish the exact type/coercion between `EuclideanSpace ℝ κ`, its coordinate function, and `Matrix.toLpLin 2 2 A`.
- **ECB-02 — absolute vector:** define the lifted coordinatewise absolute-value vector and prove its coordinate evaluation is `|x i|`.
- **ECB-03 — norm preservation:** prove equality of squared norms using `EuclideanSpace.real_norm_sq_eq` and `sq_abs`, then infer equality of norms using nonnegativity.
- **ECB-04 — quadratic expansion:** prove that `reApplyInnerSelf` for the real Euclidean operator equals the double finite sum used by `quadratic_form_le_abs_quadratic_form`.
- **ECB-05 — inequality transfer:** apply the existing scalar theorem and rewrite both sides through ECB-04.
- **ECB-06 — maximizer preservation:** retain the exact sphere-membership and maximum hypotheses; use norm preservation plus the quadratic inequality to show that the absolute-value vector is also a maximizer.

Do not hide any of these obligations in an opaque helper or use an axiom. In particular, ECB-04 must be checked against the orientation of Mathlib's inner product convention: the pinned source states
`⟪x,y⟫ = ofLp y ⬝ᵥ star (ofLp x)`.
For real scalars, the resulting quadratic expression is the stated `xᵀ A x` expression.

## 5. Rayleigh API: corrected use

The pinned theorem has the exact shape:
`IsSelfAdjoint.hasEigenvector_of_isMaxOn`
with a nonzero vector `x₀` and a proof that `x₀` maximizes `T.reApplyInnerSelf` on `sphere 0 ‖x₀‖`. It returns an eigenvector at the global supremum of the Rayleigh quotient.

The implementation must not confuse:
- maximizing the unnormalized quadratic form on a fixed sphere;
- maximizing the Rayleigh quotient over nonzero vectors;
- obtaining an eigenvector at the supremum;
- identifying that supremum with the first entry of the antitone eigenvalue list.

The first two are related because the norm is constant on the sphere, but the proof must explicitly retain the positive-radius/nonzero condition. The fourth still needs a precise spectral-ordering argument.

## 6. Remaining boundary

This note resolves the source-level coordinate identities and narrows the implementation work. It does **not** claim:
- a Lean scratch module has been written or compiled;
- a Rayleigh maximizer has been constructed in the project;
- the supremum has been formally identified with the first eigenvalue-list entry;
- a positive top eigenvector has been produced;
- the C01-L1 or THM-0002 obligation has passed.

No upstream `Absolute_Sym` file was modified. Paper A remains **NOT VERIFIED**.


## 7. Refined existence route: use Mathlib's finite-dimensional Rayleigh theorem

A further exact source inspection of lines 320–344 of the pinned
`Mathlib/Analysis/InnerProductSpace/Rayleigh.lean` resolves an important
architectural question. The declaration

`LinearMap.IsSymmetric.hasEigenvalue_iSup_of_finiteDimensional`

already proves that the supremum of the Rayleigh quotient is an eigenvalue
for a symmetric operator on a nontrivial finite-dimensional inner-product
space. Its implementation explicitly constructs a compact sphere, obtains
a maximum of `reApplyInnerSelf`, and invokes
`IsSelfAdjoint.hasEigenvector_of_isMaxOn`.

This suggests the following tighter route and avoids independently
reimplementing compactness:

1. Set `T := A.toEuclideanLin` (equivalently the pinned `toLpLin 2 2`
   representation) on `EuclideanSpace ℝ κ`.
2. Obtain symmetry from the pinned bridge
   `Matrix.isSymmetric_toEuclideanLin_iff.mpr hA`, where `hA` is the
   model's real-Hermitian proof.
3. Apply `hasEigenvalue_iSup_of_finiteDimensional` to obtain an eigenpair
   `(lambda, x)` with `x ≠ 0` and `T x = lambda • x`.
4. Prove that the Rayleigh quotient at this eigenvector is exactly the
   supremum `lambda`. This follows by unfolding the eigenvector equation
   in the inner product and using `x ≠ 0`; the scalar identity must be
   written explicitly in Lean.
5. Let `y` be the coordinatewise absolute-value vector. ECB-03 gives
   `‖y‖ = ‖x‖ > 0`; ECB-04/05 gives
   `⟪T x,x⟫ ≤ ⟪T y,y⟫`. Since the Rayleigh quotient of every nonzero
   vector is bounded above by the same supremum, and `x` attains it,
   the two quadratic forms on this common-radius sphere must be equal.
6. Thus `y` is also a maximizer of `reApplyInnerSelf` on
   `sphere 0 ‖y‖`. Apply
   `IsSelfAdjoint.hasEigenvector_of_isMaxOn` to the self-adjoint
   continuous operator corresponding to `T`, with `y ≠ 0`.
   This yields an eigenvector at the global Rayleigh supremum.
7. Translate the resulting continuous-linear-map eigenvector equation
   through `Matrix.toLpLin_apply` / `Matrix.toEuclideanLin` to the
   coordinate equation
   `∀ s, ∑ t, A s t * y t = lambda * y s`.
   Then invoke the already-existing
   `shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive`.

### Important qualification

The above is a source-grounded proof architecture, not verified Lean code.
The exact coercions between the linear map, its continuous-linear-map
self-adjoint wrapper, the Euclidean vector, and the coordinate function
still need scratch-module compilation. In addition, the finite-dimensional
instance `Nontrivial (EuclideanSpace ℝ (SpinConfig N))` must be discharged
explicitly for the full stated range of `N`; it must not be silently
assumed. The supremum/eigenpair equality and the translation back to the
matrix coordinate equation are separate Lean proof obligations.

This route constructs a nonnegative eigenvector at the largest Rayleigh
eigenvalue. It still does not, by itself, prove algebraic simplicity or
ground-state transfer.
