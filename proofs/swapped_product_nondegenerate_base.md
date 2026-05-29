# Swapped Product Over A Nondegenerate Base

Date: 2026-05-28

This note removes one arbitrary-fibre product region from the genuinely
coloured product bottleneck.  It is a symbolic observation, not a finite
search.

## Statement

Let `pi:X -> Z` be a local interval in swapped product form:

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)),
```

where

```text
L_{a,b}:A_b -> A_{a.b},
R_{a,b}:A_a -> A_{a*b}
```

are bijections.  If the quotient colour solution `Z` is left and right
nondegenerate, then the total solution `X` is left and right nondegenerate.
Consequently the interval belongs to the already known
nondegenerate/guitar finite-G-measurable branch, regardless of fibre size and
regardless of coloured product holonomy.

## Proof

Write total points as `(a,x)` with `x in A_a`.  Fix a left input `(a,x)`.
The left coordinate map of the total solution sends

```text
(b,y) |-> (a.b, L_{a,b}(y)).
```

The first component `b |-> a.b` is a bijection of quotient colours because
`Z` is left nondegenerate.  For each `b`, the second component
`L_{a,b}:A_b -> A_{a.b}` is a bijection by the product normal form.  Therefore
the displayed map is a bijection from the disjoint union of all fibres
`A_b` to the disjoint union of all fibres `A_{a.b}`.

Similarly, fix a right input `(b,y)`.  The right coordinate map of the total
solution sends

```text
(a,x) |-> (a*b, R_{a,b}(x)).
```

The colour map `a |-> a*b` is bijective because `Z` is right nondegenerate,
and each `R_{a,b}` is a fibre bijection.  Hence this right coordinate map is
also bijective.  Thus `X` is nondegenerate.

The Lebed-Vendramin guitar/derived-rack branch supplies the finite-G
detector for finite nondegenerate solutions.  Therefore no swapped product
extension over a nondegenerate quotient can be a remaining product-holonomy
obstruction.

## Boundary

The direct product form

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y))
```

does not satisfy the same conclusion: the first output ignores `y` and the
second output ignores `x`, so nondegeneracy generally fails unless the
fibres are singletons.  Direct product branches still need the coboundary,
identity-base, fibre-size-two affine, known-total, or genuinely coloured
product-label routing recorded in the product ledger.
