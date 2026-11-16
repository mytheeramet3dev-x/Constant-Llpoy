# Initial Extraction Ledger
**Project:** Constant Llapoy  
**Document ID:** CL-EL-001  
**Version:** 0.1.0  
**Status:** Initial claim-candidate records created; full extraction and independent completeness review remain open

---

## 1. Summary

The initial extraction pass has inspected the upstream Absolute Symmetry repository and pinned separate branch revisions for Paper A, Paper D, and Paper A1.

| Paper | Source material inspected | Initial Constant Llapoy records | Extraction state |
|---|---|---:|---|
| A | Six authoritative revised sections | 7 | CANDIDATE; partial extraction |
| D | Nine structured theorem/proposition source files | 9 | Candidate/source records; no integrated manuscript |
| A1 | Stage A1-1 theorem statement file | 5 | TRANSCRIBED; independent review pending |
| **Total** | — | **21** | **NOT COMPLETE** |

The seven Paper A records include one definition, one conditional local theorem, and five proposition/claim records. The nine Paper D records include two theorem-source records and seven proposition/theorem-source records. The five Paper A1 records correspond to the five formal theorem statements in Stage A1-1.

## 2. Paper A extraction findings

Source: `Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`.

The integrated Paper A manuscript explicitly says the six revised section files are authoritative. Initial records were created from:
- Section 2.5: conditional exact threshold scaling.
- Section 3.1: interior critical point definition and tangent constraint.
- Section 3.2: conditional local saddle-node normal form.
- Section 3.3: exact Picard local-attractivity criterion.
- Section 4.2: root-by-root scale independence along the dimensionless ray.
- Section 5.2: edge-response sector decomposition and exact `chi_1-chi_2=(N-2)(B-C)` identity.

Records:
- `AS-ALPHA-A-PROP-0001`
- `AS-ALPHA-A-DEF-0001`
- `AS-ALPHA-A-PROP-0002`
- `AS-ALPHA-A-THM-0001`
- `AS-ALPHA-A-PROP-0003`
- `AS-ALPHA-A-PROP-0004`
- `AS-ALPHA-A-PROP-0005`

Important source limitations preserved:
- The local fold result is conditional on regularity and nondegeneracy; model-specific negative curvature is marked open in the source.
- The exact threshold scaling is conditional on interior attainment of the infimum.
- Root scale-independence is root-by-root; it does not prove global uniqueness or branch selection.
- `B-C>0` is explicitly a numerically supported conjecture, not an analytic theorem.
- The upstream Paper A claims ledger contains many additional mixed-scope entries (including project-level Lean source theorems, open proof obligations, numerical claims, retractions, and historical stages). It has not been treated as a complete manuscript claim list.

**Completeness:** NOT COMPLETE. The six sections still require a full assertion-by-assertion scan, proof/dependency extraction, and independent reconciliation against the integrated manuscript and the secondary claims ledger.

## 3. Paper D extraction findings

Source: `Absolute_Sym`, branch `paper-d-singularity`, commit `2678e3f581d707ac57e8a72d3f961fadbba29ade`.

Nine structured source records were found in `papers/paper-d/02-theorems/` and transcribed into Constant Llapoy:
- `AS-ALPHA-D-THM-0001` — quadratic spectral zero entropy asymptotics.
- `AS-ALPHA-D-THM-0002` — candidate local coupling-space entropy singularity at the N=4 symmetric point.
- `AS-ALPHA-D-THM-0003` — global regularity of the N=4 minus-branch zero hypersurface.
- `AS-ALPHA-D-PROP-0001` — entropy regularity hierarchy.
- `AS-ALPHA-D-PROP-0002` — evenness in transverse field for parity-block spectra.
- `AS-ALPHA-D-PROP-0003` — path-connectedness of the P-minus zero set.
- `AS-ALPHA-D-PROP-0004` — strict positivity of the plus-branch coefficient.
- `AS-ALPHA-D-PROP-0005` — exact swap-symmetry zero set.
- `AS-ALPHA-D-PROP-0006` — symmetry-breaking eigenvalue evenness and conditional entropy consequence.

Critical source boundary: the current branch README says the integrated publication-facing manuscript has not yet been consolidated. These nine records are source-level claim candidates, not a complete extraction from a final Paper D manuscript. The file for THM-0002 explicitly labels its result a candidate theorem requiring independent audit. A filename/type mismatch is preserved for THM-0003 because the filename says proposition while the internal heading says theorem.

**Completeness:** BLOCKED for manuscript-level extraction pending an integrated Paper D manuscript and explicit canonical-source designation.

## 4. Paper A1 extraction findings

Source: `Absolute_Sym`, branch `stage-a1-1-repair-review`, commit `b95f5777dfadaf5d31eef27d813ea56c33540d1c`.

Five formal Stage A1-1 theorem statements were transcribed:
- `AS-ALPHA-A1-THM-0001` — compact uniform C0 convergence.
- `AS-ALPHA-A1-THM-0002` — analytic regularity, inflection structure, and unique minimizer of the thermodynamic-limit function.
- `AS-ALPHA-A1-THM-0003` — three-regime uniform bounds, equicoercivity, and Gamma-convergence.
- `AS-ALPHA-A1-THM-0004` — thermodynamic critical-threshold convergence.
- `AS-ALPHA-A1-THM-0005` — separated critical-location convergence.

The upstream README says Stage A1-1 is complete (repaired) and Stage A1-2 is pending. The separate Stage A1-1 claim ledger reports 17 epistemic entries across proven, numerical, incomplete, conjectural, unverified, and incorrect categories. Those 17 entries are not all theorem statements and must not be relabelled as proved. The source's PROVEN labels have not been independently re-proved by Constant Llapoy.

**Completeness:** PARTIAL. Five formal Stage A1-1 theorem statements are transcribed; the 17-row claim ledger, supporting definitions, assumptions, appendices, and any later A1 stages still require reconciliation.

## 5. Record status and what has not been done

- Initial source branches and commits: recorded.
- Individual claim-source records created: 21.
- Independent extraction review: NOT_RUN.
- Mathematical proof re-derivation: NOT_RUN.
- Lean formalization correspondence: NOT_RUN.
- Axiom/TCB audit per claim: NOT_RUN.
- Dependency closure and circularity analysis: NOT_RUN.
- Full manuscript completeness: NOT_ESTABLISHED.
- Any Constant Llapoy VERIFIED claim: NONE.

## 6. Next extraction operations

1. Complete the Paper A scan across all six canonical sections and reconcile every claim-bearing statement with `Arxiv/claims_ledger.md`.
2. Resolve Paper D's integrated manuscript source; until then, keep source theorem records separate from manuscript claims.
3. Expand Paper A1's 17-entry ledger into separately classified claim records, preserving negative and incorrect entries.
4. Create claim-level dependency graphs and Verification Obligation Matrix rows only after exact statement and source reconciliation.
5. Perform independent extraction review before changing any CANDIDATE/TRANSCRIBED record to REGISTERED.

---

**End of initial extraction ledger.**
