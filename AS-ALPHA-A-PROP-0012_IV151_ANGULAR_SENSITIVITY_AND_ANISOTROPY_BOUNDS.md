# AS-ALPHA-A-PROP-0012 — IV-151: Angular Sensitivity and Anisotropy Bounds

Status: ANALYTIC-PARTIAL; conditional on the stated matrix model; not Lean-verified.

## Setup
For fixed rho in (0,1/2), let t=rho^2 and m=cos^2(2theta)=(x^2-y^2)^2/rho^4. The scalar ground-state relation is d-4=R(d,t,m), where
R(d,t,m)=16t(d^2-16mt)/[d(d^2-16t)].
From the implicit differentiation identity,
d_m=R_m/(1-R_d).

## Exact angular parameter derivative
Direct differentiation with respect to m gives
R_m=-256t^2/[d(d^2-16t)].
Since R_d=-b^T A^{-2}b<=0, we have 1-R_d>=1. Thus
|d_m|=256t^2/[d(d^2-16t)(1-R_d)]
and the strict sign is d_m<0 for rho>0.

Using IV-150's bound
1-R_d <= 1+16rho^2/(d-4rho)^2,
we obtain
256t^2/[d(d^2-16t)(1+16rho^2/(d-4rho)^2)]
<= |d_m| <=
256t^2/[d(d^2-16t)].

## Angular derivative
m(theta)=cos^2(2theta)=(1+cos(4theta))/2, so m_theta=-2sin(4theta).
Therefore
d_theta=-2sin(4theta)d_m.
Consequently, for 0<rho<1/2,
2|sin(4theta)| * 256t^2/[d(d^2-16t)(1+16rho^2/(d-4rho)^2)]
<= |d_theta| <=
2|sin(4theta)| * 256t^2/[d(d^2-16t)].
The sign is determined exactly by sin(4theta): since d_m<0, d_theta has the same sign as sin(4theta) whenever sin(4theta) !=0. At angular symmetry directions sin(4theta)=0, d_theta=0.

## Anisotropy observations
- The scalar branch is decreasing in m: d_m<0.
- Since m=cos^2(2theta), the scalar branch has stationary angular directions at theta=k*pi/4.
- The sensitivity vanishes at these directions and is bounded by the displayed estimates elsewhere.
- At fixed rho, d(theta) is a function of m alone, so its angular pattern is invariant under the symmetries of cos^2(2theta); this conclusion is for the scalar d-branch, not automatically for every observable or entropy.

## Scope and verification
These formulas follow by differentiating the scalar relation and using the IV-149/150 resolvent denominator estimates. They are analytic derivations, not a Lean formalization, independent audit, or reconciliation with the original manuscript. Endpoint rho=0 and rho=1/2 are excluded from the stated bounds.
