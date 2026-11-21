# IV-52 — Fourth-Order Low Eigenvalue Schur Reconstruction

**Status:** SCHUR/EIGENVALUE FORMULA PASS / FOURTH-ORDER MATRIX COEFFICIENTS OPEN / NOT VERIFIED  
**Target:** AS-ALPHA-A-PROP-0012 low branch of the two-site odd block at uniform coupling.  
**Scope:** Algebraic eigenvalue expansion only. No fourth-order wavefunction reconstruction, numerical check, or Lean verification claimed.

## 1. Required block expansion

In the leading eigenbasis (u,v), assume the odd block admits an analytic expansion
O(r)=r^2 A+r^3 B+r^4 C+O(r^5), with A=diag(a,0), a>0. IV-51 reports the cubic null cancellation B_vv=0 at the uniform point. Write entries:
O_uu=a r^2+b_uu r^3+c_uu r^4+O(r^5,
O_uv=b_uv r^3+c_uv r^4+O(r^5,
O_vv=c_vv r^4+O(r^5.
The cubic null entry is zero by the prior conditional calculation; it is not assumed globally.

## 2. Schur/eigenvalue derivation

For the low eigenvalue lambda, the eigenvector equation or Schur complement gives, for O_uu-lambda nonzero,
lambda=O_vv - O_uv^2/(O_uu-lambda).
Since O_uu=a r^2+O(r^3), O_uv=b_uv r^3+O(r^4), O_vv=c_vv r^4+O(r^5), and lambda=O(r^4), the correction is
O_uv^2/(O_uu-lambda)=|b_uv|^2/a r^4+O(r^5
under a controlled analytic expansion and a>0. Therefore
lambda_low=r^4(c_vv-|b_uv|^2/a)+O(r^5).
This is a formula for the coefficient, not its evaluation.

## 3. Fourth-order coefficient source ledger

The direct coefficient c_vv requires the fourth-order odd-block entry projected onto v. It must include configuration-resolved amplitude products with total perturbative order four: (1,3), (2,2), (3,1) and any consistent normalization/energy corrections. The mixing correction |b_uv|^2/a is determined by cubic off-diagonal entry and leading large eigenvalue coefficient.

IV-51's second-order two-flip amplitudes do not suffice to compute c_vv. Third-order amplitudes and all relevant second-order products must be derived, including environment matching in the partial trace.

## 4. Error control

An O(r^5) remainder requires analytic expansions for the block entries in a common neighborhood, not merely pointwise estimates. Differentiated remainder control for edge directions B and C is a separate obligation and is not established here.

## 5. Disposition

- Schur/eigenvalue expansion: **PASS (conditional algebra)**.
- IV-51 cubic null cancellation at uniform point: carried forward as an analytic, not mechanized, result.
- Direct fourth-order c_vv: **OPEN**.
- Cubic mixing b_uv: **not evaluated here**.
- Low-branch coefficient sign/positivity: **OPEN**.
- Entropy derivative, B-C, and differentiated uniform remainder: **OPEN**.
- Lean: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 6. Next obligation

IV-53: derive cubic off-diagonal b_uv explicitly from the second-order configuration amplitudes and calculate the mixing correction |b_uv|^2/a. Do not evaluate or assume c_vv until the fourth-order reduced-block reconstruction is independently completed.
