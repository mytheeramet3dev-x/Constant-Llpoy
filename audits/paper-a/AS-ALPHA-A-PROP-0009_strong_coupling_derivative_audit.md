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

## 5.1 Further gap inside the conditional entropy–Schur derivative lemma

There is an additional issue in the located entropy–Schur lemma's scalar derivative argument. It assumes only
[
0\le\lambda(r,u)\le Kr^4,
\qquad
|\partial_u\lambda(r,u)|\le Kr^4/J,
]
and then claims that (|1+\ln\lambda|) is bounded by a constant times (1+|\ln r|). The upper bound on (lambda) does not imply this: (lambda) may be much smaller than (r^4), making (|\ln\lambda|) arbitrarily larger.

For example, (lambda(r)=e^{-1/r}) satisfies (lambda(r)\le Kr^4) for small (r), and its derivative can satisfy an (O(r^4)) upper bound in a suitable parameter direction while the logarithm is still of order (1/r). Thus the stated hypotheses alone do not justify the claimed derivative entropy bound.

A sufficient repair for a nonzero small eigenvalue branch is a two-sided scale bound
[
c r^4\le\lambda(r,u)\le Kr^4
]
together with the stated derivative estimate. Another sufficient route is a relative derivative estimate such as (|\partial_u\lambda|\le C\lambda/J), since then (lambda|\ln\lambda|=O(r^4(1+|\ln r|))) for (0\le\lambda\le Kr^4). Zero eigenvalue branches must be handled separately and shown to have the appropriate vanishing derivative.

The model-specific positive leading coefficient (lambda_4>0), if rigorously established with a uniform remainder, could provide the needed lower bound for that particular branch. It does not automatically provide a lower bound for every small eigenvalue branch or for the Schur complement as a whole.

**Disposition:** the entropy–Schur lemma is conditional and its derivative conclusion needs stronger hypotheses than currently displayed. Do not cite it as a closed derivative estimate until this logarithmic lower-bound issue is repaired.
 
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
| Entropy–Schur derivative lemma | CONDITIONAL_ONLY; displayed scalar derivative bound also needs a lower/relative eigenvalue bound |
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


## 10. Follow-up derivation — uniform function and derivative now independently closed

**Follow-up date:** 2026-11-17  
**New evidence:**  
- audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md
- audits/paper-a/SMALL_EIGENVALUE_COEFFICIENT_GENERAL_N_DERIVATION.md
- audits/paper-a/FINITE_N_STRONG_COUPLING_EIGENVALUE_DIAGNOSTIC.md
- working/paper-a/CANONICAL_STRONG_COUPLING_DERIVATION.md

The previous audit correctly identified that the derivative asymptotic cannot be inferred from the undifferentiated function big-O term. A new derivation now supplies the missing argument directly from the finite-N Hamiltonian perturbation problem.

For every fixed finite \(N\ge4\), the two-site reduced state has one exact zero singlet eigenvalue, two large eigenvalues analytic near \(1/2\), and one small analytic eigenvalue

\[
\lambda_s(\varepsilon)=c_N\varepsilon^4+O_N(\varepsilon^6),
\qquad c_N>0,
\]

where \(c_4=1/648\) and \(c_N=1/[8(N-2)(N-1)^4]\) for \(N\ge5\). The coefficient is derived symbolically for \(N\ge9\), and the finite cases \(N=5,6,7,8\) are obtained by exact-rational recurrence. The N=4 coefficient is additionally checked by direct high-precision diagonalization.

This gives both a two-sided small-eigenvalue scale bound and a derivative bound on the uniform path. Combining these with the analytic large eigenvalue branches and the one-site entropy expansion yields, independently,

\[
\mathcal G_N(x)
=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right)
\]

and

\[
\mathcal G_N'(x)
=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right).
\]

Therefore the uniform endpoint limits \(\mathcal G_N(x)\to\ln2\) and \(\mathcal G_N'(x)\to0\) are now supported by an independent mathematical derivation for fixed finite \(N\ge4\). The derivative is not obtained by differentiating the bare big-O remainder.

### Revised disposition

| Obligation | Follow-up status |
|---|---|
| Derive the uniform function expansion from the Hamiltonian | **DERIVED** |
| Derive the small-eigenvalue coefficient for fixed N >= 9 | **DERIVED** |
| Check finite cases N=5,6,7,8 exactly | **EXACT-RATIONAL RECURRENCE** |
| Correct the N=4 small-eigenvalue coefficient | **CORRECTED: 1/648** |
| Derive the uniform \(x\)-derivative remainder independently | **DERIVED** |
| Resolve the frozen manuscript's Lemma 5.1 citation mismatch | **NOT_RESOLVED IN UPSTREAM** |
| Prove independent edge-direction derivatives \(B-C\) | **OPEN; OUTSIDE THIS CLAIM'S UNIFORM PATH** |
| Lean verification | **NOT_RUN** |
| Proof-to-manuscript correspondence audit | **NOT_RUN** |
| Overall Constant Llapoy status | **PARTIALLY VERIFIED** |

**Scope warning:** The new derivative is \(d\mathcal G_N/dx\) along the permutation-symmetric one-parameter path. It is not the ambient edge-direction derivative \(B-C\). No \(B-C\) theorem status is upgraded by this follow-up.

No Absolute Symmetry source file was modified.
