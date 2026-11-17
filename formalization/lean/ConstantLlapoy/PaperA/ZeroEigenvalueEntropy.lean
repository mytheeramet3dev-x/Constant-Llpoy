import Mathlib
import ConstantLlapoy.PaperA.WeakCoupling

open scoped Topology

namespace ConstantLlapoy.PaperA

/-- Exact cancellation of the quadratic Schur term in the plus parity block.
This certifies only the displayed leading-order algebra
(S = (b₁+b₂)²/2, X = (b₁+b₂)/2, L = 1/2);
it does not establish that the physical reduced-state entries have these
expansions or control their remainders. -/
theorem plus_parity_leading_schur_cancellation
    (b₁ b₂ : ℝ) :
    (b₁ + b₂) ^ 2 / 2 -
      (((b₁ + b₂) / 2) ^ 2) / (1 / 2 : ℝ) = 0 := by
  ring

/-- Exact cancellation of the quadratic Schur term in the minus parity block.
As above, this is an algebraic identity for the leading coefficients only;
the model-specific expansion and differentiated remainder remain separate
obligations. -/
theorem minus_parity_leading_schur_cancellation
    (b₁ b₂ : ℝ) :
    (b₁ - b₂) ^ 2 / 2 -
      (((b₁ - b₂) / 2) ^ 2) / (1 / 2 : ℝ) = 0 := by
  ring


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


/-- Analyticity of the scalar quotient gives a locally bounded Fréchet
derivative. The bound is stated in operator norm, so it applies uniformly
to every unit parameter direction. This is the regularity input needed
before transferring a derivative estimate through the factor r^m.

The result is local in the parameter at zero; it is not yet a joint
uniform estimate in the radial variable r and an auxiliary parameter u. -/
theorem exists_eventually_fderiv_norm_bound_of_analyticAt
    {g : ℝ → ℝ}
    (hg : AnalyticAt ℝ g 0) :
    ∃ B : ℝ, 0 ≤ B ∧
      ∀ᶠ u : ℝ in 𝓝 0, ‖fderiv ℝ g u‖ ≤ B := by
  have hC1 : ContDiffAt ℝ 1 g 0 := hg.contDiffAt
  have hcont : ContinuousAt (fderiv ℝ g) 0 :=
    hC1.continuousAt_fderiv (by norm_num)
  obtain ⟨δ, hδ, hδbound⟩ :=
    Metric.continuousAt_iff.mp hcont 1 (by norm_num)
  let B : ℝ := ‖fderiv ℝ g 0‖ + 1
  refine ⟨B, by positivity, ?_⟩
  filter_upwards [Metric.ball_mem_nhds 0 hδ] with u hu
  have hdist : dist (fderiv ℝ g u) (fderiv ℝ g 0) < 1 :=
    hδbound hu
  have hnorm :
      ‖fderiv ℝ g u‖ ≤
        ‖fderiv ℝ g u - fderiv ℝ g 0‖ + ‖fderiv ℝ g 0‖ := by
    calc
      ‖fderiv ℝ g u‖ =
          ‖(fderiv ℝ g u - fderiv ℝ g 0) + fderiv ℝ g 0‖ := by
            congr 1
            abel
      _ ≤ _ := norm_add_le _ _
  have hdistnorm :
      ‖fderiv ℝ g u - fderiv ℝ g 0‖ < 1 := by
    simpa [dist_eq_norm] using hdist
  dsimp [B]
  linarith


/-- A jointly continuous auxiliary-parameter derivative is uniformly bounded
on any compact subset of the (radial, auxiliary-parameter) plane.

The continuity of the partial derivative is an explicit hypothesis. In an
application it must be derived from the joint regularity of the quotient
function; pointwise analyticity in the auxiliary parameter alone is not
silently promoted to joint continuity. -/
theorem exists_uniform_partial_deriv_bound_on_compact_of_continuousOn
    {g : ℝ × ℝ → ℝ} {K : Set (ℝ × ℝ)}
    (hK : IsCompact K)
    (hcont : ContinuousOn
      (fun p : ℝ × ℝ => deriv (fun u : ℝ => g (p.1, u)) p.2) K) :
    ∃ B : ℝ, 0 ≤ B ∧
      ∀ p ∈ K,
        |deriv (fun u : ℝ => g (p.1, u)) p.2| ≤ B := by
  obtain ⟨C, hC⟩ := hK.exists_bound_of_continuousOn hcont
  refine ⟨max C 0, le_max_right C 0, ?_⟩
  intro p hp
  have hnorm := hC p hp
  rw [Real.norm_eq_abs] at hnorm
  exact hnorm.trans (le_max_left C 0)


/-- A jointly C¹ quotient has a uniformly bounded full Fréchet derivative
on every compact subset of its parameter domain.

Unlike a family of pointwise one-variable estimates, this theorem starts
from joint C¹ regularity of g on ℝ × ℝ. The norm bound controls every
direction simultaneously. It remains an abstract compact-set result:
an application must identify a compact neighborhood on which the physical
quotient is jointly C¹. -/
theorem exists_uniform_fderiv_norm_bound_on_compact_of_contDiff
    {g : ℝ × ℝ → ℝ} {K : Set (ℝ × ℝ)}
    (hK : IsCompact K)
    (hg : ContDiff ℝ 1 g) :
    ∃ B : ℝ, 0 ≤ B ∧
      ∀ p ∈ K, ‖fderiv ℝ g p‖ ≤ B := by
  have hcont : Continuous (fderiv ℝ g) :=
    hg.continuous_fderiv (by norm_num)
  have hcontOn : ContinuousOn (fderiv ℝ g) K := hcont.continuousOn
  obtain ⟨C, hC⟩ := hK.exists_bound_of_continuousOn hcontOn
  refine ⟨max C 0, le_max_right C 0, ?_⟩
  intro p hp
  exact (hC p hp).trans (le_max_left C 0)


/-- A continuous, strictly positive leading coefficient on a nonempty compact
parameter set has a uniform strictly positive lower bound.

This is the compactness step needed to prevent the leading coefficient in a
fixed-order eigenvalue factorization from approaching zero as the auxiliary
parameter varies. It does not establish that the physical eigenvalue branch
has a common vanishing order or a continuous leading-coefficient map. -/
theorem exists_uniform_positive_lower_bound_on_compact
    {a : ℝ → ℝ} {K : Set ℝ}
    (hK : IsCompact K)
    (hne : K.Nonempty)
    (hcont : ContinuousOn a K)
    (hpos : ∀ u ∈ K, 0 < a u) :
    ∃ c : ℝ, 0 < c ∧ ∀ u ∈ K, c ≤ a u := by
  obtain ⟨u₀, hu₀, hmin⟩ := hK.exists_isMinOn hne hcont
  refine ⟨a u₀, hpos u₀ hu₀, ?_⟩
  intro u hu
  exact hmin hu


/-- Conditional transfer of an order-ε⁴ numerator estimate through a
uniformly bounded inverse Schur pivot.

This isolates the final algebraic estimate after the model-specific entry
remainders have been combined. The hypotheses deliberately expose both
missing analytical inputs: the numerator estimate and the inverse-pivot
bound. It does not derive either one from the TFIM Hamiltonian. -/
theorem parity_block_schur_remainder_bound_of_numerator_and_inverse_bound
    {num invL ε C D : ℝ}
    (hC : 0 ≤ C)
    (hD : 0 ≤ D)
    (hε : 0 ≤ ε)
    (hnum : |num| ≤ C * ε ^ 4)
    (hinv : |invL| ≤ D) :
    |num * invL| ≤ (C * D) * ε ^ 4 := by
  calc
    |num * invL| = |num| * |invL| := abs_mul num invL
    _ ≤ (C * ε ^ 4) * D :=
      mul_le_mul hnum hinv (abs_nonneg invL) (by positivity)
    _ = (C * D) * ε ^ 4 := by ring



/-- Conditional differentiated transfer for a Schur remainder written as
numerator times inverse pivot.

If both the numerator and its edge derivative are O(ε⁴), while the inverse
pivot and its edge derivative are uniformly bounded, then the Schur
remainder's edge derivative is O(ε⁴). All four bounds are explicit
hypotheses: this lemma does not establish them for the TFIM reduced state. -/
theorem hasDerivAt_parity_block_schur_remainder_bound
    {num invL : ℝ → ℝ} {num' invL' u ε Cn Cn' D D' : ℝ}
    (hnum : HasDerivAt num num' u)
    (hinv : HasDerivAt invL invL' u)
    (hε : 0 ≤ ε)
    (hCn : 0 ≤ Cn)
    (hCn' : 0 ≤ Cn')
    (hD : 0 ≤ D)
    (hD' : 0 ≤ D')
    (hnumValue : |num u| ≤ Cn * ε ^ 4)
    (hnumDeriv : |num'| ≤ Cn' * ε ^ 4)
    (hinvValue : |invL u| ≤ D)
    (hinvDeriv : |invL'| ≤ D') :
    HasDerivAt (fun v => num v * invL v)
      (num' * invL u + num u * invL') u ∧
    |num' * invL u + num u * invL'| ≤
      (Cn' * D + Cn * D') * ε ^ 4 := by
  constructor
  · exact hnum.mul hinv
  · have hε4 : 0 ≤ ε ^ 4 := by positivity
    calc
      |num' * invL u + num u * invL'| ≤
          |num' * invL u| + |num u * invL'| := abs_add_le _ _
      _ = |num'| * |invL u| + |num u| * |invL'| := by
        rw [abs_mul, abs_mul]
      _ ≤ (Cn' * ε ^ 4) * D + (Cn * ε ^ 4) * D' := by
        apply add_le_add
        · exact mul_le_mul hnumDeriv hinvValue
            (abs_nonneg (invL u)) (by positivity)
        · exact mul_le_mul hnumValue hinvDeriv
            (abs_nonneg invL') (by positivity)
      _ = (Cn' * D + Cn * D') * ε ^ 4 := by ring


end ConstantLlapoy.PaperA


/-- Exact remainder identity for a parity-block Schur complement.

Write the leading entries as
  L = 1/2 + ell,  X = t/2 + x,  S = t^2/2 + s.
The leading quadratic terms cancel, leaving precisely the displayed
combination of the entry remainders. This identity is algebraic only:
model-specific bounds on ell, x, and s (including their edge derivatives)
must still be established separately. -/
theorem parity_block_schur_remainder_identity
    {t x s ell : ℝ}
    (hL : (1 / 2 : ℝ) + ell ≠ 0) :
    (t ^ 2 / 2 + s) - (t / 2 + x) ^ 2 / ((1 / 2 : ℝ) + ell) =
      (s * ((1 / 2 : ℝ) + ell) -
        (t * x + x ^ 2 - t ^ 2 * ell / 2)) /
        ((1 / 2 : ℝ) + ell) := by
  have hD : 1 + 2 * ell ≠ 0 := by
    intro h
    apply hL
    nlinarith
  field_simp [hD] <;> ring
