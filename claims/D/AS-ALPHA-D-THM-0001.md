# AS-ALPHA-D-THM-0001 — Entropy asymptotics at a quadratic spectral zero

- Claim ID: `AS-ALPHA-D-THM-0001`
- Paper: D
- Claim version: 0.1.0
- Extraction status: TRANSCRIBED
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `paper-d-singularity`
- Source commit: `2678e3f581d707ac57e8a72d3f961fadbba29ade`
- Source path: `papers/paper-d/02-theorems/theorem_1_quadratic_spectral_zero.md`
- Source blob SHA: `6e578f930ed4494427823b18f59598985300f43e`
- Source line range: 21-37

## Verbatim source excerpt

```markdown
## 2. Theorem

**Theorem 1 (quadratic spectral zero produces a logarithmic entropy cusp).**
Under the hypotheses above, the contribution of the vanishing branch has expansion
$$
-\lambda_0(t)\log\lambda_0(t)
=-2c t^2\log|t|-c(\log c)t^2
+O(t^4|\log|t||).
$$
Consequently, this contribution is continuously differentiable at $t=0$, its first derivative at zero is zero, and it is not twice differentiable at zero. More precisely, for $t\ne0$,
$$
\frac{d^2}{dt^2}\big[-\lambda_0(t)\log\lambda_0(t)\big]
=-4c\log|t|+O(1),
$$
which diverges to $+\infty$ as $t\to0$.

Since the remaining eigenvalues stay strictly positive and are smooth, their entropy contributions are smooth. Therefore the full entropy has the same non-$C^2$ singularity, unless another vanishing branch contributes a term that cancels it. For density-matrix eigenvalue contributions of the same sign and the same quadratic order, such cancellation cannot occur.
```

## Extraction notes

General local lemma under explicit hypotheses; application to the N=4 model is conditional on verifying the selected eigenvalue branch and parameter path.

The current `paper-d-singularity` branch explicitly states that an integrated publication-facing manuscript has not yet been consolidated. These are theorem/proposition source records, not evidence that all are included in a final manuscript.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
