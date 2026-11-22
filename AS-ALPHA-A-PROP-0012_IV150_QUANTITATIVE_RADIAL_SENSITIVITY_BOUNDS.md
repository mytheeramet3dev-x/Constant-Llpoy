# AS-ALPHA-A-PROP-0012 — IV-150: Quantitative Radial Sensitivity Bounds

Status: ANALYTIC-PARTIAL; conditional on the stated matrix model; not Lean-verified.

## Setup
On the disk 0 < rho < 1/2, put t=rho^2 and m=(x^2-y^2)^2/rho^4 in [0,1]. The scalar ground-state equation is d-4=R(d,t,m), with
R=16t(d^2-16mt)/[d(d^2-16t)].
Here d>=4. From IV-149, R_t>0, R_d<=0, and implicit differentiation gives d_t=R_t/(1-R_d).

Write
P=d^4-32md^2t+256mt^2,
R_t=16P/[d(d^2-16t)^2],
and -R_d=b^T A^{-2}b, where A=dI+K, ||K||=4rho and ||b||=4rho.

## Bounds for P
For d>=4 and 0<=t<1/4, the coefficient -32d^2t+256t^2=32t(-d^2+8t) is nonpositive, so P<=d^4.
For fixed m, P decreases with t because P_t=m(-32d^2+512t)<0. The expression is minimized over m in [0,1] at m=1, and over t in [0,1/4] at t=1/4. Hence
P>=d^4-8d^2+16.
This polynomial is positive: at d^2=16 it equals 144, and its derivative with respect to d^2 is 2d^2-8>0.

## Bounds for R_t
Since d^2-16t<=d^2 and d^2-16t>d^2-4,
16(d^4-8d^2+16)/d^5 <= R_t <= 16d^3/(d^2-4)^2.

## Bounds for implicit denominator
Eigenvalues of A are at least d-4rho. Thus
0<=-R_d=b^T A^{-2}b<=16rho^2/(d-4rho)^2.
Consequently
1<=1-R_d<=1+16rho^2/(d-4rho)^2.

## Radial derivative
Combining d_t=R_t/(1-R_d), and d_rho=2rho d_t, yields the explicit bounds
2rho * [16(d^4-8d^2+16)/d^5] / [1+16rho^2/(d-4rho)^2]
<= d_rho <=
2rho * [16d^3/(d^2-4)^2],
for 0<rho<1/2, with d=d(rho,theta)>=4. In particular, d_rho>0 and the sensitivity is O(rho) as rho approaches zero (these displayed bounds themselves have constants that remain finite near d=4).

## Audit notes
- All inequalities above are strict-domain statements for rho<1/2; endpoints are not included.
- The estimates are conservative, not sharp.
- d depends on angle through m. The derivative here is radial at fixed angle.
- The derivation is analytic and not a Lean proof, independent formal verification, or manuscript reconciliation.
