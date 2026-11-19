# MCR-12 — Proposed Redline: Retire Duplicate Subcritical Proposition

- **Document ID:** CL-PA-RL-MCR-12
- **Status:** EDITORIAL PROPOSAL; CLAIM TRACEABILITY MUST BE PRESERVED
- **Affected claim:** AS-ALPHA-A-PROP-0008
- **Related claim:** AS-ALPHA-A-PROP-0001
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §2.5
- **Source blob:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Correction register item:** MCR-12

## 1. Duplication finding

PROP-0008 repeats the subcritical exclusion already contained in PROP-0001:
\[
\eta<\alpha_N
\quad\Longrightarrow\quad
f(x;\eta)<0\quad\text{for all }x>0,
\]
under the positivity and domain assumptions on \(\mathcal G_N\).

The repeated statement is not a distinct mathematical result and should not be presented as an independent proposition with a second proof.

## 2. Proposed publication-facing disposition

Preferred option: retain the subcritical exclusion once in PROP-0001, after the conditional threshold statement is clarified under MCR-06, and remove the duplicate PROP-0008 proposition from the manuscript numbering.

If numbering stability is required, alternatively relabel the second occurrence as an explicit corollary of PROP-0001 with a direct cross-reference and no repeated independent proof.

## 3. Registry and audit requirements

- Do not delete the claim record AS-ALPHA-A-PROP-0008 from Constant Llpoy.
- Mark it `DUPLICATE_OF: AS-ALPHA-A-PROP-0001` or the registry's equivalent relation.
- Preserve its source locator, proof-obligation history, and layer routing for audit traceability.
- Update manuscript numbering and all downstream cross-references only in the separate working manuscript.
- Ensure MCR-06's domain and positivity qualifications apply to the retained statement.

## 4. Disposition

**EDITORIAL DUPLICATE RETIREMENT PROPOSED.** No new theorem or stronger mathematical conclusion is introduced.

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
