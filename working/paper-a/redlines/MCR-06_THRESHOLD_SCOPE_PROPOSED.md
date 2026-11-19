# MCR-06 — Proposed Redline: Conditional Threshold and Global Root Claims

- **Document ID:** CL-PA-RL-MCR-06
- **Status:** PROPOSED STATEMENT RESTRUCTURING; GLOBAL SHAPE HYPOTHESES NOT ESTABLISHED
- **Affected claims:** AS-ALPHA-A-PROP-0001 and AS-ALPHA-A-PROP-0008
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §2.5
- **Source blob:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Correction register items:** MCR-06 and related duplicate cleanup MCR-12

## 1. Issue

The definition
\[
\alpha_N=\inf_{x>0}\frac{x}{\mathcal G_N(x)}
\]
supports a pointwise subcritical exclusion, provided \(\mathcal G_N(x)>0\) on the stated domain. It does not, by itself, prove that the infimum is attained, that a tangent point exists, that roots exist for every supercritical parameter, or that there are exactly two roots.

The source must separate these logically different conclusions.

## 2. Proposed replacement structure

Assume throughout this subsection that \(\mathcal G_N:(0,\infty)\to(0,\infty)\) is defined and set
\[
q_N(x)=\frac{x}{\mathcal G_N(x)},
\qquad
\alpha_N=\inf_{x>0}q_N(x),
\qquad
f(x;\eta)=\eta\mathcal G_N(x)-x.
\]
Then the exact identity is
\[
f(x;\eta)=\mathcal G_N(x)(\eta-q_N(x)).
\]

### Proposition A — Subcritical exclusion

For every \(\eta<\alpha_N\),
\[
f(x;\eta)<0\qquad\text{for every }x>0.
\]

**Proof.** By the definition of infimum, \(q_N(x)\ge\alpha_N>\eta\) for all \(x>0\). Since \(\mathcal G_N(x)>0\), the identity above gives \(f(x;\eta)<0\). \(\square\)

This is a pointwise statement. It does not require attainment of the infimum.

### Proposition B — Tangency if the infimum is attained in the interior

Suppose there exists \(x_c\in(0,\infty)\) such that
\[
q_N(x_c)=\alpha_N,
\]
and suppose \(q_N\) is differentiable at \(x_c\). Then \(x_c\) is a global minimizer and hence
\[
q_N'(x_c)=0.
\]
Equivalently,
\[
\mathcal G_N(x_c)=x_c\mathcal G_N'(x_c),
\]
and
\[
f(x_c;\alpha_N)=0,
\qquad
\partial_x f(x_c;\alpha_N)=0.
\]
If \(\mathcal G_N\) is twice differentiable and \(q_N''(x_c)>0\), the minimum is nondegenerate. This last condition is an additional hypothesis, not a consequence of attainment alone.

### Proposition C — A sufficient condition for at least one supercritical root

Suppose, in addition, that \(q_N\) is continuous on \((0,\infty)\) and
\[
\lim_{x\to\infty}q_N(x)=+\infty.
\]
Then for every \(\eta>\alpha_N\), there exists at least one \(x_\eta>0\) such that
\[
f(x_\eta;\eta)=0.
\]

**Reason.** Since \(\eta>\inf q_N\), there is some \(x_0>0\) with \(q_N(x_0)<\eta\), so \(f(x_0;\eta)>0\). The endpoint condition gives an \(x_1>x_0\) with \(q_N(x_1)>\eta\), so \(f(x_1;\eta)<0\). Continuity and the intermediate value theorem yield a root between \(x_0\) and \(x_1\).

This proves existence of at least one root under the additional endpoint and continuity hypotheses. It does not prove exactly two roots.

### Global root count

An assertion of exactly two roots requires further global shape information about \(q_N\), such as a proved single-minimum/unimodality property together with suitable endpoint behavior and strict monotonicity on either side. A local condition \(q_N''(x_c)>0\) proves only local nondegeneracy; it does not rule out additional extrema or roots elsewhere.

## 3. Critical scaling statement

If the infimum is attained at an interior point, then the dimensionless threshold parameter is \(\eta_c=\alpha_N\). Since \(\eta=g/h\), for \(h>0\),
\[
g_c(h)=\alpha_N h.
\]
If the infimum is not known to be attained, \(\alpha_N\) remains an infimum-defined threshold value, but no critical fixed point or tangent solution at \(x_c\) may be asserted.

## 4. Required manuscript edits

1. Separate the subcritical exclusion from the attainment/tangency statement.
2. State positivity and domain assumptions for \(\mathcal G_N\) before dividing by it.
3. Call \(\alpha_N\) an infimum-defined threshold coefficient unless attainment is proved.
4. State the interior-attainment and differentiability assumptions wherever \(x_c\) or tangent equations are used.
5. Move supercritical root existence to a separate conditional proposition with explicit continuity and endpoint hypotheses.
6. Remove any claim of exactly two global roots unless a global shape theorem is proved.
7. Preserve PROP-0008 as an audit trace but merge its repeated subcritical result into PROP-0001 or mark it as a corollary, without presenting it as an independent theorem.

## 5. Verification obligations

- **Algebraic subcritical exclusion:** elementary and suitable for direct Lean formalization once definitions/domains are fixed.
- **Attainment/tangency:** requires an actual minimizer existence result and differentiability; neither follows from the infimum definition alone.
- **Supercritical existence:** requires the stated continuity and endpoint limit, which must be established for the actual \(\mathcal G_N\).
- **Exactly-two-root statement:** remains open until a global shape/monotonicity theorem is supplied.
- **Model-specific status:** no claim is made here that the TFIM function satisfies all additional hypotheses.

## 6. Disposition

**PROPOSED CONDITIONAL RESTRUCTURING — NOT ACCEPTED.** The pointwise subcritical implication and the conditional calculus statements are separated. Model-specific attainment, endpoint, and global shape obligations remain open.

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
