# IV-62 — Intermediate-State Denominator Ledger and Vacuum-Return Path Grouping

## Scope
Exhaustively enumerate unique ordered four-edge operation sequences over the 28 pair edges on an 8-vertex pool. For each sequence, track the flipped set after operations 1–3 and the unperturbed energy gap ΔE=2h|S|. Histograms are counts of ordered sequences, not amplitudes.

## Executed results
- Ordered sequences: 614,656.
- All three intermediate denominators nonzero: 583,296.
- At least one vacuum intermediate (step 2 or 3): 31,360.
- Step 1: ΔE/h = 4 for all 614,656 sequences.
- Step 2: ΔE/h histogram: 0:21,952; 4:263,424; 8:329,280.
- Step 3: ΔE/h histogram: 0:9,408; 4:205,408; 8:329,280; 12:70,560.

## Nonzero intermediate-gap triples (ΔE/h)
| Gap triple | Sequence count |
|---|---:|
| (4,4,4) | 112,896 |
| (4,4,8) | 141,120 |
| (4,8,4) | 70,560 |
| (4,8,8) | 188,160 |
| (4,8,12) | 70,560 |
| **Total** | **583,296** |

The histogram count for zero gap at step 2 plus step 3 is 21,952 + 9,408 = 31,360; no sequence is double-counted because a four-edge sequence that returns to vacuum at step 2 cannot return to vacuum again at step 3 under this enumeration of nonempty pair edges. This total matches IV-60/IV-61 vacuum-intermediate count.

## Denominator interpretation
For an intermediate flip set S, ΔE(S)=2h|S|. In a conventional non-vacuum sequential resolvent term, each of the three intermediate energy denominators therefore has magnitude proportional to ΔE; the listed gap triples identify denominator classes. The sign convention and prefactors depend on the perturbation/resolvent convention and are not assigned here. Zero-gap cases are singular in this naive sequential denominator product and are flagged as reducible/vacuum-return candidates; they are **not** simply discarded, subtracted, or corrected in this audit.

## Limits
This is path-state/denominator bookkeeping only. It does not calculate coupling-weighted sums, signs, reducible corrections, normalization terms, fourth-order reduced density-matrix entries, mutual information, response B-C, or a Lean proof.

**Paper A status: OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
