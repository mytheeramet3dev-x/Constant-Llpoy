# Lemma 5.2 — Weak-Coupling Audit

**Date:** 2026-08-25  
**Status:** corrected conditional asymptotic derivation; the earlier negative
sign calculation omitted an order-(r^2) coherence and is invalid.

## 1. First-order state

Set \(r=J/h\) and use the \(x\)-polarized basis. To first order,

\[
|\Psi\rangle
=|+\cdots+\rangle
+\sum_{i<j}a_{ij}|i,j\rangle
+O(r^2),
\qquad
a_{ij}=\frac{J_{ij}}{4h}.
\]

For the reduced state on sites \(1,2\), define

\[
w_{ij}=a_{ij}^2.
\]

The order-\(r^2\) weights involving the observed pair are

\[
p_1=w_{12}+\sum_{k\ge3}w_{1k},\qquad
p_2=w_{12}+\sum_{k\ge3}w_{2k}.
\]

The environment-only amplitudes \(a_{kl}\), \(k,l\ge3\), occur in the
normalization of the global state and in the \(++\) component of
\(\rho_{12}\), but the same normalization contribution appears in the trace
of the reduced state. It therefore cancels from the order-\(r^2\) reduced
state. This is the algebraic reason an edge \(J_{34}\) does not enter the
leading response of \(I_{12}\).

## 2. Leading mutual-information expression

**Correction:** The one-flip sector has the order-(r^2) coherence

\[
\rho_{-+,+-}=\sum_{k\ge3}a_{1k}a_{2k}.
\]

At the uniform point its (\{| -+\rangle,|+-\rangle\}) block is

\[
(N-2)w\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

with eigenvalues (2(N-2)w) and (0). This coherence must be included in
the leading entropy calculation.

After diagonalizing the \(++/--\) coherence block and retaining the two
environment-labelled one-flip sectors, the leading entropy combination is

\[
I_{12}=2S((N-1)w)-S(2(N-2)w)+O(r^4|\ln r|),
\]

where \(S(p)=-p\ln p\). This formula is valid only after the omitted
order-\(r^4\) terms and their edge derivatives are controlled.

At the uniform point \(w_{ij}=w=(J/4h)^2\),

\[
p_1=p_2=(N-1)w,\qquad
\sum_{k\ge3}w_{1k}=\sum_{k\ge3}w_{2k}=(N-2)w.
\]

## 3. Leading \(B\) and \(C\)

For the shared edge \(J_{13}\),

\[
\partial_{J_{13}}w_{13}=\frac{J}{8h^2},
\]

and this edge enters only the site-1 environment sum. Hence

\[
B_{\mathrm{lead}}
=\frac{J}{8h^2}
\left[S'((N-1)w)-S'((N-2)w)\right]
=\frac{J}{8h^2}\ln\!\frac{N-2}{N-1}<0.
\]

For the disjoint edge \(J_{34}\), the leading reduced-state expression
contains no \(w_{34}\). Therefore

\[
C_{\mathrm{lead}}=0.
\]

Thus

\[
\boxed{
(B-C)_{\mathrm{lead}}
=\frac{J}{8h^2}\ln\!\frac{N-2}{N-1}<0.
}
\]

## 4. Correction to the sign calculation

The formula immediately above omitted the off-diagonal pair coherence. It is
therefore superseded. At the uniform point the relevant block has eigenvalues
(2(N-2)w) and (0), so the corrected leading expression is

\[
I_{12}^{\rm lead}=2S((N-1)w)-S(2(N-2)w),
\]

and hence

\[
(B-C)_{\rm lead}
=\frac{J}{8h^2}\ln\!\left(\frac{2(N-2)}{N-1}\right)>0.
\]

Thus the previous negative-sign claim is invalid. The corrected leading sign
is positive, but the remainder and its edge derivative remain unbounded, so no
weak-coupling theorem or global sign-flip conclusion follows yet.

## 5. Full order-\(r^2\) pair matrix

Let \(A=1-\frac12\sum_{i<j}a_{ij}^2+O(r^4)\). In the local \(x\)-basis
\((++,+-,-+,--)\), the reduced pair state has the relevant structure

\[
\rho_{12}=
\begin{pmatrix}
1-\sum_{j\ne1,2}(w_{1j}+w_{2j})-w_{12}&0&0&Aa_{12}\\
0&\sum_{j\ge3}w_{2j}&\sum_{j\ge3}a_{1j}a_{2j}&0\\
0&\sum_{j\ge3}a_{1j}a_{2j}&\sum_{j\ge3}w_{1j}&0\\
Aa_{12}&0&0&w_{12}
\end{pmatrix}
+O(r^3),
\]

with the order-\(r^2\) normalization contributions understood. At the
uniform point, the middle block is

\[
(N-2)w\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

whose eigenvalues are \(2(N-2)w\) and \(0\). This is the coherence omitted in
the original negative-sign calculation.

## 6. Sanity check

The exact solver gives positive \(B-C\) at \(h=1\) for \(N=4,6,8\) and
\(J=0.02,0.05,0.10\). The ratio to

\[
\frac{J}{8}\ln\!\frac{2(N-2)}{N-1}
\]

moves toward \(1\) as \(J\to0\), but finite-\(J\) corrections remain
substantial. This is a consistency check only, not a proof.

## 7. What must still be proved

The following items remain open before this is a theorem:

1. derive the displayed reduced-state formula including all order-\(r^2\)
   coherences, rather than only its diagonal shorthand;
2. prove the order-\(r^4|\ln r|\) remainder uniformly for fixed \(N\);
3. prove the corresponding edge-derivative remainder is
   \(o(J/h^2)\);
4. establish that the \(x\to0\) continuation is the lower branch for the
   self-consistency parameterization being used.

The current result is therefore:

\[
\boxed{
\text{The corrected weak-coupling leading sign is positive, but the
remainder is not yet bounded, so no endpoint theorem follows.}
}
\]
