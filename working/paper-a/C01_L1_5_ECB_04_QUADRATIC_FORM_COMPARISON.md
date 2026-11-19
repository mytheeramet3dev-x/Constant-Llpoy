# C01-L1.5 — ECB-04 Quadratic-Form Comparison

**Status:** PROPOSED / MATHEMATICAL ARGUMENT; NOT LEAN-COMPILED  
**Scope:** Prove the absolute-coordinate vector y=|x| has quadratic form at least that of x, for a real symmetric matrix K with nonnegative off-diagonal entries.

## 1. Statement

Let K=(K_ij) be a real symmetric matrix indexed by a finite set Ω, and assume K_ij≥0 whenever i≠j. For any real vector x define y_i=|x_i|. Then

\[
\langle Ky,y\rangle\ge \langle Kx,x\rangle.
\]

## 2. Diagonal contribution

The diagonal terms agree exactly:

\[
\sum_i K_{ii}y_i^2=\sum_i K_{ii}x_i^2,
\]
using y_i²=|x_i|²=x_i². No sign condition on K_ii is needed.

## 3. Off-diagonal contribution

For every i≠j, real absolute values satisfy |x_i||x_j|≥x_ix_j. Since K_ij≥0,
\[
K_{ij}|x_i||x_j|\ge K_{ij}x_ix_j.
\]
Summing over the finite set of ordered off-diagonal pairs preserves the inequality. Combining with the diagonal equality proves the statement.

## 4. Symmetry and expansion conventions

The identity can be written as a sum over all ordered pairs (i,j), with the diagonal separated. Symmetry is part of the intended operator assumptions and is needed for the Rayleigh/eigenvalue argument later; this elementary coordinate inequality itself only needs the off-diagonal sign condition for the displayed expansion.

## 5. Lean proof obligations

- ECB-04a: establish the coordinate expansion of the Euclidean inner product as the finite double sum for the concrete matrix action.
- ECB-04b: diagonal equality via |x_i|²=x_i².
- ECB-04c: pointwise off-diagonal inequality from K_ij≥0 and |x_i||x_j|≥x_ix_j.
- ECB-04d: finite-sum aggregation, preserving the separation of diagonal and off-diagonal terms.
- ECB-04e: conclude the quadratic-form comparison using the verified coordinate bridge.

Do not import an unverified quadratic-form comparison theorem or assume the desired inequality as a hypothesis.

## 6. Scope limitation

This result alone does not establish that y maximizes the Rayleigh quotient, nor that y is an eigenvector. Those require norm preservation, comparison, a maximizing argument, and the relevant finite-dimensional spectral/Rayleigh theorem.

## Disposition

The mathematical proof is elementary and sound under the stated real finite-dimensional assumptions. The precise coordinate types, Mathlib theorem names, and Lean compilation remain pending. Status: **NOT FORMALLY VERIFIED**.
