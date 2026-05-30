# Endpoint family symmetric fork

Date: 2026-05-30

This note follows `proofs/descent_endpoint_repair_contract.md` and
`proofs/symmetric_detector_reduction.md`.  It does not prove the missing
endpoint-longitudinalization theorem.  It records the exact symmetric-detector
fork for any finite family of fixed endpoint groups.

The executable mirror is `endpoint_family_symmetric_fork_audit(...)`.  It
records the finite endpoint factor orders, the left-regular symmetric cutoff,
whether all endpoint witnesses and faithfulness have been supplied, and whether
listed failed symmetric degrees form the finite prefix of the normalized-law
tail shape.

## Setup

Fix a local interval

```text
pi:X -> Z
```

with quotient rack detector `Q`, and put

```text
N_n = ker rho_{Q,n}.
```

Let a proposed faithful endpoint readout use finitely many fixed finite groups

```text
H_1,...,H_t,
```

all depending only on the interval and quotient detector, not on braid index.
For each completed-context endpoint channel `e`, let

```text
h_e(beta,z,x) in H_{s(e)}.
```

Assume the endpoint family is faithful after the transport/readout quotient is
fixed:

```text
some h_e(beta,z,x) != 1
    => Delta_n(beta) != 1
```

for the residual branch under consideration.

Put

```text
m_0 = max_s |H_s|.
```

If the endpoint family is empty, there is no endpoint obstruction.

## Positive symmetric cutoff from endpoint witnesses

Suppose every endpoint channel has the all-`n` witness property

```text
h_e(beta,z,x) in V_beta(H_{s(e)})
```

for every `n`, `beta in N_n`, and completed context.

Then `S_{m_0}` kills every endpoint channel.  Indeed, for `m_0 >= |H_s|`, the
left-regular embedding and symmetric tower monotonicity give

```text
K_{S_{m_0}}(n) subset K_{H_s}(n)
```

for every factor `H_s`.  Thus if `beta in K_{S_{m_0}}(n)`, then
`V_beta(H_s)={1}` for every `s`; the endpoint witness property forces every
`h_e(beta,z,x)` to be identity.

So a fixed endpoint-longitudinalization proof may be converted to one
symmetric detector degree:

```text
beta in N_n cap K_{S_{m_0}}(n)
    => all endpoint channels are identity.
```

Combined with the transport/readout quotient and faithful reconstruction, this
is the endpoint part of the local finite-detector implication.

## Finite endpoint-family dichotomy

Without assuming the witness property, exactly one of the following holds.

1. There exists an integer `M >= m_0` such that for every `n`,

   ```text
   beta in N_n cap K_{S_M}(n)
       => h_e(beta,z,x)=1 for every endpoint channel e
   ```

   and every completed context.

2. For every `j >= m_0`, there are `n_j`, `alpha_j in N_{n_j} cap
   K_{S_j}(n_j)`, a completed context `(z_j,x_j)`, and an endpoint channel
   `e_j` such that

   ```text
   h_{e_j}(alpha_j,z_j,x_j) != 1.
   ```

Proof.  If (1) fails, then no `S_j` with `j>=m_0` kills all endpoints.  For
each such `j`, choose a failed row and one nonidentity endpoint in that row;
this is (2).  Conversely, (2) rules out every `M>=m_0` by taking `j=M`.  QED.

## Normalized-law consequence

Assume case (2) and the endpoint family is faithful.  Right-stabilize each
`alpha_j` by adding `j` unused strands:

```text
q_j = n_j+j,
beta_j = iota_j(alpha_j).
```

Then `q_j -> infinity`, `beta_j in N_{q_j}`, and the moved residual tuple
persists after adding fixed fibre entries.  Also `beta_j in K_{S_j}(q_j)`.

For every finite group `G`, let `g=|G|`.  For all `j>=max(m_0,g)`,

```text
K_{S_j}(q_j) subset K_{S_g}(q_j) subset K_G(q_j).
```

Therefore the sequence is eventually invisible to every finite group while
still moving the residual action.  This is the normalized-law shape required
by the global-local fork.

Because there are only finitely many endpoint channels, some channel occurs
along an unbounded subsequence.  Thus a future B proof may either keep the
varying-channel sequence or pass to one recurrent endpoint channel.

## Consequence for the repair contract

The descent-endpoint repair contract needs endpoint witnesses because they
prove case (1) constructively with the fixed product group

```text
H_endpoint = product_s H_s.
```

This note shows the matching negative alternative: if no fixed symmetric
detector degree kills the finite endpoint family, then the failure already has
the normalized-law tail format.  A bounded endpoint miss remains only a seed;
the all-tail construction is still required for outcome B.
