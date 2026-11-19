# C01-L1.6 — ECB-05 Transfer of a Rayleigh Maximizer

**Status:** PROPOSED / MATHEMATICAL ARGUMENT; NOT LEAN-COMPILED  
**Scope:** Combine norm preservation and quadratic-form comparison to obtain a nonnegative Rayleigh maximizer.

## 1. Rayleigh quotient
For a nonzero real vector z define R_K(z)=⟨Kz,z⟩/‖z‖². Let y=|x| coordinatewise. From ECB-02, ‖y‖=‖x‖, so y is nonzero whenever x is nonzero and the denominators agree. ECB-04 gives ⟨Ky,y⟩≥⟨Kx,x⟩. Consequently R_K(y)≥R_K(x).

## 2. Maximizer transfer
Assume x is a maximizing vector on the unit sphere, so ‖x‖=1 and R_K(x)=M, where M is the supremum (or attained maximum) of R_K on the unit sphere. Norm preservation gives ‖y‖=1, so y remains on the same sphere. The comparison gives R_K(y)≥M. By maximality, R_K(y)≤M. Hence R_K(y)=M, and y is also a maximizer with every coordinate nonnegative.

## 3. Existence assumptions
In a finite-dimensional real inner-product space, the unit sphere is compact and the Rayleigh quotient is continuous; therefore the maximum is attained. The Lean proof must establish or invoke verified compactness/continuity facts for the concrete finite-dimensional type and the symmetric operator. Do not silently replace a maximum by a supremum without proving attainment.

## 4. Dependencies
- ECB-02: norm preservation and nonzero preservation.
- ECB-04: quadratic-form comparison.
- Finite-dimensional compactness/continuity: existence of a Rayleigh maximizer.
- Maximality: upper bound for R_K(y).

## 5. Scope
ECB-05 establishes a nonnegative maximizing vector, not yet the eigenvector equation. The eigenvector conclusion requires a separate spectral or variational theorem, and the coordinate equation must then be connected to the operator K used in the manuscript.

**Disposition:** Mathematically justified under the stated finite-dimensional real inner-product assumptions. Exact Lean implementation and compilation remain pending; status **NOT FORMALLY VERIFIED**.
