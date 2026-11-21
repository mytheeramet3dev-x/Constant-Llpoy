# PROP-0012 — Pair-Flip Perturbation-Order Lemma Audit

**Scope:** Fixed finite N, transverse-field TFIM at the uncoupled reference, real independent edge perturbations in a compact neighborhood, first edge derivatives. This is a mathematical analytic audit; no Lean formalization/build was performed.

## Claim

For the analytic ground-state vector in the x-basis, the amplitude c_E of any even flip set E satisfies
\[
c_E(r,\mathbf u)=O_N(r^{|E|/2}),\qquad
\partial_{u_e}c_E(r,\mathbf u)=O_N(r^{|E|/2})
\]
uniformly for u in a sufficiently small compact neighborhood. In particular, c_empty=1+O_N(r^2), and c_12=O_N(r).

## Proof audit

At r=0, H_0=-h sum_i X_i has a unique ground state |empty>, separated by a positive gap. The normalized ground-state vector can be chosen jointly analytic in r and u near this point. Expand it as a convergent Taylor series in r, psi(r,u)=sum_{n>=0}r^n psi_n(u), and expand the eigenvalue similarly.

Each interaction insertion is an edge operator Z_i Z_j, which flips exactly two x-basis bits. The coefficient recursion obtained by inserting the series in (H_0+rV(u))psi=Epsi and solving excited-state components with the reduced inverse of H_0-E_0 has the following support property by induction: at order n, a basis vector with flip set E can occur only if E is reachable from the empty set by at most n pair flips. Scalar energy corrections and normalization terms multiply previously occurring components and do not create new flip support, so they preserve this bound. Any sequence of n pair flips changes at most 2n bit positions. Therefore the amplitude indexed by E vanishes in Taylor orders n<|E|/2. For even E, this yields the stated order r^{|E|/2}.

The empty-set component has no first-order correction: one pair-flip interaction sends the reference vector to a two-flip vector, orthogonal to it. Thus c_empty=1+O_N(r^2), after the analytic phase/normalization convention.

Differentiating the jointly analytic Taylor coefficients in u_e cannot introduce lower powers of r: u appears in the coefficients of V, not in the prefactor r. On compact u-neighborhoods, coefficient and derivative bounds are finite for fixed N. Hence the same vanishing Taylor orders hold for first edge derivatives. Constants depend on N and the chosen compact neighborhood; no uniform-in-N claim is made.

## Scope and caveats

- Pair-flip support proves a minimum number of interaction insertions; it does not claim each coefficient is nonzero.
- The proof uses finite-dimensional analytic perturbation and the stated pair-flip structure. The recursion/support induction is reviewed at paper level but not mechanically checked.
- The lemma is fixed-N and local in coupling/edge variables.
- No source-wide PROP-0012 reconciliation, global B-C sign theorem, or Lean formalization/build is included.

**Verdict:** PAIR-FLIP AMPLITUDE ORDER — ANALYTIC ARGUMENT CLOSED AT PAPER LEVEL, NOT FORMALLY VERIFIED. This closes the specific order-lemma gap identified by the even-block Schur review, subject to checking the exact Hamiltonian/source conventions during integration.
