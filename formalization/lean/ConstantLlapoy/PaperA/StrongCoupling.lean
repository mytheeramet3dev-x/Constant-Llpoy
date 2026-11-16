import ConstantLlapoy.PaperA.WeakCoupling

namespace ConstantLlapoy.PaperA

/-- Leading coefficient in the fixed-N strong-coupling asymptotic for B - C. -/
noncomputable def strongCouplingCoefficient (N : ℕ) : ℝ :=
  1 / ((N : ℝ) - 1) ^ 3

/-- The strong-coupling leading coefficient is positive for every N ≥ 4. -/
theorem strongCouplingCoefficient_pos (N : ℕ) (hN : 4 ≤ N) :
    0 < strongCouplingCoefficient N := by
  unfold strongCouplingCoefficient
  have hNreal : (4 : ℝ) ≤ (N : ℝ) := by
    exact_mod_cast hN
  have hden : 0 < (N : ℝ) - 1 := by
    linarith
  exact div_pos (by norm_num) (pow_pos hden 3)

/-- Strong-coupling endpoint sign, conditional on an explicit remainder bound.

The theorem formalizes only the final sign inference. It does not prove the
strong-coupling asymptotic or its differentiated remainder estimate. -/
theorem strongCoupling_response_positive_of_remainder
    (N : ℕ) (hN : 4 ≤ N) (scale error : ℝ)
    (hscale : 0 < scale)
    (herr : |error| ≤ strongCouplingCoefficient N * scale / 2) :
    0 < strongCouplingCoefficient N * scale + error := by
  exact positive_of_half_relative_error
    (strongCouplingCoefficient_pos N hN) hscale herr

end ConstantLlapoy.PaperA
