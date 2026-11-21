# PROP-0012 — Fresh Differentiated Entropy Remainder Closure Review

**Frozen Paper A source:** `8deb7de4a49cb2060720246b7101820ee7e08c91`.  
**Review target:** `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md` plus the reusable nonnegative-eigenvalue entropy lemma.  
**Scope:** fixed finite (N\ge4), (r=J/h\to0^+), local uniform-edge perturbations. Analytic review only; no Lean build.

## Result

**REMAINDER ROUTE: ANALYTICALLY CONSISTENT, BUT NOT CLOSED AS A FULL INDEPENDENT PROOF.**

The proposed (O_N(r^3(1+|\ln r|))) entropy-derivative remainder is compatible with the displayed expansions, provided the stated joint analytic expansions and derivative bounds for all reduced-state eigenvalue branches are established. The working file gives several of these estimates but does not provide the complete block-to-entropy derivative calculation in one self-contained proof. Thus this pass does not upgrade the claim to VERIFIED.

## Chain-rule remainder check

For a positive small eigenvalue (s(r,u)=r^2S(u)+O_N(r^3)), with (S(0)>0) and joint analyticity, its edge derivative has expansion (partial_us=r^2S_u(0)+O_N(r^3)), and
[
\partial_u[-s\ln s]=-(\partial_us)(1+\ln s).
]
Since (s\asymp_N r^2), (ln s=2\ln r+O_N(1)). The (O_N(r^3)) derivative error therefore contributes (O_N(r^3(1+|\ln r|))).

For a nonnegative analytic branch (\lambda=O_N(r^3)), the reusable lemma controls its first directional entropy derivative by (O_N(r^3(1+|\ln r|))), under the lemma's two-sided parameter-neighborhood and joint-analyticity assumptions. The exactly zero branch at the symmetric point has zero first directional entropy derivative.

For a large eigenvalue (1-O_N(r^2)), the entropy derivative is multiplied by (\ln\lambda=O_N(r^2)); with derivative (O_N(r^2)), its contribution is (O_N(r^4)), not an (O_N(r^2)) leading term.

## Leading-log cancellation

The displayed shared-edge leading terms are (p_1'=r^2/8+O_N(r^3)), (q'=r^2/8+O_N(r^3)); disjoint-edge terms are (O_N(r^3)). Their logarithmic contributions to the contrast reduce to
[
\frac{r^2}{8}\ln\frac{q}{p}
=\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}+O_N(r^3),
]
where (p\sim (N-1)r^2/16), (q\sim (N-2)r^2/8). Scaling back (r=J/h) yields the stated leading coefficient.

## Remaining obligations

1. Put the eigenvalue branch expansions, first-edge-derivative bounds, and block entropy calculation into one fully explicit derivation, including the rank-changing branches and normalization.
2. Independently rederive the block expansions from the Hamiltonian (not merely review the working artifact).
3. Establish the analytic neighborhood and constants for each fixed N.
4. Formalize the corresponding finite-dimensional spectral/entropy statements in Lean or provide a separately checked proof certificate.
5. Reconcile the original Lemma 5.2 sign/source language.

**Disposition:** The logarithmic remainder mechanism is sound under the stated expansions. Full analytic proof closure is still **OPEN**; the weak-coupling endpoint is not globally verified, and this review makes no claim about all coupling strengths.
