# IV-196 — Independent Full-Chain Numerical Recalculation from Retrieved Source Bounds

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Independent numerical recomputation from the formulas and inherited ceilings retrievable in IV-180, IV-186–IV-192. This is not a certification of upstream hypotheses or formulas.

## 1. Source records actually inspected
- IV-180: component definitions and preliminary component/derivative ceilings.
- IV-186: dependency-aware amplitude identity and \(S\) bound.
- IV-187: dependency-aware radial derivative of \(P_u+P_z\).
- IV-188: dependency-aware angular derivative of \(P_u+P_z\).
- IV-190: corrected normalization and quotient-ceiling calculations.
- IV-191: vector norm aggregate.
- IV-192: arithmetic audit.

## 2. Recalculation of IV-180 component bounds
Using \(M=(256/63)^2+1/4\), \(H\le1/3969\), \(|H_t|<0.002131\), \(|H_p|<1.535\cdot10^{-6}\), \(|A_t|,|G_t|<50.084572\), and \(|A_p|,|G_p|<0.532250\), I independently evaluate the displayed IV-180 formulas:
- \(P_u,P_z\) individual ceiling arithmetic: \(1.1326321505836299\), below the stated \(1.132633\).
- Radial pair component derivative expression: \(16.348318013091443\), below \(16.348319\).
- Angular pair component derivative expression: \(2.3452195399836016\), below \(2.345220\).
- \(P_w\) amplitude expression: \(0.01612496850592089\), below \(0.016124969\).
- \(|(P_w)_t|\): \(1.134551907697353\), below \(1.134552\).
- \(|(P_w)_p|\): \(0.06456590948204138\), below \(0.064566\).

These are arithmetic reproductions of the stated formulas, conditional on their input ceilings and definitions.

## 3. Dependency-aware pair derivative recomputation
From \(a_*=(256/63)^2\), \(a_{t,*}=2(256/63)(4.194)\), \(B_*=a_*^2\), \(t_*=1/64\):
- \(B_{t,*}=1679.0319421228808\), below \(1679.031943\).
- \(B_{p,*}=128a_*t_*=33.02393550012597\), below \(33.023936\).
- Radial pair derivative bound: \(16.06469090966374\), below \(16.064691\).
- Angular pair derivative bound: \(0.1398236431100007\), below \(0.139823644\).

Using the more precise computed \(P_w\) angular derivative ceiling:
- \(S_t\) recomputed: \(17.199242817361093\), below \(17.199242818\).
- \(S_p\) recomputed: \(0.20438955259204208\), below the recorded rounded ceiling \(0.204389644\).

The IV-192 \(S_p\) ceiling is valid but slightly looser because it adds already rounded component ceilings. No error is implied by that conservatism.

## 4. Corrected normalization recomputation
With \(D=1+tS\), \(0\le t\le1/64\), use the recorded upward ceilings \(S<1.081145\), \(S_t<17.199242818\), and \(S_p<0.204389644\):
- \(D<1.016892890625\).
- \(|D_t|<1.349883169026\).
- \(|D_p|<0.003193588188\).

The quotient derivative arithmetic, using the IV-190 rounded inputs, reproduces:
- \(|(Q_u)_t|,|(Q_z)_t|<17.877241223383425\), below the IV-190 ceiling \(17.877241224\).
- \(|(Q_u)_p|,|(Q_z)_p|<2.348837163370139\), below IV-190's ceiling \(2.348837164\).
- \(|(Q_w)_t|<1.156318824254166\), below \(1.156318825\).
- \(|(Q_w)_p|<0.06461749651053027\), below \(0.064617497\).
- \(|(Q_3)_t|<19.03356008948397\), below \(19.033560090\).
- \(|(Q_3)_p|<2.4134546599796707\), below \(2.413454660\).

## 5. Vector norm aggregation
Using the rounded IV-191 component inputs, independent recomputation reproduces the stated conservative ceilings:
- \(\|Q_t\|_2<25.308668\).
- \(\|Q_p\|_2<3.322387\).
- Combined Frobenius/Jacobian ceiling \(<25.525810\).

The operator-norm inequality \(\|J\|_{op}\le\|J\|_F\) is mathematically valid. The Lipschitz inference remains conditional on differentiability and the derivative bounds holding throughout the connecting segment.

## 6. Full-chain verdict and limitations
**Arithmetic propagation: pass for the displayed formulas and rounded input ceilings.** The numerical ceilings in IV-190, IV-191, and IV-192 are reproduced and remain conservative.

This audit is not fully independent of the underlying mathematics: it relies on the same displayed source formulas and inherited hypotheses. It does not establish \(R_d\le0\), existence/uniqueness of the implicit root, the admissible branch's full domain, differentiability of the branch, or upstream derivative assumptions. No interval-arithmetic or Lean proof is supplied here.

The phrase “full-chain” means the arithmetic chain from the retrievable component formulas through normalized derivatives and aggregate norm; it does not mean the proposition's entire proof chain is closed.
