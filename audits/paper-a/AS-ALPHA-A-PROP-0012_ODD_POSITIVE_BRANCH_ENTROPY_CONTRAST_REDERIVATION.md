# PROP-0012 — Odd Positive Branch and Leading Entropy Contrast Re-derivation

**Scope:** Fixed finite N≥4, weak coupling r=J/h, uniform reference with independent edge perturbations u. This derives the leading response contrast from the one-site small eigenvalues and the odd positive eigenbranch; it does not prove global sign.

## 1. Branch separation and analyticity

The odd block has the leading matrix
[
M_o=r^2Q(mathbf u)+O_N(r^3),
]
jointly analytic in (r,u). At the uniform point,
[
Q(0)=rac{N-2}{16}egin{pmatrix}1&1\1&1end{pmatrix}.
]
Its positive eigenvalue is (N−2)/8, separated from zero for fixed N≥4. Thus the positive branch q=r²Q_+(mathbf u)+O_N(r³) is analytic near u=0, and its edge derivatives have the same remainder order.

## 2. Edge derivatives

At the uniform point, set a=r/4. For the shared edge 13, the leading odd-block matrix derivative is
[
partial_{u_{13}}M_o=r^2/16egin{pmatrix}0&1\1&2end{pmatrix}
]
up to the labeling convention of the block, whose symmetric eigenvector gives
[
partial_{u_{13}}q=r^2/8+O_N(r^3).
]
Edge 34 is absent from the leading odd-block Gram matrix, so
[
partial_{u_{34}}q=O_N(r^3).
]

One-site small eigenvalues:
[
p_1=p_2=(N-1)r^2/16+O_N(r^3),
]
and
[
partial_{u_{13}}p_1=r^2/8+O_N(r^3),quad
partial_{u_{13}}p_2=O_N(r^3),quad
partial_{u_{34}}p_1,partial_{u_{34}}p_2=O_N(r^3).
]

## 3. Entropy derivative bookkeeping

For a small eigenvalue z, (rac{d}{du}[-zln z]=-(ln z+1)z_u). Since p,q are both order r², (ln p=2ln r+O_N(1)), (ln q=2ln r+O_N(1)). The first-order edge derivatives of mutual information (I_{12}=H(p_1)+H(p_2)-S(ho_{12})) therefore yield, in dimensionless edge variables,
[
partial_{u_{13}}I_{12}-partial_{u_{34}}I_{12}
=rac{r^2}{8}lnrac{q}{p}+O_N(r^3(1+|ln r|)).
]
The shared-edge site-1 and odd-positive-branch contributions both have coefficient r²/8; their entropy derivatives combine to log(q/p). Contributions from the even-block small branch are O_N(r⁴|ln r|) by the shared-amplitude closure; the odd zero branch has zero first directional entropy derivative at the symmetric reference. The large pair eigenvalue is 1-O(r²), and its entropy derivative is O_N(r⁴).

Since q/p→2(N−2)/(N−1), the physical derivatives (u-derivatives divided by J) give
[
B-C=rac{J}{8h^2}lnrac{2(N-2)}{N-1}
+O_Nleft(rac{J^2}{h^3}(1+|ln(J/h)|)ight).
]
The logarithm is strictly positive for N≥4. This is a local weak-coupling asymptotic, not a global sign result.

## 4. Verification boundary

The analytic branch and derivative bookkeeping is consistent with the corrected block structure and even-block closure. This report is an independent algebraic derivation, not machine-checked. The complete edge derivative expansion of all higher-order block entries is not formalized; no Lean proof/build was run. The earlier source Lemma 5.2 sign conflict remains to be reconciled.

**Verdict:** Leading weak-coupling asymptotic remains analytically supported at fixed finite N≥4; full PROP-0012 remains NOT-VERIFIED until complete remainder derivation and source conflict/formalization are resolved.
