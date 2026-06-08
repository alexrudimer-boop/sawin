# Linear F3 Pure-Kernel Monodromy Audit

This generated audit tests the corrected monolith obstruction against
actual pure detector-kernel monodromy in the 144 degenerate
non-involutive six-point linear skew-over-flip rows.

The detector used for the audit is stronger than the abstract detector
in the minimal-counterexample theorem: it is the monolith quotient
action itself, together with the identity-extension contextual rack.
Therefore triviality here is evidence against actual pure-kernel
monodromy in these finite test cases, while a nontrivial element would
only be a candidate for a rack-detector witness.

## Summary

- subdirect rows audited: `64`;
- skipped contextual completions: `0`;
- two-strand pure detector-kernel X-motion count: `0`;
- three-strand rows audited: `4` (minimal contextual class count `42`);
- three-strand pure detector-kernel X-motion count: `0`;
- three-strand truncations: `0`;
- all claimed checks passed: `True`.

## Three-Strand Exact Closures

| row | matrices | P classes | joint image | kernel X-motion | truncated |
|---:|---|---:|---:|---|---|
| 105 | [12, 20, 2, 44] | 42 | 216 | False | False |
| 113 | [12, 38, 1, 44] | 42 | 216 | False | False |
| 133 | [44, 1, 38, 12] | 42 | 216 | False | False |
| 134 | [44, 2, 20, 12] | 42 | 216 | False | False |

## Distribution

| cases | P classes | monolith block sizes |
|---:|---:|---|
| 4 | 42 | [1, 1, 1, 3] |
| 4 | 48 | [1, 1, 1, 3] |
| 4 | 54 | [1, 1, 1, 3] |
| 12 | 60 | [1, 1, 1, 3] |
| 4 | 72 | [1, 1, 1, 3] |
| 4 | 78 | [1, 1, 1, 3] |
| 8 | 84 | [1, 1, 1, 3] |
| 4 | 90 | [1, 1, 1, 3] |
| 20 | 108 | [1, 1, 1, 3] |

## Consequence

All 64 subdirectly irreducible proper-quotient rows have trivial
two-strand pure kernel against the monolith quotient plus contextual
rack detector.  The four smallest contextual quotients also have exact
three-strand joint image size 216 and no detector-kernel X-motion.

This does not prove domination.  It narrows the current obstruction:
the formal monolith contextual collisions seen earlier are not
automatically realized by small-arity pure detector-kernel monodromy
in this six-point family.
