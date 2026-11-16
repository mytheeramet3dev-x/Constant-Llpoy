# Constant Llapoy Working Formulation — Strong-Coupling Asymptotics

> Working note only. This file does not modify the Absolute Symmetry manuscript or any immutable source snapshot.

## Function asymptotic target

For fixed finite (N\ge4), the manuscript claims
[
G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right),
\qquad x\to\infty.
]

If this estimate is independently proved, then it implies
[
\lim_{x\to\infty}G_N(x)=\ln2.
]
It does not by itself imply a derivative estimate.

## Separate derivative obligation

Write
[
G_N(x)=\ln2-a_Nx^{-2}+R_N(x),
\qquad a_N=(N-1)^{-2}.
]
Then
[
G_N'(x)=2a_Nx^{-3}+R_N'(x).
]
The required derivative conclusion is conditional on proving
[
R_N'(x)=O_N\!\left(\frac{\ln x}{x^5}\right).
]
Do not obtain this by formally differentiating (R_N=O_N(\ln x/x^4)).

A sufficient proof target is a differentiated asymptotic estimate, or a symbol-class bound
[
R_N^{(k)}(x)=O_N\!\left(\frac{\ln x}{x^{4+k}}\right)
]
for the required (k). Any complex-analytic route must specify and prove its domain and uniform bound.

## Citation correction target

The cited `Lemma 5.1` currently located in the pinned source is about the response difference (B-C), not the displayed (G_N) expansion. The proof dependency for the function expansion must be located or reconstructed.

## Conditional entropy remainder tool

The entropy–Schur lemma may be used only after its hypotheses
[
\|Q\|=O(r^4),\qquad \|\partial_uQ\|=O(r^4/J)
]
are established for the full TFIM reduced pair. Analyticity of the projector alone is insufficient.

## Scope and status

- Fixed finite (N\ge4); do not imply uniformity in (N).
- Strong coupling (x=J/h\to\infty), with ferromagnetic (J>0).
- Function endpoint limit: conditional on the function expansion.
- Derivative asymptotic and derivative limit: open until separately proved.
- Global branch continuation: separate obligation.
- Claim status: NOT_VERIFIED.

## Additional logarithmic eigenvalue obligation

The entropy–Schur auxiliary lemma's derivative estimate also needs care: `lambda <= K r^4` does not upper-bound `|ln lambda|`. For each nonzero small eigenvalue branch, establish a lower bound `lambda >= c r^4` (when applicable), or a relative derivative bound such as `|partial_u lambda| <= C lambda/J`. Handle identically zero branches separately. Do not use the entropy derivative lemma until this is closed.
