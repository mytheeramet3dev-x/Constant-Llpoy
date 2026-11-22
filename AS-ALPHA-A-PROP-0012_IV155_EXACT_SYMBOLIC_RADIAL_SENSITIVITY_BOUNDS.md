# IV-155 — Exact Symbolic Verification of Candidate Radial Sensitivity Bounds

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC; conditional on the established implicit model; not Lean-verified

## 1. Definitions and domain

Assume \(0\le t=\rho^2<1/4\), \(d\ge4\), and \(m\in[0,1]\). Define
\[
R(d,t,m)=\frac{16t(d^2-16mt)}{d(d^2-16t)}.
\]
The implicit branch satisfies \(d-4=R\). Its radial derivative in the variable \(t\) is
\[
d_t=\frac{R_t}{1-R_d}.
\]
The prior resolvent representation gives \(R_d=-b^TA^{-2}b\le0\), where \(A=dI+K\), \(\|K\|=4\rho\), and \(\|b\|=4\rho\).

This record proves the candidate bounds symbolically within these hypotheses.

## 2. Exact expression for \(R_t\)

Direct differentiation yields
\[
R_t=\frac{16P(d,t,m)}{d(d^2-16t)^2},
\]
where
\[
P=d^4-32md^2t+256mt^2.
\]

## 3. Lower bound for P

For fixed \(d,m\),
\[
P_t=m(-32d^2+512t).
\]
Since \(d^2\ge16\) and \(0\le t<1/4\),
\[
-32d^2+512t\le-512+128=-384<0.
\]
Thus \(P\) is nonincreasing in \(t\). Its minimum over the closed comparison interval \([0,1/4]\) occurs at \(t=1/4\):
\[
P\ge d^4-8md^2+16m.
\]
The right side is decreasing in \(m\) because its derivative with respect to m is \(-8d^2+16<0\). Therefore
\[
P\ge d^4-8d^2+16.
\]
The lower expression is strictly positive for \(d^2\ge16\): write \(s=d^2\); \(s^2-8s+16=(s-4)^2\ge144\) for \(s\ge16\).

## 4. Upper bound for P

For \(t<1/4\) and \(d^2\ge16\),
\[
-32d^2t+256t^2=32t(-d^2+8t)\le0.
\]
Since \(m\in[0,1]\),
\[
P=d^4+m(-32d^2t+256t^2)\le d^4.
\]

## 5. Denominator bounds

Because \(d^2-16t>0\) and \(d\ge4\), the denominator of \(R_t\) is positive. Also,
\[
(d^2-16t)^2\le d^4,
\]
so the lower estimate
\[
R_t\ge \frac{16(d^4-8d^2+16)}{d^5}
=:L_t
\]
follows.

And since \(16t<4\),
\[
d^2-16t>d^2-4>0,
\]
hence
\[
(d^2-16t)^2>(d^2-4)^2.
\]
Using \(P\le d^4\), we get
\[
R_t<\frac{16d^3}{(d^2-4)^2}
=:U_t.
\]
A non-strict upper bound \(R_t\le U_t\) is consequently valid as well.

## 6. Resolvent correction

The eigenvalues of \(K\) are \(0,\pm4\rho\), so
\[
\lambda_{\min}(A)\ge d-4\rho>0.
\]
Therefore
\[
0\le -R_d=b^TA^{-2}b
\le \frac{\|b\|^2}{(d-4\rho)^2}
=\frac{16t}{(d-4\rho)^2}
=:B.
\]
Consequently,
\[
1\le1-R_d\le1+B.
\]

## 7. Certified radial sensitivity bounds

Since \(d_t=R_t/(1-R_d)\) with positive numerator and denominator,
\[
\boxed{\frac{L_t}{1+B}\le d_t\le U_t}.
\]
Explicitly,
\[
\boxed{
\frac{16(d^4-8d^2+16)}{d^5\left(1+\frac{16t}{(d-4\rho)^2}\right)}
\le d_t
\le
\frac{16d^3}{(d^2-4)^2}.
}
\]
For \(\rho>0\), multiplying by \(2\rho\) yields bounds on \(d_\rho=2\rho d_t\). The lower bound is strictly positive throughout the open disk; at the center, \(d_\rho=0\) by symmetry and radial-coordinate regularity.

## 8. Audit caveat

The algebraic inequalities above are proven under the stated resolvent/implicit-branch premises. They do not constitute independent verification of every earlier record, nor do they replace a Lean proof or source-manuscript reconciliation. The bounds may be conservative; no sharpness claim is made.

## 9. Next review target

Independently review the entropy/probability identities recorded in IV-146 and the small-coupling expansions recorded in IV-147. Do not infer entropy monotonicity from these radial bounds alone.
