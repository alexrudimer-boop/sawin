# Symmetric law-separator audit

Date: 2026-05-28

This generated audit targets the B-route obstruction to the direct
`G_X = Sym(X)` detector candidate.  It searches for short free words
that are laws on `Sym(X)` but whose pure-braid embedding moves a tuple
inside a structure orbit of `X^n`.

The check uses `structure_orbit_law_separation()`, so a failure is an
assigned pure-generator mover, not merely non-lawhood in an abstract
orbit image group.  The audit is finite diagnostic evidence only: no
bounded scan proves the all-`n` theorem or outcome B.

## Exhaustive Tiny Scans

- size `2`, n `3`, word length <= `6`: solutions `5`, detector order `2`, failures `0`, truncated orbit total `0`.
- size `2`, n `4`, word length <= `6`: solutions `5`, detector order `2`, failures `0`, truncated orbit total `0`.
- size `3`, n `3`, word length <= `6`: solutions `73`, detector order `6`, failures `0`, truncated orbit total `0`.

## Named Stress Rows

- `dihedral_quandle_3`, n `4`, word length <= `6`: failure `False`, orbit size `None`, target group size `None`, truncated orbits `0`.
- `size3_affine_commutator_candidate`, n `4`, word length <= `6`: failure `False`, orbit size `None`, target group size `None`, truncated orbits `0`.

## Consequence

No short law on the full symmetric detector appears in these rows.
This rules out the first tempting moving-variety obstruction to the
direct `A_{Sym(X)}` route in the size-`2` and size-`3` corpora
checked here.  It also sharpens the B search target: a genuine
normalized-law counterexample must escape the full symmetric
detector for each finite stage, not only small cyclic or abelian
detectors.
