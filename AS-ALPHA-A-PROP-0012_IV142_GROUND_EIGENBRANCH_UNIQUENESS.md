# AS-ALPHA-A-PROP-0012 — IV-142: Ground Eigenvalue Branch Uniqueness in the Radius-1/2 Disk

Status: ANALYTIC spectral argument for the displayed matrix; NOT Lean formalized; source-proposition reconciliation remains unresolved.

## 1. Block setup
M=[[-3,b^T],[b,N]], b=(-4x,0,-4y)^T, N=I+K.
For rho=sqrt(x^2+y^2)<1/2, exact lower-block spectrum gives lambda_min(N)>=1-4rho>-1.
The Rayleigh quotient at e1 gives the lowest eigenvalue lambda_min(M)<=-3. Thus lambda_min(M)<lambda_min(N), with a strict spectral separation.

## 2. First coordinate cannot vanish
If a lowest-eigenvector had first coordinate a=0, then it would be an eigenvector of N with eigenvalue lambda_min(M), contradicting lambda_min(M)<lambda_min(N). Hence a!=0, and the eigenvector can be normalized to (1,v).

## 3. Schur complement equation
For lambda below spectrum of N, define R(lambda)=(N-lambda I)^(-1. The lower block equation gives v=-R(lambda)b. The upper equation yields scalar secular equation
f(lambda)=lambda+3+b^T R(lambda)b=0.
At the lowest eigenvalue this equation holds.

## 4. Uniqueness of root below lower-block spectrum
For lambda<lambda_min(N), R is positive definite. Differentiation gives
f'(lambda)=1+b^T R(lambda)^2 b>0.
Thus f is strictly increasing and has at most one root below lambda_min(N). The ground eigenvalue is therefore uniquely determined and simple: its eigenvector is determined by its nonzero first coordinate and the resolvent equation.

## 5. Parameter regularity
The matrix depends polynomially on x,y and the ground eigenvalue is simple with a spectral separation in the disk. Therefore the ground eigenvalue and normalized first-coordinate eigenvector branch are locally analytic in x,y (standard simple-eigenvalue perturbation result). This does not identify the branch with any original manuscript's branch without source reconciliation.

## 6. Scope
This proves uniqueness/regularity for the lowest eigenpair of the displayed 4x4 matrix within rho<1/2. It does not prove the paper's proposition unless the source Hamiltonian, parity reduction, basis, and definitions match exactly. No Lean proof or independent audit.
