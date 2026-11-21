# IV-59 — Support-Graph Isomorphism Classification Framework

**Status:** GRAPH-THEORETIC FILTERS DERIVED / FULL CLASSIFICATION OPEN  
**Scope:** Undirected simple support graphs formed from four pair-edge operations, with multiplicity retained separately.

## 1. Separate support graph from multiplicity

Given four edge occurrences, define the support graph by retaining each distinct edge once. It is a simple graph (no loops, because each pair flip connects two distinct spins) with between one and four support edges. The multiplicity function on support edges sums to four.

For fixed multiplicity pattern, support graphs are considered equivalent only under vertex relabeling (graph isomorphism); order of operations is not part of support graph and must remain in the separate ordered-path ledger.

## 2. Degree/parity and endpoint filters

The endpoint flipped set is determined by odd multiplicity-degree in the multigraph, equivalently by the parity of the sum of support-edge multiplicities incident to each vertex. The sum of degrees is eight, so the number of odd-degree vertices is even and at most eight. For the support graph, degree sequence alone is not a complete isomorphism invariant; distinct graphs may share it.

## 3. Support graph buckets by edge count

The support graph has 1, 2, 3, or 4 distinct edges.

- **1 edge:** a single edge, multiplicity four.
- **2 edges:** support must be either adjacent (a 2-edge path) or disjoint (two components); multiplicity partitions 3+1 or 2+2 can both appear depending assignment.
- **3 edges:** support types include a 3-edge path, a 3-edge star, a triangle, and a disconnected path-plus-edge. This is a preliminary list of common types; exact admissibility depends on multiplicity placement and this list is not claimed exhaustive as written.
- **4 edges:** support graph may be connected or disconnected; the complete isomorphism-class list has not been generated here.

## 4. Required canonicalization

A reproducible exhaustive classification should define a canonical encoding for each labeled support graph (e.g., minimum adjacency encoding across all vertex permutations for the fixed small vertex count), then deduplicate by that encoding. Multiplicity assignments must be canonicalized jointly with the support graph, and operation order must be enumerated afterward rather than erased.

## 5. Disposition

- Support/multiplicity distinction: **DERIVED**.
- One-edge support: **CLASSIFIED**.
- Two-edge support types (adjacent/disjoint): **CLASSIFIED**.
- Three-edge bucket: **PARTIAL; not claimed exhaustive**.
- Four-edge support isomorphism classes: **OPEN**.
- Canonical encoding procedure specified conceptually; no code or enumeration run.
- Complete ordered paths, denominator treatment, normalization, and \(c_{vv}\): **OPEN**.
- Lean verification: **NOT PERFORMED**.

This report is a classification framework and partial catalog, not a complete topology enumeration.
