# Paper A Audit — Strong-coupling branch limits (Section 4.4.2)

**Audit ID:** AS-ALPHA-A-PROP-0014  
**Frozen source:** Paper A Section 4.4.2, source commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`  
**Audit scope:** Algebraic implications of strong-coupling asymptotics for the upper/selected branch. No numerical diagnostics or Lean build run in this pass.

## Claim

For the branch satisfying
\[
x_*(\gamma)=\gamma\alpha_N\mathcal G_N(x_*(\gamma)),
\]
and with fixed finite \(N\ge4\), the manuscript claims
\[
x_*(\gamma)\to\infty,\quad T'(x_*)\to0,\quad F_J(x_*)\to-1
\quad(\gamma\to\infty).
\]

## Conditional algebraic verification

Assume the strong-coupling limit
\[
\mathcal G_N(x)\to L=\ln2>0
\]
and that the selected branch remains in a domain bounded away from zero (e.g. \(x_*\ge x_c>0\)). The fixed-point identity then gives
\[
\frac{x_*}{\gamma}=\alpha_N\mathcal G_N(x_*).
\]
Because \(\mathcal G_N\to L>0\), the right side is bounded away from zero along sufficiently large \(x_*\); bounded \(x_*\) on the selected positive branch cannot satisfy the equation as \(\gamma\to\infty\). Thus \(x_*\to\infty\), and more sharply,
\[
x_*(\gamma)\sim \gamma\alpha_N\ln2.
\]

If the derivative asymptotic is independently valid,
\[
\mathcal G_N'(x)=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right),
\]
then
\[
T'(x_*)=\gamma\alpha_N\mathcal G_N'(x_*)
=O(\gamma/x_*^3)=O(\gamma^{-2})\to0.
\]
At the fixed point \(F_J=T'-1\), hence
\[
F_J(x_*)\to-1.
\]
These limit implications are algebraically correct under the stated asymptotic and branch assumptions.

## Important limitations / gaps

- The fixed-point identity alone does not select or guarantee a global upper/physical branch. A global continuation/no-branch-exchange assumption or a precise branch-selection rule is required.
- The manuscript's strong-coupling expansion for \(\mathcal G_N\) and especially its differentiated entropy remainder are not independently rederived in this audit. PROP-0009 has a prior fixed-\(N\) asymptotic follow-up review, but remains partial and does not constitute a fresh complete proof of the entropy asymptotics here.
- Lemma 5.1 citation mismatch is unresolved; this audit does not validate the perturbative derivation behind the expansions.
- No Lean theorem or build was checked.
- Fixed finite \(N\) only; no interchange of \(N\to\infty\) and \(\gamma\to\infty\) is established.

## Verdict

**ANALYTIC-PARTIAL — conditional asymptotic implications verified; source asymptotics and branch-selection prerequisites remain open.** Do not label the full strong-coupling claim verified until the expansion, derivative control, and branch assumptions are independently closed.
