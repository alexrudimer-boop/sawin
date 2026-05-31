# Post-linear completion audit

Date: 2026-05-31

This audit records the current state after the finite-linear overlap
obstruction was closed.  It is meant to prevent two opposite mistakes:

1. treating the solved finite-linear algebraic system as a full resolution of
   Sawin finite-rack domination; or
2. reopening finite-linear overlap as a possible remaining obstruction.

## Requirements from the overlap prompt

The prompt asked for one of the following final outcomes:

```text
1. prove finite-linear overlap cannot exist;
2. prove finite-linear overlap is always A-controlled;
3. construct a finite-linear B example;
4. prove nonlinear overlap cannot exist;
5. construct a nonlinear primitive overlap B example.
```

It also asked, if the whole problem cannot be closed, to solve one exact
finite algebraic system or prove an equivalent remaining finite system.

## Completed items

[Proved] The finite-linear overlap obstruction cannot exist.

Evidence:

```text
proofs/finite_linear_overlap_resolution.md
```

The proof derives, from the seven block YBE equations alone,

```text
AS = SA = DS = SD = 0,
BS = SB,
CS = SC.
```

Thus `im S` is invariant.  Irreducibility and `S != 0` force `im S=V`, hence
`A=D=0`; invertibility of the anti-diagonal block matrix then forces `B,C`
invertible, contradicting the singularity hypotheses.

[Proved] The semisimple and higher-nilpotent finite-linear systems in the
prompt are both closed by the same argument.

Evidence:

```text
proofs/overlap_resolution_verdict.md
```

[Proved] The finite-linear branch is A-controlled vacuously: no primitive
finite-linear overlap datum survives to the braid-survival test.

## Narrowed nonlinear branch

[Proved] After the closed branches and finite-linear no-go theorem, any
remaining nonlinear survivor must be a local-minimal
`bi_free_universal_corridor_bottleneck` interval with universal continuation
and terminal endpoint/gauge data not yet controlled by a fixed finite group.

Evidence:

```text
proofs/nonlinear_overlap_reduction_after_linear_closure.md
proofs/nonlinear_overlap_refined_obstruction.md
proofs/triangular_recovery_unit_observer.md
proofs/triangular_recovery_detector_lift_fork.md
proofs/triangular_recovery_longitude_expression_certificate.md
proofs/triangular_recovery_derived_series_fork.md
proofs/triangular_recovery_kink_completion_deficit.md
proofs/triangular_recovery_side_dual_completion.md
proofs/right_rack_kink_latin_triangular_cancellation.md
proofs/triangular_latin_ybe_projection_consistency.md
proofs/triangular_k_left_defect_ledger.md
proofs/triangular_k_left_kernel_closure.md
proofs/triangular_k_left_structural_independence.md
proofs/triangular_k_left_recovery_routing.md
proofs/triangular_k_left_missing_row_profile.md
proofs/triangular_k_left_rack_cardinality_closure.md
proofs/triangular_k_left_coordinate_unit_routing.md
proofs/triangular_k_left_partial_constant_closure.md
proofs/triangular_k_left_partial_constant_continuation_route.md
proofs/triangular_k_left_side_dual_replacement_ledger.md
proofs/universal_continuation_identity_routing.md
proofs/universal_continuation_identity_endpoint_witness.md
proofs/post_linear_remaining_finite_system.md
proofs/continuation_congruence_descent_gate.md
proofs/elementary_continuation_closure.md
proofs/universal_continuation_derivation_certificate.md
proofs/descent_endpoint_repair_contract.md
```

This means the remaining nonlinear problem is no longer an arbitrary
middle-carrier overlap phrase.  It is the following exact local detector
problem:

```text
For every local-minimal bi_free_universal_corridor_bottleneck interval over a
rack-dominated quotient, construct one finite group G(pi,Q), independent of
braid index n, such that identity recursive G-longitude data kills the
residual action.
```

The code-level wrapper for this shape is:

```text
src/ybe_domination/nonlinear_overlap.py
nonlinear_overlap_obstruction_audit(interval)
```

The wrapper distinguishes the exact remaining obstruction from three exits:
not reaching the corridor target at all, closing by strand-continuing
transport-state rackification, or closing by a supplied descent-endpoint
repair contract.  A supplied normalized-law prefix is recorded separately as
one B-shaped row, not as `[Resolution: B]`.

The refinement wrapper narrows the row-level survivor further.  Its final
nominal unit-endpoint status is:

```text
triangular_recovery_unit_longitude_obstruction
```

but the direct occurrence of this status is now preempted by the kink
dichotomy.  The executable predicate
`direct_unit_longitude_status_preempted_by_kink_dichotomy` records that, once
the triangular recovery unit observer is ready and the rack-kink completion
deficit list is empty, the refinement must already close as
`latin_triangular_kink_contradiction` or `latin_triangular_kink_impossible`.
Thus `U_tri` remains as the endpoint layer reached after a K deficit has been
routed, not as a separate direct survivor.  The refinement inserts the earlier
status,

```text
triangular_recovery_kink_completion_deficit
```

when the triangular recovery row has not yet been proved to satisfy the
rack-kink all-pairs Latin hypotheses.  Once that completion deficit is closed
or routed to a fixed detector, the current A-route is to prove active Artin
detector-lift rows in `U_tri`, direct endpoint-longitude expression
certificates, or derived-series quotient lifts plus one stable
perfect-residual `P_tri` witness, which would give endpoint-longitude
expressions uniformly in braid index.  If the completion deficit is not yet
routed, the exact K-left row ledger is `missing_left_latin_row_defects`:
no triangular row, a constant-map kernel/codomain defect, a companion-section
kernel/rank defect, hidden nonunit opposite column, or missing/non-Latin
side-dual replacement.
Impossible triangular-row structural defects are now closed explicitly as
`triangular_structural_inconsistency`.
The raw `base_not_finite_rack` deficit is now closed as
`rack_base_consistency_inconsistent` in target-ready data.
Kink-cancellation and side-dual diagonal-cancellation failures under the full
Latin theorem hypotheses are now recorded as closed inconsistency states:
`latin_triangular_kink_cancellation_inconsistent` and
`side_dual_latin_triangular_diagonal_cancellation_inconsistent`.
The K wrapper now exposes `live_kink_completion_deficits`; after these
preemptions the only direct live deficit is
`latin_rows_not_present_for_all_pairs`.  The side-dual all-pairs marker is a
modifier on that missing-row state, not a separate endpoint branch.
The wrapper also exposes `live_k_missing_latin_row_defects`; raw K rows with
that tuple empty are now classified as `closed_by_recorded_k_deficit_routing`
rather than active System K.
Side-dual non-Latin and no-replacement labels remain in
`k_left_side_dual_replacement_rows`, but they are pointers to opposite-side
row ledgers rather than members of the live K tuple.
Raw no-triangular-row labels are now filtered by the supplied
`missing_triangular_row_profile_audit` and its route ledgers: proper-kernel,
coordinate-unit, partial-constant, and cardinality/profile-closed subcases are
removed from the live tuple when their certificates are present.
Constant-map kernel labels are now filtered by the supplied
`triangular_latin_defect_closure_audit` plus
`triangular_constant_kernel_recovery_route_audit`: proper closures contradict
local minimality, while universal closures must be separated by the triangular
recovery table before the constant-map reason is removed.
That same triangular recovery separation removes the companion
injective-nonsurjective block-image reason for the side/pair, while companion
proper-kernel and constant reasons stay with the structural/kernel ledger.
For the kernel subcases, `triangular_latin_defect_closure_audit` now proves
that proper generated closures are incompatible with local minimality and
records the universal generated seed edges that still require detector
routing.
For the structural subcases, the triangular row itself proves constant-map
surjectivity, companion-section injectivity, companion nonsurjectivity only
through constant-map fibres, and hidden opposite nonunits only through product
collapse.
For constant-map kernel subcases, the triangular recovery table separates the
collapsed constant-map inputs, so the remaining burden is the System U
`V_beta(U_tri)` endpoint theorem.
For no-triangular-row subcases, the missing-row profile audit now separates
proper-kernel, injective-nonsurjective, coordinate-unit, partial-constant,
and nonconstant-hidden profiles; the partial-constant rows are exactly
mixed-unit context-recovery rows on that coordinate side, while coordinate-unit
rows are two-sided-unit branch rows when global and otherwise mixed-unit
context with the nonunit data on the opposite side.  The constant sections in
partial-constant rows now produce explicit generated seed-edge closures:
proper closure contradicts local minimality, and universal closure is the
exact seed edge.  Companion separation then routes those seed edges into
nontrivial continuation seed closures, so they are part of the
descent-endpoint repair channel rather than a separate K-left endpoint system.
For the universal-continuation channel itself, identity external routing now
lists every saturation-lost fibre edge whose fixed endpoint witness is still
required.
For side-dual replacement subcases, `k_left_side_dual_replacement_rows`
records the right-side defect ledger or missing-row profile explicitly.
If the U-route fails after K is routed, the finite miss has been localized to
`P_tri`, where it must be upgraded to a normalized-law sequence before it can
serve as `[Resolution: B]`.

Equivalently, in the repair-contract format, construct:

```text
1. a fixed descent-separating readout;
2. fixed endpoint groups;
3. a faithful reconstruction rule;
4. all-n V_beta witnesses for every endpoint channel.
```

## Conditional route to A

[Conditional] If the uniform descent-endpoint theorem holds for every
local-minimal bottleneck interval, then the positive finite-rack domination
theorem follows.

Evidence:

```text
proofs/descent_endpoint_repair_contract.md
proofs/global_local_normalized_fork.md
proofs/master_local_dichotomy.md
proofs/sharp_obstruction_theorem.md
proofs/congruence_chain_mechanics.md
```

The proof-critic gap remains precisely the construction of the readout,
endpoint witnesses, and faithful decomposition in the nonlinear bottleneck.
The triangular and mixed-unit reductions are useful, but they do not by
themselves prove that every residual endpoint component has a fixed
`V_beta` witness.

## Conditional route to B

[Conditional] If one explicit finite local-minimal bottleneck interval is
proved to have no finite group detector, then a normalized-law counterexample
sequence follows by the local normalized-law fork.

Evidence:

```text
proofs/global_local_normalized_fork.md
proofs/normalized_law_domination_dichotomy.md
proofs/symmetric_tower_counterexample_certificate.md
```

However, no such explicit interval and no all-prefix normalized-law sequence
is currently constructed.

## Finite diagnostic evidence

[Proved as finite audit, not theorem evidence] The existing exhaustive
size-2/3 local-minimal cover corpus has no interval reaching the narrowed
`bi_free_universal_corridor_bottleneck` target.

Evidence:

```text
python tools/run_bifree_corridor_certificate_audit.py
proofs/bifree_corridor_certificate_audit.md
```

The rerun on 2026-05-31 reports:

```text
size 2: 5 local-minimal covers, all product_finite_g_branch
size 3: 134 local-minimal covers, all known_total, locally_nondegenerate, or
        product_finite_g_branch
target-shaped intervals: 0
listed-factor B-shaped failures: 0
```

This is candidate-search evidence only.  It does not prove the arbitrary
finite-fibre theorem.

## Current final verdict

[Proved] The finite-linear overlap obstruction is solved.

[Open] The full problem is not yet resolved as `[Resolution: A]` or
`[Resolution: B]`.

The exact remaining obstruction is:

```text
an explicit or universally controlled local-minimal
bi_free_universal_corridor_bottleneck interval whose elementary
universal-continuation seed and triangular recovery unit endpoint either:

  A. always complete to a closed rack-kink Latin branch or admit fixed finite
     V_beta(U_tri) endpoint witnesses; or
  B. produce, from a kink-completion deficit or from the stable perfect
     residual P_tri, a normalized-law residual sequence invisible to every
     finite group while moving an explicit residual tuple.
```
