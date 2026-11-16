# Canonical Strong-Coupling Derivation — Paper A

**Status:** WORKING DERIVATION / PARTIAL  
**Scope:** Uniform all-to-all TFIM, fixed finite \(N\ge4\), \(J>0\), \(h>0\), strong coupling \(x=J/h\to\infty\), with edge derivatives evaluated in the ambient real coupling space near the uniform point.  
**Repository boundary:** This document is confined to Constant Llapoy. It is not an instruction to modify Absolute Symmetry.

## 0. Proof objective and non-claims

The target is to derive, from the Hamiltonian and the two-site reduced state rather than by citation to an unrelated lemma,

\[
\mathcal G_N(x)
=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right),
\]

and, separately, a justified differentiated expansion

\[
\mathcal G_N'(x)
=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right).
\]

The first formula does not imply the second by differentiation of big-O notation. The derivative estimate is a separate obligation.

A second target is the fixed-\(N\) response asymptotic

\[
B-C
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(\frac{h^4}{J^5}
  \left[1+\left|\ln(h/J)\right|\right]\right),
\]

where \(B=\partial_{J_{13}}I_{12}\), \(C=\partial_{J_{34}}I_{12}\), and \(J_{13}\) shares one endpoint with observed edge \(12\), whereas \(J_{34}\) is disjoint. This requires coupling-derivative control of the entropy remainder and is not established in this document.

No uniform-in-\(N\) result, global sign theorem, explicit numerical threshold, or Lean proof is claimed.

## 1. Hamiltonian, scaling, and perturbation domain

At the uniform point,

\[
H(J,h)=-J\sum_{i<j}\sigma_i^z\sigma_j^z
-h\sum_i\sigma_i^x.
\]

Set

\[
\varepsilon=\frac hJ,\qquad
H=J(K_0+\varepsilon V),\quad
K_0=-\sum_{i<j}\sigma_i^z\sigma_j^z,\quad
V=-\sum_i\sigma_i^x.
\]

The unperturbed ground space of \(K_0\) is
\(\operatorname{span}\{|0^N\rangle,|1^N\rangle\}\), with energy
\(-\binom N2\). The global bit-flip parity
\(P=\prod_i\sigma_i^x\) commutes with \(H\). In the even-parity sector the selected unperturbed vector is

\[
|C_+\rangle=2^{-1/2}(|0^N\rangle+|1^N\rangle).
\]

A configuration with exactly \(k\) flipped spins has excitation energy

\[
E_k-E_0=2J\,k(N-k).
\]

Thus the first even-sector excitations (the one-flip/one-hole parity pairs) are separated by \(2J(N-1)\). For each fixed finite \(N\), this gives an isolated simple eigenvalue in the even sector at \(\varepsilon=0\), hence a locally analytic spectral projector for sufficiently small real \(\varepsilon\). The permitted radius is \(N\)-dependent and is not quantified here.

The perturbation is permutation invariant. The ground state for \(\varepsilon>0\) is in the fully symmetric spin sector; the perturbative coefficients may therefore be organized by Hamming weight. For edge-response derivatives, however, permutation symmetry is broken infinitesimally. Those derivatives must be obtained from the nonuniform-coupling problem before setting all \(J_{ij}=J\); they cannot be inferred by differentiating a uniform-only formula.

## 2. First-order state and the one-site reduced state

Let \(|\phi_i^+\rangle=2^{-1/2}(|i\rangle+|\bar i\rangle)\), where \(|i\rangle\) has spin \(i\) flipped relative to \(0^N\), and \(|\bar i\rangle\) is its global complement. The first-order even-sector correction is

\[
|\Psi(\varepsilon)\rangle
=|C_+\rangle+
\frac{\varepsilon}{2(N-1)}
\sum_{i=1}^N|\phi_i^+\rangle
+O_N(\varepsilon^2)
\]

in the even-sector Hilbert norm, with normalization corrections beginning at order \(\varepsilon^2\). Write

\[
b=\frac{\varepsilon}{2(N-1)}.
\]

By tracing out all sites except \(i\), or equivalently evaluating the parity-even one-site expectation, one obtains

\[
\rho_i=\frac12 I_2+b\,\sigma^x+O_N(\varepsilon^2)
\]

at the level of matrix entries. The eigenvalues are
\(1/2\pm b+O_N(\varepsilon^2)\), and the entropy expansion gives

\[
S(\rho_i)=\ln2-2b^2+O_N(\varepsilon^4)
=\ln2-\frac{\varepsilon^2}{2(N-1)^2}
+O_N(\varepsilon^4).
\]

The absence of an odd power in the entropy follows from the evenness of the binary entropy around eigenvalue \(1/2\), together with the parity relation mapping \(\varepsilon\) to \(-\varepsilon\) by a unitary transformation. A fully coefficient-level proof should keep the normalized state and the reduced-state eigenvalues to the order required; the displayed expression is the leading contribution only.

## 3. Two-site reduced state: exact symmetry structure and leading orders

For sites \(1,2\), define

\[
\rho_{12}=\operatorname{Tr}_{3,\ldots,N}
|\Psi(\varepsilon)\rangle\langle\Psi(\varepsilon)|.
\]

Global bit-flip parity implies that \(\rho_{12}\) commutes with
\(\sigma_1^x\sigma_2^x\). At the uniform point it also commutes with the swap \(1\leftrightarrow2\). Consequently it decomposes into parity/swap-adapted invariant subspaces. This symmetry statement is exact.

The GHZ limit is

\[
\rho_{12}(0)=\frac12|00\rangle\langle00|
+\frac12|11\rangle\langle11|,
\]

whose nonzero eigenvalues are \(1/2,1/2\), so \(S(\rho_{12}(0))=\ln2\).

The first-order state correction produces \(O(\varepsilon)\) coherences between the large-support subspace and one-excitation pair states. In each relevant \(2\times2\) block, write

\[
M(\varepsilon)=
\begin{pmatrix}
L(\varepsilon)&X(\varepsilon)\\
\overline{X(\varepsilon)}&S(\varepsilon)
\end{pmatrix},
\quad
L(0)=\tfrac12,\quad
X=O_N(\varepsilon),\quad S=O_N(\varepsilon^2).
\]

The small eigenvalue is controlled by the Schur complement

\[
Q=S-\frac{|X|^2}{L}.
\]

The cancellation of the coefficient of \(\varepsilon^2\) in \(Q\) is a coefficient identity that must be checked using the complete second-order reduced-state expansion, not merely the order estimates \(X=O(\varepsilon)\), \(S=O(\varepsilon^2)\). If the coefficient vanishes, analyticity of the matrix entries implies \(Q=O_N(\varepsilon^4)\) for the value of the parameter. It does not, by itself, imply a corresponding edge-derivative bound.

A candidate fourth-order coefficient recorded in upstream proof materials is \(1/[8(N-2)(N-1)^4]\). It is not valid unchanged for the full range \(N\ge4\): the independent exact-rational diagnostic gives \(1/648\) at \(N=4\), twice the candidate value, while it matches at \(N=5,6,7,8\). The coefficient formula is now derived for fixed \(N\ge9\) and checked by exact-rational finite calculations for \(N=5,6,7,8\); it is not valid at \(N=4\). Every coefficient must be recomputed from one normalized state expansion through the necessary order, with every parity block and branch accounted for.

### 3.1 Exact-rational finite-\(N\) diagnostic and a coefficient discrepancy

An independent exact-rational perturbation recurrence was run in the full even-parity complement-orbit basis for \(N=4,5,6,7,8\). It reconstructs the normalized state, traces out all but two sites, and expands the small eigenvalue of the symmetric parity block. The resulting coefficients are:

\[
\begin{array}{c|c|c}
N & [\varepsilon^4]\lambda_{\rm small} &
1/[8(N-2)(N-1)^4]\\
\hline
4 & 1/648 & 1/1296\\
5 & 1/6144 & 1/6144\\
6 & 1/20000 & 1/20000\\
7 & 1/51840 & 1/51840\\
8 & 1/115248 & 1/115248
\end{array}
\]

The \(N=4\) result differs by a factor of two. It was additionally checked against direct high-precision diagonalization of the full \(2^4\)-dimensional Hamiltonian at \(\varepsilon=0.01\) and \(0.005\). The ratio \(\lambda_{\rm small}/\varepsilon^4\) approaches \(1/648\).

A separate symbolic recurrence derivation now establishes the displayed coefficient for every fixed \(N\ge9\), and the exact-rational finite calculations establish it for \(N=5,6,7,8\). The exceptional \(N=4\) coefficient is twice the candidate value. The detailed derivation is recorded in audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md. The reproducible finite-N script and diagnostic report are stored at:

- working/paper-a/finite_n_strong_coupling_exact_diagnostic.py
- audits/paper-a/FINITE_N_STRONG_COUPLING_EIGENVALUE_DIAGNOSTIC.md

The discrepancy affects a fourth-order eigenvalue coefficient. It does not, by itself, alter the leading \(O(\varepsilon^2)\) one-site entropy term or prove/disprove the leading \(x^{-2}\) coefficient of \(\mathcal G_N\). It also does not provide any edge-coupling derivative bound.

## 4. Mutual-information leading coefficient

Combining the one-site entropy contribution with the GHZ-limit two-site entropy gives the candidate leading term

\[
\begin{aligned}
I_{12}
&=S(\rho_1)+S(\rho_2)-S(\rho_{12})\\
&=\ln2-\frac{\varepsilon^2}{(N-1)^2}
+\text{terms of order at least }\varepsilon^4
\text{, possibly with }\varepsilon^4\ln\varepsilon.
\end{aligned}
\]

Thus the coefficient of \(\varepsilon^2\) is fixed by the one-site terms provided the two-site entropy has no order-\(\varepsilon^2\) correction. That latter fact must be verified from the complete two-site block expansion. If the small eigenvalues are \(O(\varepsilon^4)\) and the two large eigenvalues are \(1/2+O(\varepsilon^2)\) with opposite shifts, then the two-site entropy correction is at most \(O_N(\varepsilon^4|\ln\varepsilon|)\). The needed eigenvalue estimates remain a model-specific proof obligation.

Subject to that obligation, the function asymptotic is

\[
\mathcal G_N(x)
=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right).
\]

This function expansion alone gives \(\mathcal G_N(x)\to\ln2\), but does not justify differentiating its remainder.

## 5. Why the derivative expansion is a separate theorem

The implication

\[
R(x)=O(\ln x/x^4)
\quad\Longrightarrow\quad
R'(x)=O(\ln x/x^5)
\]

is false without additional derivative hypotheses. For example, for \(x>1\),

\[
R(x)=x^{-4}\ln x\,\sin(x^6)
\]

has the stated function bound, while its derivative contains the term
\(6x\ln x\cos(x^6)\), which is not \(O(\ln x/x^5)\).

A valid route is to prove a parameter-dependent expansion in
\(\varepsilon=1/x\) with differentiated remainder estimates, e.g.

\[
I_{12}(\varepsilon)
=\ln2-c_N\varepsilon^2
+\varepsilon^4\bigl(a_N\ln\varepsilon+b_N\bigr)
+\mathcal R_N(\varepsilon),
\]

together with

\[
\mathcal R_N'(\varepsilon)
=O_N(\varepsilon^5|\ln\varepsilon|)
\]

(or a stronger explicit bound). Then the chain rule
\(d/dx=-\varepsilon^2d/d\varepsilon\) gives

\[
\mathcal G_N'(x)
=2c_Nx^{-3}
+O_N(\ln x/x^5),
\qquad c_N=(N-1)^{-2}.
\]

This differentiated expansion must be established from the finite-dimensional analytic perturbation problem and the entropy eigenvalue branches. It is not a consequence of Kato analyticity alone because \(-\lambda\ln\lambda\) is not analytic at \(\lambda=0\).

## 6. General-coupling edge derivatives and the \(B-C\) coefficient

Let \(J_{ij}\) vary independently near the uniform point. The first-order amplitude for a one-spin flip at site \(i\) is

\[
b_i=\frac{h}{2\sum_{k\ne i}J_{ik}}
+O_N((h/J)^3)
\]

at the uniform scale, with the higher-order term understood only after a uniform local expansion in the edge variables is proved. At the uniform point, \(b_i=h/[2J(N-1)]\).

For the leading one-site entropy,
\(S(\rho_1)=\ln2-2b_1^2+\cdots\), the shared edge \(J_{13}\) changes the excitation denominator of site \(1\), while the disjoint edge \(J_{34}\) does not change the first-order denominators of sites \(1,2\). Therefore

\[
\partial_{J_{13}}b_1
=-\frac{2h}{[2J(N-1)]^2}
=-\frac{h}{2J^2(N-1)^2},
\qquad
\partial_{J_{34}}b_1=0
\]

at the leading order. Hence

\[
\partial_{J_{13}}\{-2b_1^2\}
=\frac{h^2}{J^3(N-1)^3}
\]

and the corresponding leading contribution to \(C\) is zero. The same conclusion holds for the site-2 marginal contribution.

This establishes the formal leading single-site contribution

\[
(B-C)_{\mathrm{one-site,lead}}
=\frac{h^2}{J^3(N-1)^3}.
\]

It does **not** establish the full \(B-C\) asymptotic. The two-site entropy contribution and its edge derivatives must be bounded at smaller order.

## 7. Required model-specific entropy/Schur estimates

For each small block, a sufficient value estimate would be

\[
Q(\varepsilon,\mathbf J)=O_N(\varepsilon^4).
\]

For response derivatives one additionally needs, in a neighborhood of the uniform point,

\[
\partial_{J_e}Q
=O_N(\varepsilon^4/J),
\]

with constants uniform over the chosen edge neighborhood and for each relevant edge direction. Neither estimate follows merely from analyticity of the ground-state projector. The first requires a coefficient cancellation in the reduced-state Schur complement; the second requires differentiating that cancellation in the general-coupling family.

For a small eigenvalue \(\lambda\), the entropy derivative is

\[
\partial_{J_e}[-\lambda\ln\lambda]
=-(1+\ln\lambda)\partial_{J_e}\lambda.
\]

An upper bound \(\lambda\le C\varepsilon^4\) does not control \(|\ln\lambda|\) from above when \(\lambda\) may be much smaller. One needs, branch by branch, either a two-sided comparability
\(c\varepsilon^4\le\lambda\le C\varepsilon^4\), or a relative derivative estimate such as
\(|\partial_{J_e}\lambda|\le C\lambda/J\), together with a separate treatment of branches that vanish identically or change rank. The Schur complement and eigenvalue comparison must be uniform in the edge perturbation.

## 8. Closure obligations (not yet discharged)

1. Compute the normalized even-sector ground-state vector to sufficient order (at least through the order needed for all \(O(\varepsilon^4)\) reduced-state coefficients), including two-flip and higher-weight amplitudes.
2. Derive the full \(4\times4\) \(\rho_{12}\) for general edge couplings near the uniform point, or derive an equivalent symmetry-adapted block representation.
3. Verify all parity blocks and show exactly which \(\varepsilon^2\) Schur coefficients cancel.
4. Recompute every \(\varepsilon^4\) small-eigenvalue coefficient; do not reuse an unverified coefficient from an earlier proof file.
5. Prove the general-edge derivatives of the Schur complements and small eigenvalue branches, including lower/relative bounds needed for logarithms.
6. Derive the entropy expansion with differentiated remainders, treating rank-changing/zero branches explicitly.
7. Combine both one-site and two-site entropy derivatives to obtain the full \(B-C\) expansion.
8. Independently derive the \(x\)-derivative expansion for \(\mathcal G_N\); do not differentiate a bare big-O statement.
9. Validate the formulas numerically for small finite \(N\) as a diagnostic only; numerical agreement is not a proof.
10. Only after the analytic statement is stable, translate the theorem into Lean and audit proof-to-manuscript correspondence.

## 9. Current defensible conclusions

- The fixed-\(N\) parity-sector gap at the unperturbed point is \(2J(N-1)\).
- The leading one-spin-flip amplitude is \(h/[2J(N-1)]\).
- The leading one-site entropy correction is \(-h^2/[2J^2(N-1)^2]\).
- The formal leading one-site contribution to \(B-C\) is \(h^2/[J^3(N-1)^3]\).
- The claimed \(\mathcal G_N\) coefficient at order \(x^{-2}\) is consistent with this leading marginal contribution, conditional on the two-site entropy having no order-\(x^{-2}\) term.
- The full function remainder, derivative remainder, and full \(B-C\) differentiated remainder have not been proved here.
- No claim status is upgraded. No upstream file is changed.

**Verdict: PARTIAL DERIVATION. The central obstruction has been localized to the complete two-site reduced-state expansion and its mixed edge-derivative entropy control.**
