# Linear F3 Residual Representative Closure Audit

This generated audit checks the displayed six-point residual
representative closed by the quotient-and-alternating-sum invariant.

## Summary

- degenerate non-involutive row index: `20`;
- matrix indices: `[5, 26, 4, 12]`;
- YBE: `True`;
- nondegenerate: `False`;
- involutive: `False`;
- monolith blocks: `[[0], [1], [2], [3, 4, 5]]`;
- quotient size: `4`;
- quotient left-nondegenerate: `True`;
- local rule failures: `0`;
- invariant checked moves through arity `6`: `537480`;
- invariant failure count: `0`;
- all claimed checks passed: `True`.

## Consequence

The executable audit verifies the finite bookkeeping behind the
all-arity proof note: the monolith collapses the three `f_i` points,
the four-point quotient is left-nondegenerate, and the stated
alternating-sum quantity is preserved by positive and negative local
crossings in all tested arities.  The symbolic proof gives the
all-arity kernel inclusion.
