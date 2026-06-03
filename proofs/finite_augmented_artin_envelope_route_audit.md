# Finite augmented Artin-envelope route audit

Date: 2026-06-03

This generated audit records the corrected point-pushing route.
It is a symbolic checklist, not a proof of the missing lemma.
The finite rack side supplies an operator-label Hurwitz quotient
with bounded-exponent vertical kernel; the route now asks whether
every finite bijective YBE point-pushing tower has the same form.

## Route flags

- rack operator-label exact sequence recorded: `True`;
- rack vertical-kernel bound recorded: `True`;
- whole point-pushing exponent bound rejected: `True`;
- domination transfers marked point-pushing quotients: `True`;
- obstruction must defeat every fixed group-Hurwitz base: `True`;
- bounded vertical extension is the live invariant: `True`;
- records route-(1) pressure test: `True`.

## Remaining lemmas

- `finite augmented Artin-envelope lemma`;
- `finite rack realization of compatible augmented Artin-envelope towers`.

## First obstruction-prefix generators

The first finite pressure test is at point-pushing arities `3` and `4`.
The standard generator rows are:

- `alpha_{1,4}` in `K_3`: `(3, 2, 1, 1, -2, -3)`.
- `alpha_{2,4}` in `K_3`: `(3, 2, 2, -3)`.
- `alpha_{3,4}` in `K_3`: `(3, 3)`.
- `alpha_{1,5}` in `K_4`: `(4, 3, 2, 1, 1, -2, -3, -4)`.
- `alpha_{2,5}` in `K_4`: `(4, 3, 2, 2, -3, -4)`.
- `alpha_{3,5}` in `K_4`: `(4, 3, 3, -4)`.
- `alpha_{4,5}` in `K_4`: `(4, 4)`.

## Meaning

A counterexample to the finite augmented Artin-envelope lemma
cannot be just unbounded order in `Q_X(n)`.  It must show that
no fixed finite pair `(H,C)` and no fixed exponent bound `e`
can produce compatible normal subgroups `V_X(n)` with
`exp V_X(n) | e` and `Q_X(n)/V_X(n)` a marked quotient of
the corresponding group-Hurwitz point-pushing tower.
