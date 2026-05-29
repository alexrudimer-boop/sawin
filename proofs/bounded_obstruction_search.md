# Bounded obstruction search

Date: 2026-05-28

This note records the current bounded candidate-search harness.  It is useful
for finding and debugging local obstruction candidates, but it is explicitly
not a finite-search proof or counterexample.

## Local table to quotient map

`solution_from_local_interval(interval)` realizes a coloured local table as a
finite braided-set quotient map:

```text
total point = (colour, fibre point),
pi(colour, fibre point) = colour.
```

The total braiding is induced by the base table and the local maps
`T_{a,b}`.  Tests verify that the realized total solution satisfies YBE when
the local interval satisfies the coloured YBE, and that the quotient map is a
braided-set homomorphism.

## Visibility profile

`bounded_local_obstructions(...)` searches a bounded list of braid words for
words that:

1. lie in the supplied base-detector kernel;
2. move the local residual fibre action;
3. have identity recursive Artin-longitude signature for every finite group in
   a supplied finite test list.

Such a word is only a bounded candidate.  A final counterexample B would need
a symbolic sequence `beta_j in B_{q_j}`, `q_j -> infinity`, such that for
every finite group `G`, not merely every group in a test list,

```text
Lambda_{G,q_j}(beta_j) = Lambda_{G,q_j}(1)
```

eventually, while the fixed finite YBE solution still moves explicit tuples.

## Demo scan

`tools/run_bounded_obstruction_scan.py` scans a one-colour two-point
permutation-rack interval.  The trivial group misses `sigma_1^2`, but adding
small nontrivial test groups already sees the pure braid longitude.  This is a
sanity check for the harness, not evidence for a counterexample.

The generated report is `proofs/bounded_obstruction_scan.json`.

