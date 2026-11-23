# IV-216 — Eigenbranch Analyticity, Entropy Logarithms, and Derivative Closure Audit

**Target:** Weak-coupling fixed-finite-`N` derivation for `B-C) in AS-ALPHA-A-PROP-0012.
**Status:** CONDITIONAL PASS for the scalar entropy-derivative mechanism; OPEN for its full model-specific application and the overall sign theorem.
**Scope:** Audit the current working proof, the reusable nonnegative-eigenvalue entropy lemma, and the Schur-remainder source lemma. This record does not claim live upstream Paper A recovery.

## 1. Source inspection

Inspected from Constant-Llpoy main:
- `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md`
- `audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md`
- `source_snapshots/paper-a/docs/entropy_schur_remainder_lemma.md`

## 2. Positive isolated branch: closure is valid under explicit hypotheses

For an eigenvalue branch with `lambda(r,0)>0`, the identity
[
\partial_u[-\lambda\ln\lambda]=-(1+\ln\lambda)\partial_u\lambda
]
is valid. If `lambda(r,0)=c r^k(1+O(r))`, `c>0`, then `|ln lambda|=O(1+|ln r|)`. A derivative bound `partial_u lambda=O(r^m)` therefore yields `O(r^m(1+|ln r|))`.

The joint analytic, uniform-in-u order hypothesis in the scalar lemma is stronger than a pointwise eigenvalue upper bound and is needed to infer the derivative order. The lemma must not be used from `lambda=O(r^m)` alone.

## 3. Zero eigenvalue at the symmetric interior point

If a branch is nonnegative for all real u in a two-sided neighborhood and has value zero at u=0 (for fixed r>0), the eigenvalue function has a minimum there. If differentiable, its first directional derivative is zero. Entropy derivative at that point is zero, provided the branch opening has enough regularity to justify the derivative of `-lambda ln lambda`; the scalar lemma's analytic hypotheses suffice. No `ln 0` is evaluated.

For a matrix eigenvalue with degeneracy, analytic labeling in several perturbation variables is not automatic. The proof should use either (a) an explicitly justified analytic eigenvalue branch, (b) the nonnegative scalar branch assumptions of the lemma, or (c) a direct PSD matrix/block argument for the directional entropy. Do not infer multi-parameter eigenbranch analyticity merely from analyticity of the matrix or ground-state projector.

## 4. Schur remainder application

The working proof claims fixed-N bounds `D=O_N(r^4)`, `partial_u D=O_N(r^4)` after shared-amplitude cancellation, conditional on the pair-flip amplitude-order and environment-sum hypotheses. The entropy-Schur source lemma is also conditional: it requires the Schur complement and its directional derivative bounds, plus a bounded positive large block and fixed dimension.

The small eigenvalue's order and derivative are not established by the source lemma itself. The application remains conditional until the model-specific block estimates are independently justified.

## 5. Leading term and asymptotic dominance

The leading coefficient previously audited is
[
(B-C)_{lead}=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}>0,\quad N\ge4.
]
If a remainder of `O_N(J^2 h^{-3}|ln(J/h)|)` is rigorously established, then for each fixed finite N it is asymptotically smaller than the positive leading term as `r=J/h\to0^+`. This does **not** provide an explicit threshold, uniform-in-N control, or positivity at finite coupling. The current IV-215 `O_N(r^4|ln r|)` even-block entropy remainder is stronger but remains conditional on its model-specific hypotheses.

## 6. Verdict

- **PASS:** chain-rule/logarithmic estimate for a positive branch under the stated vanishing-order and derivative assumptions.
- **PASS (conditional regularity):** zero nonnegative branch has zero first directional derivative at an interior reference point; no `ln 0` shortcut.
- **OPEN:** analytic eigenbranch labeling for the specific reduced-state blocks under multi-edge perturbations; direct PSD block verification is preferred.
- **OPEN:** full TFIM proof of Schur complement order and derivative bounds for every needed branch.
- **OPEN:** rigorous closure of all entropy remainders and hence fixed-N asymptotic positivity theorem.
- **NOT CLAIMED:** global `B-C>0`, explicit coupling radius, uniform-in-N result, or Lean formalization.

## 7. Next proof task

Proceed with IV-217: replace potentially fragile eigenvalue-label arguments by a direct `2\times2` PSD-block eigenvalue/entropy directional analysis, with explicit branch splitting and derivative bounds; then test the exact assumptions against the TFIM environment-sum expressions. Any failing hypothesis should be recorded as a failure, not silently weakened.

