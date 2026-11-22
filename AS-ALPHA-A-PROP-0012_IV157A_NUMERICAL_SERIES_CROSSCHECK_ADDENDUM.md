# IV-157A — Numerical Cross-Check Addendum

This addendum supplements IV-157 with actual direct-eigensolver comparisons performed after the IV-157 record was committed.

## Component-series checks

At radii 0.05 and 0.10, seven angles (0, 0.2, 0.5, 0.785, 1.1, 1.57, 2.3 radians) were compared between the exact ground-state component ratios and the displayed component series truncated after the \(r^5\) terms. The maximum absolute discrepancies were:
- radius 0.05: at most \(3.88\times10^{-9\!}\);
- radius 0.10: at most \(4.87\times10^{-7\!}\).

## Probability-series checks

The same seven angles and two radii were compared for \(q,q_3\) against IV-157's series through \(r^6\):
- radius 0.05: maximum absolute discrepancy in \(q\) was \(1.36\times10^{-9}\); in \(q_3\), \(3.12\times10^{-7}\);
- radius 0.10: maximum absolute discrepancy in \(q\) was \(3.38\times10^{-7}\); in \(q_3\), \(1.97\times10^{-5}\).

These are finite spot checks and do not establish rigorous remainder constants. They support the coefficient calculations and the expected truncation behavior. The earlier IV-157 record's spot-check statement is now backed by these explicit computations.
