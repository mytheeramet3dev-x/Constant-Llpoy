# MCR-07 — Proposed Redline: Root-Set Scaling Versus Differentiable Branch Claims

- **Document ID:** CL-PA-RL-MCR-07
- **Status:** PROPOSED QUALIFICATION; ROOT-EQUATION IDENTITY EXACT UNDER DIMENSIONLESS MODEL ASSUMPTIONS
- **Affected claim:** AS-ALPHA-A-PROP-0004
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §4.2
- **Source blob:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Correction register item:** MCR-07

## 1. Issue

Along the parameter ray
\[
g=\gamma\alpha_N h,\qquad h>0,
\]
the dimensionless feedback ratio is
\[
\eta=\frac gh=\gamma\alpha_N.
\]
If the dimensionless function \(\mathcal G_N\) is independent of \(h\), the root equation is
\[
f(x;\eta)=\eta\mathcal G_N(x)-x=0,
\]
which contains no absolute field scale \(h\).

This proves invariance of the root set as a set. It does not, without a branch-selection/regularity condition, prove that an arbitrarily selected root function \(x_*(h)\) is differentiable or that its derivative is zero.

## 2. Proposed replacement statement

**Proposition — Root-set invariance along a dimensionless scaling ray.** Assume \(h>0\), \(g=\gamma\alpha_Nh\), and the exact scaling identity
\[
I_{12}(J,h)=\mathcal G_N(J/h)
\]
on the domain under consideration. Then the nontrivial fixed-point equation is
\[
x=\gamma\alpha_N\mathcal G_N(x).
\]
Consequently, for fixed \(\gamma\), \(N\), and \(\alpha_N\), the set
\[
\mathcal R_\gamma
=\{x>0:x=\gamma\alpha_N\mathcal G_N(x)\}
\]
is independent of \(h\). This is a statement about the entire root set and does not assert uniqueness or select one root.

**Corollary — Derivative of a simple selected root.** Suppose \(x_*(h)\) is a differentiable selected root on an interval of positive \(h\), and suppose
\[
f_x(x_*(h);\gamma\alpha_N)\ne0
\]
throughout that interval. Then
\[
\frac{d x_*}{dh}=0.
\]

**Proof.** Differentiate
\[
f(x_*(h);\gamma\alpha_N)=0.
\]
Since \(\gamma\alpha_N\) is constant along the ray and \(f\) has no explicit \(h\)-dependence,
\[
f_x(x_*(h);\gamma\alpha_N)\,x_*'(h)=0.
\]
The nonzero derivative hypothesis gives \(x_*'(h)=0\). \(\square\)

At a tangent/fold point where \(f_x=0\), this implicit-function argument does not apply. Root-set invariance remains valid there, but a derivative statement requires a separate branch analysis.

## 3. Required wording changes

- Make root-set invariance the primary proposition.
- Do not write \(\partial x_*/\partial h=0\) as an unconditional consequence of substitution.
- State the simple-root/differentiable-selection hypotheses for the derivative corollary.
- Explicitly exclude or separately analyze tangent points where \(f_x=0\).
- Do not infer global uniqueness or a preferred physical branch from scale covariance alone.

## 4. Verification obligations

1. Confirm the exact positive-rescaling identity and \(h>0\) domain from the Hamiltonian.
2. Confirm \(\alpha_N\) and \(\mathcal G_N\) are independent of \(h\) under the definitions used.
3. Formalize the root-set equivalence and the simple-root derivative corollary.
4. Keep the physical branch-selection prescription separate from the algebraic root-set statement.

## 5. Disposition

**PROPOSED QUALIFICATION — ELEMENTARY ROOT-SET RESULT; BRANCH DERIVATIVE CONDITIONAL.** No global uniqueness or branch-selection claim is added.

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
