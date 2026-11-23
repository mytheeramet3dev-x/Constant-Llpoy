# IV-217 — Direct 2×2 PSD-Block Eigenvalue and Entropy Directional Analysis

**Status:** CONDITIONAL PASS for exact algebra and directional entropy rules; OPEN for TFIM model-specific coefficient/remainder closure.
**Scope:** Replace fragile eigenvalue-label reasoning by exact 2×2 block formulas. Fixed finite N, real edge perturbation, interior symmetric reference.

## 1. Exact block algebra

For a Hermitian PSD block
\[
M(u)=\begin{pmatrix}a(u)&b(u)\\\overline{b(u)}&d(u)\end{pmatrix},
\quad a,d\in\mathbb R,\quad ad-|b|^2\ge0,
\]
write
\[
s=a+d,\quad \Delta=(a-d)^2+4|b|^2.
\]
The eigenvalues, without branch ambiguity, are
\[
\lambda_\pm=\frac{s\pm\sqrt{\Delta}}2,\qquad
0\le\lambda_-\le\lambda_+.
\]
The formula is exact. PSD implies \(s\ge0\), \(\Delta\ge0\), and \(\lambda_-\ge0\).

When \(\Delta>0\), the eigenvalues are distinct and differentiable. For a real direction u,
\[
\partial_u\lambda_\pm=\frac12\partial_us
\pm\frac{\partial_u\Delta}{4\sqrt\Delta},
\quad
\partial_u\Delta=2(a-d)(\partial_ua-\partial_ud)
+8\operatorname{Re}(\bar b\,\partial_ub).
\]
This formula exposes the possible singular denominator at a degeneracy; no uniform bound follows without controlling it or avoiding it via a matrix-level trace argument.

## 2. Entropy derivative for positive spectrum

For both eigenvalues positive, the block entropy is
\[
S(M)=-\sum_{\pm}\lambda_\pm\ln\lambda_\pm,
\]
and
\[
\partial_uS(M)=-\sum_\pm(1+\ln\lambda_\pm)\partial_u\lambda_\pm.
\]
At a repeated positive eigenvalue \(\lambda_+=\lambda_-=\lambda>0\), the spectral function is differentiable and
\[
\partial_uS(M)=-(1+\ln\lambda)\partial_u\operatorname{tr}M.
\]
The apparent \(1/\sqrt\Delta\) singularities in individual eigenvalue derivatives cancel in the sum. This statement follows from the smooth scalar function \(f(x)=-x\ln x\) on positive spectrum and trace functional calculus.

## 3. Zero eigenvalues at a two-sided interior reference

Fix r>0 and suppose M(u) remains PSD for u in a two-sided neighborhood of 0. If \(\lambda_-(r,0)=0\), then \(\lambda_-(r,u)\ge0\) and zero is a local minimum. When the smallest eigenvalue is differentiable along the direction, \(\partial_u\lambda_-(r,0)=0\). More robustly, for a PSD 2×2 block the determinant \(\det M\ge0\); if trace is bounded below by c>0 and det vanishes at u=0, then
\[
\lambda_-=\frac{\det M}{\lambda_+},\quad \lambda_+\ge c,
\]
and its first derivative vanishes at an interior minimum. Entropy contribution \(-\lambda_-\ln\lambda_-\) has zero first directional derivative under the differentiability/analytic opening conditions (for example \(\lambda_-=O(u^2)\) at fixed r). Do not invoke \(\ln0\).

For a one-sided parameter endpoint, this conclusion is not automatic: a branch may open linearly and entropy can have a \(u\ln u\) singularity. The edge variables here are independent real perturbations and the reference is interior, so the two-sided condition is the relevant one—provided the model parameter neighborhood actually preserves PSD, as it does for physical density matrices.

## 4. Degeneracy-safe method

For positive spectrum, calculate the block entropy derivative as a trace spectral-function derivative rather than separately bounding \(\partial_u\lambda_\pm\). This removes artificial singularity at eigenvalue collision. At a zero eigenvalue, split into:
- zero branch at the reference: use PSD interior minimum and a verified quadratic opening/directional regularity;
- strictly positive branch: use the chain rule and a bound on its derivative.

This controls branch-labeling issues but does not itself give asymptotic powers in r.

## 5. Application to the TFIM source expressions

The current weak-coupling source describes:
- odd block with a leading rank-one Gram matrix and positive branch \(q\asymp_N r^2\);
- even block with large eigenvalue separated from zero and small Schur eigenvalue claimed \(O_N(r^4)\);
- environment sums and pair-flip amplitude-order assumptions for first edge derivatives.

Exact 2×2 formulas validate the algebraic route. They do **not** independently establish:
1. environment coefficient bounds with first edge derivatives;
2. the small eigenvalue and derivative estimates \(O_N(r^4)\);
3. analyticity/differentiability of the chosen zero branch in all edge directions;
4. the full entropy remainder estimate for every block.

Those remain conditional/open.

## 6. Verdict

- **PASS:** exact eigenvalue formulas for Hermitian PSD 2×2 blocks.
- **PASS:** positive-spectrum trace entropy derivative is degeneracy-safe; individual eigenvalue derivative singularities cancel in the sum.
- **CONDITIONAL PASS:** zero eigenvalue at a two-sided interior PSD reference has zero first directional opening, when directional differentiability/analyticity is verified.
- **OPEN:** source TFIM block derivative and environment-sum bounds needed to apply these identities quantitatively.
- **NOT CLAIMED:** global \(B-C>0\), explicit weak-coupling threshold, uniform-in-N theorem, or formal Lean certificate.

## 7. Next task (IV-218)

Audit the odd block as a Gram matrix directly: establish its rank-one leading matrix, positive eigenvalue coefficient, and whether its small eigenvalue's first edge derivative can be bounded through determinant/trace without branch splitting. Then reconcile these explicit bounds with the entropy contribution and leading \(B-C\) coefficient. Record any unsupported coefficient assertion as a gap.
