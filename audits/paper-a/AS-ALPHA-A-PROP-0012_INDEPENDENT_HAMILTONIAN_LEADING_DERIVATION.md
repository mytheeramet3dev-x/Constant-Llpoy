# PROP-0012 — Independent Hamiltonian-to-Leading-Entropy Derivation

**Frozen source:** `8deb7de4a49cb2060720246b7101820ee7e08c91`.  
**Scope:** Fixed finite (N\ge4), (h>0), (r=J/h\to0^+), symmetric reference and independent edge perturbations. Leading order only.

## 1. First-order ground state from the Hamiltonian

For (H_0=-h\sum_iX_i), the ground state is (|+\cdots+\rangle_x). A pair flip (|ij\rangle_x) has excitation energy (4h). The perturbation (-J_{ij}Z_iZ_j) has matrix element (-J_{ij}), so nondegenerate first-order perturbation theory gives
[
a_{ij}=\frac{J_{ij}}{4h}+O_N(r^2)=\frac r4(1+u_{ij})+O_N(r^2).
]
The sign is positive. This independently confirms the coefficient in the working derivation.

## 2. One-site small eigenvalue

At leading order the small one-site eigenvalue is the total pair-flip probability incident to site (i):
[
p_i=\sum_{j\ne i}a_{ij}^2+O_N(r^3).
]
At the symmetric point (p=(N-1)r^2/16+O_N(r^3)). For edge (13), (partial_{u_{13}}p_1=r^2/8+O_N(r^3)); the derivative for site 2 is higher order. For disjoint edge (34), both one-site derivatives relevant to sites 1,2 are (O_N(r^3)).

## 3. Two-site odd block and eigenvalue derivative

The odd block has equal diagonal entries at the symmetric point, (D=(N-2)r^2/16+O_N(r^3)), and coherence (C=(N-2)r^2/16+O_N(r^3)). The positive eigenvalue is (q=D+C=(N-2)r^2/8+O_N(r^3)).

For perturbing edge (13), the positive eigenvalue derivative is the symmetric eigenvector expectation: the diagonal derivative contributes half of (partial(a_{13}^2)=r^2/8), i.e. (r^2/16); the coherence derivative contributes (partial(a_{13}a_{23})=r^2/16). Their sum is (r^2/8). Edge (34) does not enter these first-order amplitudes, so its derivative has no (r^2) term.

## 4. Leading entropy cancellation

Using (H'(p)=\ln((1-p)/p)) and the entropy derivative (-q'(1+\ln q)), the contrast for **dimensionless edge variables** (u_e) is
\[
\partial_{u_{13}}I_{12}-\partial_{u_{34}}I_{12}=\frac{r^2}{8}\ln\frac{q}{p}+O_N(r^3(1+|\ln r|)).
\]
Because (u_e) perturbs (J_e=J(1+u_e)), physical response derivatives satisfy (B-C=J^{-1}(\partial_{u_{13}}I-\partial_{u_{34}}I)). Hence

Since
[
\frac qp=\frac{(N-2)r^2/8}{(N-1)r^2/16}+O_N(r)=\frac{2(N-2)}{N-1}+O_N(r),
]
this gives
[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right).
]
The leading coefficient is strictly positive for each fixed (N\ge4). Hence the asymptotic statement (B-C>0) sufficiently near (J/h=0) follows **if** the stated model-specific remainder bounds are established.

## 5. Independently reproduced diagnostic

The full-Hilbert-space central-difference calculation was independently executed at 40 dps for (N=4,5,6), (J/h=0.005,0.001), step (10^{-4}J). All six (B-C) values are positive and ratios to the leading expression approach 1 as the coupling decreases. Values are listed in the companion fresh numerical report.

## Limitations

This independent derivation closes the Hamiltonian-to-first-order-amplitude and leading reduced-block algebra. It does **not** prove the joint analytic eigenbranch bounds and differentiated entropy remainders in a complete standalone fashion, does not formalize in Lean, and does not prove a global sign for arbitrary coupling or sizes.

**Disposition:** Leading weak-coupling coefficient independently derived; remainder and global conjecture remain OPEN.
