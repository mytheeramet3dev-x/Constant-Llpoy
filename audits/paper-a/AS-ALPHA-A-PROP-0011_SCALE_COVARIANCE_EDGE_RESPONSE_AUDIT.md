# Paper A PROP-0011 — Scale Covariance of Edge-Response Eigenvalues Audit

**Claim:** AS-ALPHA-A-PROP-0011  
**Source baseline:** Absolute_Sym frozen commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Source files:** Section 2.3 and Section 5.4  
**Audit type:** Analytic chain-rule audit (not Lean verification)

## Verdict

**PASS — conditional chain-rule/spectral scaling identity.** This audit verifies the scaling identity assuming the manuscript's dimensionless dependence and the response derivatives exist. It does not establish model-specific entropy differentiability, full source-to-Lean correspondence, or any sector ordering.

## 1. Source statement

Section 2.3 gives, at the symmetric point, (H(J,h)=h\widetilde H(J/h,1)), for (h>0), and consequently (I_{12}(J,h)=\mathcal G_N(x)), where (x=J/h). Section 5.4 asserts dimensional response eigenvalues scale as (h^{-1}) times functions of (x), and feedback eigenvalues depend on (g/h).

The response matrix is the derivative of the mutual-information output vector with respect to independent dimensional edge couplings, evaluated at the symmetric point. The independent-edge perturbation coordinates and the output coordinates must use consistent conventions.

## 2. Chain-rule derivation

For a general edge vector \\mathbf J and fixed (h>0), the energy-rescaled Hamiltonian is
\\[
H(\\mathbf J,h)=h\\widetilde H(\\mathbf J/h,1).
\\]
Positive scalar multiplication leaves the ground-state projector unchanged. In a differentiability region, the mutual-information output map therefore has the dimensionless form
\\[
\\mathbf I(\\mathbf J,h)=\\widetilde{\\mathbf I}(\\mathbf J/h).
\\]
Differentiating componentwise with respect to a dimensional edge variable gives
\\[
\\frac{\\partial I_e}{\\partial J_f}(\\mathbf J,h)
=\\frac1h\\frac{\\partial\\widetilde I_e}{\\partial r_f}(\\mathbf r),
\\qquad \\mathbf r=\\mathbf J/h.
\\]
Hence the response matrices satisfy
\\[
\\chi(\\mathbf J,h)=h^{-1}\\widetilde\\chi(\\mathbf J/h).
\\]
At a permutation-symmetric point, if the response matrix decomposes into the same invariant sectors under the same edge-coordinate convention, each sector eigenvalue inherits the scalar factor:
\\[
\\chi_k(J,h)=h^{-1}\\widetilde\\chi_k(J/h).
\\]
Multiplication by feedback gain (g) yields
\\[
g\\chi_k=(g/h)\\widetilde\\chi_k(J/h),
\\]
so the dimensionless feedback spectrum depends on (g/h) and (x=J/h).

## 3. Scope and assumptions

- (h>0); the (h=0) case is excluded because the ratio coordinates are undefined.
- The ground-state projector and mutual-information map are sufficiently regular for the response derivatives to exist.
- Response variables are independent edge couplings; no hidden normalization of the uniform direction is introduced between dimensional and dimensionless coordinates.
- Sector eigenvalues are those of the same response-matrix convention at the symmetric point.
- No claim is made that (chi_1\gtreqless\chi_2), or that a sector is unstable/suppressed.

## 4. Independent consistency checks

1. Positive rescaling (H=h\widetilde H) with (h>0) preserves the spectral projector, supporting dimensionless dependence.
2. The derivative of (J_f/h) with respect to (J_f) is exactly (1/h), yielding the response factor.
3. The sector decomposition is unaffected by multiplication by a positive scalar; eigenvectors and ordering are preserved for fixed (h>0).
4. Feedback scaling is (g/h), consistent with Section 5.4.

## 5. Limitations

This is a hand-checkable analytic chain-rule result, not a Lean theorem. It does not discharge entropy differentiability from the Hamiltonian alone, construct response derivatives, prove the representation decomposition of the response map, or verify every source convention by formal equivalence. Those obligations remain.

## 6. Conclusion

PROP-0011 passes at the conditional analytic level. The manuscript scaling formula is correct under the explicit differentiability and coordinate-normalization assumptions above. Status remains **ANALYTIC-VERIFIED (conditional chain-rule scope only); NOT-LEAN-VERIFIED**.
