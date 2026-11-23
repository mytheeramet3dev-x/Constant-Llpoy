# IV-215 — Pair-Flip Support and Amplitude-Order Lemma Audit

**Date:** 2026-11-23  
**Scope:** Fixed finite N, TFIM pair-flip perturbation around the x-polarized product ground state; checks the support-order lemma invoked in IV-214.  
**Disposition:** Combinatorial support bound PASS; analytic coefficient control CONDITIONAL; Schur remainder closure remains CONDITIONAL.

## 1. Support-order statement

Let S be a target x-basis flip set. In the perturbative expansion around H0=-h sum_i sigma_i^x, each interaction V_e=-J_e sigma_i^z sigma_j^z flips exactly two x-basis bits. A term with n interaction insertions can therefore reach S only if |S|<=2n. Consequently, coefficients of order r^n vanish whenever 2n<|S|. For even S, the first possible nonzero order is n>=|S|/2.

This proves the formal perturbative support statement:
- c_E=O(r^{|E|/2}) for even environment E;
- c_{E union {1,2}}=O(r^{(|E|+2)/2});
provided these amplitudes are defined in the normalized ground-state expansion with the analytic normalization factor treated consistently.

## 2. Edge-direction derivative

Differentiating with respect to an independent edge variable u_e in J_e=J(1+u_e) differentiates a coefficient of perturbative degree n but does not lower its power of r: each interaction insertion remains proportional to r, and the derivative replaces one factor (1+u_e) by 1. Thus the same order bounds hold for first edge derivatives, in the formal series and within a jointly analytic neighborhood with fixed N.

## 3. Environment sums

For fixed finite N, the number of environment flip sets and perturbative paths is finite at each order. Summing the support bounds preserves the indicated orders:
- R_L=O_N(r^2),
- R_X=O_N(r^3),
- R_S=O_N(r^4),
and the same first edge derivative orders.

The R_X estimate follows because for nonempty even E, the minimum orders of c_E and c_{E∪{1,2}} add to |E|+1>=3. R_S similarly has order |E|+2>=4. R_L has minimum nonempty even |E|=2, giving order r^2.

## 4. Schur cancellation recheck

Use exact shared amplitudes c_empty and c_12:
L=|c_empty|^2+R_L, X=c_empty conjugate(c_12)+R_X, S=|c_12|^2+R_S.
With c_empty=1+O_N(r^2), c_12=O_N(r), R_L=O_N(r^2), R_X=O_N(r^3), R_S=O_N(r^4), the expansion of |X|^2/L cancels |c_12|^2, and the cross remainder is O_N(r^4). First edge derivatives obey the same order bookkeeping, yielding D=S-|X|^2/L=O_N(r^4) and ∂_{u_e}D=O_N(r^4).

**Algebraic order conclusion:** PASS conditional on the coefficient/amplitude expansions and uniform analytic derivative bounds established in the finite-dimensional perturbation setting.

## 5. What is not proved by this support argument

The bit-flip counting alone does not establish:
- convergence radius or numerical constants for the multivariate perturbation series;
- a uniform-in-N radius or bounds;
- the exact ground-state amplitude expansion beyond the formal support;
- all entropy eigenvalue branches' analytic labeling near degeneracies.

These must be kept separate from the combinatorial statement. The repository's candidate proof uses finite-dimensional analytic perturbation and branch-specific arguments to address them; a fully independent derivation of coefficient bounds and branch handling remains a proof obligation.

## 6. Verdict

- Pair-flip combinatorial support: PASS.
- First edge derivatives preserve perturbative order: PASS at coefficient/formal level.
- Finite environment sums preserve order: PASS for fixed finite N.
- Shared-amplitude Schur cancellation: PASS algebraically under the stated expansion/derivative bounds.
- Analytic remainder and entropy-derivative closure: CONDITIONAL; requires rigorous joint analytic estimates and branch hypotheses.
- Corrected weak-coupling leading sign: positive.
- Fixed-N eventual positivity theorem: still CONDITIONAL; no Lean formalization.
- PROP-0012: OPEN.

This audit does not modify upstream Absolute_Sym.
