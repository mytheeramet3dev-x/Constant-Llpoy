# IV-20 — Aggregate Small-Spectral-Cluster Entropy Derivative Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Audit class:** conceptual/analytic adversarial review; no Lean or source-code proof claimed

## Question

Can entropy of a small spectral cluster be bounded without tracking each eigenbranch through crossings or zero-leading coefficients?

## 1. Cluster formulation

For a positive semidefinite density matrix \(\rho(u,r)\), let \(P(u,r)\) be a spectral projection onto a small cluster, with cluster mass
\[
q=\operatorname{Tr}(P\rho)=\sum_{i\in I}\lambda_i.
\]
Cluster entropy is
\[
S_I=-\sum_{i\in I}\lambda_i\ln\lambda_i.
\]
Writing \(\lambda_i=q\mu_i\), where \(\mu_i\ge0\) and \(\sum_i\mu_i=1\), gives
\[
S_I=-q\ln q+q\,H(\mu),\qquad H(\mu)=-\sum_i\mu_i\ln\mu_i.
\]
This decomposition exposes the mass term and the internal cluster entropy; it does not automatically remove singular derivative behavior in \(\mu\).

## 2. Cluster mass bound is not enough

If \(q=O(r^4)\), this alone does not bound \(q_u\). A differentiated cluster mass estimate is required. When the cluster projection is smooth and isolated, its derivative can be controlled by spectral-gap/projector estimates; those hypotheses and constants must be established for the target system.

## 3. Internal entropy can retain a logarithmic issue

Even if \(q\) and \(q_u\) are controlled, the term \(q H(\mu)\) requires controlling \(H_u\), or using a direct matrix entropy derivative estimate. The normalized cluster spectrum can approach the boundary of the probability simplex; branch crossings may be harmless for the aggregate entropy's continuity but do not, without additional bounds, yield a uniform derivative estimate.

A useful conditional estimate is that for cluster dimension \(m\), \(0\le H(\mu)\le\ln m\). This bounds the entropy value, not its derivative. Thus \(|q_u|\ln m\) controls the derivative of the prefactor contribution only; it does not close \(q H_u\).

## 4. Direct matrix derivative route

For a positive definite matrix \(A(u)\), the derivative of \(\operatorname{Tr}(A\ln A)\) is \(\operatorname{Tr}(A_u(\ln A+I))\). If the cluster spectrum contains eigenvalues approaching zero, \(\ln A\) is unbounded and an estimate must use spectral structure, positivity, cancellations, or a regularized limit. No uniform bound follows merely from a trace norm bound on \(A_u\).

## 5. Cross-cluster normalization and trace cancellation

The full normalized entropy derivative has the identity \(\sum_i\lambda_i'=0\), which cancels the additive \(+1\) terms in the eigenvalue derivative formula when valid. This identity does not bound the remaining \(\sum_i\lambda_i'\ln\lambda_i\), nor justify splitting and discarding a small cluster without a quantified estimate.

## 6. Disposition

- Aggregate mass estimate \(q=O(r^4)\): **insufficient alone**.
- Aggregate derivative estimate \(q_u=O(r^4)\): **separate obligation**.
- Cluster entropy value bound \(H\le\ln m\): **valid but does not bound \(H_u\)**.
- Cluster derivative uniform near internal zero eigenvalues: **OPEN**.
- Smooth isolated cluster projector: **conditional on spectral gap and demonstrated bounds**.
- Branch crossing avoided by aggregation: **partially; eigenvalue labels are unnecessary for the value, but derivative control remains unresolved**.
- Counterexample to exact target proposition: **not established**.
- Lean formalization/build: **not performed**.

## 7. Next audit

IV-21: **Spectral Projection Differentiability, Gap Dependence & Cluster Boundary Audit** — test whether the cluster can be isolated uniformly in the edge parameter, quantify projection derivatives, and attack cluster-boundary crossings and gap collapse.
