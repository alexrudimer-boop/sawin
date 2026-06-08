# Nondegenerate Reflection Brunnian Obstruction

This note attaches the nondegenerate-reflection quotient to the standard
finite-image Brunnian obstruction.  It gives a canonical split for the
counterexample search:

```text
either E_nd is universal,
or the relative last-strand kernel over X/E_nd has unbounded all-meridian
Brunnian survival.
```

## Setup

Let `X` be a finite bijective YBE solution, and let

```text
E_nd
```

be the nondegenerate-reflection congruence from
`proofs/nondegenerate_reflection_congruence.md`.  Put

```text
Z = X/E_nd.
```

Assume `E_nd != X x X`, so `Z` is a nontrivial finite two-sided
nondegenerate quotient.  By the known nondegenerate theorem, `Z` is dominated
by a finite rack.  Fix such a rack and call it `Y_Z`:

```text
ker rho^{Y_Z}_n <= ker rho^Z_n
```

for every `n`.

For each `n`, let

```text
F_{n-1} = ker(d_n:P_n -> P_{n-1})
```

be the last-strand free group, with free meridian generators

```text
x_i = A_{i,n},        1 <= i <= n-1.
```

Let

```text
G^X_n = rho^X_n(F_{n-1}),
G^Z_n = rho^Z_n(F_{n-1}).
```

The quotient map `X -> Z` induces a surjection

```text
G^X_n -> G^Z_n.
```

Let its kernel be

```text
E_n = ker(G^X_n -> G^Z_n).
```

For each meridian generator, define

```text
M_{i,n} = << rho^X_n(x_i) >>_{G^X_n}.
```

Set

```text
C^X_n = [M_{1,n},...,M_{n-1,n}]_Sigma,
```

the full all-meridian symmetric commutator layer inside the `X`-image of the
last-strand group.

## Theorem

If

```text
E_n cap C^X_n = 1
```

for all sufficiently large `n`, then `X` is dominated by a finite rack.

Equivalently, if `X` is not dominated by any finite rack and
`E_nd != X x X`, then

```text
E_n cap C^X_n != 1
```

for unbounded `n`.

## Proof

Choose `N` such that

```text
E_n cap C^X_n = 1
```

for all `n > N`.

For each fixed arity `2 <= k <= N`, fixed-arity rack cofinality gives a
finite rack `Y_k` such that

```text
ker rho^{Y_k}_k <= ker rho^X_k.
```

Now form the finite rack

```text
Q = Y_Z^0 x T_2 x product_{k=2}^N Y_k^0.
```

Here `(-)^0` denotes the transparent extension, and `T_2` is the two-element
trivial rack.

We use the standard transparent Brunnian reduction from the ledger: to prove
that `Q` dominates `X`, it is enough to show that every

```text
beta in Brun_n cap ker rho^Q_n
```

acts trivially on `X^n`.

First suppose `n <= N`.  Since `Q` contains the transparent factor `Y_n^0`,
coloring all `n` strands nontransparent shows

```text
beta in ker rho^{Y_n}_n.
```

By the choice of `Y_n`, this gives

```text
beta in ker rho^X_n.
```

Now suppose `n > N`.  Since `Q` contains `Y_Z^0`, coloring all strands
nontransparent gives

```text
beta in ker rho^{Y_Z}_n.
```

Because `Y_Z` dominates `Z`,

```text
beta in ker rho^Z_n.
```

The `T_2` factor forces `beta` to be pure.  Since `beta` is Brunnian, deleting
the last strand gives the identity, so

```text
beta in ker(d_n:P_n -> P_{n-1}) = F_{n-1}.
```

Its `X`-image is therefore an element of `G^X_n`.  Since `beta` is
`Z`-trivial, this image lies in the relative kernel `E_n`.

The standard finite-image Brunnian theorem for the last-strand free group
also gives

```text
rho^X_n(beta) in C^X_n.
```

Indeed, a last-strand Brunnian braid deletes trivially after deleting any one
of the first `n-1` strands, so its image lies in the full symmetric
commutator of the normal closures of the meridian images.

Thus

```text
rho^X_n(beta) in E_n cap C^X_n.
```

By the large-arity assumption, this intersection is trivial.  Hence

```text
rho^X_n(beta)=1.
```

So every Brunnian `Q`-invisible braid is `X`-invisible.  The Brunnian
reduction implies that `Q` dominates `X`.

This proves the theorem.

## Consequence

The nondegenerate reflection gives a canonical two-branch obstruction.

If

```text
E_nd != X x X,
```

then the quotient `Z=X/E_nd` is nontrivial and nondegenerate.  Therefore a
failure of finite-rack domination must produce unbounded relative
all-meridian survival:

```text
E_n cap [M_{1,n},...,M_{n-1,n}]_Sigma != 1
```

for unbounded `n`.

If

```text
E_nd = X x X,
```

then `X` has no nontrivial two-sided nondegenerate quotient.  This is the
degeneracy-perfect branch.  Any braided-simple degenerate candidate lies
here.

Thus a minimal counterexample must be one of:

```text
degeneracy-perfect: E_nd = X x X,
```

or

```text
proper nondegenerate reflection but cofinal relative all-meridian survival:
E_n cap C^X_n != 1 for unbounded n.
```

The next positive target in the proper-reflection branch is to prove
eventual vanishing

```text
E_n cap C^X_n = 1
```

for the quotient `X -> X/E_nd`, perhaps by a stratified decoder tower.

The next negative target is to construct one fixed finite `X` with proper
`E_nd` for which the intersections `E_n cap C^X_n` survive cofinally and
lift to rack-prefix-invisible Brunnian witnesses.
