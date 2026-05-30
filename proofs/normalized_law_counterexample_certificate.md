# Normalized-law counterexample certificate

Date: 2026-05-30

This note records the constructive data needed to turn the normalized-law
domination dichotomy into outcome B.  The dichotomy proves that failure of all
finite group detectors forces a normalized-law obstruction sequence.  Outcome B
still requires an explicit sequence, not only a nonconstructive existence
argument.

## Product-prefix witness data

Fix an enumeration of finite groups up to isomorphism

```text
G_1, G_2, G_3, ...
```

and write

```text
P_j = G_1 x ... x G_j.
```

For a finite YBE solution `X`, a constructive B certificate may give, for every
`j`, explicit data:

- an integer `n_j`;
- a braid word `alpha_j in B_{n_j}`;
- a tuple `x_j in X^{n_j}`;

such that

```text
Lambda_{P_j,n_j}(alpha_j)=Lambda_{P_j,n_j}(1),
rho_{X,n_j}(alpha_j)(x_j) != x_j.
```

Then choose `q_j=n_j+j`, stabilize `alpha_j` by adding `j` unused right
strands, and extend `x_j` by a fixed element of `X`.  The result is the
normalized-law obstruction sequence required by outcome B:

```text
beta_j in B_{q_j},        q_j -> infinity.
```

For every fixed finite group `G_r`, projection `P_j -> G_r` gives identity
finite-`G_r` longitude data for all `j >= r`; right stabilization preserves
the old Artin longitude data and gives empty longitudes on the added strands.
The moved tuple remains moved because the stabilized braid acts on the first
`n_j` strands as `alpha_j`.

Thus a B proof can be presented constructively by supplying the product-prefix
witnesses above.

## What is not enough

A single finite group miss is not outcome B.  A finite list of misses is not
outcome B.  A row-level endpoint failure is not outcome B.  Each of these
becomes relevant only after it is promoted to product-prefix witnesses for
`P_j` for every `j`, or to an equivalent symbolic construction.

This is the difference between:

```text
some proposed detector failed
```

and

```text
every finite group detector fails coherently enough to diagonalize.
```

## Local residual certificate

For a local interval with quotient rack detector `Q`, use the same data but
require

```text
alpha_j in N_{n_j} = ker rho_{Q,n_j}
```

and a moved residual tuple:

```text
Delta_{n_j}(alpha_j) != 1.
```

Right stabilization must preserve membership in `N_n`.  This is automatic for
the standard inclusion by unused right strands: the stabilized braid acts as
`alpha_j` on the first `n_j` quotient coordinates and trivially on the added
coordinates.

## Executable finite-prefix check

The helper

```text
normalized_law_prefix_witness_audit(...)
```

checks one supplied global prefix record:

1. identity finite-longitude signature in the product group `P_j`;
2. identity signatures in the listed factors after projection;
3. right-stabilization preservation of Artin permutation and longitudes;
4. movement of the supplied tuple before and after stabilization.

The property

```text
proves_one_prefix_normalized_law_witness
```

means exactly that this one row has the shape required by the constructive
diagonal argument.  It is not an all-`j` proof by itself.  A final B proof must
give a symbolic construction of such prefix records for every `j`, plus the
explicit finite YBE solution and moved tuples.

