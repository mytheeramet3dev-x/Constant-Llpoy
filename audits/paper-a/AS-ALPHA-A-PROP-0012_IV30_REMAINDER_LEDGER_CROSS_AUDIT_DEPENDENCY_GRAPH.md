# IV-30 — Remainder Ledger Cross-Audit and Dependency Graph

**Target:** AS-ALPHA-A-PROP-0012, candidate weak-coupling edge-response sign \(B-C\  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Cross-check dependencies, assumption reuse, and circularity risks across the working derivation and prior audits. This is a document-level audit, not an independent reconstruction of every coefficient.

## 1. Dependency graph (current proof route)

\[
\text{Hamiltonian + edge parametrization}
\to \text{isolated ground projector}
\to \text{amplitude support/order}
\to \text{partial trace blocks}
\to \text{small eigenvalue estimates}
\to \text{entropy derivatives}
\to \partial_{u_{13}}I-\partial_{u_{34}}I.
\]

Each arrow carries distinct obligations. A downstream conclusion cannot be promoted above the assumptions supporting its input.

## 2. Remainder ledger

| Item | Current source/claim | Cross-audit disposition | Downstream dependency |
|---|---|---|---|
| Ground projector analyticity | IV-29, working setup; finite N, gap 2h at r=0 | Standard finite-dimensional principle PASS; quantitative common neighborhood OPEN | Uniform edge-derivative remainder |
| Pair-flip support/order | IV-16/17 claimed induction; working derivation uses orders for c_E and first derivatives | Conditional on induction details and normalization/analytic neighborhood; no fresh full recurrence verification here | Even-block environment sums |
| First-order amplitudes a_ij | Working derivation, a_ij=J_ij/(4h) | Leading coefficient stated; independently recomputed sign/convention not cross-checked against full Hamiltonian definition in this audit | One-site/odd-block leading terms |
| One-site small eigenvalues p_i | Working derivation: sum w_ij + O_N(r^3), with differentiated form | Conditional on amplitude expansion and uniform C^1 remainder | Binary entropy derivatives |
| Odd 2-site block | Leading Gram matrix and simple positive branch | Leading algebra structurally consistent; remainder C^1 uniformity depends on joint analytic neighborhood | q ln q entropy derivative |
| Even block shared-amplitude cancellation | Exact environment sums; D=S-|X|^2/L | Algebraic Schur cancellation is valid for L>0; order D=O(r^4), D_u=O(r^4) depend on amplitude orders and C^1 bounds | Small even-block eigenvalue entropy |
| Normalization | IV-27 | Scalar normalization preserves support/order structurally; derivative remainder needs uniform neighborhood | All reduced density estimates |
| Spectral small branches | IV-18/19/20/21/22/23/24/25 | Branch-specific logarithm, cluster, projector, kernel, and low-spectrum derivative controls remain conditional/open | Entropy derivative remainder |
| Entropy assembly | Working candidate and IV-18–25 | Large branches/positive branches plausible under stated bounds; zero/low branches not fully closed across all blocks | Final B-C remainder |
| Final sign | Candidate coefficient \(\frac{J}{8h^2}[1+\ln\frac{2(N-2)}{N-1}]\) | Leading expression not independently rederived in IV-30; strict sign follows algebraically if coefficient and asymptotic remainder are valid | Proposition conclusion |

## 3. Circularity / assumption-reuse checks

- **No proven circular identity identified from the inspected working document.** The even-block cancellation is algebraic and uses the shared amplitude \(c_{12}\), not an assumed first-order-only value.
- The pair-flip support/order lemma is an upstream assumption in the even-block remainder ledger. Its downstream use is not independent evidence for the lemma.
- Analyticity supplies a derivative estimate only when a common neighborhood and uniform remainder bound are available; IV-28/29 clarify the principle but do not certify every remainder term.
- Small eigenvalue order and entropy derivative order are distinct obligations. IV-18–24 show that \(\lambda=O(r^4)\) alone does not close \(\lambda_u\ln\lambda\).
- Partial trace and leading block calculations do not, by themselves, establish the differentiated high-order remainder.
- The final sign is conditional on both the leading coefficient derivation and a remainder small enough relative to it.

## 4. IV-30 findings

**PASS (structural):** dependency graph is coherent; shared-amplitude Schur cancellation avoids one identified shortcut; no explicit circular equality found in the inspected derivation.

**OPEN:** independent verification of pair-flip recursion with normalization and edge differentiation; common C^1/holomorphic remainder radius; complete small-spectrum entropy derivative closure; independent reconstruction of final leading coefficient and sign.

**NOT CLAIMED:** proof of PROP-0012; counterexample; Lean formalization or build.

## 5. Current proposition status

\[
\boxed{\text{OPEN / ANALYTIC-PARTIAL / NOT VERIFIED}}
\]

## 6. Next audit

IV-31: **Leading-Coefficient Independent Reconstruction Audit** — reconstruct the proposed coefficient from the one-site and two-site entropy derivative terms independently of the working derivation, and compare signs, factors, logarithm arguments, and cancellations. This checks whether the leading coefficient itself is internally consistent before further remainder work.
