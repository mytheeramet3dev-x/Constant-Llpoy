# PROP-0012 — Odd Positive Branch Differentiated Remainder Audit

**Scope:** Fixed finite N >= 4, r=J/h -> 0+, uniform edge reference with independent edge variables u, first derivatives only. This audit examines the positive odd-block branch and entropy contrast. It does not certify all reduced-block remainders.

## 1. Branch construction

The odd block has analytic entries in (r,u) from the analytic ground-state spectral projector, for fixed finite dimension and a nondegenerate unperturbed ground state. Its leading matrix is r^2 Q(u)+O_N(r^3). At u=0, Q(0) has a simple positive eigenvalue (N-2)/8 and the other eigenvalue zero. By factoring r^2 and applying simple-eigenvalue analytic perturbation locally to the positive branch, q/r^2 is analytic near (0,0), hence

q(r,u)=r^2 Q_+(u)+O_N(r^3),

with differentiated expansion in edge directions. This does not assert analytic splitting for the zero branch.

At the uniform point, independently checked leading coefficients are:
q=(N-2)r^2/8+O_N(r^3);
partial_u13 q=r^2/8+O_N(r^3);
partial_u34 q=O_N(r^3).

## 2. Entropy derivative bookkeeping

For one-site binary entropy, exactly
partial_u H(p)=ln((1-p)/p) partial_u p.
Given p=(N-1)r^2/16+O_N(r^3), partial_u13 p_1=r^2/8+O_N(r^3), and all relevant p_2/u13, p_1,p_2/u34 terms O_N(r^3), the one-site contribution to the edge contrast is
-(r^2/8) ln p + O_N(r^3(1+|ln r|)).

For the positive two-site branch, entropy derivative is -(1+ln q) partial_u q. Taking the edge contrast and inserting the leading derivatives above gives
-(r^2/8)(1+ln q)+O_N(r^3(1+|ln r|)).
The constant -1 terms cancel with the corresponding binary-entropy derivative bookkeeping, leaving the leading contrast
(r^2/8) ln(q/p)+O_N(r^3(1+|ln r|).

The zero odd branch contributes zero first directional entropy derivative at the uniform point, because it is nonnegative and has an interior minimum of zero (for each fixed r>0).

## 3. Physical-coupling conversion

The variables u_e are defined by J_e=J(1+u_e). Therefore partial/partial J_e = J^{-1} partial/partial u_e at the reference point. Dividing the dimensionless contrast by J yields the corrected physical formula:
B-C=J/(8h^2) ln(2(N-2)/(N-1))+O_N(J^2/h^3(1+|ln(J/h)|)).

The logarithm is strictly positive for every fixed N>=4. The local asymptotic sign follows only after the model-specific differentiated remainder bounds, including the even-block small eigenvalue, are established.

## 4. Scope and unresolved items

- The positive odd branch differentiated remainder is analytically justified by simple-branch construction and finite-dimensional analytic entry expansions.
- The one-site expansions and their first edge derivatives follow from the first-order pair-flip state and analytic projector expansion, at the stated fixed-N orders.
- The even-block small eigenbranch remains conservative O_N(r^3) in the checked working proof. An earlier conversational claim of O_N(r^4) is not yet backed by an independently committed source derivation and is NOT accepted by this audit.
- No full closure of the complete entropy remainder chain is claimed here; it still depends on the even-block branch estimate and source-to-working-proof reconciliation.
- No global B-C sign, arbitrary-coupling sign, or Lean formalization/build is claimed.

**Verdict:** ODD POSITIVE BRANCH + LEADING CONTRAST: ANALYTIC-PASS WITH FIXED-N SCOPE. FULL PROP-0012: OPEN / ANALYTIC-PARTIAL.
