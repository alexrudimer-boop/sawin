# Finite racks are finite-group longitude quotients

Date: 2026-05-28

This note records the direct reason that a normalized-law sequence whose
Artin longitudes are eventually trivial in every finite group defeats every
finite rack.

## Inner group of a finite rack

Let `Y` be a finite rack with operation `a ▷ b` and braided convention

```text
R_Y(a,b) = (a ▷ b, a).
```

For each `a in Y`, let

```text
L_a(b) = a ▷ b.
```

The rack axioms say that every `L_a` is a bijection and

```text
L_{a▷b} L_a = L_a L_b.
```

Thus the left translations generate a finite permutation group

```text
Inn(Y) = < L_a : a in Y > <= Sym(Y).
```

## Longitude formula

For a braid `beta in B_n`, write its recursive Artin data as

```text
beta(x_i) = L_i(beta) x_{p(i)} L_i(beta)^{-1}.
```

Given a rack tuple `(y_1,...,y_n)`, evaluate each free generator `x_i` in
`Inn(Y)` as the left translation `L_{y_i}`.  Then the `j`-th output coordinate
of the rack braid action is

```text
eval(L_j(beta)) ( y_{p(j)} ).
```

This is proved by induction over braid words.  For the positive generator
`sigma_i`, the recursive longitude update has

```text
L_i' = x_i,      p(i)=i+1,
L_{i+1}' = 1,    p(i+1)=i,
```

so the two affected output coordinates are

```text
L_{y_i}(y_{i+1}) = y_i ▷ y_{i+1},
y_i,
```

which is exactly `R_Y(y_i,y_{i+1})`.  The negative generator follows by using
the inverse permutations in `Inn(Y)`.  Composition is compatible with the
recursive Artin-longitude update, so the formula holds for every braid word.

## Consequence

If

```text
Lambda_{Inn(Y),n}(beta)=Lambda_{Inn(Y),n}(1),
```

then the braid permutation `p` is identity and every recursive longitude
evaluates to the identity permutation of `Y` for every assignment of
generators to elements of `Inn(Y)`.  In particular, this holds for the
assignment `x_i -> L_{y_i}` attached to any rack tuple.  The formula above
therefore gives

```text
rho_{Y,n}(beta)(y_1,...,y_n) = (y_1,...,y_n).
```

Thus every finite rack action is killed by identity finite-group longitude
data in the finite group `Inn(Y)`.

## Use for B

Suppose a proposed finite YBE solution `X` has braids `beta_j in B_{q_j}`
with `q_j -> infinity` such that

```text
Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)
```

eventually for every finite group `G`, but

```text
rho_{X,q_j}(beta_j) != 1.
```

Let `Y` be any finite rack.  Taking `G=Inn(Y)`, the preceding paragraph shows
that `rho_{Y,q_j}(beta_j)=1` for all sufficiently large `j`, while
`rho_{X,q_j}(beta_j) != 1`.  Hence

```text
ker rho_{Y,q_j} not subset ker rho_{X,q_j}
```

for large `j`.  Therefore no finite rack `Y` dominates `X`.

This is the direct rack-action version of the sharp obstruction theorem's
finite-group detector.  It is the final step needed after a B construction
has supplied the explicit normalized-law sequence.

## Executable convention checks

The implementation exposes:

```text
rack_inner_group(Y)
rack_longitude_action(Y,beta,tuple)
```

in `src/ybe_domination/artin_longitudes.py`.  Unit tests verify on the
three-point dihedral rack that `rack_longitude_action` agrees with the direct
braid action for mixed positive and negative braid words, and that longitude
invisibility in `Inn(Y)` kills the finite rack action.
