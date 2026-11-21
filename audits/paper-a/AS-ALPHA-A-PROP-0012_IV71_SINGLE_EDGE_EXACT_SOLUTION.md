# IV-71 — Single-edge exact solution and fourth-order coefficient

## Scope
Independent analytic check of the one-edge Ising Hamiltonian H=-h(σ_1^x+σ_2^x)-Jσ_1^zσ_2^z, h>0.

## Exact spectrum / ground energy
In the even-parity subspace spanned by |++>_x and |-->_x, the Hamiltonian matrix has diagonal entries -2h,+2h and off-diagonal -J. The lower eigenvalue is
E(J)=-sqrt(4h^2+J^2).
The other parity block does not yield a lower eigenvalue for h>0, so this is the ground-state branch.

## Taylor expansion
E(J)=-2h-J^2/(4h)+J^4/(64h^3)-J^6/(512h^5)+O(J^8).

Thus E_2=-J^2/(4h), E_4=+J^4/(64h^3). This verifies the fourth-order coefficient for the one-edge graph analytically.

## Intermediate-normalized ground-state amplitude
With |ψ>=|++>_x+c|-->_x and <++|ψ>=1,
c=J/(sqrt(4h^2+J^2)+2h)
=J/(4h)-J^3/(64h^3)+J^5/(1024h^5)+O(J^7).

## Limits
This is a single-edge exact check only. It does not prove the general graph fourth-order formula, the fourth-order vacuum-return correction, or Proposition 0012. No Lean verification is claimed.
