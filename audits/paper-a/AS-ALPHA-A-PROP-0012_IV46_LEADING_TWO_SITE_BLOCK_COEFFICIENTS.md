# IV-46 — Leading Two-Site Parity-Block Coefficients from First-Order State

**Status:** FIRST-ORDER AMPLITUDES PASS / LEADING BLOCK COEFFICIENTS DERIVED CONDITIONALLY / HIGHER-ORDER TERMS OPEN  
**Scope:** Use the frozen Hamiltonian and first-order ground-state amplitudes to derive leading coefficients of two-site parity blocks. This is not a complete entropy expansion.

## 1. First-order state amplitudes

With H0=-h sum_i sigma_i^x, h>0, the unperturbed state is all + in the x-basis. Pair interaction -J_ab sigma_a^z sigma_b^z creates a two-flip state with energy gap 4h and amplitude +J_ab/(4h). Define g_ab=J_ab/(4h). To first order:
|psi> = (1 - 1/2 sum_(a<b) g_ab^2)|0> + sum_(a<b)g_ab |ab> + higher-order terms,
where |ab> is the x-basis configuration with spins a,b flipped. The normalization correction shown is the quadratic norm correction from first-order amplitudes; it is not a complete second-order wavefunction.

## 2. Leading even block for retained sites i,j

Let g_ab=J_ab/(4h), and let A_i = sum_(k != i) g_ik^2, A_j = sum_(k != j) g_jk^2. Then through quadratic probability order:
E11 = 1 - A_i - A_j + g_ij^2 + higher order,
E22 = g_ij^2 + higher order,
E12 = g_ij + higher order,
E21 = conjugate(E12).
For real couplings, E12 is real. The E11 correction removes all first-order pair-excitation probabilities involving either retained site, while environment-only excitations cancel between vacuum normalization and traced environmental configurations. Note E11+E22+Tr(O)=1 imposes consistency on the remaining block.

## 3. Leading odd block

For k outside {i,j}, a retained single flip accompanied by an environment flip is a first-order pair excitation:
O11 = sum_(k != i,j) g_jk^2 + higher order,
O22 = sum_(k != i,j) g_ik^2 + higher order,
O12 = sum_(k != i,j) g_jk g_ik + higher order,
O21 = conjugate(O12).
These expressions follow by matching identical environment configurations in the partial trace. Terms are real for the frozen real Hamiltonian. Higher-order paths and differentiated remainder are not evaluated.

## 4. Checks

- E11+E22+O11+O22 = 1 through quadratic order, after substituting A_i,A_j.
- The even block determinant at this order has cancellation of the g_ij^2 vacuum-pair contribution; its small eigenvalue is controlled by incident-edge/environment terms and requires higher-order matrix accuracy before a reliable coefficient is claimed.
- The odd block is a Gram matrix at leading order, hence positive semidefinite; O11 O22 - |O12|^2 >= 0 follows from Cauchy-Schwarz over k.

## 5. Scope and cautions

The listed coefficients are leading terms derived from first-order amplitudes and normalization bookkeeping. They do not certify complete O(g^2) matrix entries where second-order state amplitudes also contribute, nor entropy derivatives involving small eigenvalues. The “higher order” remainders need coupling-uniform and differentiated estimates before use in B or C. No B-C sign or final asymptotic coefficient is claimed.

## 6. Disposition

First-order pair-flip amplitudes: **PASS**.  
Leading block coefficients from first-order amplitudes: **CONDITIONAL PASS (order bookkeeping)**.  
Full second-order state and matrix entries: **OPEN**.  
Low-spectrum entropy derivative and B-C: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
