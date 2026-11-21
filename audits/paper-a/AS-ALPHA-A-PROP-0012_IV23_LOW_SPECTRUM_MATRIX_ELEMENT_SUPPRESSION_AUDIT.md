# IV-23 — Low-Spectrum Matrix-Element Suppression Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** analytic structural review; no mechanized proof claimed

## 1. Spectral-basis expression

For positive definite \(\rho\), in its eigenbasis, the entropy derivative is
\[
S_u=-\sum_i (\rho_u)_{ii}\ln\lambda_i,
\]
with \(\sum_i(\rho_u)_{ii}=0\). This formula makes the issue explicit: suppression of low-eigenvalue diagonal derivatives, or a proven cancellation among them, is needed to compensate large logarithmic weights. Off-diagonal entries do not appear in this first derivative in the instantaneous eigenbasis, but may affect eigenvectors, spectral structure, and higher derivatives.

## 2. What amplitude-order suppression would need to show

Suppose a low eigenvalue scales as \(\lambda_i\asymp r^p\). Its contribution is controlled if the corresponding diagonal derivative has a verified order, e.g. \((\rho_u)_{ii}=O(r^p)\), yielding \(O(r^p|\ln r|)\). But this is not implied merely by \(\lambda_i=O(r^p)\), nor by a generic matrix norm estimate on \(\rho_u\). It requires a structural relation between the edge perturbation and the low-spectrum directions.

## 3. Positivity and tangent constraints

Differentiating positivity and normalization constrains \(\rho_u\), but normalization only gives the sum of diagonal derivatives zero. Positivity at a rank-deficient point imposes additional tangent-cone restrictions on matrix elements involving the kernel, yet these pointwise restrictions do not automatically supply the desired uniform rate in the weak-coupling parameter or a neighborhood of edge parameter.

## 4. Potential suppression mechanisms and evidence status

Candidate mechanisms include:
- perturbation selection rules that forbid edge response in low-eigenvalue directions to a specified order;
- transition-amplitude support/order estimates inherited from pair-flip structure;
- an explicit factorization of low-sector diagonal response with uniform coefficient bounds;
- cancellations verified in the complete entropy derivative, not presumed from trace normalization.

The previous pair-flip support audit is relevant background, but it has not been connected in a checked derivation to the exact diagonal entries \((\rho_u)_{ii}\) of the entropy eigenbasis at low eigenvalues. That connection is an open proof obligation.

## 5. Adversarial checks

- Does \(\lambda_i=O(r^p)\) imply \((\rho_u)_{ii}=O(r^p)\)? **No, not without further structure.**
- Does normalization \(\sum_i(\rho_u)_{ii}=0\) control weighted sum with \(\ln\lambda_i\)? **No, not alone.**
- Does low-sector positivity close the uniform derivative estimate? **Not established.**
- Do off-diagonal matrix elements automatically suppress the entropy derivative? **No direct first-derivative contribution in the eigenbasis, but they can matter through spectral/eigenvector dynamics and higher orders.**
- Is there a concrete counterexample to the target proposition? **Not established.**

## 6. Disposition

- Full-spectrum entropy derivative spectral-basis identity: **PASS (positive definite case)**.
- Low-spectrum diagonal derivative suppression from current Paper A premises: **OPEN**.
- Pair-flip-to-low-spectrum suppression bridge: **OPEN; not derived here**.
- Uniform logarithmic remainder: **OPEN**.
- Global \(B-C>0\): **not proved**.
- Lean formalization/build: **not performed**.

## 7. Next

IV-24: **Kernel/Tangent-Cone and Rank-Deficient Boundary Audit** — inspect positivity constraints at zero eigenvalues and whether they can be upgraded to quantitative weak-coupling order bounds; attack nonuniform limiting behavior.
