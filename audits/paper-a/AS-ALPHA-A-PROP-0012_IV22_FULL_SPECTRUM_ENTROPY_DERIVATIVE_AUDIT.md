# IV-22 — Gap-Free Full-Spectrum Entropy Derivative Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** analytic identity/obstruction audit; no mechanized proof claimed

## 1. Full-spectrum derivative identity

For a differentiable normalized density matrix \(\rho(u)\), with eigenvalues \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\), the entropy is \(S=-\operatorname{Tr}(\rho\ln\rho)\). Away from zero eigenvalues, the derivative is
\[
S_u=-\operatorname{Tr}(\rho_u\ln\rho),
\]
because \(\operatorname{Tr}\rho_u=0\) cancels the identity contribution. This expression is label-free and avoids explicit eigenbranch differentiation, but it still contains the logarithm of the spectrum.

## 2. Gap-free is not log-free

No cluster projector or spectral-gap estimate is required for the formal full-matrix identity. However, as eigenvalues approach zero, \(\ln\rho\) is unbounded. A uniform estimate of \(S_u\) therefore requires more than a bound on \(\|\rho_u\|\) alone: one needs structure controlling the matrix elements of \(\rho_u\) in low-eigenvalue directions, an entropy continuity/differentiability theorem with suitable hypotheses, or a directly verified cancellation.

## 3. Finite-dimensional caveat

In finite dimensions, entropy is continuous on the density-matrix space, but its derivative need not be uniformly bounded near the boundary of positive semidefinite matrices. The derivative formula is first justified for positive definite \(\rho\); boundary cases require limiting arguments. The audit does not assert that the target density matrix stays positive definite uniformly in \(r\), nor that a limiting derivative bound follows automatically.

## 4. What trace identity closes

The trace identity closes the additive \(+1\) term in the eigenvalue derivative formula (or corresponding matrix differential) when normalization is differentiable. It does **not** close \(-\operatorname{Tr}(\rho_u\ln\rho)\), since low eigenvalues may magnify logarithmic weights.

## 5. Potential direct route and required hypotheses

A full-spectrum approach may be viable if the target has a verified decomposition/structure that suppresses \(\rho_u\) on low-eigenvalue spectral subspaces, or if the combined trace can be bounded directly by an explicit cancellation. Required proof obligations include:
- uniform control of \(\rho_u\) and its low-spectrum matrix elements;
- justification of the derivative identity at/near rank-deficient points;
- quantified estimates for small eigenvalue logarithms;
- no unjustified interchange of derivative, spectral limit, and weak-coupling expansion.

These are not established in the working derivation.

## 6. Disposition

- Full-spectrum trace derivative identity: **PASS (formal identity on positive-definite states; boundary requires justification)**.
- Avoiding eigenbranch labels and cluster projector gap: **PASS as an identity-level route**.
- Uniform logarithmic bound without additional spectral structure: **FAIL / not implied**.
- Trace normalization cancellation: **PASS for additive constant only**.
- Target remainder closure: **OPEN**.
- Counterexample to exact proposition: **not established**.
- Lean formalization/build: **not performed**.

## 7. Next

IV-23: **Low-Spectrum Matrix-Element Suppression Audit** — determine whether the structure of the target \(\rho_u\) forces sufficient suppression on low-eigenvalue directions, or identify a concrete obstruction.
