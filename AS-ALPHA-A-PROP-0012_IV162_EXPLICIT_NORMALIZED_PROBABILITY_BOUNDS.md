# IV-162 — Explicit Bounds for Normalized Probability Factors

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PARTIAL ANALYTIC BOUNDS; not Lean-verified

## 1. Domain and inherited constants

On \(0\le t=\rho^2\le1/64\), \(p\in[0,1]\), inherit
\[
4\le d\le d_*:=256/63,\quad
F=d^2-16t\ge F_*:=63/4,\quad
1\le D\le50/49.
\]
Define \(H_*:=d_*^2+1/4\). The component numerator factors satisfy
\[
|d^2-16pt+16(1-p)t|\le H_*,
\]
\[
|d^2+16pt-16(1-p)t|\le H_*.
\]

## 2. Upper bounds for normalized probabilities

From the exact component formulas:
\[
\frac{u^2}{t}\le\frac{H_*^2}{F_*^2},\quad
\frac{z^2}{t}\le\frac{H_*^2}{F_*^2},\quad
\frac{w^2}{t}\le\frac{16}{F_*^2}.
\]
Using \(D\ge1\), it follows
\[
\boxed{0\le Q=q/t\le
2H_*^2/F_*^2+16/F_*^2<2.329765}
\]
and
\[
\boxed{0\le Q_3=q_3/(t(1-p))\le
H_*^2/F_*^2+16/F_*^2<1.197133}.
\]
At the endpoints, normalized ratios are interpreted by their continuous factored expressions.

## 3. Lower bound for Q3

From IV-161:
\[
Q_3\ge\frac{16F_*^2}{d_*^6(50/49)}>0.8639939.
\]
Thus throughout this disk, the endpoint-normalized \(Q_3\) is bounded away from zero, while the exact factor \((1-p)\) is preserved.

## 4. Spectral derivative bound (partial)

From the implicit spectral equation and previous derivative identities, a conservative bound for \(d_t\) is
\[
d_t\le\frac{16d_*^3}{(16-1/4)^2}<4.327700.
\]
This only bounds the spectral parameter's radial derivative. It does not yet bound the derivatives of normalized probability factors \(Q,Q_3\), which also involve differentiating component rational functions and \(D\).

## 5. Status and limits

Established here:
- explicit rational upper bounds for \(Q,Q_3\);
- explicit positive lower bound for \(Q_3\);
- inherited nonvanishing denominator bounds;
- conservative radial derivative upper bound for \(d\).

Not established:
- \(Q\) positive lower bound on full disk (not required for the endpoint argument);
- derivative bounds for \(Q,Q_3\) in \(t,p\);
- concrete Taylor remainder constants for \(q,q_3\);
- rigorous uniform entropy remainder constant/radius;
- Lean proof.

## 6. Next task

IV-163: derive explicit derivative bounds for \(Q,Q_3\) (including normalization \(D\)) from rational component formulas and the implicit spectral derivative estimates. Use interval arithmetic or transparent hand bounds, but do not present finite numerical interval sampling as proof.
