# IV-164 — Normalized Component and Normalization Derivative Bounds

## Scope and status
Analytic bounds on the normalized component amplitudes and normalization factor over
\(0\le t\le 1/64\), \(0\le p\le1\). This note is a derivation preparation;
it does not certify derivative bounds for \(Q\) or \(Q_3\).

Use the prior domain bounds \(4\le d\le d_*=256/63\), \(F=d^2-16t\ge F_*=63/4\), and the previously derived conservative bound \(|d_t|\le L_t=7.455139\), \(|d_p|\le L_p=0.003968254\). These numerical bounds are rounded upward.

## Regularized components
Define
\[
U=\frac{u}{\sqrt t}=\frac{4\sqrt p\,A}{dF},\quad
Z=\frac{z}{\sqrt t}=\frac{4\sqrt{1-p}\,G}{dF},\quad
W=\frac{w}{\sqrt t}=\frac{32\sqrt{p(1-p)}}{F},
\]
where \(A=d^2+16t(1-2p)\), \(G=d^2+16t(2p-1)\).
The square-root factors are not differentiable at angular endpoints in p; for endpoint derivative work, use squared components or a different angular coordinate. This note only uses amplitude bounds and interior derivative preparation.

Set \(M=d_*^2+1/4\). Then \(|A|,|G|\le M\), \(dF\ge 63\), and \(F\ge63/4\). Therefore
\[
|U|,|Z|\le \frac{4M}{63},\qquad
|W|\le\frac{32}{F_*}\frac12=\frac{64}{63}.
\]
These are conservative.

## Normalization
\[
D=1+t(U^2+Z^2+W^2).
\]
Hence
\[
1\le D\le 1+\frac1{64}\left(2(4M/63)^2+(64/63)^2\right).
\]
This bound is a direct consequence of the regularized component bounds and is independent of angular endpoint issues.

## Derivative status
Interior derivatives of \(U,Z,W\) require controlling \(d_t,d_p,A_t,A_p,G_t,G_p,F_t,F_p\), as well as the p-derivatives of \(\sqrt p\) and \(\sqrt{1-p}\). Those latter terms blow up in this coordinate at endpoints, so a uniform \(p\)-derivative bound on amplitudes cannot be claimed on the closed interval.

A viable endpoint-regular approach is to differentiate the squared components \(u^2/t,z^2/t,w^2/t\) directly, or switch to \(p=\cos^2\theta\) and derive bounds in \(\theta\). No complete derivative bounds for \(D\), \(Q\), or \(Q_3\) are asserted here.

## Conclusion
IV-164 provides regularized amplitude and normalization bounds, and identifies the correct endpoint-aware derivative route. It is partial analytic progress only; no entropy Taylor remainder certification is completed.
