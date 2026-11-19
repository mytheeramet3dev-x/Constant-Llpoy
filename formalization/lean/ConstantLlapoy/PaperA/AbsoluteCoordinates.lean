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

/-- ECB-03 scalar core: absolute value preserves nonzeroness. -/
theorem absoluteValue_ne_zero_iff (r : ℝ) : |r| ≠ 0 ↔ r ≠ 0 := by
  simp
/-- ECB-03 coordinate core: taking absolute value preserves coordinate nonzeroness. -/
theorem absoluteCoordinate_ne_zero_iff {ι : Type*} (x : ι → ℝ) (i : ι) :
    absoluteCoordinateVector x i ≠ 0 ↔ x i ≠ 0 := by
  simp [absoluteCoordinateVector]
/-- ECB-03: the absolute-coordinate transformation preserves vector nonzeroness.
This statement also handles the empty index type, where the unique vector is zero. -/
theorem absoluteCoordinateVector_ne_zero_iff {ι : Type*} (x : ι → ℝ) :
    absoluteCoordinateVector x ≠ 0 ↔ x ≠ 0 := by
  constructor
  · intro h_abs h_x
    apply h_abs
    subst x
    rfl
  · intro h_x h_abs
    apply h_x
    funext i
    have hi := congrFun h_abs i
    have h_coord : |x i| = 0 := by
      simpa [absoluteCoordinateVector] using hi
    exact abs_eq_zero.mp h_coord

/-- ECB-02 bridge: Euclidean norm defined from the finite sum of coordinate squares. This is intentionally distinct from the default norm on function spaces. -/
noncomputable def absoluteCoordinateEuclideanNorm {ι : Type*} [Fintype ι] (x : ι → ℝ) : ℝ :=
  Real.sqrt (∑ i, (x i) ^ 2)
/-- ECB-02: the coordinatewise absolute-value transform preserves this Euclidean norm. -/
theorem absoluteCoordinateVector_euclideanNorm {ι : Type*} [Fintype ι]
    (x : ι → ℝ) :
    absoluteCoordinateEuclideanNorm (absoluteCoordinateVector x) =
      absoluteCoordinateEuclideanNorm x := by
  unfold absoluteCoordinateEuclideanNorm
  rw [absoluteCoordinateVector_sum_sq]

end ConstantLlapoy.PaperA
