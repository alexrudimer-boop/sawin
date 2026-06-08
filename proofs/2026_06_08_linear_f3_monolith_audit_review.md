# Review: Linear F3 Skew-Over-Flip Monolith Audit

Date: 2026-06-08.

## Verdict

The six-point linear skew-over-flip degenerate non-involutive family has now
been tested against the monolith part of the minimal-counterexample criterion.

This is finite evidence only.  It does not prove A or B.  It shows that the
first six-point structured degenerate family is not made of braided-simple
rows, and that formal monolith `J`-collisions occur in some, but not all,
subdirectly irreducible rows.

## Generated Audit

```text
tools/run_linear_f3_skew_flip_monolith_audit.py
proofs/linear_f3_skew_flip_monolith_audit.json
proofs/linear_f3_skew_flip_monolith_audit.md
```

The audit checks the 144 degenerate non-involutive rows in the family

```text
X={0,1} x F_3,
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T = M_ab (i,j)^T.
```

It enumerates braided congruences, computes the monolith when the row is
subdirectly irreducible, and applies the finite relative contextual separation
graph to that monolith.

## Results

```text
rows checked = 144
braided-simple rows = 0
subdirectly irreducible rows = 64
monolith J-separating rows = 32
monolith J-collision rows = 32
monolith check skips = 0
collision mismatch-generation failures = 0
```

For rows with formal monolith collisions, the mismatch pairs in the finite
path are checked to generate the monolith as a braided congruence.

## Interpretation

The six-point degenerate linear family does not currently supply a B
counterexample:

```text
1. no row is braided-simple;
2. rows with monolith J-collisions still lack actual Brunnian or pure
   detector-kernel monodromy witnesses;
3. rows with monolith J-separation cannot be nonsimple minimal
   counterexamples via this monolith route.
```

The next target is the stronger pure-kernel monodromy congruence, not formal
`J`-collision alone.
