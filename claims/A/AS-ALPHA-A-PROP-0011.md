# AS-ALPHA-A-PROP-0011 — Scale covariance of edge-response eigenvalues

- **Claim ID:** `AS-ALPHA-A-PROP-0011`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** NOT_ASSESSED
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_05_revised.md`
- **Source blob SHA:** `671c97fa68fa48c929760bf9956d197b358c4904`
- **Source line range:** 127-131
- **Claim-specific Verification Obligation Matrix:** Pending extraction review

## Verbatim source excerpt

The following is transcribed from the pinned source. It is not a rewritten theorem statement.

```markdown
3. **Scale covariance of perturbations.** Since the ground state depends on (J,h) through (x=J/h), response eigenvalues have the dimensional scaling
\[
\chi_k(J,h)=h^{-1}\,\widetilde\chi_k(x).
\]
Thus the ordering of the sectors is independent of the overall energy scale (h), but the dimensional eigenvalues themselves are not strictly invariant under changing (h). The same qualification applies to the feedback eigenvalues (g\chi_k), which depend on the dimensionless ratio (g/h).
```

## Extraction notes







This is a dimensional covariance claim for response eigenvalues. The underlying differentiability and chain-rule assumptions, and the meaning of the response matrix in the ambient real edge space, remain proof obligations.

## Review state

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.

## Independent extraction review — 2026-11-17

- **Review status:** REVIEWED — excerpt boundary corrected
- **Source locator:** Section 5, lines 127–131 is correct.
- **Finding:** The first extraction omitted the numbered-item prefix; this record now includes the complete contiguous source passage from lines 127–131.
- **Disposition:** Excerpt boundary corrected. Retain CANDIDATE / NOT_ASSESSED; mathematical proof review remains separate. The (h^{-1}) scaling is a chain-rule consequence once the ground state is a differentiable function of (J/h); differentiability and the response-map domain remain proof obligations.
- **Proof review:** NOT_COMPLETED. Formal verification: NOT_RUN.
