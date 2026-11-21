# PROP-0012 — Independent Review of Rank-Changing Entropy Derivative Lemma

**Scope:** Review the reusable lemma in `audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md` and its stated weak-coupling use. Fixed finite dimension, first directional derivative only.

## Lemma review

Let λ(r,u) be jointly real-analytic near (0,0), nonnegative for 0<r<r0 and real u in an open interval, and uniformly O(r^m) on a smaller u-compact neighborhood. At fixed r>0:

- If λ(r,0)=0 for all sufficiently small r, nonnegativity and interiority imply λ_u(r,0)=0. Since λ(r,u)=O_r(u^2), the entropy function -λ ln λ has derivative 0 at u=0.
- Otherwise, analyticity of r↦λ(r,0) gives a finite first nonzero Taylor order k≥m, with positive leading coefficient (nonnegativity for positive r). Thus |ln λ(r,0)|=O(1+|ln r|).
- Uniform joint O(r^m) plus analyticity on an open parameter neighborhood implies λ_u(r,0)=O(r^m), e.g. by Taylor/coefficient bounds or Cauchy estimates in u.
- At positive λ, the exact chain rule is ∂u(-λ ln λ)=-(1+lnλ)λ_u, yielding O(r^m(1+|ln r|).

## Verdict

**LEMMA: ANALYTIC PASS, ASSUMPTIONS MATERIAL.** The argument is correct for the stated local, fixed-dimensional, first-directional-derivative setting. It does not prove twice differentiability, and its nonnegativity assumption must hold on a two-sided open edge-parameter neighborhood at each positive r. It is not enough to know only λ=O(r^m); the uniform joint analytic derivative control is required.

## Application status for PROP-0012

The lemma's logic itself closes the entropy contribution once the relevant small eigenvalue is established as a jointly analytic nonnegative branch with a uniform O_N(r^3) bound. This review does not independently establish that branch property for every weak-coupling block of the reduced density matrix. The outstanding obligation is therefore the block-level spectral expansion/analytic factorization and its edge-direction bounds, not the lemma's entropy-chain-rule step.

No Lean formalization/build was performed.
