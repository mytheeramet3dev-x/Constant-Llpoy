# IV-74 — General fourth-order walk formula and correction

## Setup
H=H0+V, H0=-h sum_i sigma_i^x, V=-sum_e J_e sigma_i^z sigma_j^z, h>0, with nondegenerate product ground state |0>. A state indexed by nonempty flip set S has positive excitation gap Delta(S)=2h|S|. Vacuum is excluded from reduced resolvent denominators.

## Recorded expressions
Raw closed four-edge walk term:
E4_raw=-sum over ordered e1,e2,e3,e4 returning to vacuum with S1,S2,S3 nonempty of (J_e1 J_e2 J_e3 J_e4)/(Delta(S1)Delta(S2)Delta(S3)).

Recorded correction:
E4_corr=(sum_e J_e^2)^2/(64h^3).

The expression is conditional on the stated convention and E1=0; it is not yet verified for arbitrary graphs in this recovered note.

## Required remaining checks
Derive the correction directly from the complete intermediate-normalized recurrence; check coefficients and signs against exact small-graph diagonalization and independently enumerated path sums; handle all reducible vacuum returns; test graph families; no Lean proof is claimed. This is a working analytic record, not a closed theorem.