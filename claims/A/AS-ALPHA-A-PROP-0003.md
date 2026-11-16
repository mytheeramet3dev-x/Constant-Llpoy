# AS-ALPHA-A-PROP-0003 — Exact Picard local-attractivity criterion

- **Claim ID:** `AS-ALPHA-A-PROP-0003`
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
- **Source line range:** 192-225
- **Source revision date:** 2026-11-14T13:40:34Z
- **Claim-specific Verification Obligation Matrix:** Pending population after extraction review

## Verbatim source excerpt

The following is copied from the source revision above. It is not a rewritten theorem statement.

```markdown
### Picard iteration

The dimensionless fixed-point iteration is

\[
x^{(k+1)}=T(x^{(k)}),
\qquad
T(x)=\frac gh\mathcal G_N(x).
\]

At a fixed point,

\[
T'(x_*)=\frac gh\mathcal G_N'(x_*)
=1+\frac1hF_x(x_*,g,h).
\]

The exact linear stability condition for this iteration is

\[
\boxed{|T'(x_*)|<1}
\]

or equivalently

\[
\boxed{-2h<F_x(x_*,g,h)<0.}
\]

Near a generic saddle-node, \(F_x\) is small, so the branch with \(F_x<0\) has \(0<T'<1\) and is locally attracting, while the branch with \(F_x>0\) has \(T'>1\) and is locally repelling

Away from the bifurcation, the condition \(F_x<0\) alone is not sufficient: if \(F_x\le-2h\), the Picard multiplier has magnitude at least one

The term “physical branch” will therefore mean the branch selected by the documented continuation/iteration prescription, while “Picard stable” requires the full inequality \(|T'|<1\)
```

## Extraction notes

The source distinguishes the exact multiplier condition from the weaker descending-branch condition.

## Review state

- Verbatim transcription: source excerpt copied from the identified immutable revision.
- Independent extraction review: COMPLETED (see `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`).
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.
