# C01-L1 Rayleigh Construction — Refined Lean Implementation Design

- **Document ID:** CL-PA-C01-L1-DESIGN-001
- **Version:** 0.1.0
- **Branch:** `paper-a-mcr01-pf-redline`
- **Status:** DESIGN REVIEW; NO NEW LEAN THEOREM CLAIMED
- **Target:** Construct a nonzero coordinatewise nonnegative eigenvector of the actual shifted TFIM matrix at its largest eigenvalue.
- **Pinned Lean:** `leanprover/lean4:v4.36.0`
- **Pinned Mathlib:** `96f6b8b8e029545577421f198a89fb174a4d62e6`

## 1. Correction to the previous execution report

The previous C-01 execution report described the absolute-value quadratic-form inequality as not yet formalized. That description is too broad.

The working-branch file
`formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean`
already contains:

`quadratic_form_le_abs_quadratic_form`

with statement
`(∑ i, ∑ j, A i j * x i * x j) ≤ ∑ i, ∑ j, A i j * |x i| * |x j|`
under entrywise nonnegativity of A.

The theorem was inspected in the exact working-branch file (blob `d1553a8dbcf60aaec449a98d59e92ab91c1812ea`, as fetched in this audit session). It is source-present. This report does not assert a fresh Lean build of it.

Thus the scalar order inequality is already present; the remaining C01-L1 task is to connect it to the finite-dimensional Rayleigh maximizer in the Euclidean-space representation used by Mathlib's spectral API.

## 2. Pinned Mathlib APIs inspected

The exact pinned Mathlib source was fetched directly at commit `96f6b8b8e029545577421f198a89fb174a4d62e6`.

### 2.1 Rayleigh extremizer to eigenvector

File: `Mathlib/Analysis/InnerProductSpace/Rayleigh.lean`

Relevant exact declarations:
- `IsSelfAdjoint.hasEigenvector_of_isMaxOn`
- `LinearMap.IsSymmetric.hasEigenvalue_iSup_of_finiteDimensional`
- `ContinuousLinearMap.rayleighQuotient`
- `ContinuousLinearMap.iSup_rayleigh_eq_iSup_rayleigh_sphere`

The key theorem `IsSelfAdjoint.hasEigenvector_of_isMaxOn` takes:
- a self-adjoint continuous linear map (T);
- a nonzero vector (x_0);
- proof that (x_0) maximizes (T.reApplyInnerSelf) on the sphere of radius (|x_0|);

and returns an eigenvector at the global supremum of the Rayleigh quotient.

The finite-dimensional API obtains a maximizer by compactness of a sphere. Therefore the planned construction need not build compactness or a bespoke eigenvalue existence proof from scratch.

### 2.2 Matrix-to-Euclidean spectral bridge

File: `Mathlib/Analysis/Matrix/Spectrum.lean`

Relevant exact declarations inspected:
- `Matrix.IsHermitian.eigenvalues₀`
- `Matrix.IsHermitian.eigenvalues₀_antitone`
- `Matrix.IsHermitian.eigenvectorBasis`
- `Matrix.IsHermitian.mulVec_eigenvectorBasis`
- `Matrix.isSymmetric_toEuclideanLin_iff`
- `Matrix.spectrum_toLpLin`

The pinned source defines the Hermitian matrix eigenbasis through the symmetric linear operator on `EuclideanSpace`. This confirms the correct finite-dimensional representation to use and the ordering convention: the linear-map eigenvalue sequence is sorted in decreasing order.

### 2.3 Project configuration

The exact working-branch project files were inspected:
- `formalization/lean/lean-toolchain`: blob `00f848359b1cdaf7c12cd6b7acc5b4364752e154`, Lean v4.36.0.
- `formalization/lean/lakefile.lean`: blob `c135825a39770b3f26860aeae9983b8351d490f6`, Mathlib pinned to the revision above.

No build was run as part of this API inspection.

## 3. Refined proof architecture

Let (A=K) be the shifted TFIM matrix, indexed by the finite type `SpinConfig N`. The existing model file establishes:
- (A) is real symmetric / Hermitian;
- every entry is nonnegative for (h>0);
- its positive support is connected;
- every diagonal entry is strictly positive.

The intended route is:

### Step L1.1 — Obtain a Rayleigh maximizer

Move from the matrix (A) to its symmetric operator on
`EuclideanSpace ℝ (SpinConfig N)`.

Use finite-dimensional compactness of a sphere and continuity of the quadratic form to obtain a nonzero vector (x) maximizing
[
q(x)=\langle Ax,x\rangle
]
on its norm sphere.

This is the compactness step already used internally by Mathlib's finite-dimensional Rayleigh theorem. The implementation should reuse the exact pinned API rather than recreate a parallel spectral framework.

### Step L1.2 — Define the coordinatewise absolute-value vector

Define (y) by (y_i=|x_i|) in the same Euclidean space.

Prove:
1. (y_i\ge0) for all i.
2. (|y|=|x|), using the finite (ell^2) norm and (|x_i|^2=x_i^2).
3. (q(x)\le q(y)), by the already-present `quadratic_form_le_abs_quadratic_form`, after proving the exact coordinate expansion of the inner product quadratic form for the chosen Euclidean representation.

The coordinate-expansion bridge and the norm-preservation proof are explicit Lean obligations; neither should be hidden behind an unproved helper.

### Step L1.3 — Transfer maximality

Since x is a maximizer on its sphere, and y lies on the same sphere with (q(x)\le q(y)), y is also a maximizer.

This step must retain the exact sphere membership and the universal upper-bound statement. Merely proving the inequality between the two quadratic forms is insufficient.

### Step L1.4 — Invoke the pinned Rayleigh theorem

Apply `IsSelfAdjoint.hasEigenvector_of_isMaxOn` to y.

This yields an eigenvector at the global supremum of the Rayleigh quotient. Show y is nonzero from (|y|=|x|>0).

Translate the continuous-linear-map eigenvector equation back to the matrix equation
[
\sum_j A_{ij}y_j=\lambda y_i.
]

### Step L1.5 — Show the eigenvalue is the largest real eigenvalue

The Rayleigh theorem identifies the eigenvalue with the global supremum of the Rayleigh quotient. The real-symmetric spectral theorem identifies this supremum with the largest eigenvalue in the antitone eigenvalue list.

The implementation must state the precise list index and the `eigenvalues₀_antitone` ordering. Do not call an arbitrary eigenvalue “the Perron root.”

### Step L1.6 — Show strict positivity

Feed the nonzero nonnegative eigenvector into the already-present model theorem:
`shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive`.

This should discharge strict positivity using the existing nonnegativity and hypercube connectivity results, once the matrix eigen-equation has been translated correctly.

## 4. Important separation: existence versus simplicity

C01-L1 only constructs a nonzero nonnegative eigenvector at the top eigenvalue.

It does not by itself prove:
- uniqueness of the top eigenvector up to scalar;
- characteristic-root multiplicity one;
- spectral-radius equality in every formulation;
- the transfer to the ground eigenvalue of H.

The current ratio/Markov-kernel argument in `PerronFrobeniusCore.lean` is the separate simplicity mechanism once a strictly positive eigenpair is available. The existing model-level conditional characteristic-root theorem is downstream of that. Keep these obligations separate.

## 5. Mathematical sanity check for positivity of the top eigenvalue

The current model shift gives (A_{ss}>0) for every state. In particular, for any coordinate unit vector (e_s),
[
q(e_s)=A_{ss}>0.
]
Hence the maximal Rayleigh quotient is strictly positive.

This is a direct route to (lambda_{\max}>0), independent of off-diagonal edges. Formalization still needs to connect the chosen unit vector to the matrix quadratic form and the Rayleigh supremum.

## 6. Remaining implementation blockers to resolve before editing Lean

1. **Representation:** identify the exact coercions between `Matrix.toLpLin 2 2 A`, `EuclideanSpace ℝ κ`, and the `ContinuousLinearMap` required by the Rayleigh API.
2. **Coordinate expansion:** prove `reApplyInnerSelf` equals the finite double sum used by `quadratic_form_le_abs_quadratic_form`.
3. **Absolute-value vector:** construct it in `EuclideanSpace` and prove norm preservation and coordinatewise nonnegativity.
4. **Maximality transfer:** show the absolute-value vector lies on the same sphere and retains the maximum property.
5. **Eigen-equation translation:** turn the Rayleigh API's linear-map eigenvector into the exact matrix mulVec equation used by the existing TFIM theorems.
6. **Top-eigenvalue identity:** bind the supremum Rayleigh eigenvalue to the first entry of the antitone real eigenvalue list, with no ordering ambiguity.

A small standalone Lean scratch module importing Mathlib should be used to test the representation and coordinate lemmas before modifying the main model files. Any helper moved into the production module must then be built under the pinned project and checked by the configured axiom audit.

## 7. Status

- Absolute-value quadratic-form inequality: **SOURCE-PRESENT** (fresh build not asserted).
- Pinned Rayleigh extremizer API: **LOCATED**.
- Pinned matrix/Euclidean spectral bridge: **LOCATED**.
- Coordinatewise absolute-value Euclidean vector bridge: **OPEN**.
- Rayleigh maximizer to nonnegative matrix eigenvector: **NOT IMPLEMENTED**.
- Largest-eigenvalue identity: **OPEN**.
- C01-L1: **IN PROGRESS; NOT VERIFIED**.
- THM-0002: **NOT VERIFIED**.

## 8. Verification boundary

This document records source inspection and a proof architecture only. It does not report a Lean compilation, CI result, axiom audit, or independent formal verification. No upstream `Absolute_Sym` file was modified.
