# Fixed-Transition Bound Attempt Audit

This note records the current status of the attempted proof of the
fixed-transition bounded residual theorem.

## Statement Under Audit

For finite `X`, a dominated braided quotient `X/E`, and a fixed
color-changing contextual transition

```text
t : (A,a,B) -> (A',b,B'),        a E b,        a != b,
```

one wants constants `M,N` such that every sufficiently high witness

```text
beta in W_n^E(t)
```

has

```text
r(beta) <= M.
```

Here `r(beta)` is the least size of a finite rack detecting `beta`, and
`W_n^E(t)` is the class of Brunnian, `X/E`-trivial, `T_2`-invisible braids
that actually realize the fixed raw contextual transition `t`.

## Dominated X Case

The theorem is immediate if `X` itself is already finite-rack dominated.
Suppose a finite rack `Y_X` satisfies

```text
ker rho^{Y_X}_n <= ker rho^X_n        for all n.
```

Every `beta in W_n^E(t)` is `X`-visible, since it realizes a color-changing
transition with `a != b`.  Therefore

```text
rho^X_n(beta) != 1,
```

so domination gives

```text
rho^{Y_X}_n(beta) != 1.
```

Hence

```text
r(beta) <= |Y_X|.
```

Thus one may take `M=|Y_X|` and `N=0`.  This includes already handled
branches such as finite left-nondegenerate solutions, where the guitar map
identifies the braid action with the action of the associated finite rack.

## Quotient Domination Does Not Prove The Bound

The hypothesis that `X/E` is rack-dominated does not itself control the
transition.  By definition every witness satisfies

```text
beta in ker rho^{X/E}_n.
```

So any rack detector that only dominates `X/E` is deliberately blind to
`beta`.  The desired detector must see the fiber motion inside one `E`-class,
namely

```text
a -> b,        a E b,        a != b.
```

The missing theorem is therefore a bounded finite rack or finite group witness
for actual contextual fiber monodromy.  Existing contextual partial-rack
machinery does not supply this automatically: actual braid trajectories only
force the YBE identities on jointly realizable contextual triples, while a
finite rack completion must satisfy the rack identities on all triples in the
completed structure.

## Purity Nuance

The explicit `T_2` condition is necessary for the detector setup
`Y^0 x T_2` and for realization-aware contextual separability.  It is not
logically necessary for the unbounded residual-complexity formulation.

Let `W'_n^E(t)` be the same witness class but without
`beta in ker rho^{T_2}_n`.  If `beta in W'_n^E(t)` is not pure, then its
strand permutation is nontrivial.  The two-element trivial rack `T_2` detects
that permutation, so

```text
rho^{T_2}_n(beta) != 1
```

and therefore

```text
r(beta) <= 2.
```

Consequently any sequence with `r(beta_m)->infinity` is eventually pure.  The
bounded-residual theorem with the `T_2` condition is equivalent to the same
boundedness statement without it, after replacing `M` by `max(M,2)`.

## Current Status

The attempted proof of the fixed-transition bound stops exactly at the
following missing ingredient:

```text
For every finite X, dominated quotient X/E, and fixed color-changing
contextual transition t inside an E-class, actual contextual fiber monodromy
has a bounded finite rack or finite group witness.
```

This statement is proved when `X` is already rack-dominated, but it is not
known from the quotient hypothesis alone.
