# Point-Pushing Central Stem Relation Tail

Date: 2026-05-30

This note refines the central trivial branch from
`proofs/point_pushing_abelian_relation_action_split.md`.

It does not prove outcome A or B.  It identifies the remaining central
coinvariant obstruction as a stem central-extension, equivalently a
Schur-multiplier quotient of a finite detector-orbit quotient.

## Setup

Use the notation from `proofs/point_pushing_abelian_chief_relation_module.md`.
Let

```text
mu_D:F_C -> N_D,
R=ker(mu_D),
mu_H:F_C -> H
```

be a minimal central abelian first-failure quotient.  The central action split
gives

```text
M ~= F_p,
mu_H(R)=M,
M <= Z(H).
```

Let

```text
Q = H/M.
```

Since `mu_H` modulo `M` kills `R`, the quotient map `F_C -> Q` factors through
`N_D`.  Thus `Q` is a finite quotient of the detector orbit group.

## Theorem

The central trivial first-failure quotient is a stem central extension:

```text
1 -> F_p -> H -> Q -> 1,
F_p <= Z(H) cap [H,H].
```

Equivalently, the moved central layer is a nonzero quotient of the
`p`-primary Schur multiplier of the detector-orbit quotient `Q`.  In
presentation terms, if `K=ker(F_C->Q)`, then the moved layer is a quotient of

```text
(K cap [F_C,F_C]) / [F_C,K]
```

and the actual first-failure relation map factors through the coinvariants

```text
R/[F_C,R] tensor F_p ->> F_p.
```

## Proof

The central action split already gives `M ~= F_p`, `M<=Z(H)`, and
`mu_H(R)=M`.  The cyclic p-power branch has been closed by
`proofs/point_pushing_cyclic_tail_closure.md`, so a central first-failure
quotient cannot be the abelian cyclic p-power case.  The central monolith
depth split in `proofs/point_pushing_central_monolith_depth.md` therefore
forces

```text
M <= [H,H].
```

Hence

```text
M <= Z(H) cap [H,H],
```

so `H` is a stem central extension of `Q=H/M`.

Now take the free presentation

```text
F_C -> Q,
K=ker(F_C->Q).
```

The Hopf formula identifies the Schur multiplier of `Q` as

```text
H_2(Q,Z) ~= (K cap [F_C,F_C])/[F_C,K].
```

Every stem central extension of `Q` is a quotient of a Schur cover; in this
presentation, its central kernel is obtained by quotienting the Hopf-formula
group.  Since the stem kernel here is `M ~= F_p`, the moved central layer is a
nonzero `p`-quotient of that multiplier.

Finally, because `R<=K` and `mu_H(R)=M`, the actual detector relation lift is
the map

```text
R -> M.
```

Centrality of `M` kills commutators with `F_C`, so this map factors through

```text
R/[F_C,R],
```

and after reducing mod `p` it gives the nonzero coinvariant quotient

```text
R/[F_C,R] tensor F_p ->> F_p.
```

This proves the claim.  QED.

## Consequence For The Fork

The central trivial branch is no longer a generic abelian relation tail.  It
is exactly a stem multiplier tail:

```text
finite quotient Q of N_D,
nonzero p-quotient of H_2(Q,Z),
detector relation coinvariant maps onto F_p.
```

The remaining fork is therefore:

1. central stem multiplier/coinvariant tails;
2. noncentral irreducible relation-module tails;
3. nonabelian simple-wreath coordinate relation-lift tails.

Rule out all three uniformly for finite YBE point-pushing action images and
outcome A follows from the product-prefix criterion.  Construct one explicit
infinite tail of any one type and outcome B follows after right stabilization.

## Audit Hook

The helper

```text
point_pushing_central_stem_relation_audit(...)
```

checks the finite-group bookkeeping for this branch: the central monolith is
contained in the commutator subgroup and the supplied relation image equals
the monolith.  This verifies the finite stem-extension shape of a row; the
symbolic proof above is the all-arity reduction.
