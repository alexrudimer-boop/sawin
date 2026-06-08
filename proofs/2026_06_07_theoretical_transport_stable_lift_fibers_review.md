# Theoretical Review: Transport-Stable Lift Fibers

Date: 2026-06-07.

## Verdict

This is theorem-level progress in the positive route.  It corrects the
multi-copy rack reduction: `P x Sym(P)` is always a rack, but not every copy is
a legitimate contextual lift.  The missing finite datum is a transport-stable
family of allowed permutation extensions over contextual classes.

## Setup

Let `P=P_X` be the finite two-sided contextual quotient.  For each
contextual class `p in P`, let

```text
lambda_p : D_p -> P
```

be the forced partial left translation.

The multi-copy rack is

```text
Y = P x Sym(P),
(p,g)*(q,h) = (g(q), g h g^{-1}).
```

This rack is always finite, but arbitrary `g in Sym(P)` is too loose.  If
`q in D_p`, a legitimate lift over `p` must send `q` to the forced output
`lambda_p(q)`.

## Correct Finite Lift Condition

For each `p in P`, choose a nonempty set

```text
E_p subseteq Sym(P)
```

such that:

1. **Extension condition.**  Every `g in E_p` extends the forced partial map:

```text
g(q)=lambda_p(q)  for every q in D_p.
```

2. **Transport condition.**  Whenever `q in D_p` and `r=lambda_p(q)`, then for
   every `g in E_p`,

```text
g E_q g^{-1} = E_r.
```

Equality is needed, not merely inclusion, because braid generators are
invertible.

## Lift Relation

If such sets `E_p` exist, define

```text
Pi_n subseteq Y^n x X^n
```

by `(y,x) in Pi_n` when

```text
J_n(x)=(p_1,...,p_n),
y_i=(p_i,g_i),
g_i in E_{p_i}.
```

Then `Pi_n` is braid-equivariant.  For a positive crossing with forced
contextual product `p*q=r=lambda_p(q)`, a lift `(p,g),(q,h)` maps to

```text
(g(q), g h g^{-1}) = (r, g h g^{-1}),
```

and `g h g^{-1} in E_r` by transport.  The inverse crossing uses the equality
`g E_q g^{-1}=E_r`.

## Domination Criterion

If in addition the contextual readout

```text
J_n:X^n -> P^n
```

is injective on every braid orbit for every `n`, then `Y=P x Sym(P)`
dominates `X`.

The proof is the standard lift argument: if `beta` fixes `Y^n`, choose a lift
`(y,x) in Pi_n`.  Equivariance gives `(y,rho^X_n(beta)x) in Pi_n`, so the
`P`-part gives equal contextual readouts.  Orbit-injectivity forces
`rho^X_n(beta)x=x`.

## Current Sharp Positive Target

A proof of A by this route now needs exactly:

```text
For every finite bijective YBE solution X, the contextual quotient P_X admits
nonempty E_p subseteq Sym(P_X) satisfying extension and transport;
J_n:X^n -> P_X^n is braid-orbit-injective for every n.
```

The previous one-copy condition `L_{lambda_p(q)}=L_p L_q L_p^{-1}` is the
special case `E_p={L_p}`.  The new condition is weaker and is the correct
finite augmented-rack completion problem.

## Current Negative Target

A negative route should find a fixed finite `X` where either:

1. no nonempty transport-stable extension fibers `E_p` exist; or
2. such fibers exist but the contextual readout fails all-arity orbit
   separation in a way that produces actual Brunnian detector-kernel braid
   witnesses.
