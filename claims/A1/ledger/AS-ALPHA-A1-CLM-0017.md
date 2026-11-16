# AS-ALPHA-A1-CLM-0017 — Stage A1-1 source ledger item C16

- Claim ID: `AS-ALPHA-A1-CLM-0017`
- Upstream ledger ID: `C16`
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
- Source line: 28
- Related formal theorem records: To be cross-linked after claim-to-theorem dependency review.

## Verbatim source ledger row

```markdown
| **C16** | Pure-`mpmath` critical sequence ($N=4..160$, even & odd, `dps=80` eigensolver residuals $\le 4.05\times 10^{-79}$, `h=1e-18` FD ~36–37-digit $u_c, G''$) and corrected `numpy` OLS extrapolations | `NUMERICALLY_REPRODUCED` | [`run_a1_1_verification.py`](numerical_verification/run_a1_1_verification.py) | Replaces earlier float64 RQI seeding with pure-`mpmath` Sturm bisection + Thomas RQI and Perron–Frobenius sign verification; resolves Stage A1-0's mislabeled quadratic fits. |
```

## Interpretation control

This is a transcription of an upstream epistemic ledger entry, not a declaration that the entry is a theorem. Source categories such as PROVEN, CONJECTURAL, INCORRECT, UNVERIFIED, and NUMERICALLY_REPRODUCED are retained as reported. Constant Llapoy has not independently verified the mathematical content or the source's classification.

- Independent extraction review: NOT_RUN.
- Mathematical review: NOT_RUN.
- Source dependency review: NOT_RUN.
- Constant Llapoy verification status: NOT_VERIFIED.
