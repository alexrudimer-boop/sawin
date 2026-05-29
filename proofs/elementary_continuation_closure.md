# Elementary continuation closure

Date: 2026-05-29

This note sharpens `proofs/continuation_congruence_descent_gate.md`.  It does
not prove descent separation, and it does not prove the Master Local-Minimal
Residual Theorem.  It proves that a genuine local-minimal continuation
obstruction cannot be collective-only: every individual nontrivial
continuation seed already generates the all-universal admissible congruence.

## Setup

Work in the rack-base convention

```text
R_A(a,b) = (a*b, a).
```

For a local interval, write

```text
T_{a,b}(x,y) = (u,v),
```

where `x in A_a`, `y in A_b`, `u in A_{a*b}`, and `v in A_a`.

A continuation seed is a nontrivial pair

```text
x ~ v
```

arising from a row with `v != x`.  Let

```text
Theta(x,v)
```

be the least admissible congruence family containing this single pair.  It is
computed by closing the pair under all local tables and inverse local tables.

The executable helper is:

```text
continuation_seed_pair_closure_audits(interval)
```

and the failure list is:

```text
continuation_seed_pair_closure_failures(interval).
```

## Lemma

If the interval is local-minimal and `(x,v)` is a nontrivial continuation
seed, then

```text
Theta(x,v) = universal.
```

Proof.  By construction, `Theta(x,v)` is an admissible congruence family: it
is the intersection of all admissible congruence families containing the seed,
equivalently the finite closure obtained by transporting product relations
through every local table and inverse local table.

The seed is nontrivial, so `Theta(x,v)` is not the all-equality family.  In a
local-minimal interval, the only admissible congruence families are all
equality and all universal.  Therefore the only remaining possibility is the
all-universal family.  QED.

## Consequence

The universal-continuation branch is now elementary.

It is not enough for all continuation seeds together to generate the universal
corridor.  In a valid local-minimal target, each individual non-strand-
continuing row already opens the universal corridor by itself.

Thus a positive proof of descent separation may work seed-by-seed:

```text
for each representative continuation seed row, prove its universal closure is
visible in the fixed Green/Schutzenberger/atom readouts.
```

And a negative proof must start from one such elementary seed:

```text
choose a continuation seed whose single-pair closure is universal, then
upgrade the resulting motion to a normalized-law sequence invisible to every
finite group.
```

This combines with `proofs/chart_transport_collapse.md`: after choosing one
representative in each finite chart-conjugacy orbit of elementary
continuation seeds, transported copies require no separate certificate because
ordinary `V_beta(G)` membership is closed under finite chart conjugation.

## Diagnostic meaning of failures

If `continuation_seed_pair_closure_failures(interval)` is nonempty, then at
least one continuation seed has a proper or semisplit/mixed closure.  Such an
interval is not a valid local-minimal endpoint for the Master Local-Minimal
Residual Theorem.  It must be refined along that congruence before one invokes
the local theorem.

This is not finite-search proof of A.  It is a finite exact gate that removes
collective continuation closures from the final obstruction list.
