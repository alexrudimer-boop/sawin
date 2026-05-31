# Universal continuation symmetric endpoint fork

Date: 2026-05-31

This note follows `proofs/universal_continuation_identity_endpoint_witness.md`
and `proofs/endpoint_family_symmetric_fork.md`.  It does not construct the
missing endpoint witnesses for the universal-continuation channel.  It records
the parallel supplied symmetric-detector certificate for identity-routed
continuation edges.

## Setup

System C is reached when a partial-constant missing triangular row routes to
the universal-continuation seed channel.  The canonical identity routing
ledger records finite lost edges

```text
universal_continuation_identity_lost_edges.
```

The endpoint-expression checker closes this row when each identity-routed edge
has a fixed product endpoint-longitude witness.  The symmetric fork below is
the coarser alternative: one finite endpoint-family symmetric cutoff kills the
whole finite family of identity-routed endpoint channels.

## Executable object

The helper is

```text
universal_continuation_identity_symmetric_endpoint_fork_audit(
    identity_routing,
    endpoint_family,
    covered_edges,
)
```

where `endpoint_family` is an `EndpointFamilySymmetricForkAudit`.

It records:

```text
identity_routing_proved
routed_edges
supplied_covered_edges
missing_identity_routed_edges
extra_covered_edges
proves_universal_continuation_identity_symmetric_endpoint_cutoff
proves_universal_continuation_identity_symmetric_tail_seed_prefix
failure_reasons
```

The covered edge set must match the identity-routed edge set exactly.

## Lemma: keyed symmetric cutoff closes System C

[Proved, supplied-data form] Suppose:

1. the identity routing ledger proves the canonical identity-routed universal
   continuation route;
2. a finite endpoint-family fork proves a faithful symmetric cutoff for the
   fixed endpoint groups used by those continuation edge channels;
3. the covered edge set is exactly the identity-routed lost edge set.

Then System C has no remaining endpoint obligation for this supplied data.

Proof.  The endpoint-family fork says that one symmetric degree kills every
covered endpoint channel.  Exact edge coverage identifies the covered family
with precisely the identity-routed continuation losses.  Faithfulness converts
endpoint identity into residual fixedness for the continuation channel.  No
extra edge is admitted, so no unrelated endpoint certificate is used.  QED.

## Post-linear consequence

[Proved] The post-linear wrapper accepts this symmetric fork as an alternative
System C certificate.  In a C-only endpoint row it returns

```text
closed_by_universal_continuation_symmetric_endpoint_fork.
```

In a product endpoint row, it removes only C from

```text
unclosed_routed_endpoint_systems.
```

Any still-unclosed U or M endpoint family remains the reported finite system.

## Remaining burden

[Open] A supplied symmetric cutoff is not a construction of the uniform
universal-continuation endpoint theorem.  To prove `[Resolution: A]`, one must
show that every local-minimal bottleneck interval supplies such a fixed cutoff
or stronger endpoint-longitude witnesses.  To prove `[Resolution: B]`, one
must turn failure of every symmetric cutoff into the all-tail normalized-law
sequence with residual movement.
