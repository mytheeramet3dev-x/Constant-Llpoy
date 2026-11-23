# IV-210 — Domain and Segment Coverage Reconciliation Audit

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PASS for explicit-box convexity and conditional pathwise implication; OPEN for implicit admissible-branch coverage.

## 1. Records cross-checked
- IV-194: explicit parameter box and implicit-branch admissibility distinction.
- IV-183: conditional Lipschitz theorem via line-segment FTC; corrected older rounding ceilings.
- IV-208/209: current conditional component and Jacobian ceilings.

## 2. Explicit parameter box
The stated box is
\[
\mathcal B=[0,1/64]\times[0,1]
\]
in \((t,p)\). It is convex: for any two points in the box and \(\lambda\in[0,1]\), their coordinatewise convex combination remains within the same closed intervals. Thus straight parameter segments remain inside \(\mathcal B\). **This elementary geometric statement is verified.**

## 3. The implicit admissible domain is a separate set
The relevant domain for \(Q\) is not merely \(\mathcal B\), but the subset where the implicit solution \(d(t,p)\) is defined, selected, and satisfies all required conditions. Denote it \(\mathcal D_{\mathrm{adm}}\).

IV-194 explicitly does not establish:
- existence of the required root for every point of the box;
- uniqueness of the selected root throughout the box;
- coverage of one smooth branch on the entire box;
- pointwise validity along every segment of the inherited root/domain bounds and sign assumptions.

Therefore convexity of \(\mathcal B\) does not imply convexity or segment coverage of \(\mathcal D_{\mathrm{adm}}\). Two admissible endpoints alone are insufficient to use the straight-line FTC argument if the branch/domain fails at an intermediate point.

## 4. Conditional Lipschitz implication
If a segment \(\gamma(\lambda)\) between \(x,y\) lies wholly in a domain where \(Q\) is continuously differentiable and the current derivative ceilings apply at every point, then:
\[
\|Q(y)-Q(x)\|_2\le
M_t|t_y-t_x|+M_p|p_y-p_x|,
\]
where IV-209 provides the conditional ceilings \(M_t=24.940207179\), \(M_p=3.322153311\).

For Euclidean input distance, the Frobenius/operator ceiling gives the conditional bound:
\[
\|Q(y)-Q(x)\|_2\le25.160497545\,\|y-x\|_2,
\]
provided the entire connecting segment is in the valid differentiable domain and all upstream assumptions hold there.

If the admissible branch domain is nonconvex, the straight segment statement is not automatically available. A pathwise estimate may be possible along an admissible piecewise-smooth path, but it requires path existence and length/coordinate-variation control; this audit does not assert those.

## 5. Coverage matrix
| Obligation | Result |
|---|---|
| Explicit box convexity | PASS |
| Segment stays in explicit box | PASS |
| Implicit root exists at all box points | OPEN |
| Unique root/branch across box | OPEN |
| Implicit admissible set convex | OPEN |
| All derivative ceilings hold pointwise on connecting segment | OPEN |
| Global Lipschitz on full claimed domain | OPEN |
| Conditional segmentwise Lipschitz implication | PASS |

## 6. Verdict
IV-210 closes the explicit-box geometry but does not close the implicit branch coverage. The numerical Jacobian ceiling is available for conditional segmentwise use only. Do not report a full-domain/global Lipschitz theorem unless the root/domain, smooth branch, and pointwise derivative hypotheses are established on every relevant segment or a valid pathwise substitute is proved.
