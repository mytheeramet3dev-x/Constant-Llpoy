# IV-158 — Endpoint-Sensitive Entropy Expansion and Uniform Remainder Analysis

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC ASYMPTOTIC RESULT; not Lean-verified

## 1. Endpoint mechanism

Binary entropy is \(h(s)=s\log(1/s)+s+O(s^2)\) as \(s\to0^+\). The derivative of the leading singular term diverges, so expanding entropy by a naive Taylor series at zero is invalid. At the \(y=0\) endpoint, \(q_3=0\) exactly; the continuous convention \(0\log0=0\) is required.

## 2. Uniformly structured probability expansions

Let \(r\to0\), \(p=\cos^2\theta\), and \(\varepsilon=1-p=\sin^2\theta\). The audited probability expansions from IV-157 can be written
\[
q=r^2\big(1+a(p)r^2+O(r^4)\big),
\]
\[
q_3=\varepsilon r^2\big(1+b(p)r^2+O(r^4)\big),
\]
where
\[
a(p)=-8p^2+8p-3,\quad b(p)=8p-3.
\]
The factor \(\varepsilon\) in \(q_3\) is essential: it preserves the exact vanishing at the endpoint \(p=1\). The coefficients are bounded polynomials on \([0,1]\).

## 3. Leading entropy-difference expansion

Using \(h(s)=s\log(1/s)+s+O(s^2)\), the leading expression is
\[
\boxed{
h(q)-h(q_3)=r^2\left[
p\log\frac1{r^2}+p+\varepsilon\log\varepsilon
\right]+O\!\left(r^4\log\frac1{r^2}\right).
}
\]
Here \(\varepsilon\log\varepsilon\) is defined as 0 at \(\varepsilon=0\). The error estimate is intended uniformly in angle for sufficiently small \(r\): probability remainders preserve the factor \(\varepsilon\) for \(q_3\), and \(\varepsilon|\log\varepsilon|\) is bounded on \([0,1]\). The remainder can be bounded by a constant times \(r^4(1+|\log r|)\) on a sufficiently small fixed radius interval, using analytic probability expansions with bounded angular coefficients and the endpoint-factorized form of \(q_3\).

## 4. Endpoint values and interpretation

- \(p=1\) (\(y=0\), \(\varepsilon=0\)): the expression reduces to \(r^2[\log(1/r^2)+1]+O(r^4\log(1/r^2))\), consistent with \(q_3=0\).
- \(p=0\) (\(x=0\)): the leading coefficient is zero, and the exact entropy difference is zero by symmetry / IV-156, not merely asymptotically.
- Interior \(0<p<1\): the term \(\varepsilon\log\varepsilon\) is finite and captures the angular endpoint dependence.

## 5. Correction to the uniformity language

IV-157's probability expansions have bounded angular coefficient functions. Entropy's naive termwise expansion involving \(\log\varepsilon\) is not uniformly regular as a coefficient derivative at \(\varepsilon=0\), but the combined expression \(\varepsilon\log\varepsilon\) is bounded and continuous. IV-158 therefore distinguishes uniform asymptotic control of the entropy difference from smoothness in angle: the former can hold with a logarithmic remainder, while the latter fails at the endpoint in the usual differentiability sense.

This record's uniform remainder statement is an analytic estimate based on factorized probability remainders and compact angular coefficients; it has not yet been formalized in Lean or independently refereed.

## 6. Numerical spot-check status

No new numerical spot-checks are claimed in this record. IV-157/IV-157A finite samples remain supporting checks only; they do not certify the uniform remainder.

## 7. Next task

IV-159 should independently test the claimed uniform remainder bound with explicit inequalities and a symbolic/numerical adversarial sweep, including angles arbitrarily close to \(p=1\), and identify what would be needed for a rigorous constant and radius.
