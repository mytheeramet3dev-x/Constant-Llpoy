# IV-31 — Leading-Coefficient Independent Reconstruction Audit

**Target:** AS-ALPHA-A-PROP-0012, candidate leading weak-coupling coefficient for \(B-C\)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Independently reconstruct the leading coefficient from the leading one-site and two-site entropy branches stated in the working derivation; check constants, logarithm arguments, signs, and edge dependence. This is an algebraic leading-order audit, not a complete proof of all remainders.

## 1. Definitions and parameter conversion

The working derivation uses independent dimensionless edge variables \(u_e\) with \(J_e=J(1+u_e)\), \(r=J/h\). For derivatives with respect to physical edge couplings, at the uniform point
\[
\partial_{J_e}=J^{-1}\partial_{u_e}.
\]
The target is \(B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}\), where \(I_{12}=S(\rho_1)+S(\rho_2)-S(\rho_{12})\).

## 2. Leading branches

The one-site small eigenvalue at the uniform point is
\[
p=\frac{N-1}{16}r^2+O_N(r^3).
\]
Its leading edge-13 derivative is \(\partial_{u_{13}}p_1=r^2/8+O_N(r^3)\), while edge 34 has no leading direct contribution to either site 1 or 2.

The positive odd-block small eigenvalue is
\[
q=\frac{N-2}{8}r^2+O_N(r^3),
\]
with \(\partial_{u_{13}}q=r^2/8+O_N(r^3)\) and no leading \(u_{34}\) contribution.

For \(x=cr^2+O(r^3)\), with a derivative \(x_u=dr^2/8+O(r^3)\), binary/small-branch entropy gives
\[
\partial_u[-x\ln x-(1-x)\ln(1-x)]
=-\frac{dr^2}{8}\ln(cr^2)+O_N(r^2)+O_N(r^3|\ln r|),
\]
where the \(O(r^2)\) term includes the \(+1\) and regular derivative terms. In the difference between one-site and two-site entropy derivatives, those common \(+1\) terms cancel.

## 3. Leading mutual-information derivative

At leading logarithmic order,
\[
\partial_{u_{13}}I_{12}
=\frac{r^2}{8}\ln\frac{q}{p}+O_N(r^2)+O_N(r^3|\ln r|),
\]
and
\[
\partial_{u_{34}}I_{12}=O_N(r^2)+O_N(r^3|\ln r|),
\]
provided the previously audited branch/remainder controls apply. The leading logarithmic coefficient in the difference is therefore
\[
\frac{r^2}{8}\ln\frac{(N-2)/8}{(N-1)/16}
=\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}.
\]
Converting to physical edge derivatives yields the candidate
\[
\boxed{
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\left(\frac{J^2}{h^3}|\ln(J/h)|\right)
}
\]
**if** the physical derivatives are defined as \(\partial_{J_e}\) and the leading entropy/remainder bookkeeping closes as assumed.

## 4. Comparison with the prior candidate

The previously recorded candidate had an extra additive \(+1\) inside the bracket:
\[
\frac{J}{8h^2}\left[1+\ln\frac{2(N-2)}{N-1}\right].
\]
IV-31 finds that this \(+1\) does not arise from the leading binary entropy derivatives shown here: the entropy derivative contributes \(-\ln x-1\), but the regular \(-1\) terms cancel between the one-site and positive two-site branch when their edge derivatives have the same leading \(r^2/8\). The coefficient requires independent correction/reconciliation against the original definition and full block eigenvalue bookkeeping.

## 5. Scope and limitations

- The logarithmic leading coefficient is reconstructed from the displayed leading branches only.
- The regular \(O(r^2)\) terms are not independently fully computed; their cancellation is stated only for the common derivative piece.
- Higher/zero branches and all uniform remainder bounds remain open.
- No Lean formalization/build.
- No counterexample to the exact proposition established.

## 6. Disposition

**Finding:** The leading logarithmic coefficient from the currently displayed one-site/odd-block terms is \(\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}\), not the prior candidate with an extra \(+1\). This is a material coefficient-reconciliation issue. Do not treat either candidate as theorem until full entropy derivative bookkeeping is independently closed.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 7. Next

IV-32: **Exact Edge-Direction Entropy Bookkeeping Audit** — reconstruct both edge directional derivatives term by term across the one-site, even, and odd blocks, including trace/normalization contributions and the cancellation (or noncancellation) of regular \(+1\) terms. Resolve the IV-31 coefficient discrepancy without assuming the proposed coefficient.
