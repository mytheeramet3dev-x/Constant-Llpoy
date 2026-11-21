# IV-79 — Raw fourth-order coefficient classification and IV-78 correction

## Scope and convention
For H0=-h sum_v sigma_v^x (h>0), V=-sum_e J_e sigma_i^z sigma_j^z, a four-edge ordered walk updates its flipped-vertex set by symmetric difference. The raw resolvent chain includes only sequences with all three intermediate sets nonempty and final set empty. Each denominator is Delta(S)=2h|S|; thus a valid sequence contributes -1/[8h^3 |S1||S2||S3|] times its edge monomial.

## Correction to IV-78
IV-78 incorrectly included e,e,e,e as a valid raw non-vacuum-intermediate chain. It is NOT valid: after the second operation the flip set is empty, so the second intermediate denominator is zero and the sequence is excluded from the Q-resolvent raw chain. Its four-edge multiset has no valid raw chain. Any physical fourth-order J_e^4 term must arise through the complete perturbation recurrence/reducible correction, not from this raw chain. The IV-78 single-edge statement is therefore withdrawn.

## Closed four-edge multiset classification
For loopless simple graphs, edge-multisets with four occurrences that return to the vacuum and have non-vacuum intermediate sets fall into:
1. Two distinct edges each repeated twice, adjacent: 4 valid ordered sequences, sizes (2,2,2), aggregate coefficient -4/(8*2*2*2)=-1/16; monomial contribution -J_e^2 J_f^2/(16h^3.
2. Two distinct edges each repeated twice, disjoint: 4 valid ordered sequences, sizes (2,4,2), aggregate coefficient -4/(8*2*4*2)=-1/32; contribution -J_e^2 J_f^2/(32h^3.
3. Four distinct edges forming a C4: 24 valid orders; 16 have sizes (2,2,2), 8 have sizes (2,4,2). Aggregate coefficient -[16/(8*2*2*2)+8/(8*2*4*2)]=-5/16; contribution -5 J_eJ_fJ_gJ_k/(16h^3.

No other four-edge multiset returns to vacuum: endpoint closure is even incidence at each vertex. Patterns with an edge appearing 4 times or 3+1 are not valid non-vacuum-intermediate closed raw chains; the two-distinct-edge 2+2 and distinct-edge C4 are the surviving classes.

## Exhaustive labeled-pool enumeration (analytic script in session; not committed)
Pool of 8 vertices, 28 possible edges, multisets of 4 edges with repetition: 31,465. Closed edge-occurrence parity patterns classified into three classes:
- adjacent 2+2 edge pairs: 168 labeled multisets;
- disjoint 2+2 edge pairs: 210;
- C4 with four distinct edges: 210;
total valid closed raw-chain multiset count: 588.
This count was obtained by enumerating edge multisets and unique permutations, checking flip-set closure and excluding vacuum at all three intermediate positions. The enumeration was performed as an analysis calculation; no script or machine-generated artifact is committed, and no independent runtime/numerical/Lean verification is claimed.

## Status and limitation
This corrects IV-78. These are raw non-vacuum resolvent-chain coefficients only, not the complete fourth-order energy correction. Complete recurrence/reducible corrections, general graph energy polynomial, reduced density matrix/response B-C, proposition AS-ALPHA-A-PROP-0012, and Lean remain open/unverified.
