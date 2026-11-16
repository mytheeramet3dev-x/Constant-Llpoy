# AS-ALPHA-D-PROP-0001 — Entropy regularity from the even order of a spectral zero

- Claim ID: `AS-ALPHA-D-PROP-0001`
- Paper: D
- Claim version: 0.1.0
- Extraction status: TRANSCRIBED
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `paper-d-singularity`
- Source commit: `2678e3f581d707ac57e8a72d3f961fadbba29ade`
- Source path: `papers/paper-d/02-theorems/proposition_entropy_regularity_hierarchy.md`
- Source blob SHA: `ae50d0218e744b3976b62d560b13aaed1e5757fe`
- Source line range: 3-19

## Verbatim source excerpt

```markdown
## Statement

Let \(\lambda(t)\) be a nonnegative real-analytic eigenvalue branch near \(t=0\), with
\[
\lambda(0)=0,\qquad
\lambda(t)=c t^{2k}+O(t^{2k+2}),
\quad c>0,\quad k\in\mathbb N.
\]
Assume the branch is even and that the remainder is analytic. Then
\[
-\lambda(t)\log\lambda(t)
=-2kc\,t^{2k}\log|t|
-c(\log c)t^{2k}
+O(t^{2k+2}|\log|t||).
\]

The entropy contribution is \(C^{2k-1}\) but not \(C^{2k}\) at zero. More precisely, its derivative of order \(2k\) has a logarithmic divergence.
```

## Extraction notes

Scalar entropy contribution only; applying it to a full reduced-state entropy requires accounting for all eigenvalue branches.

The current `paper-d-singularity` branch explicitly states that an integrated publication-facing manuscript has not yet been consolidated. These are theorem/proposition source records, not evidence that all are included in a final manuscript.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
