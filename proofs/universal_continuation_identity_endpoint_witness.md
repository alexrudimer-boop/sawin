# Universal continuation identity endpoint witnesses

Date: 2026-05-31

This note refines `proofs/universal_continuation_identity_routing.md` by making
the endpoint-witness layer executable.  It is a supplied-certificate theorem:
it checks a proposed endpoint package for the canonical identity-routed
universal-continuation ledger.  It does not construct the missing endpoint
witnesses and therefore does not by itself prove `[Resolution: A]`.

## Executable object

The helper

```text
universal_continuation_identity_endpoint_witness_audit(
    identity_routing,
    edge_endpoint_audits,
)
```

takes:

```text
identity_routing:
    UniversalContinuationIdentityRoutingAudit

edge_endpoint_audits:
    pairs ((colour, left, right), EndpointProductExpressionAudit)
```

and internally runs

```text
routed_lost_edge_endpoint_witness_audit(
    identity_routing.routing,
    edge_endpoint_audits,
).
```

The returned audit records:

```text
identity_routing_proved
endpoint_witnesses_proved
routed_witness_uses_identity_routing
routed_edges
witnessed_edges
missing_identity_routed_edges
extra_witness_edges
failure_reasons
proves_universal_continuation_identity_endpoint_witnesses
```

It also exposes the generic repair-contract interface:

```text
routing_audit
proves_routed_lost_edge_endpoint_visibility
```

so the same object can be supplied directly to
`descent_endpoint_repair_contract_audit(...)`.

## Lemma: supplied witnesses close the identity ledger

[Proved, supplied-data form] Suppose:

1. `identity_routing.proves_identity_routed_universal_continuation`;
2. every edge in `identity_routing.routing.routed_edges` is paired with an
   `EndpointProductExpressionAudit` proving product endpoint visibility by
   recursive-longitude expression;
3. no endpoint witness is supplied for an edge outside that identity-routed
   ledger.

Then

```text
proves_universal_continuation_identity_endpoint_witnesses = True.
```

Proof.  The generic routed-edge witness audit already proves exactly the
second and third conditions against its supplied `routing_audit`.  The
identity wrapper constructs that generic audit using precisely
`identity_routing.routing`, and separately requires the canonical
universal-continuation identity routing theorem.  Hence the checked endpoint
witnesses close every edge lost by the identity saturation and no unrelated
edge has been mixed into the certificate.  QED.

## Repair-contract consequence

The descent-endpoint repair checker now accepts either the generic
`RoutedLostEdgeEndpointWitnessAudit` or the identity-specific wrapper.  In the
identity-specific case, the repair contract checks:

```text
descent separation proved,
endpoint residual action proved,
identity-routed lost edges endpoint-visible,
supplied descent == identity_routing.routing.dichotomy.seed_saturation.saturated_descent.
```

Thus the local finite ledger for universal continuation has the following
executable shape:

```text
identity routing audit
  -> identity-routed edge endpoint witness audit
  -> descent endpoint repair contract audit
```

Any successful certificate now proves the whole supplied-data repair package
for that edge set, including the endpoint visibility obligations.

## Exact remaining fork

[Open] To prove `[Resolution: A]`, construct the missing fixed endpoint factors
and all-`n` recursive-longitude witnesses for every edge in
`universal_continuation_identity_lost_edges`, then feed them to the audit
above.

[Open] To prove `[Resolution: B]`, exhibit an identity-routed edge for which no
such fixed endpoint package exists and upgrade that finite failure to the
normalized-law obstruction sequence.
