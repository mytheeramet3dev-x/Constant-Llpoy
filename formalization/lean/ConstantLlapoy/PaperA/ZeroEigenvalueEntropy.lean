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
    calc
      |1 + Real.log (f x)| ≤ |(1 : ℝ)| + |Real.log (f x)| :=
        abs_add _ _
      _ ≤ 1 + (A + (m : ℝ) * |Real.log r|) := by
        simpa using add_le_add_left hlog 1
      _ = 1 + A + (m : ℝ) * |Real.log r| := by ring
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
  · exact entropy_derivative_bound_of_log_control
      hA hlog hf'bound

end ConstantLlapoy.PaperA
