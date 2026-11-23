# IV-197 — Dependency, Assumption, and Proof-Closure Audit

**Project:** Absolute Symmetry — Paper A  
**Target:** AS-ALPHA-A-PROP-0012  
**Audit scope:** Retrieved records IV-176, IV-180, IV-183, IV-186–IV-196. This is a source-limited audit; unavailable upstream records are explicitly treated as unresolved, not presumed valid.

## 1. Root equation and implicit derivative dependency

The retrieved IV-176 record states
\[
d-4=R(d,t,p),\qquad R=\frac{16tN}{dF},
\]
where
\[
N=d^2-16mt,\quad F=d^2-16t,\quad m=(2p-1)^2.
\]
At fixed \(d,t\), the angular derivative calculation is:
\[
m_p=4(2p-1),\quad
R_p=-\frac{1024t^2(2p-1)}{dF},\quad
d_p=\frac{R_p}{1-R_d}.
\]
Thus the conditional implication \(R_d\le0\Rightarrow |d_p|\le 1/252\) is arithmetically consistent with the stated \(t,d,F\) ceilings. This audit does **not** independently prove \(R_d\le0\).

The precise upstream records IV-163 and IV-175, and the complete derivation of the radial derivative/root-domain premises, were not successfully retrieved in this pass. They remain source-verification blockers.

## 2. Assumption ledger

| Premise | Retrieved support | IV-197 status |
|---|---|---|
| \(0\le t\le1/64\) | Repeated in retrieved downstream records | Inherited; original derivation not independently checked |
| \(4\le d\le256/63\) | IV-180 and downstream ceilings | Inherited; root-domain proof not verified |
| \(F=d^2-16t\ge63/4\) | IV-180 | Arithmetic compatibility follows from bounds; source proof not verified |
| \(R_d\le0\) | Required by IV-176 and IV-180 | **Open / not independently established** |
| Implicit root existence | Equation retrieved in IV-176 | **Open** |
| Root uniqueness | Needed for a well-defined branch | **Open** |
| \(d_t,d_p\) valid uniformly on intended domain | Downstream inherited bounds | **Open** |
| \(H,H_t,H_p\) ceilings | IV-180 | Arithmetic propagation checked in IV-196; upstream derivation open |
| A/G component derivative premises | IV-180, IV-186–188 | Algebra and arithmetic checked conditionally; premise validity open |
| Normalization \(D=1+tS\) | Corrected IV-190 | Structurally consistent |
| Uniform quotient derivative ceilings | IV-190–192, IV-196 | Arithmetic propagation reproduced; analytic premises remain conditional |
| Convexity of explicit \([0,1/64]\times[0,1]\) box | IV-194 | Directly verified |
| Convexity/segment validity of true implicit admissible branch | Not established | **Open** |
| Differentiability of branch throughout full domain | Not established | **Open** |
| Full global Lipschitz theorem | IV-183, IV-195 conditional statements | **Not closed** |

## 3. Circularity/dependency review

A complete circularity audit would require the exact original root equation, admissible interval, all intermediate inequalities proving \(R_d\le0\), and the source derivations of \(d_t,d_p\), \(H\), and their derivative bounds. The current downstream records refer to these premises but do not contain the entire derivation chain.

No circularity is positively identified in the retrieved records. **Absence of a detected cycle is not a proof of dependency acyclicity.** Because the upstream premise graph is incomplete, the circularity audit is classified unresolved.

## 4. Lipschitz closure status

IV-193–196 validate structural calculus/norm assembly and arithmetic propagation conditionally. IV-194 verifies convexity only of the explicit parameter box. The theorem-level inference still requires a single admissible differentiable root branch with all component derivative ceilings valid uniformly along every relevant segment.

Therefore:
- conditional segmentwise Lipschitz estimate: valid when its hypotheses hold;
- full-box implicit-branch Lipschitz claim: not established;
- global Lipschitz conclusion for PROP-0012: not closed by the retrieved evidence.

## 5. Verdict

**Dependency / proof closure: OPEN.**

The downstream arithmetic and structural calculations have substantial conditional support. However, root existence, uniqueness, the sign \(R_d\le0\), the uniform implicit-derivative premises, and admissible-branch domain coverage remain proof obligations. This audit does not declare the proposition false; it records that the proof chain is not yet closed from the evidence retrieved.

## 6. Next action

The next work item should not be another downstream Lipschitz calculation. It should be an upstream root-and-sign audit: retrieve and reconstruct the exact IV-163/IV-175 source chain, prove or refute \(R_d\le0\) on the claimed domain, establish existence/uniqueness for \(d\), and independently derive \(d_t,d_p\). Only after those premises close should the derivative bounds and Lipschitz conclusion be promoted.
