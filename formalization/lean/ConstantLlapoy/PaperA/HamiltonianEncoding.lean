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

end ConstantLlapoy.PaperA
