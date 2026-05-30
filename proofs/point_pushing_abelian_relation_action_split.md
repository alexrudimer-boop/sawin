# Point-Pushing Abelian Relation Action Split

Date: 2026-05-30

This note refines the abelian-chief relation-module branch from
`proofs/point_pushing_abelian_chief_relation_module.md`.

It does not prove outcome A or B.  It splits the abelian relation-module tail
by the action of the detector orbit group on the chief layer.

## Setup

Use the notation of `proofs/point_pushing_abelian_chief_relation_module.md`.
Thus `F_C` is the transporter-indexed free group, `mu_D:F_C->N_D` is the
detector orbit map, and

```text
R = ker(mu_D).
```

In a minimal abelian-chief first failure, the monolith is

```text
M ~= C_p^r,
```

and the vertical relation image gives a surjective module quotient

```text
Rel_D tensor F_p ->> M,
Rel_D = R/[R,R].
```

The conjugation action of `F_C` on `M` factors through `N_D`.

## Theorem

Exactly one of the following holds.

1. **Central trivial-module tail.**

   The `N_D`-action on `M` is trivial.  Then

   ```text
   |M|=p,
   ```

   and the relation-lift map factors through the coinvariants:

   ```text
   (Rel_D tensor F_p)_{N_D} ->> M ~= F_p.
   ```

2. **Noncentral irreducible-module tail.**

   The `N_D`-action on `M` is nontrivial.  Then `M` is a nontrivial irreducible
   `F_p[N_D]`-module and

   ```text
   [N_D,M]=M.
   ```

## Proof

The action of `N_D` on `M` is induced by conjugation in the minimal quotient
`H`.  Since `M` is the unique minimal nontrivial normal subgroup of `H`, every
nonzero `N_D`-stable subgroup of `M` is a nontrivial normal subgroup of `H`
contained in `M`.  Hence it is all of `M`.  Thus `M` is irreducible as an
`F_p[N_D]`-module.

If the action is trivial, then every subgroup of the elementary abelian group
`M` is `N_D`-stable, hence normal in `H`.  By uniqueness of the minimal normal
subgroup, `M` has no proper nonzero subgroup.  Therefore `M ~= F_p`.

For trivial action, the equivariant relation map

```text
Rel_D tensor F_p -> M
```

kills all elements of the form `n.x-x`; equivalently it factors through the
coinvariant module

```text
(Rel_D tensor F_p)_{N_D}.
```

Since the row is a vertical failure, the induced map is nonzero, and since
`M ~= F_p` it is surjective.

If the action is nontrivial, then `[N_D,M]` is a nonzero `N_D`-stable subgroup
of `M`; irreducibility forces `[N_D,M]=M`.  The quotient from
`Rel_D tensor F_p` is therefore onto a nontrivial irreducible module.  QED.

## Consequence For The Fork

The abelian side of a product-prefix B tail is now exactly one of:

1. a central one-dimensional trivial coinvariant relation quotient;
2. a noncentral irreducible relation-module quotient with `[N_D,M]=M`.

The cyclic p-power quotient branch is already closed by
`proofs/point_pushing_cyclic_tail_closure.md`.  Thus a surviving central
abelian tail is a stem/coinvariant relation phenomenon, not a large cyclic
quotient phenomenon.

The remaining complete fork is:

```text
central trivial coinvariant relation tails,
noncentral irreducible relation-module tails,
nonabelian simple-power relation-group tails.
```

Rule out all three uniformly for finite YBE point-pushing action images and
outcome A follows from the product-prefix criterion.  Construct one explicit
infinite tail of any one type and outcome B follows after right stabilization.

## Audit Hook

The helper

```text
point_pushing_abelian_relation_action_split_audit(...)
```

records the finite central/noncentral split for an abelian-chief row.  It
labels valid rows as either

```text
central_trivial_coinvariant
noncentral_irreducible_module
```

and rejects data that do not represent an elementary-abelian unique minimal
normal subgroup with surjective relation image.
