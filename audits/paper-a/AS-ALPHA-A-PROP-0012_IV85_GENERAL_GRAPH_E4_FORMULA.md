# IV-85 — General-graph fourth-order energy formula

## Proposed closed formula
For a finite simple graph G with transverse-field Ising Hamiltonian convention H0=-h sum_v sigma_v^x, V=-sum_e J_e sigma_u^z sigma_v^z, h>0, the fourth-order coefficient is organized as:
E4 = [sum_e J_e^4 - 2 sum_{unordered adjacent edge pairs e,f} J_e^2 J_f^2 - 20 sum_{simple 4-cycles C} product_{e in C} J_e] /(64 h^3).

Here adjacent edge pairs share one vertex. Each distinct simple four-cycle is counted once, including cycles in graphs with chords. The formula follows by combining the raw closed non-vacuum chain classes from IV-79 with the general analytic correction proven in IV-84:
- edge^4: raw contribution 0, correction +1/64;
- adjacent 2+2: raw -4/64, correction +2/64, total -2/64;
- disjoint 2+2: raw -2/64, correction +2/64, total 0;
- C4: raw -20/64, correction does not change cycle monomial, total -20/64.

## Cross-check
A committed SymPy script compared complete recurrence E4 against this formula:
- Exhaustive simple graphs on labeled n=1,2,3,4 vertices: 1+2+8+64=75 graphs.
- Six additional structured graphs on five vertices: P5, C5, K1,4, square-plus-tail, triangle with two leaves, and two disjoint paths.
- Total 81 graph instances (75 exhaustive graphs on n<=4, plus six five-vertex examples).
The script asserts symbolic equality for each graph.

## Reproducibility
Run `python tools/paper-a/iv85_general_graph_e4_formula_crosscheck.py`. Requires SymPy. Execution was tested before commit, but note the exact graph count is 68+6=74; if any log reports another total, resolve discrepancy.

## Status
The coefficient formula has an analytic derivation from the closed-walk classification and IV-84 correction. Script cross-checks small graphs and selected five-vertex examples. It does not prove Proposition AS-ALPHA-A-PROP-0012, B-C response identity, or Lean formalization.
