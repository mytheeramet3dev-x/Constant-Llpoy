# IV-230 — Remainder Scaling and Symmetry-Adapted Physical Block Lifting Criterion

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, lifting IV-228 coefficient to a physical odd block  
**Status:** SCALING OBSTRUCTION AND SUFFICIENT CRITERION DERIVED / MODEL-SPECIFIC BOUNDS OPEN / NOT LEAN-FORMALIZED  
**Scope:** Quantify the nonuniformity problem in a generic \(O(r^3)\) remainder and derive symmetry-adapted sufficient estimates that could close the physical-block positivity gap. This is a model-independent matrix analysis, not a TFIM proof.

## 1. Leading coefficient and generic error

From IV-228, write
\[
c_N=\frac{N-3}{32(N-2)}>0,\qquad N\ge4.
\]
For fixed small \(u\),
\[
r^2\lambda_{\min}(M_2(u))=c_Nr^2u^2+O(r^2u^3).
\]
Suppose only a generic bound \(\|E(r,u)\|\le Cr^3\) is known. Weyl's inequality gives a lower bound of the form
\[
\lambda_{\min}(O(r,u))\ge c_Nr^2u^2-Cr^3
\]
after absorbing the \(u\)-expansion remainder into the local coefficient (restrict \(u\) to a sufficiently small fixed neighborhood).

This bound certifies positivity only in a region where
\[
u^2>\frac C{c_N}r.
\]
Thus a generic \(O(r^3)\) error does not establish positivity uniformly over perturbations that approach the symmetric point faster than order \(\sqrt r\).

## 2. Explicit matrix counterexample to automatic lifting

Consider the model family
\[
O_-(r,u)=
\begin{pmatrix}
r^2L_0&0\\
0&c_Nr^2u^2-\gamma r^3
\end{pmatrix},
\quad L_0>0,\ \gamma>0.
\]
The leading Gram contribution is positive semidefinite, and the correction has norm \(\gamma r^3\), but the smallest eigenvalue is negative whenever
\[
u^2<\frac{\gamma}{c_N}r.
\]
This is a matrix-level counterexample showing that positivity of the leading coefficient plus an unconstrained \(O(r^3)\) error cannot logically imply physical-block positivity. It is not asserted to arise from the TFIM amplitudes.

## 3. Symmetry-adapted sufficient condition

Let the null/antisymmetric direction be represented by \(v\), and let \(P_v\) be its orthogonal projection. A sufficient form of a symmetry-compatible error estimate is
\[
v^TE(r,u)v\ge -K r^3u^2,\qquad
\|E(r,u)\|\le Kr^3
\]
in a neighborhood where the exact symmetry forces \(v^TO(r,0)v=0\) and the mixed common/null coupling vanishes at \(u=0\). If the leading physical null-direction coefficient is \(c_Nr^2u^2\), the first inequality yields
\[
v^TO(r,u)v\ge (c_N-Kr)r^2u^2
\]
(up to the separately controlled leading expansion remainder). This is positive for \(0<r<c_N/K\) when \(u\ne0\). However, controlling the diagonal null entry alone does not always suffice for the full 2x2 matrix; the mixed term must also be bounded so that its Schur-complement contribution is included.

A stronger direct sufficient criterion is: for \(L(r,u)>0\),
\[
s(r,u)-\frac{t(r,u)^2}{L(r,u)}
\ge c_Nr^2u^2-Kr^3u^2-K_t r^4u^2,
\]
with verified constants \(K,K_t\) and local domain. This implies strict positivity for nonzero \(u\) and sufficiently small \(r\), provided \(c_N-Kr-K_tr^2>0\).

These inequalities are proof targets. IV-230 does not establish that the TFIM satisfies them.

## 4. Scaling conclusion

- Leading positive scale: \(r^2u^2\).
- Generic remainder scale: \(r^3\); competing region: \(u^2\lesssim r\), i.e. \(|u|\lesssim\sqrt r\).
- Symmetry-adapted remainder carrying the same \(u^2\) factor can avoid this nonuniform obstruction, if rigorously derived and if the mixed term is also controlled.
- Fixed nonzero \(u\) and uniform-in-\(u\) positivity are distinct statements; do not conflate them.

## 5. Disposition

- Generic remainder scaling obstruction: **DERIVED**.
- Explicit abstract counterexample to automatic positivity lifting: **DERIVED**.
- Symmetry-adapted sufficient Schur estimate: **DERIVED AS A CRITERION**.
- TFIM amplitude estimates satisfying the criterion: **OPEN**.
- Global \(B-C>0\), physical reduced odd-block positivity, manuscript mapping, and Lean formalization: **OPEN**.

Next audit: compute the normalized TFIM reduced block entries from a reproducible perturbative state/amplitude construction, or identify a rigorous simplification that gives the required symmetry-adapted remainder estimates.
