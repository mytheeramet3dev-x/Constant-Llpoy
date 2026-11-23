# IV-192 — Independent Arithmetic and Dependency Audit of IV-186–IV-191

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Arithmetic audit only; inherited analytic hypotheses are not certified.

## 1. Recomputed key constants
From \(d_*=256/63\), \(t_*=1/64\):
\[
a_*=d_*^2=16.511967750062986,\quad
a_{t,*}=2d_*(4.194)=34.08457142857143,
\]
\[
B_*=a_*^2=272.6450789791201.
\]
IV-187's absolute-value expression gives
\[
B_{t,*}=2a_*a_{t,*}+512t_*+32a_{t,*}t_*+32a_*
=1679.0319421228808,
\]
so its stated upward ceiling \(1679.031943\) is valid.
Then
\[
16(B_{t,*}/3969+B_*\cdot0.002131)
=16.06469090966374,
\]
so IV-187's \(16.064690910\) ceiling is valid. Adding \(1.134551908\) gives \(S_t<17.199242817663738\); \(17.199242818\) is valid.

For IV-188:
\[
B_{p,*}=128a_*t_*=33.02393550012597,
\]
\[
16(1.535\times10^{-6}B_*+B_{p,*}/3969)
=0.1398236431100007.
\]
The ceilings \(33.023936\), \(0.139823644\), and aggregate \(S_p<0.204389644\) are valid.

## 2. Amplitude and denominator arithmetic
IV-186 exact separated amplitude arithmetic:
\[
16a_*/(63/4)^2=1.0650198397621882,
\]
and adding \(P_w<0.016124969\) gives
\[
S<1.0811448087621882,
\]
so \(1.081145\) is a valid upward ceiling.

Correct denominator is \(D=1+tS\). Recalculation:
\[
D<1.016892890625,
\]
\[
|D_t|<1.349883169025996,\quad
|D_p|<0.0031935881735937607.
\]
IV-190's displayed ceilings (\(1.016892890625\), \(1.349883169026\), \(0.003193588188\)) are valid upward ceilings.

## 3. Quotient arithmetic
Using IV-180 input ceilings and \(D\ge1\), direct quotient upper estimates reproduce:
\[
|(Q_u)_t|,|(Q_z)_t|<17.87724122338342,
\]
\[
|(Q_u)_p|,|(Q_z)_p|<2.348837163353822,
\]
\[
|(Q_w)_t|<1.156318824254166,\quad
|(Q_w)_p|<0.06461749651029797.
\]
Their rounded IV-190 ceilings are valid.

For \(Q_3=(P_z+P_w)/D\), the radial numerator ceiling must be the sum of IV-180's component ceilings:
\[
|(P_z+P_w)_t|<16.348319+1.134552=17.482871,
\]
not the earlier \(17.482870918\) entry. Using the corrected ceiling gives
\[
|(Q_3)_t|<19.033560089483963,
\]
hence the corrected upward ceiling \(19.033560090\). The angular quotient calculation reproduces \(2.4134546599631213\), with ceiling \(2.413454660\).

## 4. IV-191 norm ceilings
Recompute from its rounded component inputs:
\[
\|Q_t\|_2<25.30866722454758,\quad
\|Q_p\|_2<3.3223855873546646,
\]
\[
\sqrt{\|Q_t\|_2^2+\|Q_p\|_2^2}<25.525808168870007.
\]
Therefore IV-191 ceilings \(25.308668\), \(3.322387\), and \(25.525810\) are conservative and valid for these rounded inputs.

## 5. Correction committed to IV-190
IV-190's Q3 radial numerator and quotient ceilings corrected to \(17.482871\) and \(19.033560090\). This correction was committed after the initial IV-192 calculation.

## 6. What this audit does NOT verify
This checks arithmetic/ceiling propagation only, not the validity of inherited formula assumptions, implicit root existence/uniqueness, \(R_d\le0\), the domain bounds, differentiability, or a formal proof. It is not an interval-arithmetic proof.
