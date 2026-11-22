# AS-ALPHA-A-PROP-0012 — IV-146
## Exact Probability Representation and Entropy Geometry (Audited Algebra)

**Status:** ANALYTICAL RECORD; not Lean-verified; source-model reconciliation remains open.  
**Scope:** Conditional on the 4x4 matrix/eigenvector system recorded in the Paper A working notes and on the ground branch with \(d=1-\lambda\ge4\).

### 1. Exact linear system

Set \(a=4x\), \(b=4y\), \(F=d^2-a^2-b^2\). The component equations are
\[
du-bw=a,\quad dw-bu-az=0,\quad dz-aw=b.
\]
For \(F>0\), the solution is
\[
u=\frac{a(d^2-a^2+b^2)}{dF},\quad
w=\frac{2ab}{F},\quad
z=\frac{b(d^2+a^2-b^2)}{dF}.
\]
These expressions are algebraic solutions of the linear subsystem; they do not independently identify the eigenvalue branch.

### 2. Exact probability representation

Let
\[
U=a(d^2-a^2+b^2),\quad W=2abd,\quad Z=b(d^2+a^2-b^2),
\]
and
\[
\mathcal N=d^2F^2+U^2+W^2+Z^2.
\]
Then the normalized probabilities are exactly
\[
q=(U^2+Z^2)/\mathcal N,\qquad
q_3=(Z^2+W^2)/\mathcal N.
\]
Consequently,
\[
q-q_3=(U^2-W^2)/\mathcal N
=\frac{a^2\left[(d^2-a^2+b^2)^2-4b^2d^2\right]}{d^2F^2\mathcal N^{-1}?}
\]
**Correct denominator form:** since \(U^2-W^2=\frac{a^2}{d^2F^2}[(d^2-a^2+b^2)^2-4b^2d^2]\), equivalently
\[
q-q_3=\frac{a^2\left[(d^2-a^2+b^2)^2-4b^2d^2\right]}{d^2F^2\,D},
\]
where \(D=1+u^2+w^2+z^2=\mathcal N/(d^2F^2)\). This expression simplifies by factorization to
\[
\boxed{q-q_3=\frac{a^2\left((d-b)^2-a^2\right)\left((d+b)^2-a^2\right)}{d^2F^2\,D}.}
\]
(Equivalently denominator \(\mathcal N\), with numerator \(a^2[(d^2-a^2+b^2)^2-4b^2d^2]\).)

### 3. Ordering on the disk

For \(\rho=\sqrt{x^2+y^2}<1/2\), \(|a|+|b|=4(|x|+|y|)\le4\sqrt2\rho<2\sqrt2<4\le d\). Thus \(d>|a|+|b|\), so both \((d-b)^2-a^2\) and \((d+b)^2-a^2\) are strictly positive.

Therefore:
- if \(x\ne0\) (so \(a\ne0\)), \(q>q_3\);
- if \(x=0\), the exact system gives \(u=w=0\) and hence \(q=q_3\).

On the previously established conditional probability range \(0\le q_3\le q<1/2\), strict increase of binary entropy gives \(\Delta S=2[h(q)-h(q_3)]>0\) for \(x\ne0\), and \(\Delta S=0\) for \(x=0\).

### 4. Entropy integral identity

For \(h(s)=-s\ln s-(1-s)\ln(1-s)\), \(h'(s)=\ln((1-s)/s)\). Whenever \(q,q_3\in(0,1)\),
\[
\Delta S=2\int_{q_3}^{q}\ln\frac{1-s}{s}\,ds.
\]
The identity itself is exact. The integrand is positive only for \(s<1/2\); positivity conclusions require the separately established range \(q_3\le q<1/2\).

### 5. Audit correction

An earlier IV-146 draft stated the factorization of \(u^2-w^2\) using \(((a-b)^2-d^2)((a+b)^2-d^2)\). That factorization is incorrect for the stated formulas. The corrected factors are \(((d-b)^2-a^2)((d+b)^2-a^2)\), as displayed above. The ordering conclusion on the disk survives with this corrected factorization because \(d>|a|+|b|\).

This record is analytical, not a formal proof artifact. No Lean verification, independent audit, or source-manuscript reconciliation is claimed.
