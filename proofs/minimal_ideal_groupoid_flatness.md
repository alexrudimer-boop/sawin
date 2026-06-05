# Minimal-Ideal Groupoid Flatness

Date: 2026-06-05

This note sharpens the minimal-ideal transport groupoid route by recording the
part of the Yang-Baxter identities that is already a theorem: finite
semigroup-valued observers and flat transport in the minimal-ideal groupoids.

It also records why this still does not prove Sawin domination.

## Coordinate identities

Write

```text
r(x,y) = (u,v) = (L_x(y), R_y(x)).
```

The first and third coordinate Yang-Baxter identities give

```text
L_u L_v = L_x L_y,                         (L)
```

and

```text
R_v R_u = R_y R_x.                         (R)
```

The second identity is the mixed compatibility condition.  The two displayed
identities are enough to construct finite inert observers.

## Finite semigroup observers

Let

```text
S_L = <L_x : x in X>,       S_R = <R_y : y in X>.
```

For each arity `n`, define

```text
O^L_n(x_1,...,x_n) = L_{x_1} L_{x_2} ... L_{x_n},
```

and

```text
O^R_n(x_1,...,x_n) = R_{x_n} R_{x_{n-1}} ... R_{x_1}.
```

Then both `O^L_n` and `O^R_n` are braid-invariant.

Proof.  It is enough to check a generator `sigma_i`.  If

```text
r(x_i,x_{i+1})=(u,v),
```

then identity `(L)` replaces the adjacent factor

```text
L_{x_i} L_{x_{i+1}}
```

by

```text
L_u L_v
```

without changing the product.  Hence `O^L_n` is fixed.  Similarly, in the
reversed right product the affected adjacent factor is

```text
R_{x_{i+1}} R_{x_i},
```

and identity `(R)` replaces it by

```text
R_v R_u.
```

Thus `O^R_n` is fixed.

These are genuine finite observer channels, but they are global sequential
observers, not one-state point observers.  They do not by themselves separate
`X^n`.

## Minimal-ideal flatness

Let `K_L` be the minimal ideal of `S_L`.  For `s in K_L`, write

```text
Omega_s = im(s).
```

For every generator `L_x`, the restriction

```text
L_x : Omega_s -> Omega_{L_x s}
```

is a bijection, because `s` and `L_x s` have the same minimal rank.

For `r(x,y)=(u,v)`, identity `(L)` gives, for every `s in K_L`,

```text
L_u L_v s = L_x L_y s.
```

Consequently the two transport paths

```text
Omega_s --L_v--> Omega_{L_v s} --L_u--> Omega_{L_u L_v s}
```

and

```text
Omega_s --L_y--> Omega_{L_y s} --L_x--> Omega_{L_x L_y s}
```

have the same target object and the same underlying map

```text
Omega_s -> Omega_{L_x L_y s}.
```

Thus the left minimal-ideal transport groupoid is flat for every local YBE row.

The right minimal-ideal transport groupoid has the dual flatness statement:
for `t in K_R`,

```text
R_v R_u t = R_y R_x t,
```

so the two right transport paths across a local crossing agree.

## Why flatness is not rackification

Flatness gives finite transport and finite inert observers.  It does not yet
give a rack detector.

There are three missing ingredients.

1. **Object observability.**  The transport groupoid tracks maps between
   minimal-rank images.  A point of `X` need not be recoverable from its
   position in any chosen minimal image, and the union of minimal images may be
   all of `X` or may have cross-coordinate escapes.

2. **Coordinate output.**  A rack factor requires a coordinatewise output

   ```text
   omega(q,x) in Y
   ```

   whose adjacent pair transforms by a rack Yang-Baxter map.  A flat groupoid
   gives operator labels, not automatically such rack colours.

3. **All-arity injectivity.**  Sawin domination requires a finite rack `Y` and
   observers `I_n` such that

   ```text
   Phi_n : X^n -> Y^n x I_n
   ```

   is injective and braid-equivariant for every `n`.  The observers
   `O^L_n,O^R_n` are finite and braid-invariant, but they generally have far
   fewer than `|X|^n` possible values.

## The exact next lemma

The minimal-ideal rackification route now reduces to the following proof
obligation.

> Flat groupoid observability lemma.  In an everywhere-singular
> quotient-rigid, subsolution-rigid, observer-rigid finite bijective YBE
> solution, the flat left/right minimal-ideal transport groupoids, together
> with the finite semigroup observers `O^L_n,O^R_n`, either produce a proper
> quotient/subsolution/observer or admit a finite rack output whose product
> with those inert observers separates `X^n` in every arity.

This is the first point at which the route must construct actual rack colours.
Everything before it is finite semigroup flatness rather than domination.

