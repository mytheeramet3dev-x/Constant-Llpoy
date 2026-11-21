# PROP-0012 IV-11 — Full Differentiated Entropy Contrast Closure (REOPENED)

**Scope:** Independent check of the claimed leading weak-coupling coefficient for the edge contrast, fixed finite $N\ge4$, $r=J/h\to0^+$, under the local analytic expansions currently in the working proof.
**Verdict:** REOPENED / LEADING COEFFICIENT NOT CONFIRMED. This audit found an uncancelled additive constant in the current entropy-derivative bookkeeping. The source convention and exact branch-to-contrast signs must be reconciled before accepting the coefficient.

## 1. Exact derivative identities

For the one-site binary entropy,
\[
H(p)=-p\ln p-(1-p)\ln(1-p),\qquad
H'(p)=\ln\frac{1-p}{p}.
\]
Therefore, for $p=\frac{N-1}{16}r^2+O_N(r^3)$,
\[
H'(p)=\ln\frac{16}{(N-1)r^2}+O_N(r)
\]
(the error depends on the stated precision of $p$; this audit does not assume an $O(r^2)$ error unless the expansion is sharpened). There is no standalone $-1$ constant in $H'(p)$.

For a positive reduced-state eigenvalue $q$,
\[
\frac{d}{du}[-q\ln q]=-(1+\ln q)q'.
\]
If $q=\frac{N-2}{8}r^2+O_N(r^3)$, then
\[
1+\ln q=1+\ln\frac{N-2}{8}+2\ln r+O_N(r).
\]
The explicit $+1$ is present.

## 2. Constant-term audit of the claimed contrast

The IV-10 bookkeeping says that the logarithmic terms combine and the constant chain-rule terms cancel, yielding the claimed coefficient
\[
\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}.
\]
Using the derivative identities above, the candidate combination for the one-site logarithmic contribution and the positive-branch entropy contribution, with the edge-direction coefficients reported in the working proof, instead retains an additive $+1$ inside the bracket:
\[
\frac{r^2}{8}\left[\ln\frac{2(N-2)}{N-1}+1\right]
\]
before confirming all one-site edge-direction terms and block/contrast conventions from the frozen source.

This is a discrepancy, not a replacement theorem: the source manuscript could use a different $B,C$ convention or an additional term not present in the fetched working derivation. The frozen source remains unavailable (previous fetch returned 404), so this audit cannot close that reconciliation.

## 3. What is checked vs not checked

- Checked: the scalar entropy derivative identities; absence of a $-1$ term in $H'(p)$; presence of $+1$ in $d(-q\ln q)/du$.
- Not fully checked: the complete site-1/site-2 directional derivative coefficients for both edge directions against the authoritative frozen manuscript; all entropy branches with source conventions; a corrected final coefficient.
- The conditional IV-9 even small-branch remainder and IV-10 odd positive-branch remainder do not resolve this constant-term discrepancy.
- No Lean formalization/build performed.

## 4. Required repair

1. Recover the exact source definitions for $B,C$ and the frozen Paper A sections.
2. Recompute every one-site entropy derivative for $u_{13}$ and $u_{34}$ separately, including both sites.
3. Recompute all two-site eigenbranch derivatives with explicit signs and coefficients.
4. Combine branch-by-branch in a single table and independently verify the constant and logarithmic terms.
5. Only then update the leading coefficient and its sign statement.

**Disposition:** IV-11 FAIL-TO-CLOSE / REOPENED. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED. The previously claimed coefficient $\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}$ is not accepted pending the constant-term repair.
