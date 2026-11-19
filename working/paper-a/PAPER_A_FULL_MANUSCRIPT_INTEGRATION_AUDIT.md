# Paper A — Full Manuscript Integration Audit

**Document ID:** CL-PA-FMIA-001  
**Status:** AUDIT FINDINGS RECORDED / PROPOSED REMEDIATION / NOT VERIFIED  
**Audit target:** Paper A at frozen upstream source commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Repository:** `mytheeramet3dev-x/Absolute_Sym`  
**Branch:** `paper-a-interval-audit-2026-11-14`  
**Audit home:** Constant Llpoy, branch `paper-a-mcr01-pf-redline`

## 1. Executive result

The frozen source manifest identifies six revised section files as the authoritative Paper A manuscript sources. The integrated Markdown file is explicitly designated as a cross-check, and the claim ledger is secondary. However, the frozen LaTeX generator reads `Arxiv/paper_01_manuscript.md` and writes `Arxiv/paper_01.tex`. This creates a release-critical source-authority conflict: the files declared authoritative are not the direct input to the TeX build.

The integrated Markdown is not a byte-equivalent assembly of the six revised sections. Most sections differ only by appended claim-status tags or formatting, but Section 4 has substantive differences. In particular, the integrated Markdown contains a more cautious asymptotic statement and removes the superseded weak-coupling/opposite-sign language, while the authoritative revised Section 4 reintroduces stronger formulas and the disputed Lemma 5.1 / Lemma 5.2 references.

**Conclusion:** Do not submit or regenerate the release TeX from the current integrated Markdown until the source-authority conflict and Section 4 divergence are resolved. This is an editorial/build-integrity blocker, independent of whether individual mathematical claims are true.

## 2. Frozen source identity

The governing Constant Llpoy manifest is `MANUSCRIPT_SOURCE_MANIFEST.md`, version 0.2.3, blob SHA `73f50a3bec3fea48eb778c65b52f6ac3894c8412`.

Frozen upstream commit:
`8deb7de4a49cb2060720246b7101820ee7e08c91`

| Item | Path | Blob SHA |
|---|---|---|
| Section 1 | `Arxiv/paper_01_section_01_revised.md` | `1f7857bcd44e1605900bf71193e9b593a62397bd` |
| Section 2 | `Arxiv/paper_01_section_02_revised.md` | `541382fa7ab4b9e254c8e7e5158f202c1a975e0d` |
| Section 3 | `Arxiv/paper_01_section_03_revised.md` | `9ac164ac67cc121af212c4fb7268b809d9234bd6` |
| Section 4 | `Arxiv/paper_01_section_04_revised.md` | `a7570431eac62dd4555194df283edb5a9c87a28d` |
| Section 5 | `Arxiv/paper_01_section_05_revised.md` | `671c97fa68fa48c929760bf9956d197b358c4904` |
| Section 6 | `Arxiv/paper_01_section_06_revised.md` | `5e734065c2ddd42ee602dada89e7455d2ad9e7a0` |
| Integrated Markdown (manifest says cross-check only) | `Arxiv/paper_01_manuscript.md` | `ec2361c1ae17b955e845ec1726636795cc3b74ff` |
| Generated LaTeX | `Arxiv/paper_01.tex` | `7b3e5b6552e2cc9a14a27edc5acb53a97cbaac82` |
| Technical proof audit | `Arxiv/paper_01_technical_audit.md` | `6cf0f8ba18a6cebb80c440fa83c53042e50c1819` |
| Secondary claims ledger | `Arxiv/claims_ledger.md` | `7a9eadbf363b75fe29088ad3c5443e145779316c` |
| Markdown-to-TeX generator | `code/md_to_arxiv_tex.py` | `08f8af1b0e91630ce9b9fbcec7d44d622940d9f1` |

The six section files were fetched from the frozen commit and their returned blob SHAs match the manifest. The upstream repository was read only; no upstream file was modified.

## 3. Source authority and build-path conflict — BLOCKER

The source manifest says:
- the six revised section files are authoritative;
- `paper_01_manuscript.md` is an integrated cross-check only;
- the claims ledger is secondary and must not be imported wholesale as manuscript theorem claims.

But the frozen generator `code/md_to_arxiv_tex.py` explicitly calls:
- `build("paper_01", "paper_01_manuscript.md")`;
- reads the Markdown source;
- writes `Arxiv/paper_01.tex`.

Therefore the artifact produced by the recorded build pipeline is generated from the file the manifest calls cross-check-only, not from the six authoritative files.

This is not merely a formatting discrepancy. Until the authority policy is reconciled, it is impossible to state unambiguously that the TeX being compiled is the authoritative revised manuscript.

**Required decision (not made in this audit):**
1. Either promote the integrated Markdown to canonical authority after reconciling it against all six sections and updating the manifest; or
2. change the build pipeline so it assembles the six authoritative sections into the TeX source, with deterministic ordering and a reproducible assembly manifest.

Do not silently choose one policy in Constant Llpoy or alter the upstream repository without authorization.

## 4. Integrated Markdown versus six revised sections

A structural comparison was performed by extracting each section block from the integrated Markdown, removing its claim-status appendix, and comparing it with the corresponding revised section file.

| Section | Revised source lines | Integrated lines | Observed difference |
|---|---:|---:|---|
| 1 | 106 | 110 | Integrated file appends four claim-status lines |
| 2 | 204 | 207 | Integrated file appends three claim-status lines |
| 3 | 248 | 251 | Integrated file appends three claim-status lines |
| 4 | 132 | 146 | Substantive content and wording differ; not a formatting-only delta |
| 5 | 131 | 135 | Mostly math-format normalization plus appended claim-status lines; requires exact semantic check |
| 6 | 62 | 65 | Integrated file appends three claim-status lines |

### Section 4 divergence — BLOCKER

The authoritative revised Section 4 contains:
- an explicit coefficient expansion
  `G_N(x) = ln 2 - 1/((N-1)^2 x^2) + O(ln x/x^4)`;
- a derivative expansion
  `G_N'(x) = 2/((N-1)^2 x^3) + O(ln x/x^5)`;
- a claim that analytic control of the entropy remainder guarantees the derivative order;
- a citation to Lemma 5.1 for the strong-coupling mutual-information expansion;
- a weak-coupling reference to Lemma 5.2 and “opposite-sign response characteristics”.

The integrated Markdown instead:
- downgrades the function/derivative result to a finite-(N), conditional `O(x^{-2})` derivative estimate;
- explicitly states that the endpoint limit alone does not imply derivative decay;
- cites Kato for the perturbation-theory framework;
- removes the “opposite-sign response characteristics” assertion.

The integrated Markdown is closer to the cautious dispositions in the existing audit history, but it is not the authoritative section file under the current manifest. The stronger claims in the revised section cannot be accepted solely because they appear in the file designated authoritative.

### Citation reconciliation

The source manifest itself records that the located `docs/lemma_5_1_proof.md` concerns the `B-C` strong-coupling positivity problem, not the `G_N(x)` asymptotic cited by revised Section 4.4.2. Therefore the Lemma 5.1 citation in revised Section 4.4.2 is mismatched.

The manifest also records the original Lemma 5.2 negative-sign derivation as superseded by `docs/lemma_5_2_audit.md`. Revised Section 4's reference to Lemma 5.2 and opposite-sign response language must be reconciled with that audit. The corrected candidate weak-coupling calculation has a positive leading coefficient for (B-C) at fixed finite (N\ge4), but its model-specific differentiated remainder and independent review remain open. It does not establish a global sign.

## 5. Mathematical and editorial findings across sections

### P0 — Must resolve before a release build

**FMIA-01 — Canonical-source/build mismatch.** The manifest says six section files are authoritative, but the generator consumes the integrated Markdown cross-check. A release TeX built today is not demonstrably generated from the manifest-authoritative source.

**FMIA-02 — Section 4 authority conflict.** The revised Section 4 and integrated Markdown differ materially on strong-coupling derivative control and weak-coupling sign language. The stronger authoritative-file statements include a mismatched Lemma 5.1 citation and superseded Lemma 5.2 framing.

### P1 — Mathematical corrections / proof obligations

**FMIA-03 — Perron–Frobenius operator sign.** Revised Section 2 says shifting (H) by a sufficiently large multiple of the identity makes the matrix nonnegative. Adding (cI) changes only diagonal entries; it does not change the negative single-spin-flip off-diagonal entries (-h). The correct nonnegative operator for this sign convention is (K=cI-H), with (c) chosen to make the diagonal nonnegative. Its single-spin-flip entries are (+h>0), and its positive-entry graph is the connected Boolean hypercube. This supports finite-(N), (h>0) ground-state simplicity. The precise proof must be reconciled with the Lean declaration and the supporting PF proof source.

**FMIA-04 — (C^2) versus cubic Taylor/branch remainder.** Revised Section 3 assumes only (C^2) regularity but writes a cubic (O(|\delta x|^3)) remainder and a branch remainder (O(g-g_c)). In general, (C^2) gives a Peano remainder (o(|\delta x|^2)), not a cubic big-O remainder. For this (F=g\mathcal G_N(x)-hx), a safe (C^2) expansion keeps (o(|\delta x|^2)) and the mixed (O(|\delta g\,\delta x|)) term. The local fold existence can be stated under suitable (C^2) hypotheses, but the displayed quantitative (O(g-g_c)) branch remainder needs stronger regularity (for example, locally Lipschitz second derivative / suitable (C^{2,1}) or (C^3) assumptions) and a proof. The earlier technical audit's blanket statement that the displayed cubic remainder is correct under (C^2) is itself incorrect and must be corrected.

**FMIA-05 — Threshold attainment and global root count.** The infimum (α_N=\inf_{x>0}x/\mathcal G_N(x)) need not be attained. Subcritical exclusion follows from the infimum definition on a domain where (mathcal G_N>0). Interior tangency requires interior attainment and differentiability. Exactly two global roots, or a root for every supercritical parameter, needs continuity, endpoint, and global-shape assumptions. Keep these as separate claims.

**FMIA-06 — Entropy regularity at rank-changing points.** Smoothness of the ground-state projector for (h>0) does not by itself prove differentiability/analyticity of von Neumann entropy at reduced states whose rank changes or which have zero eigenvalues. The (x=0) product-state endpoint has zero mutual information, but endpoint differentiability is a separate obligation. Positivity (mathcal G_N(x)>0) for all (x>0), used when dividing by (mathcal G_N), also needs proof or an explicit restricted domain.

**FMIA-07 — Strong-coupling function versus derivative asymptotics.** A function-level estimate does not automatically justify differentiating the remainder. The derivative estimate requires its own controlled perturbation/entropy argument. Constants should be denoted (O_N) if they may depend on fixed (N). Do not infer uniform-in-(N) behavior. The coefficient formulas and the (N=4) exception recorded in the internal Constant Llpoy audit must be reconciled with the source manuscript before publication.

**FMIA-08 — Weak-coupling sign conflict.** The original negative-sign (B-C) derivation omitted an order-(r^2) coherence contribution and is superseded in the audit history. The corrected fixed-finite-(N) candidate has a positive leading coefficient near (J/h=0^+), conditional on a model-specific differentiated remainder. It is provisional and does not establish global (B-C>0). Remove or redefine “opposite-sign response characteristics” in revised Section 4.

**FMIA-09 — Edge-response decomposition domain and hypotheses.** The three-sector edge decomposition and the three nonzero sector interpretation must state (N\ge4). The Schur-lemma scalar action requires differentiability of the response map and (S_N)-equivariance. The exact identity (chi_1-chi_2=(N-2)(B-C)) is conditional on the response Jacobian existing and on the stated sector conventions.

**FMIA-10 — Uniform response derivative.** Keep the uniform-path derivative distinct from an independent-edge partial. With (chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C) and (F_J=gchi_0-1), (F_J<0) implies (chi_0<1/g), not (chi_0<0). A negative response requires the stronger (F_J<-1) when (g>0).

**FMIA-11 — Scaling and branch selection.** Positive rescaling requires (h>0). Root-set invariance along fixed (eta=g/h) does not alone prove differentiability of a selected branch. Branch derivatives require a simple-root/IFT condition; folds need separate treatment. Distinguish the projector from phase-dependent eigenvectors.

**FMIA-12 — Stale technical audit statements.** The technical audit says revised Section 4 is absent and that Section 1 describes Sections 1–7. At the frozen commit, a Section 4 revised file exists with the manifest-listed SHA, and revised Section 1 organizes Sections 1–6. Those two technical-audit statements are stale. Separately, the technical audit's (C^2)/cubic-remainder assessment is mathematically too permissive, as described in FMIA-04. The audit document must be versioned and corrected rather than treated as an unquestionable authority.

### P2 — Editorial consistency

**FMIA-13 — Claim-status tags.** The integrated Markdown appends status tags absent from the six revised section files. Their classifications need a claim-by-claim audit and must not silently alter the authoritative source policy.

**FMIA-14 — Notation lock.** Maintain the distinction:
- (F(J;g,h)=gI_{12}(J,h)-J), with (F_J=\partial_JF);
- (f(x;\eta)=\eta\mathcal G_N(x)-x), with (f_x=\partial_xf);
- (T(x)=\eta\mathcal G_N(x)), with (T'=\eta\mathcal G_N'(x));
- (F_J=T'-1) at corresponding points.
Avoid using (F') ambiguously.

**FMIA-15 — Conclusion scope.** The conclusion's (B-C>0) statement remains a strong numerical conjecture for the stated reliable tested cases, not a theorem. (N=50) near-degenerate data remain excluded. The exact sector identity does not prove an ordering or emergent geometry.

## 6. Required remediation order

1. **Resolve source authority**: decide whether the six sections or integrated Markdown is the actual publication source; update the manifest/build design only after an explicit source-policy decision.
2. **Reconcile Section 4**: use the corrected Lemma 5.2 audit; remove the incorrect Lemma 5.1 citation; decide whether the stronger (G_N) and derivative expansions are proved and manuscript-ready. If not, use conditional/provisional wording and keep the proof obligation visible.
3. **Correct Section 3 regularity**: retain the local fold theorem only with a mathematically valid remainder and quantified hypotheses. Do not silently strengthen (C^2) to (C^3) unless the model proof establishes it.
4. **Correct Section 2 PF shift**: use (K=cI-H) and reconcile with the Lean proof.
5. **Complete Section 5 hypotheses/domain**: (N\ge4), differentiability, equivariance, and uniform-path derivative conventions.
6. **Reconcile Sections 1 and 6**: make abstract/introduction/conclusion claims exactly match the final theorem status.
7. **Regenerate TeX from the chosen canonical source** and rerun structural, citation, reference, and compilation checks.
8. **Only then** resume the 14-layer mathematical/formal verification gates.

## 7. Verification status

- Frozen source identity: verified against the Constant Llpoy manifest.
- Six revised section blob SHAs: verified.
- Integrated Markdown and TeX blob SHAs: verified.
- Generator input: verified from `code/md_to_arxiv_tex.py`; it reads `paper_01_manuscript.md`.
- Full mathematical proof review: not complete.
- Lean build / axiom audit: not run in this integration-audit step.
- CI: not run in this integration-audit step.
- Independent external review: not run.
- Upstream files changed: none.
- Paper A overall status: **NOT VERIFIED**.
