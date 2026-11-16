# AS-ALPHA-A1-THM-0001 — Theorem 1 — OP-2: Compact Uniform $C^0$ Convergence Near & Across the Critical Window (`PROVEN`)

- Claim ID: `AS-ALPHA-A1-THM-0001`
- Paper: A1
- Claim version: 0.1.0
- Extraction status: TRANSCRIBED
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `stage-a1-1-repair-review`
- Source commit: `b95f5777dfadaf5d31eef27d813ea56c33540d1c`
- Source path: `Alphabet/paper_a1/stage_a1_1/theorem_statements.md`
- Source blob SHA: `b83ac8cb242cb754dbf2e56e00995e90ec0a7d31`
- Source line range: 7-20

## Verbatim source excerpt

```markdown
## Theorem 1 — OP-2: Compact Uniform $C^0$ Convergence Near & Across the Critical Window (`PROVEN`)

- **Statement:** For every finite $U > 0$,
  $$\lim_{N \to \infty} \sup_{u \in [0, U]} \left|G_N(u) - G_\infty(u)\right| = 0,$$
  where the limit holds over all integers $N \ge 2$ (both even and odd $N$).
- **Hypotheses:** Exact finite-$N$ global ground states $|\Psi_0^{(N)}(u/N)\rangle$ on the $P_x = +1$ permutation-symmetric branch (`h > 0, J = u h / N >= 0`); Størmer's quantum de Finetti theorem (1969).
- **Important Caveats:**
  1. Proven via sequential continuous convergence + hypercube Perron–Frobenius + Banach–Alaoglu compactness, **not** Dini's theorem (which fails due to non-monotonicity in $N$, e.g. at $u = 1.25$).
  2. Yields uniform $C^0$ convergence without explicit algebraic $N$-rates across the LMG critical window.
  3. Does **not** yield uniform convergence of derivatives $G_N', G_N''$; uniform $C^1$ convergence fails near $u = 1$ because $G_\infty'(1^-) = 0 \neq \ln 2 = G_\infty'(1^+)$.
  4. Finite-$N$ curves satisfy $G_N \in C^1([0, \infty))$ with $\lim_{u\to 0^+} G_N'(u) = G_N'(0^+) = 0$ (proved directly via two-sided Kato analyticity and Rellich even-order eigenvalue branching around $u = 0$, giving $G_N'(u) = \frac{u}{2N^2}\ln\frac{N}{u} + O_N(u)$ and $\lim_{u\to 0^+} G_N''(u) = +\infty$ on $(0, \delta_N)$; [`proofs/op2_uniform_convergence.md`](proofs/op2_uniform_convergence.md) §3(2)), rather than $C^\omega([0, \infty))$.
- **Proof:** [`proofs/op2_uniform_convergence.md`](proofs/op2_uniform_convergence.md) (Theorem 4.1).

---
```

## Extraction and epistemic notes

This is one of the five formal theorem statements listed for Stage A1-1. The source marks the results as PROVEN and links proof files. Constant Llapoy has not independently rederived or checked those proofs, their imported results, or their hypotheses. The record is limited to the exact Stage A1-1 source revision; it does not imply completion of Paper A1 as a whole or Stage A1-2.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
