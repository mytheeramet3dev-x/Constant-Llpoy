# AS-ALPHA-A-PROP-0008 — Subcritical exclusion of nontrivial roots

- **Claim ID:** `AS-ALPHA-A-PROP-0008`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** NOT_ASSESSED
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_02_revised.md`
- **Source blob SHA:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Source line range:** 197-206
- **Claim-specific Verification Obligation Matrix:** Pending extraction review

## Verbatim source excerpt

The following is transcribed from the pinned source. It is not a rewritten theorem statement.

```markdown
The statement that subcritical parameters have no nontrivial roots follows directly from the definition of the infimum:

\[
\eta<\alpha_N
\quad\Longrightarrow\quad
f(x;\eta)<0
\quad\text{for all }x>0,
\]

provided \(\mathcal G_N(x)>0\) on the domain considered.
```

## Extraction notes




The implication is conditional on positivity of G_N(x) over the considered domain. It proves subcritical exclusion only; it does not prove existence or exact root counts above threshold.




## Review state

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.
