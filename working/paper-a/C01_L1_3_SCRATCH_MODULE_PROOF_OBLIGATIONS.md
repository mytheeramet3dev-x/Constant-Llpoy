# C01-L1.3 — Scratch Module Proof-Obligation Breakdown

- **Doc ID:** CL-PA-C01-L1.3-SCRATCH-PO-001
- **Version:** 0.1.0
- **Status:** DECLARATION DESIGN ONLY; NOT LEAN-COMPILED
- **Scope:** C01-L1 Rayleigh existence construction
- **No production files modified.**

## 1. Verified context

The project's existing source contains the nonnegative quadratic-form absolute-value inequality
`quadratic_form_le_abs_quadratic_form` in `PerronFrobeniusCore.lean`, and the shifted TFIM's nonnegativity, Hermitian property, positive-support connectivity, and nonnegative-eigenvector strict positivity propagation in `HamiltonianEncoding.lean`.

Pinned Mathlib is commit `96f6b8b8e029545577421f198a89fb174a4d62e6`. Project Lean is `v4.36.0`. No Lean or Lake executable is available in this working execution environment. The exact declaration snippets below are proof targets, not purported compilable Lean.

## 2. Minimal declaration sequence

### ECB-01 — coordinate absolute value

Mathematical target:
[
y_s=|x_s|.
]
Use a Euclidean-space coordinate lift, not a raw function unless coercions are resolved.

Expected obligation: prove the coordinate rewrite lemma that `y s = |x s|`.

**Risk:** high coercion ambiguity between `EuclideanSpace`, `WithLp 2`, and `Fin N → Bool → ℝ` (the actual index is `SpinConfig N`).

### ECB-02 — pointwise positivity

For all `s`, `0 ≤ y s`, directly from `abs_nonneg`.

This should remain independent of norm proof.

### ECB-03 — norm preservation

Target:
[
\|y\|^2=\|x\|^2,qquad \|y\|=\|x\|.
]
Coordinate route:
[
\sum_s |x_s|^2=\sum_s x_s^2.
]
Use `sq_abs` coordinatewise, then equality of squared norms, then nonnegativity of norms. Avoid introducing an assumption `x ≠ 0` just to prove norm preservation.

### ECB-04 — quadratic form identity

For real matrix `A`, identify:
[
\operatorname{re}\langle A.toEuclideanLin(x),x\rangle
=\sum_s\sum_t A_{st}x_sx_t.
]
Mathlib source inspected at pinned revision shows the matrix-vector application through `Matrix.toLpLin_apply` and the real inner-product coordinate identity. The exact rewrite chain and coercion normalization remain to be compiled.

**Important:** The theorem is about real `A`; the complex conjugation/star convention is not to be silently copied. For this project, real coordinates let the star reduce to identity.

### ECB-05 — quadratic comparison

Apply the existing theorem:
`quadratic_form_le_abs_quadratic_form A x hA`.

Rewrite its left side using ECB-04 at `x`, and its right side using ECB-04 at `y`. The comparison should have no new mathematical assumptions beyond `hA : ∀ s t, 0 ≤ A s t`.

### ECB-06 — nonzero preservation

If `x ≠ 0`, then `y ≠ 0`. Use ECB-03: if `y = 0`, its norm is zero; norm equality would force `‖x‖=0`, contradicting `x ≠ 0`.

Do not replace this with a coordinate witness unless that makes the Lean proof simpler and is separately checked.

### ECB-07 — maximizer transfer

Let `R(x)=Q(x)/‖x‖²` for nonzero vectors. If `x` maximizes R over nonzero vectors, `‖y‖=‖x‖`, and `Q(x)≤Q(y)`, then maximality of x gives `R(y)≤R(x)`, while comparison gives `R(x)≤R(y)`. Hence equality and y also maximizes.

Lean implementation should prefer Mathlib's actual Rayleigh quotient and its exact domain rather than introduce a custom quotient definition unless necessary. This target depends on ECB-03, ECB-05, ECB-06, and the Rayleigh API.

### ECB-08 — eigenvector from maximizing point

Use the pinned theorem `IsSelfAdjoint.hasEigenvector_of_isMaxOn` or the verified finite-dimensional symmetric-operator route. Inputs must be explicitly aligned:
- operator is self-adjoint/symmetric;
- maximizer belongs to the theorem's specified sphere/subtype;
- nonzero/norm constraint;
- maximum predicate has the exact Rayleigh form.

Do not assume the returned eigenvalue is already the largest entry in the manuscript's chosen eigenvalue ordering; that bridge is a separate obligation.

### ECB-09 — matrix-coordinate eigen-equation

Convert the Euclidean operator equation back into:
[
\sum_t K_{st}v_t=\lambda v_s.
]
The existing model theorem expects exactly this coordinate form. Verify the equivalence using `Matrix.toLpLin_apply` / `ofLp`, not by asserting it.

## 3. Finite-dimensionality and edge cases

- `SpinConfig N` is finite because it is `Fin N → Bool`; confirm the local `Fintype` instance is available where the declaration is placed.
- At `N=0`, the index type is a singleton empty function; do not assume the sphere is nonempty without proving it.
- A nonzero Rayleigh maximizer requires a nontrivial vector space. The theorem should either carry a precise `Nontrivial` condition or discharge it for the actual finite configuration space.
- The project PF target may be valid for every finite N, but the L1 construction must explicitly handle the vector-space edge case. Do not silently restrict N to positive if the target theorem claims N≥0.

## 4. Proof order and failure isolation

Build and test one declaration per commit (or at minimum per isolated scratch file):
1. ECB-01 + ECB-02
2. ECB-03
3. ECB-04
4. ECB-05
5. ECB-06
6. ECB-07
7. ECB-08
8. ECB-09

If ECB-04 coercions fail, stop there and keep the earlier proofs intact. Avoid a monolithic proof whose first compiler error obscures all later obligations.

## 5. Acceptance criteria for L1

L1 is not complete until:
- every ECB declaration compiles at the pinned toolchain;
- the top-Rayleigh eigenvector construction has no extra mathematical assumptions hidden in helper lemmas;
- the resulting vector is explicitly nonzero and coordinatewise nonnegative;
- its eigenvalue is proved to be the top spectral value used by the intended theorem;
- the coordinate equation exactly matches the existing strict-positivity propagation theorem;
- an axiom/dependency audit is run and reviewed;
- a fresh CI result is attached to the exact commit.

## 6. Current status

| Obligation | Status |
|---|---|
| ECB-01 coordinate abs | OPEN |
| ECB-02 pointwise nonnegative | Proof straightforward; not compiled |
| ECB-03 norm preservation | OPEN |
| ECB-04 inner product ↔ double sum | Source API inspected; exact Lean rewrite OPEN |
| ECB-05 comparison | Depends on ECB-04; OPEN |
| ECB-06 nonzero preservation | Depends on ECB-03; OPEN |
| ECB-07 maximizer transfer | OPEN |
| ECB-08 maximizer → eigenvector | API located; exact application OPEN |
| ECB-09 matrix eigen-equation | OPEN |
| Lean build | NOT RUN |
| Axiom audit | NOT RUN |

## 7. Disposition

This is a more granular proof plan than C01-L1.2, not new verification evidence. No Lean code has been compiled, no proof has been accepted by Lean, and no production source was modified. C01-L1 remains **IN PROGRESS — NOT VERIFIED**. THM-0002 and Paper A remain **NOT VERIFIED**.
