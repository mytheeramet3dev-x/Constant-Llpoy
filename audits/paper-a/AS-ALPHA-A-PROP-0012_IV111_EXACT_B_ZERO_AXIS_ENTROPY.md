# IV-111 — Exact boundary analysis on B=0

**Scope:** Axis case \(B=0, A\ne0\). This is derived directly from the decoupled Hamiltonian, not by taking a limit of the generic two-coupling entropy expansion.

When \(J_{23}=0\), spin 3 decouples and its Hamiltonian is \(-hX_3\). For \(h>0\), its ground state is the \(X_3=+1\) eigenstate, hence \(q_3=0\) exactly and \(h(q_3)=0\).

The coupled pair (1,2) in the even X-parity basis \((|++\rangle,|--\rangle)\) has matrix
\[
\begin{pmatrix}-2h&-J_{12}\\-J_{12}&2h\end{pmatrix}.
\]
Its ground-state energy is \(-\sqrt{4h^2+J_{12}^2}\). The exact probability of the \(|--\rangle\) component, equivalently either pair spin's \(X=-1\) probability, is
\[
q=q_1=q_2=\frac12\left(1-\frac{2h}{\sqrt{4h^2+J_{12}^2}}\right).
\]
With \(a=J_{12}/(4h)=\varepsilon A\), this becomes
\[
q=\frac12\left(1-\frac1{\sqrt{1+4a^2}}\right)
=a^2-3a^4+10a^6+O(a^8).
\]
The expansion through fourth order is therefore \(q=\varepsilon^2A^2-3\varepsilon^4A^4+O(\varepsilon^6)\), while \(q_3=0\) identically.

For \(L=\ln(\varepsilon^2A^2)\), the entropy expansion is
\[
h(q)=\varepsilon^2A^2(1-L)+\varepsilon^4A^4(3L+\tfrac12)+O(\varepsilon^6|\ln\varepsilon|).
\]
Because the exact pure-state identity gives \(I_{12}-I_{13}=2[h(q)-h(q_3)]\), the axis result is
\[
I_{12}-I_{13}=2\varepsilon^2A^2(1-L)+2\varepsilon^4A^4(3L+\tfrac12)+O(\varepsilon^6|\ln\varepsilon|).
\]
Here \(q_3=0\) and \(h(q_3)=0\) exactly. This audit covers only the axis \(B=0,A\ne0\); it does not settle the other axis or the full proposition, and it is not a Lean verification.
