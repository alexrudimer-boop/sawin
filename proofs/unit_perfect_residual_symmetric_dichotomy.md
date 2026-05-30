# Unit perfect-residual symmetric dichotomy

Date: 2026-05-30

This note follows `proofs/unit_perfect_residual_symmetric_seed.md`.  It does
not prove the terminal unit theorem and it does not construct outcome B.  It
records the exact all-`n` dichotomy for one fixed nonsolvable terminal-unit
readout channel.

## Setup

Fix a local interval

```text
pi:X -> Z
```

with quotient rack detector `Q`, and set

```text
N_n = ker rho_{Q,n}.
```

Let `P` be the stable perfect residual of one fixed interval-level terminal
unit group.  Suppose the completed-context proof has identified a terminal
readout

```text
S_P(beta,z,x) in P
```

with the following faithfulness property for this channel:

```text
S_P(beta,z,x) != 1
    => Delta_n(beta) != 1.
```

The positive theorem for this channel asks for a fixed detector degree `m`
such that

```text
beta in N_n cap K_{S_m}(n)
    => S_P(beta,z,x)=1
```

for all `n,beta,z,x`.

## Dichotomy

Exactly one of the following holds.

1. There exists an integer `m >= |P|` such that for every `n`,

   ```text
   beta in N_n cap K_{S_m}(n)
       => S_P(beta,z,x)=1
   ```

   for every completed-context terminal readout in this channel.

2. For every `j >= |P|`, there are `n_j`, `alpha_j in N_{n_j} cap
   K_{S_j}(n_j)`, and a completed-context tuple `(z_j,x_j)` such that

   ```text
   S_P(alpha_j,z_j,x_j) != 1.
   ```

Proof.  If (1) fails, then for every `j >= |P|`, `S_j` is not a detector for
this terminal readout.  Hence there is some degree, braid, and context with
identity `S_j` longitude data but nonidentity endpoint in `P`; this is (2).

Conversely, (2) rules out every `m >= |P|` by taking `j=m`.  Thus (1) and (2)
are mutually exclusive and exhaustive.  QED.

## Relation to normalized laws

Assume case (2).  Since `j >= |P|`, the symmetric seed lemma gives

```text
K_{S_j}(n_j) subset K_P(n_j).
```

Thus each row has identity finite-`P` longitude data and a nonidentity
perfect-residual endpoint.  If the readout is attached to the actual residual
motion by the faithfulness property above, then each row is a one-row
perfect-residual symmetric seed.

Right-stabilizing the row by `j` unused strands gives a braid

```text
beta_j in B_{q_j},      q_j=n_j+j,
```

still in `N_{q_j}`, still moving the residual action, and still invisible to
`S_j`.  The symmetric tower argument then makes the sequence eventually
invisible to every finite group.

Therefore failure of fixed symmetric detection for this one faithful
perfect-residual readout channel already has the correct normalized-law tail
shape.

## Consequence

For a nonsolvable terminal-unit channel, the remaining positive burden can be
stated without product-prefix groups:

```text
find m >= |P| such that K_{S_m} kills S_P uniformly in n,
```

or the channel supplies the symmetric-tail B seed described above.

This is still channel-local.  A full outcome B requires an explicit finite YBE
solution, a concrete local-minimal interval, and the all-tail sequence with
moved residual tuples.  A full outcome A still requires uniform fixed-detector
visibility for every Green/Schutzenberger/atom/unit endpoint channel and a
faithful residual decomposition.
