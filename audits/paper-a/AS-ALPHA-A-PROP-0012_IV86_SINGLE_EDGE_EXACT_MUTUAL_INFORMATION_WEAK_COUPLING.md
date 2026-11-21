# IV-86 — Exact single-edge mutual information and weak-coupling singularity

## Scope
Compute the exact ground-state mutual information for the two-spin single-edge transverse-field Ising model as a controlled observable-side check. This is not a derivation of B-C for general graphs.

## Hamiltonian and reduction
H=-J sigma_1^z sigma_2^z-h(sigma_1^x+sigma_2^x), h>0.
The even-parity subspace in the x basis spanned by |++>_x and |-->_x has matrix (up to convention-consistent basis ordering):
[[-2h, -J],[-J, +2h]].
Its lower eigenvalue is -sqrt(4h^2+J^2). The ground state can be written cos(theta)|++>_x + sin(theta)|-->_x with tan(2theta)=J/(2h), sign chosen consistently with J. Schmidt probabilities are p_±=(1±2h/sqrt(4h^2+J^2))/2.

Because the state is pure, I(1:2)=2 S(rho_1)=2[-p_+ ln p_+ - p_- ln p_-] (natural logarithms).

## Weak-coupling asymptotic
Let x=J^2/(16h^2). Then p_small=x+O(x^2), and
I(1:2)=2x[1-ln x]+O(x^2 ln x)
= J^2/(8h^2)[1-ln(J^2/(16h^2))]+O(J^4/h^4 ln(h/|J|)).
This shows the MI is nonanalytic at J=0 in the ordinary Taylor sense (J^2 log J), although it tends continuously to zero. Therefore a response derivative at weak coupling may contain logarithmic terms and cannot be assumed to have a plain power-series expansion without checking the observable definition and graph connectivity.

## Exact formula
I=2 h_2((1+2h/sqrt(4h^2+J^2))/2), where h_2(p)=-p ln p-(1-p)ln(1-p).

## Limitations
Single-edge exact observable only. No general graph expansion, no B-C response identity, no Proposition 0012 proof, and no Lean verification. The asymptotic was derived analytically and is recorded as a warning for subsequent response analysis.
