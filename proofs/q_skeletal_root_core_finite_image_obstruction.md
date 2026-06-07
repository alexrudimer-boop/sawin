# Q-Skeletal Root-Core Finite-Image Obstruction

Date: 2026-06-06

This note records a C-type sharpening of the recursive root-core obstruction
for Sawin's finite-rack domination problem.  It does not prove Sawin's
statement and does not provide a cofinal counterexample.  Its contribution is
to add exact small-support containment tests to the fixed-depth recursive
root-core hierarchy.

The guiding point is that an all-meridian commutator on a support `S` lies not
only in weighted block approximations and recursive root-core approximations,
but in every exact all-meridian subgroup attached to a nonempty subset
`T subset S`.

## Exact Support Monotonicity

Let `G` be a group and let

```text
N_1,...,N_r triangleleft G.
```

For every nonempty subset `S subset {1,...,r}`, write

```text
C_S=[N_i | i in S]_Sigma,
```

with `C_{ {i} }=N_i`.

Lemma.  If `empty != T subset S`, then

```text
C_S <= C_T.
```

Proof.  It is enough to prove the claim for one fully parenthesized
commutator word with one leaf from each `N_i`, `i in S`.

More generally, consider a subtree whose leaf support is `U` and suppose
`empty != T subset U`.  We prove by induction on the subtree that its value
lies in `C_T`.

If the subtree has one leaf, the claim is immediate.  Otherwise the subtree
is a commutator `[a,b]` with child supports `U_a` and `U_b`.  If
`T subset U_a`, then by induction `a in C_T`; since `C_T` is normal,
`[a,b] in C_T`.  The case `T subset U_b` is the same.

If `T` meets both child supports, put

```text
T_a=T cap U_a,
T_b=T cap U_b.
```

By induction, `a in C_{T_a}` and `b in C_{T_b}`.  Hence

```text
[a,b] in [C_{T_a},C_{T_b}].
```

The root-split/fat-commutator containment gives

```text
[C_{T_a},C_{T_b}] <= C_T,
```

because commutators between all-support words on `T_a` and `T_b` are fat
commutators using every label in `T=T_a sqcup T_b`.  Thus `[a,b] in C_T`.

Applying this to the root gives every generator of `C_S` lies in `C_T`.

## Q-Skeletal Recursive Root Cores

Fix an integer `q>=3`.  For nonempty `S`, define the exact `q`-skeleton

```text
J_{S,q}
  =
intersection_{empty != T subset S, |T|<=q} C_T.
```

By exact support monotonicity,

```text
C_S <= J_{S,q}.
```

Let `R_S^(d)` be the recursive root core from
`proofs/recursive_root_core_finite_image_obstruction.md`.

Define the q-skeletal recursive root core `Sk_{S,q}^{(d)}` as follows:

```text
Sk_{S,q}^{(0)} = R_S^(0) cap J_{S,q}.
```

For `d>=0`,

```text
Sk_{S,q}^{(d+1)}
  =
Sk_{S,q}^{(d)} cap
product_{ {A,B} in Bip(S) } [Sk_{A,q}^{(d)},Sk_{B,q}^{(d)}].
```

For `q=3`, the new base condition forces membership in every exact
three-meridian subgroup

```text
[N_i,N_j,N_k]_Sigma,
```

not merely in every weighted three-block collapse.

## Skeletal Root-Core Containment and Exactness

Theorem.  For every nonempty `S`, every `q>=3`, and every `d>=0`,

```text
C_S <= Sk_{S,q}^{(d+1)} <= Sk_{S,q}^{(d)} <= R_S^(d).
```

If `q' >= q`, then

```text
Sk_{S,q'}^{(d)} <= Sk_{S,q}^{(d)}.
```

Finally,

```text
Sk_{S,q}^{(d)} = C_S       whenever d>=max(0, |S|-q).
```

Proof.  First, `C_S<=Sk_{S,q}^{(0)}` because `C_S<=R_S^(0)` and
`C_S<=J_{S,q}`.

Assume `C_T<=Sk_{T,q}^{(d)}` for every nonempty `T subseteq S`.  The
root-split factorization gives

```text
C_S =
product_{ {A,B} in Bip(S) } [C_A,C_B].
```

Since `C_A<=Sk_{A,q}^{(d)}` and `C_B<=Sk_{B,q}^{(d)}`, each factor
`[C_A,C_B]` lies in `[Sk_{A,q}^{(d)},Sk_{B,q}^{(d)}]`.  Together with
`C_S<=Sk_{S,q}^{(d)}`, this gives `C_S<=Sk_{S,q}^{(d+1)}`.

The descending inclusion `Sk_{S,q}^{(d+1)}<=Sk_{S,q}^{(d)}` is immediate.
The inclusion `Sk_{S,q}^{(d)}<=R_S^(d)` follows by induction from
`Sk_{S,q}^{(0)}<=R_S^(0)` and from

```text
[Sk_{A,q}^{(d)},Sk_{B,q}^{(d)}] <= [R_A^(d),R_B^(d)].
```

If `q'>=q`, then `J_{S,q'}<=J_{S,q}` because it intersects over at least as
many exact small-support subgroups.  The recursive definition gives
`Sk_{S,q'}^{(d)}<=Sk_{S,q}^{(d)}` by induction on `d`.

For exactness, if `|S|<=q`, then `J_{S,q}` includes the factor `C_S` itself.
Since `C_S<=C_T` for every nonempty `T subset S`, the intersection
`J_{S,q}` equals `C_S`; hence `Sk_{S,q}^{(0)}=C_S`.

Now let `|S|=m>q`, and assume the statement for all proper nonempty subsets.
If `d>=m-q`, then for every proper nonempty `A subsetneq S`,

```text
d-1 >= m-q-1 >= |A|-q.
```

Thus `Sk_{A,q}^{(d-1)}=C_A` and `Sk_{S\A,q}^{(d-1)}=C_{S\A}`.  Hence

```text
product_{ {A,B} in Bip(S) }
[Sk_{A,q}^{(d-1)},Sk_{B,q}^{(d-1)}]
  =
product_{ {A,B} in Bip(S) } [C_A,C_B]
  =
C_S.
```

Therefore

```text
Sk_{S,q}^{(d)}=Sk_{S,q}^{(d-1)} cap C_S.
```

Since `C_S<=Sk_{S,q}^{(d-1)}`, this gives `Sk_{S,q}^{(d)}=C_S`.

## Finite-Image Consequence

Return to the finite-image setup, and let

```text
R_n={1,...,n-1}.
```

For every nonempty `S subset R_n`, define

```text
C_{n,S}=[N_{i,n} | i in S]_Sigma,
Sk_{n,S,q}^{(d)}
  =
Sk_{S,q}^{(d)}(Gamma_n;(N_{i,n})_{i in S}).
```

For full support write

```text
Sk_{n,q}^{(d)}=Sk_{n,R_n,q}^{(d)}.
```

Then

```text
C_n <= Sk_{n,q}^{(d)} <= R_n^(d)
```

for every fixed `q>=3` and `d>=0`.

Corollary.  A finite rack detector `Q=Y^0 x T_2` dominates `X` if there
exist fixed integers `q>=3` and `d>=0` such that

```text
K_n cap Sk_{n,q}^{(d)}=1
```

for all sufficiently large `n`, together with fixed-arity rack detectors for
the remaining small arities.

Proof.  Since `C_n<=Sk_{n,q}^{(d)}`, the assumed vanishing gives
`K_n cap C_n=1` in all sufficiently large arities.  The finite-image
Brunnian theorem identifies that with the large-arity domination condition,
and fixed-arity rack cofinality handles the finitely many remaining arities.

## Relative Quotient Version

Let `Z` be a braided quotient of `X` already dominated by a finite rack
`Y_Z`, and put

```text
Q=Y_Z^0 x T_2.
```

Recall

```text
G^X_n=rho^X_n(F_{n-1}),
E_n=ker(G^X_n -> G^Z_n),
M_{i,n}=<<rho^X_n(x_i)>>_{G^X_n}.
```

For nonempty `S subset R_n`, set

```text
C^X_{n,S}=[M_{i,n} | i in S]_Sigma,
Sk_{n,S,q}^{X,(d)}
  =
Sk_{S,q}^{(d)}(G^X_n;(M_{i,n})_{i in S}),
```

and write

```text
Sk_{n,q}^{X,(d)}=Sk_{n,R_n,q}^{X,(d)}.
```

Corollary.  If there is a dominated braided quotient `Z` of `X` and fixed
integers `q>=3` and `d>=0` such that

```text
E_n cap Sk_{n,q}^{X,(d)}=1
```

for all sufficiently large `n`, then one finite rack dominates `X`.

Proof.  Take `gamma in K_n cap C_n` and choose `beta in F_{n-1}` with
`Phi_n(beta)=gamma`.  Since `gamma in K_n`, the `Q` action of `beta` is
trivial.  Since `Q` contains a rack detector dominating `Z`, the `Z` action is
trivial.  Hence `rho^X_n(beta) in E_n`.

Also, because `gamma in C_n`, its `X` projection lies in

```text
C^X_n=[M_{1,n},...,M_{n-1,n}]_Sigma.
```

By the theorem, `C^X_n<=Sk_{n,q}^{X,(d)}`.  Therefore
`rho^X_n(beta) in E_n cap Sk_{n,q}^{X,(d)}=1`.  Thus
`gamma in K_n cap L_n=1`, because
`Gamma_n<=Sym(Q^n) x Sym(X^n)` has trivially intersecting projection kernels.
So `K_n cap C_n=1` in all sufficiently large arities, and fixed-arity rack
cofinality handles the rest.

## Strictness Status

The response included a nilpotent Lie algebra model intended to show
`Sk_{S,3}^{(0)}<R_S^(0)`.  This model is not needed for the finite-image
criterion above.  It is best treated as a group-theoretic strictness model
until all quotient choices and Hall-support assertions are independently
checked.  The theorem/proof content of this note does not depend on that
strictness example.

## Remaining Boundary

The current finite-image positive target is:

```text
exists Q=Y^0 x T_2, fixed q>=3, and fixed d>=0 such that
K_n cap Sk_{n,q}^{(d)}=1
for all sufficiently large n.
```

The quotient target is:

```text
exists dominated quotient Z, fixed q>=3, and fixed d>=0 such that
E_n cap Sk_{n,q}^{X,(d)}=1
for all sufficiently large n.
```

A cofinal counterexample must still produce, for every finite rack prefix,
unbounded arities `n_m` and nontrivial elements in

```text
K_{n_m} cap C_{n_m}.
```

Such elements automatically lie in every fixed `q,d` skeletal root-core
`Sk_{n_m,q}^{(d)}` once `n_m` is large enough.  Conversely, membership in a
skeletal root-core approximation is not enough for a counterexample unless
membership in the exact all-meridian subgroup `C_n` is proved.
