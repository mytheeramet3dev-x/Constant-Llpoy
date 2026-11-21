# THM-0002 — Corrected Perron–Frobenius Proof Closure Review

**Claim:** AS-ALPHA-A-THM-0002, finite-N TFIM ground-state nondegeneracy.  
**Frozen source:** Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`, §2.1.  
**Working proof reviewed:** `working/paper-a/AS-ALPHA-A-THM-0002_pf_corrected_working_proof.md` (Constant-Llpoy main).  
**Audit type:** Independent mathematical review of the corrected proof route and status cross-check; no Lean build was executed.

## Verdict

**ANALYTIC-PASS (finite-dimensional theorem, proof route); FORMALIZATION-INCOMPLETE.**

The corrected working proof is mathematically sound under the stated finite-(N), real-coupling, (h>0) hypotheses. It closes the conceptual PF argument in ordinary finite-dimensional mathematics. It does not close the Lean implementation or amend the frozen manuscript.

## 1. Hamiltonian and shifted matrix

For
[
H=-sum_{i<j}J_{ij}Z_iZ_j-hsum_iX_i,
]
the computational (Z)-basis interaction is diagonal and real. Off-diagonal matrix entries are (-h) exactly for pairs of bitstrings differing at one coordinate, and zero otherwise. Choosing (cgemax_s H_{ss}) and setting (K=cI-H) makes the diagonal nonnegative and the single-flip entries (+h>0); all other entries are zero. Thus (Kge0) entrywise.

The source's phrasing “shift the Hamiltonian upward” is sign-inconsistent with this construction: (H+cI) does not make the negative single-flip entries nonnegative. The corrected manuscript should say shift the negative Hamiltonian by forming (cI-H), or equivalently apply PF to (-H) after a suitable diagonal shift.

## 2. Irreducibility

The positive off-diagonal support of (K) is the single-spin-flip graph on bitstrings, i.e. the (N)-dimensional hypercube. For finite (Nge1), it is connected. Since (h>0), every hypercube edge has strictly positive weight. Therefore (K) is irreducible as a nonnegative matrix. This argument does not require (J_{ij}ge0); the couplings only affect the diagonal.

## 3. Perron eigenvalue and ground-state correspondence

Because (K) is real symmetric, its eigenvalues are real and its spectral radius equals its largest eigenvalue. PF for an irreducible nonnegative matrix gives a simple spectral-radius eigenvalue with a strictly positive eigenvector. Since
[
K=cI-H,qquad lambda_k(K)=c-E_k(H),
]
the largest eigenvalue of (K) corresponds exactly to the smallest eigenvalue of (H). The PF simplicity/positive eigenvector therefore gives a simple TFIM ground eigenvalue and strictly positive ground vector in the computational basis.

## 4. Lean status (not closed)

The reviewed Lean core contains the conditional propagation/simplicity route and model structural lemmas, but the audit baseline still lacks a demonstrated theorem constructing a nonnegative eigenvector at the maximal eigenvalue and a complete theorem tying that result to the ground-state eigenspace. No build was run in this pass. Therefore do not mark the full manuscript theorem as Lean-verified.

## 5. Scope

- Valid for finite (Nge1), arbitrary finite real (J_{ij}), and (h>0).
- Does not imply reduced-state eigenvalues are strictly positive or entropy differentiability at rank-deficient endpoints.
- Does not prove any saddle-node curvature, response-sector ordering, or thermodynamic-limit result.
- Frozen source remains unchanged; correction is tracked separately.

**Disposition:** corrected analytic proof route passes; manuscript sign wording requires correction; Lean closure remains open.
