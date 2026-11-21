# PROP-0012 — Independent Leading Coefficient Re-Derivation

**Date:** 2026-11-21  
**Scope:** Leading-order algebra for fixed finite N >= 4, uniform weak-coupling r=J/h, one adjacent-edge perturbation. This re-derives the coefficient from leading reduced-state entries and does not use the previously summarized final coefficient as an input. It is not a full independent spectral or remainder proof.

## 1. Hamiltonian and first-order pair amplitude

Take
\[
H=-h\sum_i\sigma_i^x-J\sum_{i<j}\sigma_i^z\sigma_j^x? 
\]
**Convention correction:** the interaction in this audit is the TFIM Ising term \(-J\sum_{i<j}\sigma_i^z\sigma_j^z\), and the transverse field is \(-h\sum_i\sigma_i^x\). The pair-flip matrix element is \(-J\), the excitation energy is \(4h\), and the first-order pair amplitude is
\[
a_{ij}=\frac{J_{ij}}{4h}=\frac r4
\]
at uniform coupling. Hence \(a^2=r^2/16\).

## 2. One-site eigenvalue

To leading order, the small one-site eigenvalue is the probability that site i is flipped:
\[
p_i=\sum_{j\ne i}a_{ij}^2+\text{higher order}.
\]
At the uniform point, \(p=(N-1)a^2=(N-1)r^2/16\). Under \(J_{13}=J(1+u)\), only \(p_1\) changes at leading order, with
\[
p_1'=2a^2=r^2/8.
\]

## 3. Odd two-site block and its positive eigenvalue

For pair 12, leading odd block entries are
\[
M=\begin{pmatrix}
A&C\\C&B
\end{pmatrix},\quad
A=\sum_{k=3}^N a_{2k}^2,\quad B=\sum_{k=3}^N a_{1k}^2,\quad
C=\sum_{k=3}^N a_{1k}a_{2k}.
\]
At uniform coupling, \(A=B=C=(N-2)a^2\), so \(q=2(N-2)a^2=(N-2)r^2/8\).
Under edge perturbation 13: \(A'=0\), \(B'=2a^2\), and \(C'=a^2\). At the symmetric point, the normalized positive eigenvector is \((1,1)/\sqrt2\), therefore
\[
q'=\frac{A'+B'}2+C'=2a^2=r^2/8.
\]
Thus, independently from the prior final-form summary, the leading derivatives match: \(p_1'=q'=r^2/8\).

## 4. Leading entropy contrast

For small eigenvalue x, \(H'(x)=\ln((1-x)/x)=-\ln x+O(x)\). The adjacent-edge leading contrast is consequently
\[
B-C=2a^2\ln(q/p)+\text{higher-order terms}
=\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}+\text{remainder}.
\]
The disjoint edge 34 does not enter the leading one-site or odd-block entries for sites 1,2. Even-block terms and zero-branch derivatives require the previously audited higher-order/branch estimates; this note does not independently rederive them.

Since \(q/p=2(N-2)/(N-1)>1\) for N>=4, the leading coefficient is positive. Conversion from dimensionless edge parameter to physical coupling uses \(\partial_{J_e}=J^{-1}\partial_{u_e}\), yielding the leading physical scale \(J/(8h^2)\) multiplying the logarithm.

## 5. Scope / verdict

**INDEPENDENT LEADING-COEFFICIENT ALGEBRA — PASS.** The pair-flip amplitude, leading one-site eigenvalue, odd-block eigenvalue, adjacent-edge derivatives, logarithmic ratio, and physical-coupling conversion are recomputed in this note.

Not established here: complete source reconciliation; independently closed even-block and all-branch remainders; uniform-in-N bounds; formal Lean theorem/build; or global \(B-C>0\). PROP-0012 remains OPEN. The remainder is inherited only conditionally from other audit reports, not proved by this independent coefficient check.
