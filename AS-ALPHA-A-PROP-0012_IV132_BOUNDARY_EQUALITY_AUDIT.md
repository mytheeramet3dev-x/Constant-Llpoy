# AS-ALPHA-A-PROP-0012 — IV-132: Boundary, Degeneracy, and Equality-Case Audit

Status: ANALYTIC BOUNDARY AUDIT; NOT LEAN-FORMALIZED; source-proposition definitions still require reconciliation.

## Local domain
Use the box |x|,|y| <= r=1/1000, with IV-129's spectral estimate |delta|<=0.008 and d=4-delta in [3.992,4.008]. Thus d>4r, in particular d^2-16x^2>0 and d^2-16y^2>0 throughout this box.

The component equations are:
d u - 4y w = 4x,
d w - 4y u - 4x z = 0,
d z - 4x w = 4y,
delta = -4x u - 4y z.

## Case x=0 (the equality axis)
The first two equations reduce to
d u - 4y w = 0,
d w - 4y u = 0.
Their coefficient matrix has determinant d^2-16y^2>0, so u=w=0. The third equation gives z=4y/d. Hence q=(u^2+z^2)/D=z^2/D and q_3=(z^2+w^2)/D=z^2/D, so q=q_3 and ΔS=0 exactly, assuming the recorded q,q_3 definitions. This includes the origin y=0.

## Case y=0, x != 0 (strict positivity axis)
The first equation gives u=4x/d. The remaining pair is
d w - 4x z=0,
d z - 4x w=0.
Its determinant d^2-16x^2>0, hence w=z=0. Therefore q=u^2/(1+u^2)>0 and q_3=0. Since 0<q<1/2 follows from the local component bound, h(q)>h(0)=0 and ΔS>0. This is also consistent with the strict ordering q>q_3.

## Interior and box boundary
For x!=0 and |x|,|y|<=r, IV-131's exact-rational estimates show u^2-w^2>0 and 0<=q_3<q<1/2, so ΔS>0. The estimates are non-strict with respect to |x|<=r and |y|<=r; no separate loss occurs on the faces of the closed box.

## Equality classification within this local box
- x=0: equality ΔS=0, with q=q_3.
- x!=0: strict ΔS>0.
Thus, conditionally on the source proposition using the stated matrix, eigenvector branch, and probability definitions, the equality set in this local box is exactly the axis x=0.

## Remaining caveats
1. The eigenvector branch and component normalization must be matched to the original proposition text.
2. This boundary derivation is analytic but not Lean formalization or independent peer audit.
3. It is local only: |x|,|y|<=1/1000.
4. No global positivity or global equality classification is claimed.
