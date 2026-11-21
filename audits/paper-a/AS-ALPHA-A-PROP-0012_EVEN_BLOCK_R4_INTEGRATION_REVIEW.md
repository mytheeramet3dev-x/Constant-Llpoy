# PROP-0012 — Even-Block O(r^4) Integration Review

**Scope:** Fixed finite N >= 4; local weak coupling r -> 0+; real edge variables in a compact neighborhood; first edge-direction derivatives. Paper-level analytic review only; no Lean formalization/build.

## Objective

Integrate the pair-flip amplitude-order lemma with the environment-resolved even-block entries and check whether the Schur complement and small eigenbranch retain O_N(r^4), including first edge derivatives.

## 1. Entry-level estimates

For even environment flip sets E subset {3,...,N}, exact entries are
L=sum_E |c_E|^2, X=sum_E c_E conjugate(c_{E union {1,2}}), S=sum_E |c_{E union {1,2}}|^2.

The empty-environment terms and pair-flip orders give:
- L=|c_empty|^2+O_N(r^2), with first edge derivatives of the remainder O_N(r^2);
- X=c_empty conjugate(c_12)+R_X, R_X=O_N(r^3), and first edge derivatives R_X'=O_N(r^3);
- S=|c_12|^2+R_S, R_S=O_N(r^4), and first edge derivatives R_S'=O_N(r^4).
Also c_empty=1+O_N(r^2), c_12 and its first edge derivatives are O_N(r).

The estimates follow termwise: for a nonempty even E, |E|>=2. In X, the product has orders r^{|E|/2} and r^{(|E|+2)/2}, hence at least r^3. In S, the squared second amplitude is at least r^4. Differentiating either factor preserves its order by the pair-flip derivative lemma.

## 2. Schur cancellation and derivative

Since L is bounded away from zero and L=|c_empty|^2+O_N(r^2), write X=c_empty conjugate(c_12)+R_X. Expanding the quotient:
|X|^2/L = |c_12|^2 (|c_empty|^2/L) + cross/error terms.
Here |c_empty|^2/L=1+O_N(r^2), multiplying |c_12|^2=O_N(r^2) contributes O_N(r^4). The cross term is O_N(r)·O_N(r^3)=O_N(r^4), and |R_X|^2=O_N(r^6). These estimates also hold after one edge derivative using the product/quotient rule and the derivative estimates above. Therefore D=S-|X|^2/L and its first edge derivatives are O_N(r^4).

## 3. Small eigenvalue and derivative

The large eigenvalue λ_L of the Hermitian 2x2 block is bounded away from zero and is O(1); the determinant identity gives λ_s=det(M)/λ_L=(L/λ_L)D. Since L/λ_L=O(1), its first edge derivatives are bounded locally (indeed analytic), and D,D' are O_N(r^4), the small branch and its first edge derivatives are O_N(r^4).

This argument uses the determinant identity exactly; it does not replace λ_s by D without the multiplicative factor.

## 4. Entropy directional derivative

For λ_s>0, the binary-entropy derivative is H'(λ_s)λ_s', where H'(x)=ln((1-x)/x). With λ_s=O_N(r^4) and λ_s'=O_N(r^4), this is O_N(r^4(1+|ln r|)) whenever the branch's positive scale is controlled by the analytic expansion. If λ_s is identically zero at the reference edge point, nonnegativity and an interior minimum in the real edge variables imply its first directional derivative is zero; its entropy directional derivative is treated by the zero-branch case, not by evaluating ln(0).

The positive-branch estimate is understood with the standard analytic/nonnegative branch expansion: a nonzero analytic branch has a finite leading power in r with positive coefficient locally at the reference, so |ln λ_s|=O_N(1+|ln r|). This branch-scale condition must be explicitly checked for the exact source branch during reconciliation.

## Verdict and limitations

**EVEN-BLOCK SCHUR O(r^4) — ANALYTIC INTEGRATION CLOSED, CONDITIONAL ON SOURCE/BRANCH RECONCILIATION.** The pair-flip order lemma supplies the amplitude and derivative orders; environment summation gives the entry estimates; the determinant/Schur identity closes the small eigenbranch order. Entropy derivative follows under the branch-scale/zero-branch conditions stated above.

This is not a full PROP-0012 pass. Exact Hamiltonian and convention reconciliation, branch-scale verification against the source, all entropy branches/remainder integration, and Lean formalization/build remain outstanding. Constants are fixed-N only; no uniform-in-N assertion.
