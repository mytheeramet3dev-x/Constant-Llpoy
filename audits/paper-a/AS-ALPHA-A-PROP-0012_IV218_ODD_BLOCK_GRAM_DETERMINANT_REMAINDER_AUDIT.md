# IV-218 — Odd-Block Gram Matrix & Determinant Remainder Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling lower-branch response, fixed finite N≥4.
**Inputs inspected on main:** 
- `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md`
- `source_snapshots/paper-a/docs/final_fixed_N_corrected_proof.md`
- `source_snapshots/paper-a/docs/fixed_N_theorem_hard_audit.md`
- `source_snapshots/paper-a/docs/entropy_schur_remainder_lemma.md`

## Verdict
**PASS** for the leading odd-block Gram representation and rank-one uniform leading matrix, conditional on the source's first-order pair-flip amplitude expansion.
**CONDITIONAL / OPEN** for determinant-derived small eigenvalue, derivative remainder, and its full entropy response. The documents do not furnish the required explicit higher-order matrix-entry remainder constants or a closed derivative determinant bound. No theorem promotion.

## 1. Gram structure
For the odd block on basis ((+-,-+)), the leading environment sum over (k\ge3) is
\[
M_{odd}^{(2)}=\begin{pmatrix}\sum_{k\ge3}a_{2k}^2&\sum_{k\ge3}a_{1k}a_{2k}\\
\sum_{k\ge3}a_{1k}a_{2k}&\sum_{k\ge3}a_{1k}^2\end{pmatrix}.
\]
This is a Gram matrix: take vectors (v_2=(a_{2k})_{k\ge3}), (v_1=(a_{1k})_{k\ge3}); entries are their squared norms and inner product. Consequently PSD and determinant
\[
\det M_{odd}^{(2)}=\|v_1\|^2\|v_2\|^2-|\langle v_1,v_2\rangle|^2\ge0.
\]
This representation is valid for real leading amplitudes; the complex version uses conjugation in the inner product.

## 2. Uniform point and rank-one leading order
At uniform (a_{ik}=r/4), (m=N-2):
\[
M_{odd}^{(2)}=\frac{mr^2}{16}\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Eigenvalues are (q=mr^2/8=(N-2)r^2/8) and zero. Thus leading rank is one, with the zero direction proportional to ((1,-1)). This is an exact statement about the displayed leading matrix, not the complete block at finite (r).

## 3. First edge-derivative check of the positive branch
The positive leading eigenvalue is (q=\frac12\sum_{k\ge3}(a_{1k}+a_{2k})^2) for real amplitudes.
Using (a_{ij}=r(1+u_{ij})/4):
- (u_{13}) changes (a_{13}) only in the displayed leading environment sum, giving (\partial_{u_{13}}q=r^2/8).
- (u_{34}) is not one of the edges (1k) or (2k) with (k\ge3) in that first-order amplitude sum; its derivative of this leading (q) is zero.
Therefore the leading derivatives reconcile with the source's stated (partial_{u_{13}}q=r^2/8+O_N(r^3)) and (partial_{u_{34}}q=O_N(r^3)), **provided** the higher-order entry/branch remainder and its edge derivatives are controlled.

## 4. Determinant and small eigenvalue: what follows, what does not
For a full (2\times2) block (M(r,u)=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix}\), its eigenvalues obey
\[
\lambda_s=\frac{\det M}{\lambda_L},\quad \det M=ad-|b|^2,\quad \lambda_L\asymp_N r^2
\]
when the leading positive branch is (O(r^2)) and bounded away from zero after division by (r^2).
However, the audited source's leading Gram matrix has rank one; it only gives determinant zero at leading order. It does **not**, on its own, prove a full-block (det M=O_N(r^4)), nor (\partial_{u_e}\det M=O_N(r^4)). These need consistent expansions of all block entries through higher order, with derivative bounds and cancellation.

In particular, a generic entrywise (O_N(r^3)) error in a matrix whose entries are (O(r^2)) is insufficient to assert the determinant and its edge derivative have the desired (O(r^4)) control without tracking cross-terms/cancellation. The support-order lemma helps bound individual amplitudes but does not supply these determinant constants by itself.

## 5. Entropy implication
If (and only if) full-block bounds are established:
\[
\lambda_s=O_N(r^4),\quad \partial_{u_e}\lambda_s=O_N(r^4),
\]
with positive branch/log-scale control, then the small-branch entropy derivative is (O_N(r^4(1+|\ln r|))). The entropy–Schur lemma inspected is explicitly conditional on these hypotheses; it cannot close them itself. A nonnegative eigenvalue exactly zero at the uniform point requires separate regularity/opening analysis; do not substitute (ln0).

## 6. Reconciliation with (B-C)
The leading positive-branch response difference remains the source's corrected coefficient:
\[
(B-C)_{lead}=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}>0\quad(N\ge4).
\]
The odd-block leading branch contributes the (u_{13}) derivative (r^2/8) but no (u_{34}) derivative at this order. It is consistent with the coefficient above, but does not prove the full entropy remainder or fixed-N positivity threshold.

## 7. Status table
| Obligation | Status |
|---|---|
| Leading block is a Gram matrix | PASS, given first-order amplitude expansion |
| PSD of leading block | PASS, Gram identity |
| Uniform leading rank one | PASS |
| Positive leading eigenvalue (q=(N-2)r^2/8) | PASS |
| ∂u13 q = r²/8 | PASS, conditional on amplitude normalization |
| ∂u34 q = 0 at leading order | PASS |
| Full-block determinant (O_N(r^4)) | OPEN |
| Edge derivative determinant (O_N(r^4)) | OPEN |
| Small-branch log/entropy derivative closure | CONDITIONAL |
| Fixed-N weak-coupling theorem / positivity threshold | NOT ESTABLISHED |

## 8. Next proof obligation (IV-219)
Obtain a source-backed higher-order expansion for the odd block's four entries and their first edge derivatives, then compute the determinant expansion explicitly. Required outputs: (i) coefficient of (r^4) in (det M_{odd}), (ii) edge derivative coefficients for (u_{13},u_{34}), (iii) remainder order/constants, (iv) decide whether determinant cancellation is structural or merely asserted. If no such expansion is recoverable, record the missing amplitude coefficients as the precise blocker rather than estimating them.
