# Point-Pushing Nonabelian-Chief Relation Quotient

Date: 2026-05-30

This note is the nonabelian counterpart of
`proofs/point_pushing_abelian_chief_relation_module.md`.

It does not prove outcome A or B.  It shows that the nonabelian-chief side of
a Brunnian product-prefix first failure is also controlled by the detector
orbit relation group: the relation image surjects onto the simple-power
monolith, and the detector orbit acts on that monolith through outer
automorphisms.

## Setup

Use the same transporter-indexed orbit presentation as in
`proofs/point_pushing_abelian_chief_relation_module.md`.

Let `F_C` be the free group on generators `t_c`, indexed by old suffix
detector elements `c in C_D`.  Let

```text
mu_D:F_C -> N_D=<o_c:c in C_D>
```

be the detector orbit map, and let

```text
R = ker(mu_D).
```

After passing to a finite quotient of the transported action orbit subgroup,
let

```text
mu_H:F_C -> H
```

be the corresponding action-orbit map.  Choose `H` of minimal order among
finite quotients in which a vertical Brunnian failure survives.

By monolithic compression, `H` has a unique minimal nontrivial normal subgroup
`M`, and

```text
1 != mu_H(R) <= M.
```

Assume now that the chief layer is nonabelian:

```text
M ~= S^r
```

for a nonabelian finite simple group `S`.

## Theorem

The relation image surjects onto the nonabelian monolith:

```text
mu_H(R)=M.
```

Moreover, conjugation by `F_C` induces an outer action of `N_D` on `M`.  More
precisely, the homomorphism

```text
F_C -> Out(M)
```

defined by conjugation through `mu_H` factors through `mu_D:F_C->N_D`.

Thus every nonabelian-chief first failure is a relation-group quotient

```text
R ->> S^r
```

with an `N_D`-controlled outer action.

## Proof

Let

```text
V = mu_H(R).
```

As in the abelian-chief note, `V` is normal in `H`.  The minimal quotient
argument gives `1 != V <= M`.  Since `M` is the unique minimal nontrivial
normal subgroup of `H`, the nontrivial normal subgroup `V` must contain `M`.
Together with `V <= M`, this gives

```text
V=M.
```

Now consider the conjugation action on `M`.  Each `f in F_C` acts by

```text
x |-> mu_H(f) x mu_H(f)^{-1}.
```

If `f_1` and `f_2` have the same image in `N_D`, then

```text
f_2^{-1} f_1 in R.
```

Applying `mu_H`, we get

```text
mu_H(f_2)^{-1} mu_H(f_1) in mu_H(R)=M.
```

Therefore the automorphisms of `M` induced by `f_1` and `f_2` differ by an
inner automorphism of `M`.  Their classes in `Out(M)` are equal.  Hence the
outer conjugation action factors through `N_D`.

This proves the theorem.  QED.

## Consequence For The Fork

After the abelian-chief linearization and this nonabelian-chief quotient
compression, every product-prefix B tail has a subsequence of exactly one of
the following two forms.

1. **Abelian relation-module tail.**

   ```text
   Rel_D tensor F_p ->> M ~= C_p^r.
   ```

2. **Nonabelian relation-group tail.**

   ```text
   R ->> M ~= S^r,
   ```

   with the detector orbit group `N_D` controlling the outer action on `S^r`.

The earlier nonabelian parameter split still applies to the second case:
either the simple factors `S_j` escape in size, or a fixed simple factor occurs
with multiplicity `r_j -> infinity`.

So the remaining positive target is no longer phrased in terms of arbitrary
large action quotients.  It is:

```text
rule out unbounded irreducible abelian quotients of detector relation modules,
and rule out unbounded simple-power quotients of detector relation groups.
```

Conversely, an explicit infinite tail of either type gives outcome B after
right stabilization by the product-prefix obstruction theorem.

## Audit Hook

The helper

```text
point_pushing_nonabelian_chief_relation_quotient_audit(...)
```

checks the finite-group bookkeeping for a nonabelian-chief row: the supplied
monolith is nonabelian and normal, the relation image is nontrivial and normal,
and the relation image equals the monolith.  The helper takes the
unique-minimal-normal assertion as an explicit input so that large simple
groups can be audited without enumerating all normal subgroups.  The symbolic
proof above is the all-arity reduction.
