# IV-36 — Frozen-Source Edge Definition Reconciliation

**Target:** AS-ALPHA-A-PROP-0012, (B-C) response ordering at the symmetric point  
**Status:** SOURCE-RECONCILED / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Re-fetch the previously unavailable frozen source at its recorded branch/commit and reconcile the exact response definitions, edge convention, sign, and entropy convention with the current weak-coupling working derivation.

## 1. Source recovery

The previously cited frozen source ref is now accessible for the revised Section 2–5 files of repository `mytheeramet3dev-x/Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`.

Retrieved exact file/blob IDs:
- `Arxiv/paper_01_section_02_revised.md`: `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- `Arxiv/paper_01_section_03_revised.md`: `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- `Arxiv/paper_01_section_04_revised.md`: `a7570431eac62dd4555194df283edb5a9c87a28d`
- `Arxiv/paper_01_section_05_revised.md`: `671c97fa68fa48c929760bf9956d197b358c4904`

The manifest file itself was not retrievable at the recorded path; source recovery is based on the exact section paths and frozen ref, whose blobs were returned above.

## 2. Exact response definitions recovered from Section 5.2

The source explicitly defines
[
A=\frac{\partial I_{12}}{\partial J_{12}},\qquad
B=\frac{\partial I_{12}}{\partial J_{13}},\qquad
C=\frac{\partial I_{12}}{\partial J_{34}},
]
where (J_{13}) shares one endpoint with the observed edge (12), and (J_{34}) is disjoint from edge (12). Thus the target is exactly
[
B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12},
]
at the permutation-symmetric reference point. This matches the target written in the working weak-coupling derivation; no sign reversal or alternate edge labeling is needed.

Section 2.2 defines (I_{ij}=S(\rho_i)+S(\rho_j)-S(\rho_{ij})), with (S(\rho)=-\operatorname{Tr}(\rho\ln\rho)), explicitly using natural logarithms. This convention matches the working derivation.

## 3. Exact symmetry identity

The source Section 5.2 states the response-sector identity
[
\chi_1-\chi_2=(N-2)(B-C),
]
and Section 5.3 states that (B-C>0) is equivalent to response ordering (\chi_1>\chi_2). This is an exact symmetry-level relation; it does not prove the sign.

## 4. Candidate coefficient reconciliation

The corrected displayed-branch candidate from IV-31/32,
[
\frac{J}{8h^2}\ln\!\left(\frac{2(N-2)}{N-1}\right),
]
uses the source's exact (B-C) orientation, edge labels, and natural-log entropy convention. The previously recorded candidate with an extra (+1) is not supported by that leading-branch bookkeeping and remains superseded for this calculation.

This source reconciliation removes the earlier blocker regarding exact target definition and edge convention. It does **not** independently recompute all reduced-density eigenvalue branches or close the remainder estimate.

## 5. Source status statement

The frozen Section 5 explicitly characterizes (B-C>0) as a strong numerically supported conjecture, not an exact theorem. It lists small-N solver/dense-ED agreement, positive scans for (N=4,6,8,10,20), and a tested (h)-scan at (N=8), while excluding unreliable (N=50) near-critical data. It also notes different excited-state/resolvent channels and noncommuting entropy Fréchet terms as the analytic barrier. These source claims are recorded as manuscript statements, not independently reproduced numerical validation in this audit.

## 6. Disposition

- Frozen source sections 2–5 retrieved at the recorded branch/commit: **PASS**.
- Exact target definition (B-C), edge 13 adjacent vs edge 34 disjoint, and sign: **PASS / SOURCE-RECONCILED**.
- Natural logarithm convention: **PASS / SOURCE-RECONCILED**.
- Symmetry identity (\chi_1-\chi_2=(N-2)(B-C)): **PASS / SOURCE-CONFIRMED**.
- Leading candidate formula: source-convention consistent, still unverified beyond displayed perturbative branches.
- Full entropy/remainder proof and Lean verification: **OPEN**.
- No counterexample to the target proposition established.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.