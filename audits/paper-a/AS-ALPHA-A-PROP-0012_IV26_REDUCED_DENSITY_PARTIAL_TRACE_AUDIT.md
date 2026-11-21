# IV-26 — Reduced-Density-Matrix Construction and Partial-Trace Error Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Recheck IV-14 reduced-matrix formulas against the working derivation using explicit partial trace, basis/index convention, normalization, and edge differentiation.

## 1. General exact partial-trace identity

For a bipartite pure state \(|\Psi\rangle=\sum_{a,b}c_{a b}|a\rangle_S|b\rangle_E\), the reduced matrix is
\[
(\rho_S)_{aa'}=\sum_b c_{ab}\overline{c_{a'b}}.
\]
This Gram-matrix formula is exact. It implies Hermiticity and positive semidefiniteness; trace equals the full state norm and equals one only if the state coefficients are normalized.

## 2. One-site audit

The one-site probability of the flipped x-basis state is the sum of squared amplitudes over all environment configurations with that site flipped. At leading perturbative order, only single-pair amplitudes contribute:
\[
p_i=\sum_{j\ne i}|a_{ij}|^2+\text{higher-order terms},
\quad a_{ij}=J_{ij}/(4h).
\]
At the uniform point the leading term is \((N-1)r^2/16\). Differentiating the leading term with respect to the incident edge \(u_{13}\) gives \(r^2/8\) for site 1; site 2 has no direct leading contribution from that edge. This agrees with IV-14, subject to its perturbative remainder and fixed-finite-N scope.

## 3. Two-site odd block and environment labels

With two-site basis \((|+-\rangle,|-+\rangle)\), environment configurations must have odd flip parity under the ground-state parity selection. The leading environment configurations are single flips at \(k\ge3\). Their amplitudes are respectively \(a_{2k}\) and \(a_{1k}\), so the leading odd-block Gram matrix has diagonals \(\sum_{k\ge3}|a_{2k}|^2\), \(\sum_{k\ge3}|a_{1k}|^2\), and cross term \(\sum_{k\ge3}a_{2k}\overline{a_{1k}}\) (up to basis-convention conjugation). At uniform coupling this is the rank-one matrix with eigenvalues \((N-2)r^2/8\) and zero to leading order. Direct leading differentiation gives the adjacent-edge coefficient \(r^2/8\); a disjoint edge is absent at this order. Index ordering is consistent with IV-14 under the stated basis convention.

## 4. Even block: exact environment Gram sums and Schur complement

For system states \(++\) and \(--\), the environment is even-flip. Exact block entries are environment Gram sums \(L=\sum_E|c_E|^2\), \(X=\sum_Ec_E\overline{c_{E\cup\{1,2\}}}\), \(S=\sum_E|c_{E\cup\{1,2\}}|^2\), with environment index range restricted to valid configurations and amplitudes understood in the full normalized state. This is an exact partial trace, not a truncated formula.

Separating the empty environment produces a shared-amplitude rank-one outer-product contribution. Its determinant cancellation is exact algebraically. The residual Schur quantity \(D=S-|X|^2/L\) is nonnegative when \(L>0\), but its claimed \(O_N(r^4)\) value and edge derivative require the stated amplitude-order/tail estimates. IV-26 independently checks the algebraic cancellation only, not those order estimates.

## 5. Normalization, Hermiticity, and differentiation

- Exact partial trace preserves Hermiticity and PSD.
- Trace of reduced state equals trace of the full state; it is 1 only for normalized amplitudes. Perturbative truncated states need normalization corrections if used beyond their claimed order.
- Edge differentiation commutes with the finite environment sum when amplitudes are differentiable; derivative estimates still require uniform remainder control.
- Leading Gram-matrix derivatives are internally consistent. The higher-order remainder in IV-14 is not independently closed here.

## 6. Disposition

- Exact partial-trace Gram formula: **PASS**.
- One-site leading coefficient/indexing: **PASS (conditional perturbative setup)**.
- Odd-block environment parity/index convention and leading Gram matrix: **PASS (leading order)**.
- Even-block shared-amplitude determinant cancellation: **PASS (algebraic identity)**.
- Normalization of the full state in higher-order remainder ledger: **OPEN for independent audit**.
- Higher-order branch/tail orders and differentiated remainders: **OPEN; not re-proved here**.
- No counterexample to exact target proposition established; no Lean proof/build.

**Important scope note:** The IV-14 direct reconstruction was internally consistent at the displayed leading orders. This audit does not upgrade its conditional higher-order estimates or close the low-spectrum entropy derivative.

## 7. Next

IV-27: **Normalization and Truncation-Remainder Audit** — independently reconcile exact normalization, perturbative amplitude truncation, and derivative remainder order in the entropy ledger.
