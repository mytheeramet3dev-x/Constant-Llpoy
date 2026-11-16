import Mathlib

namespace ConstantLlapoy.PaperA

/-- The coefficient of the leading weak-coupling term for the edge response B - C. -/
noncomputable def weakCouplingCoefficient (N : ℕ) : ℝ :=
  Real.log (2 * ((N : ℝ) - 2) / ((N : ℝ) - 1)) / 8

/-- The logarithmic coefficient is strictly positive for every finite N ≥ 4. -/
theorem weakCouplingCoefficient_pos (N : ℕ) (hN : 4 ≤ N) :
    0 < weakCouplingCoefficient N := by
  unfold weakCouplingCoefficient
  have hNreal : (4 : ℝ) ≤ (N : ℝ) := by
    exact_mod_cast hN
  have hden : 0 < (N : ℝ) - 1 := by
    linarith
  have hratio : 1 < 2 * ((N : ℝ) - 2) / ((N : ℝ) - 1) := by
    apply (lt_div_iff₀ hden).2
    nlinarith
  exact div_pos (Real.log_pos hratio) (by norm_num)

/-- If the absolute remainder is at most half the positive leading term,
then the total expression is strictly positive. -/
theorem positive_of_half_relative_error {a scale error : ℝ}
    (ha : 0 < a) (hscale : 0 < scale)
    (herr : |error| ≤ a * scale / 2) :
    0 < a * scale + error := by
  have herr_lower : -(a * scale / 2) ≤ error := (abs_le.mp herr).1
  nlinarith

/-- Weak-coupling endpoint sign, conditional on an explicit remainder bound.

This theorem formalizes the algebraic sign step only. It does not prove that
the analytic asymptotic remainder eventually satisfies the stated bound; that
requires a separate formalization of the differentiated remainder. -/
theorem weakCoupling_response_positive_of_remainder
    (N : ℕ) (hN : 4 ≤ N) (scale error : ℝ)
    (hscale : 0 < scale)
    (herr : |error| ≤ weakCouplingCoefficient N * scale / 2) :
    0 < weakCouplingCoefficient N * scale + error := by
  exact positive_of_half_relative_error
    (weakCouplingCoefficient_pos N hN) hscale herr

/-- Derivative of the positive-eigenvalue entropy contribution
- f * log f, assuming the eigenvalue is strictly positive at the point. -/
theorem hasDerivAt_neg_mul_log_comp
    {f : ℝ → ℝ} {f' x : ℝ}
    (hf : HasDerivAt f f' x) (hpos : 0 < f x) :
    HasDerivAt (fun t => -(f t * Real.log (f t)))
      (-(1 + Real.log (f x)) * f') x := by
  have hid : HasDerivAt (fun y : ℝ => y) 1 (f x) :=
    hasDerivAt_id' (f x)
  have hlog : HasDerivAt (fun y : ℝ => Real.log y) ((f x)⁻¹) (f x) :=
    Real.hasDerivAt_log (ne_of_gt hpos)
  have hmul := hid.mul hlog
  have houter : HasDerivAt (fun y : ℝ => -(y * Real.log y))
      (-(1 + Real.log (f x))) (f x) := by
    convert hmul.neg using 1 <;> simp [ne_of_gt hpos] <;> ring
  have hcomp := houter.comp x hf
  simpa [Function.comp_def, add_comm] using hcomp

end ConstantLlapoy.PaperA
