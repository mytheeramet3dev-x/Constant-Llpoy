# C01-L1.4 — ECB-01–03 Absolute-Coordinate Construction

**Status:** PROPOSED / SOURCE-LEVEL MATHEMATICAL AUDIT; NOT LEAN-COMPILED  
**Scope:** Construct the coordinatewise absolute-value vector, prove coordinate nonnegativity, norm preservation, and nonzero preservation.

## 1. Definitions

For a real coordinate vector x : Ω_N → ℝ, define y(ω)=|x(ω)|. This is the coordinatewise absolute-value construction; do not confuse it with the scalar absolute value of a vector norm.

## 2. ECB-01: coordinate nonnegativity

For every configuration ω, y(ω)=|x(ω)|≥0. This follows from real absolute-value nonnegativity. In Lean, the construction must be typed as the same coordinate-indexed vector space as x, and the proof should be pointwise.

**Proof status:** Mathematical argument established; exact Lean declaration names and elaboration not checked.


## 3. ECB-02: norm preservation

For a finite real coordinate space with its Euclidean norm,
||y||² = Σ_{ω∈Ω_N}|y(ω)|² = Σ_{ω∈Ω_N}|x(ω)|² = ||x||²,
because y(ω)=|x(ω)| and absolute value leaves the square unchanged.

Both norms are nonnegative. Equality of their squares therefore implies equality of norms: ||y||=||x||.

A Lean proof should avoid assuming norm equality directly. Establish either the coordinatewise squared identity and sum it over the finite index set, or use a verified norm/squared-norm identity already available for the concrete Euclidean-space type. Then derive norm equality from nonnegativity and square equality.

**Proof status:** Mathematical argument established; concrete Mathlib proof route and exact theorem names remain unverified.

## 4. ECB-03: nonzero preservation

If x ≠ 0, then ||x||>0. Norm preservation gives ||y||=||x||>0, hence y ≠ 0.

This step is downstream of ECB-02. It must not be proved by an independent assertion about coordinates unless that assertion is separately established.

**Proof status:** Mathematical consequence of ECB-02; Lean compilation pending.

## 5. Index edge case N=0

For a configuration type Fin 0 → Bool (or an equivalent spin assignment), there is exactly one empty configuration, not zero configurations. Thus the configuration-indexed vector space has one coordinate and is nontrivial. The N=0 case is not automatically a zero-vector-space obstruction.

The concrete type used in the repository must be inspected before encoding this observation. Do not add N≥1 merely to avoid a nonexistent zero-dimensional issue.

## 6. Minimal dependency chain

- ECB-01 supplies y(ω)≥0.
- ECB-02 supplies ||y||=||x||.
- ECB-03 uses ECB-02 and x≠0 to supply y≠0.

These obligations are independent of the later matrix positivity, Rayleigh comparison, maximizer transfer, and eigenvector extraction. They do not yet prove the Perron–Frobenius conclusion.

## 7. Remaining risks

1. Concrete coordinate type may be EuclideanSpace over a different index than the paper's configuration set; verify definition rather than assume.
2. The norm-square expansion must match Mathlib's inner-product and norm conventions.
3. Equality of squared norms must be converted to equality of norms with the nonnegativity hypotheses explicit.
4. No Lean/Lake compiler is available in the current execution environment; this note is not a compilation report.

## Disposition

ECB-01–03 are mathematically straightforward and have a clear dependency structure. Their status remains NOT FORMALLY VERIFIED until concrete Lean declarations are written, compiled against the pinned Mathlib revision, and included in the axiom audit.
