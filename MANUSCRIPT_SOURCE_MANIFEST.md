# Manuscript Source Manifest
**Project:** Constant Llapoy  
**Document ID:** CL-MSM-001  
**Version:** 0.2.3  
**Status:** Core source revisions frozen; supplementary and supporting proof-source inventory added; mathematical verification not established

---

## 1. Purpose and source policy

This manifest pins the exact upstream source revisions used for the initial Paper A, Paper D, and Paper A1 claim-candidate extraction.

A branch name is not a stable source identity. Each entry therefore records its resolved commit SHA. Blob SHAs identify individual files at that revision.

This manifest distinguishes:
- authoritative source files explicitly designated by the upstream repository;
- structured theorem/claim source records;
- secondary ledgers and indexes;
- provisional or historical manuscript drafts that are not the current authoritative source.

No title, claim, or source is promoted to final status merely because a file exists.

## 2. Paper A source freeze

| Field | Value |
|---|---|
| Upstream repository | `mytheeramet3dev-x/Absolute_Sym` |
| Branch | `paper-a-interval-audit-2026-11-14` |
| Frozen commit | `8deb7de4a49cb2060720246b7101820ee7e08c91` |
| Commit date | 2026-11-14T13:40:34Z |
| Manuscript identity | Paper 1 / Paper A |
| Working title | Bifurcation Structure and Saddle-Node Dynamics in Self-Consistent Quantum Entanglement Networks |
| Canonical source policy | The integrated manuscript states that the six revised section files are the authoritative manuscript text. |
| Integrated manuscript (cross-check only) | `Arxiv/paper_01_manuscript.md`, blob `ec2361c1ae17b955e845ec1726636795cc3b74ff` |
| Secondary claim index | `Arxiv/claims_ledger.md`, blob `7a9eadbf363b75fe29088ad3c5443e145779316c` |

### Authoritative section files

| Section | Path | Blob SHA |
|---|---|---|
| 1 | `Arxiv/paper_01_section_01_revised.md` | `1f7857bcd44e1605900bf71193e9b593a62397bd` |
| 2 | `Arxiv/paper_01_section_02_revised.md` | `541382fa7ab4b9e254c8e7e5158f202c1a975e0d` |
| 3 | `Arxiv/paper_01_section_03_revised.md` | `9ac164ac67cc121af212c4fb7268b809d9234bd6` |
| 4 | `Arxiv/paper_01_section_04_revised.md` | `a7570431eac62dd4555194df283edb5a9c87a28d` |
| 5 | `Arxiv/paper_01_section_05_revised.md` | `671c97fa68fa48c929760bf9956d197b358c4904` |
| 6 | `Arxiv/paper_01_section_06_revised.md` | `5e734065c2ddd42ee602dada89e7455d2ad9e7a0` |

The six section files, not the integrated manuscript alone, govern the initial Paper A extraction. The existing claims ledger is a secondary index and contains mixed mathematical, numerical, project-stage, and Lean-source entries; it must not be imported wholesale as a list of manuscript theorems.


### Supporting and supplementary sources inspected at the same frozen commit

These files are **not** authoritative replacements for the six revised sections. They are separately inventoried supporting material whose declared status and proof dependencies must be reconciled.

| Path | Blob SHA | Scope / treatment |
|---|---|---|
| `Arxiv/supplementary_material.md` | `cdead5041ba89f239b3051bcca41ccfae005a349` | Supplementary numerical protocol, finite data, solver checks, and exact sector-identity derivation |
| `docs/tfim_ground_state_simplicity_lemma.md` | `472328b596ccdcc82ece65faf5ef65a9dab63e50` | Candidate corrected Perron–Frobenius proof for ground-state simplicity |
| `docs/lemma_5_1_proof.md` | `db2c552f2d9bea663b20e05aefdc5447d2494a7b` | Proposed strong-coupling (B-C) positivity proof; derivative remainder remains open |
| `docs/lemma_5_2_proof.md` | `4c1b70a7233f470ca46adaafe59868b2e0779253` | Original weak-coupling negative-sign derivation; superseded by its audit |
| `docs/lemma_5_2_audit.md` | `a5e47defd859b4eb5ed5e63d65d12eeff320f9c7` | Corrected weak-coupling sign calculation; derivative remainder remains open |
| `docs/entropy_schur_remainder_lemma.md` | `ef404349c6effa7f13bb14b5cc24f45e3ce6b80e` | Conditional entropy derivative estimate requiring model-specific Schur bounds |
| `STRONG_COUPLING_PROOF_RECONCILIATION.md` | `8b75e3790cd0aaa223a2ffbbdbaedb2b6f50afbc` | Forensic status reconciliation; strong-coupling derivative proof not closed |

The supporting-source reconciliation is recorded in `PAPER_A_SUPPORTING_SOURCE_RECONCILIATION.md`. In particular, the located Lemma 5.1 concerns (B-C), not the (mathcal G_N(x)) asymptotic cited by Section 4.4.2; do not treat that citation as resolved.

### Constant Llapoy snapshot and derivation mapping

The following immutable source snapshots were copied into Constant Llapoy from the frozen Paper A branch. Their destination blob SHAs were checked against the upstream blob SHAs after creation.

| Frozen upstream source | Upstream blob SHA | Constant Llapoy snapshot | Exact blob match |
|---|---|---|---|
| Section 1 revised | \`1f7857bcd44e1605900bf71193e9b593a62397bd\` | \`source_snapshots/paper-a/Arxiv/paper_01_section_01_revised.md\` | YES |
| Section 2 revised | \`541382fa7ab4b9e254c8e7e5158f202c1a975e0d\` | \`source_snapshots/paper-a/Arxiv/paper_01_section_02_revised.md\` | YES |
| Section 3 revised | \`9ac164ac67cc121af212c4fb7268b809d9234bd6\` | \`source_snapshots/paper-a/Arxiv/paper_01_section_03_revised.md\` | Recorded in prior snapshot inventory |
| Section 4 revised | \`a7570431eac62dd4555194df283edb5a9c87a28d\` | \`source_snapshots/paper-a/Arxiv/paper_01_section_04_revised.md\` | YES |

Provenance sidecars for Sections 1 and 2 record the frozen repository, branch, commit, original path, and blob SHA. These snapshots are read-only evidence. Any proposed manuscript correction must be made in a separate Constant Llapoy working copy and must not alter the upstream repository without prior authorization.

New independent Paper A mathematical work added under Constant Llapoy:

- \`audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md\`
- \`audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md\`
- \`audits/paper-a/FINITE_N_STRONG_COUPLING_EIGENVALUE_DIAGNOSTIC.md\`
- \`working/paper-a/CANONICAL_STRONG_COUPLING_DERIVATION.md\`

These are verification artifacts, not upstream manuscript sources and not replacements for the frozen source files.

**Source freeze status:** FROZEN for this extraction snapshot. Any upstream change requires a new manifest revision and impact analysis.

## 3. Paper D source freeze

| Field | Value |
|---|---|
| Upstream repository | `mytheeramet3dev-x/Absolute_Sym` |
| Branch | `paper-d-singularity` |
| Frozen commit | `2678e3f581d707ac57e8a72d3f961fadbba29ade` |
| Commit date | 2026-11-15T01:45:49Z |
| Working title in branch README | Singularity Geometry and Spectral Entropy: Detection, Localization, and Classification of Spectral-Entropy Singularities |
| Integrated manuscript status | NOT_CONSOLIDATED |
| Manuscript directory record | `papers/paper-d/09-manuscript/README.md`, blob `dae018fd1b804fe38495c914b0346618a3a0925f` |
| Theorem source directory | `papers/paper-d/02-theorems/` |

The branch README explicitly states that the integrated publication-facing draft is not yet consolidated. Therefore the nine files in `papers/paper-d/02-theorems/` are registered as theorem/proposition source records and claim candidates, **not** as a complete extraction of a final Paper D manuscript.

### Theorem/proposition source files

| Source file | Blob SHA | Constant Llapoy record |
|---|---|---|
| `theorem_1_quadratic_spectral_zero.md` | `6e578f930ed4494427823b18f59598985300f43e` | `AS-ALPHA-D-THM-0001` |
| `theorem_2_coupling_space_singularity.md` | `d68fd99ac61a6581d2b841387e4e87c913cb7a4d` | `AS-ALPHA-D-THM-0002` |
| `proposition_global_regular_zero_hypersurface.md` | `726b26f4d7078b7f4299b13ad70650a6d6e52a71` | `AS-ALPHA-D-THM-0003` |
| `proposition_entropy_regularity_hierarchy.md` | `ae50d0218e744b3976b62d560b13aaed1e5757fe` | `AS-ALPHA-D-PROP-0001` |
| `proposition_even_field_parity_spectrum.md` | `7319ccc15117ab4be3d239574543672e08eafd6e` | `AS-ALPHA-D-PROP-0002` |
| `proposition_pminus_zero_set_path_connected.md` | `92eb4b9ef1063003b6928e9e25048baf30447398` | `AS-ALPHA-D-PROP-0003` |
| `proposition_pplus_strict_positivity.md` | `aa8758900808d5171e67581b4bc0ac1b608e18de` | `AS-ALPHA-D-PROP-0004` |
| `proposition_swap_symmetry_exact_zero.md` | `a44667e6dca77e14df7eb4333888b45f7551fe50` | `AS-ALPHA-D-PROP-0005` |
| `proposition_symmetry_breaking_even_eigenvalue.md` | `a7d2fd5f5799d252fbcbc9251f8b3b39bde2b543` | `AS-ALPHA-D-PROP-0006` |

A separate provisional integrated manuscript exists on the upstream `main` snapshot at `Alphabet/paper_d/paper_04_manuscript.md`, but it is not the active structured manuscript on the frozen `paper-d-singularity` branch. It is retained as a historical/secondary reference and is not silently substituted for the branch's current source state.

**Source freeze status:** FROZEN for theorem-source inventory only. Integrated manuscript extraction is BLOCKED pending consolidation and explicit canonical designation.

## 4. Paper A1 source freeze

| Field | Value |
|---|---|
| Upstream repository | `mytheeramet3dev-x/Absolute_Sym` |
| Branch | `stage-a1-1-repair-review` |
| Frozen commit | `b95f5777dfadaf5d31eef27d813ea56c33540d1c` |
| Commit date | 2026-11-15T17:31:06Z |
| Working title | Finite-Size Extension and Thermodynamic Limit of Self-Consistent Quantum Entanglement Networks |
| Stage status in README | A1-1 Complete (Repaired); Stage A1-2 Pending |
| Formal theorem statements | `Alphabet/paper_a1/stage_a1_1/theorem_statements.md`, blob `b83ac8cb242cb754dbf2e56e00995e90ec0a7d31` |
| Stage claim ledger | `Alphabet/paper_a1/stage_a1_1/claim_ledger.md`, blob `2f840b9c795e78ef67c0c2cec1da14c59d3f0a75` |
| Stage README | `Alphabet/paper_a1/stage_a1_1/README.md`, blob `e556635bcda26ec1f926a603ce420d728a2051c3` |
| Project README | `Alphabet/paper_a1/README.md`, blob `dd3f3a1a55cc85bf61e7c71d9851951357458a41` |

Five formal theorem statements are present in the Stage A1-1 theorem statement file. The stage claim ledger reports 17 classified entries. The five formal theorem records have been transcribed separately; the 17-entry status ledger remains a secondary classification source and is not treated as 17 proved theorems.

This is a Stage A1-1 source freeze, not a claim that all of Paper A1 is a completed integrated manuscript. Stage A1-2 is pending according to the source README.

**Source freeze status:** FROZEN for Stage A1-1 statement extraction. Whole-paper completeness is NOT_ESTABLISHED.

## 5. Cross-paper and branch controls

1. Paper A, D, and A1 use different branches and different source policies. Do not substitute one branch's file for another without a recorded source decision.
2. The branch commit SHA and blob SHA are both required for evidence provenance.
3. The existence of a theorem file does not prove that it is included in a final manuscript.
4. The word PROVEN in an upstream source is a source-reported status, not a Constant Llapoy verification result.
5. A branch or file update invalidates the corresponding source freeze until re-reviewed.
6. Any conflict between a branch-specific working source and a historical/main-branch copy must remain visible.

---


## 5. Paper B source snapshot and redesign record

| Field | Value |
|---|---|
| Upstream repository | `mytheeramet3dev-x/Absolute_Sym` |
| Branch | `main` |
| Frozen commit at retrieval | `122a62b48484715a660200dfd792a452ea0bdfa1` |
| Commit date | 2026-11-15T16:33:08Z |
| Upstream canonical draft | `Alphabet/paper_b/paper_02_manuscript.md` |
| Upstream blob SHA | `7aeace0eedbcaa47c156f8e8c7170e2413541851` |
| Constant Llpoy immutable snapshot | `source_snapshots/paper-b/paper_02_manuscript_original.md` |
| Snapshot creation commit | `84244c71354c3372933baa0496ccb3e6099b6552` |
| Source character count | 21,585 |
| Snapshot treatment | Verbatim archival copy; no scope rewrite applied to the source snapshot |

The former Paper B draft is a linear-response study of the permutation-symmetric fixed point, including the edge-space (S_N) decomposition and the conditional sign question (B-C>0). It substantially overlaps the representation/response setup already present in Paper A. It is therefore preserved as historical source material and is **not** the scope of the redesigned Paper B.

The redesigned Paper B working programme is recorded separately:
- `working/paper-b/README.md`
- `working/paper-b/PAPER_B_SCOPE_CHARTER.md`
- `working/paper-b/PAPER_B_THEOREM_OBLIGATIONS.md`
- `working/paper-b/PAPER_B_ASSUMPTION_REGISTER.md`

The new official working title is:

**Equivariant Bifurcation, Isotropy Classification, Representation-Resolved Stability, and Nonlinear Branch Structure in Self-Consistent Quantum Interaction Networks**

The new scope targets model-specific nonlinear nonuniform branches, isotropy classification, representation-resolved stability, and local nonlinear branch structure. It also introduces a mandatory entropy-regularity gate: the smoothness of the ground-state projector does not by itself establish the differentiability of von Neumann mutual information when reduced density matrices have zero eigenvalues.

**Important:** The Paper B scope charter is a research specification only. Its theorem families remain OPEN or NOT YET INVESTIGATED unless later proof artifacts establish otherwise. No file in the upstream `Absolute_Sym` repository was modified during this redesign.


**End of manifest.**