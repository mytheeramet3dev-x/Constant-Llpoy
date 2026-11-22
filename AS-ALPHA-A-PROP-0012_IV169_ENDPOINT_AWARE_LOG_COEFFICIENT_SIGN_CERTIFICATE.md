# Paper A — IV-169: Endpoint-Aware Logarithmic Coefficient Sign Certificate

## Status and scope
This note derives an exact factorization and a uniform positive lower bound for the logarithmic coefficient in IV-168. The bound is analytic on the IV-161 domain and does not rely on an angular grid. It does not certify the IV-165/166 derivative constants.

## 1. Coefficient definition
With \(t=\rho^2\), \(p=\cos^2\theta\), and \(\varepsilon=1-p\),
\[
q=tQ,\qquad q_3=t\varepsilon Q_3.
\]
The coefficient of \(t\log(1/t)\) in IV-168 is
\[
C(t,p)=Q-\varepsilon Q_3=\frac{q-q_3}{t}
\]
for \(t>0\), with endpoint continuation where appropriate.

## 2. Exact factorization
Using \(q-q_3=(u^2-w^2)/D\) and the previously established identity,
\[
u^2-w^2=\frac{16x^2[d^2-16(x-y)^2][d^2-16(x+y)^2]}{d^2F^2},
\]
and \(x^2=tp\), we obtain
\[
\boxed{
C(t,p)=\frac{16p[d^2-16(x-y)^2][d^2-16(x+y)^2]}{d^2F^2D}.
}
\]
Here \(F=d^2-16t\), \(D=1+u^2+w^2+z^2\). This identity is exact for \(t>0\); its continuous limit at \(t=0\) is used when defined.

## 3. Uniform sign and explicit lower bound
On \(t\le1/64\), \(d\ge4\), and \(d\le d_*:=256/63\), while \(F\ge63/4\), \(D\le50/49\).
Moreover,
\[
(x\pm y)^2\le(|x|+|y|)^2\le2(x^2+y^2)=2t,
\]
so \(16(x\pm y)^2\le32t\le1/2\). Hence each bracket is at least
\[
d^2-\frac12\ge\frac{31}{2}.
\]
Bounding the denominator from above gives the rigorous estimate
\[
C(t,p)\ge c_*p,
\qquad
c_*:=\frac{16(31/2)^2}{d_*^6(50/49)}
\approx0.8367832138900445.
\]
This constant uses \(d^2F^2\le d_*^6\) because \(F\le d^2\le d_*^2\), and \(D\le50/49\).

## 4. Uniform upper bound
Also \(16(x\pm y)^2\le1/2\), so the brackets are at most \(d_*^2+1/2\). Using \(d^2\ge16\), \(F\ge63/4\), and \(D\ge1\),
\[
C(t,p)\le c^*p,
\quad
c^*:=\frac{16(d_*^2+1/2)^2}{16(63/4)^2}
\approx1.166669878474913.
\]
Therefore,
\[
\boxed{0.8367832\,p\le C(t,p)\le1.1666699\,p}
\]
throughout the IV-161 disk, with rounded decimals displayed only for readability; the exact rational expressions above are the certificate.

## 5. Endpoint behavior and interpretation
- At \(p=0\), \(x=0\) and \(C=0\) exactly. The logarithmic coefficient vanishes, so this certificate is endpoint-aware rather than falsely claiming a uniform positive lower bound independent of angle.
- For \(0<p\le1\), \(C>0\) and is quantitatively bounded below by \(c_*p\).
- The \(p\to0\) behavior is at least linearly controlled by this bound and at most linearly by the upper bound. Thus the coefficient has no angular sign reversal.
- At \(p=1\), the coefficient remains positive and bounded, while \(q_3=0\) by the exact endpoint structure; terms involving \(\varepsilon Q_3\log(1/(\varepsilon Q_3))\) use the continuous zero convention.

## 6. What this does not prove
This certificate controls the sign and size of the leading logarithmic coefficient only. It is not by itself a lower bound for the full entropy difference, because the finite \(t\)-terms in IV-168 must also be controlled. It also does not replace the independent audit of the inherited IV-165/166 estimates.

## Repository record
Analytic derivation, exact factorization, and rational-constant bounds; not Lean-certified.
