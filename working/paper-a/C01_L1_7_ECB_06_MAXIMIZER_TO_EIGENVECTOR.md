# C01-L1.7 — ECB-06 Maximizer-to-Eigenvector via Orthogonal Perturbation

**Status:** PROPOSED / MATHEMATICAL AUDIT; NOT LEAN-COMPILED  
**Scope:** Prove a unit Rayleigh maximizer of a symmetric operator is an eigenvector, using a two-sided perturbation argument.

## 1. Hypotheses

Let V be a real finite-dimensional inner-product space, K:V→V self-adjoint, and y a unit vector maximizing q(u)=⟨Ku,u⟩ over unit vectors u. Fix arbitrary z with ⟨y,z⟩=0.

## 2. Rayleigh quotient for the orthogonal perturbation

Because y is unit and z⊥y, ‖y+tz‖²=1+t²‖z‖². By self-adjointness,

q(y+tz)=⟨Ky,y⟩+2t⟨Ky,z⟩+t²⟨Kz,z⟩.

Let a=⟨Ky,y⟩, b=⟨Ky,z⟩, c=⟨Kz,z⟩. The maximality of y gives for all real t:

(a+2bt+ct²)/(1+t²‖z‖²) ≤ a.

Since the denominator is positive, rearrangement yields

2bt+(c-a‖z‖²)t²≤0.

## 3. Two-sided sign argument

The inequality holds for every real t. If b≠0, choose t with the sign of b. Then 2bt>0 and is first order in |t|, while the remaining term is bounded in magnitude by a constant times t². For sufficiently small nonzero |t|, the expression becomes positive, a contradiction. Thus b=0.

Therefore ⟨Ky,z⟩=0 for every z orthogonal to y. The orthogonal complement of y has codimension one, so Ky lies in span{y}; hence Ky=λy for some real λ. Taking inner product with y and using ‖y‖=1 gives λ=⟨Ky,y⟩.

## 4. Alternative derivative route

The normalized path u(t)=(y+tz)/‖y+tz‖ is differentiable at zero. The derivative of the Rayleigh quotient at a constrained maximum vanishes in tangent direction z. Under self-adjointness this derivative is 2⟨Ky,z⟩. This is concise, but the algebraic two-sided argument above may be preferable in Lean if differentiability infrastructure is costly.

## 5. Lean proof obligations

- ECB-06a: prove ‖y+tz‖²=1+t²‖z‖² from unit y and orthogonality.
- ECB-06b: expand ⟨K(y+tz),y+tz⟩ using linearity and self-adjointness to identify the cross terms as 2t⟨Ky,z⟩.
- ECB-06c: clear the positive denominator and derive the quadratic inequality for every t.
- ECB-06d: prove b=0 from the two-sided inequality (an explicit small-t argument or a verified derivative theorem).
- ECB-06e: use orthogonal decomposition to show Ky is a scalar multiple of y.
- ECB-06f: identify the scalar as ⟨Ky,y⟩ using ‖y‖=1.

## 6. Scope and caveats

Self-adjointness is essential to the symmetric cross-term expansion. Finite-dimensionality is used for the maximizer existence step upstream and can support the orthogonal decomposition; the local perturbation argument itself does not need compactness once a maximizer is given. This establishes the eigenvector property of a maximizing vector, not positivity of all coordinates, uniqueness, strict positivity, or simplicity. Those require separate steps.

**Disposition:** Mathematical argument is sound under the stated assumptions. Exact Lean declaration mapping and compilation remain pending. **NOT FORMALLY VERIFIED.**
