# IV-173 — Independent Recovery and Audit: IV-166 Formula Defect

## Scope
Recover the committed IV-165 and IV-166 files from the repository tree and inspect their actual equations. This note records a concrete algebraic error found in IV-166, rather than treating inherited constants as verified.

## Definitions recovered
From IV-165:
\[
P_z=\frac{z^2}{t}=16(1-p)G^2H,\qquad
P_w=\frac{w^2}{t}=\frac{1024tp(1-p)}{F^2}.
\]
Set endpoint-regular factors
\[
R_z=16G^2H,\qquad R_w=\frac{1024t}{F^2}.
\]
Then necessarily
\[
P_z=(1-p)R_z,\qquad P_w=p(1-p)R_w.
\]
By definition,
\[
q_3=\frac{z^2+w^2}{D},\qquad Q_3=\frac{q_3}{t}=\frac{P_z+P_w}{D}.
\]

## Defect in IV-166
IV-166 states
\[
Q_3=\frac{R_z+R_w}{D}.
\]
This drops the factors \((1-p)\) in the z-component and \(p(1-p)\) in the w-component. It does not follow from the recovered definitions and is generally false.

## Correct identity
The correct endpoint-regular expression is
\[
\boxed{Q_3(t,p)=\frac{(1-p)R_z+p(1-p)R_w}{D}
=\frac{(1-p)(R_z+pR_w)}{D}.}
\]
This formula also correctly gives \(Q_3(t,1)=0\), consistent with \(q_3=0\) at the axis \(p=1\). The erroneous IV-166 formula would generally fail to vanish there.

## Downstream impact / dependency invalidation
The following IV-166 estimates and any downstream uses of them are **not certified by IV-166 as written** and must be recomputed from the corrected numerator:
- \(N_3\) upper bound and its \(t,p\) derivative bounds;
- \(Q_3\), \((Q_3)_t\), \((Q_3)_p\) bounds;
- IV-167 entropy derivative formulas when using numeric Q3 derivative estimates;
- IV-168 through IV-172 finite/logarithmic estimates whenever they depend on the incorrect Q3 representation or inherited numeric Q3 bounds.

The entropy chain-rule identities and the exact entropy decomposition remain algebraically valid when Q3 is correctly defined; their downstream numerical certificates do not automatically survive.

## What remains valid
- IV-165 definitions of \(P_z,P_w\) are consistent with the original amplitudes.
- The definition \(Q_3=(P_z+P_w)/D\) is valid.
- The corrected factorization above is exact.
- The axis endpoint check \(Q_3(t,1)=0\) is exact.

## Status
This is a verified algebraic correction from the actual committed files. It invalidates downstream Q3 derivative/numerical bounds pending repair. It is not a claim that the entire proposition fails.

## Next audit target
Re-derive conservative bounds for the corrected numerator
\[
N_3=(1-p)R_z+p(1-p)R_w
\]
and its derivatives, then propagate quotient-rule estimates to \(Q_3\). Recompute every dependent entropy bound before using it.
