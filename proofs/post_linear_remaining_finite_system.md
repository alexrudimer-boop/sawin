# Post-linear remaining finite system

Date: 2026-05-31

This note packages the current endpoint of the post-linear reductions as an
explicit finite system.  It does not prove `[Resolution: A]` or construct
`[Resolution: B]`.  It records what a nonlinear survivor must now satisfy if
the finite-linear obstruction has already been ruled out.

## Input data

The remaining finite datum is a local interval

```text
I = (C, (A_c)_{c in C}, R_C, T)
```

where:

- `C` is a finite quotient colour set;
- each `A_c` is a finite fibre;
- `R_C` is in left rack convention, `R_C(a,b)=(a*b,a)`;
- `T_{a,b}:A_a x A_b -> A_{a*b} x A_a` is a finite bijective local row;
- the coloured YBE holds for all colour triples.

The datum must pass:

```text
nonlinear_overlap_obstruction_audit(I).status
  == exact_remaining_nonlinear_obstruction
```

That means it is local-minimal, semisplit-free, in the
`bi_free_universal_corridor_bottleneck`, with universal continuation seed
closure.

## Row-level finite alternatives

Apply:

```text
nonlinear_overlap_refinement_audit(I)
```

The executable classifier is:

```text
post_linear_remaining_finite_system_audit(I)
```

It returns a `PostLinearRemainingFiniteSystemAudit` with:

```text
system_name
finite_obstruction_data
remaining_obligations
```

Raw interval data reaches active System K only if the real bottleneck ledger
first certifies the `bi_free_universal_corridor_bottleneck` target and the
active missing-Latin ledger is nonempty.  If the raw K status has no live
unrouted row and no row has been routed to a triangular recovery endpoint,
the wrapper reports:

```text
closed_by_recorded_k_deficit_routing.
```

A caller may mark `kink_completion_deficits_routed=True` only when an external
supplied certificate has routed a nonempty K-deficit ledger to fixed detector
data; then the same finite recovery rows are classified as the downstream
System U endpoint problem.

For either System K or System U, the universal-continuation descent ledger is
made explicit by `proofs/universal_continuation_identity_routing.md`:

```text
universal_continuation_identity_lost_edges
universal_continuation_identity_unrouted_edges
universal_continuation_identity_routing_proved
```

These rows use the equality readout as the descent candidate and the identity
readout as the external routing ledger.  In the universal-continuation branch,
they list the exact original fibre edges whose endpoint witnesses are still
needed.

The supplied endpoint-witness checker for this exact ledger is recorded in
`proofs/universal_continuation_identity_endpoint_witness.md`.  It validates a
proposed fixed endpoint package against the identity-routed edge set and then
fits the generic descent-endpoint repair contract interface.

Every closed branch has already been routed out if the status is one of:

```text
closed_by_repair_contract
closed_by_transport_state_rackification
closed_by_locally_nondegenerate_branch
section_kernel_visible_to_existing_readouts
closed_by_product_triangular_collapse
triangular_structural_inconsistency
rack_base_consistency_inconsistent
latin_triangular_kink_contradiction
latin_triangular_kink_impossible
latin_triangular_ybe_projection_inconsistent
latin_triangular_kink_cancellation_inconsistent
side_dual_latin_triangular_ybe_projection_inconsistent
side_dual_latin_triangular_diagonal_cancellation_inconsistent
side_dual_latin_triangular_kink_contradiction
side_dual_latin_triangular_kink_impossible
```

Thus a genuine remaining nonlinear finite system has one direct active shape,
with a downstream endpoint layer after supplied K routing.

## System K: kink-completion deficit

The first survivor shape is:

```text
status == triangular_recovery_kink_completion_deficit.
```

Equivalently:

```text
triangular_recovery_verified = True,
not all_triangular_rows_close_by_product,
not latin_triangular_kink_impossible,
rack_kink_completion_deficits != empty.
```

The finite deficit is not abstract.  It is one of:

```text
base_not_finite_rack
latin_rows_not_present_for_all_pairs
side_dual_latin_rows_present_for_all_pairs
latin_ybe_equations_not_verified
kink_cancellation_not_verified
```

In genuine target-ready data, `base_not_finite_rack` is closed by
`rack_base_consistency_inconsistent`: left-rack base form plus bijective base
map gives bijective left translations, coloured YBE gives
self-distributivity, and the finite kink map is bijective.

The executable wrapper now separates:

```text
live_kink_completion_deficits
nonlive_kink_completion_deficits
live_k_missing_latin_row_defects
recovery_routed_k_missing_latin_row_defects
continuation_routed_k_missing_latin_row_defects
mixed_context_routed_k_missing_latin_row_defects
```

After the recorded status-order closures, the only live direct K deficit is:

```text
latin_rows_not_present_for_all_pairs.
```

The other raw names are nonlive in the remaining target system:
`base_not_finite_rack` is the rack-base consistency inconsistency,
`latin_ybe_equations_not_verified` is a coloured-YBE projection
inconsistency when all Latin rows are present, and
`kink_cancellation_not_verified` is the kink-cancellation inconsistency under
the theorem hypotheses.  The side-dual marker
`side_dual_latin_rows_present_for_all_pairs` is not a separate live deficit;
it is a modifier saying that the missing-left row has a complete side-dual
candidate, which is then handled by the side-opposite YBE and right-rack
diagonal-cancellation statuses.

Active System K additionally requires:

```text
live_k_missing_latin_row_defects != empty.
```

If `live_k_missing_latin_row_defects` is empty and all routed endpoint tuples
are empty, the raw K row has no remaining finite obstruction row after
product, profile, side-dual-Latin, and nonlive-deficit preemptions.  The
wrapper therefore classifies it as `closed_by_recorded_k_deficit_routing`,
not as a current remaining finite system.  If the live tuple is empty because
constant-map kernel rows have been separated by the triangular recovery
table, the wrapper classifies the row as downstream System U instead.  If it
is empty because a partial-constant no-triangular row has been routed to
continuation seeds, the wrapper classifies the row as downstream System C,
the universal-continuation endpoint system.  If it is empty because a
coordinate-unit row has routed to mixed-unit context, the wrapper classifies
the row as downstream System M.

These endpoint systems are not mutually exclusive.  A single finite ledger can
route one K defect to triangular recovery and another to universal
continuation or mixed-unit context.  The executable wrapper therefore records:

```text
active_routed_endpoint_systems
unclosed_routed_endpoint_systems
```

If more than one endpoint system remains unclosed, `system_name` is a product
name such as `system_uc_routed_endpoint_product` and `remaining_obligations`
contains every unclosed endpoint obligation.  A supplied witness for one
endpoint family removes only that family from the unclosed tuple; it does not
hide the remaining endpoint families.

The finite obstruction payload is product-aware as well.  For any routed
endpoint system it uses one shared evidence table containing all routed
families:

```text
recovery_routed_k_missing_latin_row_defects
system_u_endpoint_defects
continuation_routed_k_missing_latin_row_defects
mixed_context_routed_k_missing_latin_row_defects
active_routed_endpoint_systems
unclosed_routed_endpoint_systems
```

and then appends all supplied witness/routing ledgers for U, C, and M.  Thus a
closed C/M product reports both
`universal_continuation_endpoint_witness_proved` and
`mixed_unit_endpoint_witness_proved`; a closed U witness does not erase the C
or M witness fields, and an unclosed C or M family remains visible.

The side-dual replacement statuses are deliberately not members of this live
tuple.  They remain in:

```text
k_left_side_dual_replacement_rows
```

as finite routing data.  A side-dual triangular-but-non-Latin row is handled
by the opposite-side active defect ledger, and a missing side-dual triangular
replacement is handled by the opposite-side missing-row profile.  Therefore
the live tuple contains only actual left/right row defects, not side-dual
pointer labels.

The no-triangular-row reason is further refined by supplied profile ledgers. A
raw defect:

```text
no_left_triangular_row
no_right_triangular_row
```

stays live when no profile ledger has been supplied.  Once
`missing_triangular_row_profile_audit` is supplied, the wrapper removes that
row from `live_k_missing_latin_row_defects` whenever the profile proves one of
the recorded exits: proper-kernel visibility, coordinate-unit routing,
partial-constant continuation routing, or the finite cardinality/profile
closure.  Thus the live tuple is the raw active row list after applying the
available profile proofs, not merely after string-level filtering.
For partial-constant continuation routing, removal means "no longer System
K"; the row is recorded in
`continuation_routed_k_missing_latin_row_defects` and must be handled by the
universal-continuation endpoint witness layer.
For coordinate-unit routing, a two-sided-unit/global locally nondegenerate
route is closed, but a mixed-unit-context route is only no longer System K.
Such rows are recorded in `mixed_context_routed_k_missing_latin_row_defects`
and must be handled by the mixed-unit context endpoint/readout layer.

Constant-map kernel reasons are refined the same way.  Raw defects:

```text
left_constant_map_proper_kernel
left_constant_map_universal_kernel
right_constant_map_proper_kernel
right_constant_map_universal_kernel
```

stay live until the supplied kernel-closure and triangular-recovery route
ledgers account for their kernel edges.  Proper generated closures contradict
local minimality; universal generated closures must be separated by
`triangular_constant_kernel_recovery_route_audit`.  When every constant-map
kernel edge for the side/pair is handled in this way, the corresponding
constant-map reason is removed from `live_k_missing_latin_row_defects`.
The labels are kernel-local: a one-point constant map that is injective but
not surjective is a codomain defect, not a universal-kernel edge.
Removal here means "no longer System K."  The removed rows are recorded in
`recovery_routed_k_missing_latin_row_defects`; when this tuple is nonempty
and no live K rows remain, the current remaining finite system is the fixed
triangular recovery endpoint problem in System U.

The same supplied route removes the side/pair's companion
injective-nonsurjective block-image reason.  The companion image is a block
in the constant-map bundle partition, so the recovery table separation that
handles the universal constant-map kernel edge also accounts for that block.
Companion proper-kernel and companion constant reasons are not filtered this
way; they remain structural/kernel cases rather than block-image cases.
Here `companion constant` means rank-one with a nontrivial collapsed
companion fibre.  A one-point companion image is recorded only as
injective-nonsurjective and is removed by the block-image route above once
the recovery table separation is supplied.

together with the concrete rows:

```text
left_triangular_row_pairs
right_triangular_row_pairs
missing_left_latin_row_pairs
missing_right_latin_row_pairs
missing_left_latin_row_defects
missing_right_latin_row_defects
active_missing_left_latin_row_defects
active_missing_right_latin_row_defects
live_k_missing_latin_row_defects
recovery_routed_k_missing_latin_row_defects
continuation_routed_k_missing_latin_row_defects
mixed_context_routed_k_missing_latin_row_defects
active_companion_block_image_support_rows
active_companion_block_images_have_constant_kernel_support
k_left_side_dual_replacement_rows
triangular_latin_defect_closure_rows
triangular_latin_defect_proper_closure_rows
triangular_latin_defect_universal_closure_rows
triangular_constant_map_non_surjective_rows
triangular_companion_kernel_rows
triangular_companion_nonbijective_without_constant_kernel_rows
triangular_hidden_nonunit_opposite_without_product_rows
triangular_constant_kernel_recovery_route_rows
triangular_constant_kernel_unrouted_universal_rows
missing_triangular_row_profiles
missing_triangular_partial_constant_rows
missing_triangular_partial_constant_mixed_unit_rows
missing_triangular_nonconstant_hidden_rows
missing_triangular_left_rack_section_cardinality_failures
missing_triangular_injective_non_surjective_rows
missing_triangular_profile_unclassified_rows
missing_triangular_left_rack_cardinality_proved
missing_triangular_coordinate_unit_routes
missing_triangular_coordinate_unit_mixed_rows
missing_triangular_coordinate_unit_unrouted_rows
missing_triangular_coordinate_unit_unclosed_two_sided_rows
missing_triangular_locally_nondegenerate_closed_branch
missing_triangular_partial_constant_closure_rows
missing_triangular_partial_constant_proper_closure_rows
missing_triangular_partial_constant_universal_closure_rows
missing_triangular_partial_constant_continuation_routes
missing_triangular_partial_constant_unrouted_continuation_rows
universal_continuation_identity_lost_edges
universal_continuation_identity_unrouted_edges
universal_continuation_identity_routing_proved
side_dual_latin_completion_available
latin_ybe_failure_triples.
side_dual_latin_ybe_failure_triples
```

The side-dual flag is important.  It separates a genuinely missing Latin
completion from the case where the right triangular Latin rows are present
for every colour pair but the left-handed rack-kink theorem has not yet been
transported across the side-opposite symmetry.  Such a row is still System K,
not System U, until that side-dual completion is supplied or routed by a fixed
detector certificate.

The side-dual replacement rows make this finite:

```text
k_left_side_dual_replacement_rows
```

lists, for each missing left pair, whether the right side is already Latin,
is triangular but non-Latin with explicit right defects, or has no right
triangular replacement with an explicit missing-row profile.

The side-dual equations are exposed by
`proofs/triangular_recovery_side_dual_completion.md` using
`side_opposite_local_interval(interval)`.  This converts right triangular rows
into left triangular rows for the purpose of the Latin YBE audit.  The
right-rack diagonal cancellation theorem in
`proofs/right_rack_kink_latin_triangular_cancellation.md` closes this subcase
when the side-dual Latin YBE equations hold.  Therefore a surviving K-dual
row must carry explicit side-dual alpha, middle, or endpoint YBE projection
failures.  The consistency note
`proofs/triangular_latin_ybe_projection_consistency.md` then closes those
projection-failure states for genuine coloured-YBE interval data.

Thus, after the current refinements, the only live K-subsystem is the
left-missing completion problem.  The exact finite ledger is recorded in
`proofs/triangular_k_left_defect_ledger.md`; its left-handed defect reasons
are:

```text
no_left_triangular_row
left_row_product_collapse
left_constant_map_not_bijective
left_constant_map_not_surjective
left_constant_map_proper_kernel
left_constant_map_universal_kernel
left_companion_sections_not_bijective
left_companion_sections_proper_kernel
left_companion_sections_constant
left_companion_sections_injective_non_surjective
left_opposite_sections_not_bijective
left_opposite_proper_kernel_visible
left_opposite_injective_non_surjective
left_opposite_hidden_nonunit_unclassified
side_dual_right_latin_available
side_dual_right_triangular_nonlatin
no_side_dual_right_latin_replacement
```

After product collapse, proper-kernel visibility,
injective-nonsurjective visibility, and side-dual Latin availability are
routed out, the K-left subsystem is measured by the nonempty part of
`active_missing_left_latin_row_defects`.  This active tuple is status-faithful:
it is empty unless the refinement status is exactly
`triangular_recovery_kink_completion_deficit`.  Therefore structural labels
that appear in the raw defect ledger do not leak into active System K after
`triangular_structural_inconsistency` has closed them.  Side-dual non-Latin
and missing replacement labels remain in the finite replacement ledger, but
they are not themselves live defects; they point to the opposite-side active
defect ledger or missing-row profile.

```text
some required left Latin-unit triangular colour pair is missing,
the row has not already routed to product triangular collapse, proper kernel
readouts, side-dual Latin completion, or strand-continuing transport, and any
non-Latin/missing side-dual replacement is accounted for on the opposite-side
finite ledger.
```

After the status-order closures, the active reason names are:

```text
no_left_triangular_row
left_constant_map_proper_kernel
left_constant_map_universal_kernel
left_companion_sections_injective_non_surjective
```

and the symmetric right-handed names.  The companion
injective-nonsurjective name can survive only as a block-image companion to a
constant-map kernel; the supplied recovery-table route removes it together
with the corresponding constant-map kernel reason.

The executable ledger records this dependency explicitly:

```text
active_companion_block_image_support_rows
active_companion_block_images_have_constant_kernel_support
```

Each support row lists the side, colour pair, and same-side
`*_constant_map_proper_kernel` or `*_constant_map_universal_kernel` reason
that carries the companion block-image.  An unsupported companion
injective-nonsurjective row is structural, not active System K.

For any active row with an actual kernel edge, the closure rows split the
case further:

```text
triangular_latin_defect_proper_closure_rows != empty
```

contradicts local minimality, while

```text
triangular_latin_defect_universal_closure_rows
```

lists the exact universal seed edges that still need fixed detector routing.
The executable post-linear wrapper reflects this distinction directly.  When
a supplied triangular-Latin defect closure has a proper generated congruence
row, the branch is classified as
`closed_by_triangular_latin_proper_closure`, has no active routed endpoint
systems, and is not a current remaining finite system.  Only universal
closure rows may route onward to the System U recovery endpoint layer.

The structural rows must be empty for genuine bijective triangular interval
data:

```text
triangular_constant_map_non_surjective_rows
triangular_companion_kernel_rows
triangular_companion_nonbijective_without_constant_kernel_rows
triangular_hidden_nonunit_opposite_without_product_rows
```

Nonempty structural rows are inconsistency certificates, not additional live
branches.  The refinement records them as:

```text
triangular_structural_inconsistency.
```

Finally, constant-map kernel rows are checked against the triangular recovery
table:

```text
triangular_constant_kernel_unrouted_universal_rows
```

must be empty before those constant-map kernel seeds can be routed onward to
System U.

For colour pairs with no triangular row on the missing side, the profile rows
separate proper-kernel visibility, injective-nonsurjective size/codomain
misses, coordinate-side unit rows, partial-constant hidden rank loss, and
nonconstant hidden rank loss.  In the post-linear rank-profile branch,
coordinate-side unit rows are routed by
`proofs/triangular_k_left_coordinate_unit_routing.md`: if every colour pair is
two-sided unit then the locally nondegenerate/guitar branch applies; otherwise
the one-sided unit row is mixed-unit context with the nonunit data on the
opposite side.  The supplied coordinate-unit route is trusted only when its
coloured-YBE premise is present; otherwise the no-triangular row remains live
System K and no System M endpoint obligation is created from that data.  A
two-sided unit row is removed from live K only when the global
locally-nondegenerate branch is actually proved; otherwise it remains live and
is listed in
`missing_triangular_coordinate_unit_unclosed_two_sided_rows`.  Mixed-unit
coordinate routes are recorded in
`mixed_context_routed_k_missing_latin_row_defects`; if no live K row remains,
the wrapper reports `system_m_mixed_unit_context_endpoint`.  Nonconstant
hidden rows are inconsistency certificates.
Injective-nonsurjective and unclassified profile rows are closed by
`proofs/triangular_k_left_rack_cardinality_closure.md`: in a left-rack-base
local interval, every relevant finite coordinate section has equal domain and
codomain size, and the remaining finite-map kernel split is exhaustive.
Partial-constant hidden rows are mixed-unit context-recovery rows: their
nonunit sections are constant and their remaining sections are units.  The
constant nonunit sections now have their own closure ledger in
`proofs/triangular_k_left_partial_constant_closure.md`: proper generated
closures contradict local minimality and are classified as
`closed_by_missing_triangular_partial_constant_proper_closure`, while
universal generated closures are then routed by
`proofs/triangular_k_left_partial_constant_continuation_route.md` into the
universal continuation seed channel.  The supplied continuation route must
reach a universal continuation seed closure; a merely nonuniversal
continuation-seed containment leaves the row live in System K and does not
create a System C endpoint obligation.
The downstream identity-routing ledger is also non-vacuous: a forced
universal-continuation route proves only when its lost-edge tuple is exactly
the seed-saturation lost-edge tuple, its routed and unrouted tuples partition
that lost tuple, its routing labels distinguish exactly the routed edges, and
the forced lost-edge tuple is nonempty.
Rows moved this way are recorded in
`continuation_routed_k_missing_latin_row_defects`.  If no live K row remains,
the wrapper reports `system_c_universal_continuation_endpoint` rather than a
closed branch.

`proofs/universal_continuation_identity_endpoint_witness.md` gives the
supplied-certificate checker for the next endpoint layer: once endpoint
factors are supplied for the identity-routed lost edges, the executable audit
checks exact coverage and exposes the resulting endpoint-visibility certificate
to the repair-contract audit.  The post-linear wrapper now accepts that same
certificate as `universal_continuation_endpoint_witness`; when it matches the
supplied `universal_continuation_identity_routing` object and proves all
identity-routed endpoint witnesses, System C is reported as
`closed_by_universal_continuation_endpoint_witness` rather than as a current
remaining finite system.

To close System K on the A side, prove that every such finite deficit either
cannot occur in a genuine local-minimal bi-free universal-corridor interval or
is visible in a fixed interval-level detector/readout.  To turn System K into
B, construct one explicit interval with such a deficit and upgrade the
resulting residual motion to a normalized-law sequence invisible to every
finite group.

## System C: universal-continuation endpoint

The continuation endpoint layer is reached when:

```text
raw System K and
live_k_missing_latin_row_defects == empty and
continuation_routed_k_missing_latin_row_defects != empty.
```

This is not a triangular recovery endpoint.  It is the descent/continuation
endpoint channel recorded by:

```text
universal_continuation_identity_lost_edges
universal_continuation_identity_unrouted_edges
universal_continuation_identity_routing_proved.
universal_continuation_endpoint_witness_matches_routing
universal_continuation_endpoint_witness_proved
universal_continuation_endpoint_missing_edges
universal_continuation_endpoint_extra_edges
universal_continuation_symmetric_fork_matches_routing
universal_continuation_symmetric_fork_group_orders
universal_continuation_symmetric_fork_minimum_degree
universal_continuation_symmetric_fork_degree
universal_continuation_symmetric_fork_cutoff_proved
universal_continuation_symmetric_fork_tail_seed_prefix_proved
universal_continuation_symmetric_fork_missing_edges
universal_continuation_symmetric_fork_extra_edges
```

The remaining A-route is to construct fixed endpoint witnesses for those
routed universal-continuation seed closures.  The B-route would have to
upgrade one such endpoint miss to the normalized-law sequence required in the
original problem.

[Proved] If the supplied `universal_continuation_endpoint_witness` matches the
same identity-routing ledger and proves all routed endpoint witnesses, then
this row has no remaining System C obligation.  The executable classifier
returns `closed_by_universal_continuation_endpoint_witness`, empties
`remaining_obligations`, and no longer counts the row as a current remaining
finite system.

[Proved] If the supplied
`universal_continuation_symmetric_endpoint_fork` matches the same
identity-routing ledger, covers exactly the identity-routed lost edges, and
proves a faithful symmetric endpoint cutoff for the fixed continuation
endpoint family, then this row also has no remaining System C obligation.  The
executable classifier returns
`closed_by_universal_continuation_symmetric_endpoint_fork` in the C-only case.
In a product endpoint row, this certificate removes only C from
`unclosed_routed_endpoint_systems`.

## System M: mixed-unit context endpoint

The mixed-unit endpoint layer is reached when:

```text
raw System K and
live_k_missing_latin_row_defects == empty and
mixed_context_routed_k_missing_latin_row_defects != empty.
```

This layer is produced by coordinate-unit missing triangular rows whose
opposite side carries the nonunit data.  The remaining A-route is to prove
that each such mixed-unit context endpoint factors through fixed
detector/readout data.  The B-route would have to upgrade one mixed-unit
endpoint miss to the normalized-law sequence required in the original
problem.

The supplied-certificate checker for this endpoint layer is:

```text
mixed_unit_context_endpoint_witness_audit(...)
```

It uses the coordinate-unit routing ledger itself as the list of endpoint
channels.  Each mixed row contributes one key

```text
(left_color, right_color, side)
```

for every coordinate-unit side routed to mixed context.  A witness proves the
layer only when the coordinate-unit routing ledger is proved, every mixed
context key has a product endpoint-longitude expression certificate, no
endpoint display fails, and no extra key is supplied.

The post-linear data records:

```text
missing_triangular_coordinate_unit_mixed_rows
missing_triangular_coordinate_unit_unrouted_rows
missing_triangular_coordinate_unit_routing_proved
mixed_unit_endpoint_witness_matches_routing
mixed_unit_endpoint_witness_proved
mixed_unit_endpoint_missing_context_keys
mixed_unit_endpoint_extra_context_keys
mixed_unit_symmetric_fork_matches_routing
mixed_unit_symmetric_fork_group_orders
mixed_unit_symmetric_fork_minimum_degree
mixed_unit_symmetric_fork_degree
mixed_unit_symmetric_fork_cutoff_proved
mixed_unit_symmetric_fork_tail_seed_prefix_proved
mixed_unit_symmetric_fork_missing_context_keys
mixed_unit_symmetric_fork_extra_context_keys
```

[Proved] If the supplied `mixed_unit_context_endpoint_witness` matches the
same coordinate-unit routing ledger and proves all mixed context endpoint
witnesses, the wrapper returns
`closed_by_mixed_unit_context_endpoint_witness`, empties
`remaining_obligations`, and removes the row from the current remaining
finite-system list.  This is not a uniform endpoint theorem; it is the exact
finite certificate interface that a positive proof must fill.

[Proved] If the supplied `mixed_unit_context_symmetric_endpoint_fork` matches
the same coordinate-unit routing ledger, covers exactly the mixed context
keys, and proves a faithful symmetric endpoint cutoff for the fixed mixed-unit
endpoint family, then this row also has no remaining System M obligation.  The
executable classifier returns `closed_by_mixed_unit_symmetric_endpoint_fork`
in the M-only case.  In a product endpoint row, this certificate removes only
M from `unclosed_routed_endpoint_systems`.

## System U: triangular recovery unit endpoint

The endpoint unit group is still needed, but it is no longer an independent
direct survivor of the refinement status.  The nominal direct status is:

```text
status == triangular_recovery_unit_longitude_obstruction.
```

The executable predicate

```text
direct_unit_longitude_status_preempted_by_kink_dichotomy
```

records the following closure.  If the triangular recovery unit observer is
ready and the rack-kink completion deficit list is empty, then the rack-kink
hypotheses, Latin triangular YBE equations, and kink cancellation identities
all hold.  The kink dichotomy then fires before a direct unit-longitude status
can occur: either a non-singleton Latin fibre gives
`latin_triangular_kink_contradiction`, or all Latin fibres are singleton and
`latin_triangular_kink_impossible` closes the row.  Thus direct System U is
preempted by a closed kink status.

Consequently System U should be read as the endpoint layer reached after a
System K deficit has already been routed by external fixed-detector data or
by the triangular recovery table:

```text
raw System K and either
  (live_k_missing_latin_row_defects != empty and
   kink_completion_deficits_routed == True)
or
  (live_k_missing_latin_row_defects == empty and
    recovery_routed_k_missing_latin_row_defects != empty).
```

Here the finite recovery unit group

```text
U_tri = < triangular recovery row permutations >
```

is fixed by the interval.  A residual endpoint word in its generators must be
handled by one of the following finite certificate systems:

```text
triangular_recovery_detector_lift_transition_audit(...)
triangular_recovery_detector_lift_braid_audit(...)
triangular_recovery_longitude_expression_audit(...)
triangular_recovery_derived_series_lift_audit(...)
triangular_recovery_perfect_residual_audit(...)
triangular_recovery_longitude_route_audit(...)
triangular_recovery_endpoint_witness_audit(...)
triangular_recovery_symmetric_endpoint_fork_audit(...)
```

To close System U on the A side, prove uniformly in braid index that every
triangular recovery endpoint lies in `V_beta(U_tri)`, by active detector-lift
rows, explicit endpoint-longitude expressions, derived-series lifts plus a
`P_tri` witness, direct subgroup membership, or a fixed symmetric endpoint
cutoff for the finite routed `U_tri` endpoint family.

The post-linear wrapper now exposes and checks the bundled supplied
certificate:

```text
system_u_endpoint_defects
triangular_recovery_endpoint_witness_matches_system
triangular_recovery_endpoint_witness_proved
triangular_recovery_endpoint_missing_keys
triangular_recovery_endpoint_extra_keys
triangular_recovery_symmetric_fork_matches_system
triangular_recovery_symmetric_fork_group_orders
triangular_recovery_symmetric_fork_minimum_degree
triangular_recovery_symmetric_fork_degree
triangular_recovery_symmetric_fork_cutoff_proved
triangular_recovery_symmetric_fork_tail_seed_prefix_proved
triangular_recovery_symmetric_fork_missing_keys
triangular_recovery_symmetric_fork_extra_keys
```

The endpoint keys are exactly:

```text
(left_color, right_color, routed_defect_reason).
```

[Proved] If the supplied `triangular_recovery_endpoint_witness` uses the same
fixed `U_tri` observer, covers exactly the current
`system_u_endpoint_defects`, and each covered key carries a recovery endpoint
certificate proving membership in `V_beta(U_tri)`, then System U is closed for
that supplied data.  The executable classifier returns
`closed_by_triangular_recovery_endpoint_witness`, empties
`remaining_obligations`, and no longer counts the row as a current remaining
finite system.

[Proved] If the supplied `triangular_recovery_symmetric_endpoint_fork` uses
the same fixed `U_tri` observer, its endpoint-family group list is exactly
`(|U_tri|,)`, it covers exactly the current `system_u_endpoint_defects`, and
it proves a faithful symmetric endpoint cutoff, then System U is also closed.
The executable classifier returns
`closed_by_triangular_recovery_symmetric_endpoint_fork` for a U-only endpoint
row.  In a product endpoint row, this certificate removes only U from
`unclosed_routed_endpoint_systems`; any unclosed C or M endpoint family remains
the reported current finite system.

To turn System U into B, construct an explicit interval and a stable
perfect-residual finite miss in `P_tri` that upgrades to the normalized-law
residual sequence required by the local normalized-law fork.

## Equivalence to the current remaining problem

[Proved relative to the recorded branch reductions] After the finite-linear
overlap no-go theorem, any unresolved nonlinear primitive overlap must supply
a survivor of System K, followed by the System U endpoint layer only after the
K deficit has been routed.

Proof.  The obstruction audit localizes any survivor to a local-minimal
`bi_free_universal_corridor_bottleneck` interval.  The refinement audit then
routes strand-continuing, locally nondegenerate, proper-kernel, product
triangular, and rack-kink impossible/contradictory rows to closed branches.
If triangular recovery is not verified, the status is an earlier
constant-section or endpoint-recovery obstruction rather than a final
post-linear survivor.  Once triangular recovery is verified, an empty
rack-kink deficit list is preempted by the closed kink dichotomy: the status is
`latin_triangular_kink_contradiction` when a non-singleton Latin fibre remains,
and `latin_triangular_kink_impossible` when no such fibre remains.  Therefore
the only direct nonclosed refinement status is System K, and the post-linear
wrapper keeps it active only when `live_k_missing_latin_row_defects` is
nonempty.  When such a K deficit is separately routed to fixed endpoint data,
the remaining endpoint problem is the System U `V_beta(U_tri)` membership
problem.
QED.

This equivalence does not itself solve the problem.  It is the current exact
finite target: close the nonempty `live_k_missing_latin_row_defects` ledger
and its routed System U endpoint layer uniformly to prove A, or construct one
explicit normalized-law counterexample from that finite chain to prove B.
