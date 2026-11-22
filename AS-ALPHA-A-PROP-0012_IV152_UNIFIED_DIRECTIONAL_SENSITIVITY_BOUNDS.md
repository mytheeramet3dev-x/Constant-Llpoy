# AS-ALPHA-A-PROP-0012 — IV-152: Unified Directional Sensitivity Bounds

Status: ANALYTIC-PARTIAL; conditional on the stated matrix model; not Lean-verified.

## Coordinates and derivatives
Let rho=sqrt(x^2+y^2)>0, theta be the polar angle, t=rho^2, and m=cos^2(2theta)=(x^2-y^2)^2/rho^4. The scalar ground-state variable d is differentiable on the open disk rho<1/2 by the separated simple eigenbranch/implicit relation established in prior records.

The polar gradient identity is
grad d = d_rho e_r + (d_theta/rho)e_theta,
where e_r=(cos theta,sin theta), e_theta=(-sin theta,cos theta), an orthonormal pair.

For any direction v=(a,b), the directional derivative is
D_v d = grad d dot v
= d_rho(a cos theta+b sin theta)
+(d_theta/rho)(-a sin theta+b cos theta).

## Norm and direction-independent estimate
By orthogonality,
||grad d||^2=d_rho^2+(d_theta/rho)^2.
Thus |D_v d|<=||grad d|| ||v|.

Define the IV-150 radial upper bound
U_r=2rho*16d^3/(d^2-4)^2.
Define the IV-151 angular upper bound
U_theta=2|sin(4theta)|*256t^2/[d(d^2-16t)].
Then, for 0<rho<1/2,
|D_v d|<=sqrt(U_r^2+(U_theta/rho)^2)*sqrt(a^2+b^2).
This is a valid direction-independent Lipschitz estimate at each point (rho,theta), expressed in terms of the local d and coordinates. It is not a uniform constant over the full disk.

## Radial nondegeneracy
IV-150 provides a strictly positive lower bound L_r for d_rho on the open punctured disk. Since ||grad d||>=d_rho, it follows that ||grad d||>=L_r>0 at each such point. Hence no stationary point of d exists inside 0<rho<1/2. This statement concerns the scalar d branch only.

## Origin and domain notes
Polar coordinates and m are undefined at rho=0, so the displayed directional decomposition is stated for rho>0. The model may have a differentiable extension at the origin, but this record does not prove it. The disk rho<1/2 is open; no boundary claim at rho=1/2 is made.

## Audit status
The derivation combines the earlier radial and angular bounds with the Euclidean Cauchy–Schwarz inequality. It is analytic, not Lean-verified, and dependent on the validity of prior IV-149 through IV-151 derivations. Independent verification and reconciliation to the original manuscript remain open.
