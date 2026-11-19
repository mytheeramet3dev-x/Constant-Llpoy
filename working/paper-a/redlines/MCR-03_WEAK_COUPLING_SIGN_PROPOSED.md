# MCR-03 — Proposed Redline: Weak-Coupling Response Sign

- **Document ID:** CL-PA-RL-MCR-03
- **Status:** PROPOSED MANUSCRIPT CORRECTION; INTERNAL ANALYTIC REVIEW RECORDED; NOT UPSTREAM-APPLIED
- **Affected claims:** AS-ALPHA-A-PROP-0012; supporting Lemma 5.2
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Affected manuscript locations:** §4.4.3; supporting Lemma 5.2 source proof
- **Frozen §4 source blob:** `a7570431eac62dd4555194df283edb5a9c87a28d`
- **Correction register item:** MCR-03

## 1. Exact conflict

The frozen supporting proof `lemma_5_2_proof.md` claims
\[
B-C<0
\]
for weak coupling and then claims a global sign flip between weak and strong coupling.

That derivation treats the order-\(r^2\) block in the \((|-+\rangle,|+-\rangle)\) sector as diagonal. It omits the coherence
\[
\rho_{-+,+-}=\sum_{k\ge3}a_{1k}a_{2k}.
\]
At the uniform point this coherence changes the leading block to a rank-one matrix. The original negative-sign calculation is therefore invalid. The immutable source audit `lemma_5_2_audit.md` explicitly identifies this omission and corrects the leading coefficient.

## 2. Corrected local asymptotic

Use the definitions from §5.2:
\[
B=\left.\frac{\partial I_{12}}{\partial J_{13}}\right|_{J_{ij}=J},
\qquad
C=\left.\frac{\partial I_{12}}{\partial J_{34}}\right|_{J_{ij}=J},
\]
where \(J_{13}\) shares one endpoint with the observed pair \(12\), while \(J_{34}\) is disjoint from it.

For each fixed finite \(N\ge4\), the corrected candidate asymptotic at the uniform reference point is
\[
B-C
=
\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)
+
O_N\!\left(
\frac{J^2}{h^3}
\left[1+\left|\ln(J/h)\right|\right]
\right),
\qquad J/h\to0^+.
\]
Since
\[
\frac{2(N-2)}{N-1}>1
\qquad(N\ge4),
\]
the leading coefficient is strictly positive. The relative remainder tends to zero for each fixed finite \(N\), so the reviewed asymptotic implies \(B-C>0\) for sufficiently small positive \(J/h\), with the smallness threshold and constants allowed to depend on \(N\).

The remainder is deliberately conservative. Do not restore the stronger remainder from the superseded source proof.

## 3. Proposed replacement for the §4.4.3 weak-coupling sentence

**Replace the sentence claiming “opposite-sign response characteristics” with:**

> The corrected fixed-finite-size weak-coupling expansion of the edge-response contrast is
> \[
> B-C=
> \frac{J}{8h^2}
> \ln\!\left(\frac{2(N-2)}{N-1}\right)
> +O_N\!\left(
> \frac{J^2}{h^3}
> [1+|\ln(J/h)|]
> \right),
> \qquad J/h\to0^+,
> \]
> for each fixed finite \(N\ge4\). Its leading coefficient is positive, and hence \(B-C>0\) sufficiently close to the weak-coupling endpoint. This corrects the negative-sign conclusion in the superseded version of Lemma 5.2. The result is local to the weak-coupling endpoint: it does not establish the sign for intermediate couplings, prove global positivity, or by itself establish a global continuation or branch-identification statement.

Do not retain “opposite-sign response characteristics” if it is intended to refer to \(B-C\). If the phrase was intended to refer to a different response observable, that observable must be named, defined, and proved separately before the phrase is reinstated.

## 4. Proposed disposition of supporting Lemma 5.2

The old negative-sign proof must be marked **SUPERSEDED — INVALID DERIVATION** and must not be cited as proof support.

The replacement supporting result should be stated as a **fixed-\(N\) weak-coupling endpoint asymptotic**, not as a global sign-flip theorem. Its proof must retain the full order-\(r^2\) coherence in the two-site reduced state and control the edge-derivative remainder. The detailed candidate derivation and its internal review are recorded in:

- `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md`
- `audits/paper-a/WEAK_COUPLING_B_MINUS_C_PROOF_AUDIT.md`
- `audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md`

The source snapshots of both the original proof and its correction audit remain immutable under `source_snapshots/paper-a/docs/`.

## 5. Evidence status and limitations

**Internal analytic review:** The audit records PASS for the listed finite-\(N\) perturbative steps, including the pair-flip amplitude, full coherence block, positive eigenvalue branch, shared/disjoint edge derivatives, entropy contributions from rank-deficient branches, and the leading logarithmic coefficient. This is an internal analytic review, not an external referee report.

**Numerical consistency:** Full-Hilbert-space high-precision checks for \(N=4,5,6\) are reported as consistent with the corrected leading term. These checks are corroborative only.

**Lean:** The current Lean declarations prove positivity of the logarithmic coefficient and the final sign implication conditional on an explicit remainder bound. They do not prove the model-specific differentiated remainder. Therefore the complete asymptotic is not Lean-verified and the full manuscript claim is not formally verified.

**Scope restrictions:**
- fixed finite \(N\ge4\);
- uniform all-to-all reference point;
- independent real edge derivatives evaluated at that point;
- sufficiently small positive \(J/h\);
- constants and endpoint neighborhood may depend on \(N\).

This result does not prove:
- \(B-C>0\) at all couplings;
- monotonicity or absence of intermediate sign changes;
- a uniform-in-\(N\) asymptotic;
- a global lower-branch continuation or branch-selection theorem;
- that a response-sector ordering alone determines dynamical stability.

The global sign-ordering problem therefore remains open.

## 6. Required follow-up before acceptance

1. Independently review the complete derivative proof, not only its summary audit.
2. Verify the exact definitions of \(B,C\), the uniform reference point, and the perturbation coordinates against the manuscript.
3. Formalize the differentiated remainder or clearly record it as analytic-only evidence with an explicit outstanding obligation.
4. Reconcile §4.4.3, the supporting Lemma 5.2, §5.3, claim registry, and semantic-correspondence records so no stale negative-sign or global sign-flip statement remains.
5. Preserve the old proof as a superseded source artifact and produce a new source manifest if/when the manuscript working copy is assembled.

## 7. Disposition

**PROPOSED CORRECTION — INTERNAL ANALYTIC REVIEW PASS WITH FORMALIZATION/CORRESPONDENCE OPEN.**

This redline does not modify the frozen source snapshot or the upstream `Absolute_Sym` repository. MCR-03 must not be marked fully resolved until the derivative proof receives independent review and all affected source and verification records are reconciled.
