# IV-81 — General-graph fourth-order coefficient framework (independent derivation)

## Scope
Derive a coefficient-level organization for fourth-order perturbation theory on a finite simple loopless graph G=(V,E), keeping raw closed walks and complete recurrence corrections distinct. This is an organizing framework; no arbitrary-graph closed formula is claimed.

## Hamiltonian and basis
H0=-h sum_v sigma_v^x, h>0; V=-sum_e J_e sigma_u^z sigma_v^z. The x-basis ground state is represented by mask S=empty. A perturbing edge e={u,v} toggles S to S triangle {u,v}. For a sequence e1...ek define S_t={v: incidence count of v among e1...et is odd}. The unperturbed gap is Delta(S_t)=2h|S_t|.

## General coefficient formula from the complete recurrence
Use intermediate normalization and define c_k(S) as coefficient of lambda^k in ground-state wavefunction on nonempty mask S. Then:
c_0(empty)=1; c_k(empty)=0 for k>=1.
E_k = (V c_{k-1})(empty).
For nonempty S:
c_k(S)= -1/(2h|S|) * [ (V c_{k-1})(S) - sum_{j=1}^{k-1} E_j c_{k-j}(S) ].
Here (V c)(S)=-sum_e J_e c(S triangle e).
This recurrence is exact, finite, and graph-independent, but is not yet a closed combinatorial coefficient formula.

## Closed fourth-order raw-chain organization
For an ordered 4-tuple (e1,e2,e3,e4), let S_t be its prefix toggle set. A raw Q-resolvent chain contributes only when S1,S2,S3 are all nonempty and S4=empty. Its weight is:
- J_e1 J_e2 J_e3 J_e4 / [8 h^3 |S1||S2||S3|]
with a negative sign (since V contributes four negative signs and three resolvents negative signs: overall raw-chain sign is negative).
The complete E4 additionally includes recurrence/reducible terms involving E2 and state corrections. Do not equate raw-chain sum with E4.

## Parity closure and finite graph structure
Vacuum return S4=empty iff every vertex has even degree in the edge-occurrence multigraph formed by e1...e4. For a simple loopless graph, closed 4-edge occurrence multisets can be:
- one edge repeated 4 times,
- two distinct edges each repeated twice,
- four distinct edges forming a 4-cycle.
However, raw Q-chain exclusions remove patterns with vacuum at an intermediate prefix. Thus closure classifies endpoint, not raw-chain validity.

## Four-edge raw-chain classes (recap)
- Adjacent 2+2: four valid permutations; denominator product 64h^3; raw aggregate -1/16.
- Disjoint 2+2: four valid permutations; denominator product 128h^3; raw aggregate -1/32.
- Distinct C4: 16 permutations with prefix sizes (2,2,2), 8 with (2,4,2); aggregate raw coefficient -5/16.
- e^4: no valid non-vacuum raw chain because S2=empty. Its contribution in full E4 is recurrence-generated and must not be counted in raw-chain sum.

## Verification obligations for any implementation
1. Correctly apply edge toggles by XOR.
2. Preserve distinct edge identities for monomial bookkeeping.
3. Exclude vacuum from all Q-resolvent denominators.
4. Apply lower-order recurrence correction terms before reading E4.
5. Normalize and combine symbolic monomials exactly.
6. Cross-check on one-edge, triangle, square, and at least one additional graph.
7. Separate machine checks from analytic proof and Lean verification.

## Status
The recurrence is exact as stated for the finite graph under this Hamiltonian convention. The raw fourth-order classification is an independently derived organization. General-graph complete E4 closed form is not yet derived; no B-C response or Proposition 0012 verification is claimed.
