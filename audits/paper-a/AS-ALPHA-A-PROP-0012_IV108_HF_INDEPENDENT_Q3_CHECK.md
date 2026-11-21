# IV-108 — Independent Hellmann–Feynman Check of q3

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Symbolic calculation completed; no Lean proof  
**Date:** 2026-11-22

## 1. Auxiliary-field construction

Add `-k X_3` to the Hamiltonian. In the even-parity X-basis `(000,110,101,011)`, the dimensionless block (with `a=εA`, `b=εB`) is
\[
M(k)=\begin{pmatrix}
-3-k&-4εA&0&-4εB\\
-4εA&1-k&-4εB&0\\
0&-4εB&1+k&-4εA\\
-4εB&0&-4εA&1+k
\end{pmatrix}.
\]
At `k=0`, the ground energy branch is `E(0)`. Hellmann–Feynman gives
\[
E'(k)=-\langle X_3\rangle_k,\qquad
q_3=\frac{1+E'(0)}2.
\]

## 2. Characteristic-polynomial perturbation

Using the characteristic polynomial `det(M(k)-λI)`, and expanding the ground branch around its unperturbed energy `-3-k`,
\[
E(k)=-3-k+ε^2d_2(k)+ε^4d_4(k)+O(ε^6),
\]
then differentiating at `k=0` and applying HF yields
\[
\boxed{q_3=B^2ε^2+(5A^2B^2-3B^4)ε^4+O(ε^6.}
\]
This matches IV-107's amplitude-derived q3 through fourth order, coefficient-by-coefficient.

## 3. Independent confirmation scope

This checks the endpoint-3 probability expansion via a distinct route (characteristic polynomial plus Hellmann–Feynman), independent of directly normalizing the eigenvector amplitudes. It supports the q3 expansion through `ε^4`, but is not a proof of the global target identity `χ_1-χ_2=(N-2)(B-C)`, nor a Lean verification.

## 4. Next

IV-109: derive q1 by adding `-kX_1`, swapping endpoint roles, and compare the HF expansion to IV-107's q1. Then audit the entropy-difference expansion with special cases `A=0`, `B=0`, and both nonzero kept separate.
