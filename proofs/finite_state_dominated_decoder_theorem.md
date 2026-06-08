# Finite-State Dominated-Decoder Theorem

Date: 2026-06-08

This note records the finite-state dominated-decoder abstraction.  It is a
general all-arity positive mechanism: a finite solution `X` is dominated if
it has a dominated quotient plus a braid-equivariant dominated readout that
jointly decodes every `X^n`.

The theorem is deliberately stated with an arbitrary dominated readout
solution `U`.  This includes the gap-gauged one-fiber theorem by taking `U`
to be a transparent extension of the internal fiber solution, so visible
positions map to the transparent color and fiber positions map to gauged
hidden values.

For clarity, if `W` is a finite bijective YBE solution, its transparent
extension `W^0` means `W sqcup {0}` with the old `R_W` on `W x W` and

```text
R(0,a)=(a,0),
R(a,0)=(0,a),
R(0,0)=(0,0).
```

This is again a finite bijective YBE solution.  If a finite rack `Y_W`
dominates `W`, then the rack transparent extension `Y_W^0` dominates this
YBE transparent extension `W^0`: a braid trivial on `(Y_W^0)^n` preserves each
nontransparent support set and acts trivially on the induced `Y_W` subword;
therefore it acts trivially on the corresponding `W` subword.

## Decoder Theorem

Let `X` be a finite bijective YBE solution.  Assume:

```text
pi:X -> Z
```

is a braided quotient, and `U` is another finite bijective YBE solution.
Assume `Z` and `U` are finite-rack dominated by racks `Y_Z` and `Y_U`:

```text
ker rho^{Y_Z}_n <= ker rho^Z_n,
ker rho^{Y_U}_n <= ker rho^U_n
```

for every `n`.

Suppose there are maps

```text
Gamma_n:X^n -> U^n
```

for every `n`, satisfying braid equivariance:

```text
Gamma_n(rho^X_n(beta)(x))
  =
rho^U_n(beta)(Gamma_n(x))
```

for all `n`, all `beta in B_n`, and all `x in X^n`.

Suppose also that the combined decoder

```text
D_n:X^n -> Z^n x U^n,
D_n(x)=(pi^n(x), Gamma_n(x))
```

is injective for every `n`.

Then

```text
Y_Z x Y_U
```

dominates `X`:

```text
ker rho^{Y_Z x Y_U}_n <= ker rho^X_n
```

for every `n`.

### Proof

Let

```text
beta in ker rho^{Y_Z x Y_U}_n.
```

Then `beta` is in both rack-detector kernels.  Since `Y_Z` dominates `Z`
and `Y_U` dominates `U`,

```text
rho^Z_n(beta)=1,
rho^U_n(beta)=1.
```

Fix `x in X^n` and set

```text
x' = rho^X_n(beta)(x).
```

Because `pi` is braided,

```text
pi^n(x') = rho^Z_n(beta)(pi^n(x)) = pi^n(x).
```

Because `Gamma_n` is braid-equivariant,

```text
Gamma_n(x') = rho^U_n(beta)(Gamma_n(x)) = Gamma_n(x).
```

Thus

```text
D_n(x')=D_n(x).
```

By injectivity of `D_n`, `x'=x`.  Since `x` was arbitrary,

```text
beta in ker rho^X_n.
```

This proves the kernel inclusion for every `n`.

## Finite Local Certificate For The Readout

The decoder theorem is useful when `Gamma_n` is built from finite two-sided
context.

Let `L` and `R` be finite monoids, and let

```text
lambda:X -> L,
rho:X -> R
```

be context-update maps.  For a word

```text
x=(x_1,...,x_n),
```

define left contexts

```text
A_1=1_L,
A_{i+1}=A_i lambda(x_i),
```

and right contexts

```text
B_n=1_R,
B_i=B_{i+1} rho(x_{i+1}).
```

Let

```text
gamma:L x X x R -> U
```

be a finite readout, and define

```text
Gamma_n(x)_i = gamma(A_i,x_i,B_i).
```

Assume the context updates satisfy, for every

```text
R_X(x,y)=(u,v),
```

the identities

```text
lambda(x) lambda(y) = lambda(u) lambda(v),
rho(y) rho(x) = rho(v) rho(u).
```

These say that all left and right contexts outside the crossing block are
unchanged.

Assume also the local crossing identity

```text
R_U(
  gamma(A,x,B rho(y)),
  gamma(A lambda(x),y,B)
)
 =
(
  gamma(A,u,B rho(v)),
  gamma(A lambda(u),v,B)
)
```

for every `A in L`, `B in R`, and `x,y in X`.

Then every `Gamma_n` is braid-equivariant:

```text
Gamma_n(rho^X_n(beta)(x))
  =
rho^U_n(beta)(Gamma_n(x))
```

for all `n`, `beta`, and `x`.

### Proof

It is enough to check a positive braid generator.  The corresponding inverse
generator follows because the `X` and `U` braid generators are bijections:
from `Gamma sigma_i^X = sigma_i^U Gamma`, apply the identity to
`(sigma_i^X)^{-1}x` and rearrange.

For a positive crossing, let the adjacent `X`-colors be

```text
x_i=x,
x_{i+1}=y,
R_X(x,y)=(u,v).
```

Write `A` for the left context before `x`, and `B` for the right context
after `y`.  Before the crossing, the two `U` readout colors are

```text
gamma(A,x,B rho(y)),
gamma(A lambda(x),y,B).
```

After the crossing, the two adjacent `X` colors are `u,v`, and the two
readout colors are

```text
gamma(A,u,B rho(v)),
gamma(A lambda(u),v,B).
```

The imposed local identity says precisely that these two pairs are related
by `R_U`.  The context identities ensure all non-adjacent readout positions
have the same left and right contexts before and after the crossing.  Hence
`Gamma_n` intertwines every braid generator, and therefore the whole braid
group action.

## Finite All-Arity Injectivity Test

For a fixed finite local readout, injectivity of

```text
D_n=(pi^n,Gamma_n)
```

for every `n` is equivalent to a finite graph reachability condition.

Build a finite directed graph with vertices

```text
(A,A',B,B',x,x') in L^2 x R^2 x X^2
```

satisfying

```text
pi(x)=pi(x'),
gamma(A,x,B)=gamma(A',x',B').
```

There is an edge

```text
(A,A',B,B',x,x') -> (bar A,bar A',bar B,bar B',y,y')
```

iff

```text
bar A  = A  lambda(x),
bar A' = A' lambda(x'),
B  = bar B  rho(y),
B' = bar B' rho(y').
```

The target tuple must itself be a vertex, so it also satisfies
`pi(y)=pi(y')` and the corresponding readout equality.

Initial vertices have

```text
A=A'=1_L.
```

Terminal vertices have

```text
B=B'=1_R.
```

Then `D_n` fails to be injective for some `n` if and only if this graph has
an initial-to-terminal path containing at least one coordinate mismatch

```text
x_i != x_i'.
```

Equivalently, add a one-bit flag recording whether a mismatch has occurred.
If a collision exists, one exists with

```text
n <= 2 |L|^2 |R|^2 |X|^2.
```

### Proof

A collision in arity `n` gives two words `x,x' in X^n` with equal quotient
and readout coordinates.  Recording the left and right contexts at each
position gives a path in the graph.  The first coordinate has
`A=A'=1_L`, the last coordinate has `B=B'=1_R`, and a genuine collision has
at least one mismatch.

Conversely, an initial-to-terminal path spells two words

```text
(x_1,...,x_n),   (x'_1,...,x'_n)
```

whose contexts obey the defining recursions.  Since every vertex satisfies
the quotient and readout equalities, the two words have the same `D_n`
image.  A flagged mismatch makes them distinct.

The bound follows by deleting loops in the finite flagged graph.

## Consequences

This theorem subsumes several positive mechanisms:

- If the contextual quotient `P_X` has a finite YBE or rack completion, take
  `U=P_X` or that completion and recover the contextual-readout route.
- If a one-fiber gauge produces a hidden readout, take `U` to be the
  transparent extension of the internal fiber solution and recover the
  gap-gauged one-fiber theorem.
- If a multi-fiber or non-coordinatewise construction produces a finite
  dominated readout solution `U`, the theorem gives domination without
  requiring a direct rackification of the contextual quotient.

The remaining positive target is no longer merely "rackify the contextual
partial rack."  It is enough to construct finite data

```text
Z, U, L, R, gamma
```

with `Z` and `U` already dominated, satisfying the local equivariance
identities and the finite all-arity injectivity test.

The corresponding negative target is also sharper: a fixed counterexample
must defeat every such finite-state dominated decoder, and then that failure
still has to be converted into cofinal Brunnian rack-prefix witnesses.
