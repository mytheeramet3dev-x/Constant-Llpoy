# Paper A Full Extraction Audit — Pass 1

- **Document ID:** CL-AUDIT-A-001
- **Version:** 0.1.0
- **Audit scope:** Full assertion-by-assertion scan of the six authoritative revised sections
- **Upstream repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Upstream branch:** `paper-a-interval-audit-2026-11-14`
- **Frozen commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Integrated manuscript:** `Arxiv/paper_01_manuscript.md` (cross-check only)
- **Secondary claim index:** `Arxiv/claims_ledger.md`, blob `7a9eadbf363b75fe29088ad3c5443e145779316c`
- **Audit status:** STRUCTURAL_SCAN_COMPLETED; RECONCILIATION_AND_INDEPENDENT_REVIEW_OPEN
- **Mathematical verification result:** NONE; no claim is promoted to VERIFIED

## 1. Scope and method

The six revised section files are the authoritative Paper A text at the frozen revision. All six were fetched directly from the pinned branch and their blob SHAs matched the source manifest:

| Section | Source blob SHA | Scan |
|---|---|---|
| 1 | `1f7857bcd44e1605900bf71193e9b593a62397bd` | Scanned |
| 2 | `541382fa7ab4b9e254c8e7e5158f202c1a975e0d` | Scanned |
| 3 | `9ac164ac67cc121af212c4fb7268b809d9234bd6` | Scanned |
| 4 | `a7570431eac62dd4555194df283edb5a9c87a28d` | Scanned |
| 5 | `671c97fa68fa48c929760bf9956d197b358c4904` | Scanned |
| 6 | `5e734065c2ddd42ee602dada89e7455d2ad9e7a0` | Scanned |

The scan distinguishes (a) mathematical assertions, (b) definitions and conventions, (c) conditional results, (d) numerical evidence/conjectures, (e) interpretive statements, and (f) explicit limitations. Repeated statements in Sections 1 and 6 are treated as cross-references or restatements, not automatically as new claims.

## 2. Paper A claim inventory

The initial seven records were not a complete extraction. Seven additional candidate records have now been created, giving **14 Paper A source-linked candidate records**. Every record remains CANDIDATE / NOT_ASSESSED.

### 2.1 Existing records retained

| Claim ID | Source content | Extraction observation |
|---|---|---|
| AS-ALPHA-A-PROP-0001 | Threshold coefficient `alpha_N = inf x/G_N(x)`; exact dimensional scaling when the infimum is attained internally | Preserve interior-attainment condition; no global root-count claim |
| AS-ALPHA-A-DEF-0001 | Definition 1: interior critical point | Definition, not a theorem |
| AS-ALPHA-A-PROP-0002 | Proposition 1: tangent constraint | Exact algebraic consequence of the two critical-point equations |
| AS-ALPHA-A-THM-0001 | Conditional local saddle-node normal form | Requires local regularity and nondegeneracy; model-specific curvature is open |
| AS-ALPHA-A-PROP-0003 | Exact scalar Picard-attractivity condition | Must retain full multiplier inequality; descending-branch condition alone is insufficient |
| AS-ALPHA-A-PROP-0004 | Root-by-root dimensionless branch scale independence | Does not imply uniqueness or branch selection |
| AS-ALPHA-A-PROP-0005 | Edge-response representation decomposition and `chi_1-chi_2=(N-2)(B-C)` | Identity/decomposition only; sign of `B-C` is not theorem |

### 2.2 Newly created candidate records

| Claim ID | Source content | Key limitation / obligation |
|---|---|---|
| AS-ALPHA-A-THM-0002 | Perron–Frobenius nondegeneracy of finite-`N`, `h>0` ground state | Check matrix sign convention, irreducibility, and exact coupling domain |
| AS-ALPHA-A-PROP-0006 | Positive energy rescaling preserves ground-state projector; `I_12(J,h)=G_N(J/h)` | Requires `h>0` and nondegenerate ground state; not a unitary symmetry |
| AS-ALPHA-A-PROP-0007 | Product state at `x=0`, `G_N(0)=0`, and trivial fixed point | Entropy derivatives at rank-deficient endpoint need separate treatment |
| AS-ALPHA-A-PROP-0008 | Subcritical exclusion: `eta<alpha_N` implies `f(x;eta)<0` | Conditional on `G_N(x)>0` on the domain; says nothing about existence above threshold |
| AS-ALPHA-A-PROP-0009 | Strong-coupling expansion of `G_N(x)` and `G_N'(x)` | Source points to absent Lemma 5.1; proof and entropy-remainder control not located in the six authoritative sections |
| AS-ALPHA-A-PROP-0010 | Uniform-response upper bound and correction of the false implication that `F_J<0` forces negative response | Verify derivative conventions and relation between Sections 3–5 |
| AS-ALPHA-A-PROP-0011 | Response eigenvalue scaling `chi_k(J,h)=h^{-1} chi_tilde_k(x)` | Requires differentiability and a precise response-matrix definition |

### 2.3 Additional assertions captured for obligation mapping

These assertions are present in the six sections but should be represented as sub-obligations or split into separate records after independent extraction review:

1. **Regularity of `G_N`:** smoothness/analyticity is conditional on reduced density matrices remaining in a fixed-rank regularity region; entropy derivatives at `x=0` require separate treatment.
2. **Threshold minimizer curvature:** the relation between `G_N''(x_c)<0` and strict nondegeneracy of the minimum of `x/G_N(x)` must be checked algebraically with all positivity and differentiability hypotheses.
3. **`F_g>0`:** exact at a nontrivial point where `G_N(x_c)>0`; this is a coefficient in the local normal form.
4. **Local branch orientation:** the signs of `F_x` on the two local branches follow under the stated negative-curvature condition; this is not a global branch theorem.
5. **Global continuation:** claims extending `x_*(gamma) >= x_c` or the selected upper branch to all `gamma >= 1` are conditional on the explicit no-turning/no-branch-exchange assumption.
6. **Strong-coupling branch limits:** the limits of the Picard multiplier and fixed-point derivative require the selected branch to continue globally and the asymptotic derivative expansion to be valid.
7. **Response-sector ordering:** `B-C>0 iff chi_1>chi_2` is algebraic, but the positivity of `B-C` remains a numerical conjecture; it does not by itself prove dynamical instability or geometric suppression.
8. **Numerical exclusions:** the `N=50` near-critical data are explicitly excluded because the spectral gap falls below the reliability threshold.
9. **Physical-branch terminology:** the manuscript defines it by a documented continuation/iteration prescription; do not silently identify it with every descending root.

## 3. Structural and cross-reference findings

### A-ISSUE-001 — Unresolved internal references to Lemma 5.1 and Lemma 5.2

Section 4.4.2 invokes **Lemma 5.1** for the Schrieffer–Wolff strong-coupling expansion. Section 4.4.3 invokes **Lemma 5.2** for a weak-coupling perturbative expansion. The pinned authoritative Section 5 contains subsections 5.1–5.4 but no Lemma 5.1 or Lemma 5.2 statements.

**Disposition:** OPEN / SOURCE CROSS-REFERENCE GAP. Locate the intended lemma source or correct the manuscript reference in the upstream project. Constant Llapoy does not invent missing lemma statements.

### A-ISSUE-002 — Threshold notation in the conclusion needs a precise attainment distinction

Section 2 defines `alpha_N` as an infimum and conditions `g_c(h)=alpha_N h` on interior attainment. Section 6 first writes a minimum formula and then says the statement also holds with an infimum. This is not necessarily a mathematical contradiction, but the exact meaning of `g_c` when the infimum is not attained must be stated consistently: threshold as an infimum of admissible feedback values versus an attained critical fixed point.

**Disposition:** CLARIFICATION REQUIRED; do not rewrite the theorem to assume attainment.

### A-ISSUE-003 — Ground-state nondegeneracy scope

Section 2.1 states nondegeneracy for finite `N` and `h>0`, with `J_ij >= 0` as the reference model, while response derivatives are evaluated in the ambient real edge space. The proof's irreducibility argument must be checked against the exact domain in which the theorem is used.

**Disposition:** MATHEMATICAL AUDIT REQUIRED; preserve the stated distinction between reference couplings and ambient response directions.

### A-ISSUE-004 — Strong-coupling asymptotics are asserted but proof dependency is unresolved

Section 4.4.2 calls the expansion rigorous and refers to Lemma 5.1, which is absent from the authoritative Section 5. It also invokes analytic control of the entropy remainder near a degenerate subspace without exposing that proof in the scanned sections.

**Disposition:** CLAIM CANDIDATE EXISTS; PROOF SOURCE / DEPENDENCY UNRESOLVED. Do not count this as independently established.

### A-ISSUE-005 — Numerical conjecture must remain separate from exact response identity

Section 5 proves the algebraic identity for `chi_1-chi_2`, while the sign of `B-C` is described as a strong numerically supported conjecture. Numerical support for finite tested cases does not prove the universal sign.

**Disposition:** STATUS SEPARATION CONFIRMED. Exact identity candidate and numerical conjecture are separate epistemic objects.

## 4. Reconciliation against upstream `Arxiv/claims_ledger.md`

The upstream ledger is broader than the six-section manuscript and contains project-stage, formal-source, historical, numerical, and retracted entries. It must not be imported wholesale as Paper A theorem statements.

| Upstream ledger item | Six-section manuscript relationship | Disposition |
|---|---|---|
| Collective-spin reduction for symmetric all-to-all TFIM | Not stated as a result in the six revised sections | OUTSIDE CURRENT MANUSCRIPT CLAIM SCOPE; retain as separate project/source claim |
| `V_E = V_0 ⊕ V_1 ⊕ V_2` | Section 5.2 states the corresponding edge-space decomposition | MATCH; covered by AS-ALPHA-A-PROP-0005 |
| `chi_1-chi_2=(N-2)(B-C)` | Section 5.2 states exact identity | MATCH; covered by AS-ALPHA-A-PROP-0005 |
| Generic nondegeneracy of `I''` | Section 3 has a conditional `G_N''(x_c) != 0` assumption and curvature discussion | PARTIAL / NOT AUTOMATICALLY IDENTICAL; notation and hypotheses require reconciliation |
| `G_N(0)=0` | Section 2.3–2.4 states it and identifies trivial root | MATCH; newly recorded as PROP-0007 |
| `lim_{x→∞} G_N(x)=ln 2` | Section 4.4.2 states this as part of a stronger asymptotic expansion for `N>=4` | MATCH WITH SCOPE DIFFERENCE: ledger says closed for `N>=3`, with `N=2` exception; manuscript expansion is stated for `N>=4`. Reconcile proof/scope before merging |
| Nontrivial branch appears at tangent threshold | Sections 2–3 state threshold and local conditional saddle-node structure | PARTIAL MATCH; global existence/root count remains explicitly conditional |
| Stable uniform branch has `F'<0` | Sections 3–5 define descending branch condition and distinguish full Picard stability | MATCH WITH QUALIFICATION; `F'<0` is not the complete Picard criterion |
| `B-C>0` for tested finite sizes and field scan | Section 5.3 reports the same numerical evidence and excludes unreliable `N=50` data | MATCH AS NUMERICAL EVIDENCE ONLY |
| `B-C>0` for all `N)/all parameters | Section 5.3 calls the sign conjectural and says algebraic proof remains open | MATCH AS OPEN CONJECTURE, NOT THEOREM |
| `∂I/∂J_*<0` inferred from `F'<0` | Section 5.1 explicitly rejects this inference and gives the correct upper bound | RETRACTION/CORRECTION MATCH; never register the false inference as a theorem |
| Uniform negative response implies full edge-space instability ordering | Section 5.3 says the sector comparison requires separate eigenvalue/sign analysis | MATCH AS OPEN / NOT ESTABLISHED |
| Universal critical constant independent of `N` | Section 1 and 6 explicitly retain `N)-dependence and disclaim universality | MATCH AS NON-CLAIM / UNSUPPORTED |
| Stage V-F, Gram-wedge, Bell bridge, and later Lean-source entries | Not statements of the six-section Paper A manuscript; they belong to broader project/formalization stages | OUTSIDE PAPER A MANUSCRIPT SCOPE; preserve separately with their own provenance/status |
| Pointwise strong-coupling positivity of `(B-C)/h^2` | Not stated in the six revised sections as a Paper A theorem | OUTSIDE CURRENT PAPER A TEXT; do not merge without explicit source linkage |

## 5. Registry reconciliation and status

- Existing Paper A records before this pass: 7.
- New candidate records created in this pass: 7.
- Total Paper A candidate records after this pass: **14**.
- All 14 remain CANDIDATE / NOT_ASSESSED.
- Structural scan of the six authoritative sections: COMPLETED for this pass.
- Upstream ledger comparison: INITIAL RECONCILIATION COMPLETED; ambiguous scope/notation items remain open.
- Independent extraction review: NOT_RUN.
- Appendix/supplement review: NOT_ESTABLISHED.
- Proof re-derivation: NOT_RUN.
- Lean correspondence / axiom / TCB review: NOT_RUN.
- Dependency closure / circularity analysis: NOT_RUN.
- Constant Llapoy VERIFIED claims from this pass: **0**.

## 6. Required next actions

1. Resolve the missing Lemma 5.1 / 5.2 source references without inventing their contents.
2. Independently review all 14 Paper A records against the pinned source and verify every transcription/line locator.
3. Split or link the additional sub-obligations in §2.3–2.9 only after review determines whether they require independent Claim IDs or are proof obligations of existing claims.
4. Build dependency edges for the threshold, tangent, saddle-node, asymptotic, branch-selection, response, and representation-theory claims.
5. Reconcile the `N>=3` endpoint-limit ledger claim against the `N>=4` asymptotic statement and identify the exact source/proof for each range.
6. Only after independent extraction review, mark records REGISTERED; mathematical verification remains a separate later process.

---

**End of Paper A Full Extraction Audit — Pass 1.**
