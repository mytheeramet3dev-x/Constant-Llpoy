# AS-ALPHA-A-PROP-0012 — IV-140: Critical Elimination Correction and Salvaged Radius-1/2 Certificate

Status: ANALYTIC; exact linear algebra checked; NOT LEAN-FORMALIZED; source proposition definitions and eigenbranch reconciliation remain open.

## 1. Critical correction to IV-133
Previously recorded IV-133 formulas for u,w,z do not satisfy the middle eigenvector equation. Substitution into d w-4y u-4x z yields residual -16xy/d, generally nonzero. Therefore IV-133 formulas are invalid for generic xy!=0. Dependent ratio criterion IV-135 and ordering claims IV-136, IV-137, IV-138's ordering step, and IV-139 must not be relied upon as originally stated. IV-130/131 component bounds and IV-132 axis cases should also be revisited where their derivations relied on the flawed elimination.

## 2. Correct simultaneous inversion
The system is
A v=(4x,0,4y)^T, A=[[d,-4y,0],[-4y,d,-4x],[0,-4x,d]], with F=d^2-16x^2-16y^2.
Correct formulas:
u=4x(d^2-16x^2+16y^2)/(dF),
w=32xy/F,
z=4y(d^2+16x^2-16y^2)/(dF).
Correct ratio w/u=8dy/(d^2-16x^2+16y^2), for x!=0.

## 3. Independent ordering proof on rho<1/2
Let Q=d^2-16x^2+16y^2. For rho<1/2, d>=4, and Q>=d^2-16x^2>=16-16rho^2>0.
To prove |w/u|<1 it is sufficient to show Q-8d|y|>0:
Q-8d|y|=(d-4|y|)^2-16x^2.
Since d>=4 and |x|+|y|<=sqrt(2)rho<sqrt(2)/2<1, we have d-4|y|>=4(1-|y|)>4|x|, so the expression is strictly positive. Thus u^2>w^2 for x!=0, without relying on the invalid IV-135 criterion.

## 4. Entropy-range proof from valid block-resolvent argument
This part of IV-138 does not depend on IV-133 elimination:
K has eigenvalues 0, +/-4rho, hence ||K||=4rho and lambda_min(N)>=1-4rho. Rayleigh gives lambda<=-3, so gap lambda_min(N-lambda I)>=4-4rho. With ||b||=4rho, ||v||<=rho/(1-rho). For rho<1/2, ||v||<1.
With D=1+||v||^2 and each numerator bounded by ||v||^2, q,q3<=||v||^2/(1+||v||^2)<1/2.
Combining the independent valid ordering argument and valid entropy range, conditional on source definitions/physical eigenbranch: for rho<1/2, x!=0 gives q3<q<1/2 and DeltaS>0. On x=0, direct equations give u=w=0 and q=q3, so DeltaS=0.

## 5. IV-139 status
IV-139's optimization of the old ordering criterion is invalid due to its dependence on the incorrect ratio formula. Do not cite its margin 16(1-R) as established. Its commit remains in history but is superseded by this correction. IV-138's claimed radius 1/2 is salvaged using the corrected independent ratio proof here, not IV-135/139.

## 6. Verification
Correct formulas were checked by symbolic matrix inversion and substitution into the three linear equations. This is analytic computational checking, not Lean proof or independent external audit.
