# PROP-0012 — Even-Block Entry Orders via Pair-Flip Parity

**Scope:** Fixed finite N; TFIM ground state in the x-basis; small r; independent real edge perturbations in a fixed small neighborhood. This derives the stronger even-block entry orders from selection rules, conditional only on the analytic perturbation expansion and explicit coefficient bookkeeping.

## 1. Pair-flip selection rule

The interaction is a sum of pair-flip operators in the x-basis. A configuration with Hamming weight k can be reached from the vacuum only after a number of pair flips whose parity matches k/2 (modulo 2): for a 2-flip configuration, only odd perturbation orders occur; for a 4-flip configuration, only even orders occur. The finite-N analytic ground-state vector can be normalized with vacuum coefficient c_empty=1+O_N(r^2).

Consequently:
- two-flip amplitudes: c_{ij}=a_{ij}+O_N(r^3);
- four-flip amplitudes: c_{ijkl}=O_N(r^2);
- vacuum coefficient: c_empty=1+O_N(r^2).

The same order statements hold for first edge derivatives because coefficients are jointly analytic in (r,u), with the perturbation variables confined to a fixed neighborhood.

## 2. Reduced even-block entries

Use the even block indexed by |++>,|-->, with environmental configurations traced out.

- L = rho_{++,++}=1+O_N(r^2).
- X = rho_{++,--}. Environment empty contributes c_empty*c_{12}=a_12+O_N(r^3). Nonempty even environment first contributes products of two-flip and four-flip amplitudes, O_N(r^3). Thus X=a_12+O_N(r^3).
- S = rho_{--,--}. Environment empty contributes |c_12|^2=a_12^2+O_N(r^4); nonempty even environment first contributes squared four-flip amplitudes, O_N(r^4). Hence S=a_12^2+O_N(r^4).

All bounds are joint in the edge-perturbation neighborhood and hold for first edge derivatives.

## 3. Schur cancellation upgraded

Since L=1+O_N(r^2), X=a_12+O_N(r^3), and S=a_12^2+O_N(r^4), we have |X|^2=a_12^2+O_N(r^4) and
D=S-|X|^2/L=O_N(r^4).

For the block's small eigenvalue, lambda_s=det M/lambda_L=(L/lambda_L)D, where lambda_L stays bounded away from zero and L/lambda_L=1+O_N(r^2). Therefore lambda_s=O_N(r^4), jointly analytic, nonnegative; its first edge derivatives are also O_N(r^4).

The entropy directional derivative is consequently O_N(r^4(1+|ln r|)) by the already-reviewed nonnegative analytic entropy lemma.

## 4. Caution / verification boundary

The parity/order argument is analytically sound, but the derivation is written as a selection-rule closure, not a machine-checked formal proof. It depends on the Hamiltonian's exact pair-flip form and finite-N analytic ground-state vector. A detailed coefficient-level independent computation or Lean proof could strengthen confidence, but no Lean formalization/build was run.

**Verdict:** Stronger even-block remainder PASS by pair-flip selection rules, for fixed finite N and local edge-perturbation neighborhood. This is not a global theorem and does not resolve the odd positive branch or full source-conflict issue.
