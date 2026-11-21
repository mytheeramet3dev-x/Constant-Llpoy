# IV-80 — Independent complete fourth-order recurrence cross-check

## Goal
Independently reconstruct perturbative energy coefficients through fourth order for finite simple graphs, using intermediate-normalized state recurrence, and compare with selected earlier audit formulas. This is a symbolic computation cross-check, not a proof of Proposition 0012.

## Convention
H0=-h sum_v sigma_v^x, h>0; V=-sum_edges J_e sigma_u^z sigma_v^z. In the x-basis, a state is represented by a flip mask S, with gap 2h|S|. Intermediate normalization: <0|psi(lambda)>=1; psi_k has no vacuum component. E(lambda)=E0+sum lambda^k E_k, psi=lambda series.

Recurrence:
E_k=<0|V|psi_{k-1}>
psi_k=R0 Q [V psi_{k-1}-sum_{j=1}^{k-1} E_j psi_{k-j}],
where R0 on a nonempty mask S multiplies by -1/(2h|S|).

The committed script performs symbolic propagation using SymPy for single-edge, triangle, and square graphs.

## Results (script execution in analysis session)
### Single edge
E1=0, E2=-J^2/(4h), E3=0, E4=+J^4/(64h^3). This confirms IV-78 was wrong to classify the four-repeated-edge sequence as a raw Q-resolvent chain: the positive E4 arises from the complete recurrence, not that invalid raw chain.

### Triangle (J0,J1,J2)
E2=-(J0^2+J1^2+J2^2)/(4h)
E3=-3J0J1J2/(8h^2)
E4=(J0^4+J1^4+J2^4-2J0^2J1^2-2J0^2J2^2-2J1^2J2^2)/(64h^3).
This agrees with corrected IV-72.

### Square C4 (cyclic edges J0,J1,J2,J3)
E2=-(J0^2+J1^2+J2^2+J3^2)/(4h), E3=0.
E4=[sum_i J_i^4 -2(J0^2J1^2+J1^2J2^2+J2^2J3^2+J3^2J0^2)-20J0J1J2J3]/(64h^3).
This agrees with IV-76; opposite-edge terms cancel.

## Reproducibility
Run: python tools/paper-a/iv80_complete_fourth_order_recurrence.py
Dependency: SymPy.

## Execution results
The symbolic run produced:
- Single edge: [0, -J0^2/(4h), 0, J0^4/(64h^3)]
- Triangle: [0, -(J0^2+J1^2+J2^2)/(4h), -3J0J1J2/(8h^2), triangle E4 above]
- Square: [0, -sum(J_i^2)/(4h), 0, square E4 above].

## Status
Computational/analytic evidence for three finite examples only. No arbitrary-graph proof, response B-C proof, proposition AS-ALPHA-A-PROP-0012 proof, or Lean verification is claimed.
