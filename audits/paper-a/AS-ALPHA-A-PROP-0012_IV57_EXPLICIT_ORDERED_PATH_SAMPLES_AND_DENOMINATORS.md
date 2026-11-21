# IV-57 — Explicit Ordered Pair-Edge Path Samples and Denominators

**Status:** SAMPLE PATHS DERIVED / COMPLETE ENUMERATION OPEN / c_vv OPEN  
**Scope:** Explicitly calculate representative four-operation pair-flip paths under H0=-h sum sigma_x and V=-sum J_ij sigma_i^z sigma_j^z. This is not a complete topology enumeration.

## 1. Set-update rule and energy denominators

Represent an x-basis excitation by a flipped vertex set S. Acting with edge e=(i,j) updates S to S △ {i,j}. If |S|=2q, then E(S)-E0=4qh. The resolvent denominator E0-E(S)=-4qh for a non-vacuum intermediate set.

For a four-operation sequence e1,e2,e3,e4, define S_k=e1△...△e_k (interpreting each edge as its two-vertex set). The raw sequential-path denominator product is Π_{k=1}^3 (E0-E(S_k)), but paths passing through vacuum require special/reducible treatment and cannot be included by this simple product without the chosen perturbation formalism.

## 2. Representative path A: four-edge chain with endpoint target

Take distinct vertices a,b,c,d and sequence (ab,bc,cd,ab).
- S1={a,b}; gap 4h.
- S2={a,c}; gap 4h.
- S3={a,d}; gap 4h.
- S4={b,d}; target two flips, gap 4h (final target is not a denominator).

No intermediate is vacuum. The raw sequential term with three resolvent denominators is
(-J_ab)(-J_bc)(-J_cd)(-J_ab)/(-4h)^3
= - J_ab^2 J_bc J_cd/(64 h^3),
where the displayed sign is for this specific resolvent convention and raw path term only. It is not by itself the normalized fourth-order wavefunction amplitude; other paths to the same target and perturbative normalization/reducible terms must be added.

## 3. Representative path B: two disjoint edges repeated

For distinct vertices a,b,c,d sequence (ab,cd,ab,cd):
S1={a,b} (gap 4h), S2=∅ (vacuum return), S3={a,b} (gap 4h), S4=∅.
This path passes through the reference vacuum at the second step; it is reducible and the naive product of denominators is undefined. It demonstrates why vacuum-return paths require explicit normalization/reducible-term rules rather than blind path multiplication.

## 4. Representative path C: shared-vertex pair edges

Sequence (ab,bc,ab,bc) gives:
S1={a,b} (4h), S2={a,c} (4h), S3={a,b} (4h), S4=∅.
The intermediate states are non-vacuum; however the final return to vacuum is not a fourth-order amplitude to a non-vacuum target. Its contribution to energy/normalization sectors must be handled by the selected perturbation expansion, not automatically assigned to c_vv.

## 5. What this audit does and does not establish

- XOR path-set update and H0 gaps: derived.
- One non-vacuum-intermediate four-edge path sample: explicit raw term derived.
- Vacuum-return/reducible example: identified.
- Exhaustive four-edge topology enumeration, path aggregation by target, and all denominator corrections: OPEN.
- Complete normalized amplitudes, environment matching, c_vv, B-C, entropy, Lean: OPEN.

Paper A PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
