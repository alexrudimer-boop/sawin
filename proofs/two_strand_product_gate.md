# Two-strand product gate

Date: 2026-05-28

This note records a symbolic closure property for the direct symmetric
detector route.  It is not a proof of the all-`n` theorem, but it rules out a
large class of possible two-strand counterexamples to the shortcut
`Y_X=A_{Sym(X)}`.

## Statement

Let `X` and `Y` be finite bijective YBE solutions, and let `X x Y` be their
Cartesian product solution:

```text
R_{X x Y}((x,y),(x',y')) =
  ((u,v),(u',v'))
```

where

```text
R_X(x,x')=(u,u'),   R_Y(y,y')=(v,v').
```

If `X` and `Y` pass the direct symmetric two-strand gate, then `X x Y` also
passes it.

Equivalently, if

```text
ord(R_X) divides 2*lcm(1,...,|X|)
ord(R_Y) divides 2*lcm(1,...,|Y|)
```

then

```text
ord(R_{X x Y}) divides 2*lcm(1,...,|X||Y|).
```

## Proof

The two-strand crossing action of the product solution is the Cartesian
product of the two crossing permutations.  Therefore

```text
ord(R_{X x Y}) = lcm(ord(R_X), ord(R_Y)).
```

Let

```text
L_m = lcm(1,...,m).
```

If `m=|X|` and `r=|Y|`, then both `L_m` and `L_r` divide `L_{mr}`, because
every integer at most `m` or at most `r` is also at most `mr`.  Thus

```text
lcm(2 L_m, 2 L_r) divides 2 L_{mr}.
```

Since `ord(R_X)` divides `2L_m` and `ord(R_Y)` divides `2L_r`, their least
common multiple divides `2L_{mr}`.  This proves the product gate.

## Consequence

A first two-strand failure of the direct `A_{Sym(X)}` route cannot be a
Cartesian product of smaller solutions that already pass the gate.  It must
come from a genuinely indecomposable crossing-order phenomenon, or from a
factor that already fails the gate.

The helper

```text
two_strand_product_gate_summary(X,Y)
```

records the factor crossing orders, product crossing order, and symmetric
longitude period for audits.  The regression test combines a three-point rack
with a two-point permutation solution and verifies the product gate.

This lemma is only about `B_2`.  The all-`n` direct symmetric detector target
still requires a global factorization through `W_{Sym(X)}(n)`.
