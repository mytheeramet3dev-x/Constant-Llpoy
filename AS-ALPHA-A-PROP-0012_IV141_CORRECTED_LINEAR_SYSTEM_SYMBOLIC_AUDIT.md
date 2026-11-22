# AS-ALPHA-A-PROP-0012 — IV-141: Corrected Linear-System Algebraic Audit

Status: symbolic exact algebra audit; NOT an independent human audit; NOT Lean formalization.

## 1. Matrix and determinant
A=[[d,-4y,0],[-4y,d,-4x],[0,-4x,d]], RHS=(4x,0,4y)^T.
Exact symbolic determinant:
det(A)=d(d^2-16x^2-16y^2)=dF.

## 2. Candidate solution
u=4x(d^2-16x^2+16y^2)/(dF),
w=32xy/F,
z=4y(d^2+16x^2-16y^2)/(dF).

Exact symbolic multiplication gives A(u,w,z)^T-(4x,0,4y)^T=(0,0,0)^T. Thus the corrected candidate solves all three equations when denominators are nonzero.

## 3. Ratio
For x!=0 and F,d nonzero:
w/u=8dy/(d^2-16x^2+16y^2).

## 4. Corrected ordering criterion
For rho<1/2, d>=4. Q=d^2-16x^2+16y^2>=16-16rho^2>0.
Moreover Q-8d|y|=(d-4|y|)^2-16x^2.
Because |x|+|y|<=sqrt(2)rho<sqrt(2)/2<1, d-4|y|>=4(1-|y|)>4|x|, so Q-8d|y|>0. Therefore |w/u|<1 for x!=0, and u^2>w^2.

## 5. Limits
The symbolic residual check verifies the algebraic candidate only. It is not independent external verification and is not a proof of source eigenbranch identification, original proposition, or Lean theorem.
