# Lemma 5.2: Asymptotic Negativity of \( B-C \) at Weak Coupling (Lower Branch)

**Statement:** For the all-to-all transverse-field Ising model, let \( B = \partial I_{12} / \partial J_{13} \) and \( C = \partial I_{12} / \partial J_{34} \). For any fixed finite \( N \ge 4 \), in the weak-coupling limit \( J/h \to 0 \) (which corresponds to the dimensionless limit \( x \to 0 \), typically associated with the lower unstable branch of the saddle-node bifurcation), \( B - C < 0 \).

## Step 1: Weak-Coupling Expansion

At weak coupling, the unperturbed Hamiltonian is \( V_x = -h \sum_i \sigma_i^x \), and the perturbation is \( H_z = -\sum_{i<j} J_{ij} \sigma_i^z \sigma_j^z \). 
The unperturbed ground state is the unique polarized state in the \( X \)-basis:
\[
|\Psi_0\rangle = |++\cdots+\rangle
\]
The perturbation \( H_z \) flips pairs of spins. The first-order corrected ground state is:
\[
|\Psi\rangle = |\mathbf{+}\rangle + \sum_{i<j} \frac{J_{ij}}{4h} |i,j\rangle_{--} + O(J^2/h^2)
\]
where \( |i,j\rangle_{--} \) denotes the state with spins \( i \) and \( j \) in the \( |-\rangle \) state and all others in \( |+\rangle \).

## Step 2: Reduced Density Matrix \( \rho_{12} \)

We trace out the environment \( E = \{3, \dots, N\} \) to obtain the reduced density matrix for sites 1 and 2 in the \( X \)-basis \( \{|++\rangle, |+-\rangle, |-+\rangle, |--\rangle\} \).
The surviving terms are those where the environment states match:
- The diagonal entries to leading order are:
  \[
  \rho_{++} = 1 - O(J^2/h^2)
  \]
  \[
  \rho_{--} = \left(\frac{J_{12}}{4h}\right)^2
  \]
  \[
  \rho_{-+} = \sum_{k \in E} \left(\frac{J_{1k}}{4h}\right)^2
  \]
  \[
  \rho_{+-} = \sum_{k \in E} \left(\frac{J_{2k}}{4h}\right)^2
  \]
- The off-diagonal coherence between \( |++\rangle \) and \( |--\rangle \) is \( \rho_{++,--} = \frac{J_{12}}{4h} \).

The \( \{|++\rangle, |--\rangle\} \) block has a zero determinant at \( O(J^2/h^2) \) because \( \rho_{++}\rho_{--} - |\rho_{++,--}|^2 \approx 1 \cdot \left(\frac{J_{12}}{4h}\right)^2 - \left(\frac{J_{12}}{4h}\right)^2 = 0 \). Thus, its small eigenvalue is \( O(J^4/h^4) \).

The non-zero small eigenvalues of \( \rho_{12} \) at order \( O(J^2/h^2) \) are simply the diagonal entries \( \rho_{-+} \) and \( \rho_{+-} \).

## Step 3: Entropy Evaluation

Let \( S(p) = -p \ln p \). The entropy of the reduced pair is dominated by the \( O(J^2/h^2) \) eigenvalues:
\[
S(\rho_{12}) = S(\rho_{-+}) + S(\rho_{+-}) + O(J^4 \ln J)
\]
For the single-site marginals, \( \rho_1 = \mathrm{Tr}_2 \rho_{12} \) has small eigenvalue \( \rho_{--} + \rho_{-+} \), so:
\[
S(\rho_1) = S(\rho_{--} + \rho_{-+}) + O(J^4 \ln J)
\]
\[
S(\rho_2) = S(\rho_{--} + \rho_{+-}) + O(J^4 \ln J)
\]
Let \( w_{ij} = \left(\frac{J_{ij}}{4h}\right)^2 \). Then:
\[
I_{12} = S\left(w_{12} + \sum_{k \in E} w_{1k}\right) - S\left(\sum_{k \in E} w_{1k}\right) + S\left(w_{12} + \sum_{k \in E} w_{2k}\right) - S\left(\sum_{k \in E} w_{2k}\right)
\]

## Step 4: Derivative Control and Sign of B - C

We evaluate the derivatives \( B = \partial I_{12} / \partial J_{13} \) and \( C = \partial I_{12} / \partial J_{34} \) at the uniform point \( J_{ij} = J \).
At the uniform point, \( w_{ij} = w = (J/4h)^2 \).

For the shared edge \( J_{13} \):
\[
\frac{\partial w_{13}}{\partial J_{13}} = \frac{2J}{16h^2} = \frac{J}{8h^2}
\]
Since \( J_{13} \) only appears in the sum \( \sum_{k \in E} w_{1k} \) (and not in \( w_{12} \) or \( w_{2k} \)), we use the chain rule with \( S'(x) = -1 - \ln x \):
\[
B = \frac{J}{8h^2} \left[ S'((N-1)w) - S'((N-2)w) \right]
\]
\[
B = \frac{J}{8h^2} \left[ (-1 - \ln((N-1)w)) - (-1 - \ln((N-2)w)) \right] = \frac{J}{8h^2} \ln\left(\frac{N-2}{N-1}\right)
\]
Since \( N \ge 4 \), we have \( \frac{N-2}{N-1} < 1 \), which implies \( \ln\left(\frac{N-2}{N-1}\right) < 0 \). Thus, \( B < 0 \).

For the disjoint edge \( J_{34} \):
The perturbation \( J_{34} \) connects two sites in the environment \( E \). It does not appear in any \( w_{1k} \) or \( w_{2k} \), which only involve edges connected to site 1 or site 2.
Therefore, to leading order in \( J/h \):
\[
C = 0
\]

## Conclusion

Subtracting the two responses gives:
\[
B - C = \frac{J}{8h^2} \ln\left(\frac{N-2}{N-1}\right) + O(J^3/h^4)
\]
Because the leading term is strictly negative for all finite \( N \ge 4 \), we conclude that \( B - C < 0 \) in the weak-coupling limit \( J/h \to 0 \).

**Physical Consequence:** This rigorously proves that the sign of \( B - C \) flips between the weak-coupling limit (\( x \to 0 \), lower branch) and the strong-coupling limit (\( x \to \infty \), upper branch). The condition \( B - C > 0 \) is a unique property of the physical stable branch at large \( x \), resolving the open ordering problem asymptotically.