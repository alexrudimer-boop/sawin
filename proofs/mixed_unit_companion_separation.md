# Mixed-unit companion separation

Date: 2026-05-30

This note follows `proofs/two_sided_unit_collapse.md`.  It does not prove the
Master Local-Minimal Residual Theorem.  It turns the phrase "mixed-unit
context recovery" into a finite algebraic ledger: every coordinate-section
collapse in a bijective local row is separated by the companion output
coordinate.

## Setup

Let one coloured local row be

```text
T_{a,b}: A_a x A_b -> A_c x A_d,
T_{a,b}(x,y)=(u,v).
```

The row is a bijection of finite product fibres.  For a fixed `x in A_a`, the
left coordinate section is

```text
L_x^{a,b}: A_b -> A_c,
y |-> pr_1 T_{a,b}(x,y).
```

For a fixed `y in A_b`, the right coordinate section is

```text
R_y^{a,b}: A_a -> A_d,
x |-> pr_2 T_{a,b}(x,y).
```

The remaining continuation obstruction after the two-sided unit collapse is a
row where some coordinate sections are units and some are nonunits, but the
whole local row is still bijective.  Such a row can only recover lost
one-coordinate information through the companion coordinate.

## Lemma: companion output separates every section kernel

Suppose `y_0 != y_1` and

```text
L_x^{a,b}(y_0)=L_x^{a,b}(y_1)=u.
```

Write

```text
T_{a,b}(x,y_i)=(u,v_i).
```

Then

```text
v_0 != v_1.
```

Proof.  If `v_0=v_1`, then

```text
T_{a,b}(x,y_0)=T_{a,b}(x,y_1).
```

Since `T_{a,b}` is injective and `x` is fixed, this forces `y_0=y_1`, a
contradiction.  QED.

The right-section version is identical.  If `x_0 != x_1` and

```text
R_y^{a,b}(x_0)=R_y^{a,b}(x_1)=v,
```

then writing

```text
T_{a,b}(x_i,y)=(u_i,v)
```

gives `u_0 != u_1`.

## Consequence: nonunit is shuttled, not destroyed

A one-sided nonunit section cannot delete information from the bijective local
row.  It only moves the distinction into the companion output.  Therefore a
genuine mixed-unit universal-continuation obstruction has a precise shape:
the residual braid must shuttle section-kernel distinctions through companion
outputs and later recover them before endpoint readout.

Thus the remaining obstruction is not an arbitrary nonunit row.  It is a
finite companion-shuttle path in which every collapse edge

```text
y_0 ~ y_1  with  L_x(y_0)=L_x(y_1)
```

is paired with a separated companion edge

```text
v_0 != v_1,
```

and similarly for right-section collisions.

## Updated A-route target

The positive proof target becomes:

```text
No invisible companion-shuttle cycles.
```

For every local-minimal interval in the
`bi_free_universal_corridor_bottleneck`, every companion-separated
section-kernel distinction must either:

1. be visible in the fixed Green, Schutzenberger, atom, quotient,
   known-branch, or endpoint/unit readout; or
2. enter a strand-continuing transport-state rack after quotienting by those
   readouts.

If this holds, then mixed-unit context recovery cannot supply a new endpoint
obstruction.  The previous transport-rack, Green gauge, unit-continuation, and
product-detector reductions then give the fixed finite detector group
`H(pi,Q)` required by the sharp obstruction theorem.

## Updated B seed

A B route can no longer use a bare nonunit section.  The local seed must be a
companion-shuttle cycle:

```text
section-kernel collapse -> companion separation -> context transport -> endpoint recovery
```

that can be upgraded to braid words

```text
beta_j in B_{q_j},  q_j -> infinity,
```

whose finite-group recursive longitude data is eventually trivial for every
finite group while the shuttle still moves an explicit residual tuple.  A
bounded finite shuttle failure is still only diagnostic evidence.

## Executable audit

The helper

```text
section_kernel_companion_audit(interval)
```

records every section-kernel collision:

- a left-section collision `L_x(y_0)=L_x(y_1)` and the two companion right
  outputs `v_0,v_1`;
- a right-section collision `R_y(x_0)=R_y(x_1)` and the two companion left
  outputs `u_0,u_1`.

For a valid local bijection, every recorded collision must have distinct
companion outputs.  The audit exposes:

```text
has_section_kernel
every_collision_companion_separated
left_section_collision_rows
right_section_collision_rows
```

This helper does not prove the all-`n` theorem.  It identifies the finite
companion-shuttle edges that a future proof must route through fixed readouts,
or that a future counterexample must turn into a normalized-law obstruction
sequence.
