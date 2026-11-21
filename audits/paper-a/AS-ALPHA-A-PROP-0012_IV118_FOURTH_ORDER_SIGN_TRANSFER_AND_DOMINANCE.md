# IV-118 — Fourth-order sign transfer and leading-order dominance

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** analytic asymptotic comparison conditional on IV-107 probability coefficients and IV-110 entropy expansion.

## Entropy-difference expansion

Let \(X=A^2>0\), \(r=B^2/A^2>0\), and \(L=\ln(\varepsilon^2X)\). From IV-110:
\[
\Delta h=\varepsilon^2X C_2(r,L)+\varepsilon^4X^2 C_4(r,L)+O(\varepsilon^6|\ln\varepsilon|),
\]
where
\[
C_2(r,L)=1-L-(1+r)\ln(1+r)+r\ln r.
\]
The fourth-order coefficient decomposes as
\[
C_4(r,L)=-3(1+r)(1-L)+\Phi(r),
\]
with \(\Phi\) as analyzed in IV-115–117.

## Fixed-r asymptotic dominance

For any fixed \(X>0\) and fixed \(r>0\), as \(\varepsilon\to0^+\), \(L=\ln(\varepsilon^2X)\to-\infty\). Thus
\[
C_2(r,L)= -L + \underbrace{1-(1+r)\ln(1+r)+r\ln r}_{\text{finite for fixed }r},
\]
so \(C_2\to+\infty\). The fourth-order coefficient grows at most linearly in \(|L|\) for fixed r; therefore its contribution relative to the second-order term is of order \(\varepsilon^2\) (up to fixed constants), and vanishes as \(\varepsilon\to0^+\).

Consequently, conditionally on the cited expansion being correct, for each fixed \(X>0,r>0\), the leading asymptotic entropy difference is positive:
\[
\Delta h>0\quad\text{for all sufficiently small }\varepsilon>0.
\]
This is a pointwise-in-r asymptotic conclusion, not uniform over r or X.

## Why IV-117's Phi sign does not transfer to Delta h

The fourth-order coefficient \(C_4\) includes the scale-logarithmic term \(-3(1+r)(1-L)\), in addition to \(\Phi(r)\). Even a sign-certified negative interval for \(\Phi\) does not determine the sign of \(C_4\), much less of the full \(\Delta h\), because:
1. the second-order term dominates for fixed parameters in the weak-coupling limit;
2. \(C_4\) is not equal to \(\Phi\);
3. the omitted remainder needs control for any finite-\(\varepsilon\) sign claim.

## Limits

- The dominance result assumes the IV-107 probability expansions and IV-110 entropy expansion/remainder are valid.
- It is pointwise for fixed \(X,r\), not uniform near ratio axes, \(r\to0,\infty\), or varying X.
- It does not settle Proposition 0012, whose exact target identity still needs the manuscript definitions and full proof.
- No Lean proof is claimed.

Paper A target remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
