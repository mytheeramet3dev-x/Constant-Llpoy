# IV-113 — Generic entropy logarithm cancellation and ratio structure

**Scope:** Algebraic structural reduction of the generic-sector entropy difference from IV-110, assuming \(A\ne0\), \(B\ne0\), and \(\varepsilon>0\). This is not a proof of Proposition 0012.

Let \(S=A^2+B^2\), \(R=B^2\), \(T=-3A^4+2A^2B^2-3B^4\), and \(T_3=5A^2B^2-3B^4\). At order two,
\[
\Delta h^{(2)}=\varepsilon^2\{S(1-\ln(\varepsilon^2S))-R(1-\ln(\varepsilon^2R))\}.
\]
Separating the scale logarithm gives
\[
\Delta h^{(2)}=\varepsilon^2\{A^2(1-\ln\varepsilon^2)-S\ln S+B^2\ln B^2\}.
\]
For \(r=B^2/A^2>0\), this is equivalently
\[
\varepsilon^2A^2\{1-\ln(\varepsilon^2A^2)-(1+r)\ln(1+r)+r\ln r\}.
\]
The scale term has coefficient \(A^2\) only; the residual is a function of the squared coupling ratio.

At fourth order, the coefficient of \(\ln\varepsilon^2\) in \(\Delta h\) is \(-(T-T_3)\), since the entropy terms contribute \(-T\ln(\varepsilon^2)\) and \(+T_3\ln(\varepsilon^2)\). Direct algebra yields
\[
T-T_3=-3A^2(A^2+B^2),
\]
so the coefficient is \(+3A^2(A^2+B^2)\). The \(B^4\) terms cancel from this scale-log coefficient.

These are algebraic reductions of the asymptotic expression, not new probability coefficients. The remainder and validity sector are inherited from IV-110; boundary axes remain excluded.
