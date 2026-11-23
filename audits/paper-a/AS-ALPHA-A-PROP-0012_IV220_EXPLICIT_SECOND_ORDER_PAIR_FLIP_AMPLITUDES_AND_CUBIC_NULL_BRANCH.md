# IV-220 — Explicit Second-Order Pair-Flip Amplitudes and Cubic Null-Branch Audit

**Target:** `AS-ALPHA-A-PROP-0012`, weak-coupling odd reduced block and cubic null branch  
**Status:** ANALYTIC DERIVATION / MODEL-STATE MAPPING OPEN / NOT VERIFIED  
**Date:** 2026-11-23  
**Scope:** Derive perturbative pair-flip coefficients for the transverse-field Ising Hamiltonian in the x-product basis. This record does not claim that the coefficients are already the retained-odd/environment amplitude coefficients of IV-50.

## 1. Convention and unperturbed basis

Use
\[
H_0=-h\sum_i\sigma_i^x,\qquad
V=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z,
\]
with \(h>0\). Let \(|S\rangle\) denote the x-basis state obtained by flipping the set \(S\) relative to the all-\(+x\) vacuum \(|0\rangle\). For even-cardinality sets, the energy gap is \(E_S-E_0=2h|S|\); in particular, a pair-flip state has gap \(4h\).

Take a small-coupling parameterization \(J_{ij}=r h g_{ij}\), where the dimensionless edge weights \(g_{ij}\) are fixed while \(r\to0\). This parameterization is introduced for this coefficient calculation and must be reconciled with the manuscript's own weak-coupling variable before claim-level use.

## 2. First-order pair-flip coefficient

For an edge/pair \(e=\{i,j\}\), the perturbation matrix element is
\[
\langle e|V|0\rangle=-J_e.
\]
The first-order Rayleigh-Schrödinger coefficient is
\[
c_e^{(1)}=\frac{\langle e|V|0\rangle}{E_0-E_e}
=\frac{J_e}{4h}=r\frac{g_e}{4}.
\]
Thus, under the stated convention, \(a_e=g_e/4\).

## 3. Second-order coefficient for a pair target

For a target pair \(e\), the standard nondegenerate second-order coefficient (intermediate states excluding the ground state) is
\[
c_e^{(2)}=\sum_{m\ne0}
\frac{\langle e|V|m\rangle\langle m|V|0\rangle}
{(E_0-E_e)(E_0-E_m)}
-\frac{\langle0|V|0\rangle\langle e|V|0\rangle}
{(E_0-E_e)^2}.
\]
Here \(\langle0|V|0\rangle=0\). Only pair-flip intermediate states \(m=f\) can contribute to this two-step path: the first perturbation flips pair \(f\), and the second must flip pair \(e\triangle f\). The resulting state is \(e\) precisely when the symmetric difference \(e\triangle f\) is another pair. For distinct pairs, this happens exactly when \(e\) and \(f\) share one vertex. Since both denominators equal \(-4h\), their product is \(16h^2\), giving
\[
c_e^{(2)}=\frac{1}{16h^2}
\sum_{\substack{f\ne e,\ |f|=2,\ |e\triangle f|=2}}
J_fJ_{e\triangle f}
= r^2\,b_e,
\]
where
\[
\boxed{b_e=\frac1{16}
\sum_{\substack{f\ne e,\ |f|=2,\ |e\triangle f|=2}}
g_fg_{e\triangle f}.}
\]
The sum is over ordered intermediate pair states \(f\), so complementary path orderings are both counted when they are distinct intermediate states. This coefficient is derived for the ground-state pair-flip wavefunction in the stated x-basis convention.

## 4. Uniform complete-graph specialization

If every edge has \(g_e=1\), then for a fixed pair \(e\), exactly \(2(N-2)\) other pairs \(f\) share one endpoint with \(e\). Hence
\[
b_e=\frac{2(N-2)}{16}=\frac{N-2}{8},
\qquad
c_e(r)=\frac r4+\frac{N-2}{8}r^2+O(r^3).
\]
This is a coefficient result for an isolated pair-flip amplitude, not a derivation of the subsystem odd-block entries.

## 5. Parameter derivatives

For a dimensionless edge parameter \(u_q\) entering \(g_e\), the coefficient derivative is obtained by differentiating the finite path sum:
\[
\partial_{u_q}b_e=\frac1{16}
\sum_{\substack{f\ne e,\ |f|=2,\ |e\triangle f|=2}}
\left[(\partial_{u_q}g_f)g_{e\triangle f}
+g_f(\partial_{u_q}g_{e\triangle f})\right].
\]
For the uniform point where \(g_e=1\) and an edge parameter independently perturbs one coupling, this derivative is an explicit count of paths containing that edge. However, the mapping of manuscript parameters \(u_{13},u_{34}\) onto the full coupling family and the corresponding environment-resolved amplitudes must be specified before these derivatives can be substituted into IV-50.

## 6. Cubic odd-block null coefficient: not yet closed

IV-50 requires amplitudes indexed by retained odd states \(\alpha\in\{+-, -+\}\) and environment configurations \(\epsilon\), with
\[
c_{\alpha,\epsilon}=r a_{\alpha,\epsilon}
+r^2b_{\alpha,\epsilon}+O(r^3).
\]
The cubic odd-block entries are interference sums
\[
O^{(3)}_{\alpha\beta}=\sum_\epsilon
(a_{\alpha,\epsilon}b_{\beta,\epsilon}
+b_{\alpha,\epsilon}a_{\beta,\epsilon}),
\]
and
\[
B_{vv}=\frac{O^{(3)}_{11}+O^{(3)}_{22}
-O^{(3)}_{12}-O^{(3)}_{21}}2.
\]
The pair-target coefficient derived in Sections 2–4 does **not** alone identify all \(a_{\alpha,\epsilon}\), \(b_{\alpha,\epsilon}\) required here. The exact reduced-state/environment basis, normalization convention, and correspondence between environment configurations and perturbative paths are still required. Therefore this audit does not evaluate \(B_{vv}\), does not prove its vanishing, and does not establish that the small eigenvalue begins at order \(r^4\).

## 7. Disposition

- First-order pair-flip coefficient in the stated convention: **DERIVED**.
- Second-order pair-flip path formula: **DERIVED**, under nondegenerate ground-state perturbation theory at \(h>0\).
- Uniform complete-graph coefficient \(b_e=(N-2)/8\): **DERIVED** for the pair-flip amplitude.
- Edge-parameter derivative of the path formula: **DERIVED FORMALLY**; concrete \(u_{13},u_{34}\) mapping remains unspecified.
- Mapping from pair-flip amplitudes to IV-50 retained-odd/environment amplitudes: **OPEN**.
- Cubic null coefficient \(B_{vv}\): **OPEN / NOT EVALUATED**.
- Small odd-block eigenvalue order, entropy derivative closure, and global \(B-C\) sign: **OPEN**.
- Lean verification or executable numerical validation: **NOT PERFORMED**.

## 8. Next obligation

IV-221 should freeze the exact subsystem/environment x-basis convention and construct the environment-resolved reduced-state amplitudes from the perturbative eigenvector, then evaluate the cubic null combination directly. Do not promote the pair-flip result above into a reduced-block theorem without that explicit mapping.
