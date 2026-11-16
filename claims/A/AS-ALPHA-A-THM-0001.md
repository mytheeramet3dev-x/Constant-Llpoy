# AS-ALPHA-A-THM-0001 — Conditional local saddle-node normal form

- **Claim ID:** `AS-ALPHA-A-THM-0001`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Mathematical verification status:** NOT_ASSESSED
- **Original source label:** See verbatim source excerpt
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_03_revised.md`
- **Source blob SHA:** `9ac164ac67cc121af212c4fb7268b809d9234bd6`
- **Source line range:** 96-165
- **Source revision date:** 2026-11-14T13:40:34Z
- **Claim-specific Verification Obligation Matrix:** Pending population after extraction review

## Verbatim source excerpt

The following is copied from the source revision above. It is not a rewritten theorem statement.

```markdown
## 3.2 Local normal form

Assume that \(\mathcal G_N\) is at least \(C^2\) near \(x_c\). Let

\[
\delta x=x-x_c,
\qquad
\delta g=g-g_c.
\]

Taylor expansion at fixed \(h\) gives

\[
F(x,g,h)
=F_c+F_g\delta g+F_x\delta x
+\frac12F_{xx}\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

At the critical point,

\[
F_c=0,
\qquad F_x=0,
\qquad F_g=\mathcal G_N(x_c)>0,
\qquad F_{xx}=g_c\mathcal G_N''(x_c).
\]

Therefore,

\[
F(x,g,h)
=\mathcal G_N(x_c)\delta g
+\frac12g_c\mathcal G_N''(x_c)\delta x^2
+O(\delta g^2+|\delta g\delta x|+|\delta x|^3).
\]

### Assumption 1 — Generic nondegeneracy

Assume

\[
\mathcal G_N''(x_c)\neq0.
\]

If \(x_c\) is an interior minimizer of \(x/\mathcal G_N(x)\), then

\[
\mathcal G_N''(x_c)<0
\]

is equivalent to strict nondegeneracy of that minimum

Solving the leading normal form gives

\[
\boxed{
x_\pm-x_c
=\pm
\sqrt{
\frac{2\mathcal G_N(x_c)}{g_c|\mathcal G_N''(x_c)|}
}
\sqrt{g-g_c}
+O(g-g_c)
}
\]

on the side \(g>g_c\) when \(\mathcal G_N''(x_c)<0\)

This is a **local conditional saddle-node theorem**. The condition \(\mathcal G_N''(x_c)<0\) is not established by the numerical scans currently documented and must not be labelled numerically verified without a dedicated curvature audit
```

## Extraction notes

Conditional on the stated regularity and nondegeneracy hypotheses. The source explicitly says model-specific negative curvature remains open.

## Review state

- Verbatim transcription: source excerpt copied from the identified immutable revision.
- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.
