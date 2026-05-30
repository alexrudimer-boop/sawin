# Unit perfect-residual normalized seed

Date: 2026-05-30

This note follows
`proofs/unit_continuation_perfect_residual_audit.md`.  It does not prove
outcome B.  It records the exact extra data needed to turn a finite
perfect-residual unit miss into one row of the local normalized-law
counterexample certificate.

## Setup

Let `pi:X->Z` be a local interval with quotient rack detector `Q`, and set

```text
N_n = ker rho_{Q,n}.
```

Let `M` be one fixed finite endpoint or continuation transition monoid in the
terminal-unit channel, let

```text
U = U(M),
```

and let

```text
P = U^(m)
```

be the stable perfect residual of the derived series of `U`.

After all abelian derived quotients have been handled, the remaining endpoint
is an element

```text
S_m(beta,z,x) in P.
```

The positive endpoint theorem must prove

```text
S_m(beta,z,x) in V_beta(P).
```

If this fails for a single finite braid, the failure is still only a bounded
finite miss.  It is not outcome B.

## One-row B seed criterion

A perfect-residual finite miss becomes one row of the local normalized-law
certificate only when it is attached to the following data:

1. a braid `alpha in N_n`;
2. a product-prefix detector `P_j=G_1 x ... x G_j` with identity finite
   longitude data:

```text
Lambda_{P_j,n}(alpha)=Lambda_{P_j,n}(1);
```

3. a moved residual tuple:

```text
Delta_n(alpha) != 1;
```

4. the same braid and completed-context readout produce a nonidentity
   perfect-residual endpoint:

```text
S_m(alpha,z,x) != 1 in P;
```

5. the finite `P` longitude data for that same braid is identity:

```text
V_alpha(P) = {1}.
```

Then this row is a valid local product-prefix B seed.  It remains only one row:
outcome B still requires such rows for every product prefix, or an equivalent
symbolic all-`j` construction.

## Lemma

An all-`j` family of rows satisfying the one-row B seed criterion is a local
normalized-law residual obstruction sequence.

Proof.  The local prefix data are exactly the data in
`proofs/normalized_law_counterexample_certificate.md`: membership in
`N_n`, identity `P_j` longitude data, and a moved residual tuple.  Right
stabilization preserves membership in `N_n`, preserves the moved residual
tuple, and gives `q_j -> infinity`.

For any fixed finite group `G_r`, projection `P_j -> G_r` gives identity
finite-`G_r` longitude data for all `j >= r`.  Hence the stabilized sequence is
eventually invisible to every finite group.  The residual movement persists by
the moved-tuple part of the local prefix certificate.

The nonidentity perfect-residual endpoint identifies where the terminal-unit
motion survives in the supplied row.  It does not replace the local moved tuple;
it ties the terminal-unit miss to the actual residual readout.  QED.

## Executable audit

The helper

```text
unit_perfect_residual_normalized_seed_audit(...)
```

pairs:

- a `local_normalized_law_prefix_witness_audit(...)` row;
- a `unit_perfect_residual_longitude_audit(...)` finite miss;
- an explicit assertion that the two audits use the same braid word;
- an explicit assertion that the perfect-residual endpoint is the terminal
  readout of the moved residual branch.

It returns true for

```text
proves_one_local_perfect_residual_normalized_seed
```

only when all of those checks pass.

The two explicit assertions are intentional.  The finite group computation can
test `S_m notin V_beta(P)` at an identity finite-`P` signature, and the local
prefix computation can test residual movement and product-prefix invisibility,
but neither computation alone knows that the terminal monoid endpoint is the
actual completed-context readout of that moving branch.

## Consequence

The nonsolvable terminal-unit B route now has no ambiguity:

```text
bounded perfect-residual miss
```

is not enough, while

```text
perfect-residual miss + local normalized-law prefix row
```

is exactly one row of the required construction.

Thus the positive route must still prove perfect-residual
recursive-longitude membership uniformly:

```text
S_m(beta,z,x) in V_beta(P).
```

The negative route must give an all-`j` family of the attached rows above.
