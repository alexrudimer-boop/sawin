# Post-linear remaining finite system

Date: 2026-05-31

This note packages the current endpoint of the post-linear reductions as an
explicit finite system.  It does not prove `[Resolution: A]` or construct
`[Resolution: B]`.  It records what a nonlinear survivor must now satisfy if
the finite-linear obstruction has already been ruled out.

The global assembly is conditionally closed: once every surviving local
U/C/M endpoint family has a full-braid fixed-assignment word-potential
observer and residual-faithfulness proof, the finite direct product of the
known branch detector groups and the U/C/M endpoint targets gives the local
group `G(pi,Q)`.  Product functoriality
`V_beta(prod_s G_s)=prod_s V_beta(G_s)` kills each known branch and endpoint
family componentwise, residual faithfulness gives `Delta_n(beta)=1`, and the
sharp rack detector replaces `Q` by `Q x A_{G(pi,Q)}`.  Iterating this along
the finite congruence chain yields a rack independent of braid index.  Thus
the remaining obstruction recorded here is local: construct those U/C/M
endpoint observers, or construct a normalized-law counterexample.
The congruence-chain helper now treats endpoint-observer closure verdicts,
including the one-family and product `endpoint_observer_family_build` verdicts,
as closed local summaries only when they carry the actual fixed detector
product group; otherwise the row remains a local gap rather than being
assembled into the final rack.

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
The coordinate-unit route is certificate-gated by the actual listed side: the
listed coordinate-unit side must have the `coordinate_side_unit_not_triangular`
explanation and must be a unit side in the supplied section data.  A row whose
listed side is nonunit, whose listed side is duplicated, whose route row is
duplicated, or whose explanation does not match remains live in System K.  The
coordinate-unit routing ledger is non-vacuous and duplicate-free: an empty row
tuple or a duplicated row tuple does not prove the route.
The missing-row profile ledger is also certificate-gated internally: each
section-profile row must be an exact rank/kernel/image summary of one finite
coordinate section.  The rank must match both the duplicate-free image and the
kernel-block count, the disjoint kernel blocks must cover the recorded domain
size, and the rank must fit within the recorded domain and codomain sizes.  An
inexact section-rank row makes the missing-row profile unclassified and leaves
the raw K defect live.

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

## Universal-K row normal form

The row-routing layer now has an explicit finite normal-form target.  A
universal-K row descriptor is:

```text
d=(a,b,lambda,rho,xi),     lambda in {L,R}
```

where `rho` is one of:

```text
constant_map_kernel
supported_companion_block_image
partial_constant_hidden_rank_loss
coordinate_side_unit_not_triangular
unsupported_companion_block_image
```

The witness tuple `xi` contains the actual finite data: the collapsed input
pair, constant-map kernel kind, and generated admissible closure kind for
constant-map kernels; the same-side support descriptor for companion block
images; the fixed input, collapsed input pair, companion outputs, closure
kind, and continuation-seed closure data for partial-constant rows; and the
left/right section profiles, listed unit side, and coloured-YBE premise for
coordinate-unit rows.

Define `K_nabla` as exactly the descriptors whose generated admissible
closure and route checks are universal and endpoint-producing:

```text
constant_map_kernel with universal closure and recovery separation,
supported_companion_block_image whose support is such a constant-map kernel,
partial_constant_hidden_rank_loss with universal partial closure and
  universal continuation seed closure,
coordinate_side_unit_not_triangular in the mixed-unit case.
```

Proper closures are terminal contradictions.  Equality closures, failed
routes, and missing route rows stay live in System K.  Two-sided coordinate
unit rows belong to the nondegenerate/guitar branch.  Unsupported companion
block-image rows are structural inconsistencies, not endpoint seeds.

The finite seed classifier is:

```text
kappa : K_nabla -> ({U} x S_U) union ({C} x S_C) union ({M} x S_M).
```

Its state spaces are:

```text
S_U = (left_color,right_color,defect_reason)
S_C = (left_color,right_color,side,fixed_input,domain_color,
       collapsed_inputs,companion_output_color,companion_outputs)
S_M = (left_color,right_color,side)
```

Here `S_U` uses the actual active constant-map or companion reason, including
proper-kernel and universal-kernel constant-map reasons.  The C fields are
read from the partial-constant witness tuple.  Thus signed endpoint generator
entries are not addressable until `d in K_nabla` and `kappa(d)=(E,s)` have
been computed.

The next finite audit layer is the reachable signed endpoint generator table
on these states.  For each `kappa(d)=(E,s)`, first define the finite reachable
state set `S_E^reach` containing the routed seed states.  The set is not a
free declaration: it must be exactly the least signed-transition closure of
the routed seeds under the supplied rows.  Starting from the seed states, each
row

```text
Gamma^{E,+/-}_{a,b}(s,x,y)=(s',x',y',h)
```

whose source state is already reached adds `s'`, and the fixed point must
match the declared reachable set.  Extra declared states are extra endpoint
channels, while omitted transition targets are missing reachable states.  The
declared reachable-state ledger must also be duplicate-free, and the `kappa`
seed classifier must be a functional map on row descriptors: duplicate or
conflicting descriptor entries leave the signed endpoint layer open.  Every
classifier target and reachable-state family must be one of `U`, `C`, or `M`;
unknown endpoint families are reported explicitly rather than routed through a
spurious extra system.
For each reachable
state, each sign, and each local row input, the table must supply one value

```text
Gamma^{E,+/-}_{a,b}(s,x,y)=(s',x',y',h)
```

with the coordinate pair equal to the positive or inverse local row and
`h` in the fixed finite endpoint group or cutoff target for `E`.  The
executable audit records the exact routed seed states, reachable state set,
transition closure of the reachable state set, required full entry domain
derived from the interval fibres, missing or extra table entries, duplicate
entries, positive/inverse coordinate-component
checks against `T`, structural opposite-sign inverse pairing, and the finite
positive-YBE and far-commutativity path checks, and the finite proof gates:

```text
fixed endpoint group or cutoff target
family-scoped endpoint target coverage
concrete endpoint group order matches the group-valued target product
endpoint-target braid-index independence
endpoint-target product-family separation
coordinate components match T and T inverse
signed inverse row pairing
signed inverse cancellation
finite positive endpoint monodromy permutation representation
positive state/coordinate endpoint YBE path
state/coordinate far-commutativity for disjoint crossings
label cocycles recorded only as word-potential diagnostics
fixed-assignment detector-track initialization
Artin detector recurrence on each track
finite word-potential certificate table supplied
positive word-potential identity rows match positive D_Gamma and Gamma labels
endpoint emissions are constant coboundary-defect values
word-potential template coverage for every reachable endpoint state
word-potential templates use only current longitude variables
word-potential variables use only declared fixed detector tracks
raw assignment variables in substitutions are initialized by fixed tracks
word-potential Artin substitution from the detector recurrence
word-potential identity for every positive row
initial word-potential normalization
exact C/M cutoff readouts when cutoff families are present
residual faithfulness for the actual interval fibre action
```

The fixed endpoint target gate is now scoped like the cutoff and residual
gates.  A supplied endpoint group only proves that some table multiplication
can be checked; it does not by itself prove that every routed U/C/M family
has a fixed target.  The target certificate must list the expected routed
families, the covered families, the finite endpoint group orders or cutoff
degrees for those families, braid-index independence, and componentwise
product-family separation.  Missing families, extra families, family labels
outside `{U,C,M}`, nonpositive orders, nonpositive cutoff degrees,
`n`-dependence, or cross-family cancellation leave the signed endpoint layer
open.  The family and target ledgers must also be duplicate-free: repeating a
routed family or assigning two target entries to the same family is not an
exact one-target-per-family certificate.
Every endpoint target-size row must have exactly two fields, `(family, size)`.
A non-sequence target-size ledger, or a row with missing fields, extra fields,
or a non-tuple shape, is a malformed target row; these are reported separately
from nonpositive size values and cannot be used as finite detector factors.
The `family` field in each target-size row must itself be a hashable known
endpoint family in `{U,C,M}`.  Unknown or unhashable family labels in either
the expected/covered ledgers or the target-size rows are certificate failures,
not implicit finite target factors.
The implementation now requires endpoint-target braid-index independence and
product-family separation as explicit finite target certificates, and also
checks that the target ledger supports those claims: each covered family must
have a positive fixed group order or cutoff degree, and target families must
match covered routed families without duplicates.  A well-formed size ledger
without the explicit independence/separation assertions remains open, and
the assertions alone remain nondecisive without the finite target rows.
For C/M cutoff families, the target cutoff degree must also match the
cutoff-readout audit's symmetric degree.  A target ledger declaring an `S_m`
cutoff and a readout audit over `S_k` with `k != m` is reported as
`cutoff_readout_target_degree_mismatch`; the readout may be faithful for its
own degree, but it does not certify the declared target.
Cutoff-routed families must not emit nonidentity labels in the endpoint-group
coordinate of the signed generator rows.  Any such label is an extra endpoint
channel outside the symmetric cutoff readout and is reported as
`cutoff_endpoint_values_have_extra_channels`.

The C/M cutoff gate is now scoped like the residual-faithfulness gate.  A bare
`cutoff_readouts_exact` flag is recorded only as supplied data; it does not
prove the gate.  The cutoff certificate must list the expected routed C/M seed
states, the covered seed states, a positive symmetric degree, and one finite
readout row for every routed C/M seed state.  A row records the seed state,
the readout permutation, and the permutation left after identity cutoff data.
Malformed readout row objects, including a non-sequence readout-row ledger,
are finite certificate failures, not runtime exceptions and not rows that can
be silently ignored.
The checker verifies row-domain exactness, actual membership in the symmetric
group, injective readouts for faithfulness, and identity killed-readouts for
channel killing.  A permutation row is an actual tuple of integers
`0,...,m-1`; booleans, strings, duplicate images, out-of-range entries, or
other malformed values are not elements of the symmetric group.  The expected
and covered cutoff seed-state ledgers must be
duplicate-free; repeated seed entries are reported as an inexact readout
ledger rather than silently collapsed.  Expected, covered, and row cutoff
state keys must also be well formed C/M endpoint states.  A U-family seed,
an unknown family, or a non-tuple seed is malformed for this cutoff-readout
gate even if the malformed sets agree.  These ledgers are compared with the
same hashability-safe markers used by the endpoint state audits: an
unhashable malformed cutoff seed key is reported as finite malformed data, not
allowed to crash the checker or to disappear during set comparison.  The
cutoff degree itself must be a
positive integer; strings, booleans, zero, negative values, or missing
degrees are not finite symmetric cutoff targets.  Cutoff braid-index
independence requires the explicit `braid_index_independent` certificate flag
in addition to the positive fixed degree and exact finite readout rows.  A
readout table whose finite rows are otherwise valid but whose independence
flag is false remains an open cutoff certificate.
The cutoff audit now exposes a separate C/M family-scope ledger as well:
expected families, covered families, and row families must agree exactly with
the routed C/M families.  This is intentionally redundant with seed-state
coverage, because product endpoint rows must not let a C readout certify an M
channel, or vice versa, through an undifferentiated symmetric cutoff.

When a finite endpoint group is supplied, inverse cancellation is checked by
multiplying the emitted endpoint labels in that group.  Adjacent-YBE and
far-commutativity label products are still computed and reported as
diagnostics, but they are no longer independent closure gates once the
word-potential detector lift is present.  The potential-implies-cocycle
argument derives those label relations from the state/coordinate braid
relations and the local word-potential identities.
The concrete group table must also match the target ledger: its order must be
the product of the endpoint-group orders listed for the active group-valued
families.  Symmetric cutoff degrees are handled by the cutoff readout audit
instead of being folded into this product.  A mismatch is reported as
`endpoint_target_group_order_mismatch` and leaves the endpoint target gate
open.  Every endpoint-group order and cutoff degree in the target ledger must
be a positive integer attached to a known routed family; noninteger,
boolean, zero, or negative sizes are malformed target rows rather than finite
target factors.
For a multi-family group-valued target, the concrete endpoint group must also
be the declared coordinate product, not merely a group with the same total
order.  The checker verifies that each product coordinate has the listed
family-factor order, that the element set is the full Cartesian product of
the coordinate supports, and that multiplication in each coordinate is
well-defined from the two coordinate inputs.  A swapped or entangled product
coordinate table is reported as `endpoint_group_product_factor_mismatch`.

The signed endpoint observer is now audited as a reduced full-braid
presentation observer.  Inverse-derived negative rows handle
`sigma_i sigma_i^-1`, the adjacent positive-YBE path gate handles
`sigma_i sigma_{i+1} sigma_i` at the state/coordinate level, and the
far-commutativity path gate handles disjoint crossings.  For every reachable
state, every four-strand local colour/fibre tuple, and every sign pair, the
checker compares the two paths
`Gamma_i^epsilon Gamma_j^delta` and
`Gamma_j^delta Gamma_i^epsilon` for `|i-j|>1`.  The paths must use defined
rows and must return the same endpoint state and colour/fibre tuple.  Label
product mismatches are kept as diagnostics; with a valid word-potential lift,
they are forced to disappear by telescoping, so they do not need to be checked
as separate local assumptions.  Without the state/coordinate path check, the
endpoint accumulation can still be word-dependent.

The remaining observer can be stated more tightly as a finite
monodromy-coboundary-faithfulness certificate.  For each active U/C/M family,
the positive local contexts `(a,b,x,y)` generate a finite presentation
`Pi_E`: adjacent coloured-YBE triples impose the `121=212` context relation,
and disjoint local contexts impose far-commutativity.  A positive endpoint
state system is exactly a finite permutation representation
`rho_E:Pi_E->Sym(S_E^reach)`, so every positive context must act as a
permutation of the exact reachable seed states and the adjacent/far state
relations must hold.

Once this monodromy representation and the word templates are fixed, endpoint
labels are no longer primitive choices.  For a positive context `r` and
state `s`, the checker forms the nonabelian coboundary defect
`W_s(U)^-1 W_{F_r(s)}(A_r^+(U,M))`.  The defect must be constant on a sound
finite detector-variable domain, with the full finite group power `H_E^V`
as the default sound domain.  The positive endpoint emission is the constant
defect value, and the negative row is then forced by inversion.  A smaller
detector domain is accepted only with a proof that all reachable detector
values lie in it.

The old rowwise two-strand witness gate is retained only as diagnostic data.
It is not a decisive endpoint-closure condition: for the standard Artin
convention, `L_1(sigma_1)=x_1`, `L_2(sigma_1)=1`,
`L_1(sigma_1^-1)=1`, and `L_2(sigma_1^-1)=x_2^-1`, so any single emitted
endpoint label can be represented by choosing a two-generator homomorphism
after the row is known.  That local representability does not prove that the
product of emitted labels over an arbitrary braid word lies in `V_beta(H)`.

The decisive replacement is the finite word-potential detector-lift gate.  A
valid audit must cover exactly the interval-derived `D_Gamma` row keys and
the exact reachable endpoint seed states, with duplicate-free ledgers.  It
must supply a positive finite number of detector tracks for every active
endpoint family, chosen before the braid word is read.  Their initial
assignments are derived from the initial interval data and each track follows
the evaluated Artin detector recurrence.

The fixed-track claim is no longer accepted as a standalone boolean.  For
each family count `R_E`, the audit derives expected keys `(E,r)` for
`0 <= r < R_E` and requires one finite initialization row for each key.  Each
family count must be a positive integer attached to one of the known endpoint
families `U`, `C`, or `M`; nonintegers, booleans, zero or negative counts, and
unknown family names are malformed track-count rows, not empty detector-track
families.  The family label itself must be a hashable certificate atom, not a
list or other structured object that merely prints like a family name; an
unhashable or non-`U/C/M` label is an invalid family row and cannot contribute
detector-track keys, initialized raw variables, or word-potential track scope.
Each family-count row must have the two-field finite shape
`(endpoint_family, positive_track_count)`; shortened rows or rows with extra
fields are malformed detector-track data, not alternate syntax.  An
initialization row records the family, nonnegative integer track index,
assignment-rule name, the finite dependencies of the rule, and the local
assignment template for the raw variables.  Allowed dependencies are interval
and initial-state data:
`interval_data`, `endpoint_family`, `routed_seed_state`,
`initial_colour_tuple`, `initial_fibre_tuple`, `strand_index`,
`strand_colour`, `local_input`, and `local_output`.  Braid-word,
braid-prefix, braid-index, failed-detector, finite-search, normalized-law, or
timeout dependencies make the row invalid.  The checker reports missing,
extra, duplicate, and invalid initialization rows before the detector-lift
gate can close.
Every listed initialization entry must be an actual detector-track
initialization row object with those fields.  Tuple-shaped stand-ins are
malformed initialization rows, not abbreviations, and cannot initialize fixed
detector tracks.
It also validates the local assignment template in every row: assignments
must use raw variables `A_{r,j}` for the same track index, must not repeat a
raw variable, and must assign endpoint-group elements.  A row with allowed
dependencies but an invalid template is still not a fixed detector track.
The checker also compares these initialized raw variables with the local
word-potential substitutions: every `A_{r,j}` used by a substitution must be
listed in the initialization template for the same endpoint family and track.
This prevents the finite word identity from using an uninitialized generator
assignment while still claiming the detector tracks were fixed before reading
the braid.

The endpoint potential itself may not be a tautological accumulated product.
For every reachable endpoint state the certificate must supply a finite word
template in current longitude variables only.  Raw generator-assignment
variables may appear in the local Artin substitution, but not in the terminal
readout word.  The variables must also be scoped to the declared fixed track
counts for their endpoint families; a word using `U_{999,j}` is not backed by
an initialized detector track just because it has the right letter.  The audit
must verify the induced positive Artin substitution and the finite local
identity

```text
W_{s'}(A_gamma^+(U,A)) = W_s(U) h
```

for every positive table row.  Equivalently, it checks that
`W_s(U)^-1 W_{s'}(A_gamma^+(U,A))` is a constant coboundary defect on a sound
detector domain and that the emitted label is exactly this constant.  With
initial normalization and inverse-derived negative rows, this word-potential
identity is what converts the finite signed row table into the all-`n`
conclusion `endpoint_E(beta) in V_beta(H_E)`.
Template-state keys, expected/covered word-potential seed-state ledger keys,
and initial-normalization keys must also be well formed endpoint states
`(E,s)` with known endpoint family and tuple-valued seed state.  Malformed
state keys are reported as certificate errors before template scope,
track-scope, or normalization diagnostics are allowed to close.
The initial-normalization ledger must include every actual initial seed state
hit by `kappa`; normalizing only a later reachable state or an unrelated
state does not start the telescope for the routed endpoint obligation.  This
ledger is exact, not merely covering: the normalized seed-state set must equal
the current `kappa` seed image.  A later transition-reachable state may have a
template, but it is not an initial state and must not be listed as one.

The word-potential certificate is concrete finite data.  It records the
template table `(E,s) |-> W_s`, the positive monodromy state map for each
local context, one identity row for each positive `D_Gamma` entry, the next
state, the emitted endpoint label, the positive Artin substitution for that
row, and the finite domain used for the constant-defect check.  The checker
verifies that the identity-row table has the same positive entry domain as
the signed endpoint table, that the next state is the monodromy image, that
the emitted label is the constant coboundary defect, that terminal templates
contain only current longitude variables `U_{r,j}` with nonnegative integer
track and local-position indices, and that the local substitutions are the
positive Artin recurrences.  Boolean indices, strings, negative values, and
other non-index objects are malformed word-potential variables rather than
finite detector-track references; malformed or unhashable variable objects
must be reported as certificate errors, not allowed to crash duplicate,
domain, or normalization checks.  Each word-potential letter, Artin
substitution row, detector-domain assignment entry, and detector-track
assignment entry must have its declared two-field finite-row shape; malformed
row shapes are certificate errors rather than implicit abbreviations.  Negative
word-potential rows, if present, are diagnostic only once the signed endpoint
audit has proved that negative endpoint rows are actual inverses.  Malformed
identity rows with any sign other than `+1` or `-1` are rejected rather than
being treated as harmless diagnostics.  The expected and covered telescoping
entry ledgers are positive-only for closure, but they also reject malformed
signs instead of filtering them away.  The same well-formedness gate checks
that every identity-row and ledger key has the full `D_Gamma` shape
`(E,epsilon,s,a,b,x,y)`, a known endpoint family, and a tuple-valued reachable
state; a shortened positive key is malformed rather than an abbreviated row.
The template table itself is also a finite row ledger: each template row must
have exactly two fields, `((E,s), W_s)`.  A short, extra-field, non-tuple, or
otherwise malformed template row is a certificate error.  Likewise, every
identity-row entry must be an actual word-potential identity row carrying the
required fields; arbitrary tuple-shaped objects are malformed identity-row
objects, not implicit abbreviations.
For positive identity rows, the `next_seed_state` must also be a tuple-valued
hashable state in the same endpoint family.  A malformed or unhashable next
state is a certificate error and must be reported before substitution or
coboundary checks try to look up the next template.
Malformed rows are reported at that gate before downstream template,
track-scope, raw-assignment, or identity diagnostics interpret row fields.
The reachable seed-state and telescoping ledgers use duplicate-safe
normalization before set comparison, so unhashable malformed keys are reported
as malformed finite data instead of escaping as runtime failures.
The same hashability-safe comparison is used for word-potential template
scope, positive identity-entry scope, Artin-substitution variable support, and
raw-assignment initialization support.  Thus a malformed or unhashable formal
variable in a substitution row is rejected as finite certificate data, and it
cannot crash the monodromy-coboundary observer builder while it is deciding
whether the U/C/M endpoint observer has actually been constructed.
Optional negative diagnostics are also scoped to the current signed
`D_Gamma` domain: a negative identity row or telescoping ledger key outside
the interval-derived signed entry domain is an extra diagnostic channel, not a
harmless ignored row.
The checker then exhausts all
assignments of the finitely many variables in the positive row to the fixed
endpoint group, or to a certified sound detector-domain subset, and checks
that the coboundary defect is constant with value equal to the row label.
When the monodromy constructor derives a word-potential certificate, a
nonconstant defect does not receive the first sampled value as a placeholder
endpoint emission; the derived endpoint value is left outside the group, so
the row remains open until a genuinely constant defect or a sound restricted
domain is supplied.
Subset detector domains are finite row data: each assignment row must contain
exactly the variables in the row's coboundary-defect support, no missing
variables, no extras, no repeated variable, and only values in the fixed
endpoint group.  A subset domain also needs an explicit soundness proof that
all reachable detector values lie in it, recorded as finite witness data such
as an exhaustive reachable-value enumeration or a symbolic detector-domain
invariant; otherwise the checker falls back to the full finite group power as
the only accepted sound domain.
This removes the previous loophole
where a bare boolean could stand in for a tautological accumulated potential.
The executable close criterion derives the Artin-recurrence and
terminal-readout-longitude gates from these same substitution and template
checks; separate `artin_detector_recurrence_verified` or
`terminal_readout_longitudes_verified` booleans are diagnostic only.
It also derives telescoping braid-index independence from the finite track
counts and exact initialization rows, because those rows explicitly forbid
`braid_index` and braid-word dependencies.
The fixed-before-braid diagnostic is now separated from local assignment
template validity: a row with forbidden braid-prefix or search dependencies
is reported as an unfixed row, while a dependency-valid row with a malformed
assignment template is reported only as a template error.

The implementation now exposes two interval-derived constructors for this
audit layer.  The lower-level constructor
`universal_k_signed_endpoint_generator_audit(...)` takes already-supplied
signed rows and recomputes the full `D_Gamma` domain from the fibres, then
fills the coordinate, inverse, YBE, and fixed-track telescoping gates by
running the finite checkers.  Its signed entry-key comparisons are
hashability-safe: a supplied row whose seed state makes the full
`(E,epsilon,s,a,b,x,y)` key malformed or unhashable is reported as an extra
or malformed signed row and cannot crash the domain, seed-key, or monodromy
permutation checks.  The higher-level constructor
`universal_k_endpoint_observer_build(...)` is the monodromy-coboundary
observer builder: it reads the positive rows from the word-potential identity
table, sets the positive coordinate part to the actual interval map
`T_{a,b}`, derives negative rows by inversion in the fixed endpoint group,
computes the reachable seed-state closure from the current `kappa` entries,
builds the finite positive local-context monodromy presentation, builds the
fixed-assignment telescoping audit, and then calls the same signed endpoint
audit.  The monodromy presentation is exposed as
`UniversalKEndpointMonodromyPresentation`: its generators are exactly the
positive local contexts `(E,a,b,x,y)`, its adjacent relations are the two
positive 121/212 context paths computed from `T`, and its far-commutativity
relations are the nontrivial disjoint context swaps inside each active family;
tautological self-swaps are omitted.  The adjacent-relation ledger is a
full-path ledger: for every active colour/fibre triple, both the 121 and 212
positive paths must be readable from the current `R_C` and `T` tables.  A
missing base row or local row is a finite monodromy-presentation failure, not
an absent relation.  The endpoint-family labels in the presentation ledger
and in every local context must be hashable members of `{U,C,M}`.  Unknown or
unhashable families, including malformed context families, are finite
monodromy-presentation failures and cannot be hidden as absent generators.
Thus the endpoint-state representation
is no longer implicit in later path checks; it is a finite object attached to
the observer build for the exact U/C/M families hit by `kappa`.  The build also records
`UniversalKEndpointMonodromyRepresentationAudit`, which reads the positive
rows as maps on the reachable seed states, checks that every context acts by
a permutation of the seed states in its family, and verifies every explicit
adjacent/far relation in the monodromy presentation.  Missing positive
contexts, nonconstant coboundary defects, out-of-scope detector tracks,
missing C/M readouts, or missing residual faithfulness remain visible audit
failures rather than being filled by defaults.  This keeps the local
certificate from being a list of unsupported boolean claims.
The monodromy representation audit uses the same well-formedness guard on
reachable seed states: malformed or unhashable reachable-state entries are
rejected as finite ledger data and cannot crash the permutation or relation
checks.
There is also a monodromy-to-word-potential handoff constructor,
`universal_k_word_potential_certificate_from_monodromy(...)`.  It takes
positive endpoint-state monodromy rows and state-indexed word templates,
derives the exact reachable seed-state closure from the current `kappa`
seeds, computes the positive entry domain, inserts the Artin substitutions
forced by the target templates, and evaluates the nonabelian coboundary
defect to obtain the emitted endpoint label.  With the full detector-variable
domain this can only certify defects that are genuinely constant on all
finite assignments; a smaller detector domain is used only when the row also
contains explicit soundness witness data such as a reachable-value
enumeration or symbolic detector-domain invariant.  The returned certificate
is still passed through the same word-potential audit, so a nonconstant
defect, missing monodromy row, unsound detector-domain subset, malformed
template, or missing residual-faithfulness theorem keeps the endpoint
observer open.  This removes another arbitrary choice from the U/C/M
observer data: positive emissions are computed from the monodromy
representation and potentials rather than supplied independently.
The family-level handoff is
`universal_k_endpoint_observer_builds_from_monodromy_by_family(...)`.  It
accepts one fixed endpoint group, positive monodromy row table, template
ledger, and optional detector-domain soundness data for each endpoint family;
derives the per-family word-potential certificates by the constructor above;
and then calls the ordinary family observer audit.  Thus the preferred
remaining certificate input is exactly the finite local data
`(H_E,rho_E,W_E,D_E,RF_E)` for each active family, with emissions and signed
rows derived and rechecked rather than supplied as an independent table.
When no restricted detector-domain assignment map is supplied for a positive
entry, the constructor checks the coboundary defect on the full finite
detector domain.  This is the safest valid path: a defect constant on the full
domain needs no separate soundness witness.  The raw monodromy front door is
now checked to build a complete U/C/M family observer package from identity
monodromy rows, empty word potentials, full-domain constant defects, fixed
endpoint targets, exact C/M cutoff readouts, per-family residual rows, and a
product residual-faithfulness theorem.  This confirms the constructor path
future nontrivial observers must use; it does not assert that nontrivial
`rho_E` and `W_E` data exist in every surviving interval.
The monodromy handoff also composes with the same explicit residual-trivial
helper flags used by the identity observer constructor.  When one of those
flags is supplied, for example the coordinate-identity residual helper, the
handoff may derive the per-family residual-faithfulness rows and the
multi-family product residual theorem from the current interval instead of
requiring those rows to be hand-supplied.  This is still limited to the
already-proved residual-trivial subcases; it only removes duplicated
certificate data from otherwise explicit monodromy-coboundary observer
packages.
The identity and monodromy observer constructors now share one residual-helper
selector for these subcases.  Thus strict identity, coordinate identity,
singleton-fibre, supplied fibre-label identity, and canonical fibre-label
identity rows are derived in one fixed order for both handoff paths, with
failed supplied fibre-label ledgers remaining sticky rather than being hidden
by the canonical fallback.  The monodromy handoff has an explicit regression
row for this sticky supplied-label case, so canonical fibre labels cannot close
an observer package after a stale or malformed supplied label ledger has been
selected.
The top-level `post_linear_remaining_finite_system_audit(...)` can now take
that smaller monodromy-coboundary package directly through its
`universal_k_monodromy_*_by_family` inputs.  It first computes the current
`K_nabla`/`kappa` ledger for the interval, derives the family observer build
from those monodromy inputs, and retains the same family-build diagnostics in
the post-linear proof object.  A stale or extra family still remains only
diagnostic data unless it matches the current routed endpoint families and
passes target, cutoff, product, and residual-faithfulness checks.
The monodromy handoff now also has its own front-door ledger,
`UniversalKMonodromyFamilyInputAudit`, exposed by
`universal_k_monodromy_family_input_audit(...)`.  Before any observer is
derived, it checks that the raw seed-classifier ledger is internally
well-formed and functional, then checks the raw finite package family-by-family:
fixed endpoint groups, state-indexed word-potential templates, positive
monodromy state rows, optional detector-domain assignments, and optional
detector-domain soundness witnesses.  It reports malformed, duplicate, or
conflicting seed-classifier rows; malformed family rows; unknown U/C/M family
names; duplicates; missing active families; extra stale families; and
detector-domain assignments without soundness witnesses.  It
normalizes every top-level by-family ledger first, so a non-sequence endpoint
group, template, positive-row, detector-domain, or detector-witness ledger is
reported as one malformed row object instead of being iterated, ignored, or
allowed to crash the handoff.  Any nonempty monodromy subledger triggers this
audit and the family-build diagnostic, including detector-domain assignments
or soundness witnesses supplied without endpoint groups, templates, or
positive rows.  Auxiliary-only observer attempts are therefore reported as
incomplete or malformed rather than silently ignored.  The monodromy-derived
family build attaches this audit and requires it to be exact, so a missing
`rho_E`, `W_E`, `H_E`, or detector-domain witness is now a finite ledger
failure rather than an opaque missing observer.
When this raw monodromy input audit is attached to retained family builds, it
must also match the current `K_nabla`/`kappa` ledger and those retained
builds.  The raw seed-classifier entries must be the current entries, with no
stale extra descriptor and no missing current descriptor.  The endpoint group
row for each family must match the finite group in the retained
word-potential certificate; the raw template rows must match the retained
templates; the raw positive monodromy state rows must match the retained
positive state/coordinate transitions after forgetting emitted endpoint
labels; and any restricted detector-domain assignment or soundness-witness
maps must match the corresponding identity-row data inside the retained
certificate.  An internally exact raw monodromy ledger for a different
observer or for a stale classifier ledger is rejected as stale input rather
than accepted as construction evidence for the retained build.
Every positive monodromy row must also have a well-formed positive signed
entry key: the family must be one of U/C/M, the seed state must be a hashable
tuple state for that family, the sign must be positive, and the local colour
and fibre inputs must form a row in the current positive context domain.
Malformed or unhashable seed states are carried as finite bad ledger data and
cannot crash the monodromy closure while the observer package is being audited.
The next seed state is part of the same finite permutation data: it must be a
hashable tuple state for the row's family.  A malformed, unhashable, or
non-tuple next state is a malformed positive-row package at the monodromy
handoff, and a direct representation audit reports it as a
next-state-outside-family context-map failure rather than accepting it as a
hidden observer state.
The raw positive monodromy rows define only the finite state map `F^E_r`.
They must not carry primitive endpoint emissions.  Any non-`None` endpoint
value in such a raw monodromy row is stale emission data and is rejected
before the observer is constructed; the actual endpoint labels must be the
constant coboundary defects forced by `rho_E` and the templates `W_s`.
The direct coboundary constructor applies the same admissible-row filter:
malformed next states and stale primitive emissions do not seed the reachable
monodromy closure and do not produce word-potential identity rows.  The
family-level audit remains the diagnostic front door for reporting those bad
raw rows, while the lower-level constructor cannot use them to derive hidden
emissions.
Restricted detector-domain maps are checked at the same entry-key granularity
as the positive monodromy table.  Every assignment key must be a well-formed
positive entry key for the same endpoint family and, when the interval is
available, must lie in the current positive context domain.  Every such
assignment key must have a matching soundness-witness key, and a witness key
without a corresponding restricted-domain assignment is also a ledger error.
The restricted-domain values themselves are finite row data: each assignment
value must be a nonempty tuple of tuple assignment rows, every assignment
entry must have a valid word-potential variable and an element of the fixed
endpoint group, and every witness value must be a nonempty duplicate-free
tuple of recognized detector-domain soundness witnesses.
Detector-domain soundness flags and witnesses are legal only when an actual
restricted detector-domain assignment subset is supplied for that positive
row.  In the full finite-domain case, any soundness flag or soundness witness
is stale certificate data and keeps the word-potential certificate open; it
cannot be interpreted as an extra proof channel.
When the interval is available, the same ledger derives the reachable
monodromy seed-state closure from the supplied positive rows, recomputes the
full positive local-context entry domain from the current fibres, and checks
that the supplied positive monodromy rows are duplicate-free, have no missing
or extra entry keys, and have coordinate outputs equal to the actual
`T_{a,b}(x,y)`.  Thus a proposed `rho_E` table must already be total on the
positive context domain before the coboundary defects are evaluated.
The word-potential side is checked against that same derived closure: the
template ledger must contain exactly one `W_s` for every reachable
family-state pair and no stale template states outside the closure.  Missing,
extra, or duplicate template states are raw monodromy input failures, not
late coboundary surprises.
The builder reads only actual word-potential identity row objects when forcing
positive endpoint rows.  Malformed tuple-shaped identity entries remain in
the word-potential certificate as certificate errors and cause the observer to
stay open; they are not interpreted as positive rows and are not silently
discarded as harmless omissions.
The signed endpoint audit itself now carries this explicit representation
gate.  A supplied signed table cannot close merely by setting the older
state/coordinate booleans: an explicit monodromy representation audit must be
present and must prove every context map and every presentation relation.
Missing explicit monodromy data is reported as
`explicit_endpoint_monodromy_representation_missing`, and the routed
obstruction data exports
`signed_endpoint_generator_explicit_monodromy_representation_present` together
with the verification result.  The derived constructor supplies that audit
automatically from the current interval, reachable seed states, and rows.
The top-level post-linear audit retains the constructed
`UniversalKEndpointObserverBuild` whenever it derives the signed endpoint
generator from a word-potential certificate.  The exported obstruction data
records whether that observer build is present, whether it proves the
endpoint observer, which positive entry keys it forced, and which monodromy
contexts it used.  This prevents the U/C/M observer construction from being
hidden behind the signed-generator audit alone.
The family-scoped constructor
`universal_k_endpoint_observer_builds_by_family(...)` builds one observer per
active U/C/M family from the family's word-potential certificate and audits
the resulting family ledger with
`UniversalKEndpointObserverFamilyBuildAudit`.  That audit requires exact
coverage of the active families hit by `kappa`, rejects malformed or duplicate
build rows, checks that each build is single-family scoped with exactly the
family's seed classifier entries and seed states, and only closes when every
family build proves its endpoint observer.  The family ledger now validates
the `kappa` entries themselves before using them as active seed evidence:
malformed classifier rows and classifier targets outside hashable U/C/M seed
states, duplicate classifier entries, duplicate descriptors, and conflicting
descriptor-to-target rows are reported as finite ledger errors, not as vague
missing observers and not as exceptions during seed-state set comparison.
Thus a combined product endpoint row cannot hide the absence of a C or M
observer behind a successful U build.
The family ledger is not allowed to be an opaque list of already-built
observers.  It must also expose exact input rows for each active routed
family: the word-potential certificate row, detector-track initialization
row family, endpoint-target audit row, and residual-faithfulness theorem row.
Active C/M cutoff families must also expose exact cutoff-readout rows.  A
wrapper containing proving build objects but omitting these explicit ledgers
remains diagnostic only and is reported with missing-family certificate,
detector-track, endpoint-target, cutoff-readout, or residual-theorem
failures.
Those auxiliary ledgers must also match the retained build internals.  The
supplied word-potential certificate for a family must equal the certificate
inside that family's telescoping audit; the supplied detector-track rows must
match the detector rows used by that audit; the supplied endpoint-target,
C/M cutoff-readout, and residual-faithfulness theorem rows must equal the
objects retained inside the corresponding observer build.  A stale auxiliary
row is rejected even when the retained build object itself proves.  This
prevents a family observer from closing with one hidden construction while the
exported proof ledger advertises different certificate, detector, target,
cutoff, or residual data.
Those top-level family-observer input ledgers are normalized before any
builder runs.  A non-sequence certificate, detector-track, endpoint-target,
cutoff-readout, residual-theorem, or identity-cutoff-degree ledger is reported
as one malformed row object.  It is not iterated character-by-character,
ignored as absent input, or allowed to crash the direct family handoff.
Any nonempty direct family-observer subledger also triggers that handoff:
detector-track, endpoint-target, cutoff-readout, or by-family residual
theorem rows supplied without a word-potential certificate ledger are audited
as incomplete observer attempts rather than ignored as absent data.
The same visibility rule now applies to direct signed-generator detector-lift
auxiliaries.  Supplying detector-track count rows or detector-track
initialization rows directly to `post_linear_remaining_finite_system_audit(...)`
without a word-potential certificate creates a diagnostic telescoping audit
instead of silently dropping those ledgers.  Malformed count rows such as
`None`, malformed initialization rows, unknown families, duplicate track
keys, nonpositive counts, missing word-potential templates, and missing
initial normalization are then exported in the signed-generator obstruction
data.  This is not an observer existence theorem; it is the finite audit gate
that prevents incomplete direct detector-lift data from masquerading as
absent input.
All family labels in these build, certificate, detector-track, endpoint-target,
cutoff-readout, and residual-theorem rows must be hashable certificate atoms
equal to `U`, `C`, or `M`.  An unhashable list-like label is not alternate
family syntax, cannot instantiate a per-family observer, cannot contribute
initialized detector-track scope, and is reported as an unknown-family ledger
error at the family aggregation gate.
There is also a canonical identity-emission constructor,
`universal_k_identity_endpoint_observer_builds_by_family(...)`.  It builds
the identity monodromy-coboundary candidate for every active family hit by
the current `kappa`: U uses the actual triangular-recovery unit group
`U_tri`, while C and M use symmetric cutoff groups with enough distinct
readout permutations for their routed seed states.  This constructor removes
only the finite bookkeeping of the identity observer candidate.  It does not
assert residual faithfulness and it does not prove that the true residual
fibre action is trivial.  Without a scoped residual-faithfulness theorem, the
constructed family builds remain open and report the missing residual gate.
If the constructor is given explicit identity cutoff degrees, those rows are
also finite ledger data: each row must have shape `(family, positive_degree)`,
the family must be a hashable active cutoff family `C` or `M`, duplicate
families are rejected, and nonpositive, boolean, unknown, unhashable, extra,
malformed rows, or a non-sequence degree ledger keep the identity observer
ledger open rather than being silently replaced by the default symmetric
degree.
The top-level helper `post_linear_remaining_finite_system_audit(...)` can
now derive this canonical candidate directly when
`universal_k_identity_endpoint_observer_candidates=True`.  This is an
explicit opt-in path for retaining the finite monodromy-coboundary ledger in
the main post-linear audit.  It remains deliberately nondecisive: if the
current `kappa` image has no active endpoint family, the derived ledger
reports that no active family exists; if active families are present but the
scoped residual-faithfulness rows are absent, the ledger remains an open
observer candidate rather than a closure proof.
When a current routed endpoint system does have an exact active `kappa`
ledger and the canonical identity observer is paired with a proved residual
faithfulness subcase, the main finite-system classifier consumes the family
observer as a closure certificate.  In particular, a routed System U row over
a strict identity local interval now closes as
`closed_by_triangular_recovery_endpoint_observer_family_build`: the observer
uses the current `U_tri` group-table fingerprint, covers the full interval
`D_Gamma` domain, proves the strict-identity residual theorem, and leaves no
remaining routed U obligation.  This is a genuine closed subcase, not a proof
of the general U observer existence theorem.
The same strict-identity family observer is now consumed by the main
classifier for product endpoint rows.  Routed U+C, U+M, C+M, and U+C+M
products close only when the U observer, if present, uses the current `U_tri`
table; the C and M observers, if present, have exact cutoff/readout and
residual theorem data; and the product residual-faithfulness theorem is
proved.  The exported closed-family tuple is checked family-by-family, and
`unclosed_routed_endpoint_systems` must be empty.  Thus these strict-identity
product closures do not use or permit cross-family endpoint cancellation.
The product closure is not limited to strict identity rows.  The main
classifier also consumes the singleton-fibre, coordinate-identity, supplied
fibre-label identity, and canonical fibre-label identity residual subcases
for every multi-family routed product U+C, U+M, C+M, and U+C+M: the U
observer, when present, still has to use the current `U_tri` table, C and M
still have to carry the exact cutoff/readout ledgers, and the product
residual theorem must report the corresponding residual channel reason.
These closures cover residually trivial non-strict local motion; they still
do not construct the general nontrivial U/C/M endpoint observer.
All automatic residual-faithfulness helpers require the supplied local
interval table to be complete and type-correct: `R_C` must be a bijection on
colour pairs, every local `T_{a,b}` row must be present exactly on its fibre
domain, and every local output must land in the fibres prescribed by
`R_C(a,b)`.  A malformed raw interval object is never an automatic residual
closure proof, even if the rows inspected by a particular subcase look
harmless.
There is one automatic residual-faithfulness subcase:
`universal_k_strict_identity_residual_faithfulness_audit(...)` proves the
residual gate when every quotient row fixes its colour pair and every local
fibre row is strictly `(x,y)->(x,y)`.  In that case every braid word has
trivial residual fibre action, so the helper emits one schematic all-`n`
residual row per active endpoint family with dependencies only on the
interval, local row table, routed seed state, residual input tuple, and
endpoint channel, and local fibre coordinate.  The identity constructor can
consume this proof when
`derive_strict_identity_residual_faithfulness=True`.  This closes only the
strict identity-fibre subcase; non-identity U/C/M endpoint observers still
need their own residual-faithfulness theorem.
There is also a coordinate-identity residual-faithfulness subcase:
`universal_k_coordinate_identity_residual_faithfulness_audit(...)` proves
the residual gate when every local row preserves the raw fibre coordinate
pair `(x,y)`, even if the quotient colour pair changes, and those same raw
coordinate values are members of the output fibres dictated by the quotient
row.  A table that merely writes `(x,y)` while moving to colours whose fibres
do not contain `x` or `y` is not type-correct and is rejected.  Along any
braid word the fibre coordinate tuple is unchanged; for a braid in the
quotient kernel the final quotient colours return, so the residual fibre
action is identity.  The identity constructor consumes this proof only when
`derive_coordinate_identity_residual_faithfulness=True`.
There is a second automatic residual-faithfulness subcase:
`universal_k_singleton_fibre_residual_faithfulness_audit(...)` proves the
residual gate when every fibre `A_c` has exactly one point.  Then each
fibre product `X_z` is a singleton for every quotient-colour tuple `z`, so
the bundled residual fibre action is trivial for every braid index.  The
identity constructor consumes this proof only when
`derive_singleton_fibre_residual_faithfulness=True`.  This is independent of
the strict identity-row condition: quotient colours may move, but there is no
nontrivial fibre coordinate left to move.
There is also a fibre-label identity residual-faithfulness subcase:
`universal_k_fibre_label_identity_residual_faithfulness_audit(...)` proves
the residual gate from finite label rows `(color, fibre_point, label)`.
The rows must cover every fibre point exactly once, labels must be finite
hashable certificate data, the label map must be injective on each fibre,
and every local row must preserve the two labels coordinatewise: if
`R_C(a,b)=(c,d)` and `T_{a,b}(x,y)=(u,v)`, then
`ell_c(u)=ell_a(x)` and `ell_d(v)=ell_b(y)`.  The preservation check ranges
over every colour pair and every fibre input; a missing quotient row or a
missing local `T` row is a finite preservation failure, not a vacuous pass.
Along any braid word the
ordered label tuple is unchanged; for a braid in the quotient kernel the
final quotient colours return, and injectivity on each returned fibre forces
the final fibre tuple to equal the initial one.  The identity constructor
consumes this proof only when
`derive_fibre_label_identity_residual_faithfulness=True` and the finite
`fibre_label_identity_rows` ledger is supplied.  That label ledger is
normalized as finite row data before the audit: a non-sequence object such as
`None` or a string is one malformed label row, not a character-by-character
ledger and not an exception.
There is now a canonical fibre-label identity residual-faithfulness subcase:
`universal_k_canonical_fibre_label_identity_rows(...)` constructs the least
finite label ledger forced by local coordinate-label preservation.  It starts
with one node `(color, fibre_point)` for every fibre point and identifies
`(a,x)` with `(c,u)` and `(b,y)` with `(d,v)` for every local row
`R_C(a,b)=(c,d)` and `T_{a,b}(x,y)=(u,v)`.  The derived component labels are
then audited by the same fibre-label checker.  The subcase closes only if
those component labels are injective on every fibre and every local row
preserves them coordinatewise; if the generated relation identifies two
distinct points in one fibre, the audit fails with a finite
`fibre_label_identity_not_injective` reason.  The identity observer
constructor consumes this proof only when
`derive_canonical_fibre_label_identity_residual_faithfulness=True`.  This is
not a general endpoint observer: it closes exactly the case where residual
motion is already killed by the canonical preserved-label quotient.
The identity observer constructor also exposes an aggregate opt-in,
`derive_automatic_residual_faithfulness=True`.  This flag tries only the
already-proved automatic residual helpers: strict identity, coordinate
identity, singleton fibres, supplied fibre-label identity when a label ledger
is present, and finally canonical fibre-label identity.  It is a convenience
constructor for these symbolic subcases, not a new existence theorem for
nontrivial U/C/M endpoint observers.  The reusable selector
`universal_k_automatic_residual_faithfulness_audit(...)` returns the first
proving residual-faithfulness audit among those subcases.  If a supplied
fibre-label ledger is present after the strict, coordinate-identity, and
singleton helpers fail, that supplied label ledger is treated as certificate
data: a failed supplied-label audit is returned as the open obligation rather
than being hidden by the canonical-label fallback.  If no supplied label
ledger is present, the selector falls back to the canonical-label audit and
returns it open when it does not prove.  At the top-level audit the
corresponding flag is
`universal_k_identity_automatic_residual_faithfulness=True`; setting it
constructs the identity endpoint observer candidate path and lets these
helpers close exactly the subcases whose finite hypotheses are verified.
The top-level audit also derives the same identity observer candidate path
when any individual helper flag is supplied:
`universal_k_identity_strict_residual_faithfulness`,
`universal_k_identity_coordinate_residual_faithfulness`,
`universal_k_identity_singleton_residual_faithfulness`,
`universal_k_identity_fibre_label_residual_faithfulness`, or
`universal_k_identity_canonical_fibre_label_residual_faithfulness`.  A
helper flag is no longer ignored merely because the aggregate automatic flag
was not set.
At the top-level post-linear audit, the same residual-trivial identity
observer path is now checked explicitly for each one-family routed endpoint
system.  A U-only route may close as
`closed_by_triangular_recovery_endpoint_observer_family_build`; a C-only
route may close as
`closed_by_universal_continuation_endpoint_observer_family_build`; and an
M-only route may close as `closed_by_mixed_unit_endpoint_observer_family_build`.
For these one-family cases the per-family residual theorem is the full
active-family residual scope, so no separate product residual-faithfulness
theorem is required.  The retained family ledger still records the residual
channel reason by family and rechecks the current `kappa` seed ledger, current
interval rows, and the current U triangular-recovery target when U is active.
This closes only the already-proved singleton-fibre, strict identity,
coordinate-identity, supplied fibre-label identity, and canonical fibre-label
identity residual-trivial subcases for individual U, C, and M obligations; it
does not construct the missing nontrivial U/C/M observers.
The aggregate automatic selector is also checked at this one-family routed
level: when an interval satisfies one of the selector's hypotheses, such as
coordinate-identity residual motion, the derived family ledger closes the
single active U, C, or M endpoint system without requiring a product theorem.
The same exactness rule applies when the identity observer constructor is
given both explicit supplied-label and explicit canonical-label flags.  If
the supplied fibre-label residual theorem is attempted and fails, that failed
certificate data remains the open obligation; the canonical-label helper is
not allowed to replace it in the same per-family or product-family observer
candidate.
All automatic residual-faithfulness helpers preserve the full supplied
routed seed-state ledger in the theorem.  They may use only the well-formed
U/C/M seed states to emit schematic rows, but malformed, wrong-family, or
unhashable seed-state entries remain in the expected and covered theorem
ledgers and therefore keep the residual theorem open.  An automatic helper
cannot silently drop bad seed data and prove residual faithfulness for a
smaller endpoint scope.
For a multi-family product endpoint row, the family ledger also requires a
separate product residual-faithfulness theorem scoped to the full active
family set and the full set of seed states hit by `kappa`.  Per-family
residual-faithfulness rows prove the individual observers, but they do not by
themselves prove that killing all endpoint channels forces the bundled
residual fibre action to be trivial.  The product theorem is not required in
the one-family case, where the family build's own residual-faithfulness audit
already has the full active-family scope.
The product theorem must also preserve the exact endpoint-channel reason
ledger by family.  Matching the active families and the seed states is not
enough: a product theorem whose rows use placeholder or different channel
names, such as a generic product channel replacing the per-family U/C/M
reasons, does not prove that the same routed endpoint channels are faithful to
the actual residual motion.  Such a certificate is reported as
`endpoint_observer_product_residual_faithfulness_channel_scope_mismatch` and
cannot close a product endpoint row.
The checker now also compares the full well-formed endpoint-channel key
ledger by family, not only the third-field channel reason.  Since channel keys
have shape `(E, s, channel_name, optional_local_data...)`, a product theorem
that keeps the same reason string but changes or drops the optional local
channel data proves faithfulness for a different concrete endpoint channel.
That narrower mismatch is reported as
`endpoint_observer_product_residual_faithfulness_channel_key_scope_mismatch`.
The product residual theorem's active and covered family ledgers must also
be finite well-formed `{U,C,M}` ledgers.  Unknown or unhashable family labels
in the product theorem do not crash the family build and do not match the
active product scope; they produce a product residual family-scope mismatch
and leave product closure open.
The top-level post-linear audit can now retain this family-build ledger
directly, or derive it from per-family word-potential certificates, endpoint
target audits, C/M cutoff readouts, and per-family residual-faithfulness
theorems.  Its routed-endpoint obstruction data reports the expected,
covered, missing, extra, duplicate, malformed, scope-mismatched, and unproved
family builds, plus the product residual-faithfulness gate, separately from
the older combined signed-generator audit.
It also rechecks any retained family-build ledger against the current
`K_nabla` seed classifier and the current endpoint interval table.  For each
family build it recomputes the full `D_Gamma` domain from the current
interval and that build's reachable seed states, compares it with the build's
required-entry ledger, and recomputes coordinate compatibility, inverse
pairing, inverse cancellation, positive state/coordinate YBE, and far
state/coordinate commutativity against the current table and endpoint group.
For a U-family build, the recheck also recomputes the current triangular
recovery unit observer on the endpoint interval and requires the build's
endpoint group to be exactly that current `U_tri` target by finite group-table
fingerprint, not just by finite group order.  Thus a word-potential observer
over some other same-order finite group can remain diagnostic evidence, but
it cannot close the System U obligation routed by the current `kappa` ledger.
The retained obstruction ledger reports this as
`signed_endpoint_generator_current_u_tri_target_mismatch` for combined signed
tables and as `endpoint_observer_family_build_current_u_tri_target_mismatch`
for per-family observer builds.
Thus a family observer built for a stale interval or stale `kappa` ledger can
still be retained as diagnostic evidence, but it cannot be reported as closing
the current routed `K_nabla` obligations.
When the retained ledger matches the current `kappa`, passes the current
interval row checks, proves every family observer, and satisfies the product
residual-faithfulness gate, it is now a routed endpoint closure certificate:
`endpoint_observer_family_build_closed_families` lists the active U/C/M
families it closes, and the corresponding
`system_*_closed_by_endpoint_observer_family_build` predicates remove those
families from `unclosed_routed_endpoint_systems`.
When the ledger is derived from per-family word-potential certificates, the
input certificate rows are themselves audited: malformed two-field rows,
non-certificate values, unknown endpoint families, duplicate certificate
families, missing active-family certificates, and extra certificate families
are reported as finite data.  Such rows are not silently collapsed into a
generic missing-build failure.
The same exact-ledger rule now applies to the auxiliary rows used to build
the per-family observers.  Detector-track initialization rows must cover
exactly the active families with no malformed rows, unknown families, or
duplicate track keys.  They must also be fixed before braid reading at the
family aggregation gate itself: forbidden dependencies such as braid words,
braid prefixes, failed detector searches, timeout data, finite-search
results, or normalized-law sequences are reported as unfixed detector rows.
Their assignment templates are checked as finite row data against the
family's word-potential endpoint group: each entry must assign a raw
`A_{r,j}` variable for the same detector track, may not duplicate a variable,
and must use a value in the fixed endpoint group.  Endpoint-target audit rows
and residual-faithfulness theorem rows must cover exactly the active families;
missing such rows is a missing-family certificate failure, not an optional
omission.  C/M cutoff readout audit rows must cover exactly the active cutoff
families whenever C or M is active.  Malformed
rows include wrong-typed auxiliary values, not merely wrong tuple shapes; the
builder may select only endpoint target audits for the endpoint target ledger,
cutoff readout audits for the cutoff ledger, and residual-faithfulness audits
for the residual ledger.  Unknown families, duplicate families or keys,
missing active families, and extra auxiliary families are reported separately.
The builder still lets the individual observer audit explain a malformed
target, cutoff, detector track, or residual proof, but it no longer allows a
missing, duplicate, or stale auxiliary row to be hidden by the first valid row
selected for a family.
When a fixed endpoint group is declared as a product over multiple endpoint
families, the signed endpoint audit now also checks family support of each
emitted label: a row in family `E` must have identity components in every
other declared endpoint-group factor.  This finite check prevents a blended
product-group label from closing a multi-family endpoint row by hidden
cross-family cancellation.  Cutoff targets remain accounted for separately by
the exact C/M cutoff readout audit.
The post-linear function now accepts this builder-level input directly:
supplying `universal_k_word_potential_certificate` plus detector-track
initialization rows causes `post_linear_remaining_finite_system_audit(...)`
to construct the observer and then run the same current-interval closure
checks.  Thus a future U/C/M certificate does not need to pre-expand or
hand-maintain a separate signed row table; the signed table is derived from
the monodromy-coboundary data and checked against the current `kappa` ledger.
The audit also records the concrete failure rows or local triples for each
derived gate, so a failed certificate can be repaired without reverse
engineering which table entry broke.  The signed endpoint table proof now
also requires that the entry domain be derived from the interval; a manual
audit that supplies a smaller prover-selected entry-key set is recorded as
`signed_entry_domain_not_derived_from_interval` and cannot close the
endpoint layer.  The post-linear wrapper also recomputes the full `D_Gamma`
domain from the current interval and the audit's reachable seed states before
allowing a signed-generator proof to close a routed endpoint family.  Thus a
manually constructed audit with a too-small required-entry ledger is reported
as `signed_entry_domain_mismatch_current_interval` even if its own boolean
gates claim success.  The wrapper also recomputes coordinate compatibility,
inverse pairing, inverse cancellation, positive state/coordinate YBE, and far
state/coordinate commutativity against the current interval and endpoint
group.  A table whose own booleans claim those row checks succeeded is still
reported as `signed_row_checks_mismatch_current_interval` if the recomputed
current-interval failures are nonempty.  Likewise, the finite row checks
themselves must be derived from the supplied rows, actual interval table,
endpoint group or cutoff multiplication, and fixed detector-lift data;
unsupported success flags are recorded as
`finite_signed_row_checks_not_derived_from_tables`.
For group-valued endpoint rows, the concrete endpoint group must be supplied
to evaluate inverse-cancellation and positive-YBE label products.  A row
audit that names only an endpoint target order, or supplies success booleans
without the group table, is reported as missing the endpoint group for finite
signed row checks.
For a routed U family, current-target matching is stronger than matching the
finite order.  The wrapper recomputes the current triangular-recovery unit
group `U_tri` and compares a finite group-table fingerprint containing the
concrete element set, identity, inverse table, and multiplication table.  A
same-order placeholder group can still prove an internally coherent signed
table, but it does not close System U unless its fingerprint is the current
`U_tri` fingerprint.

The post-linear wrapper can now derive this signed endpoint audit directly
from supplied table rows and witnesses after computing the interval's current
`K_nabla` and `kappa` entries.  This makes a table built against a stale or
different seed classifier visible as a mismatch in the obstruction data
rather than a silently accepted external certificate.  When no reachable state
set is supplied, the wrapper derives it as the least transition closure of
the current `kappa` seeds under the supplied signed rows before forming the
full `D_Gamma` domain.

The wrapper also reports whether endpoint targets are actually proved, not
only whether an endpoint group was supplied.  Its finite obstruction data now
separates the raw supplied-target flag from the scoped target audit: expected
families, covered families, target families, endpoint group orders, cutoff
degrees, scope agreement with the current `kappa`, and whether the target
audit proves the fixed endpoint target obligation.  A supplied endpoint group
table no longer creates an implicit endpoint-target audit, even in the
single-family case.  The group table is used for finite row multiplication;
the endpoint target ledger is separate finite data proving exact family
coverage, braid-index independence, and componentwise product separation.  In
multi-family rows, this explicit ledger prevents one generic group table from
hiding cross-family cancellation.
The residual bridge report likewise separates family coverage from exact
seed-state coverage, so a residual theorem or row proof built for the wrong
routed seeds is visible in the obstruction data.

Symmetric endpoint-family fork certificates are also finite-row-backed.  An
`EndpointFamilySymmetricForkAudit` now requires one endpoint factor row for
each endpoint group order.  Rows record the factor index, group order, whether
the endpoint witness is supplied, and whether the row readout is faithful.
The cutoff proof checks exact factor-row coverage, order agreement, witness
coverage, and row faithfulness; the older `all_endpoint_witnesses_supplied`
and `endpoint_family_faithful` booleans are diagnostic only.
The companion B-side symmetric seed attachment is row-backed as well: it
records endpoint value versus endpoint identity and the residual input/output
tuple claimed to move.  The attachment closes only when that row is
nonidentity, genuinely moved, and equal to the stabilized fibre tuple and
stabilized image in the normalized-law prefix row.  The old
`endpoint_channel_nonidentity` and `endpoint_miss_matches_residual_motion`
flags are diagnostic only.
The normalized-law prefix row itself now derives base fixing, staying over the
base, and source/target residual movement from its recorded source and
stabilized base/fibre/image tuples.  It also requires its finite
base-detector and group-longitude checks to be marked as table-derived.  Thus
a forged prefix with movement booleans but unchanged tuples cannot feed the
B-side seed path.

The residual-faithfulness gate is separate from the endpoint table identities:
even a trivial endpoint group satisfies all label subgroup inclusions
formally, but it closes nothing unless killed endpoint channels force the
actual residual fibre action to be trivial.  This audit therefore records
that bridge explicitly before endpoint witnesses or symmetric cutoffs can be
promoted to an all-strand proof.

When the bridge is supplied by residual action rows, the audit records the
number of covered rows, the expected row count, the exact expected residual
input-tuple domain, and whether the endpoint readout rows prove the complete
residual-action implication.  A supplied-row implication with missing
residual rows is not enough; nor is a duplicate copy of one row that merely
makes the row count match.  Omitting the expected row count or the expected
input-tuple domain does not prove residual faithfulness for this signed
endpoint layer.  Each explicit residual row must also contain at least one
coordinate readout; an empty coordinate bundle is a vacuous row and cannot
prove the supplied-row detector implication.  The row proof must now carry
its own scope audit as well:
active and covered endpoint families, exact expected and covered endpoint
seed states from the current `kappa`, exact row-count agreement with the
explicit rows, and allowed dependency data.  Scope dependencies may use only
interval data, routed seed states, residual input tuples, endpoint channels,
local fibre coordinates, and the local row table; braid-word, braid-prefix,
braid-index, failed-detector, finite-search, normalized-law, and timeout
dependencies are rejected.  The allowed list is not enough by itself: the
scope must explicitly include both `residual_input_tuple` and
`endpoint_channel`, because those are the finite dependencies that connect
killed endpoint data to the actual residual fibre tuple being fixed.  The
audit derives exact endpoint-channel coverage from this scope data and
requires the explicit braid-index-independence certificate to be present.
Every symbolic residual row must also have
`identity_endpoint_output_tuple=input_tuple`.  If the identity endpoint output
moves the tuple, the row is invalid at the row-scope level; a theorem-level
`identity_endpoint_data_forces_residual_identity` flag cannot repair that
row.
Complete finite rows without this scope and all-`n` certificate are only a
fixed-row check, not an all-strand
residual-faithfulness certificate.  A
family-scoped proof that omits the exact seed states is also incomplete,
because product endpoint rows can contain several routed seed channels within
the same family.  These residual family and seed-state ledgers must be
duplicate-free as well; exact coverage cannot rely on silently removing
repeated entries.
The residual action scope seed-state ledgers must also be well formed
endpoint states `(E,s)` with known family and tuple-valued seed state.  A
malformed seed key is an inexact endpoint channel even if the malformed
expected and covered sets agree.  These residual seed ledgers are normalized
with duplicate-safe, hashability-safe markers before comparison, so an
unhashable malformed seed key is reported as finite bad data rather than
escaping as a runtime failure.
The active and covered endpoint-family ledgers for the residual action scope
must also be subsets of `{U,C,M}`; an unknown family label is rejected even if
the active and covered ledgers match.
For multi-family residual products, aggregate row counts are no longer enough:
the residual scope must also list expected and covered residual row counts by
endpoint family, without duplicate family entries, with nonnegative integer
matching counts whose sums equal the total expected and covered residual row
counts.  The total expected and covered residual row counts are also finite
nonnegative integer data; strings, booleans, negative values, and other
non-count objects are malformed residual row-count ledgers rather than
zero-row families.
Each family row-count entry must have exactly two fields, `(family, count)`.
Rows with missing fields, extra fields, or a non-tuple shape are malformed
family-count rows, distinct from rows whose count field is present but not a
nonnegative integer.
Those ledgers must also match the actual residual rows: each row contributes
one count to every endpoint family named by that row, and a family ledger
cannot claim zero rows for a family that any supplied row uses.  This keeps a
complete-looking residual action proof from hiding that one active U/C/M
family has no residual readout rows.  For the older explicit residual-action
scope path, whose rows do not carry row-local family tags, every active family
must have a positive expected and covered residual row count; zero active-family
counts leave the product endpoint row open.

When the bridge is supplied as a symbolic theorem rather than explicit
endpoint readout rows, the theorem now carries its own finite residual row
table.  Each symbolic residual row records the residual input tuple, the
actual output tuple, the output tuple after identity endpoint data, the
endpoint families and routed seed states controlling the row, endpoint channel
keys, and the finite dependencies used by the row.  The checker requires the
row inputs to cover the expected residual input-tuple domain exactly, with no
missing, extra, or duplicate rows.  It rejects rows that mention unrouted
families, unrouted seed states, missing or duplicate endpoint channels,
malformed endpoint-channel keys, endpoint-channel keys whose `(E,s)` pairs do
not equal the row-local routed seed states, row-local family/seed mismatches,
arity-inconsistent
input/output/identity-output tuples, empty residual input tuples, duplicate
row ledgers, or dependencies on `braid_word`,
`braid_prefix`, `braid_index`, failed detector searches, normalized-law
sequences, or timeouts.  Each symbolic row must also explicitly depend on
both `residual_input_tuple` and `endpoint_channel`; a row using only
`interval_data` or routed seed labels is a finite row check, not a bridge from
killed endpoint channels to the actual residual motion.  It derives
endpoint-channel exactness from the union of row families and row seed states,
derives the residual identity implication from
`identity_endpoint_output_tuple=input_tuple` on every row, and derives
braid-index independence from the absence of forbidden or missing required
dependencies.  The same family-by-family residual row-count ledger is required for symbolic
multi-family residual theorems, and those family counts must agree with the
counts obtained by scanning the symbolic residual rows themselves.  The
symbolic theorem's total row counts and family row counts must be finite
nonnegative integers; malformed counts are reported before the theorem can
claim residual faithfulness.  The theorem-level assertions
`endpoint_channels_exact=True` and
`identity_endpoint_data_forces_residual_identity=True` are now required:
if either assertion is absent or false, the residual-faithfulness theorem is
still open even when the supplied rows line up syntactically.  Conversely,
bare booleans for endpoint-channel exactness or identity residual motion are
not accepted as proof; the row/domain ledgers above must support them.  The
braid-index-independence and product-separation flags are likewise required
finite assertions, but they still prove nothing unless the row/domain ledgers
above support them.
The symbolic residual theorem applies the same well-formedness gate to its
expected and covered seed-state ledgers and to the seed states named by each
symbolic residual row.  Malformed row-local seed states make the row invalid;
malformed theorem ledgers make endpoint-channel coverage inexact.  The theorem
uses the same hashability-safe marker comparison for residual seed coverage,
so unhashable malformed row or ledger seeds are rejected as certificate data.
The theorem's active and covered endpoint-family ledgers are checked the same
way: every family must be one of `{U,C,M}`, and row-local endpoint family
labels outside that set make the row invalid.
The residual input-tuple domain and the symbolic residual rows are also
compared by duplicate-safe, hashability-safe markers.  Thus an unhashable but
otherwise exact finite residual input tuple is allowed as explicit interval
data, while missing, extra, or duplicate rows are still detected.  The
family-by-family residual row-count ledgers use the same marker-safe
comparison for count matching, but only known endpoint-family labels can
contribute to an exact family scope; malformed or unhashable family labels
keep the residual-faithfulness theorem open instead of escaping as runtime
failures.  The row-count family labels themselves are now a separate finite
well-formedness obligation: an expected or covered family-count row naming an
unknown or unhashable family is rejected before the theorem can claim residual
faithfulness or residual-action scope.

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
universal_k_row_normal_form_domain
universal_k_seed_classifier_entries
signed_endpoint_generator_required_seed_states
signed_endpoint_generator_duplicate_seed_classifier_entries
signed_endpoint_generator_duplicate_seed_classifier_descriptors
signed_endpoint_generator_conflicting_seed_classifier_descriptors
signed_endpoint_generator_invalid_seed_classifier_targets
signed_endpoint_generator_matches_current_kappa
signed_endpoint_generator_entry_domain_matches_current_interval
signed_endpoint_generator_missing_current_interval_entry_keys
signed_endpoint_generator_extra_current_interval_entry_keys
signed_endpoint_generator_rows_match_current_interval
signed_endpoint_generator_current_coordinate_failures
signed_endpoint_generator_current_inverse_pairing_failures
signed_endpoint_generator_current_inverse_cancellation_failures
signed_endpoint_generator_current_positive_ybe_path_failures
signed_endpoint_generator_current_far_commutativity_path_failures
signed_endpoint_generator_closes_current_kappa
signed_endpoint_generator_closed_families
signed_endpoint_generator_endpoint_observer_build_present
signed_endpoint_generator_endpoint_observer_build_proved
signed_endpoint_generator_endpoint_observer_positive_entry_keys
signed_endpoint_generator_endpoint_observer_monodromy_contexts
signed_endpoint_generator_endpoint_observer_missing_adjacent_paths
endpoint_observer_family_build_present
endpoint_observer_family_build_proved
endpoint_observer_family_build_matches_current_kappa
endpoint_observer_family_build_entry_domain_matches_current_interval
endpoint_observer_family_build_missing_current_interval_entry_keys
endpoint_observer_family_build_extra_current_interval_entry_keys
endpoint_observer_family_build_rows_match_current_interval
endpoint_observer_family_build_current_coordinate_failures
endpoint_observer_family_build_current_inverse_pairing_failures
endpoint_observer_family_build_current_inverse_cancellation_failures
endpoint_observer_family_build_current_positive_ybe_path_failures
endpoint_observer_family_build_current_far_commutativity_path_failures
endpoint_observer_family_build_product_closure_proved
endpoint_observer_family_build_product_residual_faithfulness_required
endpoint_observer_family_build_product_residual_faithfulness_present
endpoint_observer_family_build_product_residual_faithfulness_proved
endpoint_observer_family_build_product_residual_faithfulness_family_scope_matches
endpoint_observer_family_build_product_residual_faithfulness_seed_scope_matches
endpoint_observer_family_build_product_residual_faithfulness_channel_scope_matches
endpoint_observer_family_build_product_residual_faithfulness_channel_key_scope_matches
endpoint_observer_family_build_product_residual_faithfulness_failure_reasons
endpoint_observer_family_build_product_residual_faithfulness_channel_reasons
endpoint_observer_family_build_product_residual_faithfulness_channel_reasons_by_family
endpoint_observer_family_build_product_residual_faithfulness_channel_keys_by_family
endpoint_observer_family_build_closes_current_kappa
endpoint_observer_family_build_closed_families
system_u_closed_by_endpoint_observer_family_build
system_c_closed_by_endpoint_observer_family_build
system_m_closed_by_endpoint_observer_family_build
endpoint_observer_family_build_expected_families
endpoint_observer_family_build_covered_families
endpoint_observer_family_build_missing_families
endpoint_observer_family_build_extra_families
endpoint_observer_family_build_duplicate_families
endpoint_observer_family_seed_classifier_ledger_well_formed
endpoint_observer_family_seed_classifier_malformed_entries
endpoint_observer_family_seed_classifier_duplicate_entries
endpoint_observer_family_seed_classifier_duplicate_descriptors
endpoint_observer_family_seed_classifier_conflicting_descriptors
endpoint_observer_family_seed_classifier_invalid_targets
endpoint_observer_family_certificate_rows
endpoint_observer_family_certificate_malformed_rows
endpoint_observer_family_certificate_unknown_families
endpoint_observer_family_certificate_duplicate_families
endpoint_observer_family_certificate_missing_families
endpoint_observer_family_certificate_extra_families
endpoint_observer_family_detector_track_rows
endpoint_observer_family_detector_track_malformed_rows
endpoint_observer_family_detector_track_invalid_rows
endpoint_observer_family_detector_track_unknown_families
endpoint_observer_family_detector_track_duplicate_keys
endpoint_observer_family_detector_track_missing_families
endpoint_observer_family_detector_track_extra_families
endpoint_observer_family_endpoint_target_rows
endpoint_observer_family_endpoint_target_malformed_rows
endpoint_observer_family_endpoint_target_unknown_families
endpoint_observer_family_endpoint_target_duplicate_families
endpoint_observer_family_endpoint_target_missing_families
endpoint_observer_family_endpoint_target_extra_families
endpoint_observer_family_cutoff_readout_rows
endpoint_observer_family_cutoff_readout_malformed_rows
endpoint_observer_family_cutoff_readout_unknown_families
endpoint_observer_family_cutoff_readout_duplicate_families
endpoint_observer_family_cutoff_readout_missing_families
endpoint_observer_family_cutoff_readout_extra_families
endpoint_observer_family_residual_theorem_rows
endpoint_observer_family_residual_theorem_channel_reasons
endpoint_observer_family_residual_theorem_channel_keys_by_family
endpoint_observer_family_residual_theorem_malformed_rows
endpoint_observer_family_residual_theorem_unknown_families
endpoint_observer_family_residual_theorem_duplicate_families
endpoint_observer_family_residual_theorem_missing_families
endpoint_observer_family_residual_theorem_extra_families
endpoint_observer_family_auxiliary_rows_match_builds
endpoint_observer_family_certificate_rows_match_builds
endpoint_observer_family_certificate_row_mismatches
endpoint_observer_family_detector_track_rows_match_builds
endpoint_observer_family_detector_track_row_mismatches
endpoint_observer_family_endpoint_target_rows_match_builds
endpoint_observer_family_endpoint_target_row_mismatches
endpoint_observer_family_cutoff_readout_rows_match_builds
endpoint_observer_family_cutoff_readout_row_mismatches
endpoint_observer_family_residual_theorem_rows_match_builds
endpoint_observer_family_residual_theorem_row_mismatches
endpoint_observer_monodromy_input_present
endpoint_observer_monodromy_input_rows_exact
endpoint_observer_monodromy_input_seed_classifier_matches_current
endpoint_observer_monodromy_input_seed_classifier_mismatches
endpoint_observer_monodromy_input_rows_match_builds
endpoint_observer_monodromy_input_build_mismatches
endpoint_observer_monodromy_seed_classifier_ledger_well_formed
endpoint_observer_monodromy_seed_classifier_malformed_entries
endpoint_observer_monodromy_seed_classifier_duplicate_entries
endpoint_observer_monodromy_seed_classifier_duplicate_descriptors
endpoint_observer_monodromy_seed_classifier_conflicting_descriptors
endpoint_observer_monodromy_seed_classifier_invalid_targets
endpoint_observer_monodromy_expected_families
endpoint_observer_monodromy_candidate_families
endpoint_observer_monodromy_endpoint_group_families
endpoint_observer_monodromy_endpoint_group_malformed_rows
endpoint_observer_monodromy_template_families
endpoint_observer_monodromy_template_malformed_rows
endpoint_observer_monodromy_derived_reachable_seed_states
endpoint_observer_monodromy_covered_template_seed_states
endpoint_observer_monodromy_missing_template_seed_states
endpoint_observer_monodromy_extra_template_seed_states
endpoint_observer_monodromy_duplicate_template_seed_states
endpoint_observer_monodromy_positive_row_families
endpoint_observer_monodromy_positive_row_malformed_rows
endpoint_observer_monodromy_missing_candidate_families
endpoint_observer_monodromy_expected_positive_entry_keys
endpoint_observer_monodromy_covered_positive_entry_keys
endpoint_observer_monodromy_missing_positive_entry_keys
endpoint_observer_monodromy_extra_positive_entry_keys
endpoint_observer_monodromy_duplicate_positive_entry_keys
endpoint_observer_monodromy_positive_coordinate_failures
endpoint_observer_monodromy_detector_domain_assignment_keys
endpoint_observer_monodromy_detector_domain_malformed_rows
endpoint_observer_monodromy_detector_domain_malformed_keys
endpoint_observer_monodromy_detector_domain_mismatched_keys
endpoint_observer_monodromy_detector_domain_duplicate_keys
endpoint_observer_monodromy_detector_domain_extra_keys
endpoint_observer_monodromy_detector_witness_keys
endpoint_observer_monodromy_detector_witness_malformed_rows
endpoint_observer_monodromy_detector_witness_malformed_keys
endpoint_observer_monodromy_detector_witness_mismatched_keys
endpoint_observer_monodromy_detector_witness_duplicate_keys
endpoint_observer_monodromy_detector_witness_extra_keys
endpoint_observer_monodromy_detector_witness_missing_domain_keys
endpoint_observer_monodromy_detector_witness_without_domain_keys
endpoint_observer_monodromy_detector_domain_entry_key_scope_exact
endpoint_observer_monodromy_detector_domain_assignment_value_failures
endpoint_observer_monodromy_detector_witness_value_failures
endpoint_observer_monodromy_detector_domain_values_well_formed
endpoint_observer_monodromy_failure_reasons
endpoint_observer_family_build_malformed_rows
endpoint_observer_family_build_unknown_families
endpoint_observer_family_build_scope_failures
endpoint_observer_family_build_unproved_families
endpoint_observer_family_build_row_failure_reasons
endpoint_observer_family_build_rows
endpoint_observer_family_build_failure_reasons
signed_endpoint_generator_reachable_seed_states
signed_endpoint_generator_duplicate_reachable_seed_states
signed_endpoint_generator_invalid_reachable_seed_states
signed_endpoint_generator_transition_reachable_seed_states
signed_endpoint_generator_unreachable_declared_seed_states
signed_endpoint_generator_missing_transition_reachable_seed_states
signed_endpoint_generator_reachable_closure_exact
signed_endpoint_generator_missing_initial_seed_states
signed_endpoint_generator_required_signed_seed_keys
signed_endpoint_generator_required_entry_keys
signed_endpoint_generator_entry_domain_derived_from_interval
signed_endpoint_generator_finite_checks_derived_from_tables
signed_endpoint_generator_supplied_entry_keys
signed_endpoint_generator_missing_entry_keys
signed_endpoint_generator_extra_entry_keys
signed_endpoint_generator_supplied_signed_seed_keys
signed_endpoint_generator_missing_signed_seed_keys
signed_endpoint_generator_extra_signed_seed_keys
signed_endpoint_generator_duplicate_entries
signed_endpoint_generator_endpoint_targets_fixed
signed_endpoint_generator_endpoint_targets_flag_supplied
signed_endpoint_generator_endpoint_target_scope_matches_required
signed_endpoint_generator_endpoint_target_expected_families
signed_endpoint_generator_endpoint_target_covered_families
signed_endpoint_generator_endpoint_target_families
signed_endpoint_generator_endpoint_target_group_orders
signed_endpoint_generator_endpoint_target_malformed_group_orders
signed_endpoint_generator_endpoint_target_malformed_group_order_rows
signed_endpoint_generator_endpoint_group_order
signed_endpoint_generator_endpoint_group_order_matches_target
signed_endpoint_generator_endpoint_group_target_families
signed_endpoint_generator_endpoint_group_family_support_verified
signed_endpoint_generator_endpoint_group_family_support_failures
signed_endpoint_generator_endpoint_group_product_factor_failures
signed_endpoint_generator_endpoint_group_product_factors_match_target
signed_endpoint_generator_endpoint_target_cutoff_degrees
signed_endpoint_generator_endpoint_target_malformed_cutoff_degrees
signed_endpoint_generator_endpoint_target_malformed_cutoff_degree_rows
signed_endpoint_generator_endpoint_target_duplicate_families
signed_endpoint_generator_endpoint_target_unknown_families
signed_endpoint_generator_endpoint_target_duplicate_target_families
signed_endpoint_generator_endpoint_target_audit_proved
signed_endpoint_generator_cutoff_endpoint_target_families
signed_endpoint_generator_cutoff_endpoint_value_failures
signed_endpoint_generator_cutoff_endpoint_values_no_extra_channels
signed_endpoint_generator_coordinate_components_verified
signed_endpoint_generator_coordinate_failures
signed_endpoint_generator_inverse_pairing_verified
signed_endpoint_generator_inverse_pairing_failures
signed_endpoint_generator_inverse_cancellation_verified
signed_endpoint_generator_inverse_cancellation_failures
signed_endpoint_generator_positive_ybe_path_verified
signed_endpoint_generator_positive_ybe_path_failures
signed_endpoint_generator_positive_ybe_cocycle_verified
signed_endpoint_generator_positive_ybe_cocycle_failures
signed_endpoint_generator_positive_ybe_label_diagnostics
signed_endpoint_generator_far_commutativity_verified
signed_endpoint_generator_far_commutativity_failures
signed_endpoint_generator_far_commutativity_path_failures
signed_endpoint_generator_far_commutativity_label_diagnostics
signed_endpoint_generator_explicit_monodromy_representation_verified
signed_endpoint_generator_explicit_monodromy_representation_failures
signed_endpoint_generator_positive_monodromy_permutation_failures
signed_endpoint_generator_positive_monodromy_representation_verified
signed_endpoint_generator_two_strand_witness_domain_exact
signed_endpoint_generator_two_strand_witness_domain_failures
signed_endpoint_generator_two_strand_base_verified
signed_endpoint_generator_two_strand_base_failures
signed_endpoint_generator_artin_update_verified
signed_endpoint_generator_artin_update_failures
signed_endpoint_generator_telescoping_detector_verified
signed_endpoint_generator_telescoping_detector_scope_matches_required
signed_endpoint_generator_telescoping_endpoint_group_matches
signed_endpoint_generator_telescoping_signed_row_mismatches
signed_endpoint_generator_telescoping_extra_diagnostic_entry_keys
signed_endpoint_generator_telescoping_expected_entry_keys
signed_endpoint_generator_telescoping_covered_entry_keys
signed_endpoint_generator_telescoping_expected_positive_entry_keys
signed_endpoint_generator_telescoping_covered_positive_entry_keys
signed_endpoint_generator_telescoping_missing_entry_keys
signed_endpoint_generator_telescoping_extra_entry_keys
signed_endpoint_generator_telescoping_duplicate_entry_keys
signed_endpoint_generator_telescoping_duplicate_positive_entry_keys
signed_endpoint_generator_telescoping_malformed_entry_keys
signed_endpoint_generator_telescoping_expected_seed_states
signed_endpoint_generator_telescoping_covered_seed_states
signed_endpoint_generator_telescoping_duplicate_seed_states
signed_endpoint_generator_telescoping_malformed_seed_states
signed_endpoint_generator_detector_track_counts_by_family
signed_endpoint_generator_detector_track_count_malformed_rows
signed_endpoint_generator_detector_track_count_unknown_families
signed_endpoint_generator_detector_track_count_malformed_values
signed_endpoint_generator_detector_track_count_duplicate_families
signed_endpoint_generator_detector_track_count_family_scope_exact
signed_endpoint_generator_detector_track_count_matches_family_sum
signed_endpoint_generator_fixed_detector_track_count
signed_endpoint_generator_detector_track_initialization_rows
signed_endpoint_generator_detector_track_initialization_missing_keys
signed_endpoint_generator_detector_track_initialization_extra_keys
signed_endpoint_generator_detector_track_initialization_duplicate_keys
signed_endpoint_generator_detector_track_initialization_invalid_rows
signed_endpoint_generator_detector_track_initialization_malformed_rows
signed_endpoint_generator_detector_track_initialization_unfixed_rows
signed_endpoint_generator_detector_track_initialization_template_failures
signed_endpoint_generator_detector_track_initialization_rows_exact
signed_endpoint_generator_detector_tracks_fixed_before_braid
signed_endpoint_generator_detector_track_initialization_verified
signed_endpoint_generator_artin_detector_recurrence_verified
signed_endpoint_generator_word_potential_expected_seed_states
signed_endpoint_generator_word_potential_covered_seed_states
signed_endpoint_generator_word_potential_duplicate_seed_states
signed_endpoint_generator_word_potential_malformed_seed_states
signed_endpoint_generator_word_potential_seed_state_scope_matches_expected
signed_endpoint_generator_word_potential_templates_use_only_current_longitudes
signed_endpoint_generator_word_potential_track_scope_verified
signed_endpoint_generator_word_potential_track_scope_failures
signed_endpoint_generator_initialized_raw_assignment_variables
signed_endpoint_generator_word_potential_raw_assignment_scope_verified
signed_endpoint_generator_word_potential_raw_assignment_scope_failures
signed_endpoint_generator_word_potential_artin_substitution_verified
signed_endpoint_generator_word_potential_identity_verified
signed_endpoint_generator_word_potential_detector_domains_sound
signed_endpoint_generator_word_potential_detector_domain_failures
signed_endpoint_generator_word_potential_coboundary_defects_constant
signed_endpoint_generator_word_potential_coboundary_defect_failures
signed_endpoint_generator_word_potential_malformed_identity_rows
signed_endpoint_generator_word_potential_certificate_malformed_identity_row_objects
signed_endpoint_generator_word_potential_certificate_malformed_template_rows
signed_endpoint_generator_word_potential_certificate_malformed_next_seed_states
signed_endpoint_generator_word_potential_certificate_malformed_template_states
signed_endpoint_generator_word_potential_certificate_malformed_normalized_states
signed_endpoint_generator_word_potential_certificate_template_states
signed_endpoint_generator_word_potential_certificate_identity_rows
signed_endpoint_generator_word_potential_certificate_positive_identity_rows
signed_endpoint_generator_word_potential_artin_substitution_failures
signed_endpoint_generator_word_potential_identity_failures
signed_endpoint_generator_terminal_readout_longitudes_verified
signed_endpoint_generator_word_potential_initial_normalized
signed_endpoint_generator_word_potential_initial_seed_states_normalized
signed_endpoint_generator_word_potential_normalized_seed_states
signed_endpoint_generator_word_potential_initial_seed_state_scope_exact
signed_endpoint_generator_word_potential_missing_initial_normalized_seed_states
signed_endpoint_generator_word_potential_extra_initial_normalized_seed_states
signed_endpoint_generator_telescoping_braid_index_independent
signed_endpoint_generator_cutoff_readouts_required
signed_endpoint_generator_cutoff_readouts_exact
signed_endpoint_generator_cutoff_readouts_flag_supplied
signed_endpoint_generator_cutoff_readout_scope_matches_required
signed_endpoint_generator_required_cutoff_families
signed_endpoint_generator_cutoff_target_degrees_match_readout
signed_endpoint_generator_cutoff_target_degree_mismatches
signed_endpoint_generator_cutoff_readout_expected_states
signed_endpoint_generator_cutoff_readout_covered_states
signed_endpoint_generator_cutoff_readout_expected_families
signed_endpoint_generator_cutoff_readout_covered_families
signed_endpoint_generator_cutoff_readout_row_families
signed_endpoint_generator_cutoff_readout_missing_families
signed_endpoint_generator_cutoff_readout_extra_families
signed_endpoint_generator_cutoff_readout_missing_row_families
signed_endpoint_generator_cutoff_readout_extra_row_families
signed_endpoint_generator_cutoff_readout_family_scope_exact
signed_endpoint_generator_cutoff_readout_missing_states
signed_endpoint_generator_cutoff_readout_extra_states
signed_endpoint_generator_cutoff_readout_duplicate_states
signed_endpoint_generator_cutoff_readout_malformed_states
signed_endpoint_generator_cutoff_readout_degree
signed_endpoint_generator_cutoff_readout_rows
signed_endpoint_generator_cutoff_readout_malformed_rows
signed_endpoint_generator_cutoff_readout_malformed_row_states
signed_endpoint_generator_cutoff_readout_invalid_permutation_rows
signed_endpoint_generator_cutoff_readout_duplicate_permutations
signed_endpoint_generator_cutoff_readout_unkilled_rows
signed_endpoint_generator_cutoff_readout_audit_proved
signed_endpoint_generator_residual_faithfulness_verified
signed_endpoint_generator_residual_faithfulness_flag_supplied
signed_endpoint_generator_residual_action_scope_matches_required
signed_endpoint_generator_residual_action_scope_matches_seed_states
signed_endpoint_generator_residual_action_scope_matches_rows
signed_endpoint_generator_residual_action_scope_expected_states
signed_endpoint_generator_residual_action_scope_covered_states
signed_endpoint_generator_residual_action_scope_malformed_row_counts
signed_endpoint_generator_residual_action_scope_duplicate_seed_states
signed_endpoint_generator_residual_action_scope_malformed_seed_states
signed_endpoint_generator_residual_action_scope_unknown_families
signed_endpoint_generator_residual_action_scope_family_rows
signed_endpoint_generator_residual_action_scope_family_rows_covered
signed_endpoint_generator_residual_action_scope_duplicate_family_rows
signed_endpoint_generator_residual_action_scope_malformed_family_rows
signed_endpoint_generator_residual_action_scope_malformed_family_row_count_rows
signed_endpoint_generator_residual_action_scope_family_rows_cover_active
signed_endpoint_generator_residual_action_scope_dependencies
signed_endpoint_generator_residual_action_scope_invalid_dependencies
signed_endpoint_generator_residual_action_scope_missing_required_dependencies
signed_endpoint_generator_residual_action_scope_proved
signed_endpoint_generator_residual_theorem_proved
signed_endpoint_generator_residual_theorem_scope_matches_required
signed_endpoint_generator_residual_theorem_scope_matches_seed_states
signed_endpoint_generator_residual_theorem_expected_states
signed_endpoint_generator_residual_theorem_covered_states
signed_endpoint_generator_residual_theorem_malformed_row_counts
signed_endpoint_generator_residual_theorem_duplicate_seed_states
signed_endpoint_generator_residual_theorem_malformed_seed_states
signed_endpoint_generator_residual_theorem_unknown_families
signed_endpoint_generator_residual_theorem_family_rows
signed_endpoint_generator_residual_theorem_family_rows_covered
signed_endpoint_generator_residual_theorem_duplicate_family_rows
signed_endpoint_generator_residual_theorem_malformed_family_rows
signed_endpoint_generator_residual_theorem_malformed_family_row_count_rows
signed_endpoint_generator_residual_theorem_actual_family_rows
signed_endpoint_generator_residual_theorem_family_rows_match_actual
signed_endpoint_generator_residual_theorem_expected_input_tuples
signed_endpoint_generator_residual_theorem_covered_input_tuples
signed_endpoint_generator_residual_theorem_missing_input_tuples
signed_endpoint_generator_residual_theorem_extra_input_tuples
signed_endpoint_generator_residual_theorem_duplicate_input_tuples
signed_endpoint_generator_residual_theorem_input_tuple_domain_exact
signed_endpoint_generator_residual_theorem_rows
signed_endpoint_generator_residual_theorem_channel_reasons
signed_endpoint_generator_residual_theorem_invalid_rows
signed_endpoint_generator_residual_theorem_malformed_channel_keys
signed_endpoint_generator_residual_theorem_channel_key_seed_mismatches
signed_endpoint_generator_residual_theorem_missing_required_dependencies
signed_endpoint_generator_residual_theorem_rows_cover_input_domain
signed_endpoint_generator_residual_theorem_rows_cover_families
signed_endpoint_generator_residual_theorem_rows_cover_seed_states
signed_endpoint_generator_residual_action_rows
signed_endpoint_generator_residual_action_rows_expected
signed_endpoint_generator_residual_action_expected_input_tuples
signed_endpoint_generator_residual_action_supplied_input_tuples
signed_endpoint_generator_residual_action_missing_input_tuples
signed_endpoint_generator_residual_action_extra_input_tuples
signed_endpoint_generator_residual_action_duplicate_input_tuples
signed_endpoint_generator_residual_action_input_tuple_domain_exact
signed_endpoint_generator_residual_action_complete
signed_endpoint_generator_tables_proved
signed_endpoint_generator_failure_reasons
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
triangular_constant_kernel_duplicate_recovery_route_keys
triangular_latin_defect_duplicate_closure_keys
missing_triangular_row_profiles
missing_triangular_duplicate_profile_keys
missing_triangular_duplicate_section_profile_inputs
missing_triangular_mismatched_section_profile_rows
missing_triangular_inexact_section_profile_rows
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
missing_triangular_coordinate_unit_duplicate_route_rows
missing_triangular_locally_nondegenerate_closed_branch
missing_triangular_partial_constant_closure_rows
missing_triangular_partial_constant_proper_closure_rows
missing_triangular_partial_constant_universal_closure_rows
missing_triangular_partial_constant_duplicate_closure_keys
missing_triangular_partial_constant_continuation_routes
missing_triangular_partial_constant_unrouted_continuation_rows
missing_triangular_partial_constant_duplicate_route_keys
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

That structural exclusion is now closed by a finite cardinality contradiction.  The post-linear
wrapper exposes the finite unsupported row ledger

```text
unsupported_companion_block_image_rows
```

with row keys `(side,left_color,right_color)`.  When no explicit
contradiction audit is supplied, the wrapper derives an
`UnsupportedCompanionStructuralContradictionAudit` whose expected and covered
ledgers match those row keys exactly and whose contradiction row for each key
is the non-circular closed branch

```text
(side,left_color,right_color,
 witness_kind=already_closed_branch,
 closed_branch=finite_triangular_bijection_cardinality_contradiction)
```

The same effective contradiction audit is exported through
`finite_obstruction_data` even when it closes the branch automatically.  Thus
the closed branch still carries the concrete unsupported row keys, the proved
flag, the expected and covered ledgers, the contradiction rows, and the empty
or nonempty contradiction failure list.  A closed unsupported-companion row is
therefore visible as finite proof data rather than disappearing as an
unexplained recorded branch.

The left triangular cardinality proof is:
`T_{a,b}(x,y)=(alpha(x),beta_x(y))`, no same-side constant-map kernel support
forces `alpha` injective, and an injective nonsurjective companion section
forces `|A_b|<|A_d|`; hence `|A_a||A_b|<|A_c||A_d|`, contradicting bijectivity
of `T_{a,b}`.  The right triangular proof is dual, with injective `delta` and
an injective nonsurjective `gamma_y`.  If an explicit contradiction audit is
supplied, it is still checked exactly and an incomplete supplied audit remains
visible as a certificate failure.

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

For unsupported companion block-image rows, that status is treated as closed
by the derived finite triangular bijection cardinality audit above, unless a
caller supplies an explicit contradiction audit, in which case that explicit
audit must prove exact coverage.  Other structural rows remain ordinary
recorded structural closes under the previously supplied branch audits.

Finally, constant-map kernel rows are checked against the triangular recovery
table:

```text
triangular_constant_kernel_unrouted_universal_rows
triangular_constant_kernel_duplicate_recovery_route_keys
```

must both be empty before those constant-map kernel seeds can be routed onward
to System U.

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
match the partial-constant closure row including its closure kind, the
partial-constant closure row itself must be universal, and the route must
reach a universal continuation seed closure.  Its keyed route ledger must also
be duplicate-free, keyed by side, colour pair, fixed input, domain colour,
collapsed inputs, and closure kind.  A nonuniversal partial-constant closure,
a merely nonuniversal continuation-seed containment, or a duplicate route key
leaves the row live in System K and does not create a System C endpoint
obligation.
The downstream identity-routing ledger is also non-vacuous: a forced
universal-continuation route proves only when its lost-edge tuple is exactly
the seed-saturation lost-edge tuple, its routed and unrouted tuples partition
that lost tuple, the lost/routed/unrouted ledgers are all duplicate-free, its
routing labels distinguish exactly the routed edges, and the forced lost-edge
tuple is nonempty.  This prevents set-normalization from hiding duplicated
identity-routing rows before the endpoint observer layer sees them.
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
identity-routed endpoint witnesses, the witness is recorded as a legacy
candidate only.  It no longer closes System C by itself.  The current closure
gate requires the full signed endpoint generator or the family endpoint
observer build, including the word-potential detector lift and residual
faithfulness.

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
universal_continuation_identity_duplicate_lost_edges
universal_continuation_identity_duplicate_routed_edges
universal_continuation_identity_duplicate_unrouted_edges
universal_continuation_identity_routing_proved.
universal_continuation_endpoint_witness_matches_routing
universal_continuation_endpoint_witness_proved
universal_continuation_endpoint_missing_edges
universal_continuation_endpoint_extra_edges
universal_continuation_endpoint_duplicate_routed_edges
universal_continuation_endpoint_duplicate_witness_edges
universal_continuation_symmetric_fork_matches_routing
universal_continuation_symmetric_fork_group_orders
universal_continuation_symmetric_fork_minimum_degree
universal_continuation_symmetric_fork_degree
universal_continuation_symmetric_fork_cutoff_proved
universal_continuation_symmetric_fork_tail_seed_prefix_proved
universal_continuation_symmetric_fork_missing_edges
universal_continuation_symmetric_fork_extra_edges
universal_continuation_symmetric_fork_duplicate_routed_edges
universal_continuation_symmetric_fork_duplicate_covered_edges
```

The remaining A-route is to construct the routed C word-potential endpoint
observer, or an exact cutoff readout, together with residual faithfulness for
those routed universal-continuation seed closures.  The B-route would have to
upgrade one such endpoint miss to the normalized-law sequence required in the
original problem.

[Legacy diagnostic] If the supplied `universal_continuation_endpoint_witness`
matches the same identity-routing ledger and proves all routed endpoint
witnesses, the executable data records
`universal_continuation_endpoint_witness_proved=True` and exact missing,
extra, and duplicate edge ledgers.  Duplicate identity-routed edges or
duplicate witness edges are certificate failures.  This does not empty
`remaining_obligations`; the current system
name remains `system_c_universal_continuation_endpoint` unless the signed
endpoint observer route also closes.

[Legacy diagnostic] If the supplied
`universal_continuation_symmetric_endpoint_fork` matches the same
identity-routing ledger, covers exactly the identity-routed lost edges, and
proves a faithful symmetric endpoint cutoff for the fixed continuation
endpoint family, and has no duplicate routed or covered edge entries, the
cutoff ledger is recorded as a candidate.  It does not
remove C from `unclosed_routed_endpoint_systems` without the current endpoint
observer/cutoff readout and residual-faithfulness bridge.

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
missing_triangular_coordinate_unit_duplicate_route_rows
missing_triangular_coordinate_unit_routing_proved
mixed_unit_endpoint_witness_matches_routing
mixed_unit_endpoint_witness_proved
mixed_unit_endpoint_missing_context_keys
mixed_unit_endpoint_extra_context_keys
mixed_unit_endpoint_duplicate_context_keys
mixed_unit_endpoint_duplicate_witness_keys
mixed_unit_symmetric_fork_matches_routing
mixed_unit_symmetric_fork_group_orders
mixed_unit_symmetric_fork_minimum_degree
mixed_unit_symmetric_fork_degree
mixed_unit_symmetric_fork_cutoff_proved
mixed_unit_symmetric_fork_tail_seed_prefix_proved
mixed_unit_symmetric_fork_missing_context_keys
mixed_unit_symmetric_fork_extra_context_keys
mixed_unit_symmetric_fork_duplicate_context_keys
mixed_unit_symmetric_fork_duplicate_covered_keys
```

[Legacy diagnostic] If the supplied `mixed_unit_context_endpoint_witness`
matches the same coordinate-unit routing ledger and proves all mixed context
endpoint witnesses, the wrapper records the witness coverage and missing,
extra, and duplicate context-key ledgers.  Duplicate routed context keys or
duplicate witness keys are certificate failures.  It does not close System M
by itself; the current closure
gate requires the routed M word-potential endpoint observer or exact cutoff
readout with residual faithfulness.

[Legacy diagnostic] If the supplied `mixed_unit_context_symmetric_endpoint_fork` matches
the same coordinate-unit routing ledger, covers exactly the mixed context
keys, and proves a faithful symmetric endpoint cutoff for the fixed mixed-unit
endpoint family, with no duplicate context or covered keys, it is retained as
a candidate cutoff ledger.  It does not
remove M from `unclosed_routed_endpoint_systems` without the current endpoint
observer/cutoff readout and residual-faithfulness bridge.

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
triangular_recovery_endpoint_duplicate_routed_keys
triangular_recovery_endpoint_duplicate_witness_keys
triangular_recovery_symmetric_fork_matches_system
triangular_recovery_symmetric_fork_group_orders
triangular_recovery_symmetric_fork_minimum_degree
triangular_recovery_symmetric_fork_degree
triangular_recovery_symmetric_fork_cutoff_proved
triangular_recovery_symmetric_fork_tail_seed_prefix_proved
triangular_recovery_symmetric_fork_missing_keys
triangular_recovery_symmetric_fork_extra_keys
triangular_recovery_symmetric_fork_duplicate_routed_keys
triangular_recovery_symmetric_fork_duplicate_covered_keys
```

The endpoint keys are exactly:

```text
(left_color, right_color, routed_defect_reason).
```

[Legacy diagnostic] If the supplied `triangular_recovery_endpoint_witness` uses
the same fixed `U_tri` observer, covers exactly the current
`system_u_endpoint_defects`, and each covered key carries a recovery endpoint
certificate proving membership in `V_beta(U_tri)`, then the wrapper records
`triangular_recovery_endpoint_witness_proved=True` and exact missing, extra,
and duplicate key ledgers.  Duplicate routed keys or duplicate witness keys
are certificate failures, not harmless repetitions hidden by set
normalization.  It does not close System U by itself.  The current closure gate
requires the routed U word-potential endpoint observer over `U_tri`, or the
full signed endpoint generator, with residual faithfulness.

[Legacy diagnostic] If the supplied `triangular_recovery_symmetric_endpoint_fork` uses
the same fixed `U_tri` observer, its endpoint-family group list is exactly
`(|U_tri|,)`, it covers exactly the current `system_u_endpoint_defects`, and
it proves a faithful symmetric endpoint cutoff, then the cutoff is retained as
a candidate ledger.  Duplicate routed keys or duplicate covered keys are
reported and keep the fork unproved.  It does not remove U from
`unclosed_routed_endpoint_systems` without the current endpoint-observer and
residual-faithfulness bridge.

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
