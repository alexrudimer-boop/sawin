# Triangular recovery kink-completion deficit

Date: 2026-05-31

This note refines `proofs/nonlinear_overlap_refined_obstruction.md`.  It does
not prove `[Resolution: A]` or construct `[Resolution: B]`.  It isolates the
exact bridge that was hidden between triangular recovery and the
rack-kink Latin cancellation theorem.

## Why this split is needed

The kink-predecessor theorem applies to a rack-base all-pairs Latin-unit
triangular situation:

```text
base is a finite rack;
left Latin-unit triangular rows are present for every colour pair;
the Latin triangular YBE equations hold for every colour triple.
```

Under those hypotheses, the theorem proves that every Latin fibre is
singleton.  Thus a nontrivial all-pairs rack-base Latin shear cannot be the
remaining nonlinear obstruction.

However, a triangular recovery endpoint audit by itself proves only that a
constant-section triangular row has a finite inverse recovery table and hence
a fixed recovery unit group `U_tri`.  It does not prove that the whole
remaining corridor has reached the all-pairs Latin-unit hypotheses of the
kink theorem.

## Executable split

The nonlinear refinement audit now exposes the bridge explicitly.  The new
deficit list is:

```text
nonlinear_overlap_refinement_audit(interval).
    rack_kink_completion_deficits
```

with possible entries:

```text
base_not_finite_rack
latin_rows_not_present_for_all_pairs
side_dual_latin_rows_present_for_all_pairs
latin_ybe_equations_not_verified
kink_cancellation_not_verified
```

For genuine target data, the first entry is a closed consistency failure.
The obstruction hypothesis already gives a coloured-YBE local interval whose
base has left-rack form.  Since the base map is bijective, every left
translation is a bijection.  The coloured YBE projection gives left
self-distributivity.  Finally, in any finite left rack the kink map

```text
kappa(a)=a*a
```

is surjective: for each `b`, let `c` be the unique element with `b*c=b`;
then

```text
b*(c*c)=(b*c)*(b*c)=b*b,
```

so left-cancellation by `b` gives `c*c=b`.  Finite surjectivity makes
`kappa` bijective.  Therefore `base_not_finite_rack` is now recorded as the
closed status

```text
rack_base_consistency_inconsistent
```

rather than as a live System K branch.

The same audit also exposes the finite row data behind those strings:

```text
expected_latin_color_pairs
left_latin_row_pairs
right_latin_row_pairs
missing_left_latin_row_pairs
missing_right_latin_row_pairs
missing_left_latin_row_defects
missing_right_latin_row_defects
active_missing_left_latin_row_defects
active_missing_right_latin_row_defects
side_dual_latin_completion_available
latin_ybe_failure_triples
side_dual_latin_ybe_failure_triples
```

Thus a completion failure is not a vague obstruction.  It is either a listed
colour pair without a left Latin-unit triangular row, a side-dual situation
where all right Latin-unit triangular rows are present but the left-handed
kink theorem has not yet been transported, or a listed colour triple where the
alpha, middle, or endpoint projection of the Latin triangular YBE system has
not been verified.  The defect rows are expanded in
`proofs/triangular_k_left_defect_ledger.md`; for example a missing left
Latin row records whether there is no triangular row, a nonbijective
constant map with proper/universal kernel or codomain failure, a nonbijective
companion section with proper/constant/injective-nonsurjective profile, a
hidden nonunit opposite column, or a side-dual right triangular replacement.
The active ledgers remove pairs already closed by product collapse, visible
opposite kernels, injective-nonsurjective sections, or side-dual Latin
availability.

The side-dual equations are audited by applying
`latin_triangular_ybe_audit(...)` to `side_opposite_local_interval(interval)`,
as recorded in `proofs/triangular_recovery_side_dual_completion.md`.  The
right-rack diagonal cancellation theorem in
`proofs/right_rack_kink_latin_triangular_cancellation.md` closes the
side-dual subcase whenever those equations hold, so only listed side-dual
Latin YBE projection failures remain.  The consistency note
`proofs/triangular_latin_ybe_projection_consistency.md` closes those failures
for actual coloured-YBE interval data.

The cancellation rows are also closed once their own theorem hypotheses hold.
If the rack-kink Latin hypotheses and Latin triangular YBE equations hold but
the kink-cancellation identities fail, the refinement records:

```text
latin_triangular_kink_cancellation_inconsistent.
```

This is not a live System K row: it contradicts
`proofs/kink_predecessor_latin_triangular_cancellation.md`, which derives the
cancellation identities from exactly those hypotheses.  The side-dual/right
rack orientation has the analogous closed status:

```text
side_dual_latin_triangular_diagonal_cancellation_inconsistent,
```

closed by `proofs/right_rack_kink_latin_triangular_cancellation.md`.

If a triangular recovery endpoint remains and this list is nonempty, the
status is:

```text
triangular_recovery_kink_completion_deficit
```

The post-linear wrapper records both the raw and live lists:

```text
deficits
live_kink_completion_deficits
nonlive_kink_completion_deficits
live_k_missing_latin_row_defects
```

After the recorded closure statuses above, the live list contains only:

```text
latin_rows_not_present_for_all_pairs.
```

Thus System K is no longer a mixture of base-rack, Latin-YBE, and
cancellation failures.  Those failures are closed or preempted before the K
status.  The direct finite target is the missing Latin-row completion ledger,
with `side_dual_latin_rows_present_for_all_pairs` retained only as a
side-dual modifier.

The wrapper treats raw K rows with empty
`live_k_missing_latin_row_defects` and empty
`recovery_routed_k_missing_latin_row_defects` and
`continuation_routed_k_missing_latin_row_defects` tuples as:

```text
closed_by_recorded_k_deficit_routing.
```

Thus active System K means a nonempty finite row ledger, not merely a raw
status string in a synthetic or already-routed subcase.
The active row ledger is also status-faithful: raw structural defect names
remain in the diagnostic `missing_*_latin_row_defects` tables, but they are
not included in `live_k_missing_latin_row_defects` after
`triangular_structural_inconsistency` closes that branch.

The tuple is now profile-aware.  A no-triangular-row reason remains live until
the missing-row profile ledgers are supplied; after that it is removed when
the profile is proper-kernel visible, coordinate-unit routed by either a
proved global two-sided-unit branch or mixed-unit context, partial-constant
routed to continuation, or closed by the finite cardinality/profile audit.  A
two-sided coordinate-unit row without the global locally-nondegenerate branch
certificate remains live.

It is also constant-map-kernel aware.  Constant-map proper/universal-kernel
reasons remain live until the kernel-closure ledger and triangular recovery
route ledger are supplied.  Proper closures are contradictions to local
minimality; universal closures are removed only when the recovery table
separates the collapsed inputs.  The filtering is reason-local, so unrelated
live defects for the same pair remain in the tuple.
The companion injective-nonsurjective block-image reason is removed by the
same supplied recovery separation, while companion proper-kernel and constant
reasons remain structural/kernel cases.
These kernel labels are now reserved for actual nontrivial fibres: singleton
constant-map or companion images are codomain/block-image cases, not
universal-kernel or companion constant-kernel cases.
The support row
`active_companion_block_image_support_rows` records that any active companion
block-image reason is attached to a same-side constant-map proper or
universal kernel reason; unsupported companion block-images close
structurally before System K.
When the triangular recovery table separates all such constant-map kernel
and supported companion block-image rows, the rows move to
`recovery_routed_k_missing_latin_row_defects`.  If no live K row remains, the
remaining obligation is no longer System K; it is the System U endpoint
condition for the fixed recovery group `U_tri`.
When a partial-constant no-triangular row is routed through continuation
seeds, it moves instead to
`continuation_routed_k_missing_latin_row_defects` and the remaining
obligation is the universal-continuation endpoint witness layer.
When a coordinate-unit no-triangular row is routed to mixed-unit context, it
moves to `mixed_context_routed_k_missing_latin_row_defects` and the remaining
obligation is the mixed-unit context endpoint/readout layer.
These routed endpoint ledgers can coexist.  The post-linear wrapper records
all active endpoint families in `active_routed_endpoint_systems`; if, for
example, a constant-map kernel route gives System U while a partial-constant
missing row gives System C, the remaining finite system is the product
endpoint system `system_uc_routed_endpoint_product` until both endpoint
families have matching witnesses.

This status says that the next A-proof cannot merely cite the
kink-predecessor theorem.  It must either prove that the remaining corridor
does satisfy the missing all-pairs Latin hypotheses, or route the failed
missing-hypothesis row into a fixed detector/readout or a normalized-law seed.

## Contradiction endpoint

There is also an explicit contradiction status:

```text
latin_triangular_kink_contradiction
```

It records the formal combination:

```text
rack-kink theorem hypotheses hold,
kink cancellation is verified,
but a non-singleton Latin fibre remains.
```

That combination is impossible by the kink-predecessor cancellation theorem,
so it is a closed row rather than a `U_tri` endpoint obstruction.

The executable refinement also records the preemption explicitly as:

```text
direct_unit_longitude_status_preempted_by_kink_dichotomy.
```

If the triangular recovery unit observer is ready and
`rack_kink_completion_deficits` is empty, then the all-pairs Latin hypotheses
and kink cancellation are already in force.  The direct
`triangular_recovery_unit_longitude_obstruction` status is therefore skipped:
the row has already closed by `latin_triangular_kink_contradiction` in the
non-singleton case or by `latin_triangular_kink_impossible` in the singleton
case.  A `U_tri` endpoint problem appears only after a genuine K-deficit has
first been routed into fixed endpoint data.

For actual interval data, the direct audit should normally detect this earlier
as a Latin YBE projection failure or as one of the cancellation-inconsistency
statuses above.  The contradiction status is still useful in the proof ledger
because it states the exact logical endpoint of the rack-kink route.

## Updated fork

After this refinement, the remaining triangular branch is not just:

```text
prove endpoint in V_beta(U_tri).
```

It is the ordered fork:

```text
1. complete the triangular recovery corridor to the rack-kink all-pairs
   Latin hypotheses, in which case nontrivial fibres are impossible; or
2. route the failed completion hypothesis through fixed detector data; or
3. if the completion deficit cannot be routed away, use the fixed U_tri
   endpoint fork:
      - active Artin detector-lift rows;
      - explicit endpoint-longitude expressions;
      - derived-series quotient lifts plus a P_tri witness;
      - or a normalized-law sequence from a P_tri finite miss.
```

This is a stricter restatement of the remaining proof burden.  It prevents
the all-pairs rack-kink theorem from being used outside its hypotheses, while
preserving the finite `U_tri` endpoint machinery for any genuine completion
failure that survives.
