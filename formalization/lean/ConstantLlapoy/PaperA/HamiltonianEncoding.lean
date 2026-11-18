import Mathlib

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

e

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
      exact le_rfl

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

end ConstantLlapoy.PaperA
