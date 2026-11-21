# IV-112 — Exact boundary analysis on A=0

**Scope:** Axis case \(A=0, B\ne0\), derived directly from decoupling and exact two-spin solution.

When \(J_{12}=0\), spin 1 decouples with Hamiltonian \(-hX_1\), so its \(X=-1\) probability is \(q_1=0\) exactly. The remaining pair (2,3) has the same two-dimensional matrix as the coupled pair in the opposite-axis audit, with \(J_{23}\) in place of \(J_{12}\).

Define \(b=J_{23}/(4h)=\varepsilon B\). The pair ground-state energy is \(-\sqrt{4h^2+J_{23}^2}\), and the exact probability for either spin in the pair to have \(X=-1\) is
\[
q_2=q_3=\frac12\left(1-\frac1{\sqrt{1+4b^2}}\right)
=b^2-3b^4+10b^6+O(b^8).
\]
Thus \(q_1=0\) exactly and \(q_2=q_3=q\).

For the pure three-spin ground state, the entropy identities imply \(I_{12}=S_1+S_2-S_3=0\), and \(I_{13}=S_1+S_3-S_2=2h(q)\). Therefore \(I_{12}-I_{13}=-2h(q)\).

Writing \(L_B=\ln(\varepsilon^2B^2)\),
\[
h(q)=\varepsilon^2B^2(1-L_B)+\varepsilon^4B^4(3L_B+1/2)+O(\varepsilon^6|\ln\varepsilon|).
\]
Consequently,
\[
I_{12}-I_{13}=-2\varepsilon^2B^2(1-L_B)-2\varepsilon^4B^4(3L_B+1/2)+O(\varepsilon^6|\ln\varepsilon|).
\]
This axis result is exact at the decoupling level and asymptotic at the entropy-expansion level. It does not prove the full proposition or a Lean theorem.
