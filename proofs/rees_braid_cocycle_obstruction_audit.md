# Rees braid-cocycle obstruction audit

Date: 2026-06-03

This generated audit records the smallest finite pattern currently
suggested by the Rees-flatness pressure test.  It is not claimed to
be an actual finite bijective YBE solution.  It is a finite local
quotient-row pattern that satisfies the braid relation while keeping
a nontrivial Rees rectangle cocycle.

The group is `C2`, written additively as `0` for the identity and
`1` for the nonidentity element.

## Rees Rectangle

The sandwich matrix is

```text
          i0  i1
lambda0   0   0
lambda1   0   1
```

- distinguished rectangle omega: `1`;
- rectangle failure count: `4`;
- coboundary failure count: `1`;
- rectangle cocycles are trivial: `False`;
- sandwich is row-column coboundary: `False`;
- is flat: `False`.

## Labeled Braid Rows

States are `q00, q01, q10, q11`.  The two quotient rows are

```text
q        q00  q01  q10  q11
s1(q)    q10  q11  q01  q00
ell1(q)  0    0    0    1
s2(q)    q01  q10  q11  q00
ell2(q)  0    0    1    0
```

A row `(s, ell)` acts on `Omega x C2` by

```text
(q,g) |-> (s(q), g + ell(q)).
```

- quotient braid relation holds: `True`;
- labeled braid relation holds: `True`;
- beta word: `(1, 1, 2, 2, -1, -1, -2, -2)`;
- beta is quotient-closed: `True`;
- beta distinct labels: `(1,)`;
- beta constant label: `1`;
- verifies closed nontrivial braid holonomy: `True`.

The beta state images are:

```text
q00 -> (q00, 1)
q01 -> (q01, 1)
q10 -> (q10, 1)
q11 -> (q11, 1)
```

## Consequence

The local braid/YBE relation only checks a braid cocycle identity
for the labels.  This audit shows that such an identity can hold
while the Rees rectangle cocycle is still nontrivial.  Therefore
a positive finite-rack-domination route needs an additional
realization or flatness lemma: actual finite bijective YBE local
quotient-fibre intervals must either avoid this pattern or force
it into a bounded vertical coboundary.

## Direct Locality Shadow

A literal three-strand set-theoretic action has coordinate-local
partitions: `sigma1` preserves the third-coordinate fibres, and
`sigma2` preserves the first-coordinate fibres.  The locality
shadow audit asks whether the two quotient rows have nontrivial
fixed partitions which jointly separate the four states.

For a direct `2 x 2` coordinate model, the control audit records:

- direct coordinate shadow possible: `True`;
- jointly separating fixed pair count: `1`.

For the nonflat obstruction rows, the locality audit records:

- row 1 cycle lengths: `(4,)`;
- row 2 cycle lengths: `(4,)`;
- row 1 has a nontrivial fixed partition: `False`;
- row 2 has a nontrivial fixed partition: `False`;
- direct coordinate shadow possible: `False`.

Thus this four-state obstruction cannot be used as a literal
visible coordinate-local quotient for a three-strand YBE action.
A genuine realization would have to occur deeper inside a
quotient-fibre interval where the outside-coordinate partitions
have already been collapsed or transported.

## Adjacent Two-Body Search

A still stronger direct-realization check asks whether there is a
single bijection `R: A^2 -> A^2`, with `|A|=2`, and an embedding
of the four quotient states into `A^3`, such that `R` on adjacent
coordinates induces both rows.  This search is exhaustive for
two-element `A`.

- without requiring global YBE for `R`, realization found: `False`;
- pair bijections checked: `24` of `24`;
- embeddings checked: `40320` total (`1680` candidates per pair map);
- requiring `R` to satisfy YBE on all of `A^3`, realization found: `False`.

Thus the four-state pattern is not directly induced by any
two-element adjacent binary bijection, even before imposing YBE
on that binary map.  This again pushes any possible realization
into a more hidden quotient-fibre interval.
