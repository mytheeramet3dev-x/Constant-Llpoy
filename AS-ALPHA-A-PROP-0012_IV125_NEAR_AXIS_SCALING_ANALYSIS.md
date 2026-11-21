# IV-125 — Near-Axis Scaling Analysis and Matched Asymptotic Regimes

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** Leading-coefficient asymptotics audited analytically and with symbolic series. This is not full entropy-difference uniformity.

## 1. Ratio r -> 0 (B/A -> 0)

For A != 0,
C2 = -ln(epsilon^2 A^2) + H(r),
H(r)=1-(1+r)ln(1+r)+r ln r.

Symbolic expansion:
H(r)=1+r(ln r-1)-r^2/2+r^3/6-r^4/12+O(r^5).

If B/A=epsilon^alpha with alpha>0, r=epsilon^(2alpha), so
C2=1-ln(epsilon^2 A^2)+epsilon^(2alpha)(2alpha ln epsilon-1)-epsilon^(4alpha)/2+O(epsilon^(6alpha)).
For fixed A != 0, the dominant term 1-ln(epsilon^2 A^2) grows as -2 ln epsilon, while the ratio corrections vanish.

## 2. Ratio r -> infinity (A/B -> 0)

Rewrite exactly:
C2=-ln(epsilon^2 B^2)+G(s), s=A^2/B^2=1/r,
G(s)=1+(1+1/s)ln(1/(1+s)).

Symbolic expansion:
G(s)=-s/2+s^2/6-s^3/12+s^4/20+O(s^5).

If A/B=epsilon^alpha with alpha>0,
C2=-ln(epsilon^2 B^2)-epsilon^(2alpha)/2+epsilon^(4alpha)/6+O(epsilon^(6alpha)).
For fixed B != 0, the leading logarithm again dominates as epsilon -> 0.

## 3. Positivity implication for C2

The analytic lower bound from IV-123,
C2> -ln(epsilon^2(A^2+B^2)),
is ratio-independent for A,B != 0. Therefore if epsilon^2(A^2+B^2)<=1, it yields C2>0, including ratios that approach either axis, at the level of the leading coefficient.

This statement does not provide uniform control of the entropy expansion remainder as parameters approach axes; IV-124's caveat remains.

## 4. Scope

- Small-r and large-r expansions are symbolic checks of the leading coefficient C2 only.
- No matched asymptotic theorem for the full entropy difference is established here.
- Actual full entropy positivity in shrinking axis neighborhoods remains open pending direct probability/entropy bounds.
- No Lean proof is claimed.
