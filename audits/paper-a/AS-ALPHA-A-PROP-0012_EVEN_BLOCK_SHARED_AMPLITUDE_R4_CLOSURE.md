# PROP-0012 — Even-Block Entries from Explicit Ground-State Amplitude Orders

**Scope:** Fixed finite N, weak coupling r=J/h, independent real edge perturbations near the uniform reference. This report corrects the earlier parity-of-order argument and derives even-block entry orders from environment amplitudes and the explicit second-order two-flip coefficient.

## 1. Ground-state amplitude bookkeeping

Use the x-basis and the normalized analytic ground state, choosing the vacuum coefficient real positive:
- c_empty=1+O_N(r^2);
- two-flip c_{ij}=a_{ij}+b_{ij}^{(2)}+O_N(r^3), with a_{ij}=J_{ij}/(4h);
- four-flip amplitudes c_{ijkl}=O_N(r^2).

The second-order coefficient for the target two-flip state {1,2} receives paths through intermediate states {1,k} and {2,k}, for k distinct from 1,2. Since each pair-flip matrix element is -J and both intermediate and target gaps are 4h,
[
b_{12}^{(2)}=sum_{k
e1,2}rac{J_{1k}J_{2k}}{8h^2}.
]
This coefficient is generally nonzero. Thus the valid amplitude order is c_{12}=a_{12}+O_N(r^2); do not assert an O(r^3) correction.

All order estimates are jointly analytic in the independent edge variables u on a smaller fixed neighborhood, and first edge derivatives have the same order.

## 2. Environment sums for the even block

For the even block indexed by (++,--), write coefficients c_E for x-basis states whose flipped-spin set is E. The reduced entries are environment sums:

[
L=sum_{Esubseteq{3,ldots,N}}|c_E|^2,
quad
X=sum_{Esubseteq{3,ldots,N}}c_E^*c_{Ecup{1,2}},
quad
S=sum_{Esubseteq{3,ldots,N}}|c_{Ecup{1,2}}|^2,
]
where only even-cardinality sets E occur by global parity.

- L: vacuum contributes |c_empty|²=1+O_N(r²); nonempty E first contributes |c_E|²=O_N(r²). Therefore L=1+O_N(r²).
- X: vacuum environment contributes c_empty*c_12=a_12+O_N(r²) (because c_12 includes b^(2) and vacuum normalization); nonempty even E first contributes a two-flip amplitude times a four-flip amplitude, O_N(r³). Therefore X=c_12+O_N(r³)=a_12+O_N(r²).
- S: vacuum environment contributes |c_12|²; nonempty even E first contributes four-flip population O_N(r⁴). Therefore S=|c_12|²+O_N(r⁴)=a_12²+O_N(r³).

The last equality is only the conservative expansion in terms of first-order a12; the key cancellation uses the shared exact c12, not the truncation a12.

## 3. Exact cancellation through shared amplitude

Since X=c_12+O_N(r³), and c_12=O_N(r), we have |X|²=|c_12|²+O_N(r⁴). With L=1+O_N(r²), |X|²/L=|c_12|²+O_N(r⁴). Hence
[
D=S-|X|^2/L=O_N(r^4).
]

The large eigenvalue λL is bounded below near 1 and satisfies L/λL=1+O_N(r²). The small eigenvalue satisfies the exact identity
[
lambda_s=det M/lambda_L=(L/lambda_L)D=O_N(r^4).
]
All estimates are jointly analytic in r and edge perturbations; first edge derivatives are O_N(r⁴) by analytic coefficient bounds on a smaller neighborhood. The eigenvalue is nonnegative because the reduced density block is positive semidefinite.

## 4. Entropy derivative

The reviewed nonnegative analytic entropy lemma then yields the even-block small-branch edge-entropy derivative
[
O_N(r^4(1+|ln r|)).
]

## 5. Verification boundary

The derivation is analytic and coefficient-based, but not machine-checked. It relies on finite-N perturbation theory and the stated amplitude order bookkeeping; no Lean formalization/build was run. It only closes this even-block contribution. It does not prove the odd positive branch's full derivative expansion, reconcile source-language conflict, or establish a global sign.

**Verdict:** Even-block small eigenbranch improved to O_N(r⁴), with entropy derivative O_N(r⁴ log r), via shared-amplitude cancellation—not via the invalid parity-only argument.
