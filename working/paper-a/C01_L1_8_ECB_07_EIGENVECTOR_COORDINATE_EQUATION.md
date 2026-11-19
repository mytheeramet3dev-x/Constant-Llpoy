# C01-L1.8 — ECB-07 Eigenvector Coordinate Equation

**Status:** PROPOSED / MATHEMATICAL AUDIT; NOT LEAN-COMPILED  
**Scope:** Translate the abstract eigenvector equation into the concrete finite-coordinate matrix equation used in Paper A.

## 1. Abstract result from ECB-06

For the self-adjoint operator K and unit Rayleigh maximizer y, ECB-06 establishes Ky=λy, with λ=⟨Ky,y⟩.

## 2. Coordinate expansion

Let Ω be the finite configuration index set and let K be represented by entries K_{ω,ω'}. Under the standard matrix action,

(Ky)_ω = Σ_{ω'∈Ω} K_{ω,ω'} y_{ω'}.

Thus the eigenvector equation yields, for every ω∈Ω,

Σ_{ω'∈Ω} K_{ω,ω'} y_{ω'} = λ y_ω.

This is a coordinate identity, not a new theorem. It requires the matrix-vector action used by the Lean representation to match the finite sum above.

## 3. Lean proof obligations

- ECB-07a: confirm the concrete index type Ω and matrix entry orientation.
- ECB-07b: expand the matrix-vector multiplication at coordinate ω into the finite sum.
- ECB-07c: apply the abstract equation Ky=λy and evaluate both sides at ω.
- ECB-07d: retain the exact diagonal/off-diagonal distinctions; do not infer all entries of K are nonnegative from an off-diagonal sign condition.

## 4. Paper correspondence check

The resulting equation must match the manuscript's definition of the shifted operator K=cI−H. Confirm the sign of the diagonal shift, the sign of off-diagonal spin-flip entries, and the configuration adjacency relation before using this coordinate formula to assert positivity or uniqueness.

## 5. Scope

ECB-07 only records the eigenvector equation coordinatewise. It does not establish that λ is the largest eigenvalue, that y is strictly positive, or that the eigenspace is one-dimensional. Those require the maximization context and subsequent irreducibility/positivity arguments.

**Disposition:** Coordinate formula is mathematically valid for the stated finite matrix action. Concrete Lean type/index conventions and compilation remain pending. **NOT FORMALLY VERIFIED.**
