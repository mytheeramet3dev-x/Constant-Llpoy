# IV-177 — Updated Derivative Bounds for F from Refined Implicit Sensitivities

## Setup and inherited assumptions
Let \(F=d^2-16t\). Inherit conditional bounds \(d\le d_*=256/63\), \(|d_t|<4.194\) from IV-175, and \(|d_p|\le1/252\) from corrected IV-176.

By the chain rule,
\[
F_t=2d d_t-16,\qquad F_p=2d d_p.
\]
Taking absolute values and using the stated bounds:
\[
|F_t|\le2d_*\cdot4.194+16
=\boxed{50.0845714286},
\]
\[
|F_p|\le2d_*\cdot\frac1{252}
=\boxed{0.0322499371}.
\]
These are sharper than IV-163's inherited coarse radial estimate \(|F_t|<76.587796\); the angular estimate is essentially unchanged at the displayed precision.

## Status
The calculations are elementary chain-rule consequences of the inherited numerical bounds. They do not independently establish the root domain or derivative bounds on d. This is a component-level refinement only; normalized entropy derivatives and Taylor remainder certification remain open.
