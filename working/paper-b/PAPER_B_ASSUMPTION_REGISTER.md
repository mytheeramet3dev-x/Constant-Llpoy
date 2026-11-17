# Paper B Assumption and Admissibility Register

Official title: **Equivariant Bifurcation, Isotropy Classification, Representation-Resolved Stability, and Nonlinear Branch Structure in Self-Consistent Quantum Interaction Networks**

| ID | Assumption / condition | Why it is needed | Status / handling |
|---|---|---|---|
| A-N | Fixed finite integer (N\ge4) | Edge representation has the three-sector decomposition used by the project. | Scope condition |
| A-H | (h>0) | Transverse-field term; supports finite-dimensional irreducibility of the computational-basis Hamiltonian. | Scope condition |
| A-G | (g>0) | Positive feedback gain. | Scope condition |
| A-J | Symmetric base coupling (J_*>0) | A sufficiently small ambient neighborhood can remain inside the nonnegative physical coupling cone. | Scope condition; verify branch-specific |
| A-DOM | Open neighborhood in (mathbb R^{\binom N2}) around the symmetric point | Needed for Fréchet derivatives and local bifurcation analysis. | Must be reconciled with physical cone |
| A-GS | Simple ground state on the domain | Needed for a smooth ground-state projector and unambiguous ground-state reduced states. | Prove/model-check; do not infer entropy smoothness from this alone |
| A-RANK | Required reduced states have controlled rank / small-eigenvalue behavior | Needed for differentiability of von Neumann entropies and mutual information. | Mandatory regularity gate; OPEN |
| A-EQ | (S_N)-equivariance of the feedback map | Needed for equivariant reduction and isotropy analysis. | Prove from model |
| A-CRIT | Exactly one nontrivial isotypic sector becomes critical, unless a mode interaction is treated | Needed for a single-critical-mode reduction. | OPEN |
| A-TR | Nonzero crossing derivative | Needed for a transverse bifurcation. | OPEN |
| A-COMP | Complementary linearization is invertible | Needed for Lyapunov–Schmidt reduction. | OPEN |
| A-NL | Sufficient differentiability for the chosen nonlinear theorem | Needed for Taylor expansion / normal form. | Must be proved on relevant subspaces; never assumed globally by convenience |
| A-ISO | Chosen isotropy subgroup has the required fixed-space dimension | Needed for a branch theorem such as EBL. | Compute per (N), sector, and subgroup |
| A-DYN | Default stability dynamics are Picard iteration (x_{n+1}=\eta\mathcal I_N(x_n)) | Stability is undefined until an update rule is specified. | Adopted default; disclose in manuscript |
| A-PHYS | Branch couplings remain nonnegative | Needed for physical admissibility under the reference ferromagnetic model. | Verify for every branch |

## Prohibited shortcuts

- Do not replace A-RANK with “the Hamiltonian is finite-dimensional.”
- Do not replace A-NL with “the ground state is analytic.”
- Do not apply EBL before verifying its hypotheses for the actual feedback map.
- Do not infer nonlinear stability from a linear response ordering alone.
- Do not claim global branch classification from a local isotropy calculation.
