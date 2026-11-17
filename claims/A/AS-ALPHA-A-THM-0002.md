# AS-ALPHA-A-THM-0002 — Perron–Frobenius nondegeneracy of the finite-N ground state

- **Claim ID:** `AS-ALPHA-A-THM-0002`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record)
- **Extraction status:** CANDIDATE
- **Constant Llapoy verification status:** MATHEMATICAL_REVIEW_PASS; LEAN_FORMALIZATION_PENDING
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_02_revised.md`
- **Source blob SHA:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Source line range:** 3-17
- **Claim-specific Verification Obligation Matrix:** Pending extraction review

## Verbatim source excerpt

The following is transcribed from the pinned source. It is not a rewritten theorem statement.

```markdown
## 2.1 The all-to-all transverse-field Ising model

We consider an \(N\)-qubit quantum many-body system with pairwise interactions represented initially by the complete graph \(K_N\). The Hamiltonian is

\[
H[\mathbf J]
=-
\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z
-h\sum_{i=1}^{N}\sigma_i^x,
\qquad h>0,
\]

where \(\sigma_i^\alpha\) are Pauli operators acting on site \(i\), and \(\mathbf J=\{J_{ij}\}_{i<j}\) is the edge-coupling configuration. The reference model takes \(J_{ij}\ge0\), although response derivatives are evaluated in the ambient real edge space around a symmetric point.

For finite \(N\) and \(h>0\), the ground state is nondegenerate. This follows from Perron–Frobenius theory after shifting the Hamiltonian by a sufficiently large multiple of the identity: the resulting matrix is nonnegative and irreducible in the computational \(\sigma^z\) basis.
```

## Extraction notes

The source invokes Perron–Frobenius theory and states nondegeneracy for finite N and h>0. The precise matrix sign convention, irreducibility proof, and full allowed coupling domain require independent mathematical review.







## Review state

- Independent extraction review: COMPLETED (see `PAPER_A_INDEPENDENT_EXTRACTION_REVIEW.md`).
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Counterexample review: NOT_RUN.
- Overall Constant Llapoy status: CANDIDATE / NOT_VERIFIED.

**Important:** Registration or transcription does not establish correctness, completeness, novelty, or Lean verification.

## Independent extraction review — 2026-11-17

- **Review status:** REVIEWED_WITH_ISSUES
- **Source transcription and locator:** Exact excerpt; Section 2, lines 3–17.
- **Finding:** The source says that shifting (H) by a large positive multiple of the identity makes the matrix nonnegative. This is false as written because the off-diagonal spin-flip entries remain (-h). The Perron–Frobenius argument should instead be applied to (cI-H) (or (-H+cI)), with (c) chosen to make the diagonal nonnegative. For finite (N), the spin-flip graph is connected and the off-diagonal entries are (+h), giving the needed irreducibility.
- **Disposition:** The nondegeneracy conclusion may be recoverable, but the source proof sentence is incorrect. Preserve the source excerpt; keep CANDIDATE / NOT_VERIFIED pending a corrected proof and domain audit.
- **Proof review:** NOT_COMPLETED. Formal verification: NOT_RUN.

### Supporting proof source located

The pinned upstream branch also contains `docs/tfim_ground_state_simplicity_lemma.md`, blob `472328b596ccdcc82ece65faf5ef65a9dab63e50`. It applies Perron–Frobenius to (cI-H), proves irreducibility from connectedness of the spin-flip hypercube, and states simplicity for finite (N\ge1), (h>0), and real couplings. This is a candidate proof dependency that repairs the sign of the argument in a separate source file. Constant Llapoy has not yet independently re-derived or formally verified that auxiliary proof; THM-0002 remains NOT_VERIFIED.


## Independent mathematical proof review — 2026-11-17

- **Review status:** MATHEMATICAL_PROOF_PASS.
- **Scope:** Finite-dimensional Hamiltonian, finite $N\ge1$, $h>0$, arbitrary finite real $J_{ij}$.
- **Corrected operator:** $K=cI-H$, with $c=1+\max_s H_{ss}$ in the computational basis.
- **Entrywise positivity:** Diagonal entries are at least $1$; single-spin-flip entries are $+h>0$; all other off-diagonal entries are zero.
- **Irreducibility:** The positive-entry graph is the connected $N$-dimensional hypercube.
- **Spectral identification:** Real symmetry identifies the Perron eigenvalue with $\lambda_{\max}(K)=c-E_{\min}(H)$, hence the ground eigenvalue of $H$ is simple.
- **Coupling domain:** The proof is valid for arbitrary real finite $J_{ij}$ because the couplings enter only the diagonal.
- **Formalization:** NOT_RUN. Do not mark the claim fully VERIFIED until Lean formalization and Hamiltonian/matrix correspondence are completed.
- **Review artifact:** `audits/paper-a/THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md`.

The original source excerpt and its incorrect shift sentence remain preserved unchanged. No upstream Absolute Symmetry file was modified.
