# Triangular bundle recovery inverse

Date: 2026-05-30

This note follows
`proofs/constant_section_triangular_bundle_partition.md`.  It does not prove
the Master Local-Minimal Residual Theorem.  It identifies the exact inverse
formula for a bijective constant-section triangular row and splits triangular
bundle holonomy into block-label recovery plus within-block companion
transport.

## Setup

Let

```text
T_{a,b}: A_a x A_b -> A_c x A_d
```

be a left constant-section triangular row

```text
T_{a,b}(x,y) = (alpha(x), beta_x(y)).
```

The preceding bundle-partition note proves that `alpha` is surjective, each
`beta_x` is injective, and for every `u in A_c` the blocks

```text
B_x = beta_x(A_b),   x in alpha^{-1}(u),
```

partition `A_d`.

## Recovery map

For each `u in A_c`, define the block-label recovery map

```text
r_u:A_d -> alpha^{-1}(u)
```

by the rule

```text
r_u(v)=x  iff  v in beta_x(A_b).
```

This is well-defined because the `B_x` form a partition of `A_d`.

Then define the within-block coordinate recovery

```text
s_{u,v}= beta_{r_u(v)}^{-1}(v).
```

The inverse of the triangular row is exactly

```text
T_{a,b}^{-1}(u,v) = (r_u(v), s_{u,v}).
```

Proof.  By definition, `v in beta_{r_u(v)}(A_b)`, so
`s_{u,v}` is the unique element of `A_b` with

```text
beta_{r_u(v)}(s_{u,v})=v.
```

Also `r_u(v) in alpha^{-1}(u)`, so

```text
alpha(r_u(v))=u.
```

Therefore

```text
T_{a,b}(r_u(v),s_{u,v})=(u,v).
```

Since `T_{a,b}` is bijective, this is the unique preimage.  QED.

The side-dual row

```text
T_{a,b}(x,y)=(lambda_y(x), gamma(y))
```

has the analogous inverse: for each `v in A_d`, the blocks
`lambda_y(A_a)` with `y in gamma^{-1}(v)` partition `A_c`; the output
`(u,v)` first recovers the unique `y` whose block contains `u`, and then
recovers `x=lambda_y^{-1}(u)`.

## Consequence for holonomy

Triangular bundle holonomy has only two finite components:

1. the block-label component `r_u(v)`, choosing which member of the constant
   fibre carried the input distinction;
2. the within-block component `beta_{r_u(v)}^{-1}(v)`, recovering the original
   companion-coordinate input.

Thus a constant-section triangular bottleneck cannot hide arbitrary endpoint
motion.  Any residual movement must be a finite transport of these recovery
labels and within-block companion coordinates.

The positive proof target is now sharper:

```text
Triangular recovery holonomy theorem.
```

Every local-minimal bottleneck interval with triangular bundle rows must show
that the block-label recovery maps and within-block companion transports are
visible in fixed Green, Schutzenberger, atom, endpoint/unit, quotient, or
known-branch factors, or else descend to a strand-continuing transport rack.

If that theorem holds, the previous product-detector and sharp-obstruction
assembly gives the finite rack promised by outcome A.

## Updated B seed

A B route must now exhibit a triangular bundle whose recovery maps

```text
r_u(v)
```

and within-block inverse coordinates

```text
beta_{r_u(v)}^{-1}(v)
```

assemble into a normalized-law sequence invisible to every finite group while
still moving a residual tuple.  A nontrivial bundle partition alone is not
enough.

## Executable audit

The helper

```text
triangular_recovery_audit(interval)
```

records every constant-section triangular row and its inverse recovery table.
For each output pair it stores:

- the output pair `(u,v)`;
- the recovered source pair `(x,y)`;
- whether the recovery formula is total;
- whether the recovery table is bijective.

The aggregate property

```text
every_recovery_formula_bijective
```

checks all triangular rows in the interval.  This is a row-level certificate
for the inverse formula.  It is not a proof of the all-`n` theorem; it
identifies the exact finite recovery data that must be longitudinalized or
turned into a normalized-law obstruction.
