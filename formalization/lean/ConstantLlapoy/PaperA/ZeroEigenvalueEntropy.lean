import Mathlib
import ConstantLlapoy.PaperA.WeakCoupling

open scoped Topology

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

/-- A differentiable function at a local minimum has zero derivative.

For a nonnegative eigenvalue branch vanishing at an interior point,
nonnegativity on a two-sided neighborhood implies the local-minimum
hypothesis. That topological conversion is intentionally kept separate
until the pinned Mathlib filter API is verified.

This is only a statement about the eigenvalue branch itself. It does not,
without a higher-order vanishing estimate, imply differentiability of
- f log f at the zero branch. -/
theorem hasDerivAt_local_min_branch_eq_zero
    {f : ℝ → ℝ} {f' x : ℝ}
    (hf : HasDerivAt f f' x)
    (hmin : IsLocalMin f x) :
    f' = 0 := by
  exact hmin.hasDerivAt_eq_zero hf

/-- A nontrivial one-variable analytic branch admits a finite-order local
factorisation. This is the pinned Mathlib isolated-zero theorem specialized
to a real-valued branch at zero. The theorem does not yet use nonnegativity
to show that the order is even or that the leading coefficient is positive. -/
theorem exists_local_power_factorization_of_analytic_nontrivial
    {f : ℝ → ℝ}
    (hf : AnalyticAt ℝ f 0)
    (hnot : ¬ ∀ᶠ r : ℝ in 𝓝 0, f r = 0) :
    ∃ (m : ℕ) (g : ℝ → ℝ),
      AnalyticAt ℝ g 0 ∧ g 0 ≠ 0 ∧
      ∀ᶠ r : ℝ in 𝓝 0, f r = r ^ m * g r := by
  obtain ⟨m, g, hg, hg0, hfactor⟩ :=
    (hf.exists_eventuallyEq_pow_smul_ne_zero_iff).2 hnot
  refine ⟨m, g, hg, hg0, ?_⟩
  filter_upwards [hfactor] with r hr
  simpa [smul_eq_mul] using hr

/-- If a differentiable branch is nonnegative on a two-sided neighborhood
and vanishes at the center, its first derivative is zero. -/
theorem hasDerivAt_nonnegative_branch_eq_zero
    {f : ℝ → ℝ} {f' x : ℝ}
    (hf : HasDerivAt f f' x)
    (hzero : f x = 0)
    (hnonneg : ∀ᶠ t : ℝ in 𝓝 x, 0 ≤ f t) :
    f' = 0 := by
  have hmin : IsLocalMin f x := by
    change ∀ᶠ t : ℝ in 𝓝 x, f x ≤ f t
    simpa [hzero] using hnonneg
  exact hmin.hasDerivAt_eq_zero hf


/-- A negative-side witness rules out odd vanishing order when the branch
has a nonnegative factorization and a positive quotient at that witness.

This is the algebraic core of the parity argument. The separate topological
obligation is to obtain such a witness from eventual hypotheses near zero. -/
theorem even_order_of_negative_factorization_witness
    {f g : ℝ → ℝ} {m : ℕ} {r : ℝ}
    (hodd : Odd m)
    (hr : r < 0)
    (hg : 0 < g r)
    (hnonneg : 0 ≤ f r)
    (hfactor : f r = r ^ m * g r) :
    Even m := by
  have hnegbase : 0 < -r := neg_pos.mpr hr
  have hpowpos : 0 < (-r) ^ m := pow_pos hnegbase m
  have hpowneg : r ^ m < 0 := by
    have hrewrite : r = -(-r) := by ring
    rw [hrewrite, hodd.neg_pow]
    exact neg_neg_of_pos hpowpos
  have hproductneg : r ^ m * g r < 0 :=
    mul_neg_of_neg_of_pos hpowneg hg
  rw [hfactor] at hnonneg
  exact (not_le_of_gt hproductneg hnonneg).elim


/-- Continuity preserves strict positivity on some neighborhood of the
base point. This is the positive-sign half of ZF-2a. -/
theorem eventually_pos_of_continuousAt_of_pos
    {g : ℝ → ℝ}
    (hg : ContinuousAt g 0)
    (h0 : 0 < g 0) :
    ∀ᶠ r : ℝ in 𝓝 0, 0 < g r := by
  exact hg.eventually (Ioi_mem_nhds h0)

/-- Continuity preserves strict negativity on some neighborhood of the
base point. This is the negative-sign half of ZF-2a. -/
theorem eventually_neg_of_continuousAt_of_neg
    {g : ℝ → ℝ}
    (hg : ContinuousAt g 0)
    (h0 : g 0 < 0) :
    ∀ᶠ r : ℝ in 𝓝 0, g r < 0 := by
  exact hg.eventually (Iio_mem_nhds h0)


/-- A nonnegative branch cannot have a negative leading coefficient in a
finite-order factorization. The witness is chosen on the positive side,
where r^m is strictly positive for every natural m. -/
theorem positive_leading_coefficient_of_nonnegative_factorization
    {f g : ℝ → ℝ} {m : ℕ}
    (hg : ContinuousAt g 0)
    (hgne : g 0 ≠ 0)
    (hnonneg : ∀ᶠ r : ℝ in 𝓝 0, 0 ≤ f r)
    (hfactor : ∀ᶠ r : ℝ in 𝓝 0, f r = r ^ m * g r) :
    0 < g 0 := by
  rcases lt_or_gt_of_ne hgne with hneg | hpos
  · have hgneg : ∀ᶠ r : ℝ in 𝓝 0, g r < 0 :=
      eventually_neg_of_continuousAt_of_neg hg hneg
    have hbase : ∀ᶠ r : ℝ in 𝓝 0,
        g r < 0 ∧ 0 ≤ f r ∧ f r = r ^ m * g r := by
      filter_upwards [hgneg, hnonneg, hfactor] with r hgr hfr hfac
      exact ⟨hgr, hfr, hfac⟩
    obtain ⟨ε, hε, hevent⟩ := (Metric.eventually_nhds_iff.mp hbase)
    let r : ℝ := ε / 2
    have hrpos' : 0 < r := by
      dsimp [r]
      linarith
    have hdist : dist r 0 < ε := by
      rw [Real.dist_eq]
      simp only [sub_zero]
      rw [abs_of_pos hrpos']
      dsimp [r]
      linarith
    obtain ⟨hgr, hfr, hfac⟩ := hevent hdist
    have hrpow : 0 < r ^ m := pow_pos hrpos' m
    have hprod : r ^ m * g r < 0 := mul_neg_of_pos_of_neg hrpow hgr
    rw [hfac] at hfr
    exact (not_le_of_gt hprod hfr).elim
  · exact hpos


/-- Full ZF-2 conclusion for a nontrivial nonnegative analytic branch:
the finite vanishing order is even and the leading coefficient is positive.

The factorization, continuity, and nonnegativity hypotheses are stated
explicitly so that the theorem remains reusable independently of the
analytic factorization theorem. -/
theorem even_order_and_positive_leading_coefficient_of_nonnegative_factorization
    {f g : ℝ → ℝ} {m : ℕ}
    (hg : ContinuousAt g 0)
    (hgne : g 0 ≠ 0)
    (hnonneg : ∀ᶠ r : ℝ in 𝓝 0, 0 ≤ f r)
    (hfactor : ∀ᶠ r : ℝ in 𝓝 0, f r = r ^ m * g r) :
    Even m ∧ 0 < g 0 := by
  have hpos0 : 0 < g 0 :=
    positive_leading_coefficient_of_nonnegative_factorization
      hg hgne hnonneg hfactor
  have hgpos : ∀ᶠ r : ℝ in 𝓝 0, 0 < g r :=
    eventually_pos_of_continuousAt_of_pos hg hpos0
  have hbase : ∀ᶠ r : ℝ in 𝓝 0,
      0 < g r ∧ 0 ≤ f r ∧ f r = r ^ m * g r := by
    filter_upwards [hgpos, hnonneg, hfactor] with r hgr hfr hfac
    exact ⟨hgr, hfr, hfac⟩
  have hparity : Even m := by
    rcases Nat.even_or_odd m with heven | hodd
    · exact heven
    · obtain ⟨ε, hε, hevent⟩ := Metric.eventually_nhds_iff.mp hbase
      let r : ℝ := -ε / 2
      have hrneg : r < 0 := by
        dsimp [r]
        linarith
      have hdist : dist r 0 < ε := by
        rw [Real.dist_eq]
        simp only [sub_zero]
        rw [abs_of_neg hrneg]
        dsimp [r]
        linarith
      obtain ⟨hgr, hfr, hfac⟩ := hevent hdist
      exact even_order_of_negative_factorization_witness
        hodd hrneg hgr hfr hfac
  exact ⟨hparity, hpos0⟩


/-- A continuous quotient with positive value at the base point is bounded
above and bounded away from zero on a sufficiently small neighborhood.
This is the scalar local estimate needed before deriving two-sided bounds
for the factored eigenvalue branch. -/
theorem eventually_quotient_two_sided_bounds
    {g : ℝ → ℝ}
    (hg : ContinuousAt g 0)
    (h0 : 0 < g 0) :
    ∀ᶠ r : ℝ in 𝓝 0,
      g 0 / 2 < g r ∧ g r < (3 / 2) * g 0 := by
  have hleft : g 0 / 2 < g 0 := by nlinarith
  have hright : g 0 < (3 / 2) * g 0 := by nlinarith
  have hinterval : Set.Ioo (g 0 / 2) ((3 / 2) * g 0) ∈ 𝓝 (g 0) :=
    Ioo_mem_nhds hleft hright
  have hevent : ∀ᶠ r : ℝ in 𝓝 0,
      g r ∈ Set.Ioo (g 0 / 2) ((3 / 2) * g 0) :=
    hg.eventually hinterval
  filter_upwards [hevent] with r hr
  exact hr


/-- Transfer the local quotient bounds through an even-order factorization.
The evenness hypothesis is essential on a two-sided neighborhood: it makes
r^m nonnegative for negative as well as positive r. The resulting bounds are
non-strict because multiplication by r^m can be zero at r = 0. -/
theorem eventually_factored_branch_two_sided_bounds
    {f g : ℝ → ℝ} {m : ℕ}
    (hg : ContinuousAt g 0)
    (h0 : 0 < g 0)
    (heven : Even m)
    (hfactor : ∀ᶠ r : ℝ in 𝓝 0, f r = r ^ m * g r) :
    ∀ᶠ r : ℝ in 𝓝 0,
      r ^ m * (g 0 / 2) ≤ f r ∧
      f r ≤ r ^ m * ((3 / 2) * g 0) := by
  have hquot := eventually_quotient_two_sided_bounds hg h0
  filter_upwards [hquot, hfactor] with r hq hfac
  have hpow : 0 ≤ r ^ m := heven.pow_nonneg r
  have hlow :
      r ^ m * (g 0 / 2) ≤ r ^ m * g r :=
    mul_le_mul_of_nonneg_left (le_of_lt hq.1) hpow
  have hupp :
      r ^ m * g r ≤ r ^ m * ((3 / 2) * g 0) :=
    mul_le_mul_of_nonneg_left (le_of_lt hq.2) hpow
  rw [hfac]
  exact ⟨hlow, hupp⟩


/-- Differentiate a factored branch with respect to an auxiliary parameter.
For fixed r, the factor r^m is constant in that parameter. If m is even,
then r^m is nonnegative on both sides of zero, and a bound on the derivative
of the quotient transfers directly to the derivative of the full branch.

This is a conditional bridge: it does not establish the required bound on
the quotient derivative itself, nor uniformity of that bound in r or in
additional parameters. -/
theorem hasDerivAt_factored_parameter_branch_bound
    {g : ℝ → ℝ} {g' u r B : ℝ} {m : ℕ}
    (hg : HasDerivAt g g' u)
    (hg' : |g'| ≤ B)
    (heven : Even m) :
    HasDerivAt (fun v => r ^ m * g v) (r ^ m * g') u ∧
    |r ^ m * g'| ≤ B * r ^ m := by
  have hpow : 0 ≤ r ^ m := heven.pow_nonneg r
  constructor
  · exact HasDerivAt.const_mul (r ^ m) hg
  · calc
      |r ^ m * g'| = r ^ m * |g'| := by
        rw [abs_mul, abs_of_nonneg hpow]
      _ ≤ r ^ m * B :=
        mul_le_mul_of_nonneg_left hg' hpow
      _ = B * r ^ m := by ring

end ConstantLlapoy.PaperA
