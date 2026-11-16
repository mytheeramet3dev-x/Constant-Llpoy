# AS-ALPHA-A-PROP-0006 — Positive energy rescaling preserves the ground-state projector and yields dimensionless mutual information

- **Claim ID:** `AS-ALPHA-A-PROP-0006`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** NOT_ASSESSED
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_02_revised.md`
- **Source blob SHA:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Source line range:** 71-111
- **Claim-specific Verification Obligation Matrix:** Pending extraction review

## Verbatim source excerpt

The following is transcribed from the pinned source. It is not a rewritten theorem statement.

```markdown
## 2.3 Dimensional scaling

Define the dimensionless coupling

\[
x=\frac Jh,
\qquad h>0.
\]

At the symmetric point,

\[
H(J,h)
=h\left[
-x\sum_{i<j}\sigma_i^z\sigma_j^z
-\sum_i\sigma_i^x
\right]
\equiv h\widetilde H(x,1).
\]

This is a positive energy rescaling, not a unitary scale transformation. Multiplication by the positive scalar \(h\) leaves the spectral projectors unchanged. Thus, for a nondegenerate ground state,

\[
|\Psi_0(J,h)\rangle
=e^{i\theta(J,h)}|\widetilde\Psi_0(x)\rangle,
\]

for some irrelevant phase \(\theta\). Equivalently, the ground-state projectors are identical:

\[
|\Psi_0(J,h)\rangle\langle\Psi_0(J,h)|
=|\widetilde\Psi_0(x)\rangle\langle\widetilde\Psi_0(x)|.
\]

Consequently,

\[
I_{12}(J,h)=\mathcal G_N(x),
\]

where \(\mathcal G_N\) is dimensionless.
```

## Extraction notes


This is a positive scalar energy rescaling, not a unitary symmetry. The statement relies on h>0 and nondegeneracy; do not extend it to h=0 or degenerate ground spaces without separate treatment.






## Review state

- Independent extraction review: COMPLETED (see `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`).
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.
