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
