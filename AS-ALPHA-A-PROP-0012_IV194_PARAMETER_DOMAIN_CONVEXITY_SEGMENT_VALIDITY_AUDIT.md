# IV-194 — Parameter Domain, Convexity, and Segment-Validity Audit

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Domain-geometry audit of inherited stated parameter bounds; admissibility of the implicit solution branch remains open.

## 1. Domain bounds retrieved

IV-180 and its inherited bounds state \(0\le t\le1/64\), with angular parameter \(p\) treated through \(p\in[0,1]\) in the component expressions, and additional implicit quantities bounded by \(4\le d\le256/63\), \(F\ge63/4\). These are distinct kinds of constraints:
- the explicit parameter box \(\mathcal B=[0,1/64]\times[0,1]\) in \((t,p)\);
- constraints on the implicit quantities \(d,F\) that must hold at the relevant solution points.

## 2. Convexity of the explicit box

The parameter box is convex. For any \((t_1,p_1),(t_2,p_2)\in\mathcal B\) and \(\lambda\in[0,1]\), the segment
\[
(t_\lambda,p_\lambda)=\lambda(t_1,p_1)+(1-\lambda)(t_2,p_2)
\]
satisfies \(0\le t_\lambda\le1/64\) and \(0\le p_\lambda\le1\). Therefore the explicit rectangular parameter box is segment-convex.

## 3. Critical distinction: parameter box vs. admissible implicit branch

Convexity of \(\mathcal B\) alone does not prove that the implicit-root admissible set
\[
\mathcal D_{\rm admissible}=\{(t,p)\in\mathcal B:\text{the required root exists, is unique, and all inherited conditions hold}\}
\]
is convex, nor does it prove that a particular implicit branch exists at every point of the box. In particular, the inherited conditions involving \(d\), \(F\), derivative bounds, and \(R_d\le0\) require separate validation.

A global Lipschitz conclusion on the admissible solution branch cannot be inferred unless every connecting segment is contained in a domain where the same branch is defined, differentiable, and the component derivative bounds hold uniformly. If the admissible set is not convex, a segment may leave it even when both endpoints are admissible.

## 4. What can be concluded now

- **Explicit parameter box convexity:** verified directly.
- **Convexity of the implicit-root admissible set:** not established.
- **Branch existence across the entire box:** not established.
- **Branch uniqueness and differentiability throughout the box:** not established.
- **Global Lipschitz estimate using IV-191:** valid only on any segment for which all inherited hypotheses and derivative ceilings are verified throughout; not yet promoted to a full-domain theorem.

## 5. Next proof obligations

1. Identify the exact implicit equation and root-selection rule defining \(d(t,p)\).
2. Establish existence and uniqueness over the intended parameter region.
3. Prove the admissible branch covers the region claimed in the proposition.
4. Establish continuity/differentiability on that region, including boundary treatment.
5. Verify the inherited bounds \(4\le d\le256/63\), \(F\ge63/4\), and sign conditions pointwise along the domain.
6. Determine whether the true branch domain is convex or replace straight-segment Lipschitz reasoning with a domain/path argument.

## 6. Verdict

**Explicit-box convexity: pass. Full admissible-domain / branch segment validity: open.** This audit closes only the elementary geometry of the stated rectangular parameter box. It does not certify the implicit branch or global Lipschitz validity of Proposition AS-ALPHA-A-PROP-0012.
