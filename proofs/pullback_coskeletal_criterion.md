# Pullback-coskeletal criterion

Date: 2026-06-03

The finite-base pullback route has two different finiteness statements, and
they must not be conflated.

## Fixed base compactness

Fix one proposed finite operator-label base `B`.  For each arity cutoff `N`,
let

```text
S_N(B)
```

be the finite set of choices through arity `N` consisting of:

- comparison maps from the YBE point-pushing action groupoids to `B`;
- vertical coefficient labels over `B`;
- section-change cochains;
- equations saying that the observed deletion `2`-cocycle is gauge-equivalent
  to a pullback from `B` through arity `N`.

If the restriction maps `S_{N+1}(B) -> S_N(B)` are part of the data and every
`S_N(B)` is nonempty, then compactness/König's lemma gives an all-arity branch
for that fixed base.  Conversely, if some `S_N(B)` is empty, this is a genuine
finite obstruction to that fixed base.

## No automatic bounded cutoff

The compactness statement does not imply that there is one bounded arity `d`
such that `S_d(B) nonempty` already forces all higher `S_N(B)` to be nonempty.
Such a cutoff requires an extra finite-type statement:

```text
the comparison tower is d-pullback-coskeletal.
```

Concretely, the higher deletion cocycles, coefficient transports, and
section-gauge relations must be forced by the `d`-skeleton.  Without that
coskeletality or a noetherian replacement, new independent gauge/pullback
constraints can first appear in arbitrarily high arity.

## Consequence for the route

The prefix finite-base/gauge audit is therefore a legitimate low-dimensional
pressure test, not a positive theorem.  A negative result for a fixed base can
be certified by an empty finite gauge/pullback system.  A positive all-arity
result needs either:

- a proof of the pullback-coskeletal lemma for finite YBE point-pushing
  deletion towers; or
- a different all-arity construction of one fixed finite group-Hurwitz base
  and compatible section-gauge data.

The generated ledger

```text
proofs/pullback_coskeletal_criterion_audit.md
```

records this boundary explicitly.
