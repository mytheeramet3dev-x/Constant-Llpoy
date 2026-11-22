# IV-174 — Corrected Q3 Bounds from Squared Components

## Purpose
Repair the Q3 numerator bounds invalidated by IV-173. This derivation uses the squared components from IV-165 directly, avoiding the incorrect IV-166 unweighted Rz+Rw expression.

## Correct definitions
\[
Q_3=\frac{P_z+P_w}{D},\quad
P_z=16(1-p)G^2H,\quad
P_w=\frac{1024tp(1-p)}{F^2}.
\]
From IV-165, conditional on its inherited spectral/derivative assumptions:
\[
P_z<1.132633,\quad P_w<0.016125,
\]
\[
|(P_z)_t|<25.587618,\quad |(P_w)_t|<1.188821,
\]
\[
|(P_z)_p|<1.211448,\quad |(P_w)_p|<0.032250.
\]
Also \(D\ge1\), \(|D_t|<3.099578\), and \(|D_p|<0.038362\).

## Corrected numerator
Let \(N_3=P_z+P_w\). Then the component bounds give:
\[
N_3<1.148758,\quad |(N_3)_t|<26.776439,\quad |(N_3)_p|<1.243698.
\]

## Quotient bounds
Using \(Q_3=N_3/D\), \(D\ge1\), and the quotient rule:
\[
Q_3<1.148758,
\]
\[
|(Q_3)_t|\le |(N_3)_t|+N_3|D_t|
<26.776439+1.148758(3.099578)
<30.337105,
\]
\[
|(Q_3)_p|\le |(N_3)_p|+N_3|D_p|
<1.243698+1.148758(0.038362)
<1.287767.
\]
These are conservative rounded-up estimates.

## Status
The corrected Q3 upper and first-derivative bounds follow from the listed IV-165 component bounds and normalization bounds. They remain conditional on the inherited IV-165 estimates (including d and its derivatives), which have not yet been fully rederived from the spectral equation in this audit. This note repairs the algebraic Q3 representation and its propagation; it does not rehabilitate the invalid IV-166 Q3 constants.

## Downstream
IV-166's old Q3 estimates \(Q_3<1.197133\), \(|(Q_3)_t|<34.053503\), and \(|(Q_3)_p|<0.189240\) are superseded for this chain. Revisit IV-167 derivative estimates and all IV-168–IV-172 claims that used these bounds. The entropy identities remain exact, but numerical certificates depending on old Q3 bounds must be recalculated.
