# PROP-0012 IV-12 — Site-by-Site and Branch-by-Branch Derivative Reconstruction

**Scope:** Reconstruct the weak-coupling directional derivative of $I_{12}=S_1+S_2-S_{12}$ from the current working expansions, fixed finite $N\ge4$, $r=J/h\to0^+$, at the uniform coupling point.
**Status:** ANALYTIC-PARTIAL / CORRECTED CANDIDATE COEFFICIENT. The frozen manuscript source remains unavailable and this is not Lean-verified.

## 1. Directional convention

$J_e=J(1+u_e)$ at the uniform point, so
$\partial_{J_e}=J^{-1}\partial_{u_e}$.
Define $\mathcal D=\partial_{u_{13}}-\partial_{u_{34}}$. The target is
$B-C=J^{-1}\mathcal D I_{12}$, with $I_{12}=S_1+S_2-S_{12}$.

## 2. One-site terms

Use $p_i=(N-1)r^2/16+O_N(r^3)$ and
$H'(p)=\ln((1-p)/p)$ (there is no standalone $-1$).
From the current edge-derivative ledger:
$\partial_{u_{13}}p_1=r^2/8+O_N(r^3)$;
$\partial_{u_{34}}p_1=O_N(r^3)$; both derivatives of $p_2$ are $O_N(r^3)$.
Consequently,
\[
\mathcal D(S_1+S_2)=\frac{r^2}{8}\ln\frac{16}{(N-1)r^2}+O_N(r^3|\ln r|).
\]
The displayed errors are conservative for the current expansions.

## 3. Two-site positive branch

For $q=(N-2)r^2/8+O_N(r^3)$,
$\partial_{u_{13}}q=r^2/8+O_N(r^3)$ and
$\partial_{u_{34}}q=O_N(r^3)$. Since
$\partial_u(-q\ln q)=-(1+\ln q)q'$,
\[
\mathcal D[-q\ln q]=-\frac{r^2}{8}\left[1+\ln\frac{(N-2)r^2}{8}\right]+O_N(r^3|\ln r|).
\]
The explicit additive $+1$ survives in this branch derivative.

## 4. Other branches

- Odd zero branch: directional entropy derivative is zero at the reference, conditional on the analytic nonnegative eigenvalue attaining its interior minimum exactly at zero.
- Even small branch: $O_N(r^4(1+|\ln r|))$, conditional on IV-9 shared-amplitude hypotheses and branch log-scale control.
- Even large branch: $O_N(r^4)$ conditional on the trace derivative cancellation.
These are below the leading $r^2$ order and cannot cancel its additive constant.

## 5. Combined candidate

Subtracting $\mathcal D S_{12}$ from the one-site contribution yields
\[
\mathcal D I_{12}=\frac{r^2}{8}\left[1+\ln\frac{2(N-2)}{N-1}\right]+O_N(r^3|\ln r|).
\]
Thus the current working expansions support the corrected candidate
\[
B-C=\frac{J}{8h^2}\left[1+\ln\frac{2(N-2)}{N-1}\right]+O_N\left(\frac{J^2}{h^3}|\ln(J/h)|\right).
\]
For $N\ge4$, the bracket is strictly positive. This is a local weak-coupling sign statement only, provided all branch/edge expansions and source conventions match.

## 6. IV-11 discrepancy resolved within current ledger; source reconciliation still open

The previous IV-10 formula omitted the $+1$. IV-11 flagged it; IV-12 independently recomputed the one-site and positive-branch terms and finds it remains after their combination. No other current branch has an $r^2$ contribution capable of cancelling it. This corrects the working candidate coefficient, but does not certify the frozen manuscript's $B,C$ definitions or exact reduced-block conventions.

## 7. Limitations / remaining obligations

- Frozen Paper A source retrieval returned 404 in the previous audit; definitions/signs and conventions cannot be reconciled here.
- The pair-flip amplitude-order and joint derivative expansions remain analytic hypotheses/lemmas requiring full proof and source matching.
- No Lean formalization or build performed.
- No global-in-coupling positivity is established.

**Verdict:** IV-12 PASS for reconstruction from the currently fetched working ledger; PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
