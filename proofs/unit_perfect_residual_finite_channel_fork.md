# Unit perfect-residual finite-channel fork

Date: 2026-05-30

This note follows
`proofs/unit_perfect_residual_symmetric_dichotomy.md`.  It does not prove
Sawin finite-rack domination and it does not construct outcome B.  It removes
one more bookkeeping ambiguity in the terminal unit branch: a local interval
has only finitely many terminal perfect-residual readout channels, so either
one fixed symmetric detector kills all of them at once, or their failures
already form an unbounded symmetric-tail normalized-law seed.

## Setup

Fix a local interval

```text
pi:X -> Z
```

with quotient rack detector `Q`, and set

```text
N_n = ker rho_{Q,n}.
```

Let the terminal nonsolvable unit readout channels be indexed by a finite set
`C`.  For each `c in C`, let

```text
P_c
```

be the stable perfect residual of the corresponding fixed interval-level unit
group, and let

```text
S_c(beta,z,x) in P_c
```

be the final perfect-residual endpoint readout.

Assume the family is faithful in the channel sense:

```text
some S_c(beta,z,x) != 1
    => Delta_n(beta) != 1.
```

This is exactly the terminal-unit part of the faithful residual decomposition
required by `proofs/descent_endpoint_repair_contract.md`.

Put

```text
p = max_{c in C} |P_c|.
```

If `C` is empty, there is no nonsolvable terminal-unit perfect-residual
obstruction.

## The finite-channel fork

Exactly one of the following holds.

1. There exists an integer `m >= p` such that for every `n`,

   ```text
   beta in N_n cap K_{S_m}(n)
       => S_c(beta,z,x)=1 for every c in C
   ```

   and every completed-context terminal readout.

2. For every `j >= p`, there are `n_j`, `alpha_j in N_{n_j} cap
   K_{S_j}(n_j)`, a channel `c_j in C`, and a completed context `(z_j,x_j)`
   such that

   ```text
   S_{c_j}(alpha_j,z_j,x_j) != 1.
   ```

Proof.  If (1) fails, then no `S_j` with `j>=p` kills the whole finite family.
For each such `j`, choose a failed row.  Since the family is finite, that row
has some channel `c_j` with nonidentity endpoint, giving (2).

Conversely, (2) rules out every proposed `m>=p` by taking `j=m`.  QED.

## Normalized-law consequence

Assume case (2).  For each row, `j>=p>=|P_{c_j}|`, so the symmetric seed lemma
gives

```text
K_{S_j}(n_j) subset K_{P_{c_j}}(n_j).
```

Thus each row has identity finite-`P_{c_j}` longitude data while its
perfect-residual endpoint is nonidentity.  By family faithfulness,

```text
Delta_{n_j}(alpha_j) != 1.
```

Right-stabilize by adding `j` unused strands:

```text
q_j = n_j+j,
beta_j = iota_j(alpha_j).
```

Then `q_j -> infinity`, `beta_j in N_{q_j}`, and the residual movement
persists after extending the moved tuple by fixed fibre entries.

For every finite group `G`, let `g=|G|`.  For all `j>=max(p,g)`,

```text
beta_j in K_{S_j}(q_j) subset K_{S_g}(q_j) subset K_G(q_j).
```

So the stabilized sequence is eventually invisible to every finite group while
still moving the residual action.  This is the normalized-law shape required
by the global-local fork.

Because `C` is finite, an equivalent sub-sequence formulation is also
available: some channel `c` occurs for infinitely many `j`, and that channel
alone supplies an unbounded symmetric-tail seed.  The full varying-channel
sequence is already sufficient for outcome B once an explicit interval and
explicit rows are supplied.

## Consequence for A

To close all nonsolvable terminal-unit channels positively, it is enough to
prove a fixed symmetric degree for each channel.  If channel `c` is killed by
`S_{m_c}`, then

```text
M = max_c m_c
```

kills all channels simultaneously, because the symmetric tower is descending:

```text
K_{S_M}(n) subset K_{S_{m_c}}(n)
```

for every `c`.

Thus the terminal perfect-residual family has no separate global obstruction:
either it contributes fixed finite symmetric detector factors to outcome A, or
it supplies the normalized-law seed shape for outcome B.

The remaining hard work is unchanged: prove the fixed detector bound for every
endpoint channel in every local-minimal bottleneck interval, or realize the
second alternative in one explicit finite YBE interval.
