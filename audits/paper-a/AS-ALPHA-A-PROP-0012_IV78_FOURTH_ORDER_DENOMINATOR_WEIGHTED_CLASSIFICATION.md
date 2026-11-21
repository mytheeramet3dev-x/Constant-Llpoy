# IV-78 — Denominator-weighted fourth-order vacuum-return classification

## Scope and convention
Simple loopless graph, transverse-field Ising Hamiltonian H0=-h sum_i sigma_i^x (h>0), perturbation V=-sum_e J_e sigma_i^z sigma_j^z. Four edge operations are ordered. Flip sets update by symmetric difference. For nonempty intermediate flip set S, gap Delta(S)=2h|S|. Raw fourth-order closed-walk term carries a minus sign and denominator product Delta(S1)Delta(S2)Delta(S3). This audit classifies the raw walk weights only; it does not replace the full recurrence's vacuum-return subtraction/correction.

## Class I: one edge repeated four times
For e,e,e,e, all three intermediate flip sets equal the two endpoints of e, each gap 4h. Denominator product 64h^3. One order, raw contribution -J_e^4/(64h^3).

## Class II: two distinct edges each repeated twice
There are six orders of e,e,f,f; two start with identical edges and return to vacuum after operation 2, so they are excluded from the non-vacuum raw resolvent chain. Four valid orders remain.

### Adjacent edges
If e and f share one vertex, every valid order has |S1|=|S2|=|S3|=2, so each denominator product is 64h^3. Summing four valid orders gives raw coefficient -4/64=-1/16:
E4_raw contribution = -J_e^2 J_f^2/(16h^3).

### Disjoint edges
If e and f are disjoint, valid orders have |S1|=2, |S2|=4, |S3|=2, giving denominator product (4h)(8h)(4h)=128h^3. Four valid orders sum to coefficient -4/128=-1/32:
E4_raw contribution = -J_e^2 J_f^2/(32h^3.

## Class III: four distinct edges forming a simple C4
There are 24 permutations. For the first two edges:
- Adjacent pair: 16 orders (four ordered adjacent choices for first pair, then two orders of remaining edges). Their flip-set sizes are (2,2,2), denominator product 64h^3.
- Opposite pair: 8 orders (two ordered opposite choices, then two orders of remaining edges). Their sizes are (2,4,2), denominator product 128h^3.
All third intermediate states have size 2.
Weighted sum coefficient: -(16/64+8/128)=-5/16, so the raw cycle monomial contribution is -5 J_e J_f J_g J_k/(16h^3.

## Check against recorded square raw polynomial
For a,b,c,d around C4, the cycle term is -5abcd/(16h^3)=-10abcd/(32h^3, matching the corrected IV-75/IV-76 raw polynomial cycle coefficient.

## Limits and status
This confirms denominator-weighted raw walk coefficients for the three vacuum-return multiset classes under the stated simple-graph convention. It does not derive the complete fourth-order energy correction, normalization/reducible subtraction, arbitrary-graph aggregate polynomial, reduced density matrix, B-C response, Proposition 0012, or Lean verification. Analytic combinatorial audit; no code runtime or numerical diagonalization claimed.
