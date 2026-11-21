# PROP-0012 — Joint Uniform O(r^3) Claim for the Odd-Block Zero Eigenbranch

**Target:** Check whether the odd-block eigenvalue that vanishes at the uniform point is actually O_N(r^3) jointly in weak-coupling parameter r and edge perturbations u, as assumed in some prior status language.

## 1. Leading odd block is a Gram matrix

The leading odd block is
[
M_{m odd}(r,mathbf u)=sum_{kge3}
egin{pmatrix}a_{2k}\a_{1k}end{pmatrix}
egin{pmatrix}a_{2k}&a_{1k}end{pmatrix}
+O_N(r^3),
]
with each amplitude (a_{ik}=r(1+u_{ik})/4+O_N(r^2)). This leading Gram matrix is rank one at the fully uniform point because the two rows coincide. But for a generic fixed nonzero edge perturbation u in any neighborhood, the two row vectors are no longer proportional; the Gram matrix has a second eigenvalue of order (r^2), proportional to the squared row mismatch.

## 2. Counterexample to the joint uniform O(r^3) bound

Take N=4 and perturb only edge 13 by a fixed small (u_{13}=t
e0), keeping other edges uniform. The row vectors over k=3,4 are proportional at t=0, but at t≠0 their k=3 components differ by (rt/4), while the k=4 components remain equal. The Gram determinant is positive at order (r^4t^2), and since its large eigenvalue is order (r^2), the smaller eigenvalue is order (r^2t^2), not O(r^3) as r→0 with t fixed. Therefore a uniform joint bound (lambda_-(r,mathbf u)=O(r^3)) on a fixed u-neighborhood is false for this odd block.

## 3. What remains valid at the uniform reference point

At the uniform reference (mathbf u=0), the odd-block zero eigenvalue is exactly zero for all sufficiently small r by the symmetry/identical-row structure. For each fixed r>0, it is nonnegative and reaches an interior minimum at u=0. Consequently its first directional derivative is zero. Its entropy contribution to the first directional derivative is also zero. This argument does **not** require the false joint O(r^3) estimate.

The positive odd-block eigenbranch is separated after factoring r^2 and can be handled by its own analytic expansion and derivative calculation.

## 4. Corrected obligation

Do not require the odd-block rank-changing zero branch to satisfy a joint uniform O(r^3) bound. The proof should instead use the exact zero at the uniform point and the interior-minimum argument for its first derivative. Keep the joint analytic O(r^3) obligation only for branches where a direct block expansion actually establishes it (notably the small branch from the even block, subject to verification).

## Verdict

**FOUND A GAP IN PRIOR AUDIT LANGUAGE; CORRECTED ROUTE AVAILABLE.** The generic fixed-u neighborhood joint O(r^3) estimate for the odd zero branch is invalid. Its first entropy directional derivative at the uniform reference is nevertheless zero by exact nonnegativity and interior minimum. This correction does not invalidate the leading coefficient calculation, but removes an unnecessary/false branch remainder requirement. The even-block small branch and full remainder closure remain to be checked.

No Lean proof/build performed.
