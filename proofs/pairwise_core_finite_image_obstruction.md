# Pairwise-Core Finite-Image Obstruction

Date: 2026-06-06

This note sharpens the pairwise-or-central finite-image boundary.  The
central high-Brunnian alternative is not independent of pairwise commutators:
the all-meridian symmetric commutator lies in every pairwise commutator
subgroup.  Thus the remaining finite-image target can be phrased as a single
pairwise-core vanishing condition.

This is still a C-type result.  It does not prove Sawin's statement and does
not construct a cofinal counterexample.

## The All-Meridian Commutator Is Pairwise-Deep

Let `G` be a group and let

```text
N_1,...,N_r triangleleft G,        r>=2.
```

Put

```text
C=[N_1,...,N_r]_Sigma.
```

Then, for every distinct pair `a,b`,

```text
C <= [N_a,N_b].
```

Equivalently,

```text
C <= D := intersection_{1<=a<b<=r} [N_a,N_b].
```

### Proof

It is enough to prove the claim for one fully parenthesized commutator word
with one input from each `N_i`.  Represent the bracketing by a binary rooted
tree.  Fix two labels `a!=b`, and let `v` be the lowest vertex of the tree
whose descendant leaves contain both `a` and `b`.  At the two children of
`v`, the labels `a` and `b` lie in different subtrees.

Every subcommutator whose leaves include `a` lies in `N_a`, because `N_a` is
normal in `G`.  Similarly, every subcommutator whose leaves include `b` lies
in `N_b`.  Therefore the commutator formed at `v` lies in

```text
[N_a,N_b].
```

Since `[N_a,N_b]` is normal in `G`, all further commutators above `v` remain
inside `[N_a,N_b]`.  Thus the original fully parenthesized commutator lies in
`[N_a,N_b]`.  Since the pair `a,b` was arbitrary, every generator of the
symmetric commutator subgroup lies in every `[N_a,N_b]`.

## Pairwise-Core Criterion

In the finite-image notation, set

```text
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma
```

and

```text
D_n=intersection_{1<=i<j<=n-1} [N_{i,n},N_{j,n}].
```

For `n>=3`,

```text
C_n <= D_n.
```

Hence

```text
K_n cap D_n = 1  =>  K_n cap C_n = 1.
```

Therefore, for a detector `Q=Y^0 x T_2`, the following condition is
sufficient for domination:

```text
K_n cap D_n = 1
```

for every sufficiently large `n`, plus finitely many fixed-arity detectors for
the remaining small arities.

This is weaker than demanding

```text
K_n cap [N_{i,n},N_{j,n}] = 1
```

for every pair `i!=j`: it only kills elements lying in all pairwise
commutator subgroups simultaneously, not arbitrary noise in a single pairwise
commutator.

## Central Chief Factors Are Pairwise-Covered

Suppose a central Type C obstruction occurs: there is a chief factor

```text
A/B <= K_n,
A/B <= Z(Gamma_n/B),
```

and

```text
C_n covers A/B.
```

Then `D_n` covers `A/B`.  More strongly, for every pair `i!=j`,

```text
[N_{i,n},N_{j,n}] covers A/B.
```

This follows immediately from `C_n<=[N_{i,n},N_{j,n}]` for every pair.

Moreover, since `A/B` is central and chief, it is cyclic of prime order:

```text
A/B ~= C_p.
```

Indeed, if `A/B` is central in `Gamma_n/B`, then every subgroup of `A/B` is
normal in `Gamma_n/B`.  Since `A/B` is chief, it has no nontrivial proper
subgroup.  A finite abelian group with no nontrivial proper subgroup has prime
order.

Thus a central high-Brunnian obstruction cannot avoid pairwise commutators.  A
central obstruction must be a prime-order central factor lying in the full
all-meridian commutator and covered by every pairwise commutator subgroup.

## Relative Commutator-Injectivity Criterion

Let `Z` be a braided quotient of `X` already dominated by a finite rack
`Y_Z`.  Put

```text
Q=Y_Z^0 x T_2.
```

For the last-strand images write

```text
G^X_n = rho^X_n(F_{n-1}),
G^Z_n = rho^Z_n(F_{n-1}),
E_n = ker(G^X_n -> G^Z_n).
```

If

```text
E_n cap gamma_2(G^X_n)=1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.

### Proof

Let

```text
gamma in K_n cap D_n.
```

Choose `beta in F_{n-1}` with `Phi_n(beta)=gamma`.  Because `gamma in K_n`,
the `Q`-action of `beta` is trivial.  Since `Q` contains the rack detector
`Y_Z` and `Y_Z` dominates `Z`, the `Z`-action of `beta` is trivial.  Hence

```text
rho^X_n(beta) in E_n.
```

On the other hand, since `gamma in D_n`, its `X`-projection lies in the
commutator subgroup:

```text
rho^X_n(beta) in gamma_2(G^X_n).
```

Thus

```text
rho^X_n(beta) in E_n cap gamma_2(G^X_n)=1.
```

So `gamma` lies in both projection kernels `K_n` and `L_n`.  But
`Gamma_n<=Sym(Q^n) x Sym(X^n)`, so

```text
K_n cap L_n = 1.
```

Therefore `gamma=1`.  Hence

```text
K_n cap D_n=1
```

for all sufficiently large `n`, and the pairwise-core criterion kills the
large-arity finite-image obstruction.  Fixed-arity rack cofinality supplies
finitely many racks for the remaining small arities; their product with `Q`
dominates `X`.

## Abelianization-Visible Relative Kernel

The condition

```text
E_n cap gamma_2(G^X_n)=1
```

has an equivalent group-theoretic form: the relative last-strand kernel `E_n`
injects into the abelianization of `G^X_n`.

Indeed, the kernel of the abelianization map

```text
G^X_n -> (G^X_n)_ab
```

is `gamma_2(G^X_n)`.  Therefore the restriction

```text
E_n -> (G^X_n)_ab
```

is injective if and only if `E_n cap gamma_2(G^X_n)=1`.

In particular, this condition forces `E_n` to be central in `G^X_n`.  Since
`E_n` is normal,

```text
[E_n,G^X_n] <= E_n cap gamma_2(G^X_n),
```

so trivial intersection gives

```text
E_n <= Z(G^X_n).
```

Thus the quotient route can be restated as follows: find a dominated braided
quotient `Z` such that the relative last-strand kernel is visible in the
abelianization of the `X` last-strand image in all sufficiently large arities.
Equivalently, no nontrivial relative-kernel element is a commutator in
`G^X_n`.

## Remaining Boundary

To prove Sawin's statement by this finite-image route, it is now enough to
prove one of the following.

Pairwise-core form:

```text
exists Q=Y^0 x T_2 such that for all sufficiently large n,
K_n cap intersection_{i<j}[N_{i,n},N_{j,n}] = 1.
```

Quotient form:

```text
For every finite bijective X, find a dominated braided quotient Z such that
E_n cap gamma_2(G^X_n)=1
```

for all sufficiently large `n`.

A cofinal counterexample must produce, for every finite rack prefix `P_m`,
with `Q_m=P_m^0 x T_2`, unbounded arities `n_m` and nontrivial elements

```text
1 != gamma_m in K_{n_m} cap C_{n_m}
              <= K_{n_m} cap intersection_{i<j}[N_{i,n_m},N_{j,n_m}].
```

It is not enough to show

```text
K_n cap [N_{i,n},N_{j,n}] != 1
```

for one pair.  The obstruction must be simultaneously pairwise-deep for every
pair and must still lie in the full all-meridian symmetric commutator.
