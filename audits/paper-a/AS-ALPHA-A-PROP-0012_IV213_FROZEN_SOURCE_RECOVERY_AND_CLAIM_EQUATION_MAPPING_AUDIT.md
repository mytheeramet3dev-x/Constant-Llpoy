# PROP-0012 — IV-213 Frozen Source Recovery and Claim-to-Equation Mapping Audit

**Date:** 2026-11-23  
**Target:** `AS-ALPHA-A-PROP-0012`  
**Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Audit type:** Source recovery, exact frozen-source cross-check, equation/claim mapping  
**Status:** FROZEN_SOURCE_RECOVERED; CLAIM_TO_EQUATION_MAPPING_PARTIAL; MATHEMATICAL_CLAIM_OPEN

## 1. Recovery result

IV-212's inaccessible-source blocker is superseded for this audit session. The frozen revision was fetched successfully through GitHub API/raw endpoints. The tree at the pinned commit confirms the six revised manuscript files. The recovered Sections 4, 5, and 6 are identified by their frozen blob IDs:

- Section 4: `Arxiv/paper_01_section_04_revised.md`, blob `a7570431eac62dd4555194df283edb5a9c87a28d`
- Section 5: `Arxiv/paper_01_section_05_revised.md`, blob `671c97fa68fa48c929760bf9956d197b358c4904`
- Section 6: `Arxiv/paper_01_section_06_revised.md`, blob `5e734065c2ddd42ee602dada89e7455d2ad9e7a0`

The source recovery is real and directly changes the prior access status. This audit does not treat accessible `main` as a substitute: the fetched files are pinned to the previously frozen commit.

## 2. Exact target statement

Section 4.4.3 states:

> “A weak-coupling perturbative expansion (x → 0, Lemma 5.2) further confirms that this lower branch possesses distinct scaling and opposite-sign response characteristics compared to the physical stable branch.”

This statement contains multiple parts that must not be conflated:
1. a weak-coupling perturbative expansion exists and is correctly sourced to Lemma 5.2;
2. the expansion applies to the lower fixed-point branch/domain;
3. it establishes a response-sign contrast relative to the physical stable branch;
4. the asserted contrast is sufficient for the branch-level interpretation in the manuscript.

The recovered manuscript wording alone does not supply the detailed response observable, the exact lower-branch response derivative being compared, or the explicit derivation of the sign comparison.

## 3. Frozen Section 5 cross-check

The recovered Section 5.2 defines, at the permutation-symmetric point:

[
A=\partial_{J_{12}}I_{12},\quad
B=\partial_{J_{13}}I_{12},\quad
C=\partial_{J_{34}}I_{12},
]

where edge 13 shares an endpoint with edge 12, while edge 34 is disjoint.

It also gives the exact identity

[
\chi_1-\chi_2=(N-2)(B-C).
]

Section 5.3 explicitly classifies the sign (B-C>0) as a strong numerically supported conjecture, not an exact theorem, and explains that permutation symmetry alone does not order the reduced matrix elements/resolvent channels.

These statements corroborate the target response vocabulary and the observable (B-C), but they do **not** by themselves establish the lower-branch weak-coupling sign comparison asserted in Section 4.4.3.

## 4. Frozen-source correspondence of IV-211 reconstructed root equation

IV-211/212 worked with the reconstructed equation

[
\Phi(d;t,p)=d-4-R(d,t,p),\
R=\frac{16t(d^2-16mt)}{d(d^2-16t)},\
m=(2p-1)^2,
]

on a compact parameter box, with root interval ([4,256/63]).

In the recovered Sections 4–6, the Paper A fixed-point equation is instead written in the mutual-information variable:

[
F(J;g,h)=gI_{12}(J,h)-J=0,
]

and its dimensionless form uses

[
f(x;\eta)=\eta\mathcal G_N(x)-x=0,
\qquad x=J/h,\
\eta=g/h.
]

The recovered target text does not identify variables (d,t,p), nor state the IV-211 rational root equation (\Phi=0), its parameter box, or its root interval. No derivation or change-of-variables bridge from (F/f) to (\Phi) is present in the recovered Sections 4–6.

**Disposition:** The IV-211 equation remains a reconstructed/conditional mathematical object. Its endpoint, root uniqueness, derivative bounds, and branch coverage cannot be promoted as Paper A source-level proof evidence based on this source recovery.

## 5. Claim-to-equation mapping status

| Obligation | Status | Reason |
|---|---|---|
| Frozen Section 4.4.3 wording recovered | PASS | Exact pinned file fetched and blob identity is confirmed by tree |
| Frozen Sections 5.2–5.3 recovered | PASS | Definitions, sector identity, and conjecture status accessible |
| Observable (B-C) definition | PASS | Section 5.2 explicit derivative definitions |
| Exact sector identity | PASS (source statement; independent proof not re-audited here) | (chi_1-chi_2=(N-2)(B-C)) |
| Lower-branch response observable explicitly mapped to IV-211 variables | OPEN | No mapping in recovered text |
| IV-211 reconstructed rational equation derived from frozen Paper A | NOT ESTABLISHED | Source contains no (d,t,p) equation/bridge in recovered sections |
| Weak-coupling branch-sign statement proven from Lemma 5.2 | OPEN / SOURCE SUPPORT INSUFFICIENT | Section 4.4.3 cross-references Lemma 5.2, but exact derivation and sign comparison are not closed by recovered manuscript sections |
| PROP-0012 theorem status | OPEN / NOT VERIFIED | No complete claim proof, no formal verification |

## 6. Corrected epistemic status after source recovery

IV-212's source-access blocker is now **RESOLVED for the frozen revised manuscript sections** in this audit. This does not retroactively validate IV-211.

- Conditional algebraic results of IV-211 remain valid only for its reconstructed equation and assumptions, subject to their stated calculations.
- Their source correspondence remains unestablished.
- The target weak-coupling opposite-sign response statement remains OPEN.
- No theorem promotion, Lean proof, or full formalization is claimed.

## 7. Next required work

The next audit should perform a line-level mathematical reconciliation of the frozen Section 4.4.3 reference to Lemma 5.2 with the exact frozen supporting proof/audit files (if those files are available at the pinned revision), and identify the precise response derivative, branch parametrization, and remainder bounds needed to prove or refute the asserted sign comparison. Do not continue tightening IV-211 bounds unless a valid source-to-equation bridge is first established.
