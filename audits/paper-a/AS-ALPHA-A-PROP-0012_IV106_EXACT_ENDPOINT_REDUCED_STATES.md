# IV-106 — Exact Endpoint Reduced States in the X Basis

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Exact reduced-state formulas; no target identity established  
**Date:** 2026-11-22

## 1. State and normalization

On the even-parity ground branch, use
\[
|\psi\rangle=\frac{|000\rangle+u|110\rangle+w|101\rangle+z|011\rangle}{\sqrt{D}},
\qquad D=1+u^2+w^2+z^2,
\]
with real amplitudes for this real Hamiltonian. The formulas also hold with squared moduli and complex conjugates for a complex state of this support.

## 2. Endpoint 1 reduced density matrix

Tracing spins 2 and 3, the rest-register labels associated with the two X-basis values of spin 1 are disjoint:
- spin 1 bit 0: rest labels `00` and `11`, amplitudes `1,z`;
- spin 1 bit 1: rest labels `10` and `01`, amplitudes `u,w`.

Therefore the off-diagonal matrix element vanishes exactly in the X basis:
\[
\rho_1^{(X)}=\frac1D
\begin{pmatrix}
1+z^2&0\\
0&u^2+w^2
\end{pmatrix}.
\]
Define
\[
q_1=\frac{u^2+w^2}{D}.
\]
Then `S_1=h(q_1)` exactly.

## 3. Endpoint 3 reduced density matrix

Similarly, tracing spins 1 and 2 gives disjoint rest-register labels for the two values of spin 3:
- spin 3 bit 0: rest labels `00` and `11`, amplitudes `1,u`;
- spin 3 bit 1: rest labels `01` and `10`, amplitudes `z,w`.

Thus
\[
\rho_3^{(X)}=\frac1D
\begin{pmatrix}
1+u^2&0\\
0&z^2+w^2
\end{pmatrix},
\]
and defining
\[
q_3=\frac{z^2+w^2}{D},
\]
we have `S_3=h(q_3)` exactly.

## 4. Exact mutual-information reduction

Using IV-105 and the exact entropy expressions,
\[
\boxed{I_{12}=h(q_1)+h(q)-h(q_3),}
\]
\[
\boxed{I_{13}=h(q_1)+h(q_3)-h(q).}
\]
Their difference is
\[
\boxed{I_{12}-I_{13}=2[h(q)-h(q_3)].}
\]
This is an exact reduction for the real even-parity state on the branch considered. It does not require endpoint-exchange symmetry and does not imply `q_1=q_3`.

## 5. Limits

- The reduced-state diagonality follows from the parity-supported four-component state and the orthogonality of the traced-out X-basis labels.
- The probability definitions above are exact with normalization D.
- No expansion of q1 or q3 is included here; those are deferred to a separately checked perturbation audit.
- The Paper A response identity remains open; response derivatives still must be matched to the original definitions.

## 6. Next

IV-107: derive perturbative expansions of q1 and q3 from the amplitude series, then independently compare q3 against the characteristic-polynomial/Hellmann–Feynman derivative with an auxiliary field on spin 3.
