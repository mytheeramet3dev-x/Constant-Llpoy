# MCR-10 — Proposed Redline: Zero-Coupling Product State Versus Entropy Regularity

- **Document ID:** CL-PA-RL-MCR-10
- **Status:** PROPOSED SCOPE CLARIFICATION
- **Affected claim:** AS-ALPHA-A-PROP-0007
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §2.4
- **Source blob:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Correction register item:** MCR-10

## 1. Exact endpoint statement

At zero interaction and \(h>0\), the Hamiltonian is
\[
H(0,h)=-h\sum_{i=1}^N\sigma_i^x.
\]
Its ground state is the product state
\[
|\Psi_0(0,h)\rangle
=\bigotimes_{i=1}^N|+x\rangle_i.
\]
Every one-site and two-site reduced state is pure on its corresponding subsystem product factor, so
\[
I_{ij}(0,h)=0.
\]
Consequently, the zero-coupling configuration is the trivial fixed point of the self-consistency equation.

These are exact endpoint statements.

## 2. What does not follow

At this endpoint the reduced density matrices have zero eigenvalues. The von Neumann entropy contains terms \(-\lambda\ln\lambda\), which are continuous at \(\lambda=0\) but are not differentiable as scalar functions there in the ordinary two-sided sense. Therefore the product-state identity does not, by itself, establish:
- differentiability of \(\mathcal G_N(x)\) at \(x=0\);
- analyticity of mutual information at \(x=0\);
- a finite or prescribed derivative at the endpoint;
- a Taylor expansion obtained by differentiating the entropy formula termwise.

A one-sided expansion may still exist for the actual model, but it requires a separate eigenvalue-branch and entropy-remainder analysis.

## 3. Proposed replacement/qualification

> At \(x=0\), the ground state is the transverse-field product state and the two-site mutual information vanishes: \(\mathcal G_N(0)=0\). This establishes the exact trivial fixed point. No differentiability or analyticity at \(x=0\) is inferred from this endpoint identity; entropy regularity at the rank-deficient reduced states is a separate question.

## 4. Verification obligations

1. Verify the product ground state directly from the decoupled Hamiltonian for \(h>0\).
2. Verify the reduced states and zero mutual information.
3. If a one-sided derivative or asymptotic at \(x=0\) is used elsewhere, prove it independently with explicit eigenvalue and entropy remainder estimates.
4. Keep the endpoint identity separate from the weak-coupling derivative theorem for \(B-C\), which concerns a different quantity and independent edge derivatives.

## 5. Disposition

**PROPOSED CLARIFICATION — EXACT PRODUCT-STATE ENDPOINT; NO ENTROPY-DERIVATIVE CLAIM.**

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
