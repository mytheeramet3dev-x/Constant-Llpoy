# Entropy–Schur Remainder Lemma

**Purpose:** isolate the finite-dimensional entropy estimate needed by the
weak- and strong-coupling endpoint analyses.

## Statement

Let \(\rho(r,u)\) be a \(C^1\) family of positive semidefinite density matrices,
where \(r>0\) is the asymptotic parameter and \(u\) is an edge perturbation.
Suppose that, after a \(C^1\) block change of basis,

\[
\rho=
\begin{pmatrix}L&X\\X^\dagger&S\end{pmatrix},
\qquad L\ge cI
\]

for some \(c>0\), and define the Schur complement

\[
Q=S-X^\dagger L^{-1}X.
\]

Assume

\[
\|Q\|\le K r^4,\qquad
\|\partial_uQ\|\le K r^4/J.
\]

Then the contribution of the small spectral block to the entropy derivative
is bounded by

\[
\left|\partial_u S_{\rm small}(\rho)\right|
\le
\frac{K'}{J}r^4\left(1+|\ln r|\right),
\]

where \(K'\) depends on \(c,K\) and the fixed matrix dimension.

## Proof mechanism

Because \(L\ge cI\), the block Gaussian elimination is uniformly bounded.
The small eigenvalues are controlled by the positive Schur complement \(Q\)
up to a bounded congruence transformation. Thus their total weight and their
first \(u\)-derivative are \(O(r^4)\) and \(O(r^4/J)\), respectively.

For \(0\le\lambda\le Kr^4\),

\[
|-\lambda\ln\lambda|
\le
K_1r^4(1+|\ln r|),
\]

and

\[
\left|\partial_u(-\lambda\ln\lambda)\right|
\le
\frac{K_2r^4}{J}(1+|\ln r|).
\]

Summing over the fixed number of small eigenvalues proves the bound.

## Important qualification

The lemma is conditional on the Schur-complement hypotheses. Kato/Rellich
analyticity of the ground-state projector does not establish those hypotheses
by itself. For the TFIM, the remaining model-specific task is therefore:

\[
\boxed{
\text{prove }Q=O(r^4)\text{ and }\partial_uQ=O(r^4/J)
\text{ for the full ground-state reduced pair.}
}
\]

Once this is done, the entropy remainder estimate is no longer the main
obstacle.

## Derivative bound for an isolated small eigenvalue

Suppose a differentiable eigenvalue branch satisfies

\[
0\le\lambda(r,u)\le Kr^4,
\qquad
|\partial_u\lambda(r,u)|\le \frac{K r^4}{J}.
\]

For \(\lambda>0\),

\[
\partial_u[-\lambda\ln\lambda]
=-(1+\ln\lambda)\partial_u\lambda.
\]

Since \(\lambda\le Kr^4\), the logarithmic factor is bounded by a constant
times \(1+|\ln r|\), provided \(r\) is sufficiently small. Hence

\[
\left|\partial_u[-\lambda\ln\lambda]\right|
\le
\frac{K'}{J}r^4(1+|\ln r|).
\]

If \(\lambda=0\) at an isolated parameter value, the same estimate is
interpreted by continuity along the nonnegative eigenvalue branch. The
estimate requires the eigenvalue derivative bound; positivity and
analyticity of the projector alone do not supply it.

For a fixed \(4\times4\) reduced state, summing over at most four eigenvalues
gives the same order for the total small-eigenvalue entropy derivative.

## Combined conditional endpoint result

The projector lemma, rank-one block lemma, and this scalar entropy estimate
would together imply

\[
\partial_u\bigl[S(\rho_{12})-\ln2\bigr]
=O\!\left(\frac{r^4}{J}(1+|\ln r|)\right)
\]

after the explicit \(O(r^2)\) one-site contribution is removed. The remaining
work is now localized to verifying the block decomposition and derivative
orders for the full TFIM reduced state.
