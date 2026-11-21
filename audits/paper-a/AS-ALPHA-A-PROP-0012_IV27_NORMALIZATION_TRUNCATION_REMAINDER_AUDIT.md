# IV-27 — Normalization and Truncation-Remainder Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Reconcile normalization of the perturbative state, truncation orders, and differentiated remainder claims in the current weak-coupling ledger.

## 1. Exact normalization versus truncated amplitudes

For exact amplitudes \(c_F(r,\mathbf u)\), normalization requires \(\sum_F|c_F|^2=1\). A finite perturbative truncation generally does not satisfy this identity exactly. A normalized analytic state may be obtained by dividing an analytic unnormalized vector by its norm; this changes the vacuum amplitude and can affect reduced-matrix entries and derivatives at orders that must be tracked.

The current working derivation uses \(c_\emptyset=1+O_N(r^2)\) and shared-amplitude cancellation, while some intermediate expressions are described as exact environment sums. This is compatible only if the exact normalized amplitudes are distinguished from truncated expansions and the claimed error orders are propagated consistently.

## 2. Normalization correction orders

If the unnormalized vector has norm squared \(1+O_N(r^2)\), normalization multiplies all amplitudes by a scalar \(1+O_N(r^2)\). The first-order pair amplitudes remain \(a_{ij}+O_N(r^2)\), but the correction's edge derivatives also need explicit order estimates. Scalar normalization preserves configuration support, but it does not automatically preserve every asserted differentiated remainder without bookkeeping.

## 3. Truncation and edge differentiation

For a jointly analytic finite-dimensional family, Taylor remainders can be differentiated with respect to edge variables when the expansion is joint and the neighborhood is controlled. However, a displayed amplitude remainder \(O_N(r^k)\) alone is not sufficient to conclude \(\partial_{u_e}O_N(r^k)=O_N(r^k)\) unless the remainder estimate is uniform in the edge neighborhood and differentiability is included. The prior pair-flip audit states such derivative-order claims conditionally; this pass does not mechanize that recurrence.

## 4. Entropy sensitivity

Normalization and truncation errors in a small eigenbranch cannot be translated directly into entropy errors without controlling the branch's logarithmic scale and its differentiated remainder. For \(\lambda_s=O_N(r^4)\), the size alone does not guarantee \(\partial_u\lambda_s=O_N(r^4)\) or a uniform bound on \(\partial_u(\lambda_s\ln\lambda_s)\). The working derivation explicitly makes these estimates conditional on amplitude-order/tail hypotheses; they are not upgraded here.

## 5. Adversarial findings

- Exact normalized-state identity and finite partial trace: **PASS (identity)**.
- Scalar normalization preserves support: **PASS (algebraic)**.
- All differentiated remainder orders from current ledger independently established: **NOT ESTABLISHED**.
- Truncation remainders uniformly differentiated in edge variables: **OPEN**.
- Normalization effects closed through the low-spectrum logarithmic entropy derivative: **OPEN**.
- Counterexample to target proposition: **not established**.
- Lean formalization/build: **not performed**.

## 6. Disposition

IV-27 finds no algebraic contradiction in normalization as used by the working derivation, but the normalization/truncation derivative bookkeeping is not independently closed. The exact normalized amplitude sums and their truncated expansions must be kept distinct in subsequent calculations. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 7. Next

IV-28: **Edge-Derivative Remainder Uniformity Audit** — isolate the joint analyticity domain, Taylor remainder estimates, and differentiation with respect to independent edge variables to determine which derivative-order statements are genuinely uniform.
