# Theoretical Review: Active-Lift Forced-Pair Criterion

Date: 2026-06-07.

## Verdict

This is theorem-level progress in the positive route.  It weakens the
transport-stable lift-fibre condition to the actual condition needed for
braid-equivariant lifts along real `X`-trajectories.

The previous condition

```text
g E_q g^{-1} = E_{lambda_p(q)}
```

controlled too much: it also constrained non-fillable or virtual products.
Actual braid moves only use compatible adjacent contextual pairs.

## Setup

Let `P=P_X` be the finite two-sided contextual quotient.  For each
`p in P`, let

```text
lambda_p : D_p -> P
```

be the forced partial left translation.  Use the finite rack

```text
Y = P x Sym(P),
(p,g)*(q,h) = (g(q), g h g^{-1}).
```

## Active Lift Sets

Choose nonempty sets

```text
C_p subseteq Sym(P)
```

such that:

1. **Forced extension.**

```text
g(q)=lambda_p(q)  for every g in C_p and every q in D_p.
```

2. **Forced-pair closure only.**  Whenever `q in D_p`, set
   `r=lambda_p(q)`.  Then for every `g in C_p` and `h in C_q`,

```text
g h g^{-1} in C_r.
```

No condition is imposed for `q notin D_p`.

## Lift Relation

For `x=(x_1,...,x_n)` with contextual readout

```text
J_n(x)=(p_1,...,p_n),
```

define `(y,x) in Pi_n` iff

```text
y_i=(p_i,g_i),  g_i in C_{p_i}.
```

Every `x` has a lift because every `C_p` is nonempty.

For a positive braid generator, adjacent contextual classes are compatible:
`q in D_p` and `r=lambda_p(q)`.  A lift `(p,g),(q,h)` maps in `Y` to

```text
(g(q), g h g^{-1}) = (r, g h g^{-1}),
```

which is active over `r` by forced-pair closure.  The second output remains
active over `p`.  Since the braid generator is a bijection on the finite
ambient product, positive preservation implies inverse preservation as well.
Thus `Pi_n` is braid-equivariant for every `n`.

## Domination Criterion

If `J_n:X^n -> P^n` is injective on every braid orbit for all `n`, then
`Y=P x Sym(P)` dominates `X`:

```text
ker rho^Y_n <= ker rho^X_n.
```

The proof is the standard single-valued lift argument.

## Exact Finite CSP

For each `p`, let

```text
V_p={g in Sym(P): g extends lambda_p}.
```

Use Boolean variables `z_{p,g}` for `g in V_p`.  Require nonemptiness:

```text
∨_{g in V_p} z_{p,g}
```

for every `p`.  For every forced pair `q in D_p`, with `r=lambda_p(q)`, impose

```text
z_{p,g} and z_{q,h} => z_{r, g h g^{-1}}
```

when `g h g^{-1} in V_r`; if not, impose incompatibility

```text
not z_{p,g} or not z_{q,h}.
```

This finite Boolean system is exact for active lift existence in the canonical
rack `P x Sym(P)`.

## Current Positive Target

A proof of A by this route now needs:

```text
For every finite bijective YBE solution X, the active-lift CSP has nonempty
solutions C_p;
J_n:X^n -> P_X^n is braid-orbit-injective for every n.
```

The one-copy identity-extension completion is the special case
`C_p={L_p}`.  The new condition is strictly weaker.
