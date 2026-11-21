# IV-39 — Second-Order Amplitude & Multi-Path Interference Audit

**Status:** PERTURBATIVE PATH COUNT / COEFFICIENT PASS (under nondegenerate unperturbed-state formula); FULL ENTROPY REMAINDER OPEN  
**Source convention:** IV-38, (H_0=-h\sum_i\sigma_i^x), (V=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z), (h>0)

## 1. State-space bookkeeping

In the (x)-basis, a pair edge (e=(ij)) flips the two sites in (e). The first-order coefficient for a two-flip state is (J_{ij}/(4h)), as verified in IV-38. At second order, amplitudes must be summed over ordered intermediate edges before the coefficient is interpreted.

For an excited state (|n\rangle), with (V_{00}=0), the second-order coefficient is
[
c_n^{(2)}=\sum_{m\ne0}\frac{V_{nm}V_{m0}}{(E_0-E_n)(E_0-E_m)}.
]
All terms here have two interaction matrix elements and two negative energy denominators, hence positive path products for the real coupling convention.

## 2. Four-flip final states: disjoint-edge paths

A four-site final flip set (Q=\{i,j,k,l\}) is reached through two disjoint pair edges. For a chosen pairing ((ab)(cd)), there are two ordered paths, (ab\to cd) and (cd\to ab). Each ordered path has denominators ((-8h)(-4h)=32h^2), and numerator (J_{ab}J_{cd}). Summing both orders gives (J_{ab}J_{cd}/(16h^2)).

There are three pairings of a four-site set, so
[
\boxed{c_{ijkl}^{(2)}=
\frac{J_{ij}J_{kl}+J_{ik}J_{jl}+J_{il}J_{jk}}{16h^2}}
]
for distinct (i,j,k,l). The three pairing channels interfere coherently in the amplitude; they must not be squared or counted as separate probabilities before being added.

## 3. Two-flip final states: shared-vertex paths

A second-order path ending in the two-flip set ({i,j}) can use edges ((i,k)) and ((j,k)) with shared intermediate vertex (k\notin\{i,j\}). Both orderings contribute. Each ordered path has denominator ((-4h)(-4h)=16h^2). Thus the second-order correction is
[
\boxed{c_{ij}^{(2)}=\sum_{k\ne i,j}\frac{J_{ik}J_{jk}}{8h^2}}
]
for this path family. This expression does not include third- or higher-order paths, nor other normalization contributions at higher orders.

## 4. Ground-state normalization bookkeeping

The second-order ground-state component from intermediate two-flip states is
[
c_0^{(2)}=-\frac12\sum_{i<j}\frac{J_{ij}^2}{16h^2}
=-\frac12\sum_{i<j}|c_{ij}^{(1)}|^2.
]
This is the standard normalization correction when the state is written with first-order amplitudes and normalized through second order. It affects the ground component and must be retained when constructing reduced density matrices to consistent order.

## 5. Audit findings

- Pair-flip denominator (4h) and first-order amplitude (J/(4h)): prior IV-38 PASS.
- Four-flip second-order amplitude path sum: derived, including three pairings and coherent summation.
- Two-flip second-order correction from shared-vertex paths: derived with ordered-path factor of 2.
- Ground-component normalization correction: identified.
- These state-amplitude results do **not** yet independently certify reduced-density eigenvalues, entropy derivative expansions, cancellations in (B-C), or uniform differentiated remainders. An explicit second-order reduced-density construction is the next obligation.
- No Lean formalization/build performed; derivation is analytic and not independently mechanized.

## 6. Disposition

Second-order path counting and denominators: **PASS (analytic derivation)**.  
Higher-order entropy and differentiated remainder implications: **OPEN**.  
PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.