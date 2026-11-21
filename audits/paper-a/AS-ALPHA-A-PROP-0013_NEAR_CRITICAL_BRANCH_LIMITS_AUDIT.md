# Paper A Audit — Near-critical branch limits (Section 4.4.1)

**Audit ID:** AS-ALPHA-A-PROP-0013  
**Frozen source:** Absolute_Sym Paper A, Section 4.4.1, commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`  
**Audit scope:** The near-critical limits claimed for the upper local saddle-node branch as \(\gamma\to1^+\). Algebraic/conditional review only; no Lean build or numerical run.

## Claim

For the upper local branch supplied by a nondegenerate saddle-node at \(x_c\),
\[
x_*(\gamma)\to x_c,\qquad
T'(x_*(\gamma))\to1,\qquad
F_J(x_*(\gamma))\to0
\quad(\gamma\to1^+).
\]

## Check

Along the ray \(g=\gamma\alpha_Nh\), the dimensionless parameter is \(\eta=\gamma\alpha_N\) and the scalar map is
\[
T_\gamma(x)=\gamma\alpha_N\mathcal G_N(x).
\]
At the tangent point, \(\alpha_N\mathcal G_N'(x_c)=1\). The local saddle-node theorem supplies the upper local solution branch with \(x_*(\gamma)\to x_c\), provided its regularity and nondegeneracy hypotheses hold and the branch is selected locally.

By continuity of \(\mathcal G_N'\) at \(x_c\),
\[
T_\gamma'(x_*)=\gamma\alpha_N\mathcal G_N'(x_*)\to
\alpha_N\mathcal G_N'(x_c)=1.
\]
Since \(F_J=T'-1\) at a fixed point in the dimensionless coordinate,
\[
F_J(x_*)=\gamma\alpha_N\mathcal G_N'(x_*)-1\to0.
\]

The conclusion is valid conditional on the existence of the local upper branch and continuity of the derivative. It is not a global continuation result and does not establish branch existence for all \(\gamma>1\), uniqueness, absence of branch exchange, or a thermodynamic transition.

## Verdict

**ANALYTIC-VERIFIED (conditional local limit).** The three limits follow from the local saddle-node branch and the tangent identity. No separate model-specific numerical evidence is needed for this conditional implication. No Lean declaration or build was checked for this claim.

## Proof obligations / caveats

- The local saddle-node hypotheses and upper-branch selection must be valid.
- The tangent identity \(\alpha_N\mathcal G_N'(x_c)=1\) must hold.
- Continuity of \(\mathcal G_N'\) at \(x_c\) is required.
- Do not use this result to assert global branch continuation.
