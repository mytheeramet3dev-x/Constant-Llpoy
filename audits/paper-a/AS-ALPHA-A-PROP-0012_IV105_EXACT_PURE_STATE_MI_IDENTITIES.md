# IV-105 — Exact Pure-State Entropy and Mutual-Information Identities

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Exact structural identities; response-identity mapping still open  
**Date:** 2026-11-22

## 1. Scope

This audit derives entropy identities for any pure three-qubit state, with the additional parity facts established for the ground-state branch in IV-101. It does not infer the target response identity, whose `chi_i` definitions and differentiation variables must be separately matched.

Let `S_i=S(ρ_i)`, `S_{ij}=S(ρ_{ij})`, and `I_{ij}=S_i+S_j-S_{ij}`.

## 2. Pure-state complement identities

For any pure `ρ_{123}`,
\[
S_{12}=S_3,\qquad S_{13}=S_2,\qquad S_{23}=S_1.
\]
Hence
\[
\boxed{I_{12}=S_1+S_2-S_3,}
\]
\[
\boxed{I_{13}=S_1+S_3-S_2.}
\]
Subtracting gives the exact identity
\[
\boxed{I_{12}-I_{13}=2(S_2-S_3).}
\]
This is not a perturbative expansion and requires no assumptions about coupling size.

## 3. Middle-spin entropy

IV-101 establishes that on the parity-eigenstate ground branch the middle reduced state is diagonal in the X basis. Write its eigenvalues as `1-q,q`. Thus
\[
S_2=h(q)=-q\ln q-(1-q)\ln(1-q).
\]
Also, because the full state is pure, the endpoint-pair entropy is exactly
\[
S_{13}=S_2=h(q).
\]
The equality is exact, so any occurrence of `S_{13}` and `S_2` in an expression can be replaced without an approximation.

## 4. What does not cancel in I12 versus I13

The identities above show
\[
I_{12}=S_1+h(q)-S_3,
\]
\[
I_{13}=S_1+S_3-h(q).
\]
The entropy `h(q)` enters with opposite signs. Therefore
\[
I_{12}-I_{13}=2h(q)-2S_3,
\]
not a cancellation of `h(q)` between these two mutual informations. The middle-spin entropy contribution doubles in the difference.

For derivatives with respect to any parameter `λ` on a smooth nondegenerate ground-state branch:
\[
\boxed{\partial_λ(I_{12}-I_{13})=2\partial_λ S_2-2\partial_λ S_3.}
\]
This derivative relation is exact locally wherever the entropies are differentiable; at zero-coupling points where the small eigenvalue vanishes, entropy derivatives may be singular or require one-sided/asymptotic treatment.

## 5. Three-qubit endpoint mutual information is not generally binary entropy of q

Schmidt rank across the cut `2 | 13` is at most two, so `ρ_{13}` has two potentially nonzero eigenvalues. Those eigenvalues are `q` and `1-q` because they equal the spectrum of `ρ_2`. This gives `S_{13}=h(q)`.

But `I_{13}=S_1+S_3-S_2` depends also on endpoint marginal entropies `S_1,S_3`. It cannot be reduced to `h(q)` alone without additional constraints.

## 6. Open obligations for Paper A

- Identify the precise `χ_1,χ_2` definitions and parameter derivatives in the manuscript, then map this exact structural relation to the target formula.
- Derive the endpoint marginal spectra/entropies or their derivatives, rather than assume endpoint symmetry. The chain Hamiltonian is generally not symmetric under swapping endpoints unless couplings and relevant conditions are also swapped.
- No target identity is proven in this audit; no cancellation is asserted without algebraic support.

## 7. Next audit

IV-106: derive the endpoint one-spin reduced density matrix in the X basis from the even-parity eigenvector components and compute its Bloch vector exactly in terms of those amplitudes. This supplies the missing endpoint entropy data without prematurely expanding.
