# IV-92 — Controlled asymptotics: boundary and ratio structure

**Status:** analytic examination of the proposed leading expression; no uniform remainder theorem proved.

Let \(x=J_{12}^2/(16h^2)\), \(y=J_{23}^2/(16h^2)\), and
\[
F(x,y)=(x+y)\ln(x+y)-x\ln x-y\ln y,
\]
with \(0\ln0=0\).

## Boundary checks
\(F(0,y)=F(x,0)=0\). This is consistent with exact decoupling when either path edge is absent.

## Homogeneity and ratio form
For \(t=x+y>0\) and \(r=x/t\in[0,1]\),
\[
F(x,y)=t[-r\ln r-(1-r)\ln(1-r)]=tH_2(r).
\]
Hence \(F\) is homogeneous of degree one in \((x,y)\), or degree two in the couplings collectively, but its coefficient is ratio-dependent. Since \(0\le H_2(r)\le\ln2\), we have \(0\le F\le (x+y)\ln2\).

## Boundary-layer behavior
As \(r\to0^+\), \(H_2(r)=-r\ln r+r+O(r^2)\). Thus
\[
F(x,y)=x\ln(y/x)+x+O(x^2/y),\quad x/y\to0,
\]
with the exact expansion requiring \(x/y\) small. This reveals a logarithmic boundary layer and prevents replacing the ratio-dependent coefficient by a constant uniformly over all coupling ratios.

## Proof obligation remaining
To promote the IV-91 expression to a theorem for the exact MI, one still needs eigenvalue expansions of \(\rho_1,\rho_3,\rho_{13}\), with errors controlled in a way that remains valid as either coupling becomes much smaller than the other. Ordinary expansions with additive errors \(O((x+y)^2)\) alone are insufficient near \(x\ll y\), because entropy is sensitive to errors relative to small eigenvalues.

No claim is made here that \(I(1:3)=F(x,y)+o(x+y)\) has been proven uniformly in every coupling direction. The expression remains a proposed leading asymptotic supported by the prior numerical checks.

## Consequences
- Exact decoupling boundary: MI is zero if either coupling is zero.
- Leading expression is nonnegative and bounded above by \((x+y)\ln2\).
- Leading expression depends on coupling ratio, not a fixed polynomial coefficient.
- The singular ratio behavior requires careful remainder control.

Paper A Proposition 0012 remains OPEN; this path-graph result does not imply the general response identity.
