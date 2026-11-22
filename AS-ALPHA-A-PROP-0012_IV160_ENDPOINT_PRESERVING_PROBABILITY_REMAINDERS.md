# IV-160 — Explicit Probability Remainder Bounds and Endpoint-Preserving Entropy Control

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PARTIAL ANALYTIC RESULT; explicit numerical constants not yet certified; not Lean-verified

## 1. Exact endpoint-preserving structure

Let \(t=r^2\), \(p=\cos^2\theta\), and \(\varepsilon=1-p\). From the corrected component formulas:
\[
u=xA(t,p),\quad z=yB(t,p),\quad
w=\frac{32xy}{F},
\]
for rational expressions \(A,B\) involving the spectral parameter \(d(t,p)\) and \(F=d^2-16t\).

Consequently, the unnormalized probability numerators have the exact factor structure
\[
u^2=t p A^2,\quad z^2=t\varepsilon B^2,\quad
w^2=\frac{1024t^2p\varepsilon}{F^2}.
\]
With normalization \(D=1+u^2+w^2+z^2\), the exact probability identities can be written
\[
q=t\,Q(t,p),\quad q_3=t\varepsilon\,Q_3(t,p),
\]
where \(Q,Q_3\) are analytic wherever the component denominators and the ground-state branch remain regular. In particular, \(q_3\) retains the exact endpoint factor \(\varepsilon\), so it vanishes identically at \(p=1\).

## 2. Coefficient cross-check

Independent symbolic re-expansion of the corrected rational components and normalization gives
\[
q=t+(-8p^2+8p-3)t^2+2(24p^2-24p+5)t^3+O(t^4),
\]
\[
q_3=\varepsilon t+\varepsilon(8p-3)t^2
-2\varepsilon(12p^2-24p+5)t^3+O(t^4).
\]
The coefficients match IV-157. This verifies coefficient algebra but not explicit remainder constants.

## 3. Entropy endpoint inequality

For \(0\le s\le1\), define \(\phi(s)=s\log(1/s)\), with \(\phi(0)=0\). If \(q_3=t\varepsilon Q_3\), then
\[
q_3\log(1/q_3)
=t\varepsilon Q_3\left[\log(1/t)+\log(1/\varepsilon)+\log(1/Q_3)\right]
\]
for positive factors, with continuous endpoint interpretation. The factor \(\varepsilon\log(1/\varepsilon)\) is bounded on \([0,1]\) (maximum \(1/e\)), so the angular endpoint does not force an unbounded value of the entropy coefficient.

This argument requires \(Q_3\) bounded above and bounded away from zero on the chosen small-radius compact domain. The exact endpoint factorization is established; explicit lower and upper constants for \(Q_3\) have not yet been derived in this record.

## 4. Uniform remainder status

Analyticity in \((t,p)\) on a compact rectangle, together with the endpoint factorization, supports the existence of uniform probability-series remainder bounds on a sufficiently small radius interval. However, this record does not calculate explicit constants \(C\) and \(r_0\) satisfying a named inequality, nor does it complete the entropy remainder propagation with those constants.

Therefore IV-158's qualitative uniform logarithmic-remainder claim remains **plausible and structurally supported but not fully certified**. The phrase "explicit probability remainder bounds" in the task title is not a completed deliverable yet.

## 5. Audit status

- Exact endpoint factor \(q_3=t\varepsilon Q_3\): established algebraically.
- Symbolic probability coefficients through \(t^3\): rechecked and match IV-157.
- Boundedness of \(\varepsilon\log\varepsilon\): elementary, maximum \(1/e\).
- Explicit probability remainder constants: **not yet established**.
- Uniform entropy remainder constant and radius: **not yet established**.
- Lean proof: **not present**.
- Independent human review: **not present**.

## 6. Next task

IV-161 should derive a concrete small-radius interval and explicit lower/upper bounds for the normalized factors \(Q,Q_3\) and the spectral denominators. If those bounds become too crude, narrow the interval or report the theorem only with a non-explicit existence constant.
