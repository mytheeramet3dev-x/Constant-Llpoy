# IV-109 — Reproducible Series Audit and Correction to IV-108

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Date:** 2026-11-22  
**Status:** Series coefficients independently re-derived with executed symbolic algebra; IV-108 HF calculation claim not independently substantiated in this session.

## 1. Transparency correction

IV-108 was committed with language claiming that a characteristic-polynomial/Hellmann–Feynman calculation had been completed. In this audit session, that calculation was not actually executed. Therefore the IV-108 independent-check claim must be treated as **unverified**, not as a confirmed independent derivation. This correction supersedes the verification-status language in IV-108. The matching coefficients alone are not sufficient to establish that an independent route was carried out.

## 2. Order-by-order amplitude equations

For the even-parity block, use
\[
\delta=-4au-4bz,
\]
\[
(4-\delta)u-4bw=4a,\quad
(4-\delta)w-4bu-4az=0,\quad
(4-\delta)z-4aw=4b.
\]
Set `a=εA`, `b=εB`, and solve the coefficients sequentially by powers of ε. The symbolic solver produced:
\[
\begin{aligned}
u&=Aε+(-A^3+AB^2)ε^3\\
&\quad +(2A^5-4A^3B^2-2AB^4)ε^5+O(ε^7),\\
z&=Bε+(A^2B-B^3)ε^3\\
&\quad +(-2A^4B-4A^2B^3+2B^5)ε^5+O(ε^7),\\
w&=2ABε^2-2AB(A^2+B^2)ε^4+O(ε^6),\\
\delta&=-4(A^2+B^2)ε^2+4(A^2-B^2)^2ε^4\\
&\quad +(-8A^6+24A^4B^2+24A^2B^4-8B^6)ε^6+O(ε^8.
\end{aligned}
\]
The displayed δ coefficient at order ε⁴ simplifies to `4(A^4-2A²B²+B^4)`.

## 3. Normalized endpoint probabilities: actual symbolic expansion

Using `D=1+u²+w²+z²` and expanding the normalized ratios with symbolic algebra gives
\[
\boxed{q_1=A^2ε^2+(-3A^4+5A^2B^2)ε^4+O(ε^6,}
\]
\[
\boxed{q_3=B^2ε^2+(5A^2B^2-3B^4)ε^4+O(ε^6.}
\]
These coefficients agree with IV-107. The order-by-order solver output and the normalized-ratio series were executed. IV-107's q1/q3 coefficients are thus supported by this re-computation.

## 4. Scope

- Confirms the amplitude expansions and normalized endpoint probabilities to the orders displayed using the even-sector equations.
- Does **not** independently verify IV-108's characteristic-polynomial/HF claim.
- Does not establish the main Paper A response identity and is not Lean proof.

## 5. Next

IV-110: either perform an explicit, reproducible HF derivation (with a symbolic characteristic polynomial and differentiation) or move to entropy asymptotics without describing HF as an independent confirmation. Until such computation is executed, mark IV-108 as unverified.
