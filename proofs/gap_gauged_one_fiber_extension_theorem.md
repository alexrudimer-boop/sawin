# Gap-Gauged One-Fibre Extension Theorem

Date: 2026-06-08

This note records the reusable all-arity theorem abstracted from the
six-point `F_3` passive, twisted-passive, active-automorphic, and
signed-affine fibre gauges.

## Setup

Let `X` be a finite bijective YBE solution with a braided quotient

```text
pi:X -> Z.
```

Assume `Z` has one distinguished point `*`, and all fibres of `pi` are
singletons except the fibre over `*`.  Write

```text
X = V union ({*} x W),
V = Z \ {*},
```

and write elements of the nontrivial fibre as `*_i`, with `i in W`.

Assume the quotient and lift have the following form.

For visible-visible crossings,

```text
R_X(z,w)=R_Z(z,w) in V x V        (z,w in V).
```

For fibre-fibre crossings,

```text
R_X(*_i,*_j)=(*_{i'},*_{j'})
```

where

```text
R_W(i,j)=(i',j')
```

for a finite bijective YBE solution `W`.

For visible-fibre crossings,

```text
R_Z(z,*)=(*, alpha(z)),
R_X(z,*_i)=(*_{S_z(i)}, alpha(z)),
```

and

```text
R_Z(*,z)=(beta(z), *),
R_X(*_i,z)=(beta(z), *_{T_z(i)}),
```

where `alpha,beta:V -> V` are mutually inverse permutations and
`S_z,T_z in Sym(W)`.

Assume the following finite identities.

First,

```text
beta = alpha^{-1}.
```

Second, tracked crossing cancellation:

```text
S_{beta(z)} T_z = id_W                 for every z in V.
```

Third, visible-visible gap coherence: for every integer `d` and every
visible-visible quotient crossing

```text
R_Z(z,w)=(u,v),
```

one has

```text
S_{alpha^d(z)} S_{alpha^d(w)}
  =
S_{alpha^d(u)} S_{alpha^d(v)}.
```

Since `V` is finite, it is enough to check `d` modulo the order of `alpha`.

Fourth, fibre-fibre gauge compatibility.  Let

```text
G_alpha =
< (S_{alpha^d(z)}, S_{alpha^{d+1}(z)}) :
    z in V, d in Z >
<= Sym(W) x Sym(W).
```

For every `(A,B) in G_alpha`, require

```text
R_W(Ai,Bj)=(Ai',Bj') whenever R_W(i,j)=(i',j').
```

Equivalently, every `(A,B)` in `G_alpha` is a two-sided gauge symmetry of
the internal fibre solution `W`.

Composition is read with the standard function convention:

```text
S_a S_b(i) = S_a(S_b(i)).
```

Thus, when the visible labels to the left of a tracked `*`-slot are listed
from left to right as `z_1,...,z_k`, the nearest visible label `z_k` acts
first on the hidden fibre.  Equivalently, one may use a right-action
convention, but then all displayed products must be reversed consistently.

## Theorem

If `Z` is dominated by a finite rack `Y_Z`, and `W` is dominated by a finite
rack `Y_W`, then `X` is dominated by

```text
Y_Z x Y_W^0,
```

where `Y_W^0` is the transparent extension of `Y_W`.  That is,

```text
ker rho^{Y_Z x Y_W^0}_n <= ker rho^X_n
```

for every `n`.

## Proof

Fix a word

```text
x = (x_1,...,x_n) in X^n.
```

Project it to `Z^n`.  Let the `*`-positions in the quotient word be

```text
p_1 < ... < p_m.
```

Write the hidden fibre at `p_s` as `i_s in W`.  The proof tracks current
quotient `*`-slots and their hidden coordinates; it does not require a
separate physical-strand labelling of identical `*` quotient letters.

For the `s`-th current `*`-slot, list all visible letters to its left:

```text
z_1,...,z_k.
```

For such a visible letter `z_r`, let

```text
g_r =
number of *-letters strictly between z_r and the tracked *-slot.
```

Define the effective visible label

```text
tilde z_r = alpha^{g_r}(z_r),
```

the gauge

```text
G_s = S_{tilde z_1} S_{tilde z_2} ... S_{tilde z_k},
```

and the gauged hidden value

```text
tilde i_s = G_s(i_s).
```

The gauged hidden word is

```text
tilde i = (tilde i_1,...,tilde i_m) in W^m.
```

We check positive braid generators.  Since all actions involved are
bijections, the corresponding inverse-generator statements follow by
inverting the same equivariance relation.

First, suppose a visible-`*` crossing involves the tracked `*`-slot.  If

```text
z *_i -> *_{S_z(i)} alpha(z),
```

then `z` is removed from the tracked slot's left list, while the hidden
coordinate changes by `i -> S_z(i)`.  The gauged hidden value is unchanged.

If

```text
*_i z -> beta(z) *_{T_z(i)},
```

then `beta(z)` is added immediately to the left list, so the new gauge gains
the factor `S_{beta(z)}`.  The hidden coordinate changes by `T_z`, and

```text
S_{beta(z)} T_z = id_W.
```

Again the gauged hidden value is unchanged.

Second, suppose a visible letter crosses a different `*`-slot to the left of
the tracked slot.  If

```text
z * -> * alpha(z),
```

then the visible label changes from `z` to `alpha(z)` and the gap count to
the tracked slot decreases by one.  Thus

```text
alpha^{g-1}(alpha(z)) = alpha^g(z).
```

If

```text
* z -> beta(z) *,
```

then the visible label changes to `beta(z)=alpha^{-1}(z)` and the gap count
increases by one.  Thus

```text
alpha^{g+1}(beta(z)) = alpha^g(z).
```

So every effective visible label `alpha^g(z)` is unchanged.

Third, suppose two adjacent visible letters to the left of the tracked slot
cross as

```text
R_Z(z,w)=(u,v).
```

They have the same gap count `d` relative to the tracked slot.  Their gauge
contribution changes from

```text
S_{alpha^d(z)} S_{alpha^d(w)}
```

to

```text
S_{alpha^d(u)} S_{alpha^d(v)},
```

which is equal by visible-visible gap coherence.

Fourth, suppose two adjacent `*`-slots cross.  There is no visible letter
between them.  If the left slot has gauge `A`, then the right slot has gauge
`B` such that `(A,B) in G_alpha`: each visible label to their left contributes
one generator pair

```text
(S_{alpha^d(z)}, S_{alpha^{d+1}(z)}),
```

and the full pair of gauge products is their product in `Sym(W) x Sym(W)`.

If

```text
R_W(i,j)=(i',j'),
```

then fibre-fibre gauge compatibility gives

```text
R_W(Ai,Bj)=(Ai',Bj').
```

Thus the gauged adjacent pair transforms exactly by the `W` braid action.

Consequently, the `X` braid action decomposes into quotient motion on `Z^n`
and ordinary `W` braid motion on the gauged `*`-subword.

Now let

```text
beta_braid in ker rho^{Y_Z x Y_W^0}_n.
```

Since `Y_Z` dominates `Z`,

```text
rho^Z_n(beta_braid) pi^n(x) = pi^n(x).
```

So the quotient word returns to itself.

Since `Y_W^0` is transparent, assigning transparent colour to visible
positions and `Y_W` colours to the `*`-positions realizes the deleted
`*`-subword braid action on the nontransparent colours.  Because
`beta_braid` lies in the `Y_W^0` kernel, the induced action on the
`Y_W`-coloured `*`-subword is trivial.  Since `Y_W` dominates `W`, the
gauged hidden word `tilde i` returns to itself.

The quotient word also returns to itself, so every current `*`-slot has the
same final visible left list and the same final gap counts as initially.
Therefore each gauge map `G_s` is the same at the end as at the beginning.
Since every `G_s` is a bijection of `W`,

```text
G_s(i_s')=G_s(i_s)  =>  i_s'=i_s.
```

All visible fibres are singletons.  Hence

```text
rho^X_n(beta_braid)(x)=x.
```

Since `x` was arbitrary,

```text
beta_braid in ker rho^X_n.
```

This proves

```text
ker rho^{Y_Z x Y_W^0}_n <= ker rho^X_n
```

for every `n`.

## Use

This theorem packages the finite local identities behind the six-point `F_3`
gap-corrected closures.  It applies whenever a one-fibre extension has
finite gap-coherent visible transport and the internal fibre solution is
already rack-dominated.

It does not cover:

- one-fibre extensions where one of the finite gap-gauge identities fails;
- multiple interacting nonsingleton fibres;
- cases where the visible transport cannot be represented by a single
  `alpha`-gap action.

Those are the remaining extension types for which this gauge theorem gives
no direct positive branch.
