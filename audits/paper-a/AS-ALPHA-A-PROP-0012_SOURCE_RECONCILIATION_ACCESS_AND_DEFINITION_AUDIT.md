# PROP-0012 — Source Reconciliation Access & Definition Audit

**Date:** 2026-11-21
**Target frozen Paper A source:** repository `mytheeramet3dev-x/Absolute_Sym`, branch `paper-a-interval-audit-2026-11-14`, expected frozen commit from audit context `8deb7de4a49cb2060720246b7101820ee7e08c91`.
**Audit scope:** Verify definitions of B and C, and attempt to reconcile the weak-coupling derivation and recent even-block remainder closure against the frozen manuscript. No Lean formalization/build.

## 1. Frozen-source access result

The source repository metadata is accessible and identifies `Absolute_Sym` as a private repository. The repository's current `main` branch README identifies the Paper A package at `Alphabet/paper_a/` and describes the audit branch as `paper-a-interval-audit-2026-11-14`, with a different referenced commit prefix `6e741d7`.

However, content fetches for the frozen manuscript using the audit branch and the frozen commit reference returned GitHub API 404/NOT FOUND. Fetching the manuscript from `main` succeeds, but `main` is not the frozen audit source and is not substituted for it. This prevents a complete source-to-proof reconciliation.

## 2. Definition cross-check on accessible main manuscript (NOT frozen source)

The accessible current-main manuscript Section 5.2 explicitly defines
`A=\partial_{J_{12}}I_{12}`, `B=\partial_{J_{13}}I_{12}`, and `C=\partial_{J_{34}}I_{12}` at the symmetric point, where edge 13 shares one endpoint with edge 12 and edge 34 is disjoint. Section 5.3 states that the sign of `B-C` orders the two nontrivial response sectors and labels `B-C>0` a numerically supported conjecture, not a theorem.

This is consistent with the working target definition of `B-C` as the difference between adjacent-edge and disjoint-edge derivatives. It is a cross-check of accessible main-branch definitions only.

## 3. Hamiltonian and scale-convention cross-check (accessible main)

The accessible manuscript gives the all-to-all TFIM convention
[
H[J]= -\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^x
]
and symmetric dimensionless coupling `x=J/h`. The working derivation uses `r=J/h`, `J_{ij}=J(1+u_{ij})`, and pair-flip interaction in the x-basis, which is structurally consistent with that accessible Hamiltonian convention.

**Limitation:** The exact frozen-source wording, definitions, normalization conventions, and target remainder order have not been compared because the frozen manuscript could not be fetched. The current-main comparison cannot establish that the frozen paper contains precisely these definitions/assumptions.

## 4. Reconciliation verdict

- **B/C definitions:** VERIFIED AGAINST ACCESSIBLE MAIN ONLY; frozen-source reconciliation BLOCKED.
- **Hamiltonian/sign convention:** STRUCTURALLY CONSISTENT AGAINST ACCESSIBLE MAIN; frozen-source reconciliation BLOCKED.
- **Even-block O(r^4) claim:** ANALYTIC-PARTIAL / CONDITIONAL, not promoted. The source's exact entropy branches and required remainder are not yet reconciled.
- **PROP-0012:** remains OPEN. No full source-reconciliation pass, no global B-C sign theorem, and no Lean verification are claimed.

## 5. Next requirement

Restore readable access to the frozen audit branch/commit (or provide a stable source snapshot in the independent audit workspace). Then compare the exact Section 5.2–5.3 definitions and relevant entropy expansion lines against the working derivation, including each branch, edge derivative, remainder, and convention, and record any discrepancy before changing status.
