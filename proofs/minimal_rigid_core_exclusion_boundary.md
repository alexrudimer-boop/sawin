# Minimal Rigid-Core Exclusion Boundary

Status: boundary theorem, not a proof of Sawin and not a finite counterexample.

This generated note records the Pro response to the minimal rigid-core
prompt.  It does not claim a proof of Sawin's problem.  It isolates
the strict theorem that would now close the existing proof strategy,
and the exact extra property a finite counterexample would need.

## Strict Smaller Theorem

Name: `Minimal rigid-core exclusion`.

No finite bijective set-theoretic YBE solution satisfies all rigid-core conditions.

A rigid core is a finite bijective YBE solution satisfying all of:

- left and right degenerate;
- non-involutive;
- not a rack and not braid-kernel equivalent to a finite rack through a finite total sequential gauge;
- no nontrivial total YBE quotient congruence;
- no nonempty proper crossing-closed subsolution;
- no nonconstant one-state invariant observer;
- not a flip-across or twisted union of proper dominated pieces;
- no proper active-factor certificate into racks or strictly smaller already dominated YBE solutions, even with optional invariant observer channels;

## Why It Implies Sawin-Positive

Hypothesis: `Minimal rigid-core exclusion plus existing positive branches`.

Conclusion: `Every finite bijective YBE solution is dominated by a finite rack`.

Choose a counterexample of minimal cardinality.  Each terminal branch or proper quotient/active-factor mechanism gives a rack domination certificate by known closure theorems and minimality.  Therefore a minimal counterexample would be a rigid core, contradicting exclusion.

The terminal or proper-factor branches used in the minimality
argument are:

- left- or right-nondegenerate solutions via the derived/guitar rack;
- involutive solutions via the two-point flip rack;
- flip-across unions of smaller dominated pieces via product racks;
- point-separating families of proper total YBE quotients, whose quotients are dominated by minimality;
- proper active-factor certificates into racks and smaller already dominated YBE solutions;
- explicit finite sequential rack gauges or all-arity rack conjugacies;

## Genuine Negative Target

A genuine Sawin-negative table must be a rigid core and must satisfy cofinal rack-prefix nonseparation.

For an enumeration of finite racks, set:

- rack prefix: `P_m = Y_1 x ... x Y_m for an enumeration of finite racks`;
- joint image: `Gamma_{m,n}(X)=< (rho^{P_m}_n(sigma_i), rho^X_n(sigma_i)) : 1 <= i < n >`;
- detector-kernel image: `N_{m,n}(X)={g_X : (1,g_X) in Gamma_{m,n}(X)}`;
- cofinal obstruction: `for all m there exists n with N_{m,n}(X) != 1`.

Thus a table that merely survives current certificates is not yet
Sawin-negative.  It must also have nontrivial rack-prefix pressure
cofinally in the rack enumeration.

## Falsifiable Finite-Table Checks

- YBE and bijectivity;
- left- and right-degeneracy;
- non-involutivity;
- quotient-rigidity by congruence enumeration;
- absence of nonempty proper crossing-closed subsolutions;
- observer-rigidity via the row-output connectivity graph;
- absence of flip-across decompositions;
- absence of currently recognized transport-split, monodromy, or proper active-factor certificates;
- real rack-prefix pressure N_{m,n}(X) != 1 for a small rack prefix;

## Current Known Status

- No proof of minimal rigid-core exclusion is recorded.
- No finite table with cofinal rack-prefix obstruction is recorded.
- The affine F_2^3 q=3 pressure row is already resolved positively by all-arity kernel equality with the tetrahedral four-element rack.
- Future negative evidence must show cofinal rack-prefix pressure, not merely pressure against a bounded rack prefix.

## Conclusion

The current exact endpoint is: prove minimal rigid-core exclusion, or find a rigid core and then prove the cofinal nontriviality of N_{m,n}(X).
