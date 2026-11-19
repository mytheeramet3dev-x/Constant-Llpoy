# Paper A — Section 4 Equation-by-Equation Audit

- **Document ID:** CL-PA-S4-AUD-001
- **Version:** 0.1.0
- **Source:** frozen `Arxiv/paper_01_section_04_revised.md`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source blob:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Status:** INTERNAL SECTION AUDIT / PROPOSED REDLINES / NOT EXTERNAL REVIEW / NOT LEAN-VERIFIED
- **Repository boundary:** This audit and proposed text belong only in Constant Llpoy. It does not authorize changes to Absolute Symmetry.

## 1. Executive disposition

Section 4 is not uniformly defective. Its central scaling identities in §§4.1–4.3 are algebraically sound under the stated definitions and hypotheses. The near-critical limits in §4.4.1 are locally supportable once the saddle-node regularity statement in Section 3 is corrected. The strong-coupling function and uniform-path derivative expansions in §4.4.2 now have a separate fixed-finite-`N` derivation in Constant Llpoy; the manuscript's Lemma 5.1 citation is nevertheless wrong. Section 4.4.3 contains an unresolved/unsupported response-sign narrative and imprecise branch wording.

**Current Section 4 disposition: PARTIALLY SUPPORTED; MANUSCRIPT CORRECTIONS REQUIRED.** This is not a Section 4 PASS and does not upgrade Paper A to VERIFIED.

## 2. Detailed audit

### S4-01 — Dimensionless scaling parameter `eta=g/h`

**Source:** §4.1.

Given `h>0` and the symmetric Hamiltonian `H(J,h)=h Htilde(J/h,1)`, the dimensionless coordinate `x=J/h` and feedback parameter `eta=g/h` are correct. If the threshold is defined by an attained interior minimizer and `g_c(h)=alpha_N h`, then along `g=gamma alpha_N h`, `eta=gamma alpha_N` is constant as `h` varies.

**Qualification:** The existence and exact threshold scaling are inherited assumptions/results from Section 2, not proved by §4.1 itself. The phrase “dynamic scaling” should not suggest time-dependent dynamics; this section establishes static homogeneity of the fixed-point equation.

**Disposition:** ALGEBRAICALLY SUPPORTED / CONDITIONAL ON THRESHOLD HYPOTHESES.

### S4-02 — Root independence from the absolute scale

**Source:** §4.2.

The equation on the ray is `x=gamma alpha_N G_N(x)`, containing no `h`. Therefore its root set is independent of `h`. For any root selected by a rule that depends only on this dimensionless equation, its value is constant along the ray.

**Precision correction:** The notation `partial x_*/partial h=0` can suggest an implicit-function theorem or differentiable branch selection. Neither is needed to establish root-set invariance, but differentiability of a selected branch would require additional hypotheses. Prefer the direct root-set statement and reserve the derivative notation for a branch already shown differentiable.

**Disposition:** EXACT ROOT-SET INVARIANCE; BRANCH-DERIVATIVE FORMULATION SHOULD BE QUALIFIED.

### S4-03 — Picard multiplier and dimensional derivative

**Source:** §4.3.

For `T(x)=eta G_N(x)`, `f(x;eta)=eta G_N(x)-x`, and `F(J,g,h)=gG_N(J/h)-J`, direct differentiation gives

```text
T'(x*) = eta G_N'(x*)
F_J = (g/h) G_N'(J/h) - 1
T'(x*) = F_J + 1
```

Thus `|T'|<1` is equivalent to `-2<F_J<0`. At a tangent point, `T'=1` and `F_J=0`.

**Qualification:** This is the scalar Picard iteration only. It does not establish stability of a vector-valued edge-coupling iteration, nor global convergence.

**Disposition:** ALGEBRAICALLY PASS, WITH SCALAR-SCOPE LABEL.

### S4-04 — Near-critical limits

**Source:** §4.4.1.

If a nondegenerate local upper saddle-node branch exists and `x_*(gamma) -> x_c` as `gamma -> 1+`, continuity of `G_N'` gives `T'(x_*) -> 1` and `F_J -> 0`. These limits follow from the tangent equations.

**Dependency:** The frozen Section 3 currently asserts a cubic Taylor remainder and an `O(g-g_c)` branch remainder under only `C^2`. That quantitative remainder is not justified by `C^2` alone. Under suitable `C^2` fold hypotheses, the leading square-root behavior and convergence to `x_c` may be retained with a weaker remainder; to claim the displayed `O(g-g_c)` correction, impose and prove stronger regularity (for example an appropriate locally Lipschitz second derivative / `C^{2,1}` condition, or `C^3`) and verify the expansion. Section 4 must not silently inherit the stronger conclusion.

**Disposition:** LIMITS CONDITIONALLY SUPPORTED; EXACT ERROR ORDER DEPENDS ON SECTION 3 REDLINE.

### S4-05 — Large-`gamma` branch continuation

**Source:** first paragraph of §4.4.2 and §4.4.3.

The manuscript explicitly assumes global continuation without turning points or branch exchanges. This is a substantive global hypothesis, not a consequence of the local saddle-node theorem. With this assumption and positivity/continuity of `G_N` on the relevant positive domain, the strong-coupling route `x_*(gamma)->infinity` is plausible and can be justified from the root equation; it must remain explicitly conditional unless the global continuation is proved.

**Disposition:** CONDITIONAL ONLY; NO GLOBAL BRANCH THEOREM ESTABLISHED.

### S4-06 — Strong-coupling function expansion

**Source:** §4.4.2.

The target statement is for each fixed finite `N>=4`, `x=J/h -> infinity`:

```text
G_N(x) = ln 2 - 1/((N-1)^2 x^2)
         + O_N(ln(x)/x^4).
```

A separate Constant Llpoy derivation now supports this formula from the finite-dimensional perturbation problem. It uses the even-parity sector, analytic reduced-state eigenvalue branches, and the small two-site eigenvalue

```text
lambda_s(epsilon) = c_N epsilon^4 + O_N(epsilon^6),
epsilon = h/J = 1/x,
c_4 = 1/648,
c_N = 1/[8(N-2)(N-1)^4] for N>=5.
```

The exceptional `N=4` coefficient was corrected and checked against exact-rational and high-precision finite-dimensional diagnostics. The derivation is fixed-`N`; it does not establish uniformity in `N`.

**Evidence:** `audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md`, blob `1c65403df3fb23531b88a8fd84cf845fd8082003`.

**Disposition:** ANALYTICALLY DERIVED FOR FIXED FINITE `N>=4`; NOT LEAN-VERIFIED; NOT EXTERNALLY REVIEWED; MANUSCRIPT CORRESPONDENCE STILL REQUIRED.

### S4-07 — Lemma 5.1 citation is wrong

**Source:** sentence immediately preceding the expansion in §4.4.2.

The frozen supporting file `docs/lemma_5_1_proof.md` is titled “Asymptotic Positivity of B-C”; it is not the proof of the uniform `G_N(x)` expansion. The Section 4 citation therefore does not identify the derivation that now exists in Constant Llpoy.

**Required action:** Replace the citation with a correctly numbered lemma/supplementary derivation that actually proves the `G_N) expansion, or cite the correct source after the manuscript's source-authority policy is reconciled. Do not relabel the unrelated `B-C` lemma.

**Disposition:** CHANGE REQUIRED; SOURCE-CITATION DEFECT CONFIRMED.

### S4-08 — Derivative expansion is now separately supported

**Source:** §4.4.2.

The target is

```text
G_N'(x) = 2/((N-1)^2 x^3)
          + O_N(ln(x)/x^5).
```

It would be invalid to infer this by formally differentiating the preceding pointwise big-O estimate. However, the new Constant Llpoy derivation does not do that: it separately differentiates the analytic large eigenvalue branches and the small eigenvalue branch in `epsilon`, obtains a two-sided scale bound for the positive small eigenvalue, derives the entropy derivative, and then uses `d/dx=-epsilon^2 d/depsilon`.

**Scope boundary:** This is the derivative along the one-dimensional uniform path `J_ij=J`. It is not an independent edge derivative such as `B-C`.

**Disposition:** ANALYTICALLY DERIVED FOR FIXED FINITE `N>=4`; LEAN AND EXTERNAL REVIEW PENDING.

### S4-09 — Endpoint limits and large-`gamma` multiplier

The limits `G_N(x)->ln 2` and `G_N'(x)->0` follow from the two fixed-`N` asymptotic formulas. The further limits `T'(x_*(gamma))->0` and `F_J->-1` follow if the selected branch is known to satisfy `x_*(gamma)->infinity`.

**Disposition:** FIRST TWO LIMITS ANALYTICALLY SUPPORTED; BRANCH-COMPOSED LIMITS CONDITIONAL ON S4-05.

### S4-10 — Cat-state wording

The unperturbed Ising Hamiltonian at `h/J=0` has a two-dimensional ferromagnetic ground space. For positive transverse field, the finite-`N) ground state is unique and lies in the even-parity sector; as `h/J->0+`, the selected state approaches the parity-even cat combination. The manuscript should distinguish the exactly degenerate limiting Hamiltonian from the unique ground state at positive field. “The transverse field selects the unique, parity-even cat state” is shorthand that should be made explicit.

**Disposition:** QUALIFY THE LIMITING STATEMENT.

### S4-11 — Weak-coupling / “opposite-sign” response statement

**Source:** §4.4.3.

The sentence says the lower branch has “distinct scaling and opposite-sign response characteristics” and cites Lemma 5.2. The original frozen Lemma 5.2 negative-sign calculation omitted the order-`r^2` coherence in the `(|+-\rangle,|-+\rangle)` block and is superseded. The corrected fixed-finite-`N` weak-coupling derivation gives

```text
B-C = J/(8h^2) * ln(2(N-2)/(N-1))
      + O_N((J^2/h^3) [1+|ln(J/h)|]),
```

which has a positive leading coefficient for each fixed `N>=4` as `J/h->0+`. The internal analytic review of that corrected derivation is marked PASS, but it is not Lean-verified or externally reviewed. It does not establish a global sign or prove that the response is “opposite” to the stable branch.

**Required action:** Remove the phrase “opposite-sign response characteristics” unless the manuscript defines a different response quantity and proves the asserted sign for that quantity. If the intended quantity is `B-C`, the local corrected result points positive, not negative. Do not infer that the small-`x` response belongs to a globally continued lower branch without proving that branch connection.

**Disposition:** CHANGE REQUIRED / SOURCE CONFLICT RESOLVED LOCALLY, GLOBAL BRANCH INTERPRETATION OPEN.

### S4-12 — “Lower interval” versus “lower local branch”

The wording “the lower interval `0<x<x_c` forms the locally unstable branch” conflates a domain interval with a solution branch. The local saddle-node theorem supplies a lower local root branch with `x<x_c` near criticality; it does not say every point in the interval is a solution. Local repelling behavior follows near the fold when `T'>1`; global instability across the whole interval is not established.

**Required action:** Replace “the lower interval ... forms the locally unstable branch” with “the lower local solution branch lies below `x_c` near the saddle-node and is locally repelling for the scalar Picard map under the stated local hypotheses.”

**Disposition:** WORDING CORRECTION REQUIRED.

## 3. Proposed Section 4 redline text

The following is a proposed replacement for the affected passages only. It is not an upstream edit and is not a publication-ready full Section 4.

### Proposed replacement for §4.2 final paragraph

“Along the ray `g=gamma alpha_N h`, the dimensionless root equation is `x=gamma alpha_N G_N(x)`, which contains no dependence on the absolute scale `h`. Hence its root set is invariant as `h) varies along this ray. Any root selected by a rule depending only on this dimensionless equation has the same dimensionless value. This statement does not imply uniqueness, differentiability of a selected branch, or global continuation.”

### Proposed replacement for §4.4.1 qualification

“For the upper local branch supplied by the nondegenerate saddle-node result, `x_*(gamma)->x_c` as `gamma->1+`. By continuity of `G_N'` and the tangent equations, `T'(x_*)->1` and `F_J|_{J_*}->0`. The precise remainder in the square-root branch expansion is subject to the regularity assumptions stated in Section 3.”

### Proposed replacement for the first paragraph of §4.4.2

“Assume that the selected upper branch has a global continuation to arbitrarily large `gamma`, with no turning points or branch exchanges, and that `G_N) remains positive on that branch. Since `G_N(x)` has the fixed-`N) positive limit `ln 2` as `x->infinity`, the root equation `x=gamma alpha_N G_N(x)` then gives `x_*(gamma)->infinity`. For fixed finite `N>=4`, the limiting Ising Hamiltonian at `h/J=0` has a two-dimensional ferromagnetic ground space. For positive transverse field the finite-system ground state is unique and parity-even; in the limit `h/J->0+` it approaches the even cat combination.”

### Proposed replacement for the Lemma 5.1 citation and asymptotic paragraph

“An independent fixed-finite-`N) perturbative derivation of the uniform mutual-information asymptotics is given in [insert correctly numbered manuscript lemma or supplementary reference after source reconciliation]. It yields
`G_N(x)=ln 2-1/((N-1)^2 x^2)+O_N(ln(x)/x^4)` for each fixed finite `N>=4`. The derivative estimate is established separately from the analytic reduced-state eigenvalue branches, not by differentiating the function-level big-O term:
`G_N'(x)=2/((N-1)^2 x^3)+O_N(ln(x)/x^5)`.
These estimates are not asserted uniformly in `N`. Consequently `G_N(x)->ln 2` and `G_N'(x)->0` for each fixed finite `N>=4`.”

### Proposed replacement for §4.4.3

“The inequality `x_*(gamma)>=x_c` holds for the upper local branch sufficiently near `gamma=1`. Extending it to every `gamma>=1` requires a global continuation result excluding reversing turning points or branch exchanges. Near the saddle-node, the lower local solution branch lies below `x_c` and is locally repelling for the scalar Picard map under the local hypotheses of Section 3. The weak-coupling expansion of the edge-response contrast `B-C` is a separate endpoint result: the corrected fixed-finite-`N) calculation has a positive leading coefficient as `J/h->0+`. It does not establish a global sign, nor does it by itself prove that this endpoint is connected to the lower local branch. The phrase ‘opposite-sign response characteristics’ is therefore withdrawn unless a different response quantity is defined and separately proved.”

## 4. Required action list

1. Reconcile the manuscript source-authority/build-input conflict before deciding where the replacement lemma belongs.
2. Add a correctly numbered proof/reference for the uniform `G_N) expansion; do not cite Lemma 5.1.
3. Correct the §4.4.3 “opposite-sign” claim and branch terminology.
4. Align §4.4.1's branch remainder with the corrected Section 3 regularity theorem.
5. State fixed finite `N>=4` explicitly for both function and derivative asymptotics, and retain the `O_N` dependence.
6. Keep the uniform derivative `G_N'` separate from edge-response derivatives `B,C`.
7. Obtain independent external mathematical review and Lean correspondence before any VERIFIED promotion.
8. Do not modify upstream `Absolute_Sym` without explicit authorization.

## 5. Verification status

- Exact algebra in §§4.1–4.3: **SUPPORTED**, subject to stated definitions and scalar scope.
- Near-critical limits: **CONDITIONAL**, with Section 3 regularity correction required.
- Fixed-`N) strong-coupling `G_N) expansion: **ANALYTICALLY DERIVED** in Constant Llapoy.
- Fixed-`N) uniform-path derivative expansion: **ANALYTICALLY DERIVED** separately.
- Lemma 5.1 citation: **INCORRECT / CHANGE REQUIRED**.
- Weak-coupling “opposite-sign” assertion: **UNSUPPORTED / CHANGE REQUIRED**.
- Global branch continuation: **OPEN**.
- Lean verification of Section 4 claims: **NOT RUN / NOT ESTABLISHED**.
- Independent external review: **NOT RUN**.
- Overall Section 4: **PARTIALLY SUPPORTED — NOT VERIFIED**.

---
**End of Section 4 audit.**
