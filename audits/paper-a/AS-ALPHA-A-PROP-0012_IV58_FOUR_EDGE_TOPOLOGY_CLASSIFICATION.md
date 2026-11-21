# IV-58 — Four-Edge Topology Classification and Completeness Ledger

**Status:** STRUCTURAL CLASSIFICATION FRAMEWORK DERIVED / FULL ENUMERATION OPEN  
**Scope:** Four pair-flip operations, support multigraphs, endpoint flipped sets, and denominator-singularity flags.

## 1. Endpoint parity invariant

Represent an ordered four-operation path by edges \(e_1,e_2,e_3,e_4\), where each edge is a pair of distinct vertices. Starting at the vacuum, the endpoint flipped set is

\[
S_4=e_1\triangle e_2\triangle e_3\triangle e_4.
\]

Equivalently, \(S_4\) is the set of vertices of odd degree in the four-edge multigraph (multiplicity counted). This exact parity identity implies \(|S_4|\in\{0,2,4,6,8\}\).

## 2. Multiplicity/support ledger

Multiplicity partitions of four edge occurrences are:

- \(4\): one edge repeated four times;
- \(3+1\): one edge tripled, a second used once;
- \(2+2\): two edges each used twice;
- \(2+1+1\): one doubled edge and two single edges;
- \(1+1+1+1\): four distinct edges.

This list exhausts multiplicity partitions, but each pattern must still be refined by support-graph isomorphism type, connected components, vertex count, and adjacency. We do not claim those refinements are exhaustively enumerated here.

## 3. Required per-path ledger

For each ordered edge sequence, record:
1. edge sequence and multiplicity pattern;
2. support graph and connected components;
3. vertex degrees and parity endpoint \(S_4\);
4. intermediate sets \(S_1,S_2,S_3\);
5. gaps \(E(S_k)-E_0=2h|S_k|\);
6. whether any intermediate state is vacuum (zero denominator in naïve nondegenerate formula);
7. target-set aggregation key;
8. perturbation convention and reducible-path/normalization corrections.

Paths with the same endpoint must be aggregated at amplitude level under a common convention; squared magnitudes cannot generally be added independently because interference is possible.

## 4. Completeness and limits

The multiplicity partition list is exhaustive for four edge occurrences. The support-graph refinement, ordered path enumeration, coefficient aggregation, normalization, and fourth-order reduced-density reconstruction remain undone. Thus IV-58 is an exhaustive multiplicity-partition classification, not a complete four-edge topology proof.

## 5. Disposition

- Four-operation multiplicity partitions: **DERIVED / EXHAUSTIVE**.
- Endpoint odd-degree parity rule: **DERIVED**.
- Endpoint flip-count bound: **DERIVED**.
- Complete support topology enumeration: **OPEN**.
- Ordered path and denominator ledger: **OPEN**.
- Reducible-path corrections and normalized amplitudes: **OPEN**.
- Direct coefficient \(c_{vv}\): **OPEN**.
- Lean verification: **NOT PERFORMED**.

This report intentionally does not overstate a bookkeeping framework as a verified fourth-order result.
