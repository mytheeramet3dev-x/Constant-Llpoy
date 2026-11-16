# Analytic Nonnegative Eigenvalue — Entropy Directional-Derivative Lemma

**Purpose:** Control the first edge-direction derivative of \(-\lambda\ln\lambda\) when a reduced-state eigenvalue may vanish at a symmetric reference point.  
**Status:** Reusable analytic lemma for fixed finite-dimensional perturbation problems.

## Statement

Let \(r\in[0,r_0)\) and \(u\in(-\delta,\delta)\). Suppose:

1. \(\lambda(r,u)\) is real analytic in a neighborhood of \((0,0)\);
2. \(\lambda(r,u)\ge0\) for all \(r>0\) and all real \(u\) in the neighborhood;
3. for some integer \(m\ge1\), \(\lambda(r,u)=O(r^m)\) jointly as \(r\to0^+\), uniformly for \(u\) in a smaller compact neighborhood.

Then the directional derivative at \(u=0\) of

\[
F(r,u)=-\lambda(r,u)\ln\lambda(r,u),
\qquad F=0\text{ when }\lambda=0,
\]

exists for every sufficiently small \(r>0\), and

\[
\left.\partial_u F(r,u)\right|_{u=0}
=O\!\left(r^m(1+|\ln r|)\right).
\]

The same conclusion holds for any fixed real edge direction \(u=t v\) in a finite-dimensional parameter space.

## Proof

Fix a sufficiently small \(r>0\).

**Case 1: \(\lambda(r,0)=0\) for every sufficiently small \(r>0\).**

For each fixed \(r\), the function \(u\mapsto\lambda(r,u)\) is differentiable, nonnegative, and attains its minimum zero at the interior point \(u=0\). Therefore

\[
\partial_u\lambda(r,0)=0.
\]

Real analyticity in \(u\) gives \(\lambda(r,u)=O_r(u^2)\) as \(u\to0\). Hence

\[
-\lambda(r,u)\ln\lambda(r,u)
=O_r(u^2|\ln|u||),
\]

whose derivative at \(u=0\) is zero.

**Case 2: \(\lambda(r,0)\) is not identically zero as an analytic function of \(r\).**

Its one-variable Taylor series has a first nonzero term

\[
\lambda(r,0)=c r^k(1+O(r))
\]

for some finite integer \(k\ge m\). Nonnegativity for \(r>0\) forces \(c>0\). Thus

\[
|\ln\lambda(r,0)|=O(1+|\ln r|).
\]

The joint analytic estimate \(\lambda(r,u)=O(r^m)\) implies

\[
\partial_u\lambda(r,0)=O(r^m).
\]

For \(\lambda(r,0)>0\), the ordinary chain rule applies:

\[
\partial_uF(r,0)
=-(1+\ln\lambda(r,0))\partial_u\lambda(r,0).
\]

Combining the two estimates proves

\[
\partial_uF(r,0)
=O(r^m(1+|\ln r|)).
\]

For a finite-dimensional edge vector, restrict to any line \(u=t v\) and apply the same argument. \(\square\)

## Important limitations

- The lemma is for first directional derivatives at an interior point. It does not claim twice differentiability; the second derivative may diverge.
- Nonnegativity must hold on a two-sided real neighborhood of the reference point. A one-sided boundary point is not sufficient.
- Joint analyticity (or a comparably strong differentiability/vanishing-order hypothesis) is essential. An upper bound on \(\lambda\) alone does not control \(\partial_u\lambda\).
- The estimate is local and fixed-dimensional; constants may depend on \(N\) and the chosen neighborhood.

## Applications

- Strong-coupling edge response: the exactly zero singlet branch at the uniform point has zero first entropy directional derivative.
- Weak-coupling edge response: the rank-deficient branches of the two-site reduced state can be controlled without incorrectly bounding \(|\ln\lambda|\) from an upper eigenvalue estimate alone.
