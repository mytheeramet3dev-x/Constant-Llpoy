# IV-45 — Environment Parity and Perturbative Order Audit

**Status:** PARITY SELECTION RULE PASS / GENERIC ORDER COUNTING CONDITIONAL / COEFFICIENTS OPEN  
**Scope:** Use x-basis spin-flip structure to infer allowed full-state amplitudes and generic orders of the two-site parity-block entries. This is order counting only, not a coefficient reconstruction.

## 1. x-basis configurations and selection rule

The unperturbed Hamiltonian H0=-h sum_i sigma_i^x has ground state |+...+>_x. The interaction V=-sum_(i<j)J_ij sigma_i^z sigma_j^z flips exactly two x-basis spins per application. Thus the global x-parity P_x is conserved. In the ground-state parity sector connected analytically to the unperturbed ground state, full-state amplitudes of configurations with odd total number of x-spin flips vanish exactly.

For a configuration with m flipped spins (m even), its first possible perturbative order under pair-flip interactions is at least m/2. This lower bound is combinatorial and may be higher if graph/coupling paths are absent or cancel.

## 2. Environment parity and two-site block entries

For retained sites i,j and environment configuration e with q flips, global parity requires the retained two-site flip count plus q to be even. Hence:
- even retained configurations (++ or --) pair only with even-parity environment configurations;
- odd retained configurations (+- or -+) pair only with odd-parity environment configurations.
This explains cross-sector partial-trace terms vanish; it is a selection rule, not a termwise numerical approximation.

## 3. Generic symmetric-coupling order estimates

Let r denote a small dimensionless coupling scale and assume generic nonzero allowed paths, with coefficients analytic near r=0. Environment parity and minimum flip count give the following expected first-possible orders for the entries in IV-44:
- E11 = 1 + O(r^2) (trace/normalization may affect the r^2 coefficient);
- E22 = O(r^2);
- E12 = O(r), from coherence of the unperturbed vacuum with a two-flip retained configuration;
- O11 = O(r^2), because one retained flip requires an odd environment flip, making each amplitude at least O(r);
- O22 = O(r^2);
- O12 = O(r^2), since both amplitudes require an odd-flip environment, with leading shared environment configurations having at least two total flips.

These are generic upper-order expectations / first-possible orders, not certified coefficients. Coupling sparsity, vanishing paths, cancellation, and derivative-specific effects may raise orders. The matrix trace normalization correlates diagonal coefficients.

## 4. Edge derivative caveat

Differentiating with respect to a coupling J_e changes coefficients in the perturbative series, but does not automatically preserve a claimed uniform remainder. To use entry-order estimates for B or C, prove differentiated analyticity and a uniform bound in a coupling neighborhood. This audit does not prove that bound.

## 5. Disposition

Exact parity selection rule: **PASS**.  
Minimum flip-count lower bound: **PASS (combinatorial)**.  
Generic entry-order pattern: **CONDITIONAL / ANALYTIC ORDER COUNTING**.  
Explicit entry coefficients and uniform edge derivatives: **OPEN**.  
Entropy/eigenvalue expansion and B-C sign: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
