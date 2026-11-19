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

/-- ECB-01: the absolute-coordinate transform is the pointwise absolute value. -/
theorem absoluteCoordinateVector_abs {ι : Type*} (x : ι → ℝ) :
    ∀ i, absoluteCoordinateVector x i = |x i| := by
  intro i
  rfl

/-- The square of a real number is unchanged by taking its absolute value. -/
theorem absoluteValue_square_eq_square (r : ℝ) : |r| ^ 2 = r ^ 2 := by
  by_cases hr : 0 ≤ r
  · rw [abs_of_nonneg hr]
  · rw [abs_of_neg (lt_of_not_ge hr)]
    ring

/-- ECB-02 algebraic core: coordinatewise absolute values preserve squares. -/
theorem absoluteCoordinateVector_square {ι : Type*} (x : ι → ℝ) :
    ∀ i, (absoluteCoordinateVector x i) ^ 2 = (x i) ^ 2 := by
  intro i
  exact absoluteValue_square_eq_square (x i)

/-- ECB-02 finite-sum core: taking absolute values preserves the sum of squares. -/
theorem absoluteCoordinateVector_sum_sq {ι : Type*} [Fintype ι] (x : ι → ℝ) :
    (∑ i, (absoluteCoordinateVector x i) ^ 2) = ∑ i, (x i) ^ 2 := by
  apply Finset.sum_congr rfl
  intro i hi
  exact absoluteCoordinateVector_square x i

end ConstantLlapoy.PaperA
