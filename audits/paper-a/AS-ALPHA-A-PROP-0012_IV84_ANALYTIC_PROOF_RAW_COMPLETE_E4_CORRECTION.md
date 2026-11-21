# IV-84 — Analytic proof of the raw-to-complete fourth-order correction

## Claim
For a finite simple graph with H0=-h sum_v sigma_v^x, h>0, V=-sum_e J_e sigma_u^z sigma_v^z, using intermediate-normalized nondegenerate perturbation theory:
E4_complete = E4_raw + (sum_e J_e^2)^2/(64 h^3),
where E4_raw is the four-operation closed Q-resolvent chain with all three intermediate states non-vacuum. This identity is proven below under the stated convention; it is not an arbitrary-graph closed form for E4_raw.

## Definitions
Let |0> be the all-+x ground state, P=|0><0|, Q=I-P, R0=Q(E0-H0)^(-1)Q. For a two-vertex edge-flip state |e>, its gap is 4h and R0|e>=-|e>/(4h). In intermediate normalization |psi(lambda)>=|0>+lambda c1+lambda^2 c2+lambda^3 c3+..., with Q ck=ck.

## Recurrence through the required order
E1=<0|V|0>=0.
c1=R0 Q V|0>.
E2=<0|V|c1>.
c2=R0 Q V c1 (because E1=0).
c3=R0 Q (V c2-E2 c1) (E1=0; the E3|0> term is removed by Q).
Therefore:
E4=<0|V|c3>
=<0|V R0 Q V R0 Q V R0 Q V|0> - E2 <0|V R0 Q c1>.
The first term is exactly E4_raw under the raw-chain definition.

## Evaluate correction
For each edge e, V|0> has coefficient -J_e on its edge-flip state. Applying R0 gives c1|e>=J_e/(4h). Applying R0 again gives R0 c1|e>=-J_e/(16h^2). Applying V from that edge state back to vacuum contributes -J_e. Summing over edges:
<0|V R0 Q c1>=sum_e J_e^2/(16h^2).
Also E2=-sum_e J_e^2/(4h).
Thus the recurrence correction is
-E2 <0|V R0 Q c1>
= (sum_e J_e^2)/(4h) * (sum_e J_e^2)/(16h^2)
= (sum_e J_e^2)^2/(64h^3).

Hence the claim follows:
E4_complete=E4_raw+(sum_e J_e^2)^2/(64h^3).

## Assumptions and limits
Finite graph, simple edges, transverse-field Ising convention above, h>0, nondegenerate H0 ground state, intermediate normalization. This is an analytic derivation of the correction identity, not a proof of a closed formula for raw E4 on all graphs. It does not prove mutual-information response B-C, Proposition AS-ALPHA-A-PROP-0012, or Lean formalization. IV-83 finite-example checks are corroborating tests, not premises.
