# Fixed-Transition Rack Residual Complexity

This note turns fixed contextual survival into an exact residual-complexity
criterion.  The remaining obstruction can be phrased as unbounded finite-rack
residual complexity for Brunnian witnesses realizing one fixed contextual
transition.

## Rack Residual Complexity

For a nontrivial braid

```text
beta in B_n,
```

define

```text
r(beta)=min{|Y| : Y is a finite rack and rho^Y_n(beta) != 1}.
```

Set

```text
r(1)=infinity.
```

For nontrivial `beta`, the number `r(beta)` is finite.  Indeed, the Artin
representation detects nontrivial braids in `Aut(F_n)`, and residual finiteness
of free groups gives a finite group quotient detecting a nontrivial Artin
displacement.  The corresponding finite conjugation rack detects `beta`.

## Fixed Contextual-Transition Witness Classes

Let

```text
hat P=M_L x X x M_R
```

be the raw two-sided contextual state set.  Let

```text
t=(p->p')
```

be a raw contextual transition, where

```text
p=(A,a,B),
p'=(A',b,B'),
a != b.
```

For a braided congruence `E` with `a E b`, define `W_n^E(t)` to be the set of
braids

```text
beta in Brun_n cap ker rho^{X/E}_n cap ker rho^{T_2}_n
```

such that there exist

```text
xword in X^n,
j in {1,...,n},
```

with

```text
hat c_j(xword)=p,
hat c_j(rho^X_n(beta)xword)=p'.
```

Thus `W_n^E(t)` is the set of quotient-trivial, `T_2`-invisible Brunnian
braids realizing the fixed contextual transition `t`.  Since `a != b`, every
element of `W_n^E(t)` is `X`-visible.

## Fixed-Transition Survival Equals Unbounded Residual Complexity

For a fixed transition `t`, the following are equivalent.

### Condition A: t Survives Every Finite Rack Detector

For every finite rack `Y` and every arity cutoff `N`, there exist

```text
n>N,
beta in W_n^E(t),
```

such that

```text
rho^{Y^0 x T_2}_n(beta)=1.
```

For `beta in W_n^E(t)`, this is equivalent to

```text
rho^Y_n(beta)=1.
```

The equivalence uses the transparent-extension deletion formula: all proper
deletions of a Brunnian braid are trivial, so the only transparent coloring
case left to check is the all-nontransparent `Y^n` coloring.  The `T_2` factor
is trivial by the explicit condition `beta in ker rho^{T_2}_n`.

### Condition B: Witness Residual Complexity Is Unbounded In Every Tail

For every rack-size bound `M` and every arity cutoff `N`, there exist

```text
n>N,
beta in W_n^E(t),
```

such that

```text
r(beta)>M.
```

### Proof

Assume Condition A.  Fix `M,N`.  Let

```text
U_M=prod_{|Y|<=M} Y,
```

where the product ranges over one representative of every finite rack
isomorphism class of size at most `M`.  This is finite, since there are only
finitely many rack operations on sets of size at most `M`.

By Condition A, there exist

```text
n>N,
beta in W_n^E(t),
```

with

```text
rho^{U_M}_n(beta)=1.
```

If some rack of size at most `M` detected `beta`, then the product rack `U_M`
would detect `beta`.  Therefore no rack of size at most `M` detects `beta`, so

```text
r(beta)>M.
```

Conversely, assume Condition B.  Let `Y` be any finite rack and let `N` be an
arity cutoff.  Put

```text
M=|Y|.
```

By Condition B, there exist

```text
n>N,
beta in W_n^E(t),
```

with `r(beta)>M`.  Since `Y` has size `M`, it cannot detect `beta`.  Hence

```text
rho^Y_n(beta)=1.
```

Because `beta in W_n^E(t)`, this is equivalent to

```text
rho^{Y^0 x T_2}_n(beta)=1.
```

This proves the equivalence.

## Relative Bounded-Complexity Domination Criterion

Let `E` be a braided congruence on finite `X`, and suppose `X/E` is dominated
by a finite rack `Y_E`.

Assume there exist constants `M,N` such that for every color-changing raw
contextual transition

```text
t=(p->p'),        p=(A,a,B),        p'=(A',b,B'),        a E b, a != b,
```

and every

```text
n>N,
beta in W_n^E(t),
```

one has

```text
r(beta)<=M.
```

Then `X` is finite-rack dominated.

### Proof

Let

```text
U_M=prod_{|Y|<=M}Y
```

be the finite product of all racks of size at most `M`.  For each

```text
2<=k<=N,
```

fixed-arity rack cofinality supplies a finite rack `Z_k` such that

```text
ker rho^{Z_k}_k <= ker rho^X_k.
```

Define

```text
Q=Y_E^0 x U_M^0 x T_2 x prod_{k=2}^N Z_k^0.
```

By the Brunnian reduction, it is enough to show that every

```text
beta in Brun_n cap ker rho^Q_n
```

is `X`-trivial.

If `n<=N`, then the `Z_n^0` factor gives `beta in ker rho^{Z_n}_n`, hence
`beta in ker rho^X_n`.

Now suppose `n>N`.  The `Y_E^0` factor gives

```text
beta in ker rho^{X/E}_n.
```

If `beta` were `X`-visible, some coordinate would change color.  Let its
before/after raw contextual transition be

```text
t=(p->p').
```

Then

```text
beta in W_n^E(t).
```

By the bounded residual-complexity assumption,

```text
r(beta)<=M.
```

So some rack of size at most `M` detects `beta`, hence the product rack `U_M`
detects `beta`.  But `beta in ker rho^Q_n` implies `beta in ker rho^{U_M^0}_n`,
and because `beta` is Brunnian this implies `rho^{U_M}_n(beta)=1`, a
contradiction.

Therefore `beta` is `X`-trivial.  Hence `Q` dominates `X`.

## Absolute Criterion

Taking `E=nabla=X x X`, the quotient `X/E` is the one-point solution and is
dominated.  Thus finite `X` is dominated iff there exist constants `M,N` such
that for every color-changing raw contextual transition `t` and every

```text
n>N,
beta in W_n^nabla(t),
```

one has

```text
r(beta)<=M.
```

The forward implication is immediate: if `Y_X` dominates `X`, then every
`X`-visible braid is detected by `Y_X`, so `r(beta)<=|Y_X|` for every
color-changing witness `beta`.

The reverse implication is the relative criterion with `E=nabla`.

## Status Of The Fixed-Transition Bound

The fixed-transition bound is immediate under the stronger hypothesis that
`X` itself is already finite-rack dominated.  If a finite rack `Y_X` satisfies

```text
ker rho^{Y_X}_n <= ker rho^X_n        for all n,
```

then every `beta in W_n^E(t)` is `X`-visible because `t` is color-changing.
Therefore `rho^{Y_X}_n(beta) != 1`, and

```text
r(beta) <= |Y_X|.
```

So one may take `M=|Y_X|` and `N=0`.  This includes the standard already
handled branches such as the finite left-nondegenerate case, where the guitar
map identifies the braid action with the action of the associated finite rack.

The quotient hypothesis alone does not supply this bound.  Every
`beta in W_n^E(t)` is already killed on `X/E`, so a rack dominating `X/E`
detects none of the relevant fiber motion.  The missing ingredient is a
bounded finite rack or finite group witness for the actual contextual motion
inside the `E`-class:

```text
a -> b,        a E b,        a != b.
```

Equivalently, one would need a bounded rack completion or bounded quotient
witness for the physical-strand contextual monodromy realizing the fixed
transition.  The known contextual partial-rack constructions do not provide
this automatically, because YBE controls jointly realizable local triples,
whereas finite rack completion has to satisfy the identities on all triples
in the completed object.

There is also a useful purity nuance.  The `T_2` condition is essential when
matching the Brunnian reduction with detectors of the form `Y^0 x T_2`, and it
is essential for the realization-aware contextual separability statement.  It
is not essential for unbounded residual complexity itself.  If `W'_n^E(t)` is
defined by omitting `ker rho^{T_2}_n`, then every non-pure `beta in W'_n^E(t)`
is detected by the two-element trivial rack:

```text
rho^{T_2}_n(beta) != 1,
```

because `T_2` records the Artin strand permutation.  Hence `r(beta) <= 2` for
non-pure `beta`.  Any sequence with `r(beta_m)->infinity` is therefore
eventually pure.  Thus the bounded-residual theorem with the explicit `T_2`
condition is equivalent to the same theorem without it after replacing `M` by
`max(M,2)`.  We keep the `T_2` condition in `W_n^E(t)` because the domination
criterion uses `Y^0 x T_2` and because it removes the low-arity non-pure
transporter artifacts from the contextual language.

## Minimal-Counterexample Consequence

If `X` is a smallest nonsimple counterexample with first-fold monolith `mu`,
then `X/mu` is dominated.  Therefore, by the relative criterion, there is one
fixed color-changing contextual transition

```text
t_*=(p_*->p'_*),        a_* mu b_*,        a_* != b_*,
```

such that

```text
for all M,N, exists n>N and beta in W_n^mu(t_*) with r(beta)>M.
```

Indeed, if every such transition had bounded residual complexity in some
tail, then finitely many transitions would allow a common `M,N`, and the
relative criterion would dominate `X`.

In the braided-simple branch, the same statement holds with `E=nabla`.

Thus a counterexample must force unbounded finite-rack residual complexity
inside one fixed contextual transition.

## Artin/Free-Group Corollary

Let

```text
delta_j(beta)=alpha_beta(x_j)x_j^{-1}
```

be the Artin displacement words.  If

```text
r(beta_m)->infinity,
```

then the finite-group residual complexity of the displacement tuple also tends
to infinity.  Equivalently, for every fixed finite group `G`, every
displacement word of `beta_m` is eventually a law on `G`.

Otherwise a bounded finite group detecting some displacement word would give a
bounded finite conjugation rack detecting `beta_m`, contradicting
`r(beta_m)->infinity`.

## Current Exact Targets

To prove Sawin domination, it is enough to prove:

```text
For every finite X, every dominated quotient X/E, and every fixed
color-changing contextual transition t inside an E-class, the values r(beta)
are bounded on all sufficiently high quotient-trivial Brunnian witnesses
realizing t.
```

Equivalently, fixed contextual transitions cannot require racks of unbounded
size to detect their realizing Brunnian braids.  By the purity nuance above,
one may state this with or without the explicit `T_2` condition when only
unbounded residual complexity is at issue.

To disprove Sawin domination, one must construct one fixed finite `X`, one
fixed contextual transition `t_*`, and a sequence

```text
beta_m in W_{n_m}^E(t_*),        n_m->infinity,
```

such that

```text
r(beta_m)->infinity.
```
