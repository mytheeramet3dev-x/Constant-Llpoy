# Paper A Supporting-Source Reconciliation

- **Document ID:** CL-SOURCE-A-001
- **Version:** 0.1.0
- **Upstream branch:** `paper-a-interval-audit-2026-11-14`
- **Upstream commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Purpose:** Locate proof/support files cited or relevant to Paper A, and reconcile their actual scope and epistemic status
- **Status:** SUPPORTING_SOURCES_LOCATED; PROOF_CLOSURE_NOT_ESTABLISHED

## 1. Executive findings

The upstream branch contains separate supporting documents for Lemma 5.1, Lemma 5.2, ground-state simplicity, and entropy/Schur remainder estimates. They are not integrated into the six revised manuscript sections, and their presence does not make the manuscript cross-references correct or the proofs closed.

Three material findings:

1. **Lemma 5.1 is not the proof of the strong-coupling expansion of `G_N(x)` cited in Section 4.4.2.** The located file `docs/lemma_5_1_proof.md` is titled “Asymptotic Positivity of B-C”. A separate reconciliation report says the derivative-remainder estimate is not closed and the global (B-C>0) claim remains a conjecture. The Section 4.4.2 citation therefore appears mismatched or incomplete; the source for the stated `G_N` expansion remains unresolved.
2. **The original Lemma 5.2 weak-coupling negative-sign proof is superseded by its own audit.** The audit identifies an omitted order-(r^2) coherence, says the earlier negative-sign calculation is invalid, and derives a corrected positive leading sign. It also says the differentiated remainder is still unbounded, so no weak-coupling theorem or global sign-flip conclusion follows. Section 4.4.3's “opposite-sign response characteristics” statement is therefore in source conflict and has been separately registered as `AS-ALPHA-A-PROP-0012`.
3. **A correct Perron–Frobenius proof source exists for the ground-state simplicity claim.** `docs/tfim_ground_state_simplicity_lemma.md` applies PF to (cI-H), not (H+cI), and states the result for finite (N\ge1), (h>0), and real couplings. This repairs the proof route through a separate source, but Constant Llapoy has not independently re-derived or formally verified it.

## 2. Supporting-source inventory

| Source file | Blob SHA | Actual scope | Reconciliation status |
|---|---|---|---|
| `docs/lemma_5_1_proof.md` | `db2c552f2d9bea663b20e05aefdc5447d2494a7b` | Proposed fixed-(N) strong-coupling positivity of (B-C) | Not a proof of the `G_N(x)) expansion cited in Section 4.4.2; derivative-control gap remains |
| `docs/lemma_5_2_proof.md` | `4c1b70a7233f470ca46adaafe59868b2e0779253` | Original weak-coupling derivation claiming (B-C<0) | Superseded by its audit; do not use as current proof support |
| `docs/lemma_5_2_audit.md` | `a5e47defd859b4eb5ed5e63d65d12eeff320f9c7` | Corrected weak-coupling calculation including omitted coherence | Corrected leading sign is positive; derivative remainder unbounded; no theorem |
| `docs/tfim_ground_state_simplicity_lemma.md` | `472328b596ccdcc82ece65faf5ef65a9dab63e50` | PF proof of simple ground state using (cI-H) | Correct proof route located; independent Constant Llapoy proof review still pending |
| `docs/entropy_schur_remainder_lemma.md` | `ef404349c6effa7f13bb14b5cc24f45e3ce6b80e` | Conditional entropy derivative bound from Schur-complement bounds | Conditional only; requires model-specific (Q=O(r^4)) and derivative bound |
| `STRONG_COUPLING_PROOF_RECONCILIATION.md` | `8b75e3790cd0aaa223a2ffbbdbaedb2b6f50afbc` | Forensic reconciliation of strong-coupling proof documents | Defensible status: not a closed theorem; global sign remains conjectural |
| `docs/final_fixed_N_corrected_proof.md` | `5353ea465e9841134003dbfb358fd60edb8fbde6` | Conditional strong-coupling proof skeleton | Explicit derivative remainder gap remains |
| `docs/fixed_N_theorem_hard_audit.md` | `b7af4ad65486779553e6ec58dd24f4714e65095f` | Claimed fixed-(N) theorem with explicit constants | Its declared theorem status conflicts with the reconciliation report's identified invalid/unproved estimates |
| `Arxiv/supplementary_material.md` | `cdead5041ba89f239b3051bcca41ccfae005a349` | Numerical protocol/table, exact sector-identity derivation, solver validation, figure caveats | Adds supporting evidence and an independent algebraic derivation of the identity; numerical data remain finite tested cases |

## 3. Detailed reconciliation

### 3.1 Lemma 5.1 citation mismatch

The manuscript's Section 4.4.2 invokes “Lemma 5.1” immediately before the claimed asymptotic expansion
[
\mathcal G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}
+O\!\left(\frac{\ln x}{x^4}\right).
]
However, the located `docs/lemma_5_1_proof.md` concerns (B-C>0), not this mutual-information expansion. The separate `STRONG_COUPLING_PROOF_RECONCILIATION.md` explicitly states that the derivative-remainder proof for (B-C) is not closed and the global sign remains conjectural.

**Disposition:** Section 4.4.2's proof citation is UNRESOLVED / POSSIBLY MISREFERENCED. The strong-coupling `G_N) expansion and its differentiated remainder require their own exact proof source. Do not treat Lemma 5.1 as satisfying that obligation.

### 3.2 Lemma 5.2 source conflict

The original `docs/lemma_5_2_proof.md` claims (B-C<0) at weak coupling. The later `docs/lemma_5_2_audit.md` identifies an omitted order-(r^2) coherence in the two-site reduced density matrix, states that the negative-sign calculation is invalid, and obtains the corrected leading expression
[
(B-C)_{\rm lead}
=\frac{J}{8h^2}\ln\!\left(\frac{2(N-2)}{N-1}\right)>0.
]
The same audit explicitly leaves the differentiated remainder unbounded and says no endpoint theorem or global sign-flip conclusion follows.

Section 4.4.3 says the lower branch has “opposite-sign response characteristics” compared with the physical stable branch. That wording is not supported by the corrected audit as a theorem. The leading sign correction points the other way, while the full sign remains unproved.

**Disposition:** Claim `AS-ALPHA-A-PROP-0012` is marked SOURCE_CONFLICT / NOT_VERIFIED. The original Lemma 5.2 proof must not be cited as valid evidence without reconciliation.

### 3.3 Ground-state simplicity

The source proof in Section 2.1 incorrectly describes adding a positive scalar multiple of the identity to (H). The separate `docs/tfim_ground_state_simplicity_lemma.md` uses (K=cI-H), whose off-diagonal spin-flip entries are (+h), and uses connectedness of the hypercube graph to establish irreducibility. Its statement covers finite (N\ge1), (h>0), and real couplings.

**Disposition:** Add this file as the candidate proof dependency for `AS-ALPHA-A-THM-0002`. The Section 2.1 sentence remains incorrect as written; the claim itself is not promoted to VERIFIED until this proof is independently reviewed.

### 3.4 Entropy remainder lemma is conditional

The entropy–Schur remainder lemma assumes both
[
\|Q\|\le Kr^4,\qquad
\|\partial_uQ\|\le Kr^4/J.
]
It then derives the entropy derivative bound. Its own qualification states that Kato analyticity alone does not establish these Schur-complement hypotheses. Thus it isolates the missing work but does not close the model-specific estimate.

**Disposition:** Treat as a conditional auxiliary lemma, not as a completed proof of the strong-coupling derivative expansion.

### 3.5 Supplementary material

The supplementary file includes:
- a finite numerical table for (N=4,6,8,10), with (N=50) explicitly excluded as unreliable;
- a short exact Johnson-scheme derivation of (chi_1-chi_2=(N-2)(B-C));
- dense-versus-reduced solver validation checkpoints;
- explicit figure placeholder and reproducibility caveats.

The sector-identity derivation independently supports the algebraic identity in `AS-ALPHA-A-PROP-0005`. The numerical data support only the tested points and do not establish universal (B-C>0).

## 4. Required corrections to the verification map

1. Link `AS-ALPHA-A-THM-0002` to `docs/tfim_ground_state_simplicity_lemma.md` as a candidate proof source; retain independent review as pending.
2. Do not link `AS-ALPHA-A-PROP-0009` to Lemma 5.1 as a proof dependency. Its actual cited proof source remains unresolved.
3. Link `AS-ALPHA-A-PROP-0012` to both versions of Lemma 5.2 and mark the conflict explicitly.
4. Treat the corrected Lemma 5.2 leading sign as a formal asymptotic calculation only until its remainder derivative is proved.
5. Treat `docs/entropy_schur_remainder_lemma.md` as conditional on model-specific Schur-complement estimates.
6. Add supplementary material to the Paper A source inventory and keep its exact algebraic result separate from finite numerical evidence.

## 5. Status

- Supporting source files located: **YES**.
- Lemma 5.1/5.2 integrated into authoritative Section 5: **NO**.
- Section 4.4.2 Lemma 5.1 citation reconciled: **NO; apparent scope mismatch**.
- Section 4.4.3 weak-coupling sign claim reconciled: **NO; source conflict recorded**.
- Ground-state simplicity proof source located: **YES; independent review pending**.
- Strong-coupling derivative remainder closed: **NO**.
- Constant Llapoy VERIFIED claims: **0**.

---

**End of Paper A Supporting-Source Reconciliation.**


## Follow-up — independent closure of the fixed-\(N\) strong-coupling \(B-C\) derivative gap

**Date:** 2026-11-17  
**New working proof:** working/paper-a/GENERAL_EDGE_B_MINUS_C_DERIVATIVE_PROOF.md  
**Internal review:** audits/paper-a/GENERAL_EDGE_B_MINUS_C_PROOF_AUDIT.md  
**Numerical diagnostic:** audits/paper-a/EDGE_RESPONSE_FINITE_DIFFERENCE_DIAGNOSTIC.md

The earlier reconciliation correctly found that the source Lemma 5.1 asserted, but did not prove, the required edge derivatives of the small-eigenvalue entropy remainder. A new independent derivation inside Constant Llapoy now supplies that missing chain for fixed finite \(N\ge4\) near the uniform positive-coupling point.

The key steps are:
1. Joint analyticity of the even-sector ground-state projector in the transverse-field parameter and independent edge perturbations.
2. Exact first-order pair-block entries depending on \(b_1\pm b_2\), with cancellation of the order-\(\varepsilon^2\) Schur-complement coefficient for both parity blocks throughout the edge neighborhood.
3. Analytic small eigenvalue branches of order \(\varepsilon^4\), hence edge derivatives of order \(\varepsilon^4/J\).
4. Separate treatment of the positive small branch (using its positive fourth-order coefficient) and the zero branch (nonnegative analytic eigenvalue with an interior minimum, so the first directional derivative of its entropy contribution is zero).
5. Exact leading one-site response from \(b_i=h/[2\sum_{j\ne i}J_{ij}]\).

The resulting candidate asymptotic is

\[
B-C
=\frac{h^2}{J^3(N-1)^3}
+O_N\!\left(
\frac{h^4}{J^5}
\left[1+\left|\ln(h/J)\right|\right]
\right).
\]

It implies \(B-C>0\) for sufficiently small \(h/J>0\), for each fixed finite \(N\ge4\). The internal analytic review found no remaining gap under the stated local positive-coupling and fixed-\(N\) hypotheses. Full-Hilbert-space finite-difference calculations for \(N=4,5,6\) independently support the leading coefficient.

**Important boundary:** this is a local strong-coupling result only. It does not establish global \(B-C>0\), an explicit \(\varepsilon_N\), or uniformity in \(N\). It does not alter the manuscript's Section 5.3 conjecture status or any claim status, because the result is not yet formalized in Lean or audited for manuscript correspondence. The original upstream Lemma 5.1 file remains a frozen source snapshot and has not been modified.


## Follow-up — weak-coupling \(B-C\) derivative remainder

**Date:** 2026-11-17  
**Frozen source snapshots:**  
- source_snapshots/paper-a/docs/lemma_5_2_proof.md
- source_snapshots/paper-a/docs/lemma_5_2_audit.md

**New independent derivation:** working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md  
**Internal review:** audits/paper-a/WEAK_COUPLING_B_MINUS_C_PROOF_AUDIT.md  
**Reusable entropy lemma:** audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md  
**Numerical diagnostic:** audits/paper-a/WEAK_COUPLING_B_MINUS_C_NUMERICAL_DIAGNOSTIC.md

The original Lemma 5.2 proof has the wrong sign because it omits the order-\(r^2\) coherence in the \((|+-\rangle,|-+\rangle)\) block. The later source audit corrected the leading sign to positive but left the differentiated remainder unbounded.

The new Constant Llapoy derivation retains the full coherence, diagonalizes the positive Gram-matrix branch, and separately handles the zero branch and the small branch of the \((++ , --)\) block using joint analyticity and the nonnegative-eigenvalue entropy lemma. It establishes the conservative fixed-\(N\) asymptotic

\[
B-C
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)
+O_N\!\left(
\frac{J^2}{h^3}
\left[1+\left|\ln(J/h)\right|\right]
\right).
\]

For every fixed finite \(N\ge4\), the leading logarithm is positive and the relative remainder tends to zero. Hence \(B-C>0\) for sufficiently small \(J/h>0\).

The remainder is intentionally weaker than the old source proof's claimed \(O(J^3/h^4)\); that stronger order is not adopted. Full-Hilbert-space high-precision finite differences for \(N=4,5,6\) support the corrected coefficient and show the ratio tending to one.

**Consequence for source claims:** the old negative weak-coupling sign assertion is contradicted by the corrected leading term and the new derivative remainder proof. This resolves the mathematical sign conflict in the supporting source, but the frozen source file remains unchanged. The result is local to \(J/h\to0^+\) and does not prove global \(B-C>0\).
