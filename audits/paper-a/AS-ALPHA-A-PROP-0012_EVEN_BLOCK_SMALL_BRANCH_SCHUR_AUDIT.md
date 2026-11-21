# PROP-0012 — Even-Block Small Eigenbranch: Schur Remainder Audit

**Scope:** Fixed finite N, weak coupling r=J/h, independent real edge perturbations u in a sufficiently small fixed neighborhood of the uniform point. This is an analytic block-level audit, not Lean formalization.

## 1. Inputs and provenance of orders

The finite-dimensional Hamiltonian has a unique gapped ground state at r=0. Kato/Riesz spectral projection therefore gives a jointly real-analytic ground-state projector in (r,u) near the origin for fixed N. Reduced density matrix entries are analytic as finite partial traces.

The even parity block entries are claimed from pair-flip selection rules and the first-order state:
- L=1+O_N(r^2);
- X=a_12+O_N(r^2), a_12=r(1+u_12)/4;
- S=a_12^2+O_N(r^3).

The last two estimates, with their u-derivatives, need to be explicitly traced to the state expansion / selection rules in the derivation. They are used here as the entry-expansion hypotheses, not independently recomputed from every higher-order wavefunction coefficient.

## 2. Schur cancellation

Let D=S-|X|^2/L. Since L stays bounded away from 0,
1/L=1+O_N(r^2), and |X|^2=a_12^2+O_N(r^3), while S=a_12^2+O_N(r^3). Therefore D=O_N(r^3) jointly on the chosen edge-perturbation neighborhood.

For a positive 2x2 block, det M=L D. Its large eigenvalue λL=L+O_N(r^2) stays bounded away from 0. Hence the small eigenvalue is exactly
λs=det(M)/λL=(L/λL)D,
and L/λL=1+O_N(r^2). Thus λs=O_N(r^3). This determinant identity is stronger/cleaner than using a truncated eigenvalue formula.

Because the block entries and the isolated large eigenvalue are analytic, λs is an analytic branch in (r,u) near the origin. If the entry expansions hold with analytic O_N(r^3) remainders jointly in u, then λs=O_N(r^3) jointly; expanding the analytic remainder in r shows its first edge derivatives are also O_N(r^3) on a smaller fixed neighborhood. PSD gives λs≥0.

## 3. Entropy derivative consequence

Under the preceding verified-entry hypotheses, the reusable nonnegative analytic entropy lemma applies and gives
∂u[-λs ln λs]|_{u=0}=O_N(r^3(1+|ln r|).

This order is below the leading r^2 logarithmic contribution from the one-site and positive odd-block branches, so it does not change the leading coefficient. It remains a remainder contribution that must be included in the final error term.

## 4. Boundary of this audit

This audit closes the eigenvalue/Schur logic **conditional on the entry expansions**. It does not independently calculate the higher-order ground-state amplitudes needed to certify S=a_12^2+O_N(r^3) and X=a_12+O_N(r^2), including edge derivatives. It also does not close the full PROP-0012 derivation, reconcile the contradictory source lemma, prove a global sign, or formalize in Lean.

**Verdict:** Schur-to-small-eigenvalue and analytic derivative transfer are mathematically consistent and PASS conditional. Entry-expansion provenance remains open; overall PROP-0012 stays NOT-VERIFIED.
