# IV-98 — Formalization Audit of Symmetry, Analyticity, and Taylor Structure

**Status:** ANALYTIC-PARTIAL. Symmetry/analytic factorization argument clarified; coefficients and quantitative constants still require a complete proof write-up.

## Hamiltonian
H(J12,J23)=-J12 Z1Z2-J23 Z2Z3-h(X1+X2+X3), h>0.

Near (J12,J23)=(0,0), the unperturbed ground state |+++>_X is nondegenerate with a gap. The spectral projection and normalized ground-state ray can be chosen analytic in couplings locally. The marginal small eigenvalue branches are analytic because they are separated from the large eigenvalue near 0; likewise the small Schmidt eigenvalue q of rho_2.

## Exact sign-flip symmetries
Conjugation by X1 flips J12 and leaves J23 fixed. Conjugation by X3 flips J23 and leaves J12 fixed.
- For rho_1, X1 acts locally, while X3 acts on traced subsystem; both preserve rho_1's spectrum. Thus p1(J12,J23) is even separately in both couplings.
- For rho_3, the corresponding argument with X3 and X1 makes p3 even separately.
- For rho_2, both X1 and X3 act on traced spins, so rho_2 is invariant under either sign flip; q is even separately.

Therefore, each analytic scalar eigenvalue branch is locally a function of squared couplings s=J12^2, u=J23^2.

## Boundary decoupling and factorization
When J12=0, spin 1 is decoupled and remains in its pure transverse-field ground state, so p1(0,J23)=0. An analytic even function p1(s,u) vanishing at s=0 is divisible by s:
p1=J12^2 g1(J12^2,J23^2).
Similarly p3=J23^2 g3(J12^2,J23^2).
This is a local analytic factorization.

## Quadratic coefficients
First-order perturbation in an edge coupling creates the two-spin X-basis excitation with amplitude J/(4h). Thus its squared amplitude is J^2/(16h^2). For p1, the first edge is the only first-order excitation that flips spin 1; for p3 the analogous edge flips spin 3. This gives
p1=J12^2/(16h^2)+ higher analytic terms,
p3=J23^2/(16h^2)+ higher analytic terms.
Since the residual factors are analytic in s,u, on a compact local neighborhood their derivatives are bounded; consequently the ratio-aware form p1=x+O(x t), p3=y+O(y t) follows, with t=x+y and constants independent of x/y.

## Joint small Schmidt eigenvalue
q is analytic and separately even. The first-order ground-state excitations are edge pair-flips |--+>_X and |+-->_X with amplitudes J12/(4h), J23/(4h), orthogonal. The middle-spin flip sector receives the sum of their probabilities at quadratic order, yielding
q=(J12^2+J23^2)/(16h^2)+O((J12^2+J23^2)^2/h^4)=x+y+O(t^2).
Analyticity in squared couplings gives a locally uniform remainder on a compact neighborhood. This coefficient argument must be written out explicitly in a rigorous derivation (e.g. via rho_2 or Schmidt perturbation); it is not independently Lean-checked here.

## Entropy consequence (conditional on coefficient derivation)
With p1=x+O(xt), p3=y+O(yt), q=t+O(t^2), the entropy mean-value estimates imply
I(1:3)=t ln t-x ln x-y ln y+O(t^2 ln(1/t)) in nats, locally uniformly in the ratio x/y. Divide by ln 2 for bits.

## Correction in proof language
Evenness in a coupling is not by itself enough to claim dependence on the square of every coupling; the IV-95/97 argument requires the explicit independent sign-flip symmetries above. This audit records those symmetries. It does not certify the whole asymptotic lemma or proposition.

## Remaining
- Fully explicit second-order coefficient derivation for q.
- Quantitative analytic neighborhood/constants (optional for existence-type theorem but required for explicit numerical bound).
- Derive/verify B-C response difference; MI asymptotics alone do not prove Proposition 0012.
- No Lean proof or independent formal verification.

Paper A remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
