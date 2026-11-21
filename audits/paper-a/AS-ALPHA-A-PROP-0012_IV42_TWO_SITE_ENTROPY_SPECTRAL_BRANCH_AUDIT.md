# IV-42 — Two-Site Entropy Derivative and Spectral Branch Audit

**Status:** EXACT SPECTRAL IDENTITY PASS / BRANCH-EXPANSION OBLIGATIONS IDENTIFIED / COEFFICIENT OPEN  
**Scope:** Establish safe entropy derivative identities for two-site reduced states, check degeneracy/zero-spectrum hazards, and identify what is required before perturbative eigenvalue expansions can be used for B-C.

## 1. Exact two-site entropy derivative

Let the two-site reduced density matrix be a differentiable positive semidefinite matrix rho(u), trace one. If rho(u) is strictly positive, then
[
S(ho)=-operatorname{Tr}(holnho),qquad
S_u=-operatorname{Tr}(ho_ulnho),
]
because (operatorname{Tr}ho_u=0). This identity does not require individual eigenvalues to be nondegenerate.

If rho has zero eigenvalues, ln(rho) is unbounded on the kernel. The identity may still be valid under a suitable support/regularity condition, but cannot be invoked without checking the low-spectrum behavior.

## 2. Eigenvalue derivative representation and degeneracy

For a positive, nondegenerate spectrum (lambda_k(u)),
[
S_u=-sum_k lambda_{k,u}lnlambda_k,qquad
lambda_{k,u}=langle k|ho_u|kangle.
]
At degeneracy, individual eigenvalue derivatives depend on diagonalizing rho_u within the degenerate eigenspace; a stable formulation uses spectral clusters or the trace identity. Near eigenvalues tending to zero, entropy derivative control is sensitive to both eigenvalue order and derivative order.

## 3. Two-site entropy and mutual information response

For the edge mutual information,
[
I_{12}=S(ho_1)+S(ho_2)-S(ho_{12}).
]
Therefore an edge-direction derivative is exactly
[
partial_u I_{12}
=partial_u S(ho_1)+partial_u S(ho_2)-partial_u S(ho_{12}),
]
provided each entropy derivative exists. This identity is bookkeeping-exact but does not provide the small-coupling coefficients.

## 4. Required branch obligations before coefficient extraction

A valid perturbative reconstruction must:
1. Construct the two-site matrix rho_12 to the matrix order sufficient for the entropy derivative, not merely state-amplitude order.
2. Separate eigenvalue clusters by justified spectral gaps or use a gap-free trace/log identity on the strictly positive region.
3. Track low eigenvalues with explicit vanishing order and factorization, e.g. lambda(r,u)=r^k a(r,u), and provide bounds on a and a_u where logarithmic terms are used.
4. Treat branches whose leading coefficient vanishes separately; ln(a) expansions are invalid at a=0.
5. Include eigenvalue mixing/off-diagonal matrix terms and normalization contributions at consistent order.
6. Prove derivative control of the matrix/eigenvalue remainder; value-only O(r^k) bounds do not suffice.

## 5. Audit finding

The exact entropy derivative identity and mutual-information derivative decomposition are PASS. No numerical or symbolic full two-site reduced matrix expansion has been reconstructed in this audit. Thus no two-site eigenvalue coefficient, low-spectrum logarithmic coefficient, or B-C coefficient is certified here. This audit intentionally does not infer a sign from the earlier candidate formula.

## 6. Disposition

Exact identities: **PASS**.  
Perturbative two-site eigenvalue branches: **OPEN**.  
Low-spectrum logarithmic derivative bounds: **OPEN**.  
Full B-C coefficient: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
