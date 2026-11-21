# IV-107 — Perturbative Endpoint Probabilities q1 and q3

**Project:** Absolute Symmetry, Paper A  
**Proposition:** `AS-ALPHA-A-PROP-0012`  
**Status:** Local amplitude-derived expansions; q3 independent HF check pending  
**Date:** 2026-11-22

## 1. Exact quantities

With the normalized even-sector state amplitudes `(1,u,w,z)` and `D=1+u²+w²+z²`, IV-106 defines
\[
q_1=\frac{u^2+w^2}{D},\qquad q_3=\frac{z^2+w^2}{D}.
\]
These are the probabilities that endpoint spins 1 and 3 are in the X=-1 sector.

## 2. Amplitudes through cubic order

For `a=εA`, `b=εB`, the even-block eigenvector equations yield
\[
\begin{aligned}
u&=εA+ε^3(-A^3+AB^2)+O(ε^5),\\
z&=εB+ε^3(A^2B-B^3)+O(ε^5),\\
w&=2ε^2AB+O(ε^4).
\end{aligned}
\]
The normalization is
\[
D=1+ε^2(A^2+B^2)+O(ε^4).
\]

## 3. Endpoint probability expansions

Expanding the exact ratios, not the numerator alone, gives
\[
\boxed{
q_1=ε^2A^2+ε^4(-3A^4+5A^2B^2)+O(ε^6),
}
\]
\[
\boxed{
q_3=ε^2B^2+ε^4(5A^2B^2-3B^4)+O(ε^6).
}
\]
The mixed term is present in each endpoint probability, but its coefficient differs in its role from the middle-spin expansion. The formulas are asymmetric in A,B as expected for fixed couplings on a path with labeled endpoints; exchanging A and B exchanges q1 and q3.

## 4. Exact consequence for entropy difference

IV-106 gives `I12-I13=2[h(q)-h(q3)]`. The expansions above show that the leading probabilities of q and q3 are `ε²(A²+B²)` and `ε²B²`, respectively. Consequently the entropy difference is not a regular polynomial expansion around `ε=0`; logarithmic terms from `h` must be kept. This report does not expand the difference because the cases `B=0` and fixed `B≠0` have distinct asymptotic behavior and need careful treatment.

## 5. Checks and limitations

- The q1/q3 formulas are derived by series-solving the parity-block eigenvector equations and expanding normalized probabilities.
- They obey endpoint exchange: `q1(A,B)=q3(B,A)`.
- The q3 auxiliary-field Hellmann–Feynman independent check is **not yet completed**; IV-107 is partial pending that check.
- This does not establish the Paper A target response identity.

## 6. Next audit

IV-108: independently derive q3 via an auxiliary `-kX_3` field and characteristic polynomial/Hellmann–Feynman, explicitly check the ε² and ε⁴ terms against IV-107. If the independent route disagrees, pause and reconcile.
