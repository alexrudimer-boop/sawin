# Fan-only regular-module conjugation detector theorem

The full regular-module framed-cover statement has a Fox-derivative gap:

```text
proofs/regular_module_framed_to_conjugation_cover_theorem.md
```

For Sawin's reduced obstruction, however, the full statement is not needed.
The remaining witnesses are ordinary Brunnian fan words

```text
Br_m subset L_m = ker(P_m -> P_{m-1}) ~= F_{m-1}.
```

On this fan subgroup the regular-module construction gives an unconditional
finite conjugation-rack detector.

## Setup

Let `H` be a finite group.  Let

```text
C_reg(H) = F_2[H] semidirect H,
```

where `H` acts on the left regular module `F_2[H]` by left translation.

Write the fan generators as

```text
y_i = A_{i,m},        1 <= i <= m-1.
```

Thus

```text
L_m ~= F(y_1,...,y_{m-1}).
```

## Theorem

Let `w in L_m` be a fan word.  Suppose there are elements

```text
h_1,...,h_{m-1} in H
```

such that

```text
w(h_1,...,h_{m-1}) != 1.
```

Then the braid `w(A_{1,m},...,A_{m-1,m})` is detected by the conjugation rack
`C_reg(H)^conj`.

Equivalently,

```text
w notin K_m(C_reg(H)^conj).
```

## Proof

Choose meridian labels

```text
g_1,...,g_{m-1} in H
```

so that the effective fan multipliers of the standard Fadell-Neuwirth
generators `A_{i,m}` on the last strand are the prescribed values `h_i`.

Concretely, under the convention used in the Artin-longitude code, these
effective multipliers have triangular form

```text
h_i = (g_{i+1}...g_{m-1})^{-1} g_i (g_{i+1}...g_{m-1}),
```

up to the harmless inverse convention.  This triangular map is bijective:

```text
g_{m-1}=h_{m-1},
g_i=(g_{i+1}...g_{m-1}) h_i (g_{i+1}...g_{m-1})^{-1}.
```

Now label the first `m-1` strands in `C_reg(H)` by

```text
(0,g_i),
```

and label the last strand by

```text
(v,1),
```

where `v in F_2[H]` will be chosen below.

For a fan word, the last strand's group component is conjugated by the
corresponding fan word value

```text
l = w(h_1,...,h_{m-1}) in H.
```

Since the last strand has group component `1`, conjugating `(v,1)` by any lift
`(a,l)` of the longitude gives

```text
(a,l)(v,1)(a,l)^{-1} = (l v, 1).
```

The vector part `a` cancels.  This is exactly why the fan-only theorem avoids
the Fox-derivative gap in the full framed-cover statement.

Because the left regular action of `H` on `F_2[H]` is faithful and `l != 1`,
there exists `v` with

```text
l v != v.
```

For example, take the basis vector `[1]`.

Thus the last coordinate is moved by the braid action on
`C_reg(H)^m`.  Therefore

```text
w notin K_m(C_reg(H)^conj).
```

The theorem is proved.

## Consequence: finite-group envelope from finite fan evaluators

Suppose finite groups

```text
H_1,...,H_s
```

have the property that every `X`-visible Brunnian fan word has a nonidentity
evaluation in at least one `H_i`.

Set

```text
C_X = C_reg(H_1) x ... x C_reg(H_s).
```

Then

```text
Br_m cap K_m(C_X^conj) subset K_m(X)
qquad for every m.
```

Indeed, if `eta in Br_m` is `X`-visible, then it is a fan word with a
nonidentity evaluation in some `H_i`, hence is detected by
`C_reg(H_i)^conj` by the theorem.

By the pointed-Brunnian detector reduction, the finite conjugation rack

```text
C_2^conj x C_X^conj
```

dominates `X`.

Thus the finite-group route now needs only the Uniform Framed Fan-Envelope
Theorem: finitely many finite groups must separate all `X`-visible Brunnian fan
words.

The full framed-cover lemma remains interesting, but it is not required for
the final Brunnian fan reduction.
