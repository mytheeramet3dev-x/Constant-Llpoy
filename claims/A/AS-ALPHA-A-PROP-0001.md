# AS-ALPHA-A-PROP-0001 — Conditional exact threshold scaling

- **Claim ID:** `AS-ALPHA-A-PROP-0001`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Mathematical verification status:** NOT_ASSESSED
- **Original source label:** See verbatim source excerpt
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_02_revised.md`
- **Source blob SHA:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Source line range:** 159-206
- **Source revision date:** 2026-11-14T13:40:34Z
- **Claim-specific Verification Obligation Matrix:** Pending population after extraction review

## Verbatim source excerpt

The following is copied from the source revision above. It is not a rewritten theorem statement.

```markdown
## 2.5 Critical threshold

Define the system-size-dependent threshold scaling coefficient by

\[
\alpha_N
\equiv
\inf_{x>0}\frac{x}{\mathcal G_N(x)}.
\]

If the infimum is attained at an interior point \(x_c>0\), then

\[
\eta_c=\alpha_N,
\qquad
g_c(h)=\alpha_Nh.
\]

At an interior differentiable minimizer,

\[
\frac{d}{dx}\left(\frac{x}{\mathcal G_N(x)}\right)_{x=x_c}=0,
\]

which is equivalent to

\[
\mathcal G_N(x_c)=x_c\mathcal G_N'(x_c).
\]

Equivalently, the tangent conditions for \(f\) are

\[
f(x_c;\alpha_N)=0,
\qquad
\partial_xf(x_c;\alpha_N)=0.
\]

The statement that subcritical parameters have no nontrivial roots follows directly from the definition of the infimum:

\[
\eta<\alpha_N
\quad\Longrightarrow\quad
f(x;\eta)<0
\quad\text{for all }x>0,
\]

provided \(\mathcal G_N(x)>0\) on the domain considered. The existence of roots for every \(\eta>\alpha_N\), and the claim that there are exactly two roots globally, require additional assumptions on continuity, endpoint behavior, and the global shape of \(x/\mathcal G_N(x)\). The saddle-node theorem used later is local and requires a nondegenerate interior minimum.
```

## Extraction notes

Section 2.5; exact scaling is conditional on interior attainment of the infimum.

## Review state

- Verbatim transcription: source excerpt copied from the identified immutable revision.
- Independent extraction review: COMPLETED (see `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`).
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.
