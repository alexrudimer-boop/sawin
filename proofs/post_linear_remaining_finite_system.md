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
The congruence-chain helper now treats endpoint-observer closure verdicts as
closed local summaries only when they carry the actual fixed detector product
group; otherwise the row remains a local gap rather than being assembled into
the final rack.

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
listed side is nonunit or whose explanation does not match remains live in
System K.  The coordinate-unit routing ledger is non-vacuous: an empty row
tuple does not prove the route.

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
product-family separation.  Missing families, extra families, nonpositive
orders, nonpositive cutoff degrees, `n`-dependence, or cross-family
cancellation leave the signed endpoint layer open.  The family and target
ledgers must also be duplicate-free: repeating a routed family or assigning
two target entries to the same family is not an exact one-target-per-family
certificate.
The implementation now derives endpoint-target braid-index independence and
product-family separation from the finite target ledger itself: each covered
family must have a positive fixed group order or cutoff degree, and target
families must match covered routed families without duplicates.  The legacy
independence/separation flags are diagnostic only.
For C/M cutoff families, the target cutoff degree must also match the
cutoff-readout audit's symmetric degree.  A target ledger declaring an `S_m`
cutoff and a readout audit over `S_k` with `k != m` is reported as
`cutoff_readout_target_degree_mismatch`; the readout may be faithful for its
own degree, but it does not certify the declared target.

The C/M cutoff gate is now scoped like the residual-faithfulness gate.  A bare
`cutoff_readouts_exact` flag is recorded only as supplied data; it does not
prove the gate.  The cutoff certificate must list the expected routed C/M seed
states, the covered seed states, a positive symmetric degree, and one finite
readout row for every routed C/M seed state.  A row records the seed state,
the readout permutation, and the permutation left after identity cutoff data.
The checker verifies row-domain exactness, actual membership in the symmetric
group, injective readouts for faithfulness, and identity killed-readouts for
channel killing.  The expected and covered cutoff seed-state ledgers must be
duplicate-free; repeated seed entries are reported as an inexact readout
ledger rather than silently collapsed.  Expected, covered, and row cutoff
state keys must also be well formed endpoint states; malformed keys are
reported even if the malformed sets agree.  Cutoff braid-index independence
is derived from the positive fixed degree and exact finite readout rows, so the
legacy `braid_index_independent` flag on this audit is diagnostic only.

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
open.

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
`0 <= r < R_E` and requires one finite initialization row for each key.  A
row records the family, track index, assignment-rule name, the finite
dependencies of the rule, and the local assignment template for the raw
variables.  Allowed dependencies are interval and initial-state data:
`interval_data`, `endpoint_family`, `routed_seed_state`,
`initial_colour_tuple`, `initial_fibre_tuple`, `strand_index`,
`strand_colour`, `local_input`, and `local_output`.  Braid-word,
braid-prefix, braid-index, failed-detector, finite-search, normalized-law, or
timeout dependencies make the row invalid.  The checker reports missing,
extra, duplicate, and invalid initialization rows before the detector-lift
gate can close.
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
contain only current longitude variables `U_{r,j}`, and that the local
substitutions are the positive Artin recurrences.  Negative
word-potential rows, if present, are diagnostic only once the signed endpoint
audit has proved that negative endpoint rows are actual inverses.  Malformed
identity rows with any sign other than `+1` or `-1` are rejected rather than
being treated as harmless diagnostics.  The expected and covered telescoping
entry ledgers are positive-only for closure, but they also reject malformed
signs instead of filtering them away.  The same well-formedness gate checks
that every identity-row and ledger key has the full `D_Gamma` shape
`(E,epsilon,s,a,b,x,y)`, a known endpoint family, and a tuple-valued reachable
state; a shortened positive key is malformed rather than an abbreviated row.
Malformed rows are reported at that gate before downstream template,
track-scope, raw-assignment, or identity diagnostics interpret row fields.
Optional negative diagnostics are also scoped to the current signed
`D_Gamma` domain: a negative identity row or telescoping ledger key outside
the interval-derived signed entry domain is an extra diagnostic channel, not a
harmless ignored row.
The checker then exhausts all
assignments of the finitely many variables in the positive row to the fixed
endpoint group, or to a certified sound detector-domain subset, and checks
that the coboundary defect is constant with value equal to the row label.
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

The implementation now exposes an interval-derived constructor for this
audit layer.  Given the interval, `kappa` entries, reachable states, signed
rows, a fixed endpoint group, literal row diagnostics, and a fixed-assignment
telescoping detector audit, it computes the full `D_Gamma` domain from the
fibres and fills the coordinate, inverse, YBE, and fixed-track telescoping
gates by running the finite checkers.  This
keeps the local certificate from being a list of unsupported boolean claims.
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
audit proves the fixed endpoint target obligation.  The convenience target
audit built from a supplied endpoint group is now limited to the single-family
case.  When more than one of U/C/M is routed, an explicit endpoint target
audit is required to prove componentwise product separation; one generic
group table is not enough to certify that no cross-family cancellation is
being used.
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
dependencies are rejected.  The audit derives exact endpoint-channel coverage
and braid-index independence from this scope data, instead of accepting
separate booleans.  Complete finite rows without this scope are only a
fixed-row check, not an all-strand residual-faithfulness certificate.  A
family-scoped proof that omits the exact seed states is also incomplete,
because product endpoint rows can contain several routed seed channels within
the same family.  These residual family and seed-state ledgers must be
duplicate-free as well; exact coverage cannot rely on silently removing
repeated entries.
The residual action scope seed-state ledgers must also be well formed
endpoint states `(E,s)` with known family and tuple-valued seed state.  A
malformed seed key is an inexact endpoint channel even if the malformed
expected and covered sets agree.
For multi-family residual products, aggregate row counts are no longer enough:
the residual scope must also list expected and covered residual row counts by
endpoint family, without duplicate family entries, with nonnegative matching
counts whose sums equal the total expected and covered residual row counts.
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
row-local family/seed mismatches, arity-inconsistent
input/output/identity-output tuples, empty residual input tuples, duplicate
row ledgers, or dependencies on `braid_word`,
`braid_prefix`, `braid_index`, failed detector searches, normalized-law
sequences, or timeouts.  It derives endpoint-channel exactness from the union
of row families and row seed states, derives the residual identity implication
from `identity_endpoint_output_tuple=input_tuple` on every row, and derives
braid-index independence from the absence of forbidden dependencies.  The
same family-by-family residual row-count ledger is required for symbolic
multi-family residual theorems, and those family counts must agree with the
counts obtained by scanning the symbolic residual rows themselves.  Bare
booleans for endpoint-channel
exactness, identity residual motion, braid-index independence, or product
separation are recorded only as supplied data; they are not accepted as proof.
The symbolic residual theorem applies the same well-formedness gate to its
expected and covered seed-state ledgers and to the seed states named by each
symbolic residual row.  Malformed row-local seed states make the row invalid;
malformed theorem ledgers make endpoint-channel coverage inexact.

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
signed_endpoint_generator_endpoint_group_order
signed_endpoint_generator_endpoint_group_order_matches_target
signed_endpoint_generator_endpoint_target_cutoff_degrees
signed_endpoint_generator_endpoint_target_duplicate_families
signed_endpoint_generator_endpoint_target_duplicate_target_families
signed_endpoint_generator_endpoint_target_audit_proved
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
signed_endpoint_generator_detector_track_count_duplicate_families
signed_endpoint_generator_detector_track_count_family_scope_exact
signed_endpoint_generator_detector_track_count_matches_family_sum
signed_endpoint_generator_fixed_detector_track_count
signed_endpoint_generator_detector_track_initialization_rows
signed_endpoint_generator_detector_track_initialization_missing_keys
signed_endpoint_generator_detector_track_initialization_extra_keys
signed_endpoint_generator_detector_track_initialization_duplicate_keys
signed_endpoint_generator_detector_track_initialization_invalid_rows
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
signed_endpoint_generator_cutoff_readout_missing_states
signed_endpoint_generator_cutoff_readout_extra_states
signed_endpoint_generator_cutoff_readout_duplicate_states
signed_endpoint_generator_cutoff_readout_malformed_states
signed_endpoint_generator_cutoff_readout_degree
signed_endpoint_generator_cutoff_readout_rows
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
signed_endpoint_generator_residual_action_scope_duplicate_seed_states
signed_endpoint_generator_residual_action_scope_malformed_seed_states
signed_endpoint_generator_residual_action_scope_family_rows
signed_endpoint_generator_residual_action_scope_family_rows_covered
signed_endpoint_generator_residual_action_scope_duplicate_family_rows
signed_endpoint_generator_residual_action_scope_family_rows_cover_active
signed_endpoint_generator_residual_action_scope_dependencies
signed_endpoint_generator_residual_action_scope_invalid_dependencies
signed_endpoint_generator_residual_action_scope_proved
signed_endpoint_generator_residual_theorem_proved
signed_endpoint_generator_residual_theorem_scope_matches_required
signed_endpoint_generator_residual_theorem_scope_matches_seed_states
signed_endpoint_generator_residual_theorem_expected_states
signed_endpoint_generator_residual_theorem_covered_states
signed_endpoint_generator_residual_theorem_duplicate_seed_states
signed_endpoint_generator_residual_theorem_malformed_seed_states
signed_endpoint_generator_residual_theorem_family_rows
signed_endpoint_generator_residual_theorem_family_rows_covered
signed_endpoint_generator_residual_theorem_duplicate_family_rows
signed_endpoint_generator_residual_theorem_actual_family_rows
signed_endpoint_generator_residual_theorem_family_rows_match_actual
signed_endpoint_generator_residual_theorem_expected_input_tuples
signed_endpoint_generator_residual_theorem_covered_input_tuples
signed_endpoint_generator_residual_theorem_missing_input_tuples
signed_endpoint_generator_residual_theorem_extra_input_tuples
signed_endpoint_generator_residual_theorem_duplicate_input_tuples
signed_endpoint_generator_residual_theorem_input_tuple_domain_exact
signed_endpoint_generator_residual_theorem_rows
signed_endpoint_generator_residual_theorem_invalid_rows
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

That structural exclusion is now also certificate-gated.  The post-linear
wrapper exposes the finite unsupported row ledger

```text
unsupported_companion_block_image_rows
```

with row keys `(side,left_color,right_color)`.  A complete close of this
upstream branch requires an `UnsupportedCompanionStructuralContradictionAudit`
whose expected and covered ledgers match those row keys exactly, with no
missing, extra, or duplicate rows.  It must also supply at least one finite
contradiction row for every expected row.  Each contradiction row is either a
coordinate-level coloured-YBE mismatch

```text
(side,left_color,right_color,
 witness_kind=colored_ybe_coordinate_contradiction,
 ybe_triple=(a,b,c),
 coordinate in {left,right,pair,fibre,state},
 left_value != right_value)
```

or a pointer to a non-circular previously closed branch

```text
(side,left_color,right_color,
 witness_kind=already_closed_branch,
 closed_branch)
```

where `closed_branch` cannot be `triangular_structural_inconsistency` itself.
If this finite table is absent or incomplete, the wrapper reports
`unsupported_companion_structural_contradiction_obligation`; the row remains
excluded from `K_nabla`, but the proof has not justified the exclusion.

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
only after the finite structural-contradiction audit above proves exact
coverage.  Other structural rows remain ordinary recorded structural closes
under the previously supplied branch audits.

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
match the partial-constant closure row including its closure kind, the
partial-constant closure row itself must be universal, and the route must
reach a universal continuation seed closure.  A nonuniversal
partial-constant closure or a merely nonuniversal continuation-seed
containment leaves the row live in System K and does not create a System C
endpoint obligation.
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
