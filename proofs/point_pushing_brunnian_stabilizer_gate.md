# Point-Pushing Brunnian Stabilizer Gate

Date: 2026-05-30

This note extracts the first obstruction in
`proofs/point_pushing_brunnian_relation_lift.md`: when is the transported
action label on the detector conjugacy orbit of the new generator
well-defined?

The answer is a stabilizer-centralizer condition.  This does not prove outcome
A or B, but it removes another ambiguity from the one-new-strand extension
problem.

## Setup

At the one-new-strand step, assume the old suffix paired subgroup is already a
graph:

```text
C={(c,q(c)): c in C_D} <= C_D x C_X.
```

Let the new detector/action pair be

```text
e=(d,h).
```

The candidate transported orbit label is

```text
q_e(c d c^{-1}) = q(c) h q(c)^{-1}.
```

Let

```text
Stab_{C_D}(d)={t in C_D: t d t^{-1}=d}
```

and

```text
Cent_{C_X}(h)={s in C_X: s h s^{-1}=h}.
```

## Theorem

The transported orbit label `q_e` is well-defined on the detector conjugacy
orbit of `d` if and only if

```text
q(Stab_{C_D}(d)) <= Cent_{C_X}(h).
```

## Proof

Suppose first that `q_e` is well-defined.  Let

```text
t in Stab_{C_D}(d).
```

Then

```text
t d t^{-1}=d=1 d 1^{-1}.
```

Well-definedness gives

```text
q(t) h q(t)^{-1}=q(1) h q(1)^{-1}=h.
```

Thus `q(t)` centralizes `h`.

Conversely, suppose

```text
q(Stab_{C_D}(d)) <= Cent_{C_X}(h).
```

Let `c_1,c_2 in C_D` satisfy

```text
c_1 d c_1^{-1}=c_2 d c_2^{-1}.
```

Then

```text
t=c_2^{-1}c_1
```

stabilizes `d`.  By hypothesis, `q(t)` centralizes `h`.  Since
`q` is a homomorphism,

```text
q(c_1)=q(c_2)q(t).
```

Therefore

```text
q(c_1) h q(c_1)^{-1}
=q(c_2) q(t) h q(t)^{-1} q(c_2)^{-1}
=q(c_2) h q(c_2)^{-1}.
```

So `q_e` is well-defined.  QED.

## Consequence For Brunnian Witnesses

If this stabilizer-centralizer condition fails, choose

```text
t in Stab_{C_D}(d)
```

with

```text
q(t) h q(t)^{-1} != h.
```

For any word `u in F_k` representing `t`, the right-based Brunnian word

```text
u a_{k+1} u^{-1} a_{k+1}^{-1}
```

has trivial detector value and nontrivial action value.  Thus it is already a
one-new-strand vertical witness in the sense of
`proofs/point_pushing_brunnian_orbit_criterion.md`.

Therefore an A proof must show, uniformly for one fixed detector `S_m`, that
all old-suffix detector stabilizers of the new point-pushing generator map into
the corresponding action centralizer.  A B proof may instead produce an
infinite symmetric-tail family of stabilizer-centralizer failures.

## Remaining Relation-Lift Burden

After the stabilizer-centralizer gate holds, the transported orbit label is
well-defined.  The only remaining one-new-strand obstruction is then a genuine
relation among detector orbit generators that fails among transported action
labels.  That is the second condition in
`proofs/point_pushing_brunnian_relation_lift.md`.

## Audit Hook

The helper

```text
point_pushing_brunnian_orbit_audit(...)
```

now records:

- `detector_stabilizer_size`;
- `stabilizer_centralizes_new_action`;
- `orbit_map_well_defined`.

When the stabilizer-centralizer condition fails, the helper returns the
explicit right-based witness word

```text
u a_{k+1} u^{-1} a_{k+1}^{-1}.
```

The helper is a finite certificate checker; the theorem above is the symbolic
equivalence.
