# Unit perfect-residual symmetric seed

Date: 2026-05-30

This note is the symmetric-tower version of
`proofs/unit_perfect_residual_normalized_seed.md`.  It does not prove outcome
B.  It removes product-prefix bookkeeping from the nonsolvable terminal-unit
B route.

## Setup

Let `pi:X->Z` be a local interval with quotient rack detector `Q`, and let
`P` be the stable perfect residual of a fixed terminal unit group `U(M)`.

The product-prefix seed note says that a finite perfect-residual miss becomes a
valid local B seed only when it is attached to a local normalized-law prefix
row.  The symmetric detector reduction permits a simpler row:

```text
alpha_j in N_n cap K_{S_j}(n),
Delta_n(alpha_j) != 1.
```

Here

```text
K_G(n) = { beta : Lambda_{G,n}(beta)=Lambda_{G,n}(1) }.
```

## Lemma: symmetric invisibility covers the perfect residual

If `j >= |P|`, then for every braid index `n`,

```text
K_{S_j}(n) subset K_P(n).
```

Proof.  Embed `P` into `S_|P|` by the left regular representation, and embed
`S_|P|` into `S_j` by fixing the last `j-|P|` points.  If
`beta in K_{S_j}(n)`, then every recursive Artin longitude evaluates to the
identity under every assignment `F_n -> S_j`.  Composing any assignment
`F_n -> P` with these two embeddings gives such an assignment into `S_j`.
Injectivity of the embeddings forces the original `P`-values to be identity.
Thus `beta in K_P(n)`.  QED.

## One-row symmetric B seed

A finite row in the perfect-residual terminal-unit channel has the symmetric
seed shape when it supplies:

1. a local symmetric prefix row with detector `S_j`;
2. right stabilization by exactly `j` unused strands;
3. a nonidentity terminal endpoint `S_m(alpha,z,x) in P`;
4. the same braid and same completed-context readout as the moved local
   residual tuple;
5. `j >= |P|`.

The degree condition is harmless for an all-`j` construction.  Since `P` is a
fixed finite interval-level group, discarding the finitely many rows with
`j<|P|` does not affect eventual invisibility to every finite group.

## Executable audit

The helper

```text
unit_perfect_residual_symmetric_seed_audit(...)
```

checks one supplied row.  It verifies:

- the local prefix row uses the declared symmetric group `S_j`;
- the row was right-stabilized by `j` strands;
- `j >= |P|`;
- the perfect-residual audit is a finite identity-signature miss;
- the caller asserts same braid and same terminal readout.

The result

```text
proves_one_local_perfect_residual_symmetric_seed
```

is still only a one-row certificate.  A final B proof must provide a symbolic
family of such rows for unbounded `j`, or otherwise invoke the local symmetric
detector dichotomy to show that no fixed symmetric detector exists.

## Tail-prefix audit

Since the fixed perfect residual has order `|P|`, the symmetric seed certificate
only needs the tail of the symmetric tower:

```text
S_|P|, S_{|P|+1}, S_{|P|+2}, ...
```

The helper

```text
unit_perfect_residual_symmetric_tower_prefix_audit(...)
```

checks a finite supplied tail prefix.  It requires:

- all rows use the same perfect-residual size;
- the symmetric degrees are exactly

```text
|P|, |P|+1, ..., |P|+r-1;
```

- every row passes
  `proves_one_local_perfect_residual_symmetric_seed`.

This is the finite-prefix shadow of a real B proof in this channel.  It still
does not prove outcome B unless a symbolic construction supplies such rows for
the whole infinite tail.

## Consequence

The terminal-unit nonsolvable B route can now be stated without enumerating all
finite groups:

```text
for unbounded j, find residual motion invisible to S_j
whose terminal unit endpoint survives in the fixed perfect residual P.
```

By the lemma and the symmetric-tower certificate, such a family is eventually
invisible to every finite group and defeats every finite rack.  A single
bounded row remains only a seed, not outcome B.
