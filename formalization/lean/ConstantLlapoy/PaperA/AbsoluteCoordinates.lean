import Mathlib

namespace ConstantLlapoy.PaperA

/-- ECB-01: the coordinatewise absolute-value transform on real vectors. -/
def absoluteCoordinateVector {ι : Type*} (x : ι → ℝ) : ι → ℝ :=
  fun i => |x i|

/-- ECB-01: every coordinate of the absolute-coordinate vector is nonnegative. -/
theorem absoluteCoordinateVector_nonneg {ι : Type*} (x : ι → ℝ) :
    ∀ i, 0 ≤ absoluteCoordinateVector x i := by
  intro i
  exact abs_nonneg (x i)

/-- ECB-02: the absolute-coordinate transform preserves pointwise absolute values. -/
theorem absoluteCoordinateVector_abs {ι : Type*} (x : ι → ℝ) :
    ∀ i, absoluteCoordinateVector x i = |x i| := by
  intro i
  rfl

end ConstantLlapoy.PaperA
