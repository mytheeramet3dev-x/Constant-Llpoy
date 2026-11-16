# Independent Strong-Coupling Asymptotic Audit — AS-ALPHA-A-PROP-0009

- Audit ID: CL-A-AUDIT-SC-0009
- Date: 2026-11-17
- Target claim: `AS-ALPHA-A-PROP-0009`
- Frozen manuscript source: `Arxiv/paper_01_section_04_revised.md`, branch `paper-a-interval-audit-2026-11-14`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Manuscript source blob: `a7570431eac62dd4555194df283edb5a9c87a28d`
- Supporting source cited as Lemma 5.1: `docs/lemma_5_1_proof.md`, blob `db2c552f2d9bea663b20e05aefdc5447d2494a7b`
- Additional conditional entropy lemma: `docs/entropy_schur_remainder_lemma.md`, blob `ef404349c6effa7f13bb14b5cc24f45e3ce6b80`
- Constant Llapoy snapshots: corresponding files under `source_snapshots/paper-a/`
- Review type: source-dependency reconciliation and asymptotic derivative audit
- Lean status: NOT_RUN

## 1. Executive verdict

**The endpoint limit for the function follows conditionally from the displayed function asymptotic. The displayed derivative asymptotic does not follow from that function asymptotic, and the cited Lemma 5.1 is not a proof of the function expansion.**

The current evidence does not close the claim's proof chain. The most defensible status is **NOT_VERIFIED / PROOF_DEPENDENCY_MISMATCH**.

This audit does not establish that either asymptotic formula is false for the actual TFIM. It establishes that the cited and displayed arguments do not, as currently documented, prove them.

## 2. Source-dependency mismatch

Section 4.4.2 claims, for (N\ge4), that Schrieffer–Wolff perturbation theory (see Lemma 5.1) yields
[
G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}
+O\!\left(\frac{\ln x}{x^4}\right).
]
But the located file named Lemma 5.1 is titled “Asymptotic Positivity of (B-C)”. Its statement concerns
[
B=\partial_{J_{13}}I_{12},\qquad C=\partial_{J_{34}}I_{12},
]
and a proposed weak/strong endpoint sign of (B-C). It does not state or derive the displayed asymptotic expansion of (G_N(x)).

The supporting-source reconciliation independently records this mismatch. No separate exact proof source for the Section 4.4.2 (G_N) expansion was identified in the files examined in this pass.

**Finding:** the reference to Lemma 5.1 is mismatched or incomplete. It cannot currently be accepted as the proof dependency for PROP-0009.

## 3. What the function asymptotic does establish

If the first displayed expansion is independently proved for fixed finite (N\ge4), then because
[
\frac{1}{(N-1)^2x^2}\to0,
\qquad
\frac{\ln x}{x^4}\to0,
]
it follows that
[
\lim_{x\to\infty}G_N(x)=\ln2.
]
This endpoint limit is a valid consequence of the function expansion itself. It does not require differentiating the remainder.

The expansion alone does not establish monotonicity, the derivative asymptotic, or the derivative limit.

## 4. Differentiating the big-O remainder is invalid without extra control

Let
[
R(x)=O\!\left(\frac{\ln x}{x^4}\right).
]
This pointwise bound alone places no corresponding bound on (R'(x)). A smooth counterexample is
[
R(x)=\frac{\ln x}{x^4}\sin(x^6),\qquad x>1.
]
It satisfies exactly
[
R(x)=O\!\left(\frac{\ln x}{x^4}\right),
]
but direct differentiation gives
[
R'(x)=
\frac{1-4\ln x}{x^5}\sin(x^6)
+6x\ln x\cos(x^6).
]
The second term comes from differentiating `sin(x^6)`; it is of order (x\ln x) along subsequences and does not tend to zero.

Thus (R'(x)) need not be (O(\ln x/x^5)), and need not even tend to zero.

Consequently, from
[
G_N(x)=\ln2-a x^{-2}+O(\ln x/x^4)
]
one may not infer
[
G_N'(x)=2a x^{-3}+O(\ln x/x^5)
]
without a separate derivative estimate. Here (a=(N-1)^{-2}).

A sufficient replacement is an explicitly proved differentiated remainder estimate, for example
[
R_N'(x)=O_N(\ln x/x^5).
]
A stronger but convenient route is a symbol-type asymptotic expansion with derivative control, such as
[
R_N^{(k)}(x)=O_N(\ln x/x^{4+k})
]
for the required derivative orders. Holomorphy in a suitable complex sector plus a justified uniform bound may also supply derivative control via Cauchy estimates, but the domain and bound must actually be proved.

## 5. The located entropy–Schur lemma is conditional

The file `docs/entropy_schur_remainder_lemma.md` assumes
[
\|Q\|\le Kr^4,
\qquad
\|\partial_uQ\|\le Kr^4/J.
]
Under these assumptions it derives an entropy-derivative bound of order
[
O\!\left(\frac{r^4}{J}(1+|\ln r|)\right).
]
Its qualification expressly says Kato/Rellich analyticity of the ground-state projector does not itself prove these Schur-complement bounds. The model-specific estimates for the full TFIM reduced pair remain to be proved.

This lemma is a useful conditional tool, but it does not close the entropy derivative remainder merely by being present in the repository.

## 6. Additional audit of the cited Lemma 5.1

The located Lemma 5.1 concerns (B-C), not (G_N). Its one-flip leading contribution is a plausible and arithmetically consistent calculation:
[
B-C\sim \frac{h^2}{J^3(N-1)^3}
]
for fixed (N\ge4), provided the omitted differentiated entropy remainder is indeed lower order.

However, the proof's Step 5 asserts that because the small eigenvalues are (O(\varepsilon^4)), their edge derivatives are (O(\varepsilon^4/J)). The first estimate does not imply the second. A separate mixed-parameter perturbation estimate is required. The entropy–Schur lemma makes exactly those derivative bounds explicit as hypotheses rather than deriving them for the TFIM.

The strong-coupling reconciliation also identifies unresolved derivative estimates and invalid/unproved complex-domain bounds in other documents that claim explicit constants. Therefore the located Lemma 5.1 does not currently close even its own (B-C) theorem claim.

## 7. Hypotheses and scope

- The source's (N\ge4) restriction must be preserved in the claim record.
- The ferromagnetic strong-coupling setup requires the sign/domain of the uniform Ising coupling to be stated (the auxiliary reconciliation uses (J>0)).
- The asymptotic regime is (x=J/h\to\infty), equivalently (h/J\to0^+), with fixed finite (N).
- A pointwise (O_N(\cdot)) estimate for each fixed (N) is not automatically uniform in (N).
- The limit (G_N(x)\to\ln2), if established, does not itself prove the derivative limit or global properties of the fixed-point branch.

## 8. Disposition matrix

| Obligation | Result |
|---|---|
| Preserve (N\ge4) and strong-coupling regime | PASS |
| Verify actual subject of cited Lemma 5.1 | PASS: it concerns (B-C), not (G_N) |
| Locate proof of (G_N) function expansion | NOT_LOCATED |
| Infer endpoint limit from function expansion | PASS, conditional on expansion |
| Infer derivative expansion from function big-O alone | FAIL (smooth counterexample) |
| Establish derivative remainder independently | NOT_ESTABLISHED |
| Entropy–Schur derivative lemma | CONDITIONAL_ONLY |
| Close cited Lemma 5.1's (B-C) derivative remainder | NOT_ESTABLISHED |
| Lean verification | NOT_RUN |
| Constant Llapoy status | NOT_VERIFIED |

## 9. Required next proof obligations

1. Locate or derive the strong-coupling expansion of (G_N(x)) from the actual TFIM ground-state reduced density matrices, independently of the unrelated (B-C) Lemma 5.1.
2. Derive the reduced-state eigenvalue expansions with controlled remainders at fixed (N).
3. Establish the model-specific Schur-complement estimates (Q=O(r^4)) and (partial_uQ=O(r^4/J)), if using the entropy–Schur lemma.
4. Prove a differentiated asymptotic remainder for (G_N'(x)), rather than differentiating a pointwise big-O statement.
5. Only after these are closed, use the derivative expansion to establish the large-(\gamma) multiplier limit on a branch whose global continuation has separately been justified.

No manuscript or upstream file was modified. No claim status was upgraded.
