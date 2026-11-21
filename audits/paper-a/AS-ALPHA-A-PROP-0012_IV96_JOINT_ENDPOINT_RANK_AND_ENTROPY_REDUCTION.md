# IV-96 — Exact Rank Bound for the Joint Endpoint State and Entropy Reduction

**Status:** VERIFIED STRUCTURAL FACT / ANALYTIC-PARTIAL. Leading expansion for q is not proved.

## Model
Three-spin path Hamiltonian H=-J12 Z1Z2-J23 Z2Z3-h(X1+X2+X3), h>0. Consider any pure ground state |psi> of the three-spin system (in particular, the nondegenerate ground state in the perturbative region).

## Exact rank fact
The bipartition (sites 1,3) versus site 2 has dimensions 4 and 2. For a pure bipartite state, reduced-state ranks agree and are bounded by the smaller subsystem dimension. Therefore
rank(rho_13)=rank(rho_2)<=2
exactly, without perturbation theory. Consequently rho_13 has at most two nonzero eigenvalues, which can be written q and 1-q. Its entropy is exactly binary entropy h(q), not merely an approximation. No additional joint-state eigenvalues contribute.

## Exact entropy identity
Writing marginal small eigenvalues p1 and p3, the mutual information is exactly
I(1:3)=h(p1)+h(p3)-h(q)
where h(u)=-u ln u-(1-u)ln(1-u) (nats), with the usual continuous extension at 0 and 1. This reduces the joint entropy obligation in IV-94 to estimating the single nontrivial eigenvalue q.

## Numerical sanity check (locally executed double precision)
A local 8x8 diagonalization and explicit tensor partial trace was performed. Results (small eigenvalues; roundoff near zero is expected):
- J12=J23=0.01: rho_13 eigenvalues approximately (0,0,1.24998437e-5,0.9999875002); marginal small eigenvalues p1=p3≈6.25007812e-6.
- J12=0.01, J23=0.1: rho_13 eigenvalues approximately (0,0,6.30088212e-4,0.9993699118); p1≈6.26937927e-6, p3≈6.23850024e-4.
- J12=0.0001, J23=0.1: rho_13 eigenvalues approximately (0,0,6.23831187e-4,0.9993761688); p1≈6.26949742e-10, p3≈6.23830563e-4.

These calculations check the rank structure and illustrate q near x+y for tested weak couplings; they are not a proof of the expansion or uniform remainder.

## Remaining spectral target
Prove q=x+y+O((x+y)^2) uniformly near the coupling origin. Combined with IV-95's ratio-aware marginal factorization, this would provide all eigenvalue inputs to the conditional entropy-remainder lemma in IV-94. The analytic coefficient and uniform constants remain to be derived.

## Status
Joint rank bound and exact binary entropy reduction are structural facts. Proposition 0012 and Paper A remain OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
