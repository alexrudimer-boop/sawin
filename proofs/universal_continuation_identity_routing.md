# Universal continuation identity routing

Date: 2026-05-31

This note refines the descent-endpoint repair target for the remaining
universal-continuation branch.  It does not prove `[Resolution: A]` or
construct `[Resolution: B]`.  It identifies the canonical finite lost-edge
ledger that every endpoint proof must control.

## Executable object

The helper

```text
universal_continuation_identity_routing_audit(I)
```

uses the equality readout

```text
r_a(x)=x
```

as the descent candidate and also as the external routing labels.  It then
runs

```text
lost_edge_external_routing_audit(I, r, r).
```

The audit records:

```text
equality_descent_readout
saturation_is_universal
has_nontrivial_continuation_seed
identity_routing_is_admissible
routes_all_saturation_lost_edges
lost_edges_match_saturation
has_required_lost_edges
routed_unrouted_edges_partition_lost_edges
routed_edges_are_distinguished
unrouted_edges_are_not_distinguished
proves_identity_routed_universal_continuation
```

The post-linear finite-system wrapper reports:

```text
universal_continuation_identity_lost_edges
universal_continuation_identity_unrouted_edges
universal_continuation_identity_routing_proved
```

## Lemma: identity labels route every lost edge

[Proved] Suppose the equality descent readout has a nontrivial continuation
seed whose seed-saturation is universal.  Then the identity external readout
routes every edge lost by the saturation.

Proof.  The equality readout has equality kernel, so it distinguishes every
distinct pair in every fibre.  The seed-saturation lost edges are precisely
the distinct pairs added by the generated admissible closure beyond equality.
Since the external routing labels are again `x |-> x`, each lost edge
`(a,x,y)` has different external labels on `x` and `y`.  Thus every lost edge
is routed.  QED.

## Certificate guardrails

[Proved, audit-side] A supplied external routing ledger is not accepted
vacuously.  The ledger must satisfy all of the following finite checks:

```text
lost_edges = seed_saturation.new_saturation_edges
routed_edges union unrouted_edges = lost_edges
routed_edges cap unrouted_edges = empty
each routed edge is distinguished by the routing labels
each unrouted edge is not distinguished by the routing labels
```

When the local-minimal dichotomy forces universal collapse, the lost-edge
ledger must also be nonempty.  Thus an empty supplied ledger cannot prove a
forced universal-continuation route and cannot close System C.

## Consequence for the repair contract

In the universal-continuation branch, the finite local part of descent
separation can always be expressed by the canonical pair:

```text
descent readout: equality labels, then seed-saturate;
external routing: identity labels on the original fibres.
```

If local minimality forces the seed-saturation to be universal, the descent
quotient collapses all fibre data and becomes strand-continuing.  The identity
external routing ledger lists exactly which original fibre distinctions were
lost.

Therefore the remaining work is not to find more finite lost edges; it is to
prove endpoint-longitude visibility for the identity-routed edges:

```text
for every routed edge (a,x,y), supply fixed finite endpoint factors and
all-n V_beta witnesses that distinguish x from y.
```

This is exactly the external endpoint part of
`proofs/descent_endpoint_repair_contract.md`.  The supplied-certificate helper
is now recorded in
`proofs/universal_continuation_identity_endpoint_witness.md`: once fixed
endpoint factors and recursive-longitude witnesses are supplied for these
identity-routed edges, the helper checks that the endpoint package covers the
ledger and can be fed directly to the repair-contract audit.

## Exact remaining fork

[Open] To prove `[Resolution: A]`, construct fixed endpoint groups and
recursive-longitude witnesses for every edge in
`universal_continuation_identity_lost_edges`, uniformly in braid index.

To prove `[Resolution: B]`, choose an explicit interval where one such
identity-routed edge has no fixed endpoint witness and upgrade that finite
failure to a normalized-law sequence invisible to every finite group while
moving the edge.
