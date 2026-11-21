# PROP-0012 IV-10 — Odd Positive Branch and IV-9 Reconciliation

**Scope:** Fixed finite \(N\ge4\), \(r\to0^+\), local real independent edge perturbations, first directional derivatives. Reconcile the already-fetched odd-positive-branch derivations with the IV-9 even-block integration. This is a paper-level audit, not Lean verification.

## 1. Evidence re-fetched

- Odd positive branch differentiated remainder audit, blob \`9ccf431ef8315a21c89c1af20ebe4cafc1159ddd\`.
- Odd positive branch entropy contrast re-derivation, blob \`ac5937f5daaa754f0b89377bec5cde7cd97d6790\`.
- Complete entropy branch bookkeeping audit, blob \`7f14d4eae59eba6de5aa6a723a4990065069cc7f\`.
- IV-9 integrated working proof, current blob fetched during this audit.
- Pair-flip amplitude-order and entropy nonnegative-branch lemmas fetched during IV-9/IV-8 review.

## 2. Positive odd eigenbranch

The odd block has an analytic matrix expansion for fixed finite dimension,
\[
M_o(r,u)=r^2Q(u)+O_N(r^3),
\]
jointly in a local edge-parameter neighborhood. At the symmetric point the positive eigenvalue of \(Q(0)\) is simple and equals \((N-2)/8\), so the positive branch is locally analytic after factoring \(r^2\):
\[
q(r,u)=r^2Q_+(u)+O_N(r^3).
\]
The audited first edge derivatives at the uniform point are
\[
\partial_{u_{13}}q=\frac{r^2}{8}+O_N(r^3),\qquad
\partial_{u_{34}}q=O_N(r^3).
\]
Thus the positive-branch entropy derivative remainder remains
\(O_N(r^3(1+|\ln r|))\). It is not upgraded to \(O(r^4)\); its order is sufficient for the leading contrast's error scale.

## 3. Entropy-derivative check

For \(q>0\),
\[
\partial_u[-q\ln q]=-(1+\ln q)\partial_uq.
\]
Because \(q\asymp_N r^2\) locally at the reference, \(\ln q=2\ln r+O_N(1)\). Combining the positive-branch derivatives with the one-site binary entropy derivatives produces the leading logarithmic contrast; the constant chain-rule terms cancel in the contrast bookkeeping. The resulting dimensionless edge-direction contrast is
\[
\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}
+O_N(r^3(1+|\ln r|)).
\]
Converting \(u_e\) to physical coupling derivative divides by \(J\), giving
\[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\!\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right).
\]
The leading logarithm is positive for fixed \(N\ge4\), but only a local asymptotic sign is supported by this conditional remainder.

## 4. Cross-branch reconciliation with IV-9

The even-block small branch integrated in IV-9 has conditional entropy derivative
\(O_N(r^4(1+|\ln r|))\); the even-block large branch contributes \(O_N(r^4)\) after trace cancellation. Both are smaller than the positive odd-branch remainder \(O_N(r^3(1+|\ln r|))\). Hence, if the IV-9 shared-amplitude hypotheses and branch logarithmic-scale condition hold, adding the even-block contribution does not worsen the \(O_N(r^3(1+|\ln r|))\) error in the leading contrast.

The odd zero branch is not assigned a uniform \(O(r^m)\) bound on a two-sided edge neighborhood. Its first directional entropy derivative at the symmetric reference is zero by nonnegativity and an interior-minimum argument for each fixed \(r>0\), under analyticity and the exact zero-at-reference condition. No second-derivative conclusion follows.

## 5. Limits and explicit caveats

- This reconciliation assumes the definitions and block conventions in the working derivation match the frozen manuscript; frozen-source retrieval/reconciliation remains blocked.
- Analyticity, pair-flip support, edge derivative expansions, and branch-scale conditions are paper-level, fixed-\(N\) arguments. They are not machine-checked.
- The positive odd branch does not close the entire source conflict or establish a global sign.
- No Lean formalization/build was run.

**Verdict:** IV-10 PASS for positive odd-branch differentiated entropy remainder and consistency with the IV-9 even-branch order, conditional on the listed analytic hypotheses. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED; only the local weak-coupling leading asymptotic with conditional remainder is supported.
