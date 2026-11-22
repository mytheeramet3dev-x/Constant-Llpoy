# Paper A — IV-168: Logarithmic Separation and Regularized Entropy Remainder

## Status
Exact analytic identity plus uniform remainder bounds. This step does not certify the derivative estimates inherited from IV-165/166, and it is not a full proof of Proposition AS-ALPHA-A-PROP-0012.

## 1. Exact entropy decomposition
For \(0\le s<1\), define
\[
h(s)=-s\log s-(1-s)\log(1-s),\qquad
g(s)=-(1-s)\log(1-s)-s.
\]
Then, for \(s>0\),
\[
\boxed{h(s)=s\log(1/s)+s+g(s).}
\]
The identity extends continuously to \(s=0\) by setting \(s\log(1/s)=0\), \(g(0)=0\).

## 2. Integral representation and uniform bounds
Direct differentiation gives
\[
g'(s)=\log(1-s),\qquad g''(s)=-\frac1{1-s}.
\]
Integrating twice from zero,
\[
g(s)=-\int_0^s\frac{s-r}{1-r}\,dr.
\]
Consequently, for every \(0\le s\le 1/2\),
\[
\boxed{-s^2\le g(s)\le -\frac{s^2}{2}},\qquad
|g'(s)|=-\log(1-s)\le 2s,\quad |g''(s)|\le2.
\]
The bounds follow since \(1\le(1-r)^{-1}\le2\) on this interval. In particular, \(g\) is a regular analytic remainder with no logarithmic singularity at zero.

## 3. Apply to the normalized probabilities
On the IV-161 domain, the established spectral argument gives \(0\le q,q_3<1/2\), with
\[
q=tQ,\qquad q_3=t\varepsilon Q_3,\quad \varepsilon=1-p.
\]
Where the arguments are positive, substitution yields the exact identity
\[
\begin{aligned}
h(q)-h(q_3)
={}&t(Q-\varepsilon Q_3)\log(1/t)\\
&+t\{Q\log(1/Q)-\varepsilon Q_3\log(1/(\varepsilon Q_3))
+Q-\varepsilon Q_3\}\\
&+g(tQ)-g(t\varepsilon Q_3).
\end{aligned}
\]
Terms of the form \(a\log(1/a)\) are assigned their continuous value zero at \(a=0\). Thus the formula extends to probability endpoints whenever the normalized factors have finite continuous limits.

## 4. Regularized remainder control
Because \(q,q_3\le1/2\), the previous bounds give
\[
-q^2\le g(q)\le -q^2/2,\qquad
-q_3^2\le g(q_3)\le -q_3^2/2.
\]
Hence a conservative absolute estimate is
\[
|g(q)-g(q_3)|\le q^2+q_3^2
=t^2\{Q^2+\varepsilon^2Q_3^2\}.
\]
The bound is valid but not sharp; it is sufficient to isolate the entropy logarithms without differentiating the singular \(s\log s\) term.

## 5. What is and is not concluded
- The entropy logarithmic singularity has been isolated exactly in the terms displayed in Section 3.
- The residual \(g\) is analytic on \([0,1/2]\) and has a quadratic-size bound.
- This step does **not** establish a uniform derivative bound for the full entropy at zero.
- This step does **not** verify the inherited IV-165/166 constants or prove the remaining Taylor estimates needed for Proposition 0012.

## Repository record
This note is intended as an auditable analytic step (not a Lean-certified result).