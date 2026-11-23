# IV-219 — Higher-Order Odd-Block Reconciliation & Determinant Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling odd two-site block.
**Audit purpose:** Before attempting fresh determinant coefficients, reconcile IV-218 against prior IV-48/49/50 and prevent duplicate or logically premature closure.
**Verdict:** IV-218's Gram/leading-order findings are consistent with the prior record. However, its proposed IV-219 task (compute determinant directly) is premature unless the cubic null-branch coefficient is resolved first. **No new higher-order coefficient is claimed in this audit.**

## 1. Previously established obligations recovered
Inspection of repository main found:
- IV-48: low eigenvalue expansion in leading eigenbasis; cubic coefficient is (B_{vv}), not automatically zero. If it vanishes, the quartic coefficient is (C_{vv}-|B_{uv}|^2/a_+).
- IV-49: global x-parity alone does not establish (B_{vv}=0); cubic null-branch coefficient remains open.
- IV-50: configuration-resolved amplitude bookkeeping formula for cubic block entries; second-order amplitudes and actual cubic null sum have not been evaluated.

These earlier audits were not surfaced in the IV-218 summary. This is a process correction: future rounds must check the prior audit chain before announcing a new obligation.

## 2. Leading Gram reconciliation
IV-218's leading block is the same rank-one matrix in IV-47/48:
\[
O(r)=\frac{N-2}{16}r^2\begin{pmatrix}1&1\\1&1\end{pmatrix}+\cdots.
\]
Its large eigenvalue is (q=(N-2)r^2/8); the null vector is (v=(1,-1)/\sqrt2). Gram PSD is sound for the leading amplitude matrix.

## 3. Why determinant-first is not sufficient
A full determinant identity (lambda_s=\det O/\lambda_L) is exact, but leading rank-one only says the (r^2) determinant coefficient vanishes. It does not determine cubic determinant coefficient or quartic coefficient. The small branch can start at (r^3 B_{vv}) unless a model-specific cancellation is proved. For PSD matrices on (r>0), restrictions on possible signs/order exist, but they do not supply the missing explicit coefficient/edge derivatives. Thus the priority remains computing (B_{vv}) from actual second-order amplitudes, not jumping directly to an (r^4) determinant bound.

## 4. Concrete blocker and next derivation
For each odd-block environment configuration (e), derive the first and second order coefficients of the ground-state amplitude from pair-flip perturbation theory:
\[
c_{\alpha,e}(r)=r a_{\alpha,e}+r^2 b_{\alpha,e}+O(r^3)
\]
for configurations with first-order support. Insert the explicit (a,b) into
\[
O^{(3)}_{\alpha\beta}=\sum_e(a_{\alpha,e}b_{\beta,e}+b_{\alpha,e}a_{\beta,e})
\]
and evaluate
\[
B_{vv}=\tfrac12(O^{(3)}_{11}+O^{(3)}_{22}-O^{(3)}_{12}-O^{(3)}_{21}).
\]
Include all allowed intermediate pair-flip edges, energy denominators, and normalization convention; also differentiate with respect to (u_{13},u_{34}). This is the immediate closure target. Only after (B_{vv}) is resolved should the quartic coefficient and determinant remainder be attempted.

## 5. Status
| Obligation | Status |
|---|---|
| IV-218 leading Gram and rank-one matrix | CONFIRMED, leading order only |
| IV-48 small-branch perturbative formula | RECONCILED |
| IV-49 symmetry argument against automatic cubic cancellation | CONFIRMED |
| IV-50 cubic amplitude-sum bookkeeping | RECONCILED |
| Actual second-order amplitude coefficients (b_{\alpha,e}) | OPEN |
| Cubic null coefficient (B_{vv}) | OPEN |
| Edge derivatives of (B_{vv}) | OPEN |
| Quartic determinant/small-eigenvalue coefficient | DEFERRED |
| Entropy/log derivative remainder | OPEN / CONDITIONAL |
| PROP-0012 fixed-N theorem | OPEN / ANALYTIC-PARTIAL / NOT VERIFIED |

## 6. Decision
**IV-219 is a reconciliation and prioritization audit, not a coefficient-computation round.** The proposed determinant-first IV-219 is deferred because it risks skipping the already identified cubic-null coefficient. Next round should be designated **IV-220: Explicit Second-Order Pair-Flip Amplitudes and Cubic Null-Branch Coefficient**. This is the mathematically correct next step in the existing audit chain.
