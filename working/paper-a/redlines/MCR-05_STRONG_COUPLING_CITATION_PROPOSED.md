# MCR-05 — Proposed Redline: Strong-Coupling Citation and Proof Placement

- **Document ID:** CL-PA-RL-MCR-05
- **Status:** PROPOSED CITATION REPAIR; PROOF ARTIFACT EXISTS IN CONSTANT LLPLOY; MANUSCRIPT APPENDIX/CORRESPONDENCE NOT YET ACCEPTED
- **Affected claim:** AS-ALPHA-A-PROP-0009
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §4.4.2, lines 105–120
- **Source blob:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Correction register item:** MCR-05

## 1. Citation defect

The frozen §4.4.2 says:

> By applying Schrieffer–Wolff degenerate perturbation theory to the parity-even sector (see Lemma 5.1), we obtain the rigorous asymptotic expansion for the dimensionless mutual information: ...

The located source `docs/lemma_5_1_proof.md` is titled “Lemma 5.1: Asymptotic Positivity of \(B-C\)”. It is about independent edge-response derivatives, not the uniform-path function \(\mathcal G_N(x)\) or its derivative. It therefore does not support the cited sentence. The fact that both arguments use strong-coupling perturbation theory does not make the citation valid.

## 2. Correct proof source now available in Constant Llpoy

A separate fixed-finite-\(N\) derivation of the uniform function and its derivative is recorded in:

- `audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md`
- `audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md`
- `audits/paper-a/FINITE_N_STRONG_COUPLING_EIGENVALUE_DIAGNOSTIC.md`
- integrated working derivation: `working/paper-a/CANONICAL_STRONG_COUPLING_DERIVATION.md`

The uniform-path result is
\[
\mathcal G_N(x)
=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right),
\]
and the derivative is established separately:
\[
\mathcal G_N'(x)
=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right),
\]
for each fixed finite \(N\ge4\).

The derivation treats the parity-even spectral branch, one-site entropy, two-site reduced-state blocks, and the small eigenvalue. The small-eigenvalue coefficient is \(1/648\) at \(N=4\), and \(1/[8(N-2)(N-1)^4]\) for \(N\ge5\); the latter is derived symbolically for \(N\ge9\) and checked by exact-rational recurrence for \(N=5,6,7,8\). The N=4 correction must not be lost when this proof is moved into the manuscript.

This derivation concerns the one-dimensional uniform path and \(d/dx\). It does **not** prove the independent edge-response asymptotic \(B-C\).

## 3. Proposed replacement wording for §4.4.2

**Delete** the parenthetical citation “(see Lemma 5.1)”.

**Replacement target (only after the proof is incorporated as a manuscript appendix or an equivalently citable, versioned supplement):**

> For each fixed finite \(N\ge4\), a perturbative analysis of the parity-even ground-state branch and the one- and two-site reduced density matrices gives the uniform strong-coupling expansion
> \[
> \mathcal G_N(x)
> =\ln2-\frac{1}{(N-1)^2x^2}
> +O_N\!\left(\frac{\ln x}{x^4}\right),
> \qquad x\to\infty.
> \]
> The differentiated expansion is established separately from the analytic reduced-state eigenvalue branches:
> \[
> \mathcal G_N'(x)
> =\frac{2}{(N-1)^2x^3}
> +O_N\!\left(\frac{\ln x}{x^5}\right).
> \]
> The constants and the perturbative neighborhood may depend on \(N\); no uniform-in-\(N\) estimate is asserted.

The final manuscript version must cite the actual new appendix/proposition number after that text exists. Do not invent a current lemma number or leave a dangling “Appendix A” reference.

## 4. Required proof placement and correspondence

Before accepting this replacement:

1. Move the complete uniform-path derivation (including the small-eigenvalue coefficient cases and the derivative argument) into a manuscript appendix or a formally versioned supplementary proof that is actually cited by the paper.
2. Retain the explicit distinction between the uniform derivative \(d\mathcal G_N/dx\) and independent edge derivatives \(B,C\).
3. Include the N=4 coefficient correction and the N≥5 coefficient formula with their actual derivation scopes.
4. Audit every use of “rigorous”, “analytic control”, and “Schrieffer–Wolff” against the proof's explicit hypotheses and remainder estimates.
5. Create exact traceability from the new appendix equations to the Constant Llpoy proof artifact and source hashes.
6. Complete independent code review of the exact-rational diagnostic and independent review of the analytic proof.
7. Run the relevant formalization and verification obligations; current status is Lean NOT RUN and manuscript correspondence NOT RUN.

## 5. What must not be conflated

- The located Lemma 5.1 is about \(B-C\), not \(\mathcal G_N\).
- The new \(\mathcal G_N'\) result is along the uniform path, not an ambient edge derivative.
- The strong-coupling \(B-C\) derivative remainder is a separate proof problem.
- Fixed finite \(N\) estimates do not establish uniformity in \(N\).
- A repository audit document is not automatically a manuscript citation or an external peer-reviewed source.

## 6. Disposition

**CITATION MISMATCH CONFIRMED; REPLACEMENT PROOF ROUTE AVAILABLE; MANUSCRIPT APPENDIX AND FORMAL/CORRESPONDENCE CHECKS OPEN.**

This proposed redline does not modify the frozen source snapshot or upstream `Absolute_Sym`. MCR-05 must not be marked fully resolved merely because the incorrect citation has been identified or a separate repository derivation exists.
