# IV-68 — Exhaustive Fourth-Order Edge-Sequence Enumeration (Audit Design and Independent Calculation)

## Status
**ANALYTIC-PARTIAL.** This file defines the finite sequence audit and records a corrected algebraic finding from IV-67. No repository script execution, external independent run, or Lean proof is asserted in this report.

## 1. Edge-operation sequences
For a finite simple graph with edge set E, consider ordered 4-tuples (e1,e2,e3,e4) in E^4. For each tuple define the intermediate vertex flip sets
S_k = e1 △ e2 △ ... △ ek, for k=1,2,3,4.
Vacuum return is equivalent to S4=∅. Reduced-resolvent chains require Sk ≠ ∅ at every intermediate k=1,2,3.

Each nonempty flip set S has energy gap Δ(S)=2h|S| and resolvent diagonal value −1/(2h|S|).

## 2. Correct fourth-order recurrence result
With intermediate normalization, E1=0, E2=<0|V R0 V|0>, E3=<0|V R0 V R0 V|0>, and the fourth-order energy is
E4 = <0|V R0 V R0 V R0 V|0> − E2 <0|V R0^2 V|0>.
This subtraction is not generally E2^2. The R0^2 matrix element is required by the state recurrence. IV-67's two-spin check is consistent with E4=+J^4/(64h^3).

## 3. Audit fields per sequence
The enumeration must record:
- ordered edge tuple
- multiplicity/canonical multigraph support
- S1, S2, S3, S4
- intermediate gaps Δ1, Δ2, Δ3 (only for nonempty S)
- vacuum-return flag (S4=empty)
- reducible flag (any S2 or S3 empty)
- irreducible-chain admissibility (all S1,S2,S3 nonempty)
- chain denominator product and signed operator coefficient
- edge-coupling monomial

## 4. Finite combinatorial criterion
Vacuum-return sequences are precisely tuples whose every vertex occurs an even number of times among the four edges. Do not infer the class solely from a visual graph shape; verify parity from the tuple.

## 5. Required checks before results are called verified
1. Independent implementation of flip sets using bitmasks.
2. For small graphs, compare exact tuple enumeration with a second implementation using edge incidence parity vectors.
3. Confirm counts: total tuples |E|^4; each tuple appears exactly once; endpoint parity agrees between implementations.
4. Check resolvent denominator products only for nonempty intermediate states; vacuum intermediates must be treated via recurrence/subtraction rather than division.
5. Compare fourth-order coefficient against symbolic expansion or exact diagonalization on small graphs (single-edge graph, triangle, square, and a graph with disjoint edges).
6. Preserve OPEN status until the checks are executed and independently reviewed.

## 6. Scope limitation
This audit is a bookkeeping specification and recurrence correction, not a proof of the target mutual-information derivative or weak-coupling edge-response proposition.