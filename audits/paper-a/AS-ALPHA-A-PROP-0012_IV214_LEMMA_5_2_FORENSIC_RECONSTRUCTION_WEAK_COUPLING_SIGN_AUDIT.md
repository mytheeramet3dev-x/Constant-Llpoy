# AS-ALPHA-A-PROP-0012 — IV-214 Lemma 5.2 Forensic Reconstruction & Weak-Coupling Sign Audit

**Date:** 2026-11-23  
**Target:** fixed finite \(N\ge4\), all-to-all TFIM, uniform positive coupling \(J\), transverse field \(h>0\), \(r=J/h\to0^+\).  
**Repository:** Constant Llpoy (independent audit; no upstream edits).  
**Disposition:** corrected leading sign independently re-derived from the source snapshot; derivative-remainder closure is CONDITIONAL on the explicit amplitude-order hypotheses in the working proof; no Lean verification.

## 0. Source-access correction

The preceding conversational IV-213 summary said frozen source recovery was confirmed. The evidence fetched for this audit does **not** establish live upstream recovery of the private frozen branch. What is available here are immutable source snapshots and provenance records stored in Constant Llpoy, which identify the upstream branch/commit/blob. This is snapshot-level evidence, not a fresh fetch from Absolute_Sym. IV-213's conversational claim of live recovery is therefore withdrawn/qualified. No upstream files were modified.

## 1. Source material actually inspected

- `source_snapshots/paper-a/docs/lemma_5_2_proof.md` — original negative-sign argument.
- `source_snapshots/paper-a/docs/lemma_5_2_audit.md` — corrected coherence/sign audit.
- Both provenance records identify upstream frozen commit `8deb7de4a49cb2060720246b7101820ee7e08c91`, original paths and blob hashes:
  - original proof blob `4c1b70a7233f470ca46adaafe59868b2e0779253`;
  - corrected audit blob `a5e47defd859b4eb5ed5e63d65d12eeff320f9c7`.
- `working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md` — independent candidate derivative proof.
- `audits/paper-a/WEAK_COUPLING_B_MINUS_C_PROOF_AUDIT.md` — prior internal analytic review.
- `audits/paper-a/ANALYTIC_NONNEGATIVE_EIGENVALUE_ENTROPY_DERIVATIVE_LEMMA.md` — entropy directional derivative lemma.

The working derivative proof was retrieved at the correct path. An earlier path under `audits/` returned 404; it is not counted as a source.

## 2. Original Lemma 5.2 — fatal omission

The original argument reduces the odd-parity block of the two-site reduced density matrix to diagonal terms and omits
\[
\rho_{-+,+-}=\sum_{k\ge3}a_{1k}a_{2k}.
\]
At the uniform point, this omitted coherence is order \(r^2\), not negligible compared with the diagonal entries. The original entropy expression and resulting negative leading sign are invalid.

**Finding:** original negative-sign derivation FAILS (specific leading-order omission).

## 3. Corrected odd block and leading response

With \(a_{ij}=J_{ij}/(4h)\), \(w=(r/4)^2\), the uniform odd block at leading order is
\[
(N-2)w\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
with eigenvalues \(2(N-2)w\) and zero. The leading entropy combination is
\[
I_{12}^{\rm lead}=2S((N-1)w)-S(2(N-2)w),
\quad S(s)=-s\ln s,
\]
subject to control of the differentiated remainder.

For the shared edge \(J_{13}\),
\[
\partial_{J_{13}}w=\frac{J}{8h^2}.
\]
The leading derivative of the positive odd eigenvalue is the same coefficient; the disjoint edge \(J_{34}\) does not enter the leading odd Gram matrix. One-site entropy derivatives and the pair entropy derivative combine; the \(\ln r\) pieces cancel, yielding
\[
\boxed{(B-C)_{\rm lead}=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)>0,\quad N\ge4.}
\]
The positivity follows because \(2(N-2)/(N-1)>1\) for every integer \(N\ge4\).

**Finding:** corrected leading coefficient PASS (local fixed-\(N\) perturbative calculation).

## 4. Remainder/derivative audit

The candidate derivative proof states a conservative joint-analytic remainder at first, then improves the even block by an exact shared-amplitude Schur cancellation:
\[
D=S-\frac{|X|^2}{L}=O_N(r^4),\quad
\partial_{u_e}D=O_N(r^4).
\]
It derives \(\lambda_s=O_N(r^4)\) and \(\partial_{u_e}\lambda_s=O_N(r^4)\), hence entropy derivative scale \(O_N(r^4(1+|\ln r|))\). The odd positive branch is simple after factoring out \(r^2\); its eigenvalue and edge derivatives are analytic. The zero branch is handled as a nonnegative analytic eigenvalue attaining an interior minimum, giving zero first directional entropy derivative without evaluating \(\ln0\).

However, the Schur cancellation relies on the pair-flip support/amplitude-order lemma for environment coefficients and their first edge derivatives. The retrieved working note presents this hypothesis and its orders but does not itself provide a separate full derivation/verification of the support lemma from the exact ground-state expansion. The internal review's PASS rows are therefore conditional on those hypotheses.

- Joint analyticity of finite-dimensional ground-state projector near the gapped \(r=0\) point: PASS, standard analytic perturbation framework.
- First-order pair-flip coefficient \(a_{ij}=J_{ij}/(4h)\): PASS, gap denominator \(4h\).
- Odd-block coherence inclusion and leading eigenvalue: PASS.
- One-site small eigenvalue and edge derivatives at leading order: PASS, under analytic expansion.
- Even-block Schur cancellation \(D=O(r^4)\) with edge derivative: CONDITIONAL PASS (amplitude-order/support lemma required).
- Entropy derivative lemma: PASS under its listed joint analyticity, nonnegativity and vanishing-order hypotheses.
- Full derivative remainder \(o(J/h^2)\): CONDITIONAL on even-block amplitude-order lemma and analytic coefficient/remainder estimates; not Lean-verified.

With the conditional remainder \(O_N(r^2h^{-1}(1+|\ln r|))\) in response units, it is smaller than the leading \(r/h\) term as \(r\to0\), since \(r|\ln r|\to0\). This yields eventual positivity for each fixed finite \(N\), if the conditional derivative closure is valid.

## 5. Scope: what this does and does not settle

1. The original negative-sign proof is invalid.
2. The corrected positive leading sign is established at the perturbative leading-order level.
3. Fixed-\(N\), sufficiently-small-\(r\) positivity is **conditional**, not promoted to unconditional theorem by this audit.
4. No explicit coupling threshold, uniform-in-\(N\) bound, global sign, or stable/unstable branch correspondence is established.
5. The lower-branch interpretation of \(r\to0\) in the manuscript's self-consistency parameterization remains a separate correspondence obligation.
6. The source snapshot's provenance does not equal a live frozen-source fetch; exact source recovery remains blocked/unverified.
7. No Lean run or formal proof correspondence is claimed.

## 6. IV-214 conclusion

\[
\boxed{\text{Corrected leading }B-C>0\text{; derivative closure CONDITIONAL; PROP-0012 OPEN.}}
\]

This audit supersedes any conversational wording that called the entire weak-coupling sign theorem unconditionally proved or claimed frozen-source live recovery based only on stored snapshots.
