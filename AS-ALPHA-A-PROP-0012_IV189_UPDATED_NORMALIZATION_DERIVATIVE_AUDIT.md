# IV-189 — Updated Normalization-Derivative Audit after IV-187/188

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Dependency-aware denominator bounds recorded; normalized component derivative ceilings intentionally not recalculated due missing verified component-source files in this retrieval.

## 1. Denominator
Use the inherited normalization \(D=1+S\), where \(S=P_u+P_z+P_w\). Since the component amplitudes are nonnegative on the stated domain, \(D\ge1\). IV-186 gives \(S<1.081145\), hence \(D<2.081145\).

## 2. Updated denominator derivative ceilings
IV-187 and IV-188 give conditional dependency-aware bounds:
\[
|D_t|=|S_t|<17.199243,\qquad |D_p|=|S_p|<0.204390.
\]
These replace the prior denominator derivative ceilings for subsequent work, subject to their inherited assumptions.

## 3. Quotient rule—correct form
For each normalized component \(Q_i=P_i/D\):
\[
(Q_i)_t=\frac{(P_i)_tD-P_iD_t}{D^2},\qquad
(Q_i)_p=\frac{(P_i)_pD-P_iD_p}{D^2}.
\]
Equivalently, because \(D>0\):
\[
(Q_i)_t=\frac{(P_i)_t}{D}-Q_i\frac{D_t}{D},\qquad
(Q_i)_p=\frac{(P_i)_p}{D}-Q_i\frac{D_p}{D}.
\]
Do not use the updated \(D_t,D_p\) to claim new numeric \(Q_i\)-derivative ceilings until verified component bounds \((P_i)_t,(P_i)_p\) and denominator dependencies are re-evaluated together. Existing component source files IV-180 and IV-185 could not be located under the guessed filenames during this retrieval; their earlier chat summaries are not treated as verified repository records.

## 4. Immediate implication
The angular denominator derivative ceiling is substantially tightened from the earlier summarized \(2.408660592\) to \(0.204390\), but the quotient-rule numerator terms can still dominate. This record therefore updates only \(D,D_t,D_p\) and fixes the propagation formulas; it does **not** assert a new normalized-vector Lipschitz constant.

## 5. Verification and scope
This is conditional on IV-186 amplitude and IV-187/188 derivative estimates and on the normalization \(D=1+S\). It is a consistency/propagation audit, not proof of the underlying proposition, root/domain assumptions, or component derivative ceilings.
