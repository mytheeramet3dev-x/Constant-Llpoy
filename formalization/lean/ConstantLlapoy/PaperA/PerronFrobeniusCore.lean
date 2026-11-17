import Mathlib

namespace ConstantLlapoy.PaperA

/-- At a maximum coordinate, a convex weighted average can equal the maximum
only if every coordinate with strictly positive weight also attains that
maximum. This is the finite weighted-average propagation step used in the
ratio proof of uniqueness for a positive Perron eigenvector. -/
theorem weighted_average_at_max_forces_positive_weight_coordinates_equal
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    (w t : ι → ℝ) (i : ι)
    (hw_nonneg : ∀ j, 0 ≤ w j)
    (hw_sum : ∑ j, w j = 1)
    (ht_max : ∀ j, t j ≤ t i)
    (ht_average : ∑ j, w j * t j = t i) :
    ∀ j, 0 < w j → t j = t i := by
  classical
  have hsum_zero : ∑ j, w j * (t i - t j) = 0 := by
    calc
      ∑ j, w j * (t i - t j)
          = (∑ j, w j) * t i - ∑ j, w j * t j := by
              simp_rw [mul_sub]
              rw [Finset.sum_sub_distrib, ← Finset.sum_mul]
      _ = 0 := by rw [hw_sum, ht_average]; ring
  have hterms_nonneg : ∀ j ∈ (Finset.univ : Finset ι),
      0 ≤ w j * (t i - t j) := by
    intro j hj
    exact mul_nonneg (hw_nonneg j) (sub_nonneg.mpr (ht_max j))
  have hterms_zero := (Finset.sum_eq_zero_iff_of_nonneg hterms_nonneg).mp hsum_zero
  intro j hj
  have hzero : w j * (t i - t j) = 0 :=
    hterms_zero j (Finset.mem_univ j)
  have hdiff : t i - t j = 0 :=
    (mul_eq_zero.mp hzero).resolve_left (ne_of_gt hj)
  linarith

end ConstantLlapoy.PaperA
