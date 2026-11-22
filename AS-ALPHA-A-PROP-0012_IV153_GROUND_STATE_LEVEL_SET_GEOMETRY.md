# IV-153 — Ground-State Level-Set Geometry and Global Radial Graph Structure

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC-PARTIAL; matrix-model conditional; not Lean-verified

## 1. Scope

This note studies the geometry of level sets of the scalar ground-state parameter \(d(x,y)\) in the open coupling disk \(\rho=\sqrt{x^2+y^2}<1/2\). It uses the implicit scalar equation established in the preceding records:

\[
d-4=R(d,t,m),\qquad
R(d,t,m)=\frac{16t(d^2-16mt)}{d(d^2-16t)},
\]
where \(t=\rho^2\), \(m=\cos^2(2\theta)\in[0,1]\), and \(d\ge4\).

The claims below are restricted to this model and domain. This record does not reconcile the matrix model with the original manuscript and is not a formal proof certificate.

## 2. Radial monotonicity and regular level sets

The preceding radial analysis establishes \(d_\rho>0\) for \(0<\rho<1/2\), at fixed angle, and the angular derivative analysis establishes a differentiable branch on the disk. Consequently, for every point with \(\rho>0\), the gradient is nonzero because its radial component is nonzero:
\[
\nabla d\ne0.
\]

By the regular-level-set theorem, for every value \(c\) and every point \(p\) in the open disk with \(d(p)=c\), the level set \(\{(x,y):d(x,y)=c\}\) is locally a smooth one-dimensional embedded submanifold near \(p\). The origin is excluded from this regularity conclusion because radial coordinates degenerate there and \(\nabla d(0,0)=0\) by symmetry.

## 3. Uniqueness along rays

Fix \(\theta\). The function \(\rho\mapsto d(\rho,\theta)\) is strictly increasing on \((0,1/2)\), and has continuous central value \(d(0)=4\). Therefore each ray has at most one point satisfying \(d(\rho,\theta)=c\).

For \(c>4\), existence along a given ray is conditional on \(c\) lying in the range attained on that ray before the open-disk boundary. This note does not assert a common range for all angles, nor that a level set is a single closed curve.

Thus, where the level intersects a ray, its radius is uniquely determined. On any angular interval where the intersection exists and remains interior, the implicit function theorem gives a local radial graph \(\rho=\rho_c(\theta)\), with
\[
\rho_c'(\theta)=-\frac{d_\theta}{d_\rho}.
\]
The denominator is strictly positive on the punctured disk.

## 4. Symmetry of the scalar branch

The scalar equation depends on the direction only through
\[
m=\cos^2(2\theta)=\frac{(x^2-y^2)^2}{(x^2+y^2)^2},
\]
and through \(t=x^2+y^2\). Both are invariant under sign flips of either coordinate and under interchange \(x\leftrightarrow y\). The uniquely selected implicit ground-state branch is therefore invariant under these transformations wherever the scalar equation characterizes that branch:
\[
d(x,y)=d(-x,y)=d(x,-y)=d(y,x).
\]
This yields the corresponding dihedral symmetry of the level sets (reflections and quarter-turn symmetry). It does not imply that each level set is a circle.

## 5. Geometric conclusions and limitations

Established conditionally from the preceding scalar model:
- every noncentral level-set point is regular;
- a fixed ray intersects a level at most once;
- level sets admit local radial-graph representations wherever they intersect and \(d_\rho>0\);
- the scalar level-set geometry inherits sign-flip and coordinate-swap symmetries.

Not established here:
- that a level set is globally connected;
- that every level is a closed curve;
- that a level set is convex;
- that its angular domain is the full circle;
- boundary values at \(\rho=1/2\);
- independent verification of all prior derivative/bound formulas.

## 6. Next audit target

Before expanding the geometry further, perform an independent symbolic and numerical consistency audit of the implicit radial/angular formulas and the symmetry claims, including the behavior at the origin and on symmetry axes. Do not promote the conditional results to a global theorem until that audit is completed.

