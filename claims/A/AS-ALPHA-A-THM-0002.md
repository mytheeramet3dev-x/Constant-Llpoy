# AS-ALPHA-A-THM-0002 — Perron–Frobenius nondegeneracy of the finite-N ground state

- **Claim ID:** `AS-ALPHA-A-THM-0002`
- **Paper:** A
- **Claim version:** 0.1.0 (first extraction record; source-faithful statement retained)
- **Extraction status:** REVIEWED_WITH_ISSUES
- **Constant Llapoy verification status:** MATHEMATICAL_PROOF_PASS; LEAN_FORMALIZATION_PENDING; HAMILTONIAN_CORRESPONDENCE_PENDING
- **Canonical source repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Source branch:** `paper-a-interval-audit-2026-11-14`
- **Source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source path:** `Arxiv/paper_01_section_02_revised.md`
- **Source blob SHA:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Source line range:** 3-17
- **Claim-specific Verification Obligation Matrix:** Open; Lean formalization and exact Hamiltonian/matrix correspondence remain outstanding.

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

## Extraction and source-integrity notes

- The source invokes Perron–Frobenius theory and states nondegeneracy for finite N and h>0.
- The source's stated shift of H by a positive multiple of the identity is incorrect as written: the off-diagonal spin-flip entries remain -h.
- Preserve the excerpt verbatim. The corrected argument below applies Perron–Frobenius to cI-H instead.
- The pinned upstream branch also contains `docs/tfim_ground_state_simplicity_lemma.md`, blob `472328b596ccdcc82ece65faf5ef65a9dab63e50`. It is supporting source material, not a substitute for this repository's independent review or formalization.

## Independent mathematical proof review — 2026-11-17

- **Review status:** MATHEMATICAL_PROOF_PASS.
- **Scope:** Finite-dimensional Hamiltonian, finite N≥1, h>0, arbitrary finite real J_ij.
- **Corrected operator:** K=cI-H, where c=1+max_s H_ss in the computational basis.
- **Entrywise nonnegativity:** Diagonal entries are at least 1; single-spin-flip entries are +h>0; all other off-diagonal entries are zero.
- **Irreducibility:** The positive-entry graph is the connected N-dimensional hypercube.
- **Spectral identification:** K is real symmetric, so its Perron eigenvalue is its largest eigenvalue, λ_max(K)=c-E_min(H). Thus the ground eigenvalue of H is simple and its computational-basis eigenvector can be chosen strictly positive.
- **Coupling domain:** The proof is valid for arbitrary finite real J_ij because the couplings affect only the diagonal.
- **Review artifact:** `audits/paper-a/THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md`.

## Verification status and remaining obligations

| Obligation | Status | Evidence / next requirement |
|---|---|---|
| Source extraction and provenance | COMPLETED_WITH_ISSUES | Exact pinned excerpt and source blob retained above |
| Corrected finite-dimensional mathematical proof | PASS | Independent review artifact |
| Counterexample/domain review | PASS within stated finite-N, h>0, finite-real-coupling scope | h>0 and finite N are essential hypotheses |
| Lean theorem formalization | OPEN | Formalize finite matrix construction and Perron–Frobenius application |
| Hamiltonian-to-matrix correspondence in Lean | OPEN | Prove computational-basis entries and hypercube connectivity for the encoded Hamiltonian |
| Full claim verification | NOT_YET_VERIFIED | Do not promote until both Lean obligations pass and assumptions are audited |

## Review chronology

1. Initial extraction record: CANDIDATE; no mathematical proof review had yet been performed.
2. Independent extraction review: REVIEWED_WITH_ISSUES; identified the incorrect shift sentence in the source.
3. Independent mathematical proof review: MATHEMATICAL_PROOF_PASS for the corrected cI-H argument and the scope stated above.
4. Current state: mathematical proof review passes; Lean formalization and formal correspondence remain pending.

**No upstream Absolute Symmetry file was modified. Registration, mathematical review, and CI success are distinct from full formal verification.**
