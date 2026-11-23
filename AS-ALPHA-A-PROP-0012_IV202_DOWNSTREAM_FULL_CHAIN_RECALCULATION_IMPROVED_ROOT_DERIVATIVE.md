# IV-202 — Downstream Full-Chain Recalculation Using Improved Root Derivative Bound

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional bound recalculation. Inherited formulas, domain, and root assumptions remain unverified.

## 1. Update and scope
IV-201 improved the conditional implicit-root derivative ceiling to \(0\le d_t<4.128\) while retaining \(|d_p|\le1/252\). This audit propagates that improved radial ceiling through the retrieved IV-180, IV-186–IV-192 formulas. It does not claim independent source-fidelity or proof closure.

Use \(d_* =256/63\), \(t_*=1/64\), \(M=d_*^2+1/4\), \(H_* =1/3969\), \(F_*=63/4\).

## 2. Recomputed upstream derivative inputs
From \(A_t,G_t=2dd_t\pm16(1-2p)\), the updated uniform ceiling is
\[
|A_t|,|G_t|<2d_*\cdot4.128+16=49.54819047619\ldots
\]
Similarly,
\[
|F_t|<49.54819047619\ldots.
\]
Retaining the IV-180 conservative angular structure, and recalculating its inputs:
\[
|A_p|,|G_p|\le 2d_*/252+32t_*=0.53224993701184\ldots,
\]
\[
|F_p|\le2d_*/252=0.03224993701184\ldots,
\]
\[
|H_t|\le H_*(2(4.128)/4+2(49.54819047619\ldots)/(63/4))
<0.002105275,
\]
\[
|H_p|\le H_*(2(1/252)/d_*+2(0.03224993701184\ldots)/(63/4))
<1.524\times10^{-6}.
\]

## 3. Component bounds recalculated
Using the IV-180 displayed conservative product-rule forms, with updated radial inputs:
- \(P_u,P_z<1.132632151\) (amplitude unchanged).
- \(|(P_u)_t|,|(P_z)_t|<16.160182018\).
- \(|(P_u)_p|,|(P_z)_p|<2.345169494\) (recomputed with updated \(H_p\) and \(A_p,G_p\), using the same conservative IV-180 angular expression).
- \(P_w<0.016124969\) (unchanged amplitude).
- \(|(P_w)_t|<1.133453605\).
- \(|(P_w)_p|<0.064565910\).

These are upward-rounded arithmetic ceilings for the displayed bounding expressions.

## 4. Dependency-aware pair and normalization
With updated \(a_{t,*}=2d_*\cdot4.128\), the IV-187 absolute expression yields
\[
|B_t|<2197.433309674,
\]
and hence, using \(B\le d_*^4\), \(H\le1/3969\), and the updated \(H_t\),
\[
|(P_u+P_z)_t|<18.042268589.
\]
Add the new \(P_w\) radial ceiling:
\[
|S_t|<19.175722194.
\]
The angular dependency-aware bound from IV-188 remains unchanged; together with the recalculated \(P_w\) angular derivative:
\[
|S_p|<0.204389553.
\]
Keep the dependency-aware amplitude \(S<1.081145\), so corrected normalization \(D=1+tS\) gives:
\[
1\le D<1.016892890625,
\]
\[
|D_t|<1.380765660,\quad |D_p|<0.003193587.
\]

## 5. Normalized quotient derivative ceilings
Using \(D\ge1\), the same absolute-value quotient-rule estimates as IV-190:
- \(|(Q_u)_t|,|(Q_z)_t|<17.724081596\).
- \(|(Q_u)_p|,|(Q_z)_p|<2.348786653\).
- \(|(Q_w)_t|<1.155718408\).
- \(|(Q_w)_p|<0.064617406\).

For \(Q_3=(P_z+P_w)/D\), use the dependency-aware radial pair ceiling:
- \(|(Q_3)_t|<20.761886575\).
- \(|(Q_3)_p|<2.413404059\).

## 6. Vector norm aggregation
For the three-component vector \(Q=(Q_u,Q_z,Q_w)\) and two input variables:
\[
\|Q_t\|_2<25.092266177,
\]
\[
\|Q_p\|_2<3.322314388,
\]
\[
\|J_Q\|_F=\sqrt{\|Q_t\|_2^2+\|Q_p\|_2^2}
<25.311254311.
\]
By \(\|J_Q\|_{op}\le\|J_Q\|_F\), this is a conditional Jacobian/operator-norm ceiling, and the global Lipschitz inference still requires differentiability and segment/domain coverage.

## 7. Comparison to IV-196 inherited chain
| Quantity | IV-196 ceiling | IV-202 recalculated ceiling |
|---|---:|---:|
| \(\|Q_t\|_2\) | 25.308668 | 25.092266177 |
| \(\|Q_p\|_2\) | 3.322387 | 3.322314388 |
| Combined \(\|J\|_F\) | 25.525810 | 25.311254311 |

The combined bound decreases by approximately 0.214554 (using the displayed ceilings). The radial improvement is substantial; the angular aggregate changes only slightly.

## 8. Verdict and limitations
- **PASS (conditional arithmetic propagation):** the updated \(d_t<4.128\) is propagated through the displayed component, normalization, quotient, and vector-norm estimates.
- **Numerical improvement:** combined ceiling becomes \(25.311254311\), compared with the prior conservative \(25.525810\).
- **Not closed:** this remains conditional on the reconstructed root equation/domain, IV-198 sign, root existence/uniqueness, inherited angular bounds, differentiability, and segment/domain conditions. This is not interval arithmetic or formal Lean verification.
- The recalculated ceilings should not be promoted to theorem-level claims until upstream dependencies and source fidelity are independently closed.
