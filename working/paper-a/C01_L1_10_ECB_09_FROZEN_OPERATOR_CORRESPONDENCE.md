# C01-L1.10 — ECB-09 Frozen-Manuscript Operator Correspondence Audit

**Status:** SOURCE-FETCH VERIFIED; MATHEMATICAL CORRESPONDENCE AUDIT; NOT LEAN-COMPILED  
**Frozen upstream:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Fetched source:** `Arxiv/paper_01_manuscript.md` (blob `ec2361c1ae17b955e845ec1726636795cc3b74ff`)  
**Scope:** Verify the Hamiltonian sign, shifted operator off-diagonal entries, edge positivity, and the finite-N connectivity assumption used in ECB-08.


## 1. Hamiltonian from frozen source

Section 2.1 gives

\[
H[\mathbf J]=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_{i=1}^N\sigma_i^x,\qquad h>0.
\]
The source specifies computational \(\sigma^z\) basis and states finite-N ground-state nondegeneracy from Perron–Frobenius after a sufficiently large identity shift.

## 2. Off-diagonal entries

In the computational \(\sigma^z\) basis, \(\sigma_i^x\) flips spin i and has matrix coefficient +1. The transverse-field term in H therefore contributes **−h** to every single-spin-flip off-diagonal entry. Other terms in H are diagonal in this basis.

For \(K=cI-H\), each single-spin-flip off-diagonal entry is consequently **+h**, strictly positive because h>0. No other off-diagonal entries are nonzero in this model. This confirms the positive-edge condition needed for the hypercube propagation argument.

## 3. Diagonal shift

The diagonal entries of H are \(-\sum_{i<j}J_{ij}z_i z_j\). The corresponding entries of K are \(c+\sum_{i<j}J_{ij}z_i z_j\). For finite couplings, choose c larger than the maximum absolute diagonal energy (or otherwise large enough that every shifted diagonal entry is nonnegative). This shift does not change eigenvectors and must be stated as an existence choice, not treated as a fixed universal value without bounds.

## 4. Graph connectivity

The configuration graph whose edges are single-spin flips is the N-dimensional hypercube. It is connected: between any two bit/spin configurations, flip each coordinate where the configurations disagree. Because K has positive coefficient h on every such edge, its positive off-diagonal graph contains the full hypercube and is connected for finite N≥1.

The frozen manuscript's theorem statement in Section 2.1 explicitly scopes this ground-state claim to finite N and h>0. ECB-08 should therefore be applied to N≥1 as in the source; the N=0 singleton case may be handled separately as a trivial extension but is not needed for the manuscript theorem.

## 5. ECB-08 correspondence result

The frozen Hamiltonian verifies the abstract ECB-08 hypotheses for finite N≥1 and h>0:
- real symmetric matrix in the computational basis;
- off-diagonal entries nonnegative after shifting;
- strictly positive coefficients on all single-spin-flip hypercube edges;
- connected positive-edge graph;
- the constructed top-eigenvector can be chosen nonnegative by ECB-01–05 and is nonzero by ECB-03.

The zero-propagation argument therefore establishes strict positivity of this nonnegative top eigenvector. The shift c is chosen to make the matrix entrywise nonnegative, but the connectivity/strict-positivity propagation only uses positive off-diagonal edges; diagonal shift magnitude does not affect graph connectivity.

## 6. Source authority and remaining formal work

This audit was fetched from the frozen upstream commit, not the moving default branch. It verifies the Hamiltonian/operator sign correspondence at source level. It does **not** establish that Lean code exists or compiles, that the proof is integrated into the formal project, or that any downstream entropy differentiability/fold claim follows.

**Disposition:** Hamiltonian sign and positive spin-flip edge correspondence verified against frozen source. Abstract strict-positivity argument is mathematically justified. Formal implementation, compilation, and axiom audit remain pending; status **NOT FORMALLY VERIFIED**.
