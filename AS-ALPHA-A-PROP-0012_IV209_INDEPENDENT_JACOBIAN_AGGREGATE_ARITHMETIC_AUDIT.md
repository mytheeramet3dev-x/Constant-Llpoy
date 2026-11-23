# IV-209 — Independent Jacobian Aggregate Arithmetic Audit

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PASS for arithmetic of supplied conditional component ceilings; mathematical premises remain open.

## 1. Inputs independently reassembled
Radial component ceilings (IV-208):
- \(R_u=R_z=17.616462585\)
- \(R_w=1.155173614\)

Angular component ceilings (IV-205/206):
- \(A_u=A_z=2.348672731\)
- \(A_w=0.064617497\)

These are componentwise upper ceilings, not claimed actual derivative values.

## 2. Radial column
\[
\|Q_t\|_2\le\sqrt{R_u^2+R_z^2+R_w^2}
=\sqrt{2(17.616462585)^2+(1.155173614)^2}.
\]
Numerically:
\[
\|Q_t\|_2<24.940207178287263,
\]
upward ceiling: \(24.940207179\).

## 3. Angular column
\[
\|Q_p\|_2\le\sqrt{A_u^2+A_z^2+A_w^2}
=\sqrt{2(2.348672731)^2+(0.064617497)^2}.
\]
Numerically:
\[
\|Q_p\|_2<3.322153310069321,
\]
upward ceiling: \(3.322153311\).

## 4. Frobenius aggregate
By the definition of the Frobenius norm:
\[
\|J_Q\|_F^2=\|Q_t\|_2^2+\|Q_p\|_2^2.
\]
Direct six-entry recomputation gives
\[
\sqrt{2(17.616462585)^2+(1.155173614)^2+
2(2.348672731)^2+(0.064617497)^2}
=25.16049754499096\ldots.
\]
Thus the upward-rounded ceiling is
\[
\boxed{\|J_Q\|_F<25.160497545}.
\]
The IV-208 rounded ceiling is arithmetically confirmed.

## 5. Operator norm implication
For every real matrix,
\[
\|J_Q\|_{\mathrm{op}}\le\|J_Q\|_F.
\]
Hence, conditional on the component derivative ceilings being valid on the relevant domain,
\[
\boxed{\|J_Q\|_{\mathrm{op}}<25.160497545}.
\]
No spectral computation is needed to establish this implication; it is a standard norm inequality.

## 6. What this audit verifies
**PASS:**
- component ceilings are assembled into the correct 3-by-2 Jacobian shape;
- radial and angular column Euclidean norms are recalculated;
- Frobenius norm is independently recomputed directly from all six entries;
- upward rounding is checked;
- operator norm bound follows from Frobenius norm inequality.

**OPEN:**
- validity of upstream componentwise derivative ceilings;
- root existence/uniqueness and root derivative assumptions;
- exact source fidelity of reconstructed formulas;
- domain and segment coverage required for a global Lipschitz inference;
- rigorous interval verification and Lean formalization.

## 7. Conclusion
IV-209 confirms the arithmetic aggregate \(25.160497545\) as an upward-rounded conditional Jacobian Frobenius/operator-norm ceiling. It does not certify the hypotheses that make this ceiling applicable globally, and it does not close Proposition AS-ALPHA-A-PROP-0012.
