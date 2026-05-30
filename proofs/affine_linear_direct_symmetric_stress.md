# Affine-linear direct-symmetric stress

Date: 2026-05-30

This note records larger affine-linear stress data for the direct

```text
G_X = Sym(X)
```

candidate.  It is not proof evidence for arbitrary finite YBE solutions and
it is not a route to outcome B.  The two-strand cyclic detector theorem already
shows that two-strand failures can refute a proposed detector but cannot, by
themselves, defeat every finite rack.

## Direct-symmetric two-strand gate

For a finite solution `X`, the direct symmetric detector must pass the exact
two-strand divisibility condition

```text
ord(R_X) divides 2 lcm(1,...,|X|).
```

The following reported affine-linear stress rows found no violation of this
condition.

## Affine-linear maps on F_2^3

For affine-linear YBE solutions on `F_2^3`, so `|X|=8`, the reported scan had:

```text
linear invertible YBE blocks: 26153
affine YBE maps: 226241
bad direct-Sym two-strand rows: 0
```

The direct symmetric invisible period is

```text
2 lcm(1,...,8) = 1680.
```

The crossing-order histogram was:

```text
1: 1
2: 23744
3: 14784
4: 149408
6: 10080
7: 5376
8: 13440
12: 6720
14: 2688
```

Every listed crossing order divides `1680`.

## Affine-linear maps on F_3^2

For affine-linear YBE solutions on `F_3^2`, so `|X|=9`, the reported scan had:

```text
linear invertible YBE blocks: 144
affine YBE maps: 912
bad direct-Sym two-strand rows: 0
```

The direct symmetric invisible period is

```text
2 lcm(1,...,9) = 5040.
```

The crossing-order histogram was:

```text
4: 144
8: 432
10: 48
12: 288
```

Every listed crossing order divides `5040`.

## Consequence

These data reinforce the existing two-strand guardrail:

1. no two-strand obstruction to the direct `Sym(X)` route appears in these
   affine-linear families;
2. even if such a two-strand obstruction appeared, it would not be outcome B,
   because a cyclic detector of order `ord(R_X)` sees the two-strand action;
3. the actual unresolved obstruction remains all-`n` terminal gauge/unit
   longitudinalization in the bi-free universal-corridor branch.

The stress rows should therefore be read only as search guidance.  They do
not replace the terminal gauge Artin-defect lemma or a normalized-law
counterexample.
