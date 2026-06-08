# Pure-Kernel Monodromy Audit Review

Date: 2026-06-08

Reviewed artifact:

- `tools/run_linear_f3_skew_flip_pure_kernel_monodromy_audit.py`
- `proofs/linear_f3_skew_flip_pure_kernel_monodromy_audit.json`
- `proofs/linear_f3_skew_flip_pure_kernel_monodromy_audit.md`

## Claim Checked

The audit tests the corrected nonsimple minimal-counterexample obstruction:
actual pure detector-kernel monodromy, not formal contextual `J`-collision.
For the six-point linear skew-over-flip degenerate non-involutive family, it
uses the monolith quotient action itself together with the identity-extension
contextual rack.

This detector is stronger than an arbitrary rack detector dominating the
monolith quotient: if pure braids invisible to the quotient action and
contextual rack act trivially on `X`, then pure braids invisible to any rack
detector whose kernel is contained in the quotient kernel also act trivially
in the same tested arity.

## Result

The generated audit reports:

- `64` subdirectly irreducible proper-quotient rows;
- `0` skipped contextual completions;
- `0` two-strand pure detector-kernel X-motion rows;
- exact three-strand closure for the four rows with minimal contextual
  quotient size `|P_X|=42`;
- each three-strand joint image has size `216`;
- `0` three-strand pure detector-kernel X-motion rows;
- `0` three-strand truncations.

## Interpretation

This is evidence against promoting the earlier formal monolith
`J`-collisions into actual small-arity braid witnesses in this family.  It is
not a proof of domination: larger contextual quotients and higher arities are
not exhausted.  It is not a counterexample: the audit found no nontrivial
pure detector-kernel X-motion.

The next theoretical target remains the all-arity statement: in a smallest
nonsimple counterexample, with

```text
Q=(Y_mu x Y_ctx)^0 x T_2,
```

prove that `P_n cap ker rho^Q_n` acts trivially on every monolith fibre, or
construct a fixed finite `X` for which this pure-kernel monodromy congruence
is nontrivial and equals the monolith.
