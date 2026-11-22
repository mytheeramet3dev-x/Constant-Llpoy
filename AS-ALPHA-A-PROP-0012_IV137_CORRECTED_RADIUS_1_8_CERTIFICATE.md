# AS-ALPHA-A-PROP-0012 — IV-137: Corrected Radius Optimization and Certified Radius-1/8 Positivity

Status: ANALYTIC RATIONAL CERTIFICATE; NOT LEAN-FORMALIZED; source proposition definitions and eigenbranch still require reconciliation.

## 1. Correction to the previous radius algebra
For disk rho<=R, Weyl gives d>=d0=4-8R. The conservative ordering bound used is
g(d)=d^2-4d|y|-16x^2
>= d0^2-4d0R-16R^2.
The earlier IV-137 draft algebraically mis-simplified this expression. The correct polynomial is
16-80R+80R^2 = 16(1-5R+5R^2),
not 16(1-3R)^2.
This is a transparent correction; no optimization conclusion should rely on the erroneous expression.

## 2. Certified explicit radius R=1/8
Take R=1/8. Then d0=4-8R=3. Since d>=3>2|y|, g(d) is increasing in d. Exact rational evaluation:
d0^2-4d0R-16R^2 = 9 - 3/2 - 1/4 = 29/4 > 0.
Also d^2-16x^2 >= 9-1/4=35/4>0. Thus the exact ratio criterion certifies u^2>w^2 whenever x!=0 in this disk.

## 3. Resolvent component bound on the same disk
Perturbation norm ||E||<=8R=1. Weyl yields lambda<=-2. Lower block N=I+K has lambda_min(N)>=0. Therefore lambda_min(N-lambda I)>=2.
Coupling vector b has norm 4rho<=1/2. With normalized first component eigenvector (1,v), the lower-block equation gives ||v||<=||b||/2<=1/4.
Hence u^2+w^2+z^2<=1/16, and since D>=1:
0<=q,q3<=1/16<1/2.

## 4. Entropy conclusion
For x!=0, ratio ordering gives u^2>w^2, hence q-q3=(u^2-w^2)/D>0. Thus 0<=q3<q<1/2, so binary entropy strictly increases and ΔS>0.
For x=0, axis equations give u=w=0, q=q3, ΔS=0.
So conditional on the original definitions and branch, within rho<=1/8 the equality set is x=0.

## 5. Radius optimization caveat
The crude resolvent estimate on a general radius R<1/4 gives
||v||<=R/(1-4R).
Requiring its square <1/2 yields R<(4-sqrt(2))/14 = 1/(4+sqrt(2)) ≈0.1846990313. This is only a supremum for this conservative entropy-range estimate, not a proven optimal theorem radius. The ratio criterion is less restrictive in this estimate family.
The radius R=1/8 is selected because it has simple exact rational margins: d>=3, ordering margin 29/4, resolvent gap >=2, and ||v||<=1/4.

## 6. Verification status
The exact rational substitutions were checked. No Lean formalization or external independent audit. No global theorem claimed.
