# IV-25 — Model-Specific Selection-Rule Bridge Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Test whether IV-16/17 pair-flip Taylor support/order results actually control low-spectrum diagonal response in the entropy eigenbasis.

## 1. Starting result from IV-16/17

The pair-flip induction is a fixed-finite-N, local analytic support/order statement in the computational configuration basis: an interaction insertion flips two sites, so after \(n\) insertions the flip set has at most \(2n\) sites; scalar recursion/normalization terms preserve support. The audit records conditional amplitude orders and first edge derivatives. IV-17 reviewed the recurrence adversarially but did not mechanically verify it.

## 2. The bridge that is required

The entropy derivative in the instantaneous eigenbasis depends on
\[
S_u=-\sum_i (\rho_u)_{ii}\ln\lambda_i.
\]
The support induction is expressed for configuration-basis amplitudes and path coefficients. To infer the low-spectrum diagonal response, one needs an explicit construction of the relevant low-eigenvalue eigenspace/projector and a controlled transformation from the computational basis to that spectral subspace. Required elements include:
- a valid reduced density-matrix construction and explicit partial trace;
- spectral identification of the low cluster (not merely its small eigenvalue scale);
- eigenvector/projector or basis-invariant cluster-response estimates;
- bounds on mixing, especially where the low cluster is degenerate or its gap to other eigenvalues is small;
- edge differentiation and remainders preserved through this mapping.

## 3. Why support/order alone does not close the bridge

Support restrictions constrain which configuration-basis coefficients can occur and their perturbative orders. They do not, by themselves, bound the eigenbasis rotation: such bounds generally depend on spectral separation, and near degeneracy a selected eigenbasis can rotate substantially. Even when a cluster projector is stable, cluster-level entropy response still requires a bound on its trace derivative and, for internal entropy, on its normalized spectrum.

No argument in the reviewed IV-16/17 dispositions establishes the above bridge for the target low-spectrum response. This is an audit of the missing implication, not a claim that the implication is false for the Paper A Hamiltonian.

## 4. Adversarial checklist

- Pair-flip support/order premise (conditional fixed-N analytic setup): **PASS as previously audited**.
- Direct implication to low-spectrum eigenbasis diagonal \((\rho_u)_{ii}\): **NOT ESTABLISHED**.
- Eigenbasis mixing controlled uniformly in \(r\): **OPEN**.
- Low-cluster basis-invariant response estimate: **OPEN**.
- Log-weighted entropy remainder: **OPEN**.
- Counterexample to exact target proposition: **not found/ not established**.
- Lean formalization/build: **not performed**.

## 5. Disposition

IV-25 identifies the precise missing bridge: the pair-flip amplitude-support result has not been converted into a low-spectrum entropy-response estimate. Paper A remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**. Do not use the support/order audit as if it proved low-spectrum logarithmic suppression.

## 6. Next

IV-26: **Reduced-Density-Matrix Construction and Partial-Trace Error Audit** — explicitly reconstruct the reduced matrix from the audited amplitudes, check normalization, index ordering, edge-variable differentiation, and the claimed low-spectrum scaling before attempting spectral response.
