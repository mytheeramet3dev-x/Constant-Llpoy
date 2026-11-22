# IV-159 — Adversarial Numerical Sweep of the Endpoint Entropy Remainder

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** NUMERICAL DIAGNOSTIC ONLY; no rigorous constant certified

## 1. Goal

Stress-test IV-158's proposed leading entropy difference
\[
L(r,p)=r^2\left[p\log(1/r^2)+p+(1-p)\log(1-p)\right],
\]
with \((1-p)\log(1-p)=0\) at \(p=1\), against direct eigenvector probabilities and exact binary entropy. This is not a proof of a uniform bound.

## 2. Method

For each radius, 2001 equally spaced angles on \([0,\pi/2]\) were tested using direct diagonalization of the 4-by-4 matrix. The residual
\[
E(r,\theta)=|[h(q)-h(q_3)]-L(r,p)|
\]
was normalized by \(r^4(1+|\log r|)\). This finite angular grid does not cover all angles or certify a supremum.

## 3. Results

| \(r\) | Maximum sampled normalized residual | Angle (rad) | Max sampled absolute residual |
|---:|---:|---:|---:|
| 0.02 | 4.87743572 | 0.05654867 | 3.83329223e-6 |
| 0.05 | 4.59979240 | 0.09738937 | 1.14872118e-4 |
| 0.10 | 4.23960441 | 0.14686946 | 1.40016543e-3 |
| 0.15 | 3.90439374 | 0.18692476 | 5.72644543e-3 |
| 0.20 | 3.57727768 | 0.21991149 | 1.49355442e-2 |

## 4. Interpretation / limitations

The sampled normalized residual stays below 4.88 on the tested grid/radii, which is consistent with an \(O(r^4(1+|\log r|))\) remainder. However:
- finite samples cannot establish uniformity;
- no analytic constant or admissible radius is certified;
- grid points may miss narrow angular behavior;
- this does not constitute a proof of IV-158's claimed remainder.

The next formal step should derive explicit probability remainder bounds with preserved \(\varepsilon=1-p\) factor, then propagate them through \(s\log s\) with a split endpoint argument.

## 5. Next

IV-160: explicit probability remainder constants and endpoint-preserving inequalities, or withdraw the uniform remainder claim if the derivation fails.
