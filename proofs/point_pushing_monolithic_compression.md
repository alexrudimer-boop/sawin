# Point-Pushing Monolithic Compression

Date: 2026-05-30

This note sharpens the product-prefix failure route again.  A moving
product-prefix relation can always be pushed down to a smallest separating
quotient of the finite action image, and that smallest quotient is monolithic.

It does not prove outcome A or B.  It says that a genuine B tail must produce
unbounded critical monolithic quotients of the point-pushing action images.

## Setup

Let `X` be a finite bijective YBE solution.  Fix `k>=1` and a product-prefix
detector group

```text
Pi_j = G_1 x ... x G_j.
```

Write

```text
delta_{j,k}:F_k -> D_k(Pi_j)
pi_{X,k}:F_k -> P_k(X)
```

for the derivative-detector and point-pushing action marked maps.

Let

```text
b(j)=max { B : every finite group of order <= B occurs among G_1,...,G_j }.
```

## Theorem

The marked quotient

```text
D_k(Pi_j) -> P_k(X)
```

fails if and only if there exist:

```text
w in F_k,
phi:P_k(X)->H,
M normal H,
```

such that:

1. `H` is finite monolithic;
2. `M` is the unique minimal nontrivial normal subgroup of `H`;
3. `phi` is surjective;
4. `w in ker(delta_{j,k})`;
5. `phi(pi_{X,k}(w)) in M \ {1}`.

Moreover, for a minimal separating quotient witness,

```text
|H| > b(j).
```

## Proof

Assume the marked quotient fails.  Then there is a word `w in F_k` with

```text
delta_{j,k}(w)=1,
g=pi_{X,k}(w)!=1 in P_k(X).
```

Among all finite quotients of `P_k(X)` separating `g`, choose one of minimal
order:

```text
phi:P_k(X)->H,
phi(g)!=1.
```

Since `P_k(X)` is finite, such a quotient exists.  Replace `H` by the image
of `phi`, so `phi` is surjective.  Write `bar g=phi(g)`.

Let `N normal H` be nontrivial.  If `bar g notin N`, then the proper quotient
`H/N` still separates `bar g`, contradicting the minimality of `H`.  Hence

```text
bar g in N
```

for every nontrivial normal subgroup `N` of `H`.

It follows that `H` has a unique minimal nontrivial normal subgroup.  If
`M_1` and `M_2` were distinct minimal normal subgroups, then

```text
M_1 cap M_2 = 1
```

and `bar g`, which lies in both, would be trivial.  This contradicts
`bar g!=1`.  Let `M` be the unique minimal normal subgroup.  Then

```text
bar g in M \ {1}.
```

So `H` is monolithic and the moved element lands in the monolith.

Conversely, if such data exists, a marked quotient

```text
D_k(Pi_j) -> P_k(X)
```

cannot exist: composing with `phi` would force every word trivial in
`D_k(Pi_j)` to be trivial in `H`, but `w` is trivial in `D_k(Pi_j)` and has
nontrivial image in `H`.

This proves the compression equivalence.

## Size Escape

Let

```text
N = ker(phi pi_{X,k}) normal F_k.
```

Then `F_k/N isomorphic H`.  By the fixed-arity cofinality theorem
`proofs/point_pushing_fixed_arity_cofinality.md`, there is a finite group

```text
G_N = F_k / Theta_k(N)
```

with

```text
ker(F_k->D_k(G_N)) <= N.
```

Equivalently, `D_k(G_N)->F_k/N isomorphic H` is a marked quotient.  The
triangular Nielsen automorphism `Theta_k` preserves index, so

```text
|G_N|=|F_k/N|=|H|.
```

If `|H|<=b(j)`, then `G_N` occurs among the first `j` product-prefix factors
up to isomorphism.  The projection `Pi_j->G_N` is surjective, and derivative
functoriality gives

```text
D_k(Pi_j) -> D_k(G_N) -> H.
```

Since `w=1` in `D_k(Pi_j)`, its image in `H` would be trivial.  But that image
is `phi(pi_{X,k}(w))`, which is nontrivial.  Therefore `|H|>b(j)`.

## Brunnian First-Failure Form

If the failure is a first arity failure for `Pi_j`, then
`proofs/point_pushing_jump_normalization.md` lets one choose

```text
w in ker(F_k->F_{k-1}).
```

Combining jump normalization with monolithic compression gives a simultaneous
normal form:

```text
w in ker(F_k->F_{k-1}),
w=1 in D_k(Pi_j),
phi(w(h_1,...,h_k)) in M \ {1},
|H|>b(j),
```

where `H` is monolithic with monolith `M`.

## Consequence

A final B proof must produce an unbounded sequence of critical monolithic
quotients.  A bounded cyclic, solvable, simple, or permutation quotient mover
cannot be the final obstruction.

Equivalently, A follows if one proves that finite YBE point-pushing action
images cannot support unbounded monolithic first-failure quotients.

## Audit Hook

The helper

```text
point_pushing_monolithic_compression_audit(...)
```

checks one finite row.  It evaluates a supplied point-pushing word in
`P_k(X)`, chooses a smallest quotient of the action group separating that
element, enumerates the quotient's normal subgroups when below the supplied
size cap, and verifies that the quotient is monolithic and the projected
element lies in the monolith.  This is only a finite row check; outcome B
still requires an all-`j` sequence, and outcome A requires a symbolic
no-unbounded-monolith theorem.
