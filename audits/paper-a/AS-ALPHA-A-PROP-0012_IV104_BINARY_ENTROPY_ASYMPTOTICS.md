# IV-104 — Binary Entropy Expansion from the Cross-Checked Middle-Spin Probability

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Local asymptotic entropy expansion; not Lean-verified  
**Date:** 2026-11-22

## 1. Input

IV-102 and IV-103 independently obtain
\[
q=ε^2S+ε^4T+O(ε^6),
\]
where
\[
S=A^2+B^2,\qquad T=-3A^4+2A^2B^2-3B^4,
\]
under `a=εA`, `b=εB`. This audit expands the binary entropy of q, not a mutual information identity.

## 2. Binary entropy and nonanalyticity

Use natural-log entropy
\[
h(q)=-q\ln q-(1-q)\ln(1-q).
\]
As `q→0+`,
\[
-(1-q)\ln(1-q)=q-\frac{q^2}{2}+O(q^3),
\]
so
\[
h(q)=q(1-\ln q)+\frac{q^2}{2}+O(q^3).
\]
The logarithm means entropy is not analytic as a polynomial in ε at ε=0. Any remainder stated merely as a regular `O(ε^6)` polynomial-scale term must account for logarithms.

## 3. Substitution of the q expansion

For `S>0`, substitute `q=ε^2S+ε^4T+O(ε^6)`:
\[
\ln q=\ln(ε^2S)+ε^2\frac{T}{S}+O(ε^4)
\]
and therefore
\[
\boxed{
\begin{aligned}
h(q)={}&ε^2S\bigl(1-\ln(ε^2S)\bigr)\\
&+ε^4\left[T\bigl(1-\ln(ε^2S)\bigr)+\frac{S^2}{2}\right]\\
&+O(ε^6|\ln ε|),
\end{aligned}}
\]
for fixed `A,B` with `S>0`. The error scale is stated logarithmically; constants may depend on fixed A,B. At `S=0` (A=B=0), q=0 and h(q)=0 exactly, so the formula with `ln S` is not used.

## 4. Explicit coefficients

The fourth-order entropy correction contains
\[
T=-3A^4+2A^2B^2-3B^4
\]
and the normalization/entropy contribution `S²/2`. Their sum in the nonlogarithmic fourth-order component is
\[
T+\frac{S^2}{2}
=-\frac52(A^4+B^4)+3A^2B^2.
\]
But the full fourth-order term also includes `-T ln(ε²S)`; it must not be discarded.

## 5. What is and is not established

- This expansion is a local asymptotic consequence of the cross-checked q expansion and standard binary entropy expansion.
- It does not establish any mutual-information expansion by itself.
- No response identity, cancellation, or target proposition is assumed.
- It is not Lean formalized.

Next audit IV-105: derive the endpoint/middle reduced-state entropy and MI relationships from exact symmetry and pure-state structure, then identify precisely which q-dependent entropy terms can legitimately cancel and which assumptions are still missing.
