# IV-156 — Exact Audit of Ground-State Probability Identities and Entropy Geometry

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC AUDIT; conditional on matrix model; not Lean-verified

## 1. Scope

This record re-derives the probability comparison from the corrected eigenvector components and audits the entropy-sign conclusion under the stated 4-by-4 matrix model. It does not claim that the model is reconciled with the original manuscript or that all earlier entropy expansions are independently verified.

## 2. Corrected eigenvector components

Let \(\lambda=-3+\delta\), \(d=4-\delta\), \(F=d^2-16x^2-16y^2\), and normalize the eigenvector as \(\psi=(1,u,w,z)\). The simultaneous solution of the three lower-row equations is

\[
u=\frac{4x(d^2-16x^2+16y^2)}{dF},\quad
w=\frac{32xy}{F},\quad
z=\frac{4y(d^2+16x^2-16y^2)}{dF}.
\]

The audit uses these corrected components, not the superseded IV-133 elimination.

## 3. Normalization and probabilities

Set
\[
D=1+u^2+w^2+z^2>0.
\]
The probability quantities are
\[
q=\frac{u^2+z^2}{D},\qquad
q_3=\frac{z^2+w^2}{D}.
\]
Subtracting directly cancels the shared \(z^2\) term:
\[
\boxed{q-q_3=\frac{u^2-w^2}{D}}.
\]

Exact symbolic factorization gives
\[
u^2-w^2=
\frac{16x^2\big(d^2-16(x-y)^2\big)
\big(d^2-16(x+y)^2\big)}
{d^2F^2}.
\]
This factorization was checked by symbolic algebra against the corrected component formulas.

For the disk \(\rho<1/2\), \(d\ge4\), we have
\[
4|x\pm y|\le4\sqrt2\rho<2\sqrt2<4\le d,
\]
so both factors \(d^2-16(x\pm y)^2\) are strictly positive. Also \(F>0\) because \(d^2\ge16>16\rho^2\). Therefore:
- if \(x\ne0\), then \(u^2-w^2>0\), hence \(q>q_3\);
- if \(x=0\), then the corrected component formulas give \(u=w=0\), hence \(q=q_3\).

## 4. Entropy range

From the resolvent bound previously obtained for \(\rho<1/2\), \(\|v\|=\sqrt{u^2+w^2+z^2}<1\). Hence
\[
u^2+w^2+z^2<1.
\]
This implies
\[
u^2+z^2<1+w^2,\quad z^2+w^2<1+u^2,
\]
and therefore
\[
0\le q<\frac12,\qquad 0\le q_3<\frac12.
\]
(The strict lower endpoint can be attained on axes, so write nonnegative rather than strictly positive.)

## 5. Exact entropy-sign consequence

Define binary entropy \(h(s)=-s\ln s-(1-s)\ln(1-s)\), with continuous endpoint convention. It is strictly increasing on \([0,1/2]\) except that strict monotonicity is understood between distinct arguments, as \(h'(s)=\ln((1-s)/s)>0\) for \(0<s<1/2\).

Thus, for \(x\ne0\), \(0\le q_3<q<1/2\) implies
\[
\boxed{h(q)-h(q_3)>0}.
\]
For \(x=0\), \(q=q_3\), so the entropy difference is zero. Under the manuscript's convention \(\Delta S=2[h(q)-h(q_3)]\), the same sign conclusion follows.

This is a sign/ordering result only. It does **not** prove radial monotonicity of the entropy difference, an asymptotic expansion, or a global extremum claim.

## 6. Numerical spot-checks (direct eigensolver)

Direct eigensolver samples (values rounded):
- (0.1,0.05): q=0.0122357248785261, q3=0.00260128104152496.
- (0.2,0.1): q=0.0459759982663630, q3=0.0114045643113493.
- (0.1,0.2): q=0.0459759982663631, q3=0.0373331397776096.
- (0.3,0.2): q=0.108830726752323, q3=0.0470264826325291.
- (0.2,-0.15): q=0.0578346796944215, q3=0.0246331682895379.
- (0.25,0): q=0.0527864045000421, q3=0.
- (0,0.25): q=q3=0.0527864045000421.

These finite samples corroborate the formula but are not the proof; the symbolic factorization and range argument establish the sign condition within the assumptions.

## 7. Conclusions and outstanding work

Audited conditionally:
- corrected component formulas yield the stated probabilities;
- the exact difference identity and factorization establish \(q-q_3\)'s sign;
- the resolvent norm bound places both probabilities below one-half;
- binary entropy monotonicity gives the sign of the entropy difference.

Not audited here:
- IV-146's complete exact probability formulas beyond the identities above;
- IV-147's small-coupling expansions and their remainder/uniformity claims;
- original manuscript reconciliation;
- Lean formalization or independent external review.

## 8. Next task

Review IV-147's small-coupling expansion independently, checking degree-by-degree terms and whether the stated remainder bounds are uniform in angle. If discrepancies appear, explicitly supersede the old expansion and preserve this audit record.
