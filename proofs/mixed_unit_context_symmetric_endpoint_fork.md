# Mixed-unit context symmetric endpoint fork

Date: 2026-05-31

This note follows `proofs/triangular_k_left_coordinate_unit_routing.md` and
`proofs/endpoint_family_symmetric_fork.md`.  It does not construct the missing
mixed-unit endpoint witnesses.  It records the supplied symmetric-detector
alternative for the finite mixed-unit context keys.

## Setup

System M is reached when a coordinate-unit missing triangular row is routed to
mixed-unit context.  Each mixed coordinate-unit side contributes one key

```text
(left_color, right_color, side).
```

The product-expression checker closes M when every key has a fixed product
endpoint-longitude witness.  The symmetric fork below instead certifies that
one symmetric detector degree kills the finite family of mixed-unit endpoint
channels.

## Executable object

The helper is

```text
mixed_unit_context_symmetric_endpoint_fork_audit(
    coordinate_routing,
    endpoint_family,
    covered_keys,
)
```

where `endpoint_family` is an `EndpointFamilySymmetricForkAudit`.

It records:

```text
mixed_context_keys
supplied_covered_keys
missing_mixed_context_keys
extra_covered_keys
coordinate_unit_routing_proved
proves_mixed_unit_context_symmetric_endpoint_cutoff
proves_mixed_unit_context_symmetric_tail_seed_prefix
failure_reasons
```

The covered key set must match the mixed-unit context key set exactly, and the
coordinate-unit routing ledger itself must be proved.

## Lemma: keyed symmetric cutoff closes System M

[Proved, supplied-data form] Suppose:

1. the coordinate-unit routing ledger proves that the relevant no-triangular
   rows have routed to mixed-unit context;
2. a finite endpoint-family fork proves a faithful symmetric cutoff for the
   fixed endpoint groups used by those mixed-unit channels;
3. the covered key set is exactly the mixed-unit context key set.

Then System M has no remaining endpoint obligation for this supplied data.

Proof.  The endpoint-family fork kills every covered mixed-unit endpoint
channel under identity symmetric-longitude data.  Exact key coverage identifies
the covered channels with precisely the mixed-unit context routes.  Faithful
endpoint reconstruction then makes the residual mixed-unit endpoint motion
trivial.  Extra keys are rejected, so the certificate cannot close another
family by accident.  QED.

## Post-linear consequence

[Proved] The post-linear wrapper accepts this symmetric fork as an alternative
System M certificate.  In an M-only endpoint row it returns

```text
closed_by_mixed_unit_symmetric_endpoint_fork.
```

In a product endpoint row, it removes only M from

```text
unclosed_routed_endpoint_systems.
```

Any still-unclosed U or C endpoint family remains the reported finite system.

## Remaining burden

[Open] This is still a supplied-certificate closure.  To prove
`[Resolution: A]`, one must construct such fixed symmetric cutoffs, or
stronger endpoint-longitude witnesses, for every mixed-unit context route in
every remaining bottleneck interval.  To prove `[Resolution: B]`, one must
turn failure of every such cutoff into a normalized-law residual sequence with
actual mixed-unit endpoint movement.
