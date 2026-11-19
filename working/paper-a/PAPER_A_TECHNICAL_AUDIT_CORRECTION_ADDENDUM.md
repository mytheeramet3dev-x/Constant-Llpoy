# Paper A Technical Audit — Correction Addendum

**Document ID:** CL-PA-TA-ADD-001  
**Status:** PROPOSED AUDIT CORRECTION / NOT AN UPSTREAM EDIT  
**Applies to:** Frozen Paper A source commit `8deb7de4a49cb2060720246b7101820ee7e08c91`  
**Supersedes:** No source file; this addendum records corrections needed before relying on `Arxiv/paper_01_technical_audit.md`.

## 1. Stale version statements

The frozen technical audit says revised Section 4 is absent and was audited from a pasted draft. That is stale for the frozen commit now pinned by the Constant Llpoy manifest: `Arxiv/paper_01_section_04_revised.md` exists and has blob SHA `a7570431eac62dd4555194df283edb5a9c87a28d`.

The technical audit also says Section 1 describes Sections 1–7. The revised Section 1 at the frozen commit explicitly organizes Sections 1–6. This audit finding is stale.

These stale statements should be corrected in a versioned audit update, not silently treated as current.

## 2. Correction to the (C^2) Taylor-remainder assessment

The technical audit says the displayed expansion
[
F=F_c+F_g\delta g+F_x\delta x+\tfrac12F_{xx}\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3)
]
is correct under (C^2) regularity. This is too strong in general.

For the model-specific function
[
F(x,g,h)=g\mathcal G_N(x)-hx,
]
at a critical point, a (C^2) assumption on (mathcal G_N) gives a quadratic Taylor expansion with a Peano remainder (o(|\delta x|^2)). Since (F) is linear in (g), the local expansion can be written with a mixed (O(|\delta g\,\delta x|)) contribution, but a cubic (O(|\delta x|^3)) bound requires additional regularity such as locally Lipschitz second derivative (or a suitable (C^3) hypothesis).

Consequently, the branch expansion with remainder (O(g-g_c)) is not justified by the stated (C^2) assumption alone. Under (C^2), a standard local fold conclusion may still be proved, but the quantitative remainder must be weakened (for example, to a suitable little-o statement) unless stronger regularity is established. Any strengthened regularity must be proved for the model; it must not be inserted as an unverified assumption merely to preserve the original formula.

## 3. Perron–Frobenius sign correction

The technical audit's prose should specify the operator used. With the Hamiltonian convention whose single-spin-flip off-diagonal entries are (-h), adding (cI) to (H) does not change those off-diagonal signs and does not make (H+cI) entrywise nonnegative. The relevant operator is
[
K=cI-H,
]
with (c) chosen so that all diagonal entries of (K) are nonnegative. Then the single-spin-flip entries are (+h>0), and the positive-entry graph is the connected Boolean hypercube. The resulting finite-dimensional Perron–Frobenius argument gives ground-state simplicity for finite (N) and (h>0). It does not establish a thermodynamic-limit gap.

## 4. Section 4 claims must be re-audited against the actual revised file

The revised Section 4 at the frozen commit includes:
- an explicit coefficient for (mathcal G_N(x)) beyond its endpoint limit;
- a separate explicit derivative asymptotic;
- a claim that entropy-remainder control justifies the derivative order;
- a Lemma 5.1 citation for the (mathcal G_N) expansion;
- a Lemma 5.2 / opposite-sign response statement.

The frozen Constant Llpoy manifest records that the located Lemma 5.1 concerns the (B-C) strong-coupling positivity proof, not the (mathcal G_N(x)) expansion. It also records the original Lemma 5.2 negative-sign derivation as superseded by its audit. Therefore the revised Section 4's stronger claims and citations require a fresh proof/citation reconciliation. The more cautious integrated Markdown wording is not automatically authoritative under the current manifest, because that manifest calls the integrated Markdown a cross-check only.

## 5. Other audit qualifications to preserve

1. The threshold infimum does not by itself imply interior attainment or a global root count.
2. Entropy differentiability at rank-changing reduced states is a separate obligation from analyticity of the ground-state projector.
3. The three nonzero edge-response sectors require (N\ge4); differentiability and (S_N)-equivariance are needed for the response representation argument.
4. (F_J<0) is an upper bound condition for the uniform response, not a proof that the response is negative.
5. (B-C>0) remains conjectural globally; numerical evidence and the corrected fixed-(N) weak-coupling candidate must be distinguished.
6. The claim ledger is a mixed-status index and is not a list of proved manuscript theorems.

## 6. Use policy

Until this addendum is independently reviewed and the upstream technical audit is versioned:
- treat the original technical audit as historical evidence, not a current complete authority;
- use the frozen source manifest and full manuscript integration audit together;
- retain all unresolved items as open obligations;
- do not change upstream Paper A files without explicit authorization.

**Overall status remains: PAPER A NOT VERIFIED.**
