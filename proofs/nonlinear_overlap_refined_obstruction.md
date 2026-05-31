# Nonlinear overlap refined obstruction

Date: 2026-05-31

This note refines `proofs/nonlinear_overlap_reduction_after_linear_closure.md`.
It does not prove `[Resolution: A]` and it does not construct `[Resolution: B]`.
Its purpose is to make the post-linear nonlinear survivor exact enough that
the next theorem has no hidden row-level alternatives.

## Standing branch

Work after the finite-linear no-go theorem and the closed branch routers.  A
candidate nonlinear survivor must first pass the audit status

```text
exact_remaining_nonlinear_obstruction
```

from

```text
nonlinear_overlap_obstruction_audit(interval)
```

Equivalently, the interval is a coloured YBE, semisplit-free, local-minimal
`bi_free_universal_corridor_bottleneck` row; the base rows are in left-rack
form; and at least one continuation seed has universal admissible closure.

The refinement helper

```text
nonlinear_overlap_refinement_audit(interval)
```

then applies the two-sided-unit, rank-profile, triangular-bundle,
triangular-recovery, triangular-column, Latin-triangular, and rack-kink audits
to that exact survivor.

The last open status after the unit-observer refinement is:

```text
triangular_recovery_unit_longitude_obstruction
```

## Unit split

[Proved] A strand-continuing survivor is closed by finite transport-state
rackification.

This is the status

```text
closed_by_transport_state_rackification
```

and uses the already recorded transport-state rack theorem.

[Proved] A two-sided-unit survivor is not in the nonlinear bottleneck; it is
locally nondegenerate and routes to the closed nondegenerate/guitar branch.

This is the status

```text
closed_by_locally_nondegenerate_branch
```

The remaining moving row must therefore be one-sided or mixed-unit.

## Rank-profile split

[Proved] A proper nontrivial coordinate-section kernel is visible to the
existing Green/Schutzenberger kernel-block readouts under the standing
constant-observer branch hypotheses.  Such a row is not the hidden nonlinear
overlap survivor.

This is the status

```text
section_kernel_visible_to_existing_readouts
```

[Proved] After proper section kernels and injective non-surjective rows are
removed, every hidden rank-losing section is constant.  Thus the remaining
hidden rank-loss has constant-section triangular form, for example

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), beta_{a,b,x}(y))
```

or the side-dual form.

This is the status

```text
constant_section_triangular_obstruction
```

unless the triangular recovery data is already verified.

## Triangular split

[Proved] A bijective constant-section triangular row has bundle-partition
structure: for each constant output value, the companion images indexed by
the fibre of the constant map partition the companion codomain.

[Proved] The inverse is exactly the triangular recovery map: first recover the
bundle block label, then invert the corresponding companion section.

These two row-level facts first isolate

```text
triangular_endpoint_recovery_obstruction
```

when the row is not closed by a simpler triangular subcase.

[Proved] Such recovery maps are fixed finite unit labels after passing to the
tagged state universe.  The helper

```text
triangular_recovery_unit_observer_audit(interval)
```

extends every recovery-row partial bijection to a permutation of one fixed
finite universe and generates the finite group `U_tri`.  The fixed-word helper

```text
triangular_recovery_longitude_route_audit(interval,n,beta,row_indices)
```

then checks the exact endpoint criterion:

```text
endpoint composite in V_beta(U_tri).
```

This bridge is recorded in
`proofs/triangular_recovery_unit_observer.md`.

The all-`n` route through that finite group is reduced further in
`proofs/triangular_recovery_detector_lift_fork.md`: verify active Artin
detector-lift rows in `U_tri`, or expose the exact row whose failure must be
upgraded to normalized-law B.

[Proved] Before the `U_tri` endpoint route may be treated as the only
remaining triangular issue, the audit must also check whether the
rack-kink all-pairs Latin hypotheses have actually been reached.  The status

```text
triangular_recovery_kink_completion_deficit
```

records the missing bridge.  Its deficit list is

```text
rack_kink_completion_deficits
```

with entries such as `latin_rows_not_present_for_all_pairs` or
`latin_ybe_equations_not_verified`.

This split is recorded in
`proofs/triangular_recovery_kink_completion_deficit.md`.

[Proved] If all triangular rows collapse to product form, the row is routed to
the already closed product/permutation holonomy branch.

This is the status

```text
closed_by_product_triangular_collapse
```

[Proved] In the rack-base all-pairs Latin-unit triangular case, the
kink-predecessor cancellation theorem forces every Latin fibre to be
singleton.  Hence that all-pairs Latin-unit row cannot be a nontrivial
local-minimal bottleneck.

This is the status

```text
latin_triangular_kink_impossible
```

## Final refined obstruction

[Open] After these refinements, the remaining nonlinear survivor is not a raw
middle-carrier overlap, not a finite-linear chief-factor obstruction, not a
strand-continuing row, not a two-sided-unit row, not a proper section-kernel
row, not a product triangular row, and not the rack-base all-pairs Latin-unit
case.

The exact remaining obstruction is:

```text
a local-minimal bi-free universal-corridor interval whose residual motion is a
triangular recovery endpoint composite, where either the corridor has not yet
been completed to the rack-kink all-pairs Latin hypotheses, or the fixed
finite group U_tri endpoint composite is not yet proved to lie in
V_beta(U_tri) and has not been upgraded to a normalized-law sequence.
```

To prove A, one must first close or route the kink-completion deficits, and
then prove fixed unit-longitude visibility for any surviving triangular
recovery endpoint composites, uniformly in braid index.  To prove B, one must
construct such an interval and upgrade either a completion-deficit endpoint or
one recovery endpoint in `U_tri` to a normalized-law sequence invisible to
every finite group while moving a residual tuple.

This is the same repair-contract fork as before, but with all row-level
alternatives exposed by executable statuses rather than implicit prose.
