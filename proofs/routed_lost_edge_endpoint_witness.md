# Routed lost-edge endpoint witness obligations

Date: 2026-05-29

This note follows `proofs/lost_edge_external_routing.md`.  It does not prove
the Master Local-Minimal Residual Theorem.  It connects the lost-edge routing
ledger to the existing endpoint-longitude expression certificate.

The previous note records which seed-saturation edges are externally routed.
This note records what still has to be proved for those routed edges: each
routed edge must be controlled by a fixed endpoint detector factor whose
endpoint lies in the recursive-longitude value subgroup.

## Setup

Let `R` be a lost-edge external routing audit.  Its routed edges are finite
triples

```text
(a,x,y)
```

where the descent quotient collapses `x` and `y`, but a separate external
routing label distinguishes them.

For a routed edge, an endpoint witness is a product endpoint-expression audit
in fixed finite groups

```text
H_1 x ... x H_m
```

of the form already recorded in
`proofs/endpoint_longitude_expression_certificate.md`.  Concretely, it gives
assignments `F_n -> H_i` and recursive-longitude words whose evaluated product
is the endpoint tuple attached to the routed edge.

## Lemma: routed edge witnesses are product-detector obligations

If every routed lost edge has a product endpoint-expression witness, then the
external routing ledger is compatible with the fixed product detector
framework.

Proof.  The lost-edge routing audit only asserts that the external labels
distinguish the finite edges collapsed by the descent quotient.  For each such
edge, the endpoint-expression audit proves that the corresponding endpoint
tuple lies in

```text
V_beta(H_1 x ... x H_m).
```

The endpoint product-expression certificate constructs the direct-product
longitude subgroup witness explicitly.  Therefore identity finite-longitude
data in the product group kills the endpoint tuple.  Since the routing labels
are external and are not inserted back into the descent quotient, this
endpoint killing preserves the strand-continuing quotient while recording the
collapsed information in fixed detector factors.  QED.

## Guardrail

This is still not a complete A proof.  The audit only checks supplied routed
edges and supplied endpoint witnesses.  A complete local theorem must prove
that all routed edges arising in every braid-index residual context have such
witnesses uniformly in `n`, with detector factors depending only on the
interval and quotient detector.

Nor is a missing witness outcome B.  It is only a finite seed until it is
upgraded to a normalized-law sequence invisible to every finite group while
moving a residual tuple.

## Code certificate

The helper

```text
routed_lost_edge_endpoint_witness_audit(routing_audit, edge_endpoint_audits)
```

records:

- the lost-edge external routing audit;
- the endpoint product-expression audit supplied for each routed edge;
- which routed edges have valid endpoint witnesses;
- which routed edges are missing witnesses;
- whether any witness is attached to an edge not routed by the ledger.

Its property

```text
proves_routed_lost_edge_endpoint_visibility
```

is true only when:

1. the external routing ledger itself passes;
2. every supplied endpoint audit proves product endpoint detector membership;
3. every routed edge has a witness;
4. no witness is attached to an unrelated edge.

## Updated A-route burden

The descent-separation route now has three distinct finite layers:

1. descent quotient labels make the quotient row strand-continuing;
2. external routing labels distinguish the edges lost by saturation;
3. endpoint-longitude witnesses prove those routed labels are visible to fixed
   interval-level detector factors.

Only the third layer is an all-`n` endpoint-factorization theorem.  The first
two layers are finite local ledgers.
