# PROP-0012 — Explicit Second-Order Two-Flip Ground-State Amplitude

**Scope:** Finite N, weak-coupling TFIM in x-basis, independent edge couplings. This calculation demonstrates why two-flip amplitudes cannot be assumed to contain only odd powers of r.

Let H0=-h sum_i X_i. In the x-basis, an edge interaction -J_ab Z_a Z_b flips exactly the two spins a,b. A two-flip target |{1,2}> has first-order coefficient J_12/(4h).

At second order, for each k distinct from 1,2, the intermediate states |{1,k}> and |{2,k}> connect the vacuum to target |{1,2}> by two pair flips. Both ordered paths contribute. The intermediate and target excitation gaps are 4h each. The coefficient therefore includes
[
c_{12}^{(2)}=sum_{k
e1,2}rac{J_{1k}J_{2k}}{8h^2},
]
with the convention that the Hamiltonian interaction matrix element for each edge is -J and the perturbative denominators are E0-E_m=-4h. (This is the direct non-normalization contribution; vacuum normalization begins at second order but multiplies the first-order c12 only at third order.)

For independent nonzero edges this term is generically nonzero and is O_N(r^2). Hence c12=a12+O_N(r^2), not a12+O_N(r^3). This concrete perturbative contribution invalidates the prior parity-only refinement.

The report is a coefficient-level perturbative derivation for the stated convention. It does not establish the complete second-order wavefunction normalization or all reduced-block entries, nor formalize in Lean.
