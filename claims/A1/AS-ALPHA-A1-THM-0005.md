# AS-ALPHA-A1-THM-0005 — Theorem 5 — Separated Critical Location Convergence (`PROVEN`)

- Claim ID: `AS-ALPHA-A1-THM-0005`
- Paper: A1
- Claim version: 0.1.0
- Extraction status: TRANSCRIBED
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `stage-a1-1-repair-review`
- Source commit: `b95f5777dfadaf5d31eef27d813ea56c33540d1c`
- Source path: `Alphabet/paper_a1/stage_a1_1/theorem_statements.md`
- Source blob SHA: `b83ac8cb242cb754dbf2e56e00995e90ec0a7d31`
- Source line range: 57-65

## Verbatim source excerpt

```markdown
## Theorem 5 — Separated Critical Location Convergence (`PROVEN`)

- **Statement:**
  1. For every finite $N \ge 2$, $M_N := \arg\min_{u>0} q_N(u)$ is non-empty and compact, and for every sufficiently small $\eta > 0$, $M_N \subset [1+\eta, 7]$ for all sufficiently large $N$.
  2. For **any** choice $u_{c,N} \in M_N$ (and more generally any near-minimizing sequence $q_N(u_N) = \tilde{\alpha}_N + o(1)$):
     $$\lim_{N \to \infty} u_{c,N} = u_c^{(\infty)} = 1.9286655968241796\dots, \qquad \lim_{N\to\infty} v_{c,N} = u_c^{(\infty)}.$$
- **Additional Hypotheses Beyond Theorem 4:** Requires Lemma 2.1 of Theorem 5 (existence & compact confinement of finite-$N$ minimizers) and Theorem 2(3) (strict uniqueness of $u_c^{(\infty)}$).
- **Explicit Non-Conclusions (Still Open):** Does **not** prove finite-$N$ global minimizer uniqueness $|M_N| = 1$ or $\mathcal{G}_N''(x_{c,N}) < 0$ for all finite $N$ (`OP-1`), does **not** prove $C^1/C^2$ convergence $G_N''(u_{c,N}) \to G_\infty''(u_c^{(\infty)})$ (`OP-4`), does **not** prove global $q_N \in C^\omega((0, \infty))$ / constant rank of $\rho_{12}^{(N)}$ for general $N \ge 4$, and does **not** settle physical/dynamical symmetry breaking (`OP-5`).
- **Proof:** [`proofs/critical_threshold_and_location_theorems.md`](proofs/critical_threshold_and_location_theorems.md) (Lemmas 2.1, 2.2 & Theorem 2).
```

## Extraction and epistemic notes

This is one of the five formal theorem statements listed for Stage A1-1. The source marks the results as PROVEN and links proof files. Constant Llapoy has not independently rederived or checked those proofs, their imported results, or their hypotheses. The record is limited to the exact Stage A1-1 source revision; it does not imply completion of Paper A1 as a whole or Stage A1-2.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
