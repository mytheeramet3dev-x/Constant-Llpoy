# AS-ALPHA-A1-CLM-0005 — Stage A1-1 source ledger item C5a

- Claim ID: `AS-ALPHA-A1-CLM-0005`
- Upstream ledger ID: `C5a`
- Paper: A1
- Scope: Stage A1-1
- Extraction status: TRANSCRIBED_FROM_STATUS_LEDGER
- Constant Llapoy verification status: NOT_ASSESSED
- Upstream source-reported classification: PRESERVED VERBATIM IN ROW BELOW; NOT INDEPENDENTLY VALIDATED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `stage-a1-1-repair-review`
- Source commit: `b95f5777dfadaf5d31eef27d813ea56c33540d1c`
- Source path: `Alphabet/paper_a1/stage_a1_1/claim_ledger.md`
- Source blob SHA: `2f840b9c795e78ef67c0c2cec1da14c59d3f0a75`
- Source line: 16
- Related formal theorem records: To be cross-linked after claim-to-theorem dependency review.

## Verbatim source ledger row

```markdown
| **C5a** | Finite-$N$ positivity, $C^1([0,\infty))$ regularity & attainment: $G_N(u) > 0$, $G_N \in C^1([0,\infty))$, $q_N \in C^1((0,\infty);(0,\infty))$, and compact non-empty $M_N := \arg\min_{u>0} q_N(u)$ for all $N \ge 2$ | `PROVEN` | [`proofs/op3_gamma_convergence_and_bounds.md`](proofs/op3_gamma_convergence_and_bounds.md) Lemma 1.1 & Lemma 2.1; [`proofs/op2_uniform_convergence.md`](proofs/op2_uniform_convergence.md) §3(2); [`proofs/critical_threshold_and_location_theorems.md`](proofs/critical_threshold_and_location_theorems.md) Lemma 2.1 | Proven via Rayleigh–Ritz against $|+\rangle^{\otimes N}$, shifted Perron–Frobenius + Rellich's theorem on $(0,\infty)$, and direct two-sided Kato/Rellich even-order eigenvalue branching around $u=0$ giving $G_N'(u) = \frac{u}{2N^2}\ln\frac{N}{u} + O_N(u) \to 0 = G_N'(0^+)$ and $\lim_{u\to 0^+} G_N''(u) = +\infty$. |
```

## Interpretation control

This is a transcription of an upstream epistemic ledger entry, not a declaration that the entry is a theorem. Source categories such as PROVEN, CONJECTURAL, INCORRECT, UNVERIFIED, and NUMERICALLY_REPRODUCED are retained as reported. Constant Llapoy has not independently verified the mathematical content or the source's classification.

- Independent extraction review: NOT_RUN.
- Mathematical review: NOT_RUN.
- Source dependency review: NOT_RUN.
- Constant Llapoy verification status: NOT_VERIFIED.
