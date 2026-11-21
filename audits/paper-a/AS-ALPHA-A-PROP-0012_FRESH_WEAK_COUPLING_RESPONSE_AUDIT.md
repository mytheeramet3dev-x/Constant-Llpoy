# PROP-0012 Fresh Audit — Weak-Coupling Edge-Response Contrast

**Claim:** AS-ALPHA-A-PROP-0012  
**Frozen source:** Absolute_Sym at commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`, Section 4.4.3 and Section 5.3 / Lemma 5.2.  
**Audit scope:** Fresh consistency/algebra review of the corrected weak-coupling derivation and its analytic remainder route. The diagnostic script was inspected but not executed. This is internal review, not Lean verification or an external referee report.

## Verdict

**SOURCE-CONFLICT / ANALYTIC-PARTIAL.** The corrected leading coefficient and its sign are algebraically consistent with the displayed weak-coupling expansions, conditional on the expansions and entropy-derivative lemma. The former negative-sign supporting argument omits a leading order-\(r^2\) coherence. The manuscript's broad phrase “opposite-sign response characteristics” is not itself a precise mathematical sign statement, so its intended meaning needs clarification; the specific negative \(B-C\) assertion in the old Lemma 5.2 conflicts with the corrected local asymptotic.

## 1. Leading coefficient spot-check

Set \(r=J/h\) and \(u_{ij}\) by \(J_{ij}=J(1+u_{ij})\). The displayed first-order pair-flip amplitudes \(a_{ij}=r(1+u_{ij})/4\) give, at the uniform point:

- one-site small eigenvalue \(p=(N-1)r^2/16+O_N(r^3)\);
- shared-edge directional derivative \(\partial_{u_{13}}p_1=r^2/8+O_N(r^3)\), while the disjoint-edge derivative has no leading \(r^2\) term;
- the coherent odd pair block has leading matrix \((N-2)r^2/16\begin{pmatrix}1&1\\1&1\end{pmatrix}\), so its positive eigenvalue \(q=(N-2)r^2/8\), with \(\partial_{u_{13}}q=r^2/8+O_N(r^3)\) and \(\partial_{u_{34}}q=O_N(r^3)\).

The leading entropy derivative terms from \(p\) and \(q\) contain logarithms. Their \(r^2\ln r\) terms cancel in the mutual-information derivative, leaving the coefficient
\[
\frac{r^2}{8}\ln(q/p)
=\frac{r^2}{8}\ln\!\left(\frac{2(N-2)}{N-1}\right).
\]
Since \(2(N-2)/(N-1)>1\) for \(N\ge4\), the leading coefficient is strictly positive. Converting the dimensionless edge direction to physical coupling yields the reported \(J/(8h^2)\) factor.

This checks the displayed coefficient's algebra and sign, conditional on the perturbative block expansions.

## 2. Remainder and rank-changing branches

The conservative remainder \(O_N(r^2[1+|\ln r|])\) in physical units corresponds to \(O_N(r^3[1+|\ln r|])\) in the dimensionless edge-direction contrast after extracting the leading \(r^2\) term. This is a relative \(O_N(r[1+|\ln r|])\) correction, which tends to zero for fixed finite \(N\).

The proposed analytic nonnegative-eigenvalue entropy lemma is a plausible route for zero/rank-changing branches: if a branch is jointly real-analytic, nonnegative on a two-sided real edge neighborhood, and jointly \(O_N(r^m)\), its first directional entropy derivative at the reference point is bounded by \(O_N(r^m(1+|\ln r|))\), or vanishes when the branch is identically zero there. The argument is consistent for first directional derivatives; it does not supply higher differentiability or uniform-in-\(N\) control.

The response proof still relies on jointly analytic expansions and the claimed block orders. They were inspected as stored derivation but not independently generated from the Hamiltonian in this pass.

## 3. Numerical script review (not execution)

The diagnostic constructs the full \(2^N\)-dimensional Hamiltonian, varies \(J_{13}\) and \(J_{34}\) separately, computes two-sided central finite differences, and compares with the leading term. The method is a useful finite-\(N\) consistency diagnostic, not proof. Precision cutoff for entropy eigenvalues and finite-difference step introduce numerical sensitivity; the script must be run and outputs independently checked before claiming replication.

## 4. Source correction boundary

The old Lemma 5.2's negative sign follows an incomplete reduced block that omits the coherence \(\sum_{k\ge3}a_{1k}a_{2k}\). At the uniform point that coherence makes the leading odd block rank one, with eigenvalues \((N-2)r^2/8\) and zero, changing the leading response cancellation and sign.

Section 4.4.3's phrase “opposite-sign response characteristics” remains semantically underspecified and should not be interpreted as a rigorous claim that \(B-C<0\) without a definition. The specific negative-sign Lemma 5.2 claim, however, is contradicted by the corrected leading term for sufficiently small \(r>0\) and fixed \(N\ge4\), assuming the displayed remainder estimate.

## 5. Defensible scope

- Leading weak-coupling coefficient: **algebraically checked conditionally**.
- Sign near \(J/h=0\): **positive conditional on remainder bound**, for each fixed finite \(N\ge4\).
- Numerical data: inspected as records; script not rerun.
- Full model-specific differentiated remainder: **not independently reproduced in this audit**.
- Lean theorem for the full asymptotic: **not established**.
- Global \(B-C>0\) for arbitrary \(J/h\): **not claimed**.
- Uniform-in-\(N\) statement: **not claimed**.

**Disposition:** Keep PROP-0012 at **SOURCE-CONFLICT / NOT-VERIFIED**. Corrected weak-coupling local result is analytically promising and internally consistent, but independent recurrence/derivation reproduction, script execution, source-language reconciliation, and proof-to-Lean correspondence remain open.
