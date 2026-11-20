# Paper A PROP-0006 — Positive energy rescaling and mutual-information audit

- Claim ID: AS-ALPHA-A-PROP-0006
- Audit date: 2026-11-21
- Frozen source: Section 2.3 at Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Disposition: ANALYTIC-VERIFIED (operator/spectral/projector and MI identity only); NOT-LEAN-VERIFIED.

## Statement under audit

For the symmetric TFIM, let (x=J/h), with (h>0), and
[
H(J,h)=h,widetilde H(x,1).
]
The manuscript claims the ground-state projector is unchanged by the positive energy rescaling, and thus the two-site mutual information depends only on (x):
[
I_{12}(J,h)=mathcal G_N(J/h).
]

## Independent derivation

1. Fix (x=J/h), so (J=hx). The source Hamiltonian factors exactly as (H(J,h)=hwidetilde H(x,1)), by direct substitution into both interaction and transverse-field terms.
2. For (h>0), multiplication of a self-adjoint operator by (h) preserves eigenvectors/eigenspaces and multiplies every eigenvalue by the same positive scalar. Hence eigenvalue ordering is preserved and the ground spectral subspace (and its projector) is the same for (H) and (widetilde H).
3. If the ground eigenspace is one-dimensional, the corresponding normalized ground vectors differ only by a phase. The projector statement does not require selecting a phase.
4. Identical global ground projectors produce identical reduced density matrices under the same partial-trace maps. The von Neumann entropies and their mutual-information combination therefore agree exactly.
5. Define (mathcal G_N(x)) as the mutual information evaluated on the dimensionless Hamiltonian's ground state. Then (I_{12}(J,h)=mathcal G_N(x)), independent of absolute (h) when (x) is fixed.

## Verdict and boundaries

- **PASS:** Hamiltonian factorization, positive spectral scaling, ground-subspace/projector invariance, and exact mutual-information scaling identity for finite-dimensional self-adjoint operators with a well-defined ground eigenspace.
- **Conditional vector statement:** A ground-state vector equality up to phase assumes a simple ground eigenvalue. If degenerate, state the equality at projector/subspace level instead.
- **Not included:** (h=0) (division defining (x) is unavailable); differentiability/analyticity of (mathcal G_N); entropy derivative claims at rank-changing reduced states; proof of any self-consistent solution.
- **Formal status:** No Lean declaration has been checked that proves this complete manuscript claim or its exact correspondence. This is an algebraic/spectral analytic audit, not formal verification.

## Reproducibility

The derivation uses only substitution and the elementary spectral fact that a positive scalar multiple of a finite-dimensional self-adjoint operator preserves eigenspace ordering. The reduced-state and entropy identities follow from equality of projectors.
