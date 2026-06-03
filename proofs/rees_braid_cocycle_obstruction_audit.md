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
