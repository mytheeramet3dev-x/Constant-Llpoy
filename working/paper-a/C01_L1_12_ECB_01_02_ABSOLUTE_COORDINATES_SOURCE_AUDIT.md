# AbsoluteCoordinates.lean — Initial Source Audit (ECB-01–02)

**Branch:** `paper-a-mcr01-pf-redline`  
**Reviewed source blob:** `64827aaaf4d82390be6c367f01054339da7743fe`  
**Toolchain:** Lean `v4.36.0`  
**Mathlib pin:** `96f6b8b8e029545577421f198a89fb174a4d62e6`  
**Status:** source-reviewed; NOT compiled; NOT formally verified.

## Scope

Reviewed `formalization/lean/ConstantLlapoy/PaperA/AbsoluteCoordinates.lean` for the existing ECB-01 and ECB-02 declarations only. No upstream manuscript changes.

## Findings

| Declaration | Source review | Compilation |
|---|---|---|
| `absoluteCoordinateVector` | Definition matches coordinatewise real absolute value | Unknown |
| `absoluteCoordinateVector_nonneg` | Proof uses `abs_nonneg`; mathematical argument sound | Unknown |
| `absoluteCoordinateVector_abs` | Definitional equality; `rfl` is appropriate | Unknown |
| `absoluteValue_square_eq_square` | Case split on sign; rewriting and ring normalization are mathematically sound | Unknown |
| `absoluteCoordinateVector_square` | Follows from scalar square lemma | Unknown |
| `absoluteCoordinateVector_sum_sq` | Finite sum congruence follows coordinatewise equality; verify elaboration against pinned Mathlib | Unknown |

## Edge cases and gaps

1. The sum-of-squares theorem is stated for a finite index type (`Fintype ι`), including the empty type. The empty-index case is consistent: both sums are zero.
2. The current file establishes equality of sums of coordinate squares, but it does not yet establish the Euclidean norm identity `‖absoluteCoordinateVector x‖ = ‖x‖`. A norm bridge is required.
3. ECB-03 (nonzero preservation) is not yet encoded as a theorem in this file.
4. No Lean compiler was available in this audit session. No claim of successful compilation, kernel checking, or axiom audit is made.
5. Proof/API compatibility must be checked with the exact Lean and Mathlib pins in the repository before these declarations are considered verified.

## Recommended next actions

1. Obtain a real Lean CI run for this branch and inspect build output.
2. Resolve any compile errors without adding axioms, `sorry`, or weakening theorem statements.
3. Add ECB-03 nonzero preservation and compile it.
4. Prove norm preservation using a verified norm/sum-of-squares bridge.
5. Proceed to ECB-04 only after ECB-01–03 have compiler-backed evidence.

## Honest status

**ECB-01/02: SOURCE REVIEWED — mathematical arguments appear sound — compilation pending.**


## Follow-up: ECB-03 source review (2026-11-19)

**Updated source blob:** `4fd25fc15bad5441cf80d54797374b215cd343c3`

Added declarations:
- `absoluteValue_ne_zero_iff`: scalar absolute-value nonzero equivalence.
- `absoluteCoordinate_ne_zero_iff`: pointwise coordinate equivalence.
- `absoluteCoordinateVector_ne_zero_iff`: vector-level nonzero preservation.

### Review notes
- Scalar and coordinate lemmas use simplification of absolute-value zero/nonzero; mathematically standard.
- Vector-level proof uses function extensionality and the scalar fact. Both directions are logically consistent by source inspection.
- The vector equivalence is stated without a nonempty-index assumption; for an empty index type, both sides are false because the unique function is the zero vector, so the equivalence remains valid.
- **Not compiled:** tactic/API elaboration remains unverified. No kernel verification or axiom audit has occurred.

### Status after ECB-03
**ECB-01–03 source-level proof candidates are present; compilation and formal verification remain pending.** Next: obtain compiler-backed evidence, then add a norm-preservation bridge before moving on.
