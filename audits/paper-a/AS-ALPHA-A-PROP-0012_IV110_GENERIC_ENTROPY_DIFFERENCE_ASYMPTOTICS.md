# IV-110 — Entropy-difference asymptotics for the generic nonzero-coupling sector

**Scope:** This audit uses symbolic series computed from the even-parity eigenvector expansions through the displayed orders. It is not a proof of the target proposition.

Let \(a=\varepsilon A\), \(b=\varepsilon B\), and suppose \(A\ne0\), \(B\ne0\). Define
\[
S=A^2+B^2,\quad T=-3A^4+2A^2B^2-3B^4,
\]
\[
S_3=B^2,\quad T_3=5A^2B^2-3B^4.
\]
Symbolic expansion (SymPy) of the normalized probabilities gives
\[
q=\varepsilon^2S+\varepsilon^4T+O(\varepsilon^6),
\quad q_3=\varepsilon^2S_3+\varepsilon^4T_3+O(\varepsilon^6).
\]
Here q is the middle-spin probability and q3 is endpoint 3's probability.

For \(s>0\) and \(q=\varepsilon^2s+\varepsilon^4t+O(\varepsilon^6)\), binary entropy obeys
\[
h(q)=\varepsilon^2s(1-\ln(\varepsilon^2s))
+\varepsilon^4\left[t(1-\ln(\varepsilon^2s))+\frac{s^2}{2}\right]
+O(\varepsilon^6|\ln\varepsilon|).
\]
Thus, with \(\Delta h=h(q)-h(q_3)\),
\[
\Delta h=\varepsilon^2\{S(1-\ln(\varepsilon^2S))-B^2(1-\ln(\varepsilon^2B^2))\}
\]
\[
+\varepsilon^4\left\{T(1-\ln(\varepsilon^2S))+\frac{S^2}{2}
-T_3(1-\ln(\varepsilon^2B^2))-\frac{B^4}{2}\right\}
+O(\varepsilon^6|\ln\varepsilon|).
\]
The mutual-information identity previously derived gives \(I_{12}-I_{13}=2\Delta h\), so this is the corresponding asymptotic expression for that difference on the generic sector.

**Boundary cases:** This expansion requires positive leading coefficients. It does not cover \(B=0\) (where q3 has no \(\varepsilon^2\) term), \(A=0\), or the origin. These must be audited separately with the appropriate leading order and logarithm. No extrapolation to those axes is made here.

**Verification limits:** The displayed probability coefficients were reproduced by symbolic series expansion in the current computation. This does not verify the full target identity, the previously claimed HF independent derivation, or any Lean proof. No repository commit is included in this file unless the GitHub create/fetchback operations succeed.
