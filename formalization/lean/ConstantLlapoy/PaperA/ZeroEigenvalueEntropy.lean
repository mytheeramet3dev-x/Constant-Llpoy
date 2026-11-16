import Mathlib
import ConstantLlapoy.PaperA.WeakCoupling

namespace ConstantLlapoy.PaperA

/-- A positive eigenvalue branch whose logarithm is controlled from both sides
has an entropy derivative bounded by its parameter derivative times a
logarithmic factor.

The hypotheses hlog and hf' are explicit analytical obligations:
in applications they must be proved from a uniform lower/upper eigenvalue
factorization and a differentiated perturbation estimate. This lemma does not
derive either estimate from analyticity by itself. -/
theorem entropy_derivative_bound_of_log_control
    {f : ℝ → ℝ} {f' x r A B : ℝ} {m : ℕ}
    (hA : 0 ≤ A)
    (hlog : |Real.log (f x)| ≤ A + (m : ℝ) * |Real.log r|)
    (hf' : |f'| ≤ B * r ^ m) :
    |(-(1 + Real.log (f x)) * f')| ≤
      B * r ^ m * (1 + A + (m : ℝ) * |Real.log r|) := by
  have hlogfactor :
      |1 + Real.log (f x)| ≤ 1 + A + (m : ℝ) * |Real.log r| := by
    have hlog_bounds := (abs_le.mp hlog)
    apply abs_le.mpr
    constructor
    · have hlow := hlog_bounds.1
      linarith
    · have hupp := hlog_bounds.2
      linarith
  have hfactor : 0 ≤ 1 + A + (m : ℝ) * |Real.log r| := by positivity
  calc
    |(-(1 + Real.log (f x)) * f')| =
        |1 + Real.log (f x)| * |f'| := by rw [abs_mul, abs_neg]
    _ ≤ (1 + A + (m : ℝ) * |Real.log r|) * (B * r ^ m) :=
      mul_le_mul hlogfactor hf' (abs_nonneg _) (by positivity)
    _ = B * r ^ m * (1 + A + (m : ℝ) * |Real.log r|) := by ring

/-- The entropy derivative bound together with the chain rule for
- f log f on a strictly positive eigenvalue branch. -/
theorem hasDerivAt_entropy_comp_with_bound
    {f : ℝ → ℝ} {f' x r A B : ℝ} {m : ℕ}
    (hf : HasDerivAt f f' x) (hpos : 0 < f x)
    (hA : 0 ≤ A)
    (hlog : |Real.log (f x)| ≤ A + (m : ℝ) * |Real.log r|)
    (hf'bound : |f'| ≤ B * r ^ m) :
    HasDerivAt (fun t => -(f t * Real.log (f t)))
      (-(1 + Real.log (f x)) * f') x ∧
    |(-(1 + Real.log (f x)) * f')| ≤
      B * r ^ m * (1 + A + (m : ℝ) * |Real.log r|) := by
  constructor
  · exact hasDerivAt_neg_mul_log_comp hf hpos
  · exact entropy_derivative_bound_of_log_control hA hlog hf'bound

/-- A differentiable nonnegative eigenvalue branch that vanishes at an
interior parameter value has zero first derivative there.

This is only a statement about the eigenvalue branch itself. It does not,
without a higher-order vanishing estimate, imply differentiability of
- f log f at the zero branch. -/
theorem hasDerivAt_nonnegative_branch_eq_zero
    {f : ℝ → ℝ} {f' x : ℝ}
    (hf : HasDerivAt f f' x)
    (hzero : f x = 0)
    (hnonneg : ∀ᶠ t in Filter.nhds x, 0 ≤ f t) :
    f' = 0 := by
  have hmin : IsLocalMin f x := by
    change ∀ᶠ t in Filter.nhds x, f x ≤ f t
    simpa [hzero] using hnonneg
  exact hmin.hasDerivAt_eq_zero hf

end ConstantLlapoy.PaperA
