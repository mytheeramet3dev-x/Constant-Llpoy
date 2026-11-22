# Paper A — IV-171: Endpoint-Preserving Finite Entropy Comparison

## Status
This is a conditional analytic derivation using IV-169's exact coefficient factorization and the reported IV-166 bound \(Q\le M=2.265265\). IV-165/166 constants have not yet been independently audited; conclusions depending on them are therefore conditional.

## 1. Set the two normalized arguments
Let
\[
a=Q,\qquad b=(1-p)Q_3,\qquad C=a-b.
\]
IV-169 gives \(C>0\) for \(p>0\) and
\[
c_-p\le C\le c_+p,
\]
where \(c_-=0.83678321389\) and \(c_+=1.16666987848\) are displayed rounded versions of the recorded constants. IV-166 supplies the provisional range \(0\le a,b\le M=2.265265<e\).

## 2. Endpoint-preserving finite term
Recall \(\Phi(s)=s(1-\log s)\), continuously extended by \(\Phi(0)=0\). Since \(\Phi'(s)=-\log s\), for \(0\le b\le a\le M\),
\[
\Phi(a)-\Phi(b)=\int_b^a-\log s\,ds
\ge-(a-b)\log M.
\]
Thus
\[
\boxed{\Phi(Q)-\Phi((1-p)Q_3)\ge-C\log M.}
\]
This estimate preserves the vanishing factor \(C\) at \(p=0\); it does not replace the finite difference by a fixed negative constant.

## 3. Endpoint-preserving analytic remainder
Because \(q=t a\), \(q_3=t b\), we have \(q-q_3=tC\). On \(0\le s\le1/2\), \(|g'(s)|=-\log(1-s)\le2s\). With \(a,b\le M\) and \(q,q_3\le1/2\), the mean-value estimate gives
\[
|g(q)-g(q_3)|
\le 2tM\,|q-q_3|
=2Mt^2C.
\]
Hence the remainder has the same angular factor \(C\).

## 4. Composite lower bound
Substituting the finite-term and remainder estimates into IV-168:
\[
\boxed{
h(q)-h(q_3)\ge
tC\left[\log(1/t)-\log M-2Mt\right].
}
\]
For \(0<t\le1/64\), the bracket is decreasing in \(t\) and therefore
\[
\log(1/t)-\log M-2Mt
\ge \log64-\log M-\frac{M}{32}
\approx3.2704018022>0.
\]
Using \(C\ge c_-p\), conditionally on the inherited factor bounds,
\[
\boxed{h(q)-h(q_3)\ge 2.7366173307\,tp}
\]
throughout \(0<t\le1/64\), with the rounded coefficient conservative. Thus
\[
\boxed{\Delta S=2[h(q)-h(q_3)]\ge5.4732346615\,tp.}
\]

## 5. Endpoints
At \(p=0\), \(C=0\) and the exact entropy difference vanishes. The estimate also vanishes with \(p\), so it does not create a false positive endpoint claim.
At \(p=1\), the lower estimate remains finite and positive for \(t>0\); the convention \(0\log0=0\) handles \(q_3=0\).

## 6. Qualification
This is an endpoint-preserving lower estimate conditional on IV-166 normalized probability bounds and IV-169's certificate. Because the IV-165/166 estimates have not been independently audited, this result is not yet an unconditional certified theorem. No Lean verification is claimed.

## Repository record
