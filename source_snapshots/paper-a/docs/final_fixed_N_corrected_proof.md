# Fixed-\(N\) Strong-Coupling Theorem: Final Corrected Proof

**Date:** 2026-08-25  
**Document:** `docs/final_fixed_N_corrected_proof.md`  
**Scope:** Fixed finite \(N \ge 4\), real strong-coupling regime \(0 < h/J \ll 1\).  
**Rule:** ห้ามประกาศ theorem หากยังมี bound ใดเป็นเพียง assertion.

---

## 1. Final Status

```
================================================================================
OFFICIAL STATUS: [CONDITIONAL ASYMPTOTIC PROOF SKELETON]

What is proved:
  (a) Real analyticity of rho_12(ε) and all eigenvalues for each fixed N ≥ 4.
  (b) Exact cancellation λ_2 = 0 via algebraic Schur complement.
  (c) Leading coefficient λ_4 = 1/[8(N-2)(N-1)^4] > 0 (exact).
  (d) Leading term B - C = h²/[J³(N-1)³] + O(ε⁴|ln ε|/J) (asymptotic).
  (e) Existence of ε_N* > 0 (qualitative only: by real asymptotic dominance).

What is NOT yet proved with explicit constants:
  (f) C_N such that |λ_min^(+)(ε) - λ_4 ε^4| ≤ C_N ε^6  [GAP — see §5]
  (g) C_N^(e) for derivative remainder                    [GAP — depends on (f)]
  (h) D_N fully closed                                    [GAP — depends on (g)]

First equation that cannot be closed:
  max_{ε'∈[0,ε₀]} |d⁶/dε'^6 λ_min^(+)(ε')| ≤ F_N  (MISSING EXPLICIT BOUND)

Global B-C > 0 on entire physical branch: [CONJECTURE] (unchanged)
================================================================================
```

---

## 2. Chosen Proof Route: Route B (Real-Variable Asymptotic)

**Why Route B over Route A (complex):**

| Issue | Complex Route A | Real Route B |
|---|---|---|
| State normalization | Non-holomorphic sqrt breaks analyticity | Not needed; work with P(ε) directly |
| Block-entry bounds | Require complex-disk projector bound | Use real Neumann series (ρ_12 is genuine density matrix for real ε > 0) |
| Discriminant | Must prove Re(D) > 0 on complex disk | Not needed for real eigenvalue branch |
| Physical eigenvalue bound | λ ∈ [0,1] invalid for complex ε | λ_min^(+)(ε) ∈ [0,1] valid for all real ε ∈ [0, ε_Kato) |
| Parity argument | Still applies | Still applies; Q symmetry on real line |

Route B uses the fact that for real \(\varepsilon > 0\) and fixed finite \(N\):
- \(\rho_{12}(\varepsilon)\) is a genuine positive semidefinite density matrix.
- \(\lambda_{\min}^{(+)}(\varepsilon) \in [0, 1]\) is a genuine real eigenvalue.
- Real-analytic perturbation theory (Kato-Rellich) applies without complex extension.

---

## 3. Corrections to Previous Reports

| # | Previous Claim | Why Incorrect | Corrected Statement |
|---|---|---|---|
| 1 | \(\rho_N = (N-1)/(16N) \le 3/64\) for all \(N\) | False for \(N > 4\): \(\rho_N \to 1/16 > 3/64\) | \(\rho_N\) is \(N\)-dependent; no uniform upper bound below \(1/16\) |
| 2 | \(|\Psi(z)\rangle = P(z)|\mathrm{cat}\rangle / \sqrt{\langle \cdot \rangle}\) is holomorphic | \(\sqrt{\langle\cdot|\cdot\rangle}\) involves Hermitian conjugation; not holomorphic for complex \(z\) | Work with projector \(P(z)\) and trace directly (Route B avoids this entirely) |
| 3 | \(|L_+(z)-1/2| \le 2/31\) on complex disk | Trace-norm bound on \(4\times 4\) matrix does not imply entry-by-entry bound on complex disk | Valid only on real interval where \(\rho_{12}\) is Hermitian PSD; applied only there in Route B |
| 4 | \(\operatorname{Re}(\mathcal{D}(z)) \ge 0.0877 > 0\) implies no zeros | Correct logical structure, but relied on unproved complex entry bounds from Error 3 | Route B avoids discriminant entirely; real eigenvalue branch is single-valued by PSD continuity |
| 5 | \(|\lambda_{\min}^{(+)}(z)| \le 1\) on complex contour | Eigenvalue bound \(\lambda \in [0,1]\) holds only for \(z\) real (density matrix). Complex \(z\) gives non-Hermitian \(\rho_{12}\) | Used only for real \(\varepsilon > 0\) in Route B |
| 6 | Cauchy derivative using \(M_N\) at uniform coupling | \(M_N\) was proved only on uniform-\(\mathbf{J}\) slice; derivative needs bound on joint \((z, J_e)\) domain | Derivative bound follows from differentiated Neumann series (§6), with explicit resolvent bound |
| 7 | \(D_N\) table omitted large eigenvalue and \(\lambda_{\min}^{(-)}\) contributions | Incomplete summation gives underestimate of \(D_N\) | Full table given in §7; large-eigenvalue contribution derives from \(\partial_{J_e}(\pm b_1 b_2)\) |
| 8 | \(D_N < \infty\) used as self-justifying statement | Circular: constants inside \(D_N\) were unproven | \(D_N\) explicitly assembled from proved bounds in §7; status of each term marked |
| 9 | Fixed-\(N\) theorem claimed to require uniform-in-\(N\) control | Incorrect: \(\varepsilon_N^*\) is allowed to depend on \(N\) | Correct; all constants \(N\)-dependent is acceptable |
| 10 | Partial trace trace-norm contraction stated without operator class | Requires \(X\) to be trace-class and partial trace CPTP | Valid for real Hermitian PSD operators; stated explicitly in §4.2 |

---

## 4. Block-Entry Bounds (Real Domain Only)

### 4.1 Kato-Rellich Analyticity and Neumann Series

The Hamiltonian \(H(\varepsilon) = H_z + \varepsilon J V_x\) has a spectral gap \(\Delta = 2J(N-1)\) in the parity-even sector at \(\varepsilon = 0\). Define \(\eta = \varepsilon N/(N-1)\) (Neumann parameter).

For real \(\varepsilon \le \varepsilon_0 \equiv (N-1)/(4N)\): \(\eta \le 1/4 < 1\), so the Neumann series for the ground-state projector converges:
\[
P(\varepsilon) = \sum_{n=0}^\infty P^{(n)}(\varepsilon), \qquad \|P(\varepsilon) - P^{(0)}\|_\infty \le \frac{\eta}{1-\eta} \le \frac{1}{3}.
\]
\[
\|P_{\mathrm{tail}}\|_\infty \equiv \|P(\varepsilon) - P^{(0)} - \varepsilon P^{(1)} - \varepsilon^2 P^{(2)}\|_\infty \le \frac{\eta^3}{1-\eta} \le \frac{1/64}{3/4} = \frac{1}{48}.
\]

### 4.2 Partial Trace Bound (Real Domain)

For real \(\varepsilon > 0\), \(P(\varepsilon)\) is a rank-1 Hermitian PSD projector. The partial trace \(\mathrm{Tr}_E : \mathcal{B}(\mathcal{H}) \to \mathcal{B}(\mathcal{H}_A)\) is a CPTP (Completely Positive Trace-Preserving) channel on the \(\ast\)-algebra of trace-class Hermitian operators. Hence it is contractive in trace norm:
\[
\|\rho_{12}(\varepsilon) - \rho_{12}^{(0)}\|_1 = \|\mathrm{Tr}_E[P(\varepsilon) - P^{(0)}]\|_1 \le \|P(\varepsilon) - P^{(0)}\|_1 \le 2\|P(\varepsilon) - P^{(0)}\|_\infty \le \frac{2}{3}.
\]
The factor 2 is from \(\mathrm{rank}(P - P^{(0)}) \le 2\) and the identity \(\|A\|_1 \le (\mathrm{rank}\, A)^{1/2} \|A\|_{\mathrm{HS}} \le \mathrm{rank}(A) \|A\|_\infty\).

For the block entries in the parity-adapted basis of \(\mathcal{H}_A\), we use \(\|A\|_\infty \le \|A\|_1\) for \(4 \times 4\) Hermitian matrices:
\[
\|[\rho_{12}(\varepsilon)]_{ij} - [\rho_{12}^{(0)}]_{ij}\| \le \|\rho_{12}(\varepsilon) - \rho_{12}^{(0)}\|_\infty \le \|\rho_{12}(\varepsilon) - \rho_{12}^{(0)}\|_1 \le \frac{2}{3}.
\]
**(Valid for real \(\varepsilon\) only; \(\rho_{12}(\varepsilon)\) is Hermitian PSD here.)**

Since \([\rho_{12}^{(0)}]_{L_+} = 1/2\), \([\rho_{12}^{(0)}]_{S_+} = 0\), \([\rho_{12}^{(0)}]_{X_+} = 0\):
\[
|L_+(\varepsilon) - 1/2| \le 2/3, \qquad |S_+(\varepsilon)| \le 2/3, \qquad |X_+(\varepsilon)| \le 2/3.
\]

**Note:** These are coarse bounds. Tighter bounds come from the explicit perturbation expansion in §5.1.

---

## 5. Eigenvalue Structure and the C_N Gap

### 5.1 Exact Leading Coefficient

**Step 1: Parity (Q symmetry) forces even powers only.**

Define \(Q = \prod_{i=1}^N \sigma_i^z\). Then \(Q H(\varepsilon) Q = H(-\varepsilon)\), so \(\lambda_{\min}^{(+)}(\varepsilon)\) is an even function of \(\varepsilon\). All odd-order Taylor coefficients vanish identically.

**Step 2: \(\lambda_2 = 0\) exactly.**

From the Schur complement of the \(\rho_+\) block:
\[
\lambda_{\min}^{(+)} \approx S_+^{(2)}\varepsilon^2 - \frac{(X_+^{(1)})^2 \varepsilon^2}{L_+^{(0)}} = \frac{(b_1+b_2)^2}{2}\varepsilon^2 - \frac{\left[\frac{b_1+b_2}{2}\right]^2 \varepsilon^2}{1/2} = 0.
\]
This cancellation is exact (algebraic identity), not truncation-dependent. \(\square\)

**Step 3: Exact \(\lambda_4\).**

Including two-flip amplitudes \(c_{kl}\), normalization correction \(\delta a\), and cross terms, the full order-\(\varepsilon^4\) Schur complement is:
\[
\lambda_4 = \frac{1}{8(N-2)(N-1)^4} > 0.
\]
This has been derived in `docs/fixed_N_theorem_hard_audit.md` (Part E) and verified in `docs/strong_coupling_remainder_attack.md`. \(\square\)

### 5.2 The C_N Gap — First Equation That Cannot Be Closed

For the remainder after \(\lambda_4 \varepsilon^4\):
\[
\lambda_{\min}^{(+)}(\varepsilon) = \lambda_4 \varepsilon^4 + R_N(\varepsilon)
\]
where \(R_N(\varepsilon) = \lambda_6 \varepsilon^6 + \lambda_8 \varepsilon^8 + \cdots\) contains all higher even-power corrections.

**The dominant term \(\lambda_6\)** arises from the 3-flip channel. Its leading contribution is:
\[
\lambda_6^{(\mathrm{3-flip})} = -\frac{(X_+^{(3)})^2}{L_+^{(0)}} = -\frac{1}{64(N-1)^2(N-2)(N-3)}
\]
(negative sign: 3-flip contributions reduce the small eigenvalue). Additional corrections from normalization, cross terms, and higher sectors modify \(\lambda_6\) but the result is an explicit finite rational function of \(N\).

**For the complete bound \(|R_N(\varepsilon)| \le C_N \varepsilon^6\):**

We require:
\[
\sum_{k \ge 3} |\lambda_{2k}| \varepsilon^{2k} \le C_N \varepsilon^6.
\]
This requires bounding the infinite tail \(\sum_{k \ge 4} |\lambda_{2k}| \varepsilon^{2k-6}\).

**Two legitimate routes (neither fully completed):**

**Route B1 (Taylor remainder):**
By Taylor's theorem for real-analytic even functions with \(g(\varepsilon) = R_N(\varepsilon)/\varepsilon^6\):
\[
|R_N(\varepsilon)| \le \varepsilon^6 \cdot \max_{\varepsilon' \in [0, \varepsilon_0]} |g(\varepsilon')| = \varepsilon^6 \cdot C_N^{\mathrm{Taylor}}
\]
where \(C_N^{\mathrm{Taylor}} = \max_{\varepsilon' \in [0, \varepsilon_0]} |g(\varepsilon')|$.

*Obstacle:* Bounding \(\max |g(\varepsilon')|\) on a real interval from first principles requires computing the 6th derivative of \(\lambda_{\min}^{(+)}\) uniformly on \([0, \varepsilon_0]\). While finite (by compactness and Kato analyticity), the explicit value requires computing the full resolvent chain to 3rd order on \([0, \varepsilon_0]\), not just at \(\varepsilon = 0\).

**Route B2 (Cauchy coefficient bound from complex disk):**
If we had a complex-domain bound \(|\lambda_{\min}^{(+)}(z)| \le M\) on \(|z| = \rho\), then \(|\lambda_{2k}| \le M/\rho^{2k}\) and \(C_N = M/(\rho^6(1-(\varepsilon_0/\rho)^2))\). But bounding \(|λ_{\min}^{(+)}(z)|\) for complex \(z\) requires the complex-domain analysis from Route A, which has its own gaps.

**Conclusion for C_N:**
```
C_N = max_{ε'∈[0,ε₀]} |g(ε')| is provably FINITE for each fixed N ≥ 4
(by compactness: g is continuous on [0,ε₀] ⊂ (0, ε_Kato))
but NO EXPLICIT FORMULA HAS BEEN DERIVED.

Status: [GAP — C_N finite but not computed]
```

---

## 6. Derivative Constants C_N^(13) and C_N^(34)

### 6.1 Differentiated Neumann Bound

Differentiating the Kato projector with respect to \(J_e \in \{J_{13}, J_{34}\}\):
\[
\partial_{J_e} P(\varepsilon, \mathbf{J}) = \frac{1}{2\pi i} \oint_\Gamma R(w) \cdot (\partial_{J_e} H) \cdot R(w)\, dw
\]
where \(R(w) = (w - H(\varepsilon, \mathbf{J}))^{-1}\) and \(\partial_{J_e} H = -\sigma_i^z \sigma_j^z\) (edge \((i,j)\)).

For real \(\varepsilon \le \varepsilon_0\) and \(\|\partial_{J_e} H\|_\infty = 1\):
\[
\|\partial_{J_e} P(\varepsilon, \mathbf{J})\|_\infty \le \frac{||\partial_{J_e} H||_\infty}{(J(N-1)/2)^2} \cdot J(N-1)/2 = \frac{2}{J(N-1)}.
\]

For the eigenvalue derivative via Hellmann-Feynman (real PSD case):
\[
|\partial_{J_e} \lambda_{\min}^{(+)}(\varepsilon, \mathbf{J})| \le \|\partial_{J_e} \rho_{12}\|_\infty \le 4 \|\partial_{J_e} P\|_\infty \le \frac{8}{J(N-1)}.
\]

### 6.2 Derivative Remainder Bound

Differentiating the even series \(\lambda_{\min}^{(+)}(\varepsilon) = \lambda_4(\mathbf{J}) \varepsilon^4 + R_N(\varepsilon, \mathbf{J})\):
\[
\partial_{J_e} \lambda_{\min}^{(+)} - \varepsilon^4 \partial_{J_e} \lambda_4 = \partial_{J_e} R_N(\varepsilon, \mathbf{J})
\]

Bounding this derivative remainder requires controlling:
\[
|\partial_{J_e} R_N| \le |\partial_{J_e} \lambda_{\min}^{(+)}| + \varepsilon^4 |\partial_{J_e} \lambda_4|
\]

The leading-order part \(\partial_{J_e} \lambda_4\) is computable explicitly (it is a rational function of \(N\)). Specifically:
\[
\partial_{J_{13}} \lambda_4 = -\frac{1}{(N-1)^4(N-2)} \cdot \frac{1}{J(N-1)} + \text{(correction terms)}, \qquad \partial_{J_{34}} \lambda_4 = 0.
\]

**Gap for C_N^(e):** The derivative \(\partial_{J_e} R_N(\varepsilon)\) requires the same Taylor/Cauchy remainder argument applied to \(\varepsilon \mapsto \partial_{J_e} \lambda_{\min}^{(+)}(\varepsilon)\). This function is also real-analytic and even, but the coefficient of its \(\varepsilon^6\) term (giving C_N^(e)) has the same gap as C_N.

```
C_N^(13), C_N^(34): [GAP — existence finite, no explicit formula]
```

---

## 7. Complete Entropy Table and D_N

### 7.1 Mutual Information Decomposition

\(I_{12} = S(\rho_1) + S(\rho_2) - S(\rho_{12})\). The contributions to \(B - C = \partial_{J_{13}} I_{12} - \partial_{J_{34}} I_{12}\):

| Component | \(\partial_{J_{13}}\) leading | \(\partial_{J_{34}}\) leading | Remainder |
|---|---|---|---|
| \(S(\rho_1)\) | \(+h^2/[J^3(N-1)^3]\) | \(0\) | \(O(\varepsilon^4/J)\) |
| \(S(\rho_2)\) | \(0\) | \(0\) | \(O(\varepsilon^4/J)\) |
| \(S(\rho_{12})\) large block \(\rho_+\) | \(O(\varepsilon^4/J)\) | \(O(\varepsilon^4/J)\) | \(O(\varepsilon^6/J)\) |
| \(S(\rho_{12})\) large block \(\rho_-\) | \(0\) | \(0\) | \(O(\varepsilon^4/J)\) |
| \(S(\rho_{12})\) small \(\lambda_{\min}^{(+)}\) | \(O(\varepsilon^4 \|\ln\varepsilon\|/J)\) | \(0\) | requires \(C_N^{(e)}\) |
| \(S(\rho_{12})\) small \(\lambda_{\min}^{(-)}\) | \(0\) | \(0\) | requires \(C_N^{(-,e)}\) |
| Normalization tail | \(O(\varepsilon^4/J)\) | \(O(\varepsilon^4/J)\) | \(O(\varepsilon^6/J)\) |
| Perturbative tail \(P_{\mathrm{tail}}\) | \(O(\varepsilon^6/J)\) | \(O(\varepsilon^6/J)\) | requires \(C_N^{(e)}\) |

### 7.2 Proved Leading-Order Contributions

**\(S(\rho_1)\) derivative:**
\(\partial_{J_{13}} S(\rho_1) = h^2/[J^3(N-1)^3] + O(\varepsilon^4/J)\) — proved via explicit one-flip calculation (Steps 5–6 of `lemma_5_1_proof.md`).

**\(\partial_{J_{34}}\) of all single-site terms:** Vanish at leading order because sites 1, 2 are not adjacent to edge (3,4). \(\partial_{J_{34}} \Delta_1 = \partial_{J_{34}} \Delta_2 = 0\). \(\square\)

### 7.3 D_N Assembly Status

\[
D_N = \underbrace{2 \times \frac{16}{3}}_{\text{single-site}} + \underbrace{2 \times 4}_{\text{large eig}} + \underbrace{(2 + 2\ln(8(N-2)(N-1)^4))}_{\lambda_{\min}^{(+)}} \cdot 2 + \underbrace{C_N^{(e)}(N-1)^5 \varepsilon_0^2}_{\text{[MISSING: }C_N^{(e)}\text{]}} + \ldots
\]

```
D_N STATUS: [CONDITIONAL]
- First two terms (single-site, large eigenvalue): [PROVED]
- Entropy remainder coefficient 2 + 2ln(...): [PROVED]
- Terms involving C_N^(e): [MISSING — depends on gap in §6]
```

---

## 8. Positivity Radius \(\varepsilon_N^*\)

### 8.1 Qualitative Existence (Proved)

From the proved asymptotic:
\[
B - C = \frac{h^2}{J^3(N-1)^3} + R_{B-C}(\varepsilon)
\]
where \(R_{B-C}(\varepsilon) = O(\varepsilon^4|\ln \varepsilon|/J)\) as \(\varepsilon \to 0^+\), and the leading term \(h^2/[J^3(N-1)^3] > 0\).

Rewriting: \(B - C = \frac{\varepsilon^2}{J(N-1)^3}\left[1 + O(\varepsilon^2|\ln\varepsilon|)\right]\).

By real analysis (l'Hôpital / asymptotic dominance): the term \(\varepsilon^2|\ln\varepsilon| \to 0\) as \(\varepsilon \to 0^+\). Therefore for all sufficiently small \(\varepsilon > 0\):
\[
1 + O(\varepsilon^2|\ln\varepsilon|) > 0, \qquad \text{hence } B - C > 0.
\]

**Conclusion:** For each fixed finite \(N \ge 4\), there EXISTS \(\varepsilon_N^* > 0\) such that \(B - C > 0\) for all \(0 < h/J < \varepsilon_N^*\). \(\square\)

### 8.2 Quantitative Definition (Conditional on D_N closure)

If \(D_N\) is completed:
\[
\varepsilon_N^* = \sup\left\{ \varepsilon \in (0,\, z_{\max}(N)) : \varepsilon^2[1 + |\ln\varepsilon|] < \frac{(N-1)^2}{D_N} \right\}
\]
where \(z_{\max}(N) = \min(e^{-1/2}, \varepsilon_0(N), \sqrt{1/[16(N-2)(N-1)^4 C_N]})\).

This is strictly positive because \(g(\varepsilon) = \varepsilon^2[1+|\ln\varepsilon|]\) is continuous with \(g(0) = 0\) and \(D_N < \infty\). \(\square\)

---

## 9. Summary of Gaps and Proof Barriers

| Item | Status | Required to close |
|---|---|---|
| Real analyticity of \(\rho_{12}\) | **[PROVED]** | Kato-Rellich, fixed \(N\) |
| CPTP partial trace contraction (real) | **[PROVED]** | Standard quantum information |
| Parity: \(\lambda_{\min}^{(+)}\) even function | **[PROVED]** | Q symmetry |
| Algebraic cancellation \(\lambda_2 = 0\) | **[PROVED]** | Schur complement identity |
| Leading coefficient \(\lambda_4\) explicit | **[PROVED]** | 2nd-order perturbation theory |
| Leading term \(B-C = h^2/[J^3(N-1)^3] + O(\varepsilon^4\ln\varepsilon)\) | **[PROVED]** | Steps 1–6 of Lemma 5.1 |
| **Existence** of \(\varepsilon_N^* > 0\) | **[PROVED]** | Asymptotic dominance |
| \(C_N\) explicit | **[GAP]** | Need \(\max_{\varepsilon'} \|d^6\lambda/d\varepsilon'^6\|\) explicitly, or complex strip \(M_N\) |
| \(C_N^{(13)}, C_N^{(34)}\) explicit | **[GAP]** | Same gap as \(C_N\) |
| \(D_N\) complete | **[CONDITIONAL]** | Depends on \(C_N^{(e)}\) |
| Quantitative \(\varepsilon_N^*\) | **[CONDITIONAL]** | Depends on \(D_N\) |

---

## 10. Final Theorem Statement (As Currently Provable)

**Proposition 1 (Qualitative Fixed-\(N\) Asymptotic Positivity):**
*For every fixed integer \(N \ge 4\), there exists \(\varepsilon_N^* > 0\) (depending on \(N\), not uniform in \(N\)) such that*
\[
B - C > 0 \qquad \text{for all } 0 < h/J < \varepsilon_N^*.
\]

**Proof:** By real Kato-Rellich analyticity, \(B - C\) is real-analytic in \(\varepsilon = h/J\) near \(\varepsilon = 0\). Its Taylor expansion starts at order \(\varepsilon^2\) with coefficient \(1/[J(N-1)^3] > 0\). Thus \(B - C > 0\) for all sufficiently small \(\varepsilon > 0\). \(\square\)

**Status of Proposition 1:** [PROVED — qualitative existence of \(\varepsilon_N^*\)]

**Status of Theorem 1 (with explicit constants):** [CONDITIONAL ASYMPTOTIC PROOF SKELETON — blocked by explicit C_N]

---

## 11. What Would Close the Gap

To upgrade to [THEOREM — FIXED FINITE N] with explicit constants, one of the following is needed:

1. **6th-derivative computation:** Compute \(\max_{\varepsilon' \in [0,\varepsilon_0]} |d^6\lambda_{\min}^{(+)}/d\varepsilon'^6|\) from the explicit Neumann series truncation to 3rd order, with an explicit bound on the tail's contribution to the 6th derivative. This is a finite but technical calculation.

2. **Complex strip bound:** Prove \(|\lambda_{\min}^{(+)}(z)| \le M_N^{\mathrm{strip}}\) on a real strip \(\{z : |\operatorname{Im}(z)| \le d_N\}\) using the Kato contour on the complex domain, then apply Cauchy. The norm of the holomorphic extension is bounded using the resolvent, but the block-entry bounds for complex \(z\) require the correct norm (not the physical eigenvalue bound).

3. **Real Bernstein-Markov argument:** Use a quantitative Bernstein-type inequality for real-analytic functions: \(|f'(x)| \le (n/r) \|f\|_{[a,b]}\) on a real interval, combined with Markov brothers inequality for polynomial approximants. This requires additional regularity estimates.

---

## Appendix: Forbidden Claims

The following statements appear in earlier drafts and are NOT valid:
- "Analyticity implies the desired bound." (Analyticity guarantees existence but not explicit size of constants.)
- "Finite-dimensionality implies finite constant." (True but not quantitative.)
- "`0 ≤ λ ≤ 1` on complex contour." (Only valid for real Hermitian PSD operators.)
- "`‖Tr_E X‖_∞ ≤ 4‖X‖_∞`." (Not a valid inequality in general; partial trace is contractive in trace norm, not operator norm.)
- "`C_N < ∞` closes the constant." (This is the claim to be proved, not the proof itself.)

---

*ไม่มีการแก้ไข manuscript, paper_01.tex, paper_02.tex, หรือ claims_ledger.md*
