# MCR-02 — Proposed Redline: C² Saddle-Node Remainder and Local Branches

- **Document ID:** CL-PA-RL-MCR-02
- **Status:** PROPOSED THEOREM REFORMULATION; PROOF REVIEW REQUIRED; NOT UPSTREAM-APPLIED
- **Affected claim:** AS-ALPHA-A-THM-0001
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source file:** `Arxiv/paper_01_section_03_revised.md`, §3.2
- **Source blob:** `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- **Correction register item:** MCR-02

## 1. Defect in the frozen statement

The source assumes only that \(\mathcal G_N\) is \(C^2\) near \(x_c\), but writes a cubic Taylor remainder \(O(|\delta x|^3)\) and a branch remainder \(O(g-g_c)\). A general \(C^2\) function only guarantees a Peano remainder \(o(|\delta x|^2)\) after its quadratic Taylor polynomial. It does not guarantee a cubic bound.

## 2. Proposed C²-level replacement

The following is a conservative replacement target. It deliberately weakens the branch remainder and keeps the result local and conditional.

**Theorem (local C² saddle-node, conditional form).** Fix \(h>0\) and define
\[
F(x,g)=g\mathcal G_N(x)-hx.
\]
Suppose \(\mathcal G_N\in C^2\) on a neighborhood of \(x_c\), and suppose
\[
F(x_c,g_c)=0,\qquad F_x(x_c,g_c)=0,
\]
with
\[
A:=F_g(x_c,g_c)=\mathcal G_N(x_c)>0,
\qquad
B:=F_{xx}(x_c,g_c)=g_c\mathcal G_N''(x_c)<0.
\]
Then, after restricting to sufficiently small neighborhoods of \(x_c\) and \(g_c\), there are exactly two local roots for \(g>g_c\) sufficiently close to \(g_c\), no local roots for \(g<g_c\) sufficiently close to \(g_c\), and one double/tangent root at \(g=g_c\). The two branches satisfy
\[
x_\pm(g)-x_c
=
\pm\sqrt{-\frac{2A}{B}}\,\sqrt{g-g_c}
+o\!\left(\sqrt{g-g_c}\right).
\]
No \(O(g-g_c)\) remainder is asserted under only \(C^2\) regularity.

## 3. Proof obligations before acceptance

A complete proof should not stop at formal Taylor balancing. It should establish:

1. Since \(F_{xx}(x_c,g_c)=B<0\) and \(F_{xx}\) is continuous, \(F(\cdot,g)\) is strictly concave in a sufficiently small fixed neighborhood for all nearby \(g\).
2. Since \(F_{x}(x_c,g_c)=0\) and \(F_{xx}(x_c,g_c)\ne0\), the implicit-function theorem applied to \(F_x(x,g)=0\) gives a unique nearby critical point \(x_m(g)\).
3. The critical value \(F(x_m(g),g)\) has leading term \(A(g-g_c)\), with a controlled smaller-order remainder. This determines the side on which the local maximum is positive.
4. The values at the two fixed neighborhood endpoints remain negative after choosing the neighborhood sufficiently small and then restricting \(g\) sufficiently close to \(g_c\). Strict concavity then gives exactly two local crossings when the maximum is positive, one tangent crossing at criticality, and no local crossing when the maximum is negative.
5. The quadratic Peano expansion at \((x_c,g_c)\), together with the branch equation, yields the stated leading square-root coefficient and only the stated \(o(\sqrt{g-g_c})\) remainder.

The proof must make the neighborhood and parameter quantifiers explicit. The phrase “exactly two local roots” must not be confused with exactly two roots globally.

## 4. Stronger alternative if the manuscript retains O(g−g_c)

If the author wants to retain
\[
x_\pm-x_c=\pm C\sqrt{g-g_c}+O(g-g_c),
\]
then the manuscript must state and prove a sufficient stronger regularity hypothesis and the associated quantitative remainder estimates (for example, locally Lipschitz second derivative with suitable uniform bounds, or a suitable \(C^3\) hypothesis). Merely changing the label from \(C^2\) to \(C^3\) without checking all mixed and branch estimates is not an adequate proof.

## 5. Model-specific limitation

This theorem is abstract and conditional. It does not show that the actual TFIM function \(\mathcal G_N\) is \(C^2\) near the proposed critical point, that a critical point exists, or that \(\mathcal G_N''(x_c)<0\). Those are separate model-specific obligations. The current manuscript itself lists the curvature condition as open; it must remain open until established.

## 6. Disposition

**PROPOSED REFORMULATION — NOT ACCEPTED.** The C²-level statement above is the conservative target, subject to a full proof audit (especially the local root-count and critical-value estimates). No source snapshot or upstream file has been changed.
