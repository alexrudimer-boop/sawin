# Triangular recovery symmetric endpoint fork

Date: 2026-05-31

This note follows `proofs/triangular_recovery_unit_observer.md` and
`proofs/endpoint_family_symmetric_fork.md`.  It does not construct the
missing uniform `U_tri` endpoint witnesses.  It makes the symmetric-detector
alternative executable for the routed triangular recovery endpoint layer
itself, with exact routed-key coverage.

## Setup

A System U row has a fixed triangular recovery unit group

```text
U_tri = < triangular recovery row permutations >
```

and a finite routed defect ledger

```text
system_u_endpoint_defects.
```

Each defect contributes one endpoint key

```text
(left_color, right_color, routed_defect_reason).
```

The existing endpoint witness checker

```text
triangular_recovery_endpoint_witness_audit(...)
```

closes this row when each key has a concrete `V_beta(U_tri)` certificate.  The
symmetric fork below is the coarser but still fixed finite-group alternative:
prove that one symmetric detector degree kills the whole finite family of
routed `U_tri` endpoint channels.

## Executable object

The specialized helper is

```text
triangular_recovery_symmetric_endpoint_fork_audit(
    observer,
    routed_defects,
    endpoint_family,
    covered_keys,
)
```

where `endpoint_family` is an `EndpointFamilySymmetricForkAudit`.

It records:

```text
routed_keys
supplied_covered_keys
missing_routed_keys
extra_covered_keys
endpoint_family_uses_recovery_unit_group
proves_triangular_recovery_symmetric_endpoint_cutoff
proves_triangular_recovery_symmetric_tail_seed_prefix
failure_reasons
```

The checker requires the endpoint-family group list to be exactly

```text
(|U_tri|,)
```

and requires the supplied covered keys to match the routed System U keys.
Thus a symmetric cutoff for one U endpoint cannot silently close an unrelated
U key, and it cannot close a continuation or mixed-unit endpoint family.

## Lemma: keyed symmetric cutoff closes System U

[Proved, supplied-data form] Suppose:

1. the triangular recovery unit observer proves the fixed finite group
   `U_tri`;
2. the endpoint-family symmetric fork proves a faithful cutoff for the fixed
   group `U_tri`, so some `S_M` with `M >= |U_tri|` kills all covered U
   endpoint channels;
3. the covered key set is exactly the routed System U endpoint key set.

Then the routed System U endpoint layer has no remaining obligation.

Proof.  The endpoint-family symmetric fork proves that identity `S_M`
longitude data kills every covered endpoint channel in `U_tri`.  Since
`M >= |U_tri|`, the left-regular embedding gives the usual finite-group
monotonicity from `S_M` to `U_tri`.  Exact key coverage says that every
routed System U endpoint channel is covered and that no unrelated endpoint
has been mixed into the certificate.  Faithfulness of the endpoint family
then converts endpoint identity into the corresponding residual fixedness.
Thus System U is closed for the supplied routed ledger.  QED.

## Product-system consequence

[Proved] The post-linear finite-system wrapper accepts the keyed symmetric
fork as an alternative System U certificate.

If U is the only active routed endpoint family, a matching fork returns

```text
closed_by_triangular_recovery_symmetric_endpoint_fork.
```

If U appears together with C or M, the fork removes only U from

```text
unclosed_routed_endpoint_systems.
```

For example, a U/C product with a proved U symmetric fork and no C endpoint
witness is still reported as

```text
system_c_universal_continuation_endpoint.
```

The finite payload records:

```text
triangular_recovery_symmetric_fork_matches_system
triangular_recovery_symmetric_fork_group_orders
triangular_recovery_symmetric_fork_minimum_degree
triangular_recovery_symmetric_fork_degree
triangular_recovery_symmetric_fork_cutoff_proved
triangular_recovery_symmetric_fork_tail_seed_prefix_proved
triangular_recovery_symmetric_fork_missing_keys
triangular_recovery_symmetric_fork_extra_keys
```

## Negative side

[Open] A finite supplied tail-prefix row is not `[Resolution: B]`.  It only
records the beginning of the endpoint-family negative alternative.  To prove
B through System U, one must construct an explicit interval and an unbounded
symmetric-tail sequence with nonidentity routed `U_tri` endpoint motion,
then attach that motion to residual tuple movement as required by the
global-local normalized fork.

## Current role

This note narrows the System U endpoint burden without solving it.  A future
positive proof may now close U either by concrete endpoint-longitude
witnesses or by a keyed symmetric cutoff for `U_tri`.  A future negative proof
must produce the all-tail version of the same keyed endpoint failure.
