# AS-ALPHA-A-PROP-0012 — IV-147
## Radial–Angular Entropy Analysis and Monotonicity

**Status:** ANALYTICAL RECORD; not Lean-verified; source-model reconciliation remains open.  
**Scope:** The matrix/eigenbranch model and exact component formulas recorded in IV-146. This note establishes symmetries and local asymptotics; it does **not** claim radial monotonicity or global angular extrema.

### 1. Radial–angular coordinates

Set \(x=\rho\cos\theta\), \(y=\rho\sin\theta\), \(0\le\rho<1/2\), and \(a=4x\), \(b=4y\). Then \(F=d^2-a^2-b^2=d^2-16\rho^2\). The exact components remain
\[
u=\frac{a(d^2-a^2+b^2)}{dF},\quad
w=\frac{2ab}{F},\quad
z=\frac{b(d^2+a^2-b^2)}{dF}.
\]
Here \(d\) is the ground-branch quantity and generally depends on both \(\rho\) and \(\theta\).

### 2. Exact probability functions

Define \(P=u^2+z^2\), \(R=z^2+w^2\), and \(T=u^2+w^2+z^2\). Then
\[
q(\rho,\theta)=\frac{P}{1+T},\quad
q_3(\rho,\theta)=\frac{R}{1+T},
\]
and
\[
\Delta S(\rho,\theta)=2\{h(q(\rho,\theta))-h(q_3(\rho,\theta))\}.
\]
These are exact reparameterizations, not monotonicity results.

### 3. Sign-reflection symmetry

Under \(x\mapsto-x\), the exact formulas transform \((u,w,z)\mapsto(-u,-w,z)\); under \(y\mapsto-y\), they transform \((u,w,z)\mapsto(u,-w,-z)\). The spectrum is invariant under these sign changes by diagonal basis conjugation, so the ground-branch \(d\) is unchanged. Consequently \(q,q_3\), and \(\Delta S\) are even in each coupling:
\[
\Delta S(-x,y)=\Delta S(x,y),\quad
\Delta S(x,-y)=\Delta S(x,y).
\]
In angular form, \(\Delta S(\rho,-\theta)=\Delta S(\rho,\theta)\) and \(\Delta S(\rho,\pi-\theta)=\Delta S(\rho,\theta)\).

### 4. Near-origin component/probability expansions

As \(\rho\to0\), the branch satisfies \(d=4+O(\rho^2)\), and the exact component expressions yield
\[
u=x+O(\rho^3),\quad z=y+O(\rho^3),\quad w=2xy+O(\rho^4).
\]
Thus
\[
q=\rho^2+O(\rho^4),\quad q_3=y^2+O(\rho^4)=\rho^2\sin^2\theta+O(\rho^4).
\]
These are local expansions.

### 5. Fixed-angle entropy asymptotics

For fixed \(\theta\), put \(s=\sin^2\theta\) and \(L=\ln(1/\rho^2)\). Using \(h(t)=t\ln(1/t)+t+O(t^2)\), the asymptotic expansion is
\[
\Delta S=2\rho^2\left[(1-s)L-s\ln s+(1-s)\right]+O(\rho^4L),
\]
with \(s\ln s:=0\) at \(s=0\). This is a fixed-angle expansion as \(\rho\to0^+\); uniformity over all angles is not claimed. At \(x=0\) (\(s=1\)), the exact entropy difference is zero.

### 6. Monotonicity/extrema status

No radial monotonicity, interior extremum exclusion, or global angular maximum has been proved here. Such claims require analyzing derivatives of the implicit ground-branch parameter \(d(\rho,\theta)\) and the entropy composition. The present step establishes exact symmetry reduction and local asymptotic geometry only.

No formal Lean verification, independent review, or source reconciliation is claimed.
