# IV-38 — Hamiltonian and Perturbation Convention Audit

**Target:** Weak-coupling candidate for (B-C), with exact source definitions reconciled in IV-36  
**Status:** SOURCE-CONVENTION PASS / LEADING AMPLITUDE CHECK PARTIAL / NOT VERIFIED  
**Scope:** Inspect the frozen Hamiltonian, derive unperturbed energy denominators and first-order pair-flip amplitude, check signs and factors, and compare the result with the working derivation.

## 1. Frozen Hamiltonian

Section 2.1 of the frozen manuscript defines
[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^x,qquad h>0.
]
At (J_{ij}=0), the ground state is the product (|+x\rangle^{\otimes N}), with energy (-Nh). A computational (z)-basis configuration with (m) spins flipped relative to the uniform transverse-field ground state is more naturally counted in the (x)-basis; each single (x)-basis excitation costs (2h), so a two-spin excitation costs (4h).

The perturbation is
[
V=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z.
]
Since (\sigma^z|+x\rangle=|-x\rangle), a single pair interaction flips exactly two (x)-basis spins. Thus
[
\langle -x_i,-x_j|V|+x,\ldots,+x\rangle=-J_{ij},
]
and the first-order Rayleigh-Schrödinger amplitude is
[
a_{ij}=\frac{\langle ij|V|0\rangle}{E_0-E_{ij}}
=\frac{-J_{ij}}{-4h}
=\boxed{\frac{J_{ij}}{4h}}.
]
**Sign and denominator PASS:** positive (J_{ij}) gives positive amplitude in the chosen real phase convention; the magnitude factor (1/(4h)) is correct.

## 2. First-order state and convention

Up to normalization and higher orders,
[
|\Psi\rangle=|0\rangle+\sum_{i<j}\frac{J_{ij}}{4h}|ij\rangle+O(J^2/h^2).
]
The phase of individual basis vectors can change amplitude signs, but reduced-density eigenvalues and the entropy are invariant under consistent phase changes. The leading probabilities depend on (|a_{ij}|^2=J_{ij}^2/(16h^2)), so the convention is consistent with the one-site leading eigenvalue (p_i=\sum_{j\ne i}|a_{ij}|^2).

## 3. Edge-direction derivative check

At the symmetric point (J_{ij}=J), (r=J/h), the one-site leading small eigenvalue is
[
p_i=\frac{N-1}{16}r^2+O_N(r^3).
]
Differentiating the leading expression with respect to an incident edge (J_{13}) gives, in dimensionless edge parameter (u_{13}) where (J_{13}=J(1+u_{13})),
[
\partial_{u_{13}}p_1=\frac{r^2}{8}+O_N(r^3).
]
For nonincident edge (J_{34}), site 1 has no direct first-order amplitude contribution; the corresponding displayed leading derivative is absent (higher order only). This is consistent with the edge-direction distinction used in the candidate coefficient calculation.

## 4. Scope limitations / items not closed

- The pair-flip amplitude check is a first-order perturbative calculation; it does not independently rederive all second-/higher-order amplitudes.
- The error notation (O_N(r^3)) in differentiated eigenvalue statements requires uniform derivative control, which is not established by the first-order calculation alone.
- Two-site block eigenvalues and their complete entropy derivatives, especially low/zero branches, remain subject to the unresolved remainder obligations.
- This audit does not establish (B-C>0), the candidate coefficient's completeness, or a global weak-coupling theorem.
- Lean formalization/build has not been run.

## 5. Disposition

Frozen Hamiltonian sign and form: **SOURCE-CONFIRMED**.  
Pair-flip excitation denominator (4h): **DERIVED**.  
First-order amplitude (J_{ij}/(4h)): **PASS**.  
Leading probability scale (J^2/(16h^2)): **PASS**.  
Higher-order differentiated remainder and full entropy coefficient: **OPEN**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.