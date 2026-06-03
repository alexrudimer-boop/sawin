# Prefix edge transducer tower

Date: 2026-06-03

This note records the finite transducer repair for the genuinely degenerate
case where some map `lambda_x` is not injective.  It follows
`proofs/edge_memory_tower_prefix.md`.

Let

```text
r(x,y)=(lambda_x(y), rho_y(x)).
```

Let `M_lambda=<lambda_x:x in X>` be the finite transformation monoid generated
by the first-coordinate maps on `X`.  For a tuple `(x_1,...,x_m)`, define
left prefixes

```text
P_0=1,                 P_j=P_{j-1} lambda_{x_j}.
```

The prefix-edge encoding is the path

```text
Phi_m(x_1,...,x_m)
  = ((P_0,x_1,P_1), (P_1,x_2,P_2), ..., (P_{m-1},x_m,P_m)).
```

Each edge remembers the real ordered neighbour colour.  Thus no step asks for
a chosen inverse image under a noninjective `lambda_x`.

## Local move

If `r(x,y)=(u,v)`, the local positive braid move replaces

```text
(P,x,P lambda_x), (P lambda_x,y,P lambda_x lambda_y)
```

by

```text
(P,u,P lambda_u), (P lambda_u,v,P lambda_u lambda_v).
```

This is endpoint-preserving exactly because the left-prefix identity holds:

```text
lambda_x lambda_y = lambda_u lambda_v.
```

For a set-theoretic YBE solution this identity is the first-coordinate
component of the YBE relation.  The code checks it directly from the table.

## Forgetting

Interior point-forgetting is not deletion of one edge.  After deleting the
colour `x_k`, all later prefixes must be recomputed from `P_0=1`.  This is
still finite-state, because the running state is an element of the finite
monoid `M_lambda`.

In the arity-four audit, the fibre of each forgetting map over a retained
prefix path has size at most `|X|`, because the forgotten colour is the only
free choice and all later prefixes are forced by the scan.

## What This Proves

The prefix-edge construction gives a finite braid-compatible transducer tower
for degenerate memory:

```text
X^m  <->  prefix-edge paths in M_lambda.
```

It repairs the derived-rack preimage ambiguity without invoking
left-nondegeneracy.  The generated audit checks:

- injectivity of the arity-3 and arity-4 encodings;
- the left-prefix identity `lambda_x lambda_y=lambda_u lambda_v`;
- arity-four bijectivity of local generator updates;
- the arity-three braid relation on prefix paths;
- well-defined arity-four point-forgetting maps;
- forgetting fibre size bounded by `|X|`.

## What This Does Not Prove

This is not yet the finite augmented Artin-envelope lemma.  The requested
route-(1) lemma needs a fixed finite group `H_X`, a conjugation-stable label
set `C_X subset H_X`, and normal vertical kernels of uniformly bounded
exponent such that

```text
Q_X(n)/V_X(n)
```

is a marked quotient of the group-Hurwitz point-pushing image
`Q_{H_X,C_X}(n)`.

The prefix-edge object is a finite transformation-monoid transducer.  A finite
transducer is not automatically a finite group-Hurwitz base.  The next
theorem gate is therefore:

```text
Can the prefix-edge monoid memory be group-completed to a fixed finite
group-Hurwitz tower up to bounded-exponent vertical noise?
```

If yes, this is the likely first missing lemma.  If no, the obstruction must
be visible in a compatible `Q_X(3), Q_X(4), ...` comparison that separates
finite transducer towers from finite group-Hurwitz towers with bounded
vertical kernels.

## Generated audit

The executable helper is

```text
prefix_edge_transducer_audit(X)
```

and the generated report is

```text
proofs/prefix_edge_transducer_audit.md
```
