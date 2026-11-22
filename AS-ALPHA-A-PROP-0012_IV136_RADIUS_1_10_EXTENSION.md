# AS-ALPHA-A-PROP-0012 — IV-136: Certified Radius-1/10 Local Extension

Status: ANALYTIC BOUNDS WITH EXACT CONSTANTS; NOT LEAN-FORMALIZED; source-proposition definitions/branch reconciliation pending.

## 1. Domain
Consider the coupling disk rho=sqrt(x^2+y^2)<=1/10. Matrix perturbation satisfies ||E||_2<=||E||_F=8rho<=4/5. Weyl gives |delta|<=4/5, so d=4-delta>=16/5.

## 2. Ratio ordering
For x!=0, exact elimination yields |w/u|=4d|y|/(d^2-16x^2), provided denominator nonzero. The sufficient ordering condition is g(d)=d^2-4d|y|-16x^2>0. Since d>=16/5>2|y| throughout the disk, g is increasing in d. Conservatively:
g(d)>=g(16/5)>= (16/5)^2 -4(16/5)(1/10)-16(1/10)^2 = 44/5 >0.
Therefore u^2>w^2 for every x!=0 in this disk. This also ensures d^2-16x^2>0.

## 3. Component norm and entropy range
Write the matrix in block form with scalar upper-left entry -3+E_11 and lower block N=I+K. The lower block satisfies ||K||<=||E||<=4/5. The lowest eigenvalue lambda satisfies lambda<=-3+4/5=-11/5. Thus
lambda_min(N-lambda I)>= (1-4/5)-(-11/5)=12/5.
The coupling column b between first coordinate and the remaining coordinates is (-4x,0,-4y), so ||b||=4rho<=2/5. Normalize the eigenvector as (1,v). Its lower block equation gives
||v||<=||b||/||N-lambda I||<= (2/5)/(12/5)=1/6.
Hence u^2+w^2+z^2<=1/36. With D=1+||v||^2>=1, both q=(u^2+z^2)/D and q3=(z^2+w^2)/D satisfy 0<=q,q3<=1/36<1/2.

For x!=0, the ordering u^2>w^2 implies q-q3=(u^2-w^2)/D>0. Therefore 0<=q3<q<1/2 and binary entropy monotonicity yields ΔS>0.

## 4. Equality axis
When x=0, the exact axis equations give u=w=0 and z=4y/d, hence q=q3 and ΔS=0. Thus, conditional on the recorded matrix, branch and probability definitions, equality occurs exactly on x=0 within this disk.

## 5. Extension significance and limitations
This proves an analytical local extension from the earlier box |x|,|y|<=1/1000 to the disk rho<=1/10, a 100-fold increase in radial scale, using conservative Weyl/resolvent estimates. It does NOT prove global positivity. No Lean proof or independent audit has been completed.
