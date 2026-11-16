# Section 4 — Dynamic Scaling from Hamiltonian Homogeneity

## 4.1 Dynamic scaling parameterization

The positive energy-rescaling structure of the all-to-all TFIM implies that the natural dimensionless control parameter is
\[
\eta = \frac{g}{h}.
\]
When the threshold is attained at an interior point and obeys
\[
g_c(h) = \alpha_N h,
\]
we may parameterize a corresponding supercritical ray by
\[
g(\gamma,h) = \gamma g_c(h) = \gamma \alpha_N h,
\qquad \gamma > 1.
\]
This keeps \(\eta = \gamma \alpha_N\) fixed while \(h\) varies. It is a scaling-homogeneity construction, not a unitary invariance, and not, by itself, evidence for a thermodynamic phase transition.

## 4.2 Independence of dimensionless fixed points

The nontrivial fixed-point equation is
\[
f(x; \eta) = \eta \mathcal G_N(x) - x = 0.
\]
Along the ray \(g = \gamma \alpha_N h\), it becomes
\[
x = \gamma \alpha_N \mathcal G_N(x).
\]
Therefore, every corresponding root \(x_*(\gamma)\), whenever it exists, is independent of the absolute scale \(h\):
\[
\frac{\partial x_*}{\partial h} = 0.
\]
This statement holds root-by-root. It does not assert global uniqueness, nor does it select a branch without an explicit continuation or iteration prescription.

## 4.3 Picard multiplier and fixed-point derivatives

Let
\[
T(x) = \eta \mathcal G_N(x)
\]
be the dimensionless Picard map. Its multiplier is
\[
T'(x_*) = \eta \mathcal G_N'(x_*).
\]
The derivative of the dimensionless fixed-point function is
\[
\partial_x f(x_*; \eta) = \eta \mathcal G_N'(x_*) - 1 = T'(x_*) - 1.
\]

In dimensional variables, with the fixed-point function
\[
F(J, g, h) = g \mathcal G_N(J/h) - J,
\]
its derivative with respect to the physical coupling \(J\) is denoted by \(F_J\):
\[
F_J \equiv \frac{\partial F}{\partial J} = \frac{g}{h} \mathcal G_N'(J/h) - 1 = \eta \mathcal G_N'(x) - 1.
\]

Thus, under \(g = \gamma \alpha_N h\), we obtain the scale-invariant relations:
\[
\boxed{ F_J\big|_{J_*} = \gamma \alpha_N \mathcal G_N'(x_*) - 1 }
\]
and
\[
\boxed{ T'(x_*) = \gamma \alpha_N \mathcal G_N'(x_*) = F_J\big|_{J_*} + 1 }.
\]
Both quantities depend on \(h\) only through the dimensionless branch coordinate \(x_*(\gamma)\). At a tangent point \(x_c\):
\[
T'(x_c) = 1,
\qquad
F_J\big|_{J_c} = 0.
\]
The exact scalar Picard-attractivity condition for the iteration \(x_{k+1} = T(x_k)\) is:
\[
|T'(x_*)| < 1
\quad \Longleftrightarrow \quad
-2 < F_J\big|_{J_*} < 0.
\]

## 4.4 Asymptotic regimes

### 4.4.1 Near-critical regime

For the upper local branch supplied by the nondegenerate saddle-node theorem,
\[
\lim_{\gamma \to 1^+} x_*(\gamma) = x_c.
\]
Consequently,
\[
\lim_{\gamma \to 1^+} T'(x_*) = 1,
\qquad
\lim_{\gamma \to 1^+} F_J\big|_{J_*} = 0.
\]
The first limit corresponds to the marginality of the Picard map; the second is the tangent condition for the fixed-point function.

### 4.4.2 Large-\(\gamma\) regime (Strong coupling)

Assuming the selected upper branch admits a global continuation devoid of turning points or branch exchanges, \(\mathcal G_N(x)\) approaches a positive finite limit as \(x \to \infty\). The equation
\[
x = \gamma \alpha_N \mathcal G_N(x)
\]
then implies \(x_*(\gamma) \to \infty\) as \(\gamma \to \infty\). For \(N \ge 4\) and \(h > 0\), the unperturbed limiting Ising Hamiltonian has a two-dimensional ferromagnetic ground space. The transverse field selects the unique, parity-even cat state.

By applying Schrieffer–Wolff degenerate perturbation theory to the parity-even sector (see Lemma 5.1), we obtain the rigorous asymptotic expansion for the dimensionless mutual information:
\[
\mathcal G_N(x) = \ln 2 - \frac{1}{(N-1)^2 x^2} + O\left(\frac{\ln x}{x^4}\right) \qquad (x \to \infty).
\]
This proves that the endpoint limit is attained as:
\[
\lim_{x \to \infty} \mathcal G_N(x) = \ln 2.
\]
Furthermore, the analytic control of the entropy remainder near the degenerate subspace guarantees that the derivative follows the leading algebraic order:
\[
\mathcal G_N'(x) = \frac{2}{(N-1)^2 x^3} + O\left(\frac{\ln x}{x^5}\right).
\]
This rigorously establishes that
\[
\lim_{x \to \infty} \mathcal G_N'(x) = 0.
\]
Consequently, on the physical stable branch at large \(\gamma\), the multiplier and the fixed-point derivative satisfy:
\[
\lim_{\gamma \to \infty} T'(x_*(\gamma)) = 0,
\qquad
\lim_{\gamma \to \infty} F_J\big|_{J_*(\gamma)} = -1.
\]

### 4.4.3 Branch-domain qualification

The inequality
\[
x_*(\gamma) \ge x_c
\]
holds for the upper local branch near \(\gamma = 1\). Extending it to every \(\gamma \ge 1\) requires a **global continuation assumption** asserting the absence of intermediate reversing turning points or branch exchanges. In contrast, the lower interval \(0 < x < x_c\) forms the locally unstable branch near the saddle-node. A weak-coupling perturbative expansion (\(x \to 0\), Lemma 5.2) further confirms that this lower branch possesses distinct scaling and opposite-sign response characteristics compared to the physical stable branch.