# MCR-08 — Proposed Redline: Exact Picard Linear-Stability Criterion

- **Document ID:** CL-PA-RL-MCR-08
- **Status:** PROPOSED CLARIFICATION; LOCAL LINEAR CRITERION ONLY
- **Affected claim:** AS-ALPHA-A-PROP-0003
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §3.3; cross-check §5.1
- **Source blob:** `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- **Correction register item:** MCR-08

## 1. Exact scalar criterion

For the dimensionless Picard iteration
\[
x_{n+1}=T(x_n),\qquad
T(x)=\frac gh\mathcal G_N(x),\qquad h>0,
\]
let \(x_*\) be a fixed point and assume \(T\) is differentiable at \(x_*\). Define
\[
F(x,g,h)=g\mathcal G_N(x)-hx.
\]
Then
\[
T'(x_*)=\frac gh\mathcal G_N'(x_*)
=1+\frac1hF_x(x_*,g,h).
\]
The exact local linear multiplier condition is
\[
|T'(x_*)|<1
\quad\Longleftrightarrow\quad
-2h<F_x(x_*,g,h)<0.
\]

This is a local linear stability test for the scalar iteration. It is not a theorem of global convergence from arbitrary initial conditions.

## 2. Proposed replacement wording

> At a differentiable fixed point of the scalar Picard map, local linear attraction is characterized by the multiplier condition \(|T'(x_*)|<1\). In the dimensionless variable this is equivalent to \(-2h<F_x(x_*,g,h)<0\), with \(h>0\). The weaker inequality \(F_x<0\) only identifies the descending side of the fixed-point curve; it does not by itself imply contraction, because values \(F_x\le-2h\) give a multiplier of magnitude at least one. The borderline cases \(|T'(x_*)|=1\) require higher-order analysis. No global convergence conclusion follows from this derivative test alone.

For the dimensional variable \(J\) in §5.1, keep the separate convention
\[
F(J;g,h)=gI_{12}(J,h)-J,
\qquad T_J(J)=gI_{12}(J,h),
\]
so
\[
T_J'(J_*)=1+F_J(J_*),
\qquad
|T_J'(J_*)|<1
\Longleftrightarrow -2<F_J(J_*)<0.
\]
Do not mix the \(x\)-derivative criterion with the \(J\)-derivative criterion without the factor of \(h\).

## 3. Scope and limitations

- Requires a fixed point and differentiability of the scalar map at that point.
- Tests linear attraction/repulsion locally; it does not establish a basin size.
- Does not establish convergence of all iterates globally.
- At multiplier \(+1\) or \(-1\), linearization is inconclusive.
- This scalar criterion does not classify the full nonuniform edge-coupling feedback map; that requires the response-matrix eigenvalues and their own hypotheses.

## 4. Disposition

**PROPOSED CLARIFICATION — EXACT ALGEBRAIC MULTIPLIER TEST; GLOBAL DYNAMICS NOT CLAIMED.** The formula itself is elementary once the map and derivative convention are fixed; manuscript wording must preserve its local scope.

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
