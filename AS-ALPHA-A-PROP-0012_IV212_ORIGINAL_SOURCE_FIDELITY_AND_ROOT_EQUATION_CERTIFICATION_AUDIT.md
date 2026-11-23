# IV-212 — Original Source Fidelity and Root Equation Certification Audit

**Target:** AS-ALPHA-A-PROP-0012 (weak-coupling lower-branch opposite-sign response claim)  
**Audit mode:** Repository evidence reconciliation; no guessed source, no theorem promotion.  
**Verdict:** SOURCE ACCESS / MATHEMATICAL OBJECT MISMATCH BLOCKER — OPEN.

## 1. Claim identity check

The canonical claim record `claims/A/AS-ALPHA-A-PROP-0012.md` identifies PROP-0012 as a claim about the weak-coupling lower branch response, specifically the assertion that it has distinct scaling and opposite-sign response characteristics relative to the physical stable branch. It records SOURCE_CONFLICT and NOT_VERIFIED.

This is not itself a claim about a generic implicit root equation or a global Lipschitz map. The IV-198–211 audit series concerns a reconstructed scalar implicit-root map and its derivative/domain bounds. The records retrieved in this pass do not establish that this scalar equation is a defining object of the PROP-0012 weak-coupling B-C claim.

## 2. Repository source status

The claim record pins the alleged source to:
- repository: `mytheeramet3dev-x/Absolute_Sym`
- branch: `paper-a-interval-audit-2026-11-14`
- commit: `8deb7de4a49cb2060720246b7101820ee7e08c91`
- file: `Arxiv/paper_01_section_04_revised.md`
- cited line: 134.

The separate source reconciliation record `AS-ALPHA-A-PROP-0012_SOURCE_RECONCILIATION_ACCESS_AND_DEFINITION_AUDIT.md` states that frozen-branch/commit manuscript fetches returned 404/NOT FOUND, the upstream repository is private, and accessible main-branch material is not a substitute for the frozen source. It expressly leaves source-to-proof reconciliation blocked.

## 3. What can and cannot be certified here

**Confirmed from the retrieved Constant Llpoy records:**
- PROP-0012's claim identity and weak-coupling source-conflict status.
- The frozen source identifiers and cited line are recorded in the claim record.
- Frozen-source access was previously reported blocked.
- IV-198–211 contain conditional analysis of a reconstructed root equation; IV-211 closes branch/segment coverage only at that reconstructed-formula level.

**Not established:**
- That IV-198's equation `R(d,t,p)` is the exact mathematical object defined in the frozen PROP-0012 source.
- That the root interval, parameter box, branch labels, or map `Q` correspond to the source claim.
- That the reconstructed root map's derivative ceilings imply the weak-coupling B-C claim.
- That the source-conflict claim itself is resolved, or that PROP-0012 is proved.

## 4. Certification decision

| Obligation | Status |
|---|---|
| Canonical PROP-0012 claim identification | PASS (record inspection) |
| Frozen source identifiers recovered from claim record | PASS (metadata only) |
| Frozen manuscript text accessible in this audit pass | BLOCKED |
| Equation/root-map correspondence to PROP-0012 source | OPEN / NOT CERTIFIED |
| IV-211 conditional branch coverage for reconstructed equation | Retained, conditional |
| IV-211 promotion to PROP-0012 source-level evidence | NOT PERMITTED |
| PROP-0012 source conflict / theorem closure | OPEN |

## 5. Correction to interpretation of IV-211

IV-211 remains a valid conditional result about the reconstructed rational equation, assuming its displayed equation and box. It must not be described as having closed a source-level root branch or segment obligation for PROP-0012 until source correspondence is established.

Accordingly, IV-212 **retracts any implied source-level promotion** of IV-211 to PROP-0012. It does not retract the conditional algebraic result itself.

## 6. Required next step

Do not continue downstream derivative tightening as if source correspondence were established. The next research action is to recover the exact frozen Paper A Section 4/5 source (or a user-supplied stable snapshot) and independently map:
1. the precise PROP-0012 statement and branch;
2. every root/implicit variable and defining equation;
3. parameterization and interval/domain;
4. response quantity and sign/scaling conventions;
5. exact hypotheses and remainder requirements.

Only after that map is verified should IV-198–211 be judged relevant to PROP-0012. Until then, theorem-level status remains **OPEN / NOT_VERIFIED**.
