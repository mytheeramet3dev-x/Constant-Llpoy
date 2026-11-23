# IV-211 — Implicit Root Branch Coverage Reconciliation Audit

**Target:** AS-ALPHA-A-PROP-0012  
**Scope:** Reconcile IV-198/199/200 root-branch coverage claims with IV-210's domain/segment-coverage blockers. Independently recheck the endpoint arithmetic.  
**Status:** Conditional mathematical closure for the reconstructed equation; original-source fidelity remains OPEN.

## 1. Equation and parameter box

Use the reconstructed defining equation recorded in IV-198–200:
\[
\Phi(d;t,p)=d-4-R(d,t,p),\
R=\frac{16t(d^2-16mt)}{d(d^2-16t)},\
m=(2p-1)^2,
\]
on
\[
\mathcal B=[0,1/64]\times[0,1],\qquad
I=[4,256/63].
\]
Throughout \(I\times\mathcal B\), \(d\ge4\), \(0\le t\le1/64\), and
\[
d^2-16t\ge16-1/4=63/4>0.
\]
Thus the rational function is continuous and smooth on an open neighborhood of this compact box.

## 2. Lower-endpoint sign

At \(d=4\), direct substitution yields
\[
R(4,t,p)=\frac{4t(1-mt)}{1-t}.
\]
Since \(0\le m\le1\), \(0\le t\le1/64<1\), the numerator and denominator are nonnegative, hence
\[
\Phi(4;t,p)=-R(4,t,p)\le0.
\]
Equality occurs at \(t=0\); otherwise the sign is strict.

## 3. Upper-endpoint sign and exact arithmetic

For positive denominator and \(m\ge0\),
\[
R(d,t,p)\le\frac{16td}{d^2-16t}.
\]
The right-hand side is increasing in \(t\) for fixed \(d\) on the allowed interval. At \(d_*=256/63\) and \(t=1/64\), exact rational calculation gives
\[
\frac{16(1/64)d_*}{d_*^2-16(1/64)}
=\frac{16128}{258175}.
\]
Also \(d_*-4=4/63\). Exact subtraction:
\[
\frac4{63}-\frac{16128}{258175}
=\frac{16636}{16265025}>0.
\]
Therefore \(\Phi(256/63;t,p)>0\) uniformly in \((t,p)\in\mathcal B\).

## 4. Existence and uniqueness

Continuity in \(d\), together with the endpoint signs, gives at least one root in \(I\) by the intermediate value theorem.

IV-198's derivative sign calculation gives \(R_d\le0\) throughout the stated box (conditional on this equation and box). Hence
\[
\Phi_d=1-R_d\ge1,
\]
so \(\Phi\) is strictly increasing in \(d\) and there is at most one root in \(I\).

**Conclusion:** the reconstructed equation has exactly one root \(d(t,p)\in I\) for every parameter pair in \(\mathcal B\), conditional on the equation/box being the proposition's correct source definition.

## 5. Branch coverage, regularity, and segment validity

IV-200 applies the implicit function theorem: the denominator conditions are uniform and \(\Phi_d\ge1\), so each root has a local smooth branch. The interval uniqueness makes overlapping local branches agree. Thus the unique branch is defined across the full closed parameter box, with local smooth extension at boundary points.

The explicit box \(\mathcal B\) is convex. Any straight segment between two parameter points in \(\mathcal B\) stays inside \(\mathcal B\). Since the unique root branch is defined throughout \(\mathcal B\), the parameter segment is covered by the branch. **For this reconstructed equation, root-branch coverage and segment validity are therefore conditionally established**, not merely inferred from convexity of the box.

## 6. Reconciliation with IV-210

IV-210 correctly warned that box convexity alone does not establish convexity or coverage of an implicit admissible set. IV-211 adds the endpoint-sign/existence proof and monotonicity/uniqueness proof from IV-199 and IV-198, plus the IFT gluing argument from IV-200.

Updated status, with strict separation:

- Explicit parameter box convexity: **PASS**.
- Endpoint signs: **PASS (exact arithmetic, conditional on reconstructed equation)**.
- Root existence on \(I\) for every parameter: **PASS (conditional)**.
- Root uniqueness on \(I\) for every parameter: **PASS (conditional)**.
- Branch defined throughout \(\mathcal B\): **PASS (conditional)**.
- Segment remains in parameter box and on covered branch: **PASS (conditional)**.
- Original proposition/source fidelity of reconstructed formula and box: **OPEN**.
- Independently source-certified downstream derivative ceilings and full theorem closure: **OPEN**.

This supersedes IV-210's root-existence/branch-coverage OPEN items only at the reconstructed-formula level. It does not retroactively certify the original source definitions.

## 7. Proof-closure impact

The domain/segment obstacle is no longer the primary mathematical blocker **if** the reconstructed equation is source-correct. The remaining critical bottleneck is source-fidelity and premise certification: establish that this exact \(\Phi\), root interval, parameter box, and inherited component formulas are the ones required by PROP-0012; then independently certify downstream derivative ceilings under those premises. Do not promote conditional Lipschitz arithmetic to an unconditional proposition theorem.

## 8. Reproducibility note

Endpoint upper bound and subtraction were checked using exact rational arithmetic:
- upper bound: \(16128/258175\);
- endpoint margin: \(16636/16265025\), strictly positive.

No numerical sampling is used for the endpoint sign or branch existence argument.

## 9. Verdict

**Conditional root branch and segment coverage: CLOSED.**  
**Original-source fidelity / full PROP-0012 proof closure: OPEN.**
