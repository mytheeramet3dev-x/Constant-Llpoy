# IV-178 — First-Principles Chain-Rule Audit for A and G

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional elementary-factor derivative bounds; inherited spectral estimates remain assumptions.

## 1. Definitions verified against IV-164

\[
A=d^2+16t(1-2p),\qquad G=d^2+16t(2p-1).
\]
With \(d=d(t,p)\), differentiate:
\[
A_t=2dd_t+16(1-2p),\quad G_t=2dd_t+16(2p-1),
\]
\[
A_p=2dd_p-32t,\quad G_p=2dd_p+32t.
\]

## 2. Bounds

Using \(d\le256/63\), \(|d_t|<4.194\), \(|d_p|\le1/252\), \(t\le1/64\), and \(|1-2p|,|2p-1|\le1\):
\[
|A_t|,|G_t|\le2d|d_t|+16
<2\frac{256}{63}(4.194)+16
=\boxed{50.084572}.
\]
And
\[
|A_p|,|G_p|\le2d|d_p|+32t
\le2\frac{256}{63}\frac1{252}+\frac12
=\boxed{0.532249938}.
\]
Rounded-up enclosures are \(|A_t|,|G_t|<50.084572\) and \(|A_p|,|G_p|<0.532250\).

## 3. Correction note

IV-163/164/165 used the radial upper bound \(7.455139\), which yielded \(76.587797\) for the radial elementary-factor derivatives. IV-175 subsequently derived the sharper conditional bound \(|d_t|<4.194\); substituting it reduces this chain-rule enclosure to \(50.084572\). The earlier bound remains conservative and not false, but is superseded for sharper downstream calculations.

## 4. Scope

Algebra and arithmetic are directly checked conditional on the inherited bounds for \(d,d_t,d_p\) and the branch sign premise used in the implicit differentiation. This note does not independently certify those assumptions or the full normalized-probability/entropy estimates.
