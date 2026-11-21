# PROP-0012 — Even-Block Shared-Amplitude Schur Cancellation Review

**Scope:** Fixed finite N >= 4, weak coupling r=J/h -> 0+, uniform reference with real independent edge perturbations. Review the even block by environment-resolved exact amplitude sums, not by truncated c_12.

## 1. Exact environment-resolved entries

Write the normalized analytic ground state in the x-basis as |Psi>=sum_E c_E |E>, where E is the flipped-spin set. Pair-flip Hamiltonian preserves even parity, so odd-cardinality amplitudes vanish. For the two-site reduced even block on (++ , --), with environment E subset {3,...,N} and E even:

L = sum_E |c_E|^2,
X = sum_E c_E conjugate(c_{E union {1,2}}),
S = sum_E |c_{E union {1,2}}|^2.

These are exact identities (with conjugation convention depending on block ordering), not truncated perturbative expressions.

## 2. Fixed-N analytic order bounds

The finite-dimensional ground-state projector is analytic near the uncoupled point because the unperturbed ground state is simple and gapped. A normalized ground vector can be selected analytic locally (fix its phase convention). For fixed N, perturbation order and pair-flip selection imply:
- c_empty = 1 + O_N(r^2);
- c_{ij}=O_N(r), with first edge derivatives O_N(r);
- c_E=O_N(r^{|E|/2}) for even E near the origin (the bound follows from the minimum number of pair-flip operations; constants depend on N);
- c_{E union {1,2}}=O_N(r^{(|E|+2)/2}).

For edge variables in a compact neighborhood, these analytic bounds also hold for first derivatives in u, with the corresponding orders, by the finite-dimensional analytic expansion.

## 3. Cancellation using the shared amplitude

The empty-environment terms are shared:
L=|c_empty|^2+O_N(r^2),
X=c_empty conjugate(c_12)+O_N(r^3),
S=|c_12|^2+O_N(r^4).

The O(r^3) in X comes from nonempty even environments: the first such E has size two, so c_E=O(r) and c_{E union 12}=O(r^2), product O(r^3). The O(r^4) in S comes from nonempty even E, whose first contribution has squared amplitude O(r^4).

Because c_empty is bounded away from zero, and L=|c_empty|^2+O_N(r^2), the ratio |c_empty|^2/L=1+O_N(r^2). Thus
|X|^2/L=|c_12|^2+O_N(r^4):
the cross term between c_empty*c_12=O(r) and the nonempty-environment correction O(r^3) is O(r^4), and the normalization factor differs from 1 only by O(r^2), multiplying |c_12|^2=O(r^2).

Consequently, the Schur complement D=S-|X|^2/L=O_N(r^4), with first edge derivatives also O_N(r^4), under the same analytic fixed-N bounds. The cancellation does not require c_12 to have a vanishing second-order coefficient; that coefficient is present in both shared empty-environment contributions.

## 4. Small eigenbranch and entropy derivative

The large even-block eigenvalue remains bounded away from zero (L=1+O_N(r^2), X=O_N(r)); the small eigenvalue satisfies
lambda_s = (L/lambda_L)D = O_N(r^4).
The joint analytic expansion and derivative bounds give partial_u lambda_s=O_N(r^4). Since lambda_s is nonnegative and either vanishes at the reference point or has a positive analytic leading coefficient, the reusable entropy lemma bounds its entropy directional derivative by O_N(r^4(1+|ln r|).

## 5. Audit limitations / explicit assumptions

This environment-sum proof is a candidate analytic closure and is stronger than the conservative O_N(r^3) working-file bound. Its entry identities are exact. The analytic order estimates rely on a rigorous fixed-N pair-flip perturbation-order statement for all amplitudes and first edge derivatives, which should be written out as a lemma (or formally verified); this review does not run Lean and does not certify the entire PROP-0012 source reconciliation.

**Verdict:** EVEN-BLOCK SCHUR CANCELLATION — ANALYTIC-PARTIAL, STRONGER O_N(r^4) CANDIDATE; exact identities and order bookkeeping reviewed, perturbation-order lemma formal closure still outstanding. Full PROP-0012 remains OPEN until the amplitude lemma is closed and integrated with all entropy branches.
