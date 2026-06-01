# Symmetric-tower counterexample certificate

Date: 2026-05-30

This note records the constructive B certificate after the symmetric detector
reduction.  A negative proof no longer has to enumerate all finite groups or
form product prefixes.  It is enough to defeat the symmetric detector tower.

## Global certificate

For a finite YBE solution `X`, a symmetric-tower B certificate consists of, for
every `j>=1`, explicit data:

- an integer `n_j`;
- a braid word `alpha_j in B_{n_j}`;
- a moved tuple `x_j in X^{n_j}`;

such that

```text
Lambda_{S_j,n_j}(alpha_j)=Lambda_{S_j,n_j}(1),
rho_{X,n_j}(alpha_j)(x_j) != x_j.
```

Right-stabilize by adding `j` unused strands:

```text
q_j = n_j+j,
beta_j = iota_j(alpha_j) in B_{q_j}.
```

Since `q_j -> infinity` and right stabilization preserves identity finite
longitude data for the old detector while giving trivial data on the new
strands, the sequence remains invisible to `S_j` at stage `j`.

To see that it is invisible to every finite group, let `H` be finite and put
`h=|H|`.  The left regular embedding gives

```text
K_{S_h}(n) subset K_H(n).
```

For every `j>=h`, the inclusion `S_h -> S_j` by fixed extra points gives

```text
K_{S_j}(n) subset K_{S_h}(n).
```

Hence

```text
beta_j in K_{S_j}(q_j) subset K_{S_h}(q_j) subset K_H(q_j)
```

eventually.  The moved tuple remains moved after stabilization.  Therefore this
is exactly the normalized-law obstruction required by outcome B.

## Local residual certificate

For a local interval `pi:X->Z` with quotient rack detector `Q`, the same
certificate is used with the additional requirements

```text
alpha_j in N_{n_j}=ker rho_{Q,n_j},
Delta_{n_j}(alpha_j) != 1.
```

Choose a moved residual tuple over a fixed base tuple and extend it by any
fixed fibre point on the added strands.  The stabilized braid remains in
`N_{q_j}` because the added strands are unused.

## What this removes

The product-prefix certificate

```text
P_j = G_1 x ... x G_j
```

is still valid, but it is no longer necessary.  A proposed B proof may use the
simpler symmetric tower:

```text
S_1,S_2,S_3,...
```

This removes bookkeeping about enumerating finite groups.  The remaining B
burden is still substantial and all-`n`: one must give a symbolic construction
of the `alpha_j`, prove the identity `S_j` longitude data, and give explicit
moved tuples.

## Executable helpers

The global helper

```text
symmetric_normalized_law_prefix_witness_audit(...)
```

checks one supplied row of the symmetric-tower certificate.

The local helper

```text
local_symmetric_normalized_law_prefix_witness_audit(...)
```

checks the corresponding quotient-kernel and residual-movement conditions for
one local row.
For the local helper, residual movement and base compatibility are derived
from the actual source/stabilized fibre tuples and their images, and the row
requires its finite base-detector and group-longitude checks to be derived
from the supplied tables.  A row with only asserted movement booleans is not a
certificate.

These helpers are finite certificate checks for supplied data.  They do not
construct the required all-`j` sequence.
