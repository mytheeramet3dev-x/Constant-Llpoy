# IV-24 — Kernel/Tangent-Cone and Rank-Deficient Boundary Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** local matrix-positivity analysis; no mechanized proof claimed

## 1. Positivity at a rank-deficient point

Let \(\rho(u_0)\succeq0\) be differentiable and have a kernel. For a two-sided differentiable PSD path, the first derivative restricted to the kernel must vanish in the kernel-to-kernel block at the base point; a one-sided path instead has a tangent-cone positivity condition on that block. This is a pointwise geometric constraint, not a weak-coupling rate estimate.

## 2. Cross-block derivatives are not automatically zero

Positivity does not force all derivative entries involving the kernel to vanish. For example,
\[
\rho(t)=\begin{pmatrix}1&t\\t&t^2\end{pmatrix}
=\begin{pmatrix}1\\t\end{pmatrix}\begin{pmatrix}1&t\end{pmatrix}
\succeq0
\]
has a rank-one base point at \(t=0\) and a nonzero cross-block derivative there. Thus tangent-cone constraints alone do not suppress every matrix element touching the kernel.

## 3. No quantitative weak-coupling order from tangent geometry alone

The tangent constraints are local in the path parameter and do not establish a uniform \(r\)-order for low-spectrum diagonal derivatives. To obtain an estimate such as \((\rho_u)_{ii}=O(r^p)\), one must use the specific Hamiltonian/edge perturbation structure and a uniform expansion or selection rule. Those ingredients must be explicitly linked to the low-spectrum directions.

## 4. Entropy boundary caveat

The matrix entropy is continuous at rank loss, but its derivative can have logarithmic sensitivity to small eigenvalues. Positivity constraints at the boundary do not alone give the needed uniform bound for \(\operatorname{Tr}(\rho_u\ln\rho)\). Limiting arguments must quantify both the eigenvalue scale and response in the corresponding subspace.

## 5. Adversarial findings

- Kernel-to-kernel derivative constraint at a two-sided PSD base point: **PASS (local tangent fact)**.
- One-sided tangent-cone positivity: **PASS (local condition)**.
- Cross-block response forced to vanish: **FAIL (counterexample matrix path above)**.
- Quantitative weak-coupling suppression from positivity alone: **FAIL (not implied)**.
- Uniform entropy derivative at rank-deficient boundary: **OPEN**.
- Counterexample to target proposition: **not established**.

## 6. Disposition

IV-24 blocks the shortcut from positivity/tangent geometry to quantitative low-spectrum response suppression. The target proof must derive the needed rate from model-specific perturbative structure or show a verified aggregate cancellation.

No Lean formalization/build has been performed.

## 7. Next

IV-25: **Model-Specific Selection Rule Bridge Audit** — revisit the pair-flip support/order induction and test whether it rigorously controls the low-spectrum diagonal response entering the entropy derivative, with explicit basis identification and uniform remainder bookkeeping.
