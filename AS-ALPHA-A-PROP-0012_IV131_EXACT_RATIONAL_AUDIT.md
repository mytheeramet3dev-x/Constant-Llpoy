# AS-ALPHA-A-PROP-0012 — IV-131: Exact Rational Audit of IV-130 Bounds

Status: ANALYTIC / EXACT-RATIONAL CHECKS; NOT LEAN-FORMALIZED; NOT INDEPENDENTLY AUDITED.

## Scope
Recheck the algebra and numerical constants used in IV-130 for the local box r=1/1000. This is an exact rational-arithmetic calculation and a paper-level audit, not a machine-checked theorem proof.

## Inputs
From IV-129, the perturbation estimate gives |delta| <= 8r = 0.008. Therefore d=4-delta lies in [3.992,4.008], represented exactly as [499/125,501/125].

Set
t_+ = 4/(3.992) = 500/499,
t_- = 4/(4.008) = 500/501.

For |x|,|y| <= r, the absolute-value inequalities are
|u| <= t_+(|x|+|y||w|),
|z| <= t_+(|y|+|x||w|),
|w| <= t_+(|y||u|+|x||z|).

Substitution yields
|w| <= 2t_+^2|xy| + t_+^2(x^2+y^2)|w|.
Since x^2+y^2 <= 2r^2 and 1-2t_+^2r^2 > 0, this gives |w| <= C_w|xy|, where
C_w = 2t_+^2/(1-2t_+^2r^2) = 1000000/498001 ≈ 2.0080280963291237.

Then
|u| <= C_u|x|, |z| <= C_u|y|,
C_u=t_+(1+C_wr^2)=499000/498001 ≈ 1.0020060200682328.

Lower estimate (for x ≠ 0):
|u| >= t_-|x|(1-C_wr^2),
C_{u,lo}=t_-(1-C_wr^2)=83000000/83166167 ≈ 0.9980019879959119.
This follows from |x+yw| >= |x|-|y||w| and 4/d >= t_-.

## Exact positivity check
The ordering bracket is
C_{u,lo}^2-(C_wr)^2
= 984138873000000/988087333353127
≈ 0.9960039358669566 > 0.
Also C_wr < C_{u,lo} exactly (r=1/1000), so the lower factor is positive.

Thus u^2-w^2 >= x^2[C_{u,lo}^2-(C_wr)^2] > 0 whenever x ≠ 0 in the box.

## Probability upper bounds
Using D >= 1:
q <= 2C_u^2r^2 = 498002/248004996001 ≈ 2.0080321285059596e-6 < 1/2.
q_3 <= C_u^2r^2 + C_w^2r^4
= 249002/248004996001 ≈ 1.0040200964298153e-6 < 1/2.

Consequently, if the probability definitions in the source proposition are indeed q=(u^2+z^2)/D and q_3=(z^2+w^2)/D, then q-q_3=(u^2-w^2)/D > 0 and 0 <= q_3 < q < 1/2. Binary entropy is strictly increasing on [0,1/2], so the recorded entropy difference is strictly positive for x != 0 in this box; equality on x=0 follows from the relevant exact symmetry only if the source definitions/eigenvector branch are verified.

## Corrections to IV-130 displayed decimals
IV-130's displayed approximate values for C_w, C_u, C_{u,lo}, the bracket, and q/q_3 upper bounds do not match the exact formulas above and are replaced by these exact fractions and decimal values. The qualitative inequalities remain positive.

## Caveats
- No Lean formalization or independent external audit has been completed.
- Decimal displays are informational; the exact fractions are the reproducible certificate for the arithmetic.
- The local result still requires checking the source proposition's definitions, domain, and normalized eigenvector convention.
- The symmetry matrices in the earlier IV-128 discussion should be corrected/rederived: for this matrix, P_x=diag(1,-1,1,-1) flips the x-edges and preserves y-edges; P_y=diag(1,1,-1,-1) flips the y-edges and preserves x-edges.

