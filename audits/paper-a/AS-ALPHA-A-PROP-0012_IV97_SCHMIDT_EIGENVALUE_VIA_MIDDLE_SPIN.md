# IV-97 — Schmidt Small Eigenvalue via the Middle-Spin Reduced State

**Status:** ANALYTIC-PARTIAL / STRUCTURAL DERIVATION; explicit uniform constants and formal proof artifact remain pending.

## Hamiltonian and Schmidt reduction
For the pure three-spin ground state of the path Hamiltonian, bipartition endpoints (1,3) against middle spin 2. The nonzero eigenvalues of rho_13 and rho_2 agree. Since rho_2 is 2x2, write its eigenvalues as q and 1-q. Exactly,
q(1-q)=det(rho_2), and q is the smaller eigenvalue near the decoupled point.

This gives an exact way to compute/control q from the middle-spin state rather than a 4x4 endpoint matrix.

## Symmetry and analytic structure
Near J12=J23=0, the ground state is unique and analytic. The small eigenvalue q is analytic. The simultaneous transformation X1 (or X3) flips the sign of the adjacent edge coupling while preserving the spectrum of rho_2; hence q is even separately in J12 and J23. When both couplings vanish, q=0. Analyticity then implies locally
q = J12^2 a(J12^2,J23^2)+J23^2 b(J12^2,J23^2)
for analytic a,b (one may choose a decomposition non-uniquely).

First-order ground-state perturbation: edge term Z_i Z_j creates the two-X-basis-spin excitation with amplitude J_ij/(4h). For the middle spin, these two orthogonal edge-excitation states each contribute flip probability J_ij^2/(16h^2). Thus the quadratic Taylor term is
q = (J12^2+J23^2)/(16h^2) + O((J12^2+J23^2)^2/h^4)
= x+y+O((x+y)^2).

Because the analytic remainder is a function of squared couplings with no degree-zero or degree-one (in squared variables) contribution, it is bounded by C t^2 on a sufficiently small compact neighborhood, with C independent of the coupling ratio. This is an existence of local uniform constant, not an explicit numeric constant.

## Consequence
This is the needed joint small-eigenvalue estimate q=t+O(t^2), provided the analytic/symmetry arguments and coefficient computation are fully formalized. Combined with IV-95 marginal factorization, it supplies the ratio-aware eigenvalue pattern required by IV-94. The conditional entropy remainder then follows as O(t^2 ln(1/t)) in natural units, subject to IV-95/IV-97 assumptions.

## Caveats / corrections
- This argument uses the middle-spin reduced density matrix and Schmidt equivalence, not a direct 4x4 eigenvalue perturbation.
- q is not asserted to be exactly x+y; only the quadratic coefficient and local analytic remainder are claimed.
- The exact rank-two fact is independent of weak coupling.
- No Lean verification, explicit constants, or global-in-coupling result is claimed.

## Status
A promising analytic route to the q estimate is recorded. Proposition 0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED until all hypotheses are formalized and the target response difference B-C is derived/controlled.
