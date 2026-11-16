# AS-ALPHA-A-PROP-0009 — Conditional strong-coupling asymptotics of the mutual-information function

- **Claim ID:** `AS-ALPHA-A-PROP-0009`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** PARTIALLY VERIFIED
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_04_revised.md`
- **Source blob SHA:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Source line range:** 105-120
- **Claim-specific Verification Obligation Matrix:** Not yet created; proof obligations are recorded in the linked follow-up audits.

## Verbatim source excerpt

The following is transcribed from the pinned source. It is not a rewritten theorem statement.

```markdown
By applying Schrieffer–Wolff degenerate perturbation theory to the parity-even sector (see Lemma 5.1), we obtain the rigorous asymptotic expansion for the dimensionless mutual information:
\[
\mathcal G_N(x) = \ln 2 - \frac{1}{(N-1)^2 x^2} + O\left(\frac{\ln x}{x^4}\right) \qquad (x \to \infty).
\]
This proves that the endpoint limit is attained as:
\[
\lim_{x \to \infty} \mathcal G_N(x) = \ln 2.
\]
Furthermore, the analytic control of the entropy remainder near the degenerate subspace guarantees that the derivative follows the leading algebraic order:
\[
\mathcal G_N'(x) = \frac{2}{(N-1)^2 x^3} + O\left(\frac{\ln x}{x^5}\right).
\]
This rigorously establishes that
\[
\lim_{x \to \infty} \mathcal G_N'(x) = 0.
\]
```

## Extraction notes





This is a source-asserted asymptotic claim. Its stated derivation points to Lemma 5.1, which is not present in the pinned Section 5 file. Keep CANDIDATE/NOT_ASSESSED until the missing proof source, perturbation hypotheses, and entropy-remainder control are located and audited.



## Review state

- Independent extraction review: COMPLETED (see PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md).
- Mathematical proof review: PARTIALLY COMPLETED; see the independent uniform strong-coupling derivation and the general-N small-eigenvalue coefficient derivation.
- Formal proof correspondence: NOT_RUN.
- Lean verification: NOT_RUN.
- Independent audit of the exact-rational diagnostic implementation: PENDING.
- Overall Constant Llapoy status: CANDIDATE / PARTIALLY VERIFIED.

### Independent mathematical derivation — 2026-11-17

The uniform strong-coupling function and its derivative have now been derived independently inside Constant Llapoy from the Hamiltonian, the parity-sector perturbation problem, and the one-/two-site reduced states:

- Uniform function and derivative proof: audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md.
- General-N fourth-order small-eigenvalue derivation: audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md.
- Exact-rational finite-N diagnostic and N=4 exception: audits/paper-a/FINITE_N_STRONG_COUPLING_EIGENVALUE_DIAGNOSTIC.md.
- Reproducible diagnostic: working/paper-a/finite_n_strong_coupling_exact_diagnostic.py.
- Integrated working derivation: working/paper-a/CANONICAL_STRONG_COUPLING_DERIVATION.md.

The derivation establishes, for each fixed finite N >= 4,

\[
\mathcal G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right),
\]

and independently establishes

\[
\mathcal G_N'(x)=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right).
\]

The derivative result is obtained from analytic eigenvalue branches and their derivatives, not by differentiating a bare big-O statement.

A correction was found in a supporting fourth-order eigenvalue coefficient: the coefficient is 1/648 at N=4, not 1/1296; for N >= 5 it is 1/[8(N-2)(N-1)^4] (derived symbolically for N >= 9 and checked by exact-rational finite calculations for N=5,6,7,8).

**Why only Partially Verified:** the mathematical asymptotic derivation is now present, but Lean formalization, proof-to-manuscript correspondence, independent code review, and source-citation reconciliation have not been completed. The frozen manuscript still cites Lemma 5.1, whose located source concerns B-C rather than this uniform asymptotic. No upstream file was changed.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.

## Independent extraction review — 2026-11-17

- **Review status:** REVIEWED_WITH_ISSUES
- **Source transcription and locator:** The quoted passage matches Section 4, lines 105–120; the source condition (N\ge4) appears immediately before it at line 103 and is missing from this record's excerpt.
- **Finding 1 — Context:** The claim's assumptions must include the immediately preceding (N\ge4) condition.
- **Finding 2 — Missing dependency:** The source cites Lemma 5.1, which is absent from the pinned authoritative Section 5.
- **Finding 3 — Differentiated remainder (at extraction-review time):** The function big-O term alone does not justify differentiation. This mathematical gap has since been addressed by a separate independent derivation in Constant Llapoy; see the follow-up section below.
- **Disposition at extraction review:** Keep CANDIDATE / NOT_VERIFIED pending an independent derivation. This disposition is superseded by the 2026-11-17 follow-up, which records PARTIALLY VERIFIED status.
- **Proof review:** PARTIALLY COMPLETED by the follow-up derivation. Formal verification: NOT_RUN.

### Supporting-source reconciliation

The file cited by the manuscript as Lemma 5.1 is located at `docs/lemma_5_1_proof.md`, blob `db2c552f2d9bea663b20e05aefdc5447d2494a7b`, but its actual subject is asymptotic positivity of (B-C), not the stated strong-coupling expansion of (mathcal G_N(x)). A separate proof-reconciliation report states that the derivative-remainder chain for (B-C) is not closed. Therefore the frozen Section 4.4.2 Lemma 5.1 citation remains mismatched or incomplete. The cited file is not the proof source for the uniform (mathcal G_N) expansion. An independent derivation has since been added inside Constant Llapoy; do not treat the upstream Lemma 5.1 citation itself as repaired.
