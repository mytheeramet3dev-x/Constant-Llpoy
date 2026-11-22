# IV-167 — Entropy Chain Rule and Endpoint Singularity Analysis

## Exact parametrization
Using the conditional IV-166 representation, set
\[
q=tQ(t,p),\qquad q_3=t(1-p)Q_3(t,p).
\]
The entropy difference is
\[
\Delta S=2[h(q)-h(q_3)],\quad h(s)=-s\ln s-(1-s)\ln(1-s).
\]
For \(0<s<1\),
\[
h'(s)=\ln\frac{1-s}{s}.
\]
Thus, wherever differentiability and domain conditions hold,
\[
\Delta S_t=2\left[h'(q)(Q+tQ_t)-h'(q_3)((1-p)(Q_3+t(Q_3)_t))\right],
\]
and
\[
\Delta S_p=2\left[h'(q)tQ_p-h'(q_3)t(-Q_3+(1-p)(Q_3)_p)\right].
\]
These are exact chain-rule identities, not numerical estimates.

## Endpoint behavior
As \(s\downarrow0\), \(h'(s)=\ln((1-s)/s)\) diverges logarithmically. Consequently, finite uniform first-derivative bounds on \(\Delta S\) across \(t=0\) cannot be obtained by simply bounding \(h'\) separately. The logarithmic terms must be isolated and canceled/organized in the asymptotic expression, with the remaining analytic part bounded.

The angular endpoint \(p=1\) also requires care for \(q_3\), since its prefactor \(1-p\) vanishes. The exact chain-rule expression is interpreted by limits where needed; no uniform entropy derivative claim is made here.

## Status
IV-167 establishes the exact derivative identities and flags the logarithmic endpoint obstruction. It does not provide a finite derivative bound or a Taylor remainder certificate. IV-166 estimates are inherited and still conditional pending audit.
