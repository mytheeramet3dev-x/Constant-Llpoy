# IV-128 — Analytic Factorization via Symmetry and the Implicit-Function Theorem

**Status:** PROVED LOCAL STRUCTURAL LEMMA (nonquantitative) / explicit bounds OPEN.  
**Proposition AS-ALPHA-A-PROP-0012:** remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.

## 1. Analytic eigenvector branch
At ((x,y)=(0,0)), the even-parity matrix is diagonal with eigenvalues (-3,1,1,1). The lowest eigenvalue (-3) is simple, separated by a gap of (4). Hence, by analytic perturbation theory, the lowest eigenvalue and an eigenvector normalized by first coordinate equal to (1), ((1,u,w,z)), are analytic in a neighborhood of the origin. The normalization is valid locally because the first component of the eigenvector at the origin is nonzero.

## 2. Symmetry parity
Let (M(x,y)) be the matrix in the active audit. Define diagonal sign matrices
\[
P_x=\operatorname{diag}(1,-1,-1,1),\qquad
P_y=\operatorname{diag}(1,1,-1,-1).
\]
Direct entrywise inspection gives
\[
P_xM(x,y)P_x=M(-x,y),\
P_yM(x,y)P_y=M(x,-y).
\]
The lowest eigenvalue is invariant under these transformations. With first-coordinate normalization fixed, uniqueness of the local eigenvector branch implies:
- (u(x,y)) is odd in (x), even in (y);
- (w(x,y)) is odd in (x), odd in (y);
- (z(x,y)) is even in (x), odd in (y).

Analytic parity implies divisibility in the local analytic ring:
\[
u=xU(x,y),\quad w=xyW(x,y),\quad z=yZ(x,y),
\]
where (U,W,Z) are analytic near the origin. This establishes the factorization without assuming it from a truncated series.

## 3. Leading values at the origin
The first-order equations at the origin give
\[
u=x+O((|x|+|y|)^3),\qquad z=y+O((|x|+|y|)^3).
\]
The second eigenvector equation is
\[
(4-\delta)w=4yu+4xz.
\]
Substituting the leading terms and (4-\delta=4+O(x^2+y^2)) gives
\[
w=2xy+\text{higher-order terms}.
\]
Thus
\[
U(0,0)=1,\quad W(0,0)=2,\quad Z(0,0)=1.
\]

## 4. Local consequence (nonquantitative)
Continuity yields some radius (ho>0) such that on (|x|,|y|<ho),
\[
|U|>1/2,\quad |W|<3,\quad |Z|<2.
\]
Taking (ho) smaller so (9y^2<1/4), we obtain
\[
u^2-w^2=x^2(U^2-y^2W^2)>0
\]
for (x\ne0). Since (D>0), (q-q_3=(u^2-w^2)/D>0). Because (q,q_3	o0) at the origin, further shrink (ho) to ensure (0le q_3<q<1/2). Binary entropy is strictly increasing on ((0,1/2)), so
\[
\Delta S=2[h(q)-h(q_3)]>0
\]
for (x
e0), and equality when (x=0).

This is a local existence result for a sufficiently small coupling neighborhood; it does not give a computable radius.

## 5. Scope and audit cautions
- The factorization and parity argument is now justified locally by matrix symmetries and analytic eigenvector uniqueness.
- The radius and bounds remain nonquantitative.
- This argument covers sufficiently small absolute couplings ((x,y)), not necessarily the full domain of Proposition 0012.
- The original paper's exact probability labels and entropy target must still be checked against the source statement before treating this local conclusion as a result about the proposition.
- No Lean proof or global theorem is claimed.

## 6. Next (IV-129)
Obtain explicit rational bounds on the analytic branch using a contraction/implicit-equation estimate, or derive a computable interval for (ho) with validated eigenvector and probability bounds. Then reconcile this local lemma with the proposition's actual parameter domain.
