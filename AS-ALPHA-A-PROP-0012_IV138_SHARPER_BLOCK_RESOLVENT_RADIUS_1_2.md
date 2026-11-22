# AS-ALPHA-A-PROP-0012 — IV-138: Sharpness Analysis and Radius-1/2 Certificate

Status: ANALYTIC; exact matrix norm and rational/algebraic inequalities checked in derivation; NOT LEAN-FORMALIZED; original source proposition/branch reconciliation remains open.

## 1. Exact lower-block norm
For the lower block N=I+K,
K=[[0,-4y,0],[-4y,0,-4x],[0,-4x,0]],
the eigenvalues are 0 and +/-4rho, where rho=sqrt(x^2+y^2). Thus ||K||_2=4rho and lambda_min(N)>=1-4rho.

## 2. Rayleigh bound and resolvent
The full matrix has M_11=-3. Its lowest eigenvalue lambda satisfies lambda<=-3 by the Rayleigh quotient at e_1. Therefore
lambda_min(N-lambda I)>=1-4rho+3=4-4rho.
For rho<1, the gap is positive, and the lowest eigenvector cannot have first coordinate zero. Writing it as (1,v), v=(u,w,z), the lower-block equation gives
||v|| <= ||b||/gap <= 4rho/(4-4rho)=rho/(1-rho).

## 3. Entropy range, using the normalization correctly
D=1+||v||^2. Since each q and q3 numerator is a subset of the lower-component squared norm,
q,q3 <= ||v||^2/(1+||v||^2).
This upper bound is strictly less than 1/2 whenever ||v||<1. Our resolvent estimate gives ||v||<1 for rho<1/2. Hence q,q3<1/2 on that open disk.

## 4. Ordering
Here d=1-lambda>=4. The IV-135 criterion requires d>2|y| and d^2-16x^2>0. For rho<1/2, these hold since d>=4, |y|<1/2 and 16x^2<4<16.
The criterion is g(d)=d^2-4d|y|-16x^2>0. Since g is increasing for d>2|y|,
g(d)>=g(4)=16-16|y|-16x^2>=16(1-rho-rho^2).
This is positive for rho< (sqrt(5)-1)/2. In particular it is positive throughout rho<1/2, because 1-rho-rho^2>1-1/2-1/4=1/4.

## 5. Conditional entropy conclusion
For rho<1/2, q,q3<1/2. For x!=0, exact ratio criterion gives u^2>w^2, so q-q3=(u^2-w^2)/D>0 and binary entropy strict monotonicity yields Delta S>0. For x=0, axis equations give u=w=0 and q=q3, hence Delta S=0. Thus the conditional equality set in the open certified disk is x=0.

## 6. Scope and correction
This is a fourfold radial enlargement relative to IV-137's radius 1/8. It is not a sharpness proof for the theorem or for the matrix's actual positivity domain: it is a larger certified disk for this proof chain. No Lean proof, independent audit, or global branch theorem is claimed. Source proposition definitions and eigenbranch assumptions still need reconciliation.
