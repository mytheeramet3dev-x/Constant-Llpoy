# IV-179 — Recomputed Logarithmic Derivative Bounds for H

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional derivative bounds; inherited spectral-domain premises remain unverified.

## 1. Definition and logarithmic derivatives

\[
H=(d^2F^2)^{-1},\qquad F=d^2-16t.
\]
For any variable \(q\in\{t,p\}\), logarithmic differentiation yields
\[
\frac{H_q}{H}=-\frac{2d_q}{d}-\frac{2F_q}{F},
\]
so
\[
|H_q|\le H\left(\frac{2|d_q|}{d}+\frac{2|F_q|}{F}\right).
\]
Under \(d\ge4\), \(F\ge63/4\), we also have
\[
H\le H_*:=\frac{1}{16(63/4)^2}=\frac1{3969}.
\]

## 2. Radial derivative

Use \(|d_t|<4.194\), \(|F_t|<50.084572\):
\[
|H_t|\le\frac1{3969}\left(\frac{2(4.194)}4+
\frac{2(50.084572)}{63/4}\right).
\]
The computed enclosure (rounded upward in this record) is
\[
\boxed{|H_t|<0.002131}.
\]

## 3. Angular derivative

Use \(|d_p|\le1/252\), \(|F_p|\le0.032249938\):
\[
|H_p|\le\frac1{3969}\left(\frac{2(1/252)}4+
\frac{2(0.032249938)}{63/4}\right).
\]
The computed rounded-up enclosure is
\[
\boxed{|H_p|<1.535\times10^{-6}}.
\]

## 4. Scope

This corrects the IV-165 logarithmic derivative estimates using the sharper IV-175/177 derivative bounds. The formulas and numerical substitutions are explicit; the result is still conditional on the inherited spectral branch/domain and derivative assumptions. It does not certify the full squared-component bounds, normalized probabilities, or entropy remainder.
