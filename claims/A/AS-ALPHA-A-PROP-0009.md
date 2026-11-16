# AS-ALPHA-A-PROP-0009 — Conditional strong-coupling asymptotics of the mutual-information function

- **Claim ID:** `AS-ALPHA-A-PROP-0009`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** NOT_ASSESSED
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_04_revised.md`
- **Source blob SHA:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Source line range:** 105-120
- **Claim-specific Verification Obligation Matrix:** Pending extraction review

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

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.

## Independent extraction review — 2026-11-17

- **Review status:** REVIEWED_WITH_ISSUES
- **Source transcription and locator:** The quoted passage matches Section 4, lines 105–120; the source condition (N\ge4) appears immediately before it at line 103 and is missing from this record's excerpt.
- **Finding 1 — Context:** The claim's assumptions must include the immediately preceding (N\ge4) condition.
- **Finding 2 — Missing dependency:** The source cites Lemma 5.1, which is absent from the pinned authoritative Section 5.
- **Finding 3 — Differentiated remainder:** The asymptotic expansion of (mathcal G_N(x)) does not by itself justify differentiating its (O(ln x/x^4)) remainder. The derivative expansion needs a separate analytic remainder estimate; the source asserts such control but the proof is not available in the six revised sections.
- **Disposition:** Keep CANDIDATE / NOT_VERIFIED. Split proof obligations for the function expansion and derivative expansion, include the (N\ge4) context, and locate the missing lemma proof. Do not infer derivative asymptotics from the function asymptotic alone.
- **Proof review:** NOT_COMPLETED. Formal verification: NOT_RUN.
