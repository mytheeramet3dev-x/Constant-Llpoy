# Strong-Coupling Proof Reconciliation — Model A

**Audit date:** 2026-11-08  
**Scope:** Fixed finite N >= 4, uniform all-to-all TFIM, epsilon = h/J -> 0+, and the response difference B-C = d_{J13} I12 - d_{J34} I12.  
**Purpose:** Reconcile the competing proof-status documents. This is a forensic proof audit, not a replacement proof.  
**Change policy:** No existing proof, manuscript, or claims-ledger file was modified.

## 1. Executive verdict

**Current defensible status: NOT YET A CLOSED THEOREM.**

The repository contains a consistent candidate leading coefficient for the single-site entropy contribution and a plausible perturbative route to fixed-N strong-coupling positivity. It does not, however, contain a complete justified bound on the coupling derivatives of the entropy remainder. The documents that announce a fully closed theorem rely on estimates that are either explicitly withdrawn by the corrected proof, asserted without derivation, or applied outside their established domain.

The strongest safe statement at this audit stage is:

> The formal leading contribution is positive and equals h^2/[J^3(N-1)^3]. Fixed-N asymptotic positivity is a plausible theorem target, but the current repository proof chain does not yet rigorously establish the required remainder estimate for B-C.

This is a conservative proof-status ruling. It is **not** evidence that the claimed theorem is false.

## 2. Documents reconciled

| File | Declared status | Audit finding |
|---|---|---|
| docs/final_fixed_N_corrected_proof.md | Conditional asymptotic proof skeleton; explicit derivative remainder remains open | Most candid account of the remaining gap; its qualitative conclusion still needs a justified derivative asymptotic |
| docs/fixed_N_theorem_hard_audit.md | Theorem, explicit C_N, C_N^(e), D_N | Not closed: complex-domain bounds and differentiated Cauchy estimates are not justified |
| docs/fixed_N_strong_coupling_theorem_report.md | Theorem, explicit constants | Inherits the same unproved complex and derivative estimates |
| docs/strong_coupling_remainder_attack.md | Fully closed theorem, universal M0 <= 10, epsilon* = 1/4 | Real-variable route avoids some complex errors but asserts the central differentiated remainder bound without deriving it |
| docs/lemma_5_1_proof.md | Qualitative fixed-N positivity proved | The derivative-control step is an assertion, not a proof of the needed uniform remainder estimate |
| Arxiv/claims_ledger.md | Global B-C positivity remains conjectural; no closed fixed-N theorem entry | Remains the conservative status authority pending a successful independent proof |

## 3. What survives the reconciliation

### 3.1 Exact model and symmetry setup

For the uniform point:
\[
H=-J\sum_{i<j}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^x,
\qquad J>0,\quad h>0.
\]

The global bit-flip parity P = product_i sigma_i^x commutes with H. At h=0, after restricting to the even parity sector, the cat state is isolated from the first even-sector excitations by the gap 2J(N-1). For fixed finite N, standard isolated-eigenvalue perturbation theory therefore supplies a local analytic ground-state projector in epsilon.

The distinction between the full Hilbert-space ground-state degeneracy at h=0 and the non-degenerate ground state in the selected parity sector must remain explicit.

### 3.2 Candidate small-eigenvalue expansion

The parity-adapted two-qubit reduced state has 2x2 blocks. The repository repeatedly derives the cancellation of the order-epsilon^2 term in the smaller eigenvalue of the even block and the candidate coefficient
\[
\lambda_4=\frac{1}{8(N-2)(N-1)^4}>0.
\]

The coefficient is algebraically consistent with the displayed sum-of-squares expression in the remainder-attack document after substituting b = epsilon/[2(N-1)]. It is a strong candidate exact perturbative coefficient. A final proof should nevertheless rederive it from a single consistent expansion with all normalization and higher-amplitude terms shown.

### 3.3 Leading single-site response coefficient

The one-flip approximation gives
\[
b_1=\frac{h}{2J(N-1)}+O(\epsilon^3).
\]
For a shared edge J13, the leading derivative changes the excitation gap at site 1, while a disjoint edge J34 does not change the leading one-flip gaps at sites 1 and 2. Differentiating the leading single-site entropy term yields
\[
\partial_{J_{13}}S(\rho_1)
=\frac{8h^2}{[2J(N-1)]^3}+\text{higher order}
=\frac{h^2}{J^3(N-1)^3}+\text{higher order}.
\]
This arithmetic is consistent across the lemma and corrected proof.

This is **not yet the full B-C result**: the two-site entropy terms and their coupling derivatives must be controlled to show they cannot contribute at the same or a larger order.

## 4. Fatal gaps in the claimed explicit-constant proof

### 4.1 Invalid complex-domain eigenvalue bound

The hard-audit and theorem-report files use a Cauchy estimate with
\[
\max_{|z|=\rho}|\lambda_{\min}^{(+)}(z)|\le 1.
\]
The bound 0 <= lambda <= 1 is a consequence of rho12 being a positive semidefinite density matrix. It holds for real physical epsilon, not for complex z. For complex z, the analytically continued reduced matrix is generally not Hermitian or positive semidefinite. Therefore this step does not establish the stated C_N.

The corrected proof itself identifies this problem in its comparison of the earlier complex route with the real-variable route. The hard-audit and theorem-report documents nevertheless retain the same kind of complex-domain estimate.

### 4.2 Holomorphic eigenvalue branch not established on the claimed disk

The hard audit asserts entrywise bounds on L_+, S_+, X_+ over a complex disk and then uses them to bound the discriminant. The displayed lower bound reaches zero, not a strict positive separation from the branch cut. Continuity at z=0 alone does not prove the stated numerical bounds on the entire claimed disk.

A valid complex proof would need:
- a proved joint complex domain for the projector and reduced-state entries;
- strict non-vanishing of the discriminant throughout that domain;
- a justified branch choice for the eigenvalue;
- an actual complex-domain bound on the eigenvalue, not the real-density-matrix bound.

Those ingredients are not supplied by the current argument.

### 4.3 Coupling-derivative Cauchy estimate lacks its domain

The hard audit varies J_e in a complex neighborhood and claims a Cauchy derivative bound. It does not establish that the isolated spectral projector and the selected eigenvalue branch remain holomorphic on the required joint domain in (z,J_e), nor that the asserted supremum bound holds there.

The real-variable projector derivative estimate in the corrected proof gives a coarse first-derivative bound. It does **not** imply the order-epsilon^6 bound for the differentiated Taylor remainder. To obtain that order one must control the Taylor coefficients or the relevant higher mixed derivatives uniformly on a real interval, with explicit estimates.

### 4.4 Inconsistent derivative of lambda_4

The hard-audit and theorem-report files state
\[
\partial_{J_{13}}\lambda_4=+\frac{1}{8J(N-1)^5},
\qquad \partial_{J_{34}}\lambda_4=0.
\]
The corrected proof instead gives a negative leading expression for the J13 derivative, followed by unspecified correction terms. These are not reconciled.

Since lambda_4 is a coefficient for the reduced-state eigenvalue under edge perturbations, its derivative must be computed from the general non-uniform-coupling expression before evaluating at the uniform point. The derivative cannot be inferred by differentiating only the uniform closed formula while holding the other coupling variables implicit.

This discrepancy does not by itself disprove positivity of B-C, because this eigenvalue entropy term is expected to enter at higher order. It does invalidate the current claimed explicit entropy constant until resolved.

### 4.5 D_N is not actually closed

The formula for D_N depends on C_N^(e), entropy remainders, and contributions from all small-eigenvalue branches. The corrected proof explicitly marks the derivative constants as missing and D_N as conditional. The hard audit calls them proved, but its derivation relies on the invalid complex estimates above and does not independently close every term.

The remainder-attack document replaces this with a universal M0 <= 10, but does not derive M0 from the full set of matrix, eigenvalue, and entropy derivative estimates. A numerical-looking constant without a traceable inequality chain is not an explicit proof constant.

### 4.6 The claimed epsilon* = 1/4 does not follow

The value epsilon* = 1/4 in the remainder-attack file follows only if its asserted universal remainder constant and all preceding derivative estimates are valid. Since those estimates are not derived, the numerical threshold is unsupported. Other files use different analyticity/radius restrictions, so the admissible domains also need to be reconciled.

## 5. Why the real-variable proof skeleton is not yet enough

The corrected proof is right to avoid applying positivity bounds to complex epsilon. But the replacement argument stops at the crucial point:

- It identifies analyticity of the ground-state projector and reduced state for real epsilon.
- It identifies the order-epsilon^4 leading small eigenvalue.
- It recognizes that entropy derivatives contain a logarithm near a vanishing eigenvalue.
- It explicitly leaves the differentiated remainder constants C_N^(13), C_N^(34) open.

The remainder-attack file then asserts
\[
|R|+J|\partial_{J_{13}}R|+J|\partial_{J_{34}}R|
\le K_N\frac{h^4}{J^5}(1+|\ln\epsilon|)
\]
and M0 <= 10, but does not derive these bounds from the Neumann series or a complete differentiated expansion.

The lemma_5_1_proof.md has the same logical gap: the statement that small eigenvalues are O(epsilon^4) does not by itself imply their coupling derivatives are O(epsilon^4/J). That derivative estimate requires a separate mixed-parameter perturbation argument. Moreover, the entropy derivative near zero must be treated branch by branch, including any eigenvalue that vanishes at the symmetric point and opens under an edge perturbation.

## 6. Important correction: qualitative positivity is not automatic from analyticity

The corrected proof's final qualitative argument says B-C is real-analytic in epsilon at epsilon=0. That claim is not justified as written.

The density matrix entries and isolated eigenvalue branches can be analytic, but von Neumann entropy contains -lambda ln(lambda). If a small eigenvalue behaves as c epsilon^4 + higher terms, its entropy contains an epsilon^4 ln(epsilon) term. Thus the entropy, and potentially B-C, need not be analytic at epsilon=0.

This does **not** prevent qualitative positivity. A sufficient route is to prove the actual asymptotic expansion
\[
B-C=\frac{\epsilon^2}{J(N-1)^3}
+O_N\!\left(\frac{\epsilon^4(1+|\ln\epsilon|)}{J}\right),
\]
with the remainder estimate justified after differentiating with respect to J13 and J34. Since epsilon^2 |ln epsilon| -> 0, this would prove positivity for sufficiently small positive epsilon. But the derivative remainder estimate is precisely what remains to be established.

## 7. Reconciled status ledger

| Claim | Reconciled status | Reason |
|---|---|---|
| Isolated parity-sector ground-state projector is analytic near epsilon=0 for fixed N | PROVEN under the stated gap and fixed-N assumptions | Standard isolated-eigenvalue perturbation theory |
| Parity block decomposition of rho12 | PROVEN under the global parity symmetry | Exact symmetry argument |
| Cancellation of the epsilon^2 coefficient in the selected small eigenvalue | PROVISIONAL_EXACT_DERIVATION | Algebra displayed; should be independently rederived in one canonical calculation |
| lambda_4 = 1/[8(N-2)(N-1)^4] | PROVISIONAL_EXACT_DERIVATION | Consistent algebraically across the perturbative documents; derivative data inconsistent |
| Leading single-site contribution h^2/[J^3(N-1)^3] | PROVEN_LEADING_CONTRIBUTION | Direct one-flip derivative arithmetic |
| Full expansion of B-C with O(epsilon^4 log epsilon) differentiated remainder | OPEN_PROOF_OBLIGATION | Current derivative estimates are asserted or rely on invalid bounds |
| Qualitative fixed-N B-C > 0 for sufficiently small epsilon | NOT YET PROVEN IN REPOSITORY | Would follow from the missing full differentiated asymptotic |
| Explicit C_N and C_N^(e) | NOT ESTABLISHED | Complex-domain and mixed-derivative estimates fail |
| Explicit D_N | NOT ESTABLISHED | Depends on unproved derivative/entropy bounds |
| epsilon_N* = 1/4 | NOT ESTABLISHED | Depends on unsupported M0 <= 10 and inconsistent domains |
| Global B-C > 0 on the physical branch | CONJECTURE | No global proof |

## 8. Required proof closure plan

Do not patch the old theorem documents by changing status labels only. Build one canonical derivation in this order:

1. **General-coupling perturbation setup:** Write the perturbation coefficients as functions of all J_ij in a neighborhood of the uniform point. State the parity-sector gap and the allowed coupling domain.
2. **Reduced-state expansion:** Derive rho12 and every relevant eigenvalue through the order needed, including the dependence on J13 and J34. Keep the two parity blocks separate.
3. **Mixed derivative control:** Prove bounds for partial_{J_e} of the eigenvalue coefficients and the Taylor remainder. Do not infer derivative bounds from an undifferentiated O(epsilon^k) statement.
4. **Entropy expansion:** Apply -lambda ln(lambda) to each eigenvalue branch with explicit lower/upper bounds and directional derivative control. Treat zero eigenvalues at the symmetric point separately.
5. **Full response subtraction:** Combine the single-site and two-site entropy terms and establish the full B-C expansion with a justified remainder.
6. **Qualitative positivity first:** Prove existence of some epsilon_N*>0 by asymptotic dominance. An explicit numerical value is not required for this theorem.
7. **Quantitative threshold second:** Only then derive explicit constants and a computable epsilon_N* if useful.

An independent symbolic derivation and a small-N numerical finite-difference check can be used as diagnostics, but neither substitutes for the analytic inequalities.

## 9. Repository action and decision

- No existing theorem report, proof file, manuscript, or claims ledger was overwritten.
- This reconciliation is a new audit record.
- The project should **not** currently cite the fixed-N strong-coupling positivity as a proved theorem.
- The next mathematical task is the general-coupling expansion and differentiated entropy remainder, not Lean formalization of the theorem. Lean should wait until the theorem statement and assumptions are stable.

**Final audit verdict: THEOREM CLAIM WITHDRAWN PENDING PROOF CLOSURE.**  
**Research direction retained: STRONG-COUPLING POSITIVITY REMAINS A LIVE, PLAUSIBLE THEOREM TARGET.**
