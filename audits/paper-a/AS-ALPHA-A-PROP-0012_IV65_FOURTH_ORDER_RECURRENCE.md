# IV-65 — Fourth-Order Perturbative Recurrence

**Claim:** Derive the fourth-order state coefficient from the Schrödinger equation under intermediate normalization, retaining energy-correction terms.  
**Status:** ANALYTIC DERIVATION ONLY — NOT LEAN-VERIFIED.

## Setup
\(H(\lambda)=H_0+\lambda V\), \(E(\lambda)=E_0+\sum_{k\ge1}\lambda^kE_k\), and \(|\psi(\lambda)\rangle=\sum_{k\ge0}\lambda^k|\psi_k\rangle\), with \(|\psi_0\rangle=|0\rangle\), \(\langle0|\psi(\lambda)\rangle=1\). Thus \(\langle0|\psi_k\rangle=0\) for \(k\ge1\).

Define \(P=|0\rangle\langle0|\), \(Q=I-P\), and \(R_0=Q(E_0-H_0)^{-1}Q\).

## Energy recurrence
Projecting the Schrödinger equation onto \(\langle0|\) gives
\[
E-E_0=\lambda\langle0|V|\psi\rangle,
\qquad E_k=\langle0|V|\psi_{k-1}\rangle.
\]
For the transverse-field Ising ZZ perturbation, \(E_1=\langle0|V|0\rangle=0\). Do not assume \(E_2\) or \(E_3\) vanish.

## State recurrence
Q-projection and multiplication by the reduced resolvent yields
\[
|\psi_k\rangle=R_0Q\left[V|\psi_{k-1}\rangle-\sum_{j=1}^{k-1}E_j|\psi_{k-j}\rangle\right],\quad k\ge1.
\]
The sum is empty at k=1. Since \(R_0Q=R_0\), Q is retained to make the projection convention explicit.

## Orders 1–4
\[
\psi_1=R_0V\psi_0.
\]
\[
\psi_2=R_0(V\psi_1-E_1\psi_1)=R_0V\psi_1 \quad (E_1=0).
\]
\[
\psi_3=R_0(V\psi_2-E_1\psi_2-E_2\psi_1)=R_0(V\psi_2-E_2\psi_1).
\]
\[
\boxed{\psi_4=R_0(V\psi_3-E_1\psi_3-E_2\psi_2-E_3\psi_1)}
\]
and using \(E_1=0\):
\[
\boxed{\psi_4=R_0(V\psi_3-E_2\psi_2-E_3\psi_1).}
\]

Energy terms required to construct this are
\[
E_2=\langle0|V|\psi_1\rangle,\quad E_3=\langle0|V|\psi_2\rangle.
\]
(\(E_4\) is not needed in the Q-state recurrence at order four because the \(E_4\psi_0\) contribution is annihilated by Q.)

## What this resolves / what remains
This recurrence removes the earlier incomplete “three-resolvent chain only” description as a complete fourth-order state coefficient: the bare chain is only one contribution. The recurrence explicitly includes energy feedback terms \(E_2\psi_2\) and \(E_3\psi_1\), while vacuum projection is handled by P/Q normalization and energy equations—not by evaluating a zero-denominator resolvent.

**Not yet done:** explicit edge-index expansion, numerical coefficient extraction for the target response, proof that all recurrence terms are included in the final observable, symbolic/numerical cross-check, Lean formalization, or verification of Proposition 0012.