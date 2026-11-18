import Mathlib
import ConstantLlapoy.PaperA.PerronFrobeniusCore

namespace ConstantLlapoy.PaperA

/-- Computational-basis configurations for an N-site spin-1/2 system. -/
abbrev SpinConfig (N : ℕ) := Fin N → Bool

/-- Unordered interaction edges, represented once by their increasing pair. -/
abbrev IsingEdge (N : ℕ) := {e : Fin N × Fin N // e.1 < e.2}

/-- The eigenvalue of sigma-z at site i in the computational basis. -/
def computationalSpinZ {N : ℕ} (s : SpinConfig N) (i : Fin N) : ℝ :=
  if s i then 1 else -1

/-- Flip exactly one computational-basis spin. -/
def flipAt {N : ℕ} (s : SpinConfig N) (i : Fin N) : SpinConfig N :=
  fun j => if j = i then !(s i) else s j

/-- Two configurations are adjacent when they differ at exactly one site. -/
def SingleSpinFlip {N : ℕ} (s t : SpinConfig N) : Prop :=
  ∃ i, t = flipAt s i

theorem flipAt_involutive {N : ℕ} (s : SpinConfig N) (i : Fin N) :
    flipAt (flipAt s i) i = s := by
  funext j
  by_cases hj : j = i
  · subst j
    simp [flipAt]
  · simp [flipAt, hj]

theorem singleSpinFlip_symm {N : ℕ} {s t : SpinConfig N}
    (h : SingleSpinFlip s t) : SingleSpinFlip t s := by
  rcases h with ⟨i, rfl⟩
  exact ⟨i, (flipAt_involutive s i).symm⟩

/-- The diagonal Ising interaction in the computational sigma-z basis.
The edge subtype ensures that each unordered pair is counted exactly once. -/
def isingDiagonalEnergy {N : ℕ}
    (J : IsingEdge N → ℝ) (s : SpinConfig N) : ℝ :=
  -∑ e : IsingEdge N,
    J e * computationalSpinZ s e.1.1 * computationalSpinZ s e.1.2

/-- Exact computational-basis matrix of the finite transverse-field Ising
Hamiltonian. The diagonal contains the pair interactions; an off-diagonal
entry is negative h exactly for a single-spin flip and zero otherwise. -/
noncomputable def transverseIsingHamiltonian {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) :
    Matrix (SpinConfig N) (SpinConfig N) ℝ := by
  classical
  exact fun s t =>
    if s = t then isingDiagonalEnergy J s
    else if SingleSpinFlip s t then -h else 0

theorem transverseIsingHamiltonian_isHermitian {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) :
    (transverseIsingHamiltonian J h).IsHermitian := by
  apply Matrix.IsHermitian.ext
  intro s t
  by_cases hst : s = t
  · subst t
    simp [transverseIsingHamiltonian]
  · have hts : t ≠ s := Ne.symm hst
    have hflip : SingleSpinFlip t s ↔ SingleSpinFlip s t := by
      constructor
      · exact singleSpinFlip_symm
      · exact singleSpinFlip_symm
    simp [transverseIsingHamiltonian, hst, hts]
    rw [hflip]

@[simp] theorem transverseIsingHamiltonian_diag {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (s : SpinConfig N) :
    transverseIsingHamiltonian J h s s = isingDiagonalEnergy J s := by
  simp [transverseIsingHamiltonian]

theorem transverseIsingHamiltonian_single_flip {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ)
    {s t : SpinConfig N} (hst : s ≠ t)
    (hflip : SingleSpinFlip s t) :
    transverseIsingHamiltonian J h s t = -h := by
  simp [transverseIsingHamiltonian, hst, hflip]

theorem transverseIsingHamiltonian_other_off_diagonal {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ)
    {s t : SpinConfig N} (hst : s ≠ t)
    (hflip : ¬ SingleSpinFlip s t) :
    transverseIsingHamiltonian J h s t = 0 := by
  simp [transverseIsingHamiltonian, hst, hflip]

/-- A finite scalar shift strictly above every diagonal entry of the
computational-basis Hamiltonian. The sum of absolute diagonal entries gives
an explicit bound without choosing an opaque maximum. -/
def isingShiftConstant {N : ℕ} (J : IsingEdge N → ℝ) : ℝ :=
  1 + ∑ s : SpinConfig N, |isingDiagonalEnergy J s|

theorem isingDiagonalEnergy_lt_shiftConstant {N : ℕ}
    (J : IsingEdge N → ℝ) (s : SpinConfig N) :
    isingDiagonalEnergy J s < isingShiftConstant J := by
  unfold isingShiftConstant
  have hsum :
      |isingDiagonalEnergy J s| ≤
        ∑ t : SpinConfig N, |isingDiagonalEnergy J t| := by
    exact Finset.single_le_sum
      (fun t ht => abs_nonneg (isingDiagonalEnergy J t))
      (Finset.mem_univ s)
  linarith [le_abs_self (isingDiagonalEnergy J s)]

/-- The shifted matrix K = cI - H, with c chosen strictly above all
diagonal entries. For h>0 its positive off-diagonal support is the
single-spin-flip graph. -/
noncomputable def shiftedTFIMHamiltonian {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) :
    Matrix (SpinConfig N) (SpinConfig N) ℝ := by
  classical
  exact fun s t =>
    (if s = t then isingShiftConstant J else 0) -
      transverseIsingHamiltonian J h s t

@[simp] theorem shiftedTFIMHamiltonian_diag {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (s : SpinConfig N) :
    shiftedTFIMHamiltonian J h s s =
      isingShiftConstant J - isingDiagonalEnergy J s := by
  simp [shiftedTFIMHamiltonian]

theorem shiftedTFIMHamiltonian_single_flip {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ)
    {s t : SpinConfig N} (hst : s ≠ t)
    (hflip : SingleSpinFlip s t) :
    shiftedTFIMHamiltonian J h s t = h := by
  simp [shiftedTFIMHamiltonian, transverseIsingHamiltonian, hst, hflip]

theorem shiftedTFIMHamiltonian_other_off_diagonal {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ)
    {s t : SpinConfig N} (hst : s ≠ t)
    (hflip : ¬ SingleSpinFlip s t) :
    shiftedTFIMHamiltonian J h s t = 0 := by
  simp [shiftedTFIMHamiltonian, transverseIsingHamiltonian, hst, hflip]

theorem shiftedTFIMHamiltonian_entrywise_nonneg {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 ≤ h) :
    ∀ s t, 0 ≤ shiftedTFIMHamiltonian J h s t := by
  classical
  intro s t
  by_cases hst : s = t
  · subst t
    rw [shiftedTFIMHamiltonian_diag]
    have hdiag := isingDiagonalEnergy_lt_shiftConstant J s
    linarith
  · by_cases hflip : SingleSpinFlip s t
    · rw [shiftedTFIMHamiltonian_single_flip J h hst hflip]
      exact hh
    · rw [shiftedTFIMHamiltonian_other_off_diagonal J h hst hflip]

theorem shiftedTFIMHamiltonian_positive_iff_single_flip {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 < h)
    {s t : SpinConfig N} (hst : s ≠ t) :
    0 < shiftedTFIMHamiltonian J h s t ↔ SingleSpinFlip s t := by
  constructor
  · intro hpos
    by_contra hflip
    have hzero :=
      shiftedTFIMHamiltonian_other_off_diagonal J h hst hflip
    rw [hzero] at hpos
    exact (lt_irrefl 0) hpos
  · intro hflip
    rw [shiftedTFIMHamiltonian_single_flip J h hst hflip]
    exact hh



theorem flipAt_ne_self {N : ℕ} (s : SpinConfig N) (i : Fin N) :
    flipAt s i ≠ s := by
  intro h
  have hi := congrFun h i
  cases hs : s i <;> simp [flipAt, hs] at hi

theorem singleSpinFlip_ne {N : ℕ} {s t : SpinConfig N}
    (h : SingleSpinFlip s t) : s ≠ t := by
  rcases h with ⟨i, rfl⟩
  exact Ne.symm (flipAt_ne_self s i)

/-- The Boolean hypercube is connected under single-coordinate flips.
The proof constructs a path by successively correcting every coordinate
on which the two configurations differ. -/
theorem singleSpinFlip_pf_connected {N : ℕ} :
    ∀ s t : SpinConfig N, PFReachable SingleSpinFlip s t := by
  classical
  have hmain :
      ∀ n, ∀ s t : SpinConfig N,
        (Finset.univ.filter (fun i : Fin N => s i ≠ t i)).card = n →
          PFReachable SingleSpinFlip s t := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro s t hcard
      let D : Finset (Fin N) :=
        Finset.univ.filter (fun i : Fin N => s i ≠ t i)
      by_cases hD : D = ∅
      · have hst : s = t := by
          funext i
          by_contra hne
          have hi : i ∈ D := by simp [D, hne]
          simpa [hD] using hi
        subst t
        exact PFReachable.refl s
      · have hDnonempty : D.Nonempty :=
          Finset.nonempty_iff_ne_empty.mpr hD
        let i : Fin N := Classical.choose hDnonempty
        have hiD : i ∈ D := Classical.choose_spec hDnonempty
        have hdiff : s i ≠ t i := by
          simpa [D] using hiD
        let u : SpinConfig N := flipAt s i
        have hsu : SingleSpinFlip s u := ⟨i, rfl⟩
        have hui : u i = t i := by
          dsimp [u, flipAt]
          cases hs : s i <;> cases ht : t i <;> simp_all
        have hD' :
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)) =
              D.erase i := by
          ext j
          by_cases hji : j = i
          · subst j
            simp [D, hui, hiD]
          · simp [D, u, flipAt, hji]
        have hDpos : 0 < D.card := Finset.card_pos.mpr ⟨i, hiD⟩
        have hcard' :
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)).card < n := by
          calc
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)).card
                = D.card - 1 := by rw [hD', Finset.card_erase_of_mem hiD]
            _ < D.card := Nat.sub_lt hDpos (by decide)
            _ = n := hcard
        exact PFReachable.step hsu (ih _ hcard' u t rfl)
  intro s t
  exact hmain _ s t rfl

/-- The positive-support graph of the shifted TFIM matrix is precisely the
single-spin-flip hypercube away from the diagonal, and is therefore connected
for every strictly positive transverse field. -/
theorem shiftedTFIMHamiltonian_pf_connected {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 < h) :
    ∀ s t : SpinConfig N,
      PFReachable
        (fun a b => 0 < shiftedTFIMHamiltonian J h a b) s t := by
  intro s t
  have hreach := singleSpinFlip_pf_connected s t
  induction hreach with
  | refl a =>
      exact PFReachable.refl a
  | @step a b c hab hbc ih =>
      rcases hab with ⟨i, rfl⟩
      have hne : a ≠ flipAt a i := Ne.symm (flipAt_ne_self a i)
      have hpos :
          0 < shiftedTFIMHamiltonian J h a (flipAt a i) :=
        (shiftedTFIMHamiltonian_positive_iff_single_flip J h hh hne).2
          ⟨i, rfl⟩
      exact PFReachable.step hpos ih



/-- The shifted computational-basis TFIM matrix remains real symmetric:
the scalar diagonal shift is symmetric and the single-spin-flip adjacency
relation is symmetric. -/
theorem shiftedTFIMHamiltonian_isHermitian {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) :
    (shiftedTFIMHamiltonian J h).IsHermitian := by
  apply Matrix.IsHermitian.ext
  intro s t
  by_cases hst : s = t
  · subst t
    simp [shiftedTFIMHamiltonian]
  · have hts : t ≠ s := Ne.symm hst
    have hflip : SingleSpinFlip s t ↔ SingleSpinFlip t s := by
      constructor
      · exact singleSpinFlip_symm
      · exact singleSpinFlip_symm
    simp [shiftedTFIMHamiltonian, transverseIsingHamiltonian, hst, hts]
    rw [hflip]

/-- Conditional model-level Perron conclusion for the actual shifted TFIM
matrix. The only analytic Perron input still assumed here is a strictly
positive eigenvector and its positive eigenvalue; the Hamiltonian encoding,
nonnegativity, Hermitian property, and connected positive support are
discharged from the model definitions. -/
theorem shiftedTFIMHamiltonian_perron_characteristic_root_multiplicity_one
    {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 < h)
    (v : SpinConfig N → ℝ) (lambdaVal : ℝ)
    (hv : ∀ s, 0 < v s)
    (hlambdaVal : 0 < lambdaVal)
    (hKv : ∀ s,
      ∑ t, shiftedTFIMHamiltonian J h s t * v t = lambdaVal * v s) :
    Polynomial.rootMultiplicity (RCLike.ofReal lambdaVal)
      (shiftedTFIMHamiltonian J h).charpoly = 1 := by
  exact perron_eigenvalue_has_characteristic_root_multiplicity_one
    (shiftedTFIMHamiltonian J h)
    (shiftedTFIMHamiltonian_isHermitian J h)
    v lambdaVal
    (shiftedTFIMHamiltonian_entrywise_nonneg J h hh.le)
    hv hlambdaVal hKv
    (shiftedTFIMHamiltonian_pf_connected J h hh)


/-- The shifted TFIM matrix acts as cI - H on every vector. This is the
explicit algebraic identity needed to transfer eigenvectors between the
shifted nonnegative matrix and the physical Hamiltonian. -/
theorem shiftedTFIMHamiltonian_mulVec_identity {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (v : SpinConfig N → ℝ)
    (s : SpinConfig N) :
    (∑ t, shiftedTFIMHamiltonian J h s t * v t) =
      isingShiftConstant J * v s -
        ∑ t, transverseIsingHamiltonian J h s t * v t := by
  classical
  have hdiag :
      (∑ t : SpinConfig N, (if s = t then isingShiftConstant J else 0) * v t)
        = isingShiftConstant J * v s := by
    rw [Finset.sum_eq_single s]
    · simp
    · intro t ht hts
      simp [hts.symm]
    · intro hs
      exact (hs (Finset.mem_univ s)).elim
  calc
    (∑ t, shiftedTFIMHamiltonian J h s t * v t)
        = ∑ t, ((if s = t then isingShiftConstant J else 0) * v t -
            transverseIsingHamiltonian J h s t * v t) := by
              apply Finset.sum_congr rfl
              intro t ht
              simp [shiftedTFIMHamiltonian]
              ring_nf
    _ = (∑ t, (if s = t then isingShiftConstant J else 0) * v t) -
          ∑ t, transverseIsingHamiltonian J h s t * v t :=
            sum_sub_distrib
    _ = isingShiftConstant J * v s -
          ∑ t, transverseIsingHamiltonian J h s t * v t := by rw [hdiag]

/-- Exact eigenvector correspondence under the scalar spectral shift
K = cI - H. No positivity or Perron assumption is used in this algebraic
equivalence. -/
theorem shiftedTFIMHamiltonian_eigenvector_iff {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ)
    (v : SpinConfig N → ℝ) (lambdaVal : ℝ) :
    (∀ s, ∑ t, shiftedTFIMHamiltonian J h s t * v t =
        lambdaVal * v s) ↔
      (∀ s, ∑ t, transverseIsingHamiltonian J h s t * v t =
        (isingShiftConstant J - lambdaVal) * v s) := by
  constructor
  · intro hK s
    have hid := shiftedTFIMHamiltonian_mulVec_identity J h v s
    rw [hK s] at hid
    linarith
  · intro hH s
    have hid := shiftedTFIMHamiltonian_mulVec_identity J h v s
    rw [hH s] at hid
    linarith



/-- A data-carrying finite path in a relation on the finite spin configurations.
Unlike PFReachable, this lives in Type, so it can be converted into Mathlib's path data. -/
inductive PFPath {N : ℕ} (R : SpinConfig N → SpinConfig N → Prop) :
    SpinConfig N → SpinConfig N → Type
  | refl (i : SpinConfig N) : PFPath R i i
  | step {i j k : SpinConfig N} : R i j → PFPath R j k → PFPath R i k

/-- Forget explicit path data when only a reachability proposition is needed. -/
theorem PFPath.toReachable {N : ℕ}
    {R : SpinConfig N → SpinConfig N → Prop} {i j : SpinConfig N}
    (p : PFPath R i j) : PFReachable R i j := by
  induction p with
  | refl a => exact PFReachable.refl a
  | @step a b c hab hbc ih => exact PFReachable.step hab ih

/-- Turn a data-carrying relation path into a quiver path. -/
noncomputable def PFPath.toQuiverPath {N : ℕ}
    {R : SpinConfig N → SpinConfig N → Prop} {s t : SpinConfig N}
    [Quiver (SpinConfig N)]
    (edge : ∀ (a b : SpinConfig N), R a b → Quiver.Hom a b)
    (p : PFPath R s t) :
    Quiver.Path s t := by
  induction p with
  | refl a => exact Quiver.Path.nil
  | @step a b c hab hbc ih =>
      exact (Quiver.Path.nil.cons (edge a b hab)).comp ih

/-- The Boolean hypercube is connected under single-coordinate flips, with
an explicit path object that can be consumed by independent graph APIs. -/
noncomputable def singleSpinFlip_pf_path {N : ℕ} :
    ∀ s t : SpinConfig N, PFPath SingleSpinFlip s t := by
  classical
  have hmain :
      ∀ n, ∀ s t : SpinConfig N,
        (Finset.univ.filter (fun i : Fin N => s i ≠ t i)).card = n →
          PFPath SingleSpinFlip s t := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro s t hcard
      let D : Finset (Fin N) :=
        Finset.univ.filter (fun i : Fin N => s i ≠ t i)
      by_cases hD : D = ∅
      · have hst : s = t := by
          funext i
          by_contra hne
          have hi : i ∈ D := by simp [D, hne]
          simpa [hD] using hi
        subst t
        exact PFPath.refl s
      · have hDnonempty : D.Nonempty :=
          Finset.nonempty_iff_ne_empty.mpr hD
        let i : Fin N := Classical.choose hDnonempty
        have hiD : i ∈ D := Classical.choose_spec hDnonempty
        have hdiff : s i ≠ t i := by
          simpa [D] using hiD
        let u : SpinConfig N := flipAt s i
        have hsu : SingleSpinFlip s u := ⟨i, rfl⟩
        have hui : u i = t i := by
          dsimp [u, flipAt]
          cases hs : s i <;> cases ht : t i <;> simp_all
        have hD' :
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)) =
              D.erase i := by
          ext j
          by_cases hji : j = i
          · subst j
            simp [D, hui, hiD]
          · simp [D, u, flipAt, hji]
        have hDpos : 0 < D.card := Finset.card_pos.mpr ⟨i, hiD⟩
        have hcard' :
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)).card < n := by
          calc
            (Finset.univ.filter (fun j : Fin N => u j ≠ t j)).card
                = D.card - 1 := by rw [hD', Finset.card_erase_of_mem hiD]
            _ < D.card := Nat.sub_lt hDpos (by decide)
            _ = n := hcard
        exact PFPath.step hsu (ih _ hcard' u t rfl)
  intro s t
  exact hmain _ s t rfl

/-- Transfer the explicit Boolean-hypercube path to positive support of
the shifted TFIM matrix when the transverse field is strictly positive. -/
noncomputable def shiftedTFIMHamiltonian_pf_path {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 < h) :
    ∀ s t : SpinConfig N,
      PFPath
        (fun a b => 0 < shiftedTFIMHamiltonian J h a b) s t := by
  classical
  intro s t
  have hpath := singleSpinFlip_pf_path s t
  induction hpath with
  | refl a => exact PFPath.refl a
  | @step a b c hab hbc ih =>
      let i : Fin N := Classical.choose hab
      have hflip : b = flipAt a i := Classical.choose_spec hab
      have hne : a ≠ b := by
        rw [hflip]
        exact Ne.symm (flipAt_ne_self a i)
      have hpos : 0 < shiftedTFIMHamiltonian J h a b := by
        rw [hflip]
        exact (shiftedTFIMHamiltonian_positive_iff_single_flip J h hh
          (Ne.symm (flipAt_ne_self a i))).2 ⟨i, rfl⟩
      exact PFPath.step hpos ih

/-- The shifted TFIM matrix is irreducible in Mathlib's matrix/quiver sense.
The Boolean-hypercube path supplies connectivity, while the strictly
positive diagonal shift supplies a positive-length loop at every vertex. -/
theorem shiftedTFIMHamiltonian_isIrreducible {N : ℕ}
    (J : IsingEdge N → ℝ) (h : ℝ) (hh : 0 < h) :
    Matrix.IsIrreducible (shiftedTFIMHamiltonian J h) := by
  refine ⟨shiftedTFIMHamiltonian_entrywise_nonneg J h hh.le, ?_⟩
  letI : Quiver (SpinConfig N) :=
    Matrix.toQuiver (shiftedTFIMHamiltonian J h)
  intro s t
  have hreach := shiftedTFIMHamiltonian_pf_path J h hh s t
  have hedge : ∀ (a b : SpinConfig N),
      (0 < shiftedTFIMHamiltonian J h a b) → Quiver.Hom a b :=
    fun a b hp => ⟨hp⟩
  have p : Quiver.Path s t := PFPath.toQuiverPath hedge hreach
  have hdiag : 0 < shiftedTFIMHamiltonian J h s s := by
    rw [shiftedTFIMHamiltonian_diag]
    have hs := isingDiagonalEnergy_lt_shiftConstant J s
    linarith
  let loop : Quiver.Path s s := Quiver.Path.nil.cons ⟨hdiag⟩
  refine ⟨loop.comp p, ?_⟩
  simp [loop]

end ConstantLlapoy.PaperA
