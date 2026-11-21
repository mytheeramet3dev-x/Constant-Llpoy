# IV-127 — Uniform Direct-Entropy Positivity Near Degenerate Coupling Axes

**Status:** CONDITIONAL ANALYTIC LEMMA / SCOPE CHECK REQUIRED.  
**Target:** AS-ALPHA-A-PROP-0012 remains OPEN until the proposition's original domain and probability definitions are reconciled with this note and a proof is formally/independently verified.

## 1. Key simplification: compare probabilities before entropy
From the recorded definitions,
\[
q-q_3=\frac{u^2-w^2}{D},\qquad D=1+u^2+w^2+z^2.
\]
This is a more direct route than comparing two asymptotic entropy expansions. Since binary entropy is strictly increasing on \((0,1/2)\), if we can establish
\[
0\le q_3<q<1/2
\]
then \(\Delta S=2[h(q)-h(q_3)]\) is positive, with equality on the \(A=0\) axis.

## 2. Local analytic factorization (proof obligations)
Write the dimensionless couplings as \(x=\varepsilon A\), \(y=\varepsilon B\). The eigenvector equations near the uncoupled lowest eigenvalue are
\[
(4-\delta)u-4yw=4x,\
(4-\delta)w-4yu-4xz=0,\
(4-\delta)z-4xw=4y,\
\delta=-4xu-4yz.
\]
The lowest eigenvalue is simple at \((x,y)=(0,0)\) (gap 4), so the normalized-to-first-component eigenvector coordinates are analytic in a sufficiently small neighborhood by the analytic implicit-function theorem.

By symmetry and the equations, the local analytic forms can be factored as
\[
u=xU(x,y),\quad w=xyW(x,y),\quad z=yZ(x,y),
\]
with \(U(0,0)=1\), \(W(0,0)=2\), and \(Z(0,0)=1\). The factorization is intended to encode exact axis symmetry, not just formal leading terms. **It must be proved from the equations (or verified by a complete analytic factorization argument) before treated as established.**

If these factorizations and continuity are rigorously secured, choose \(\rho>0\) so that on \(|x|,|y|\le\rho\):
\[
|U|\ge\tfrac12,\quad |W|\le3,\quad D\ge1.
\]
Shrinking \(\rho\) further so \(9y^2<1/4\), yields
\[
u^2-w^2=x^2(U^2-y^2W^2)
\ge x^2(1/4-9y^2)>0
\]
for \(x\ne0\). (For real parameters, the eigenvector coordinates are real.)

## 3. Small-probability control
Analyticity plus the fact that \(u,w,z\to0\) at the origin implies \(q,q_3\to0\). Thus choose a smaller neighborhood where
\[
0\le q_3<q<1/2.
\]
Since
\[
h'(t)=\ln\frac{1-t}{t}>0\quad(0<t<1/2),
\]
the desired sign follows there:
\[
\Delta S>0\quad(x\ne0),\qquad \Delta S=0\quad(x=0).
\]
This route would control the degenerate axes uniformly inside a small **absolute-coupling** neighborhood, rather than requiring a ratio \(B/A\) bounded away from 0 or infinity.

## 4. What is and is not established in this note
- The probability identity \(q-q_3=(u^2-w^2)/D\) follows algebraically from the recorded definitions.
- The analytic eigenvector premise is supported by the simple eigenvalue/gap at the origin.
- The proposed factorizations and quantitative neighborhood constants are not yet fully proved or certified here.
- No numerical value of \(\rho\) is claimed; no explicit bound on the analytic functions is supplied.
- This local argument does **not** cover arbitrary unbounded \(A,B\), nor any original proposition domain outside small \(|\varepsilon A|,|\varepsilon B|\).
- No Lean proof, verified constants, or completed proof of the original proposition is claimed.

## 5. Next proof obligations (IV-128)
1. Prove analytic divisibility/factorization: \(u/x\), \(w/(xy)\), and \(z/y\) extend analytically at axes.
2. Derive explicit bounds for \(U,W,Z\) over a closed neighborhood, preferably via a resolvent/implicit-equation contraction with rational constants.
3. Bound \(q,q_3\) explicitly below \(1/2\).
4. Compare these conditions with the exact domain and intended conclusion of Proposition 0012. If the proposition is broader, isolate the additional regimes rather than overclaim.

## 6. Audit conclusion
This is a promising sign-proof architecture that may remove the entropy-logarithm remainder problem in a local coupling regime by proving probability ordering first. It is a conditional lemma outline, not a theorem at present. The proposition remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
