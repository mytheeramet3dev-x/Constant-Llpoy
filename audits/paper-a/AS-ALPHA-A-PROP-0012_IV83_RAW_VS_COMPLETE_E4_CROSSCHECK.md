# IV-83 — Raw-chain versus complete fourth-order energy cross-check

## Result
A symbolic SymPy script computes both (i) the raw four-edge closed Q-resolvent chain sum with all three prefixes nonempty, and (ii) complete intermediate-normalized E4 recurrence, for six finite graph examples. In all six cases the difference E4_complete - E4_raw equals (sum_e J_e^2)^2/(64 h^3). This is a reproducible finite-example pattern, NOT a proved general theorem.

## Example table
| Graph | Raw valid ordered chains | Raw denominator size patterns |
|---|---:|---|
| Single edge | 0 | none |
| Triangle | 12 | (2,2,2): 12 |
| Square C4 | 48 | (2,2,2): 32; (2,4,2): 16 |
| Path P4 (3 edges) | 12 | (2,2,2): 8; (2,4,2): 4 |
| Star K1,3 | 12 | (2,2,2): 12 |
| Two disjoint edges | 4 | (2,4,2): 4 |

## Reproducibility
Run `python tools/paper-a/iv83_raw_vs_complete_e4_crosscheck.py`. Requires SymPy. Script asserts for each graph that complete E4 minus raw chain sum equals the squared edge-coupling sum squared over 64 h^3. The script was executed in the analysis environment before commit; its assertions passed for all six graphs.

## Observed correction identity
For these examples:
E4_complete - E4_raw = (sum_e J_e^2)^2/(64 h^3).

This is a candidate general identity to prove analytically. No arbitrary-graph proof is claimed. No B-C response, proposition AS-ALPHA-A-PROP-0012, or Lean verification is claimed.
