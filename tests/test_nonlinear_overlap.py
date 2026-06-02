import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    ContinuationCongruenceAudit,
    ContinuationSeedRow,
    GeneratedCongruenceAudit,
    LatinTriangularYBEAudit,
    LocalInterval,
    LocalMasterBottleneckSummary,
    MissingTriangularCoordinateUnitRoute,
    MissingTriangularCoordinateUnitRoutingAudit,
    MissingTriangularPartialConstantClosureAudit,
    MissingTriangularPartialConstantClosureRow,
    MissingTriangularPartialConstantContinuationRouteAudit,
    MissingTriangularPartialConstantContinuationRouteRow,
    MissingTriangularRowProfile,
    MissingTriangularRowProfileAudit,
    NONLINEAR_OVERLAP_TARGET_VERDICT,
    NonlinearOverlapObstructionAudit,
    NonlinearOverlapRefinementAudit,
    PostLinearRemainingFiniteSystemAudit,
    RackKinkLatinTriangularCollapseAudit,
    RightRackKinkLatinTriangularCollapseAudit,
    SectionRankProfileCollapseAudit,
    SectionRankProfileRow,
    TriangularColumnCollapseAudit,
    TriangularColumnCollapseRowAudit,
    TriangularConstantKernelRecoveryRouteAudit,
    TriangularConstantKernelRecoveryRouteRow,
    TriangularLatinDefectClosureAudit,
    TriangularLatinDefectClosureRow,
    UnsupportedCompanionStructuralContradictionAudit,
    UnsupportedCompanionStructuralContradictionRow,
    UniversalKCutoffReadoutAudit,
    UniversalKCutoffReadoutRow,
    UniversalKDetectorTrackInitializationRow,
    UniversalKEndpointMonodromyPresentation,
    UniversalKEndpointMonodromyRepresentationAudit,
    UniversalKEndpointObserverBuild,
    UniversalKEndpointObserverFamilyBuildAudit,
    UniversalKEndpointTargetAudit,
    UniversalKResidualActionScopeAudit,
    UniversalKResidualFaithfulnessAudit,
    UniversalKResidualFaithfulnessRow,
    UniversalKSignedEndpointGeneratorAudit,
    UniversalKSignedEndpointGeneratorRow,
    UniversalKTelescopingDetectorAudit,
    UniversalKWordPotentialCertificate,
    UniversalKWordPotentialIdentityRow,
    TwoSidedUnitCollapseAudit,
    cyclic_group,
    direct_product_group,
    endpoint_coordinate_readout_audit,
    endpoint_family_symmetric_fork_audit,
    endpoint_product_longitude_expression_audit,
    endpoint_residual_action_audit,
    endpoint_residual_readout_audit,
    latin_triangular_ybe_audit,
    mixed_unit_context_endpoint_witness_audit,
    mixed_unit_context_symmetric_endpoint_fork_audit,
    nonlinear_overlap_obstruction_audit,
    nonlinear_overlap_refinement_audit,
    post_linear_remaining_finite_system_audit,
    rack_kink_latin_triangular_collapse_audit,
    right_rack_kink_latin_triangular_collapse_audit,
    section_rank_profile_collapse_audit,
    section_unit_row_audits,
    side_opposite_local_interval,
    symmetric_group,
    missing_triangular_coordinate_unit_routing_audit,
    missing_triangular_left_rack_cardinality_audit,
    missing_triangular_partial_constant_closure_audit,
    missing_triangular_partial_constant_continuation_route_audit,
    missing_triangular_row_profile_audit,
    triangular_bundle_audit,
    triangular_column_collapse_audit,
    triangular_recovery_derived_series_lift_audit,
    triangular_recovery_detector_lift_braid_audit,
    triangular_recovery_detector_lift_transition_audit,
    triangular_recovery_endpoint_witness_audit,
    triangular_recovery_symmetric_endpoint_fork_audit,
    triangular_recovery_longitude_expression_audit,
    triangular_recovery_longitude_route_audit,
    triangular_recovery_perfect_residual_audit,
    triangular_recovery_audit,
    triangular_recovery_unit_observer_audit,
    triangular_recovery_unit_group,
    universal_k_signed_endpoint_artin_update_failures,
    universal_k_endpoint_monodromy_presentation,
    universal_k_endpoint_monodromy_representation_audit,
    universal_k_endpoint_observer_build,
    universal_k_endpoint_observer_builds_by_family,
    universal_k_endpoint_observer_family_build_audit,
    universal_k_endpoint_observer_positive_rows_from_word_potential,
    universal_k_endpoint_observer_signed_rows_from_positive,
    universal_k_identity_cutoff_readout_audit,
    universal_k_identity_endpoint_observer_builds_by_family,
    universal_k_identity_word_potential_certificate,
    universal_k_interval_has_strict_identity_fibre_action,
    universal_k_signed_endpoint_coordinate_failures,
    universal_k_signed_endpoint_far_commutativity_failures,
    universal_k_signed_endpoint_generator_audit,
    universal_k_signed_endpoint_inverse_cancellation_failures,
    universal_k_signed_endpoint_inverse_failures,
    universal_k_signed_endpoint_positive_ybe_cocycle_failures,
    universal_k_signed_endpoint_positive_ybe_failures,
    universal_k_signed_endpoint_required_entry_keys,
    universal_k_signed_endpoint_transition_closure,
    universal_k_strict_identity_residual_faithfulness_audit,
    universal_k_signed_endpoint_two_strand_base_failures,
    universal_k_signed_endpoint_two_strand_witness_domain_failures,
    universal_continuation_identity_endpoint_witness_audit,
    universal_continuation_identity_symmetric_endpoint_fork_audit,
    universal_continuation_identity_routing_audit,
)


def one_color_identity_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (x, y)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_flip_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (y, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_proper_rank_loss_interval():
    colors = ("*",)
    fibres = {"*": (0, 1, 2)}
    base_R = {("*", "*"): ("*", "*")}
    values = {
        (0, 0): (0, 0),
        (0, 1): (0, 1),
        (0, 2): (1, 0),
        (1, 0): (1, 1),
        (1, 1): (1, 2),
        (1, 2): (2, 0),
        (2, 0): (2, 1),
        (2, 1): (2, 2),
        (2, 2): (0, 2),
    }
    return LocalInterval(
        colors,
        fibres,
        base_R,
        {("*", "*", x, y): value for (x, y), value in values.items()},
    )


def one_color_latin_unit_triangular_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (x, (x + y) % 2)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_right_latin_unit_triangular_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): ((x + y) % 2, y)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_right_triangular_nonlatin_interval():
    colors = ("*",)
    fibres = {"*": (0, 1, 2)}
    base_R = {("*", "*"): ("*", "*")}
    permutations = {
        0: {0: 0, 1: 1, 2: 2},
        1: {0: 0, 1: 1, 2: 2},
        2: {0: 1, 1: 2, 2: 0},
    }
    T = {
        ("*", "*", x, y): (permutations[y][x], y)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def target_summary(
    *,
    verdict=NONLINEAR_OVERLAP_TARGET_VERDICT,
    colored_ybe=True,
    semisplit_count=0,
    local_minimal=True,
):
    return LocalMasterBottleneckSummary(
        colored_ybe=colored_ybe,
        semisplit_count=semisplit_count,
        local_minimal=local_minimal,
        local_minimal_error=None,
        local_minimal_pair_count=1,
        local_minimal_pair_failure_count=0,
        local_minimal_pair_max_depth=0,
        retraction_kind="two_sided_free",
        coretraction_kind="two_sided_free",
        product_branch="none",
        product_holonomy_details=(),
        output_kernel_kind="universal",
        output_kernel_stable_depth=0,
        output_kernel_pair_count=1,
        output_kernel_pair_failure_count=0,
        output_kernel_pair_max_depth=0,
        all_coordinate_kernel_kind="universal",
        all_coordinate_kernel_stable_depth=0,
        product_detector_certificates=(),
        total_branch_tags=(),
        known_total_detector_reason=None,
        known_total_detector_group=None,
        known_total_detector_group_order=None,
        known_total_detector_factor_size=None,
        green_detector_group_orders=(),
        verdict=verdict,
        remaining_obligation="test obligation",
    )


def generated(kind):
    return GeneratedCongruenceAudit(
        seed_pair_count=1,
        stable_depth=0,
        family={"*": (frozenset({0, 1}),)},
        kind=kind,
        pair_count_rows=(("*", 1),),
        edge_count_rows=(("*", 1),),
        component_count_rows=(("*", 1),),
        diameter_rows=(("*", 1),),
    )


def continuation(*, kind="universal", seeds=True, non_rack=False):
    seed_rows = ()
    if seeds:
        seed_rows = (
            ContinuationSeedRow(
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                left_input=0,
                right_input=1,
                continuing_output=1,
            ),
        )
    return ContinuationCongruenceAudit(
        seed_rows=seed_rows,
        non_rack_base_rows=(("*", "*", "left", "right"),) if non_rack else (),
        generated=generated(kind),
    )


def exact_obstruction():
    return NonlinearOverlapObstructionAudit(
        summary=target_summary(),
        continuation=continuation(),
    )


def trivial_endpoint_residual_action_audit(input_tuples=(("p",),)):
    group = cyclic_group(2)
    endpoint = endpoint_product_longitude_expression_audit(
        (group,),
        n=2,
        braid_word=(1, -1),
        endpoints=(0,),
        assignments=((1, 0),),
        expressions=((),),
    )
    readouts = tuple(
        endpoint_residual_readout_audit(
            tuple(
                endpoint_coordinate_readout_audit(endpoint, coordinate, coordinate)
                for coordinate in input_tuple
            )
        )
        for input_tuple in input_tuples
    )
    return endpoint_residual_action_audit(
        2,
        (1, -1),
        readouts,
        expected_row_count=len(input_tuples),
        expected_input_tuples=tuple(input_tuples),
    )


def uncounted_endpoint_residual_action_audit():
    group = cyclic_group(2)
    endpoint = endpoint_product_longitude_expression_audit(
        (group,),
        n=2,
        braid_word=(1, -1),
        endpoints=(0,),
        assignments=((1, 0),),
        expressions=((),),
    )
    readout = endpoint_residual_readout_audit(
        (endpoint_coordinate_readout_audit(endpoint, "p", "p"),)
    )
    return endpoint_residual_action_audit(
        2,
        (1, -1),
        (readout,),
    )


def trivial_endpoint_residual_action_scope(
    *families,
    seed_states=None,
    family_row_counts=None,
):
    if seed_states is None:
        seed_states = tuple(
            (family, ("*", "*", "left_constant_map_universal_kernel"))
            for family in families
        )
    if family_row_counts is None:
        family_row_counts = ()
    return UniversalKResidualActionScopeAudit(
        active_endpoint_families=tuple(families),
        covered_endpoint_families=tuple(families),
        expected_residual_row_count=1,
        covered_residual_row_count=1,
        expected_residual_rows_by_family=tuple(family_row_counts),
        covered_residual_rows_by_family=tuple(family_row_counts),
        endpoint_channels_exact=True,
        braid_index_independent=True,
        product_families_separated=True,
        expected_endpoint_seed_states=tuple(seed_states),
        covered_endpoint_seed_states=tuple(seed_states),
        scope_dependencies=(
            "interval_data",
            "routed_seed_state",
            "residual_input_tuple",
            "endpoint_channel",
        ),
    )


def trivial_residual_faithfulness_rows(
    *families,
    seed_states=None,
    input_tuples=(("p",),),
):
    if seed_states is None:
        seed_states = tuple(
            (family, ("*", "*", "left_constant_map_universal_kernel"))
            for family in families
        )
    seed_states = tuple(seed_states)
    return tuple(
        UniversalKResidualFaithfulnessRow(
            input_tuple=tuple(input_tuple),
            output_tuple=tuple(input_tuple),
            identity_endpoint_output_tuple=tuple(input_tuple),
            endpoint_families=tuple(families),
            endpoint_seed_states=seed_states,
            endpoint_channel_keys=tuple(
                (family, seed_state, "endpoint_channel")
                for family, seed_state in seed_states
            ),
            dependencies=(
                "interval_data",
                "routed_seed_state",
                "residual_input_tuple",
                "endpoint_channel",
            ),
        )
        for input_tuple in input_tuples
    )


def trivial_endpoint_target_audit(*families):
    return UniversalKEndpointTargetAudit(
        expected_endpoint_families=tuple(families),
        covered_endpoint_families=tuple(families),
        endpoint_group_orders=tuple((family, 2) for family in families),
        braid_index_independent=True,
        product_families_separated=True,
    )


def trivial_cutoff_readout_audit(seed_states, *, degree=2):
    seed_states = tuple(seed_states)
    return UniversalKCutoffReadoutAudit(
        expected_cutoff_seed_states=seed_states,
        covered_cutoff_seed_states=seed_states,
        cutoff_degree=degree,
        readout_rows=tuple(
            UniversalKCutoffReadoutRow(
                cutoff_seed_state=seed_state,
                readout_permutation=tuple(
                    (position + index) % degree for position in range(degree)
                ),
                killed_readout_permutation=tuple(range(degree)),
            )
            for index, seed_state in enumerate(seed_states)
        ),
        braid_index_independent=True,
    )


def trivial_telescoping_detector_audit(
    keys,
    *,
    rows=(),
    endpoint_group=None,
    normalized_seed_states=None,
):
    keys = tuple(keys)
    endpoint_group = endpoint_group or cyclic_group(2)
    row_by_key = {row.entry_key: row for row in rows}
    seed_states = tuple(
        sorted({(family, state) for family, state, *_rest in keys}, key=repr)
    )
    if normalized_seed_states is None:
        normalized_seed_states = seed_states
    else:
        normalized_seed_states = tuple(normalized_seed_states)
    families = tuple(sorted({family for family, _state in seed_states}, key=repr))
    word_potential_certificate = UniversalKWordPotentialCertificate(
        endpoint_group=endpoint_group,
        templates=tuple((seed_state, ()) for seed_state in seed_states),
        identity_rows=tuple(
            UniversalKWordPotentialIdentityRow(
                entry_key=key,
                next_seed_state=(
                    row_by_key[key].next_seed_state if key in row_by_key else key[1]
                ),
                endpoint_value=(
                    row_by_key[key].endpoint_value
                    if key in row_by_key
                    else endpoint_group.identity
                ),
                artin_substitution=(),
            )
            for key in keys
        ),
        normalized_seed_states=normalized_seed_states,
    )
    return UniversalKTelescopingDetectorAudit(
        expected_entry_keys=keys,
        covered_entry_keys=keys,
        expected_endpoint_seed_states=seed_states,
        covered_endpoint_seed_states=seed_states,
        detector_track_counts_by_family=tuple((family, 1) for family in families),
        detector_track_initialization_rows=tuple(
            UniversalKDetectorTrackInitializationRow(
                endpoint_family=family,
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), endpoint_group.identity),),
            )
            for family in families
        ),
        expected_word_potential_seed_states=seed_states,
        covered_word_potential_seed_states=seed_states,
        detector_track_count=len(families),
        detector_tracks_fixed_before_braid=True,
        detector_track_initialization_verified=True,
        artin_detector_recurrence_verified=True,
        word_potential_templates_use_only_current_longitudes=True,
        word_potential_artin_substitution_verified=True,
        word_potential_identity_verified=True,
        word_potential_certificate=word_potential_certificate,
        telescoping_identity_verified=True,
        terminal_readout_longitudes_verified=True,
        initial_readout_normalized=True,
        braid_index_independent=True,
    )


def identity_signed_endpoint_rows(keys, next_state_by_current=None):
    next_state_by_current = dict(next_state_by_current or {})
    rows = []
    for (
        endpoint_family,
        state,
        sign,
        left_color,
        right_color,
        input_left,
        input_right,
    ) in keys:
        rows.append(
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family=endpoint_family,
                seed_state=state,
                sign=sign,
                left_color=left_color,
                right_color=right_color,
                input_left=input_left,
                input_right=input_right,
                output_left=input_left,
                output_right=input_right,
                next_seed_state=next_state_by_current.get(
                    (endpoint_family, state),
                    state,
                ),
                endpoint_value=0,
            )
        )
    return tuple(rows)


def refinement_for(interval, *, colored_ybe=True):
    return NonlinearOverlapRefinementAudit(
        obstruction=exact_obstruction(),
        unit_collapse=TwoSidedUnitCollapseAudit(
            colored_ybe=colored_ybe,
            continuation=continuation(),
            row_audits=section_unit_row_audits(interval),
        ),
        rank_profile=section_rank_profile_collapse_audit(interval),
        triangular_bundle=triangular_bundle_audit(interval),
        triangular_recovery=triangular_recovery_audit(interval),
        triangular_column=triangular_column_collapse_audit(interval),
        latin_triangular=latin_triangular_ybe_audit(interval),
        side_dual_latin_triangular=latin_triangular_ybe_audit(
            side_opposite_local_interval(interval),
        ),
        rack_kink=rack_kink_latin_triangular_collapse_audit(interval),
        side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
            side_opposite_local_interval(interval),
        ),
    )


def active_system_k_refinement():
    return replace(
        refinement_for(one_color_right_triangular_nonlatin_interval(), colored_ybe=False),
        rank_profile=SectionRankProfileCollapseAudit(rows=()),
    )


def constant_map_kernel_system_k_refinement():
    interval = one_color_latin_unit_triangular_interval()
    unit_section = SectionRankProfileRow(
        side="left-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    row = TriangularColumnCollapseRowAudit(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0,),
        constant_map=((0, 0), (1, 0)),
        companion_sections=(unit_section,),
        opposite_sections=(unit_section,),
    )
    return replace(
        refinement_for(interval, colored_ybe=False),
        triangular_column=TriangularColumnCollapseAudit((row,)),
    )


def companion_block_system_k_refinement():
    interval = one_color_latin_unit_triangular_interval()
    companion_section = SectionRankProfileRow(
        side="left-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=2,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    opposite_section = SectionRankProfileRow(
        side="left-opposite",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    row = TriangularColumnCollapseRowAudit(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0,),
        constant_map=((0, 0), (1, 0)),
        companion_sections=(companion_section,),
        opposite_sections=(opposite_section,),
    )
    return replace(
        refinement_for(interval, colored_ybe=False),
        triangular_column=TriangularColumnCollapseAudit((row,)),
    )


def singleton_constant_map_non_surjective_refinement():
    interval = one_color_latin_unit_triangular_interval()
    unit_section = SectionRankProfileRow(
        side="left-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    row = TriangularColumnCollapseRowAudit(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0, 1),
        constant_map=((0, 0),),
        companion_sections=(unit_section,),
        opposite_sections=(unit_section,),
    )
    return replace(
        refinement_for(interval, colored_ybe=False),
        triangular_column=TriangularColumnCollapseAudit((row,)),
    )


def unsupported_companion_block_image_refinement():
    interval = one_color_latin_unit_triangular_interval()
    companion_section = SectionRankProfileRow(
        side="left-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=2,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    opposite_section = SectionRankProfileRow(
        side="left-opposite",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    row = TriangularColumnCollapseRowAudit(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0,),
        constant_map=((0, 0),),
        companion_sections=(companion_section,),
        opposite_sections=(opposite_section,),
    )
    return replace(
        refinement_for(interval, colored_ybe=False),
        triangular_column=TriangularColumnCollapseAudit((row,)),
    )


def constant_map_kernel_only_system_k_refinement():
    interval = one_color_latin_unit_triangular_interval()
    left_unit_section = SectionRankProfileRow(
        side="left-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    left_row = TriangularColumnCollapseRowAudit(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0,),
        constant_map=((0, 0), (1, 0)),
        companion_sections=(left_unit_section,),
        opposite_sections=(left_unit_section,),
    )
    right_unit_section = SectionRankProfileRow(
        side="right-companion",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=1,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0,),),
        image=(0,),
    )
    right_constant_opposite = SectionRankProfileRow(
        side="right-opposite",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=1,
        rank=1,
        kernel_blocks=((0, 1),),
        image=(0,),
    )
    right_product_row = TriangularColumnCollapseRowAudit(
        side="right",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        constant_codomain=(0,),
        constant_map=((0, 0),),
        companion_sections=(right_unit_section,),
        opposite_sections=(right_constant_opposite,),
    )
    return replace(
        refinement_for(interval, colored_ybe=False),
        triangular_column=TriangularColumnCollapseAudit((left_row, right_product_row)),
    )


def partial_constant_missing_row_profile_route_audits():
    unit_section = SectionRankProfileRow(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    constant_section = SectionRankProfileRow(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=1,
        domain_size=2,
        codomain_size=2,
        rank=1,
        kernel_blocks=((0, 1),),
        image=(0,),
    )
    profile = MissingTriangularRowProfileAudit(
        rows=(
            MissingTriangularRowProfile(
                side="left",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                section_profiles=(unit_section, constant_section),
            ),
        ),
    )
    closure = MissingTriangularPartialConstantClosureAudit(
        rows=(
            MissingTriangularPartialConstantClosureRow(
                side="left",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                fixed_input=1,
                domain_color="*",
                collapsed_inputs=(0, 1),
                generated=generated("universal"),
            ),
        ),
    )
    route = MissingTriangularPartialConstantContinuationRouteAudit(
        rows=(
            MissingTriangularPartialConstantContinuationRouteRow(
                side="left",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                fixed_input=1,
                domain_color="*",
                collapsed_inputs=(0, 1),
                closure_kind="universal",
                companion_output_color="*",
                companion_outputs=(0, 1),
                continuation_seed_witnesses=(
                    ContinuationSeedRow(
                        left_color="*",
                        right_color="*",
                        output_left_color="*",
                        output_right_color="*",
                        left_input=1,
                        right_input=0,
                        continuing_output=1,
                    ),
                ),
                continuation_seed_closure_kinds=("universal",),
                partial_edge_contained_in_seed_closure=True,
            ),
        ),
    )
    return profile, closure, route


def right_partial_constant_missing_row_profile_route_audits():
    unit_section = SectionRankProfileRow(
        side="right",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    constant_section = SectionRankProfileRow(
        side="right",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=1,
        domain_size=2,
        codomain_size=2,
        rank=1,
        kernel_blocks=((0, 1),),
        image=(0,),
    )
    profile = MissingTriangularRowProfileAudit(
        rows=(
            MissingTriangularRowProfile(
                side="right",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                section_profiles=(unit_section, constant_section),
            ),
        ),
    )
    closure = MissingTriangularPartialConstantClosureAudit(
        rows=(
            MissingTriangularPartialConstantClosureRow(
                side="right",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                fixed_input=1,
                domain_color="*",
                collapsed_inputs=(0, 1),
                generated=generated("universal"),
            ),
        ),
    )
    route = MissingTriangularPartialConstantContinuationRouteAudit(
        rows=(
            MissingTriangularPartialConstantContinuationRouteRow(
                side="right",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                fixed_input=1,
                domain_color="*",
                collapsed_inputs=(0, 1),
                closure_kind="universal",
                companion_output_color="*",
                companion_outputs=(0, 1),
                continuation_seed_witnesses=(
                    ContinuationSeedRow(
                        left_color="*",
                        right_color="*",
                        output_left_color="*",
                        output_right_color="*",
                        left_input=0,
                        right_input=1,
                        continuing_output=1,
                    ),
                ),
                continuation_seed_closure_kinds=("universal",),
                partial_edge_contained_in_seed_closure=True,
            ),
        ),
    )
    return profile, closure, route


def coordinate_unit_mixed_context_route_audits():
    unit_section = SectionRankProfileRow(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    profile = MissingTriangularRowProfileAudit(
        rows=(
            MissingTriangularRowProfile(
                side="left",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                section_profiles=(unit_section,),
            ),
        ),
    )
    routing = MissingTriangularCoordinateUnitRoutingAudit(
        colored_ybe=True,
        locally_nondegenerate_closed_branch=False,
        rows=(
            MissingTriangularCoordinateUnitRoute(
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                coordinate_unit_sides=("left",),
                left_explanation="coordinate_side_unit_not_triangular",
                right_explanation="proper_section_kernel_visible",
                left_unit_inputs=(0,),
                left_nonunit_inputs=(),
                right_unit_inputs=(),
                right_nonunit_inputs=(0,),
            ),
        ),
    )
    return profile, routing


def coordinate_unit_unclosed_two_sided_route_audits():
    unit_section = SectionRankProfileRow(
        side="left",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    profile = MissingTriangularRowProfileAudit(
        rows=(
            MissingTriangularRowProfile(
                side="left",
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                section_profiles=(unit_section,),
            ),
        ),
    )
    routing = MissingTriangularCoordinateUnitRoutingAudit(
        colored_ybe=True,
        locally_nondegenerate_closed_branch=False,
        rows=(
            MissingTriangularCoordinateUnitRoute(
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                coordinate_unit_sides=("left",),
                left_explanation="coordinate_side_unit_not_triangular",
                right_explanation="coordinate_side_unit_not_triangular",
                left_unit_inputs=(0,),
                left_nonunit_inputs=(),
                right_unit_inputs=(0,),
                right_nonunit_inputs=(),
            ),
        ),
    )
    return profile, routing


def continuation_and_mixed_context_route_audits():
    continuation_profile, closure, route = partial_constant_missing_row_profile_route_audits()
    unit_section = SectionRankProfileRow(
        side="right",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        fixed_input=0,
        domain_size=2,
        codomain_size=2,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
    )
    mixed_profile = MissingTriangularRowProfile(
        side="right",
        left_color="*",
        right_color="*",
        output_left_color="*",
        output_right_color="*",
        section_profiles=(unit_section,),
    )
    profile = MissingTriangularRowProfileAudit(
        rows=continuation_profile.rows + (mixed_profile,),
    )
    coordinate_routing = MissingTriangularCoordinateUnitRoutingAudit(
        colored_ybe=True,
        locally_nondegenerate_closed_branch=False,
        rows=(
            MissingTriangularCoordinateUnitRoute(
                left_color="*",
                right_color="*",
                output_left_color="*",
                output_right_color="*",
                coordinate_unit_sides=("right",),
                left_explanation="partial_constant_hidden_rank_loss",
                right_explanation="coordinate_side_unit_not_triangular",
                left_unit_inputs=(),
                left_nonunit_inputs=(0,),
                right_unit_inputs=(0,),
                right_nonunit_inputs=(),
            ),
        ),
    )
    return profile, closure, route, coordinate_routing


class TwoNoTriangularRawKRefinement:
    status = "triangular_recovery_kink_completion_deficit"
    active_missing_left_latin_row_defects = ((("*", "*"), "no_left_triangular_row"),)
    active_missing_right_latin_row_defects = ((("*", "*"), "no_right_triangular_row"),)


class PassingRepair:
    @property
    def proves_repair_contract_for_supplied_data(self):
        return True


class FailingRepair:
    @property
    def proves_repair_contract_for_supplied_data(self):
        return False

    @property
    def failure_reasons(self):
        return ("endpoint_action_detector_not_proved",)


class PassingNormalizedPrefix:
    @property
    def proves_one_local_prefix_normalized_law_witness(self):
        return True


class FailingNormalizedPrefix:
    @property
    def proves_one_local_prefix_normalized_law_witness(self):
        return False


class NonlinearOverlapObstructionAuditTests(unittest.TestCase):
    def test_function_routes_known_total_identity_out_of_target(self):
        audit = nonlinear_overlap_obstruction_audit(one_color_identity_interval())

        self.assertEqual(audit.status, "not_corridor_target")
        self.assertFalse(audit.is_corridor_verdict)
        self.assertEqual(audit.failure_reasons, (f"verdict:{audit.summary.verdict}",))

    def test_exact_remaining_shape_requires_universal_continuation_seed(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(),
            continuation=continuation(),
        )

        self.assertTrue(audit.is_valid_local_minimal_corridor)
        self.assertTrue(audit.universal_continuation_shape)
        self.assertTrue(audit.exact_remaining_nonlinear_shape)
        self.assertEqual(audit.status, "exact_remaining_nonlinear_obstruction")
        self.assertEqual(audit.failure_reasons, ())

    def test_repair_contract_closes_valid_corridor_shape(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(),
            continuation=continuation(),
            repair_contract_audit=PassingRepair(),
        )

        self.assertTrue(audit.repair_contract_closes)
        self.assertEqual(audit.status, "closed_by_repair_contract")

    def test_normalized_prefix_is_only_one_b_shaped_row(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(),
            continuation=continuation(),
            normalized_prefix=PassingNormalizedPrefix(),
        )

        self.assertTrue(audit.normalized_prefix_certifies_b_row)
        self.assertEqual(audit.status, "one_normalized_b_prefix_certified")

    def test_strand_continuing_case_is_closed_before_remaining_shape(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(),
            continuation=continuation(kind="equality", seeds=False),
        )

        self.assertTrue(audit.strand_continuing_closed)
        self.assertFalse(audit.exact_remaining_nonlinear_shape)
        self.assertEqual(audit.status, "closed_by_transport_state_rackification")
        self.assertEqual(audit.failure_reasons, ("no_continuation_seed",))

    def test_invalid_and_failed_supplied_certificates_explain_their_reasons(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(semisplit_count=1, local_minimal=False),
            continuation=continuation(kind="proper"),
            repair_contract_audit=FailingRepair(),
            normalized_prefix=FailingNormalizedPrefix(),
        )

        self.assertEqual(audit.status, "invalid_local_corridor_data")
        self.assertIn("semisplit_family_survives", audit.failure_reasons)
        self.assertIn("not_local_minimal", audit.failure_reasons)
        self.assertIn("continuation_closure:proper", audit.failure_reasons)
        self.assertIn(
            "repair_contract:endpoint_action_detector_not_proved",
            audit.failure_reasons,
        )
        self.assertIn("normalized_prefix_not_certified", audit.failure_reasons)

    def test_non_left_rack_base_rows_are_not_remaining_corridor_shape(self):
        audit = NonlinearOverlapObstructionAudit(
            summary=target_summary(),
            continuation=continuation(non_rack=True),
        )

        self.assertEqual(audit.status, "base_not_left_rack_form")
        self.assertFalse(audit.exact_remaining_nonlinear_shape)
        self.assertIn("non_left_rack_base_rows", audit.failure_reasons)

    def test_refinement_function_preserves_non_target_status(self):
        audit = nonlinear_overlap_refinement_audit(one_color_identity_interval())

        self.assertEqual(audit.status, "not_corridor_target")
        self.assertFalse(audit.target_ready)
        self.assertEqual(audit.remaining_obligations, audit.obstruction.failure_reasons)

    def test_refinement_closes_two_sided_unit_rows_by_nondegenerate_branch(self):
        audit = refinement_for(one_color_flip_interval())

        self.assertTrue(audit.closed_by_locally_nondegenerate_branch)
        self.assertEqual(audit.status, "closed_by_locally_nondegenerate_branch")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_routes_proper_section_kernels_to_existing_readouts(self):
        audit = refinement_for(one_color_proper_rank_loss_interval())

        self.assertTrue(audit.proper_section_kernel_visible)
        self.assertEqual(audit.status, "section_kernel_visible_to_existing_readouts")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_product_triangular_collapse(self):
        audit = refinement_for(one_color_identity_interval())

        self.assertTrue(audit.all_triangular_rows_close_by_product)
        self.assertEqual(audit.status, "closed_by_product_triangular_collapse")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_impossible_triangular_structural_rows(self):
        interval = one_color_latin_unit_triangular_interval()
        unit_section = SectionRankProfileRow(
            side="left",
            left_color="*",
            right_color="*",
            output_left_color="*",
            output_right_color="*",
            fixed_input=0,
            domain_size=2,
            codomain_size=2,
            rank=2,
            kernel_blocks=((0,), (1,)),
            image=(0, 1),
        )
        bad_row = TriangularColumnCollapseRowAudit(
            side="left",
            left_color="*",
            right_color="*",
            output_left_color="*",
            output_right_color="*",
            constant_codomain=(0, 1),
            constant_map=((0, 0), (1, 0)),
            companion_sections=(unit_section,),
            opposite_sections=(unit_section,),
        )
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=False,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=TriangularColumnCollapseAudit((bad_row,)),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=rack_kink_latin_triangular_collapse_audit(interval),
            side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
                side_opposite_local_interval(interval),
            ),
        )

        self.assertTrue(audit.triangular_structural_inconsistency)
        self.assertEqual(audit.status, "triangular_structural_inconsistency")
        self.assertEqual(audit.active_missing_left_latin_row_defects, ())
        self.assertEqual(audit.active_missing_right_latin_row_defects, ())
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_impossible_rack_base_deficit_in_target(self):
        interval = one_color_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=False,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=RackKinkLatinTriangularCollapseAudit(
                base_rows_are_left_rack_form=True,
                left_translations_bijective=False,
                self_distributive=False,
                kink_predecessors={},
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=False,
                alpha_kink_identity_failures=(),
                kink_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
            side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
                side_opposite_local_interval(interval),
            ),
        )

        self.assertTrue(audit.rack_base_consistency_inconsistent)
        self.assertEqual(audit.status, "rack_base_consistency_inconsistent")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_left_latin_ybe_projection_inconsistency(self):
        audit = refinement_for(one_color_latin_unit_triangular_interval())

        self.assertTrue(audit.mixed_unit_context_recovery)
        self.assertTrue(audit.triangular_recovery_verified)
        self.assertTrue(audit.triangular_endpoint_recovery_obstruction)
        self.assertTrue(audit.triangular_recovery_unit_observer_ready)
        self.assertTrue(audit.latin_triangular_ybe_projection_inconsistent)
        self.assertEqual(audit.missing_left_latin_row_pairs, ())
        self.assertEqual(
            audit.latin_ybe_failure_triples,
            (("*", "*", "*", "middle"), ("*", "*", "*", "endpoint")),
        )
        self.assertEqual(audit.status, "latin_triangular_ybe_projection_inconsistent")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_inconsistent_nontrivial_kink_latin_hypotheses(self):
        interval = one_color_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=True,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=RackKinkLatinTriangularCollapseAudit(
                base_rows_are_left_rack_form=True,
                left_translations_bijective=True,
                self_distributive=True,
                kink_predecessors={"*": "*"},
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=True,
                alpha_kink_identity_failures=(),
                kink_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
            side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
                side_opposite_local_interval(interval),
            ),
        )

        self.assertTrue(audit.latin_triangular_kink_contradiction)
        self.assertTrue(audit.latin_triangular_ybe_projection_inconsistent)
        self.assertEqual(audit.status, "latin_triangular_ybe_projection_inconsistent")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_kink_cancellation_failure_under_theorem_hypotheses(self):
        interval = one_color_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=False,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=RackKinkLatinTriangularCollapseAudit(
                base_rows_are_left_rack_form=True,
                left_translations_bijective=True,
                self_distributive=True,
                kink_predecessors={"*": "*"},
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=True,
                alpha_kink_identity_failures=(("*", 0, 1),),
                kink_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
            side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
                side_opposite_local_interval(interval),
            ),
        )

        self.assertTrue(audit.latin_triangular_kink_cancellation_inconsistent)
        self.assertEqual(audit.status, "latin_triangular_kink_cancellation_inconsistent")
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_side_dual_latin_ybe_projection_inconsistency(self):
        audit = refinement_for(one_color_right_latin_unit_triangular_interval())

        self.assertTrue(audit.triangular_recovery_verified)
        self.assertTrue(audit.side_dual_latin_triangular_ybe_projection_inconsistent)
        self.assertEqual(audit.left_latin_row_pairs, ())
        self.assertEqual(audit.right_latin_row_pairs, (("*", "*"),))
        self.assertEqual(audit.missing_left_latin_row_pairs, (("*", "*"),))
        self.assertEqual(audit.missing_right_latin_row_pairs, ())
        self.assertTrue(audit.side_dual_latin_completion_available)
        self.assertEqual(
            audit.side_dual_latin_ybe_failure_triples,
            (("*", "*", "*", "middle"), ("*", "*", "*", "endpoint")),
        )
        self.assertEqual(
            audit.status,
            "side_dual_latin_triangular_ybe_projection_inconsistent",
        )
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_closes_side_dual_diagonal_failure_under_theorem_hypotheses(
        self,
    ):
        interval = one_color_right_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=False,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=rack_kink_latin_triangular_collapse_audit(interval),
            side_dual_rack_kink=RightRackKinkLatinTriangularCollapseAudit(
                base_rows_are_right_rack_form=True,
                right_translations_bijective=True,
                right_self_distributive=True,
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=True,
                alpha_diagonal_identity_failures=(("*", 0, 1),),
                diagonal_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
        )

        self.assertTrue(
            audit.side_dual_latin_triangular_diagonal_cancellation_inconsistent
        )
        self.assertEqual(
            audit.status,
            "side_dual_latin_triangular_diagonal_cancellation_inconsistent",
        )
        self.assertEqual(audit.remaining_obligations, ())

    def test_refinement_records_missing_left_latin_defect_ledger(self):
        audit = refinement_for(
            one_color_right_latin_unit_triangular_interval(),
            colored_ybe=False,
        )

        self.assertEqual(audit.left_triangular_row_pairs, ())
        self.assertEqual(audit.right_triangular_row_pairs, (("*", "*"),))
        self.assertEqual(
            audit.missing_left_latin_row_defects,
            (
                (("*", "*"), "no_left_triangular_row"),
                (("*", "*"), "side_dual_right_latin_available"),
            ),
        )
        self.assertEqual(audit.missing_right_latin_row_defects, ())
        self.assertEqual(audit.active_missing_left_latin_row_defects, ())
        self.assertEqual(audit.active_missing_right_latin_row_defects, ())

    def test_refinement_records_side_dual_missing_right_latin_defect_ledger(self):
        audit = refinement_for(
            one_color_latin_unit_triangular_interval(),
            colored_ybe=False,
        )

        self.assertEqual(audit.left_triangular_row_pairs, (("*", "*"),))
        self.assertEqual(audit.right_triangular_row_pairs, ())
        self.assertEqual(audit.missing_left_latin_row_defects, ())
        self.assertEqual(
            audit.missing_right_latin_row_defects,
            (
                (("*", "*"), "no_right_triangular_row"),
                (("*", "*"), "side_dual_left_latin_available"),
            ),
        )
        self.assertEqual(audit.active_missing_left_latin_row_defects, ())
        self.assertEqual(audit.active_missing_right_latin_row_defects, ())

    def test_refinement_closes_inconsistent_nontrivial_side_dual_latin_hypotheses(self):
        interval = one_color_right_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=True,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=latin_triangular_ybe_audit(interval),
            side_dual_latin_triangular=latin_triangular_ybe_audit(
                side_opposite_local_interval(interval),
            ),
            rack_kink=rack_kink_latin_triangular_collapse_audit(interval),
            side_dual_rack_kink=RightRackKinkLatinTriangularCollapseAudit(
                base_rows_are_right_rack_form=True,
                right_translations_bijective=True,
                right_self_distributive=True,
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=True,
                alpha_diagonal_identity_failures=(),
                diagonal_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
        )

        self.assertTrue(audit.side_dual_latin_triangular_kink_contradiction)
        self.assertTrue(audit.side_dual_latin_triangular_ybe_projection_inconsistent)
        self.assertEqual(
            audit.status,
            "side_dual_latin_triangular_ybe_projection_inconsistent",
        )
        self.assertEqual(audit.remaining_obligations, ())

    def test_post_linear_remaining_finite_system_audit_closes_nonlive_raw_k(self):
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement_for(one_color_latin_unit_triangular_interval(), colored_ybe=False)
        )

        self.assertEqual(audit.system_name, "closed_by_recorded_k_deficit_routing")
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("live_kink_completion_deficits", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "nonlive_kink_completion_deficits",
                ("latin_ybe_equations_not_verified",),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("latin_ybe_failure_triples", (("*", "*", "*", "middle"), ("*", "*", "*", "endpoint"))),
            audit.finite_obstruction_data,
        )

    def test_post_linear_remaining_finite_system_audit_closes_routed_side_dual_k_data(self):
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement_for(
                one_color_right_latin_unit_triangular_interval(),
                colored_ybe=False,
            )
        )

        self.assertEqual(audit.system_name, "closed_by_recorded_k_deficit_routing")
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("live_kink_completion_deficits", ("latin_rows_not_present_for_all_pairs",)),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "nonlive_kink_completion_deficits",
                ("side_dual_latin_rows_present_for_all_pairs",),
            ),
            audit.finite_obstruction_data,
        )
        self.assertEqual(
            audit.k_left_side_dual_replacement_rows,
            (
                (
                    ("*", "*"),
                    "side_dual_right_latin_available",
                    (),
                    (),
                ),
            ),
        )
        self.assertIn(
            ("side_dual_latin_completion_available", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_right_latin_row_pairs", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_left_latin_row_defects",
                (
                    (("*", "*"), "no_left_triangular_row"),
                    (("*", "*"), "side_dual_right_latin_available"),
                ),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("active_missing_left_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("direct_unit_longitude_status_preempted_by_kink_dichotomy", False),
            audit.finite_obstruction_data,
        )
        for key in (
            "triangular_constant_map_non_surjective_rows",
            "triangular_companion_kernel_rows",
            "triangular_companion_nonbijective_without_constant_kernel_rows",
            "triangular_hidden_nonunit_opposite_without_product_rows",
        ):
            self.assertIn((key, ()), audit.finite_obstruction_data)
        self.assertIn(
            (
                "side_dual_latin_ybe_failure_triples",
                (("*", "*", "*", "middle"), ("*", "*", "*", "endpoint")),
            ),
            audit.finite_obstruction_data,
        )

    def test_post_linear_remaining_finite_system_audit_keeps_active_k_rows(self):
        audit = PostLinearRemainingFiniteSystemAudit(active_system_k_refinement())

        self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
        self.assertTrue(audit.is_current_remaining_finite_system)
        self.assertIn(
            ("live_kink_completion_deficits", ("latin_rows_not_present_for_all_pairs",)),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )

    def test_post_linear_routes_no_triangular_row_when_profile_is_supplied(self):
        interval = one_color_right_triangular_nonlatin_interval()
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=missing_triangular_row_profile_audit(
                interval
            ),
        )

        self.assertEqual(audit.system_name, "closed_by_recorded_k_deficit_routing")
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("active_missing_left_latin_row_defects", ((("*", "*"), "no_left_triangular_row"),)),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_triangular_row_profiles",
                (("left", "*", "*", "proper_section_kernel_visible", (), (0, 1, 2)),),
            ),
            audit.finite_obstruction_data,
        )

    def test_partial_constant_no_triangular_route_becomes_continuation_endpoint(self):
        profile, closure, route = partial_constant_missing_row_profile_route_audits()
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=closure,
            missing_triangular_partial_constant_continuation_route=route,
        )

        self.assertEqual(
            audit.system_name,
            "system_c_universal_continuation_endpoint",
        )
        self.assertTrue(audit.system_c_active)
        self.assertFalse(audit.k_deficits_closed_by_recorded_routing)
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "continuation_routed_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        descriptor = (
            "*",
            "*",
            "L",
            "partial_constant_hidden_rank_loss",
            (1, "*", (0, 1), "*", (0, 1), "universal", ("universal",), True),
        )
        self.assertEqual(audit.universal_k_row_normal_form_domain, (descriptor,))
        self.assertEqual(
            audit.universal_k_seed_classifier_entries,
            (
                (
                    descriptor,
                    ("C", ("*", "*", "left", 1, "*", (0, 1), "*", (0, 1))),
                ),
            ),
        )
        self.assertEqual(
            audit.remaining_obligations,
            (
                "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
            ),
        )

    def test_partial_constant_route_requires_universal_continuation_seed(self):
        profile, closure, route = partial_constant_missing_row_profile_route_audits()
        nonuniversal_route = MissingTriangularPartialConstantContinuationRouteAudit(
            rows=(
                replace(
                    route.rows[0],
                    continuation_seed_closure_kinds=("proper",),
                ),
            ),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=closure,
            missing_triangular_partial_constant_continuation_route=nonuniversal_route,
        )

        self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
        self.assertTrue(audit.system_k_active)
        self.assertFalse(audit.system_c_active)
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("continuation_routed_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_triangular_partial_constant_unrouted_continuation_rows",
                (
                    (
                        "left",
                        "*",
                        "*",
                        1,
                        "*",
                        (0, 1),
                        "routed_to_continuation_seed_closure",
                    ),
                ),
            ),
            audit.finite_obstruction_data,
        )

    def test_partial_constant_route_requires_universal_partial_closure(self):
        profile, closure, route = partial_constant_missing_row_profile_route_audits()
        equality_closure = MissingTriangularPartialConstantClosureAudit(
            rows=(replace(closure.rows[0], generated=generated("equality")),),
        )
        equality_route = MissingTriangularPartialConstantContinuationRouteAudit(
            rows=(replace(route.rows[0], closure_kind="equality"),),
        )

        self.assertFalse(
            equality_route.rows[0].routes_to_universal_continuation_seed
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=equality_closure,
            missing_triangular_partial_constant_continuation_route=equality_route,
        )

        self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
        self.assertTrue(audit.system_k_active)
        self.assertFalse(audit.system_c_active)
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("continuation_routed_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )

    def test_partial_constant_proper_closure_closes_system_k(self):
        profile, closure, _route = partial_constant_missing_row_profile_route_audits()
        proper_closure = MissingTriangularPartialConstantClosureAudit(
            rows=(replace(closure.rows[0], generated=generated("proper")),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=proper_closure,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_missing_triangular_partial_constant_proper_closure",
        )
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertFalse(audit.system_k_active)
        self.assertEqual(audit.live_k_missing_latin_row_defects, ())
        self.assertEqual(audit.active_routed_endpoint_systems, ())
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            (
                "missing_triangular_partial_constant_proper_closure_rows",
                (
                    (
                        "left",
                        "*",
                        "*",
                        1,
                        "*",
                        (0, 1),
                        "proper",
                    ),
                ),
            ),
            audit.finite_obstruction_data,
        )

    def test_coordinate_unit_mixed_context_route_becomes_mixed_endpoint(self):
        profile, routing = coordinate_unit_mixed_context_route_audits()
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_coordinate_unit_routing=routing,
        )

        self.assertEqual(
            audit.system_name,
            "system_m_mixed_unit_context_endpoint",
        )
        self.assertTrue(audit.system_m_active)
        self.assertFalse(audit.k_deficits_closed_by_recorded_routing)
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "mixed_context_routed_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        descriptor = (
            "*",
            "*",
            "L",
            "coordinate_side_unit_not_triangular",
            (
                ("left",),
                "coordinate_side_unit_not_triangular",
                "proper_section_kernel_visible",
                (0,),
                (),
                (),
                (0,),
            ),
        )
        self.assertEqual(audit.universal_k_row_normal_form_domain, (descriptor,))
        self.assertEqual(
            audit.universal_k_seed_classifier_entries,
            ((descriptor, ("M", ("*", "*", "left"))),),
        )
        self.assertEqual(
            audit.remaining_obligations,
            (
                "prove each routed mixed-unit context endpoint factors through fixed detector/readout data",
                "or upgrade one routed mixed-unit endpoint miss to a normalized-law sequence",
            ),
        )

    def test_coordinate_unit_route_requires_colored_ybe_certificate(self):
        profile, routing = coordinate_unit_mixed_context_route_audits()
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_coordinate_unit_routing=replace(
                routing,
                colored_ybe=False,
            ),
        )

        self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
        self.assertTrue(audit.system_k_active)
        self.assertFalse(audit.system_m_active)
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_context_routed_k_missing_latin_row_defects", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_coordinate_unit_routing_proved", False),
            audit.finite_obstruction_data,
        )

    def test_coordinate_unit_route_requires_listed_unit_side_certificate(self):
        profile, routing = coordinate_unit_mixed_context_route_audits()
        forged_rows = (
            replace(
                routing.rows[0],
                left_unit_inputs=(),
                left_nonunit_inputs=(0,),
                right_unit_inputs=(0,),
                right_nonunit_inputs=(),
            ),
            replace(
                routing.rows[0],
                left_explanation="proper_section_kernel_visible",
            ),
        )

        for forged_row in forged_rows:
            with self.subTest(forged_row=forged_row):
                forged_routing = replace(routing, rows=(forged_row,))
                audit = PostLinearRemainingFiniteSystemAudit(
                    active_system_k_refinement(),
                    missing_triangular_row_profile=profile,
                    missing_triangular_coordinate_unit_routing=forged_routing,
                )

                self.assertFalse(forged_row.coordinate_unit_route_fields_consistent)
                self.assertEqual(forged_row.status, "unrouted_coordinate_unit_row")
                self.assertFalse(forged_routing.proves_coordinate_unit_routing_ledger)
                self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
                self.assertTrue(audit.system_k_active)
                self.assertFalse(audit.system_m_active)
                self.assertIn(
                    (
                        "live_k_missing_latin_row_defects",
                        ((("*", "*"), "no_left_triangular_row"),),
                    ),
                    audit.finite_obstruction_data,
                )
                self.assertIn(
                    ("mixed_context_routed_k_missing_latin_row_defects", ()),
                    audit.finite_obstruction_data,
                )

    def test_coordinate_unit_two_sided_row_stays_live_without_global_branch(self):
        profile, routing = coordinate_unit_unclosed_two_sided_route_audits()
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_coordinate_unit_routing=routing,
        )

        self.assertEqual(routing.two_sided_unit_pair_rows, routing.rows)
        self.assertEqual(routing.unclosed_two_sided_unit_pair_rows, routing.rows)
        self.assertFalse(routing.all_coordinate_unit_rows_routed)
        self.assertFalse(routing.proves_coordinate_unit_routing_ledger)
        self.assertEqual(audit.system_name, "system_k_kink_completion_deficit")
        self.assertTrue(audit.system_k_active)
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_triangular_coordinate_unit_unclosed_two_sided_rows",
                (
                    (
                        "*",
                        "*",
                        ("left",),
                        "coordinate_side_unit_not_triangular",
                        "coordinate_side_unit_not_triangular",
                    ),
                ),
            ),
            audit.finite_obstruction_data,
        )

    def test_continuation_endpoint_witness_closes_system_c_when_matching(self):
        profile, closure, route = partial_constant_missing_row_profile_route_audits()
        identity_routing = universal_continuation_identity_routing_audit(
            one_color_identity_interval()
        )
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )
        witness = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            ((identity_routing.routing.routed_edges[0], endpoint),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=closure,
            missing_triangular_partial_constant_continuation_route=route,
            universal_continuation_identity_routing=identity_routing,
            universal_continuation_endpoint_witness=witness,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_universal_continuation_endpoint_witness",
        )
        self.assertTrue(audit.system_c_closed_by_endpoint_witness)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("universal_continuation_endpoint_witness_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("universal_continuation_endpoint_missing_edges", ()),
            audit.finite_obstruction_data,
        )

    def test_continuation_symmetric_endpoint_fork_closes_system_c_when_matching(
        self,
    ):
        profile, closure, route = partial_constant_missing_row_profile_route_audits()
        identity_routing = universal_continuation_identity_routing_audit(
            one_color_identity_interval()
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )
        fork = universal_continuation_identity_symmetric_endpoint_fork_audit(
            identity_routing,
            endpoint_family,
            identity_routing.routing.routed_edges,
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=closure,
            missing_triangular_partial_constant_continuation_route=route,
            universal_continuation_identity_routing=identity_routing,
            universal_continuation_symmetric_endpoint_fork=fork,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_universal_continuation_symmetric_endpoint_fork",
        )
        self.assertTrue(audit.system_c_closed_by_symmetric_endpoint_fork)
        self.assertTrue(audit.system_c_closed_by_routed_certificate)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("universal_continuation_symmetric_fork_cutoff_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("universal_continuation_symmetric_fork_missing_edges", ()),
            audit.finite_obstruction_data,
        )

    def test_mixed_unit_endpoint_witness_closes_system_m_when_matching(self):
        profile, routing = coordinate_unit_mixed_context_route_audits()
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )
        witness = mixed_unit_context_endpoint_witness_audit(
            routing,
            ((("*", "*", "left"), endpoint),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_coordinate_unit_routing=routing,
            mixed_unit_context_endpoint_witness=witness,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_mixed_unit_context_endpoint_witness",
        )
        self.assertTrue(audit.system_m_closed_by_endpoint_witness)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("missing_triangular_coordinate_unit_routing_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_unit_endpoint_witness_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_unit_endpoint_missing_context_keys", ()),
            audit.finite_obstruction_data,
        )

    def test_mixed_unit_symmetric_endpoint_fork_closes_system_m_when_matching(self):
        profile, routing = coordinate_unit_mixed_context_route_audits()
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )
        fork = mixed_unit_context_symmetric_endpoint_fork_audit(
            routing,
            endpoint_family,
            (("*", "*", "left"),),
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_coordinate_unit_routing=routing,
            mixed_unit_context_symmetric_endpoint_fork=fork,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_mixed_unit_symmetric_endpoint_fork",
        )
        self.assertTrue(audit.system_m_closed_by_symmetric_endpoint_fork)
        self.assertTrue(audit.system_m_closed_by_routed_certificate)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("mixed_unit_symmetric_fork_cutoff_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_unit_symmetric_fork_missing_context_keys", ()),
            audit.finite_obstruction_data,
        )

    def test_post_linear_routes_constant_map_kernel_to_recovery_when_supplied(self):
        refinement = constant_map_kernel_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        raw = PostLinearRemainingFiniteSystemAudit(refinement)
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
        )

        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                (
                    (("*", "*"), "left_constant_map_universal_kernel"),
                    (("*", "*"), "no_right_triangular_row"),
                ),
            ),
            raw.finite_obstruction_data,
        )
        self.assertEqual(routed.system_name, "system_k_kink_completion_deficit")
        self.assertIn(
            ("live_k_missing_latin_row_defects", ((("*", "*"), "no_right_triangular_row"),)),
            routed.finite_obstruction_data,
        )
        self.assertIn(
            (
                "triangular_constant_kernel_unrouted_universal_rows",
                (),
            ),
            routed.finite_obstruction_data,
        )

    def test_post_linear_proper_latin_defect_closure_closes_system_k(self):
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("proper"),
                ),
            ),
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_triangular_latin_proper_closure",
        )
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertFalse(audit.system_k_active)
        self.assertEqual(audit.live_k_missing_latin_row_defects, ())
        self.assertEqual(audit.active_routed_endpoint_systems, ())
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            (
                "triangular_latin_defect_proper_closure_rows",
                (
                    (
                        "left",
                        "constant_map_kernel",
                        "*",
                        "*",
                        "*",
                        None,
                        (0, 1),
                        "proper",
                    ),
                ),
            ),
            audit.finite_obstruction_data,
        )

    def test_post_linear_reports_combined_recovery_and_continuation_endpoints(self):
        refinement = constant_map_kernel_system_k_refinement()
        profile, partial_closure, partial_route = (
            right_partial_constant_missing_row_profile_route_audits()
        )
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
        )

        self.assertEqual(audit.system_name, "system_uc_routed_endpoint_product")
        self.assertEqual(audit.active_routed_endpoint_systems, ("U", "C"))
        self.assertEqual(audit.unclosed_routed_endpoint_systems, ("U", "C"))
        self.assertTrue(audit.system_u_active)
        self.assertTrue(audit.system_c_active)
        self.assertFalse(audit.system_m_active)
        self.assertIn(
            (
                "recovery_routed_k_missing_latin_row_defects",
                ((("*", "*"), "left_constant_map_universal_kernel"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "continuation_routed_k_missing_latin_row_defects",
                ((("*", "*"), "no_right_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("active_routed_endpoint_systems", ("U", "C")),
            audit.finite_obstruction_data,
        )
        self.assertEqual(
            audit.remaining_obligations,
            (
                "prove each routed triangular recovery endpoint composite lies in V_beta(U_tri)",
                "or upgrade one routed U_tri endpoint miss to a normalized-law sequence",
                "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
            ),
        )

    def test_closed_recovery_endpoint_does_not_hide_unclosed_continuation_endpoint(self):
        interval = one_color_latin_unit_triangular_interval()
        refinement = constant_map_kernel_system_k_refinement()
        profile, partial_closure, partial_route = (
            right_partial_constant_missing_row_profile_route_audits()
        )
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        observer = refinement.triangular_recovery_unit_observer
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity
        endpoint = triangular_recovery_longitude_expression_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
            assignment=(generator, identity),
            expression=((1, 1),),
        )
        witness = triangular_recovery_endpoint_witness_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            ((("*", "*", "left_constant_map_universal_kernel"), endpoint),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
            triangular_recovery_endpoint_witness=witness,
        )

        self.assertEqual(audit.system_name, "system_c_universal_continuation_endpoint")
        self.assertEqual(audit.active_routed_endpoint_systems, ("U", "C"))
        self.assertEqual(audit.unclosed_routed_endpoint_systems, ("C",))
        self.assertTrue(audit.system_u_closed_by_endpoint_witness)
        self.assertFalse(audit.system_c_closed_by_endpoint_witness)
        self.assertTrue(audit.is_current_remaining_finite_system)
        self.assertEqual(
            audit.remaining_obligations,
            (
                "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
            ),
        )

    def test_closed_continuation_and_mixed_product_reports_both_witnesses(self):
        profile, closure, route, coordinate_routing = (
            continuation_and_mixed_context_route_audits()
        )
        identity_routing = universal_continuation_identity_routing_audit(
            one_color_identity_interval()
        )
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )
        continuation_witness = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            ((identity_routing.routing.routed_edges[0], endpoint),),
        )
        mixed_witness = mixed_unit_context_endpoint_witness_audit(
            coordinate_routing,
            ((("*", "*", "right"), endpoint),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            TwoNoTriangularRawKRefinement(),
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=closure,
            missing_triangular_partial_constant_continuation_route=route,
            missing_triangular_coordinate_unit_routing=coordinate_routing,
            universal_continuation_identity_routing=identity_routing,
            universal_continuation_endpoint_witness=continuation_witness,
            mixed_unit_context_endpoint_witness=mixed_witness,
        )

        self.assertEqual(audit.system_name, "closed_by_routed_endpoint_witnesses")
        self.assertEqual(audit.active_routed_endpoint_systems, ("C", "M"))
        self.assertEqual(audit.unclosed_routed_endpoint_systems, ())
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            (
                "continuation_routed_k_missing_latin_row_defects",
                ((("*", "*"), "no_left_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "mixed_context_routed_k_missing_latin_row_defects",
                ((("*", "*"), "no_right_triangular_row"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("universal_continuation_endpoint_witness_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_unit_endpoint_witness_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("mixed_unit_endpoint_missing_context_keys", ()),
            audit.finite_obstruction_data,
        )

    def test_constant_map_kernel_only_route_becomes_system_u_endpoint(self):
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        raw = PostLinearRemainingFiniteSystemAudit(refinement)
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
        )

        self.assertEqual(raw.system_name, "system_k_kink_completion_deficit")
        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                ((("*", "*"), "left_constant_map_universal_kernel"),),
            ),
            raw.finite_obstruction_data,
        )
        self.assertEqual(
            routed.system_name,
            "system_u_triangular_recovery_unit_endpoint",
        )
        self.assertTrue(routed.k_deficits_routed_to_recovery_endpoint)
        self.assertFalse(routed.k_deficits_closed_by_recorded_routing)
        self.assertIn(
            (
                "recovery_routed_k_missing_latin_row_defects",
                ((("*", "*"), "left_constant_map_universal_kernel"),),
            ),
            routed.finite_obstruction_data,
        )
        descriptor = (
            "*",
            "*",
            "L",
            "constant_map_kernel",
            ("*", (0, 1), "universal", "universal"),
        )
        self.assertEqual(routed.universal_k_row_normal_form_domain, (descriptor,))
        self.assertEqual(
            routed.universal_k_seed_classifier_entries,
            (
                (
                    descriptor,
                    ("U", ("*", "*", "left_constant_map_universal_kernel")),
                ),
            ),
        )
        self.assertIn(
            ("live_k_missing_latin_row_defects", ()),
            routed.finite_obstruction_data,
        )
        self.assertEqual(
            routed.remaining_obligations,
            (
                "prove each routed triangular recovery endpoint composite lies in V_beta(U_tri)",
                "or upgrade one routed U_tri endpoint miss to a normalized-law sequence",
            ),
        )

    def test_signed_endpoint_generator_audit_requires_both_signs_and_identities(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        positive_row = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        negative_row = replace(positive_row, sign=-1)
        required_entry_keys = (positive_row.entry_key, negative_row.entry_key)
        incomplete = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row,),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
        )

        self.assertEqual(incomplete.missing_signed_seed_keys, (("U", seed_state, -1),))
        self.assertEqual(incomplete.missing_entry_keys, (negative_row.entry_key,))
        self.assertFalse(incomplete.proves_signed_endpoint_generator_tables)
        self.assertIn("signed_seed_keys_missing", incomplete.failure_reasons)
        self.assertIn("signed_generator_entries_missing", incomplete.failure_reasons)

        unpaired = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
        )

        self.assertFalse(unpaired.proves_signed_endpoint_generator_tables)
        self.assertIn("inverse_pairing_not_verified", unpaired.failure_reasons)

        unpathed = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
        )

        self.assertFalse(unpathed.proves_signed_endpoint_generator_tables)
        self.assertIn("positive_ybe_path_not_verified", unpathed.failure_reasons)

        unfaithful = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
        )

        self.assertFalse(unfaithful.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_faithfulness_not_verified",
            unfaithful.failure_reasons,
        )

        uncounted_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_audit=uncounted_endpoint_residual_action_audit(),
        )

        self.assertTrue(
            uncounted_residual.residual_action_audit.proves_supplied_rows_detector_implication
        )
        self.assertFalse(
            uncounted_residual.residual_action_audit.proves_complete_residual_action_implication
        )
        self.assertFalse(uncounted_residual.residual_faithfulness_proved)
        self.assertFalse(uncounted_residual.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_faithfulness_not_verified",
            uncounted_residual.failure_reasons,
        )

        unscoped_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(unscoped_residual.residual_faithfulness_proved)
        self.assertFalse(unscoped_residual.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_action_scope_missing",
            unscoped_residual.failure_reasons,
        )

        wrong_seed_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "U",
                seed_states=(("U", ("wrong-seed",)),),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(wrong_seed_residual.residual_faithfulness_proved)
        self.assertFalse(wrong_seed_residual.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_action_scope_seed_state_mismatch",
            wrong_seed_residual.failure_reasons,
        )

        duplicate_seed_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "U",
                seed_states=(("U", seed_state), ("U", seed_state)),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(duplicate_seed_residual.residual_faithfulness_proved)
        self.assertFalse(duplicate_seed_residual.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_action_scope_duplicate_seed_states",
            duplicate_seed_residual.failure_reasons,
        )

        malformed_seed_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "U",
                seed_states=(("U", "not_a_tuple_seed_state"),),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(malformed_seed_residual.residual_faithfulness_proved)
        self.assertFalse(malformed_seed_residual.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_action_scope_malformed_seed_states",
            malformed_seed_residual.failure_reasons,
        )

        unhashable_seed_state = ("U", (["not-hashable"],))
        unhashable_seed_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "U",
                seed_states=(unhashable_seed_state,),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(
            unhashable_seed_residual.residual_action_scope.malformed_expected_endpoint_seed_states,
            (unhashable_seed_state,),
        )
        self.assertFalse(unhashable_seed_residual.residual_faithfulness_proved)
        self.assertIn(
            "residual_action_scope_malformed_seed_states",
            unhashable_seed_residual.failure_reasons,
        )

        unknown_family_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "Z",
                seed_states=(("U", seed_state),),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(unknown_family_residual.residual_faithfulness_proved)
        self.assertIn(
            "residual_action_scope_unknown_endpoint_families",
            unknown_family_residual.failure_reasons,
        )

        braid_index_scoped_residual = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=replace(
                trivial_endpoint_residual_action_scope(
                    "U",
                    seed_states=(("U", seed_state),),
                ),
                scope_dependencies=("braid_index",),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(braid_index_scoped_residual.residual_faithfulness_proved)
        self.assertIn(
            "residual_action_scope_forbidden_dependencies",
            braid_index_scoped_residual.failure_reasons,
        )

        bare_flag = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_faithfulness_verified=True,
        )

        self.assertFalse(bare_flag.residual_faithfulness_proved)
        self.assertFalse(bare_flag.proves_signed_endpoint_generator_tables)
        self.assertIn("residual_faithfulness_not_verified", bare_flag.failure_reasons)

        theorem = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            expected_residual_row_count=1,
            covered_residual_row_count=1,
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(("U", seed_state),),
            covered_endpoint_seed_states=(("U", seed_state),),
            expected_residual_input_tuples=(("p",),),
            covered_residual_input_tuples=(("p",),),
            residual_rows=trivial_residual_faithfulness_rows(
                "U",
                seed_states=(("U", seed_state),),
                input_tuples=(("p",),),
            ),
        )
        theorem_complete = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                required_entry_keys
            ),
            residual_faithfulness_theorem=theorem,
        )

        self.assertTrue(theorem.proves_residual_faithfulness)
        self.assertTrue(theorem_complete.residual_faithfulness_proved)
        self.assertTrue(theorem_complete.proves_signed_endpoint_generator_tables)

        theorem_without_group_table = replace(theorem_complete, endpoint_group=None)
        self.assertFalse(theorem_without_group_table.signed_finite_row_checks_proved)
        self.assertFalse(
            theorem_without_group_table.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "finite_signed_row_checks_missing_endpoint_group",
            theorem_without_group_table.failure_reasons,
        )

        theorem_without_input_domain = replace(
            theorem,
            expected_residual_input_tuples=(),
            covered_residual_input_tuples=(),
        )
        self.assertFalse(theorem_without_input_domain.proves_residual_faithfulness)
        self.assertIn(
            "residual_faithfulness_input_tuple_domain_missing",
            theorem_without_input_domain.failure_reasons,
        )

        theorem_without_rows = replace(theorem, residual_rows=())
        self.assertFalse(theorem_without_rows.proves_residual_faithfulness)
        self.assertIn(
            "residual_faithfulness_rows_missing",
            theorem_without_rows.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_implication_not_proved",
            theorem_without_rows.failure_reasons,
        )

        theorem_with_braid_index_row = replace(
            theorem,
            residual_rows=(
                replace(theorem.residual_rows[0], dependencies=("braid_index",)),
            ),
        )
        self.assertFalse(theorem_with_braid_index_row.proves_residual_faithfulness)
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_braid_index_row.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_not_braid_index_independent",
            theorem_with_braid_index_row.failure_reasons,
        )

        theorem_with_duplicate_channel_key = replace(
            theorem,
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_channel_keys=(("U", seed_state, "endpoint"),) * 2,
                ),
            ),
        )
        self.assertFalse(
            theorem_with_duplicate_channel_key.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_duplicate_channel_key.failure_reasons,
        )

        theorem_with_malformed_channel_key = replace(
            theorem,
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_channel_keys=("bad_channel",),
                ),
            ),
        )
        self.assertFalse(
            theorem_with_malformed_channel_key.proves_residual_faithfulness
        )
        self.assertEqual(
            theorem_with_malformed_channel_key.malformed_residual_row_endpoint_channel_keys,
            ((("p",), ("bad_channel",)),),
        )
        self.assertIn(
            "residual_faithfulness_malformed_endpoint_channel_keys",
            theorem_with_malformed_channel_key.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_malformed_channel_key.failure_reasons,
        )

        theorem_with_wrong_channel_seed = replace(
            theorem,
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_channel_keys=(
                        ("U", ("wrong_seed_state",), "endpoint_channel"),
                    ),
                ),
            ),
        )
        self.assertFalse(
            theorem_with_wrong_channel_seed.proves_residual_faithfulness
        )
        self.assertEqual(
            theorem_with_wrong_channel_seed.residual_row_endpoint_channel_seed_mismatches,
            (
                (
                    ("p",),
                    (("U", ("wrong_seed_state",)),),
                    (("U", seed_state),),
                ),
            ),
        )
        self.assertIn(
            "residual_faithfulness_endpoint_channel_seed_mismatch",
            theorem_with_wrong_channel_seed.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_wrong_channel_seed.failure_reasons,
        )

        theorem_with_bad_tuple_arity = replace(
            theorem,
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    output_tuple=("p", "extra"),
                ),
            ),
        )
        self.assertFalse(theorem_with_bad_tuple_arity.proves_residual_faithfulness)
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_bad_tuple_arity.failure_reasons,
        )

        theorem_with_family_seed_mismatch = replace(
            theorem,
            active_endpoint_families=("U", "C"),
            covered_endpoint_families=("U", "C"),
            expected_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            covered_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            expected_residual_rows_by_family=(("U", 1), ("C", 1)),
            covered_residual_rows_by_family=(("U", 1), ("C", 1)),
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_families=("U", "C"),
                    endpoint_seed_states=(("U", seed_state),),
                ),
            ),
        )
        self.assertFalse(
            theorem_with_family_seed_mismatch.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_family_seed_mismatch.failure_reasons,
        )

        theorem_with_family_count_row_mismatch = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U", "C"),
            covered_endpoint_families=("U", "C"),
            expected_residual_row_count=1,
            covered_residual_row_count=1,
            expected_residual_rows_by_family=(("U", 1), ("C", 0)),
            covered_residual_rows_by_family=(("U", 1), ("C", 0)),
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            covered_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            expected_residual_input_tuples=(("p",),),
            covered_residual_input_tuples=(("p",),),
            residual_rows=trivial_residual_faithfulness_rows(
                "U",
                "C",
                seed_states=(
                    ("U", seed_state),
                    ("C", ("*", "*", "left")),
                ),
                input_tuples=(("p",),),
            ),
        )
        self.assertEqual(
            theorem_with_family_count_row_mismatch.actual_residual_rows_by_family,
            (("C", 1), ("U", 1)),
        )
        self.assertFalse(
            theorem_with_family_count_row_mismatch.residual_family_row_counts_match_rows
        )
        self.assertFalse(
            theorem_with_family_count_row_mismatch.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_family_row_counts_do_not_match_rows",
            theorem_with_family_count_row_mismatch.failure_reasons,
        )

        theorem_with_malformed_seed_state = replace(
            theorem,
            expected_endpoint_seed_states=(("U", "not_a_tuple_seed_state"),),
            covered_endpoint_seed_states=(("U", "not_a_tuple_seed_state"),),
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_seed_states=(("U", "not_a_tuple_seed_state"),),
                ),
            ),
        )
        self.assertFalse(
            theorem_with_malformed_seed_state.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_malformed_seed_states",
            theorem_with_malformed_seed_state.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_malformed_seed_state.failure_reasons,
        )

        theorem_with_unhashable_seed_state = replace(
            theorem,
            expected_endpoint_seed_states=(unhashable_seed_state,),
            covered_endpoint_seed_states=(unhashable_seed_state,),
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_seed_states=(unhashable_seed_state,),
                    endpoint_channel_keys=(
                        ("U", (["not-hashable"],), "endpoint_channel"),
                    ),
                ),
            ),
        )
        self.assertEqual(
            theorem_with_unhashable_seed_state.malformed_expected_endpoint_seed_states,
            (unhashable_seed_state,),
        )
        self.assertFalse(
            theorem_with_unhashable_seed_state.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_malformed_seed_states",
            theorem_with_unhashable_seed_state.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_unhashable_seed_state.failure_reasons,
        )

        unhashable_input_tuple = (["p"],)
        theorem_with_unhashable_input_tuple = replace(
            theorem,
            expected_residual_input_tuples=(unhashable_input_tuple,),
            covered_residual_input_tuples=(unhashable_input_tuple,),
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    input_tuple=unhashable_input_tuple,
                    output_tuple=unhashable_input_tuple,
                    identity_endpoint_output_tuple=unhashable_input_tuple,
                ),
            ),
        )
        self.assertEqual(
            theorem_with_unhashable_input_tuple.missing_residual_input_tuples,
            (),
        )
        self.assertEqual(
            theorem_with_unhashable_input_tuple.extra_residual_input_tuples,
            (),
        )
        self.assertEqual(
            theorem_with_unhashable_input_tuple.missing_residual_rows_for_input_tuples,
            (),
        )
        self.assertEqual(
            theorem_with_unhashable_input_tuple.extra_residual_rows_for_input_tuples,
            (),
        )
        self.assertTrue(
            theorem_with_unhashable_input_tuple.proves_residual_faithfulness
        )

        theorem_with_unknown_family = replace(
            theorem,
            active_endpoint_families=("Z",),
            covered_endpoint_families=("Z",),
            residual_rows=(
                replace(
                    theorem.residual_rows[0],
                    endpoint_families=("Z",),
                ),
            ),
        )
        self.assertFalse(theorem_with_unknown_family.proves_residual_faithfulness)
        self.assertIn(
            "residual_faithfulness_unknown_endpoint_families",
            theorem_with_unknown_family.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_invalid_rows",
            theorem_with_unknown_family.failure_reasons,
        )

        theorem_with_malformed_row_count = replace(
            theorem,
            expected_residual_row_count="1",
            covered_residual_row_count=True,
        )
        self.assertFalse(
            theorem_with_malformed_row_count.residual_row_counts_well_formed
        )
        self.assertFalse(
            theorem_with_malformed_row_count.proves_residual_faithfulness
        )
        self.assertEqual(
            theorem_with_malformed_row_count.malformed_residual_row_counts,
            (
                ("expected_residual_row_count", "1"),
                ("covered_residual_row_count", True),
            ),
        )
        self.assertIn(
            "residual_faithfulness_row_count_malformed",
            theorem_with_malformed_row_count.failure_reasons,
        )

        theorem_with_malformed_family_count = replace(
            theorem,
            expected_residual_rows_by_family=(("U", "one"),),
            covered_residual_rows_by_family=(("U", "one"),),
        )
        self.assertFalse(
            theorem_with_malformed_family_count.residual_family_row_counts_nonnegative
        )
        self.assertFalse(
            theorem_with_malformed_family_count.proves_residual_faithfulness
        )
        self.assertEqual(
            theorem_with_malformed_family_count.malformed_residual_family_row_counts,
            (("covered", "U", "one"), ("expected", "U", "one")),
        )
        self.assertIn(
            "residual_faithfulness_family_row_count_malformed",
            theorem_with_malformed_family_count.failure_reasons,
        )

        theorem_with_malformed_family_count_row = replace(
            theorem,
            expected_residual_rows_by_family=(("U", 1, "extra"),),
            covered_residual_rows_by_family=(("U", 1),),
        )
        self.assertFalse(
            theorem_with_malformed_family_count_row.residual_family_row_count_rows_well_formed
        )
        self.assertFalse(
            theorem_with_malformed_family_count_row.proves_residual_faithfulness
        )
        self.assertEqual(
            theorem_with_malformed_family_count_row.malformed_residual_family_row_count_rows,
            (("expected", ("U", 1, "extra")),),
        )
        self.assertIn(
            "residual_faithfulness_family_row_count_malformed_rows",
            theorem_with_malformed_family_count_row.failure_reasons,
        )

        rowwise_only = replace(theorem_complete, telescoping_detector_audit=None)
        self.assertTrue(rowwise_only.signed_two_strand_base_verified)
        self.assertTrue(rowwise_only.artin_homomorphism_update_verified)
        self.assertFalse(rowwise_only.telescoping_detector_proved)
        self.assertFalse(rowwise_only.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "telescoping_detector_audit_missing",
            rowwise_only.failure_reasons,
        )

        unfixed_tracks = replace(
            theorem_complete,
            telescoping_detector_audit=UniversalKTelescopingDetectorAudit(
                expected_entry_keys=required_entry_keys,
                covered_entry_keys=required_entry_keys,
                telescoping_identity_verified=True,
                terminal_readout_longitudes_verified=True,
                initial_readout_normalized=True,
                braid_index_independent=True,
            ),
        )
        self.assertFalse(unfixed_tracks.telescoping_detector_proved)
        self.assertFalse(unfixed_tracks.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "fixed_detector_tracks_not_supplied",
            unfixed_tracks.failure_reasons,
        )
        self.assertIn(
            "detector_tracks_not_fixed_before_braid",
            unfixed_tracks.failure_reasons,
        )
        self.assertIn(
            "detector_track_initialization_rows_not_exact",
            unfixed_tracks.failure_reasons,
        )
        self.assertIn(
            "artin_detector_recurrence_not_verified",
            unfixed_tracks.failure_reasons,
        )

        malformed_track_count = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_counts_by_family=(("U", "one"),),
                detector_track_count="one",
            ),
        )
        malformed_track_count_audit = (
            malformed_track_count.telescoping_detector_audit
        )
        self.assertFalse(
            malformed_track_count_audit.detector_track_count_rows_well_formed
        )
        self.assertFalse(malformed_track_count.telescoping_detector_proved)
        self.assertIn(
            "detector_track_count_rows_malformed",
            malformed_track_count.failure_reasons,
        )
        self.assertIn(
            "detector_track_count_nonpositive_or_noninteger",
            malformed_track_count.failure_reasons,
        )

        malformed_track_count_row = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_counts_by_family=(("U", 1, "extra"),),
                detector_track_count=1,
            ),
        )
        malformed_track_count_row_audit = (
            malformed_track_count_row.telescoping_detector_audit
        )
        self.assertEqual(
            malformed_track_count_row_audit.malformed_detector_track_count_rows,
            (("U", 1, "extra"),),
        )
        self.assertFalse(
            malformed_track_count_row_audit.detector_track_count_rows_well_formed
        )
        self.assertFalse(malformed_track_count_row.telescoping_detector_proved)
        self.assertIn(
            "detector_track_count_malformed_rows",
            malformed_track_count_row.failure_reasons,
        )
        self.assertIn(
            "detector_track_count_rows_malformed",
            malformed_track_count_row.failure_reasons,
        )

        malformed_track_index = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index="0",
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=((("A", 0, 0), 0),),
                    ),
                ),
            ),
        )
        self.assertFalse(malformed_track_index.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_rows_not_exact",
            malformed_track_index.failure_reasons,
        )
        self.assertIn(
            "detector_track_initialization_invalid_rows",
            malformed_track_index.failure_reasons,
        )

        malformed_track_initialization_row = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(("not", "a_track_row"),),
            ),
        )
        malformed_track_initialization_audit = (
            malformed_track_initialization_row.telescoping_detector_audit
        )
        self.assertEqual(
            malformed_track_initialization_audit.malformed_detector_track_initialization_rows,
            (("not", "a_track_row"),),
        )
        self.assertFalse(
            malformed_track_initialization_audit.detector_track_initialization_rows_exact
        )
        self.assertFalse(malformed_track_initialization_row.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_malformed_rows",
            malformed_track_initialization_row.failure_reasons,
        )

        braid_word_dependent_track = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="search_after_braid_word",
                        dependencies=("braid_word",),
                        local_assignment_template=((("A", 0, 0), 0),),
                    ),
                ),
            ),
        )
        self.assertFalse(braid_word_dependent_track.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_invalid_rows",
            braid_word_dependent_track.failure_reasons,
        )
        self.assertIn(
            "detector_track_initialization_depends_on_braid",
            braid_word_dependent_track.failure_reasons,
        )
        self.assertIn(
            "detector_tracks_not_fixed_before_braid",
            braid_word_dependent_track.failure_reasons,
        )

        invalid_track_template = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=(
                            (("U", 0, 0), 0),
                            (("A", 0, 1), 99),
                        ),
                    ),
                ),
            ),
        )
        self.assertFalse(invalid_track_template.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_invalid_templates",
            invalid_track_template.failure_reasons,
        )
        self.assertNotIn(
            "detector_tracks_not_fixed_before_braid",
            invalid_track_template.failure_reasons,
        )
        invalid_template_audit = invalid_track_template.telescoping_detector_audit
        self.assertTrue(
            invalid_template_audit.detector_track_initializations_fixed_before_braid
        )
        invalid_template_failures = (
            invalid_template_audit.detector_track_initialization_template_failures
        )
        self.assertIn(
            "detector_track_assignment_not_raw_variable",
            tuple(failure[1] for failure in invalid_template_failures),
        )
        self.assertIn(
            "detector_track_assignment_value_outside_group",
            tuple(failure[1] for failure in invalid_template_failures),
        )

        unhashable_track_template = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=((["A", 0, 0], 0),),
                    ),
                ),
            ),
        )
        self.assertFalse(unhashable_track_template.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_invalid_templates",
            unhashable_track_template.failure_reasons,
        )
        self.assertIn(
            "invalid_detector_track_assignment_variable",
            tuple(
                failure[1]
                for failure in (
                    unhashable_track_template.telescoping_detector_audit
                    .detector_track_initialization_template_failures
                )
            ),
        )

        malformed_track_assignment = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=("not_an_assignment_row",),
                    ),
                ),
            ),
        )
        self.assertFalse(malformed_track_assignment.telescoping_detector_proved)
        self.assertIn(
            "detector_track_initialization_invalid_templates",
            malformed_track_assignment.failure_reasons,
        )
        self.assertIn(
            "malformed_detector_track_assignment",
            tuple(
                failure[1]
                for failure in (
                    malformed_track_assignment.telescoping_detector_audit
                    .detector_track_initialization_template_failures
                )
            ),
        )

        tautological_potential = replace(
            theorem_complete,
            telescoping_detector_audit=UniversalKTelescopingDetectorAudit(
                expected_entry_keys=required_entry_keys,
                covered_entry_keys=required_entry_keys,
                expected_endpoint_seed_states=(("U", seed_state),),
                covered_endpoint_seed_states=(("U", seed_state),),
                detector_track_counts_by_family=(("U", 1),),
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=((("A", 0, 0), 0),),
                    ),
                ),
                expected_word_potential_seed_states=(("U", seed_state),),
                covered_word_potential_seed_states=(("U", seed_state),),
                detector_track_count=1,
                detector_tracks_fixed_before_braid=True,
                detector_track_initialization_verified=True,
                artin_detector_recurrence_verified=True,
                telescoping_identity_verified=True,
                terminal_readout_longitudes_verified=True,
                initial_readout_normalized=True,
                braid_index_independent=True,
            ),
        )
        self.assertFalse(tautological_potential.telescoping_detector_proved)
        self.assertFalse(
            tautological_potential.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "word_potential_uses_raw_assignment_variables",
            tautological_potential.failure_reasons,
        )
        self.assertIn(
            "word_potential_artin_substitution_not_verified",
            tautological_potential.failure_reasons,
        )
        self.assertIn(
            "word_potential_identity_not_verified",
            tautological_potential.failure_reasons,
        )

        word_potential_certificate = (
            theorem_complete.telescoping_detector_audit.word_potential_certificate
        )
        missing_initial_normalization = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                word_potential_certificate=replace(
                    word_potential_certificate,
                    normalized_seed_states=(),
                ),
            ),
        )
        self.assertFalse(
            missing_initial_normalization.word_potential_initial_seed_states_normalized
        )
        self.assertFalse(missing_initial_normalization.telescoping_detector_proved)
        self.assertFalse(
            missing_initial_normalization.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "word_potential_initial_seed_states_not_normalized",
            missing_initial_normalization.failure_reasons,
        )

        out_of_scope_word = ((("U", 7, 0), 1), (("U", 7, 0), -1))

        def out_of_scope_substitution(sign):
            if sign == 1:
                return (
                    (
                        ("U", 7, 0),
                        (
                            (("U", 7, 0), 1),
                            (("A", 7, 0), 1),
                            (("U", 7, 0), -1),
                            (("U", 7, 1), 1),
                        ),
                    ),
                )
            return ((("U", 7, 0), ((("U", 7, 1), 1),)),)

        out_of_scope_tracks = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                word_potential_certificate=replace(
                    word_potential_certificate,
                    templates=((("U", seed_state), out_of_scope_word),),
                    identity_rows=tuple(
                        UniversalKWordPotentialIdentityRow(
                            entry_key=key,
                            next_seed_state=key[1],
                            endpoint_value=(
                                word_potential_certificate.endpoint_group.identity
                            ),
                            artin_substitution=out_of_scope_substitution(key[2]),
                        )
                        for key in required_entry_keys
                    ),
                ),
            ),
        )
        out_of_scope_audit = out_of_scope_tracks.telescoping_detector_audit
        self.assertFalse(out_of_scope_audit.word_potential_track_scope_verified)
        self.assertFalse(out_of_scope_tracks.telescoping_detector_proved)
        self.assertFalse(out_of_scope_tracks.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "word_potential_track_variables_out_of_scope",
            out_of_scope_tracks.failure_reasons,
        )

        in_scope_word_needing_left_assignment = (
            (("U", 0, 0), 1),
            (("U", 0, 0), -1),
        )

        def left_assignment_substitution(sign):
            if sign == 1:
                return (
                    (
                        ("U", 0, 0),
                        (
                            (("U", 0, 0), 1),
                            (("A", 0, 0), 1),
                            (("U", 0, 0), -1),
                            (("U", 0, 1), 1),
                        ),
                    ),
                )
            return (
                (
                    ("U", 0, 0),
                    ((("U", 0, 1), 1),),
                ),
            )

        missing_raw_assignment = replace(
            theorem_complete,
            telescoping_detector_audit=replace(
                theorem_complete.telescoping_detector_audit,
                detector_track_initialization_rows=(
                    UniversalKDetectorTrackInitializationRow(
                        endpoint_family="U",
                        track_index=0,
                        assignment_rule="constant_identity_from_interval_seed",
                        dependencies=(
                            "interval_data",
                            "routed_seed_state",
                            "strand_index",
                        ),
                        local_assignment_template=((("A", 0, 1), 0),),
                    ),
                ),
                word_potential_certificate=replace(
                    word_potential_certificate,
                    templates=(
                        (
                            ("U", seed_state),
                            in_scope_word_needing_left_assignment,
                        ),
                    ),
                    identity_rows=tuple(
                        UniversalKWordPotentialIdentityRow(
                            entry_key=key,
                            next_seed_state=key[1],
                            endpoint_value=(
                                word_potential_certificate.endpoint_group.identity
                            ),
                            artin_substitution=left_assignment_substitution(key[2]),
                        )
                        for key in required_entry_keys
                    ),
                ),
            ),
        )
        missing_raw_assignment_audit = (
            missing_raw_assignment.telescoping_detector_audit
        )
        self.assertTrue(
            missing_raw_assignment_audit.word_potential_track_scope_verified
        )
        self.assertFalse(
            missing_raw_assignment_audit.word_potential_raw_assignment_scope_verified
        )
        self.assertFalse(missing_raw_assignment.telescoping_detector_proved)
        self.assertFalse(missing_raw_assignment.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "word_potential_raw_assignments_not_initialized",
            missing_raw_assignment.failure_reasons,
        )

        incomplete_theorem = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U", "C"),
            covered_endpoint_families=("U",),
            expected_residual_row_count=None,
            covered_residual_row_count=1,
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            covered_endpoint_seed_states=(("U", seed_state),),
        )
        theorem_missing_scope = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_faithfulness_theorem=incomplete_theorem,
        )

        self.assertFalse(incomplete_theorem.proves_residual_faithfulness)
        self.assertFalse(theorem_missing_scope.residual_faithfulness_proved)
        self.assertIn(
            "residual_faithfulness_expected_row_count_missing",
            theorem_missing_scope.failure_reasons,
        )
        self.assertIn(
            "residual_faithfulness_family_coverage_not_exact",
            theorem_missing_scope.failure_reasons,
        )

        malformed_action_scope_row_count = UniversalKResidualActionScopeAudit(
            active_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            expected_residual_row_count="1",
            covered_residual_row_count=True,
            endpoint_channels_exact=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(("U", seed_state),),
            covered_endpoint_seed_states=(("U", seed_state),),
            scope_dependencies=("interval_data",),
        )
        self.assertFalse(
            malformed_action_scope_row_count.residual_row_counts_well_formed
        )
        self.assertFalse(
            malformed_action_scope_row_count.proves_residual_action_scope
        )
        self.assertEqual(
            malformed_action_scope_row_count.malformed_residual_row_counts,
            (
                ("expected_residual_row_count", "1"),
                ("covered_residual_row_count", True),
            ),
        )
        self.assertIn(
            "residual_action_scope_row_count_malformed",
            malformed_action_scope_row_count.failure_reasons,
        )

        multi_family_theorem_missing_rows = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U", "C"),
            covered_endpoint_families=("U", "C"),
            expected_residual_row_count=2,
            covered_residual_row_count=2,
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            covered_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            expected_residual_input_tuples=(("pU",), ("pC",)),
            covered_residual_input_tuples=(("pU",), ("pC",)),
            residual_rows=(
                *trivial_residual_faithfulness_rows(
                    "U",
                    seed_states=(("U", seed_state),),
                    input_tuples=(("pU",),),
                ),
                *trivial_residual_faithfulness_rows(
                    "C",
                    seed_states=(("C", ("*", "*", "left")),),
                    input_tuples=(("pC",),),
                ),
            ),
        )
        multi_family_theorem = replace(
            multi_family_theorem_missing_rows,
            expected_residual_rows_by_family=(("U", 1), ("C", 1)),
            covered_residual_rows_by_family=(("U", 1), ("C", 1)),
        )

        self.assertFalse(
            multi_family_theorem_missing_rows.proves_residual_faithfulness
        )
        self.assertIn(
            "residual_faithfulness_family_row_counts_missing",
            multi_family_theorem_missing_rows.failure_reasons,
        )
        self.assertTrue(multi_family_theorem.proves_residual_faithfulness)

        malformed_action_scope_family_count = UniversalKResidualActionScopeAudit(
            active_endpoint_families=("U", "C"),
            covered_endpoint_families=("U", "C"),
            expected_residual_row_count=2,
            covered_residual_row_count=2,
            expected_residual_rows_by_family=(("U", 1), ("C", "one")),
            covered_residual_rows_by_family=(("U", 1), ("C", "one")),
            endpoint_channels_exact=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            covered_endpoint_seed_states=(
                ("U", seed_state),
                ("C", ("*", "*", "left")),
            ),
            scope_dependencies=("interval_data",),
        )
        self.assertFalse(
            malformed_action_scope_family_count.residual_family_row_counts_nonnegative
        )
        self.assertFalse(
            malformed_action_scope_family_count.proves_residual_action_scope
        )
        self.assertEqual(
            malformed_action_scope_family_count.malformed_residual_family_row_counts,
            (("covered", "C", "one"), ("expected", "C", "one")),
        )
        self.assertIn(
            "residual_action_scope_family_row_count_malformed",
            malformed_action_scope_family_count.failure_reasons,
        )

        malformed_action_scope_family_count_row = replace(
            malformed_action_scope_family_count,
            expected_residual_rows_by_family=(("U", 1, "extra"),),
            covered_residual_rows_by_family=(("U", 1),),
        )
        self.assertFalse(
            malformed_action_scope_family_count_row.residual_family_row_count_rows_well_formed
        )
        self.assertFalse(
            malformed_action_scope_family_count_row.proves_residual_action_scope
        )
        self.assertEqual(
            malformed_action_scope_family_count_row.malformed_residual_family_row_count_rows,
            (("expected", ("U", 1, "extra")),),
        )
        self.assertIn(
            "residual_action_scope_family_row_count_malformed_rows",
            malformed_action_scope_family_count_row.failure_reasons,
        )

        underived_domain = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                required_entry_keys
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(underived_domain.signed_generator_domain_exact)
        self.assertFalse(underived_domain.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "signed_entry_domain_not_derived_from_interval",
            underived_domain.failure_reasons,
        )

        unverified_finite_checks = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                required_entry_keys
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertTrue(unverified_finite_checks.signed_generator_domain_exact)
        self.assertFalse(
            unverified_finite_checks.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "finite_signed_row_checks_not_derived_from_tables",
            unverified_finite_checks.failure_reasons,
        )

        duplicate_reachable_state = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state), ("U", seed_state)),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(duplicate_reachable_state.signed_generator_domain_exact)
        self.assertFalse(
            duplicate_reachable_state.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "reachable_seed_states_duplicate_entries",
            duplicate_reachable_state.failure_reasons,
        )

        conflicting_kappa = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=(
                seed_entries[0],
                (seed_entries[0][0], ("C", ("*", "*", "left"))),
            ),
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(conflicting_kappa.seed_classifier_is_functional)
        self.assertFalse(conflicting_kappa.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "seed_classifier_conflicting_descriptors",
            conflicting_kappa.failure_reasons,
        )

        invalid_kappa_target = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=((seed_entries[0][0], ("Z", seed_state)),),
            reachable_seed_states=(("Z", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("Z"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "Z",
                seed_states=(("Z", seed_state),),
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(invalid_kappa_target.seed_classifier_targets_known)
        self.assertFalse(invalid_kappa_target.reachable_seed_families_known)
        self.assertFalse(invalid_kappa_target.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "seed_classifier_targets_unknown_endpoint_family",
            invalid_kappa_target.failure_reasons,
        )
        self.assertIn(
            "reachable_seed_states_unknown_endpoint_family",
            invalid_kappa_target.failure_reasons,
        )

        malformed_kappa_entry = ("malformed",)
        unhashable_kappa_target = (
            seed_entries[0][0],
            ("U", (["not-hashable"],)),
        )
        non_tuple_kappa_target = (
            seed_entries[0][0],
            "not_a_seed_target",
        )
        malformed_kappa = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=(
                malformed_kappa_entry,
                unhashable_kappa_target,
                non_tuple_kappa_target,
            ),
            reachable_seed_states=(),
            required_entry_keys=(),
            rows=(),
        )

        self.assertEqual(
            malformed_kappa.malformed_seed_classifier_entries,
            (malformed_kappa_entry,),
        )
        self.assertEqual(
            malformed_kappa.invalid_seed_classifier_targets,
            (unhashable_kappa_target, non_tuple_kappa_target),
        )
        self.assertFalse(malformed_kappa.seed_classifier_is_functional)
        self.assertFalse(malformed_kappa.seed_classifier_targets_known)
        self.assertFalse(malformed_kappa.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "seed_classifier_malformed_entries",
            malformed_kappa.failure_reasons,
        )
        self.assertIn(
            "seed_classifier_targets_unknown_endpoint_family",
            malformed_kappa.failure_reasons,
        )

        complete = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                required_entry_keys
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(complete.missing_signed_seed_keys, ())
        self.assertEqual(complete.missing_entry_keys, ())
        self.assertEqual(complete.extra_signed_seed_keys, ())
        self.assertEqual(complete.extra_entry_keys, ())
        self.assertTrue(complete.signed_generator_domain_exact)
        self.assertTrue(complete.residual_faithfulness_proved)
        self.assertTrue(complete.proves_signed_endpoint_generator_tables)
        self.assertEqual(complete.failure_reasons, ())

    def test_endpoint_monodromy_presentation_enumerates_ucm_contexts(self):
        interval = one_color_identity_interval()
        presentation = universal_k_endpoint_monodromy_presentation(
            interval,
            ("U", "C", "M"),
        )

        self.assertIsInstance(presentation, UniversalKEndpointMonodromyPresentation)
        self.assertTrue(presentation.presentation_is_finite)
        self.assertEqual(presentation.expected_endpoint_families_exact, ("C", "M", "U"))
        self.assertEqual(presentation.context_families, ("C", "M", "U"))
        self.assertEqual(len(presentation.contexts_exact), 12)
        self.assertEqual(len(presentation.adjacent_relations_exact), 24)
        self.assertEqual(len(presentation.far_commutativity_relations_exact), 18)
        self.assertFalse(
            any(
                relation[0][0] == relation[0][1]
                for relation in presentation.far_commutativity_relations_exact
            )
        )
        self.assertEqual(presentation.failure_reasons, ())

    def test_endpoint_monodromy_representation_audit_checks_relations(self):
        context_a = ("U", "*", "*", 0, 0)
        context_b = ("U", "*", "*", 1, 1)
        presentation = UniversalKEndpointMonodromyPresentation(
            expected_endpoint_families=("U",),
            contexts=(context_a, context_b),
            adjacent_relations=(((context_a, context_a, context_a), (context_b, context_b, context_b)),),
        )
        seed_a = ("*", "*", "left_constant_map_universal_kernel", "a")
        seed_b = ("*", "*", "left_constant_map_universal_kernel", "b")
        reachable = (("U", seed_a), ("U", seed_b))
        rows = (
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family="U",
                seed_state=seed_a,
                sign=1,
                left_color="*",
                right_color="*",
                input_left=0,
                input_right=0,
                output_left=0,
                output_right=0,
                next_seed_state=seed_a,
                endpoint_value=0,
            ),
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family="U",
                seed_state=seed_b,
                sign=1,
                left_color="*",
                right_color="*",
                input_left=0,
                input_right=0,
                output_left=0,
                output_right=0,
                next_seed_state=seed_b,
                endpoint_value=0,
            ),
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family="U",
                seed_state=seed_a,
                sign=1,
                left_color="*",
                right_color="*",
                input_left=1,
                input_right=1,
                output_left=1,
                output_right=1,
                next_seed_state=seed_b,
                endpoint_value=0,
            ),
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family="U",
                seed_state=seed_b,
                sign=1,
                left_color="*",
                right_color="*",
                input_left=1,
                input_right=1,
                output_left=1,
                output_right=1,
                next_seed_state=seed_a,
                endpoint_value=0,
            ),
        )

        audit = universal_k_endpoint_monodromy_representation_audit(
            presentation,
            reachable,
            rows,
        )

        self.assertIsInstance(audit, UniversalKEndpointMonodromyRepresentationAudit)
        self.assertEqual(audit.context_map_failures, ())
        self.assertFalse(audit.proves_monodromy_representation)
        self.assertIn(
            "monodromy_adjacent_relation_mismatch",
            tuple(failure[1] for failure in audit.relation_failures),
        )
        self.assertIn(
            "endpoint_monodromy_representation_relation_failures",
            audit.failure_reasons,
        )

    def test_signed_endpoint_audit_uses_explicit_monodromy_representation(self):
        interval = one_color_identity_interval()
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        reachable = (("U", seed_state),)
        seed_entries = ((("*", "*", "L", "constant_map_kernel", ("u",)), ("U", seed_state)),)
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        bad_context = ("U", "*", "*", 0, 0)
        missing_context = ("U", "*", "*", "missing", "missing")
        bad_presentation = UniversalKEndpointMonodromyPresentation(
            expected_endpoint_families=("U",),
            contexts=(bad_context,),
            adjacent_relations=(((bad_context, bad_context, bad_context), (missing_context, missing_context, missing_context)),),
        )
        bad_monodromy = universal_k_endpoint_monodromy_representation_audit(
            bad_presentation,
            reachable,
            rows,
        )

        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses={row.entry_key: () for row in rows},
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
            monodromy_representation_audit=bad_monodromy,
        )

        self.assertFalse(audit.explicit_monodromy_representation_verified)
        self.assertFalse(audit.positive_monodromy_representation_verified)
        self.assertFalse(audit.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "explicit_endpoint_monodromy_representation_not_verified",
            audit.failure_reasons,
        )

    def test_endpoint_observer_builder_forces_signed_rows_from_word_potential(self):
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_key = ("U", seed_state)
        seed_entries = ((("*", "*", "L", "constant_map_kernel", (0, 1)), seed_key),)
        seed_states = (seed_key,)
        required_keys = universal_k_signed_endpoint_required_entry_keys(
            interval,
            seed_states,
        )
        positive_keys = tuple(key for key in required_keys if key[2] == 1)
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((seed_key, ()),),
            identity_rows=tuple(
                UniversalKWordPotentialIdentityRow(
                    entry_key=key,
                    next_seed_state=seed_state,
                    endpoint_value=group.identity,
                    artin_substitution=(),
                )
                for key in positive_keys
            ),
            normalized_seed_states=seed_states,
        )
        detector_rows = (
            UniversalKDetectorTrackInitializationRow(
                endpoint_family="U",
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), group.identity),),
            ),
        )
        residual_theorem = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            expected_residual_row_count=1,
            covered_residual_row_count=1,
            expected_residual_input_tuples=(("p",),),
            covered_residual_input_tuples=(("p",),),
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=seed_states,
            covered_endpoint_seed_states=seed_states,
            residual_rows=trivial_residual_faithfulness_rows(
                "U",
                seed_states=seed_states,
            ),
        )

        build = universal_k_endpoint_observer_build(
            interval,
            seed_entries,
            certificate,
            detector_track_initialization_rows=detector_rows,
            residual_faithfulness_theorem=residual_theorem,
        )

        self.assertIsInstance(build, UniversalKEndpointObserverBuild)
        self.assertEqual(build.reachable_seed_states, seed_states)
        self.assertTrue(build.monodromy_presentation.presentation_is_finite)
        self.assertEqual(build.monodromy_presentation.context_families, ("U",))
        self.assertTrue(
            build.monodromy_representation_audit.proves_monodromy_representation
        )
        self.assertEqual(
            tuple(row.entry_key for row in build.positive_rows),
            positive_keys,
        )
        self.assertEqual(
            set(row.entry_key for row in build.rows),
            set(required_keys),
        )
        self.assertTrue(build.telescoping_detector_audit.proves_telescoping_detector_lift)
        self.assertTrue(build.audit.positive_monodromy_representation_verified)
        self.assertTrue(build.proves_endpoint_observer)

    def test_endpoint_observer_builder_records_all_ucm_active_families(self):
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        seed_entries = tuple(
            (
                ("*", "*", family, "constant_map_kernel", (0, 1)),
                (family, ("*", "*", f"{family}_seed")),
            )
            for family in ("U", "C", "M")
        )
        seed_states = universal_k_signed_endpoint_transition_closure(
            seed_entries,
            (),
        )
        required_keys = universal_k_signed_endpoint_required_entry_keys(
            interval,
            seed_states,
        )
        positive_keys = tuple(key for key in required_keys if key[2] == 1)
        state_by_family = {family: state for family, state in seed_states}
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=tuple((seed_state, ()) for seed_state in seed_states),
            identity_rows=tuple(
                UniversalKWordPotentialIdentityRow(
                    entry_key=key,
                    next_seed_state=state_by_family[key[0]],
                    endpoint_value=group.identity,
                    artin_substitution=(),
                )
                for key in positive_keys
            ),
            normalized_seed_states=seed_states,
        )
        detector_rows = tuple(
            UniversalKDetectorTrackInitializationRow(
                endpoint_family=family,
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), group.identity),),
            )
            for family in ("U", "C", "M")
        )

        build = universal_k_endpoint_observer_build(
            interval,
            seed_entries,
            certificate,
            detector_track_initialization_rows=detector_rows,
        )

        self.assertEqual(build.monodromy_presentation.context_families, ("C", "M", "U"))
        self.assertEqual(len(build.monodromy_presentation.contexts_exact), 12)
        self.assertTrue(build.monodromy_presentation.presentation_is_finite)
        self.assertTrue(
            build.monodromy_representation_audit.proves_monodromy_representation
        )
        self.assertEqual(set(row.entry_key for row in build.rows), set(required_keys))
        self.assertTrue(build.audit.signed_generator_domain_exact)
        self.assertTrue(build.audit.positive_monodromy_representation_verified)
        self.assertFalse(build.proves_endpoint_observer)
        self.assertIn("endpoint_targets_not_fixed", build.audit.failure_reasons)
        self.assertIn("cutoff_readouts_not_exact", build.audit.failure_reasons)
        self.assertIn("residual_faithfulness_not_verified", build.audit.failure_reasons)

    def test_identity_endpoint_observer_constructor_builds_ucm_candidates(self):
        interval = one_color_identity_interval()
        seed_entries = tuple(
            (
                ("*", "*", family, "constant_map_kernel", (0, 1)),
                (family, ("*", "*", f"{family}_seed")),
            )
            for family in ("U", "C", "M")
        )

        family_audit = universal_k_identity_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
        )

        self.assertEqual(
            family_audit.expected_endpoint_families_exact,
            ("C", "M", "U"),
        )
        self.assertEqual(
            family_audit.covered_endpoint_families_exact,
            ("C", "M", "U"),
        )
        self.assertEqual(family_audit.unproved_build_families, ("C", "M", "U"))
        self.assertFalse(family_audit.proves_family_endpoint_observers)
        self.assertIn(
            "endpoint_observer_family_builds_not_proved",
            family_audit.failure_reasons,
        )
        by_family = dict(family_audit.build_rows_exact)
        for family in ("C", "M", "U"):
            build = by_family[family]
            self.assertTrue(
                build.monodromy_representation_audit.proves_monodromy_representation
            )
            self.assertTrue(
                build.telescoping_detector_audit.proves_telescoping_detector_lift
            )
            self.assertTrue(build.audit.endpoint_targets_fixed)
            self.assertFalse(build.proves_endpoint_observer)
            self.assertIn(
                "residual_faithfulness_not_verified",
                build.audit.failure_reasons,
            )
        self.assertTrue(by_family["C"].audit.cutoff_readouts_exact)
        self.assertTrue(by_family["M"].audit.cutoff_readouts_exact)
        self.assertEqual(
            by_family["U"].audit.endpoint_target_audit.endpoint_group_orders,
            (("U", len(triangular_recovery_unit_group(interval).elements)),),
        )

    def test_identity_endpoint_observer_constructor_composes_with_residual_rows(self):
        interval = one_color_identity_interval()
        seed_entries = tuple(
            (
                ("*", "*", family, "constant_map_kernel", (0, 1)),
                (family, ("*", "*", f"{family}_seed")),
            )
            for family in ("U", "C", "M")
        )
        seed_state_by_family = {
            family: seed_state for _descriptor, (family, seed_state) in seed_entries
        }
        residual_theorems = []
        for family in ("U", "C", "M"):
            seed_states = ((family, seed_state_by_family[family]),)
            residual_theorems.append(
                (
                    family,
                    UniversalKResidualFaithfulnessAudit(
                        active_endpoint_families=(family,),
                        covered_endpoint_families=(family,),
                        expected_residual_row_count=1,
                        covered_residual_row_count=1,
                        expected_residual_input_tuples=(("p", family),),
                        covered_residual_input_tuples=(("p", family),),
                        endpoint_channels_exact=True,
                        identity_endpoint_data_forces_residual_identity=True,
                        braid_index_independent=True,
                        product_families_separated=True,
                        expected_endpoint_seed_states=seed_states,
                        covered_endpoint_seed_states=seed_states,
                        residual_rows=trivial_residual_faithfulness_rows(
                            family,
                            seed_states=seed_states,
                            input_tuples=(("p", family),),
                        ),
                    ),
                )
            )
        product_seed_states = tuple(
            (family, seed_state_by_family[family]) for family in ("C", "M", "U")
        )
        product_residual = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("C", "M", "U"),
            covered_endpoint_families=("C", "M", "U"),
            expected_residual_row_count=3,
            covered_residual_row_count=3,
            expected_residual_rows_by_family=(("C", 1), ("M", 1), ("U", 1)),
            covered_residual_rows_by_family=(("C", 1), ("M", 1), ("U", 1)),
            expected_residual_input_tuples=(("p", "C"), ("p", "M"), ("p", "U")),
            covered_residual_input_tuples=(("p", "C"), ("p", "M"), ("p", "U")),
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=product_seed_states,
            covered_endpoint_seed_states=product_seed_states,
            residual_rows=(
                trivial_residual_faithfulness_rows(
                    "C",
                    seed_states=(("C", seed_state_by_family["C"]),),
                    input_tuples=(("p", "C"),),
                )
                + trivial_residual_faithfulness_rows(
                    "M",
                    seed_states=(("M", seed_state_by_family["M"]),),
                    input_tuples=(("p", "M"),),
                )
                + trivial_residual_faithfulness_rows(
                    "U",
                    seed_states=(("U", seed_state_by_family["U"]),),
                    input_tuples=(("p", "U"),),
                )
            ),
        )

        family_audit = universal_k_identity_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
            product_residual_faithfulness_theorem=product_residual,
        )

        self.assertEqual(family_audit.failure_reasons, ())
        self.assertTrue(family_audit.proves_family_endpoint_observers)
        self.assertTrue(family_audit.proves_family_endpoint_product_closure)
        for _family, build in family_audit.build_rows_exact:
            self.assertTrue(build.proves_endpoint_observer)

    def test_strict_identity_residual_faithfulness_closes_identity_candidates(self):
        interval = one_color_identity_interval()
        nonidentity_interval = one_color_latin_unit_triangular_interval()
        seed_entries = tuple(
            (
                ("*", "*", family, "constant_map_kernel", (0, 1)),
                (family, ("*", "*", f"{family}_seed")),
            )
            for family in ("U", "C", "M")
        )
        seed_states = tuple(target for _descriptor, target in seed_entries)

        self.assertTrue(universal_k_interval_has_strict_identity_fibre_action(interval))
        self.assertFalse(
            universal_k_interval_has_strict_identity_fibre_action(
                nonidentity_interval
            )
        )

        strict_residual = universal_k_strict_identity_residual_faithfulness_audit(
            interval,
            seed_states,
        )
        self.assertTrue(strict_residual.proves_residual_faithfulness)
        self.assertEqual(
            strict_residual.expected_residual_rows_by_family,
            (("C", 1), ("M", 1), ("U", 1)),
        )
        self.assertEqual(
            strict_residual.expected_residual_input_tuples,
            (
                ("all_residual_fibre_tuples", "C"),
                ("all_residual_fibre_tuples", "M"),
                ("all_residual_fibre_tuples", "U"),
            ),
        )

        family_audit = universal_k_identity_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            derive_strict_identity_residual_faithfulness=True,
        )
        self.assertEqual(family_audit.failure_reasons, ())
        self.assertTrue(family_audit.proves_family_endpoint_observers)
        self.assertTrue(family_audit.proves_family_endpoint_product_closure)

        nonidentity_family_audit = (
            universal_k_identity_endpoint_observer_builds_by_family(
                nonidentity_interval,
                seed_entries,
                derive_strict_identity_residual_faithfulness=True,
            )
        )
        self.assertFalse(nonidentity_family_audit.proves_family_endpoint_observers)
        self.assertEqual(
            nonidentity_family_audit.unproved_build_families,
            ("C", "M", "U"),
        )
        self.assertIn(
            "endpoint_observer_family_builds_not_proved",
            nonidentity_family_audit.failure_reasons,
        )

    def test_endpoint_observer_builds_by_family_cover_exact_ucm_families(self):
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        seed_entries = tuple(
            (
                ("*", "*", family, "constant_map_kernel", (0, 1)),
                (family, ("*", "*", f"{family}_seed")),
            )
            for family in ("U", "C", "M")
        )
        seed_state_by_family = {
            family: seed_state for _descriptor, (family, seed_state) in seed_entries
        }
        certificates = []
        endpoint_targets = []
        cutoff_readouts = []
        residual_theorems = []
        detector_rows = []
        for family in ("U", "C", "M"):
            seed_states = ((family, seed_state_by_family[family]),)
            keys = universal_k_signed_endpoint_required_entry_keys(interval, seed_states)
            positive_keys = tuple(key for key in keys if key[2] == 1)
            certificates.append(
                (
                    family,
                    UniversalKWordPotentialCertificate(
                        endpoint_group=group,
                        templates=((seed_states[0], ()),),
                        identity_rows=tuple(
                            UniversalKWordPotentialIdentityRow(
                                entry_key=key,
                                next_seed_state=seed_state_by_family[family],
                                endpoint_value=group.identity,
                                artin_substitution=(),
                            )
                            for key in positive_keys
                        ),
                        normalized_seed_states=seed_states,
                    ),
                )
            )
            detector_rows.append(
                UniversalKDetectorTrackInitializationRow(
                    endpoint_family=family,
                    track_index=0,
                    assignment_rule="constant_identity_from_interval_seed",
                    dependencies=("interval_data", "routed_seed_state", "strand_index"),
                    local_assignment_template=((("A", 0, 0), group.identity),),
                )
            )
            if family == "U":
                endpoint_targets.append((family, trivial_endpoint_target_audit(family)))
            else:
                endpoint_targets.append(
                    (
                        family,
                        UniversalKEndpointTargetAudit(
                            expected_endpoint_families=(family,),
                            covered_endpoint_families=(family,),
                            cutoff_degrees=((family, 2),),
                            braid_index_independent=True,
                            product_families_separated=True,
                        ),
                    )
                )
                cutoff_readouts.append(
                    (family, trivial_cutoff_readout_audit(seed_states, degree=2))
                )
            residual_theorems.append(
                (
                    family,
                    UniversalKResidualFaithfulnessAudit(
                        active_endpoint_families=(family,),
                        covered_endpoint_families=(family,),
                        expected_residual_row_count=1,
                        covered_residual_row_count=1,
                        expected_residual_input_tuples=(("p",),),
                        covered_residual_input_tuples=(("p",),),
                        endpoint_channels_exact=True,
                        identity_endpoint_data_forces_residual_identity=True,
                        braid_index_independent=True,
                        product_families_separated=True,
                        expected_endpoint_seed_states=seed_states,
                        covered_endpoint_seed_states=seed_states,
                        residual_rows=trivial_residual_faithfulness_rows(
                            family,
                            seed_states=seed_states,
                        ),
                    ),
                )
            )

        family_audit = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
        )

        self.assertIsInstance(
            family_audit,
            UniversalKEndpointObserverFamilyBuildAudit,
        )
        self.assertEqual(
            family_audit.expected_endpoint_families_exact,
            ("C", "M", "U"),
        )
        self.assertEqual(
            family_audit.covered_endpoint_families_exact,
            ("C", "M", "U"),
        )
        self.assertEqual(family_audit.failure_reasons, ())
        self.assertTrue(family_audit.proves_family_endpoint_observers)
        self.assertTrue(family_audit.product_residual_faithfulness_required)
        self.assertFalse(family_audit.product_residual_faithfulness_present)
        self.assertFalse(family_audit.product_residual_faithfulness_proved)
        self.assertFalse(family_audit.proves_family_endpoint_product_closure)
        self.assertEqual(
            family_audit.product_residual_faithfulness_failure_reasons,
            ("endpoint_observer_product_residual_faithfulness_missing",),
        )
        for family, build in family_audit.build_rows_exact:
            self.assertEqual(build.audit.required_endpoint_families, (family,))
            self.assertTrue(build.proves_endpoint_observer)
        wrapper = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            universal_k_endpoint_observer_family_build=family_audit,
        )
        self.assertIn(
            ("endpoint_observer_family_build_present", True),
            wrapper.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_proved", True),
            wrapper.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_expected_families", ("C", "M", "U")),
            wrapper.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_product_closure_proved", False),
            wrapper.routed_endpoint_obstruction_data,
        )

        product_seed_states = tuple(
            (family, seed_state_by_family[family]) for family in ("C", "M", "U")
        )
        product_residual = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("C", "M", "U"),
            covered_endpoint_families=("C", "M", "U"),
            expected_residual_row_count=3,
            covered_residual_row_count=3,
            expected_residual_rows_by_family=(("C", 1), ("M", 1), ("U", 1)),
            covered_residual_rows_by_family=(("C", 1), ("M", 1), ("U", 1)),
            expected_residual_input_tuples=(("p", "C"), ("p", "M"), ("p", "U")),
            covered_residual_input_tuples=(("p", "C"), ("p", "M"), ("p", "U")),
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=product_seed_states,
            covered_endpoint_seed_states=product_seed_states,
            residual_rows=(
                trivial_residual_faithfulness_rows(
                    "C",
                    seed_states=(("C", seed_state_by_family["C"]),),
                    input_tuples=(("p", "C"),),
                )
                + trivial_residual_faithfulness_rows(
                    "M",
                    seed_states=(("M", seed_state_by_family["M"]),),
                    input_tuples=(("p", "M"),),
                )
                + trivial_residual_faithfulness_rows(
                    "U",
                    seed_states=(("U", seed_state_by_family["U"]),),
                    input_tuples=(("p", "U"),),
                )
            ),
        )
        family_audit_with_product = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
            product_residual_faithfulness_theorem=product_residual,
        )

        self.assertTrue(product_residual.proves_residual_faithfulness)
        self.assertTrue(
            family_audit_with_product.product_residual_faithfulness_present
        )
        self.assertTrue(
            family_audit_with_product.product_residual_faithfulness_proved
        )
        self.assertTrue(
            family_audit_with_product.proves_family_endpoint_product_closure
        )

        missing_m = universal_k_endpoint_observer_family_build_audit(
            seed_entries,
            tuple(row for row in family_audit.builds if row[0] != "M"),
        )

        self.assertFalse(missing_m.proves_family_endpoint_observers)
        self.assertEqual(missing_m.missing_build_families, ("M",))
        self.assertIn(
            "endpoint_observer_family_builds_missing_families",
            missing_m.failure_reasons,
        )

        malformed_inputs = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates)
            + (
                ("Z", certificates[0][1]),
                ("M", "not_a_certificate"),
                ("C", certificates[1][1]),
                ("short",),
            ),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
        )

        self.assertFalse(malformed_inputs.proves_family_endpoint_observers)
        self.assertEqual(
            malformed_inputs.invalid_certificate_families,
            ("Z",),
        )
        self.assertEqual(
            malformed_inputs.duplicate_certificate_families,
            ("C",),
        )
        self.assertEqual(
            malformed_inputs.malformed_certificate_rows,
            (("M", "not_a_certificate"), ("short",)),
        )
        self.assertIn(
            "endpoint_observer_family_certificates_malformed_rows",
            malformed_inputs.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_certificates_unknown_families",
            malformed_inputs.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_certificates_duplicate_families",
            malformed_inputs.failure_reasons,
        )

        malformed_seed_classifier_entry = ("bad-kappa-row",)
        unhashable_seed_classifier_target = (
            ("*", "*", "U", "constant_map_kernel", ("bad",)),
            ("U", (["not-hashable"],)),
        )
        invalid_family_seed_classifier_target = (
            ("*", "*", "Z", "constant_map_kernel", ("bad",)),
            ("Z", ("bad",)),
        )
        non_tuple_seed_classifier_target = (
            ("*", "*", "U", "constant_map_kernel", ("non-tuple-target",)),
            "not_a_seed_target",
        )
        malformed_seed_classifier = universal_k_endpoint_observer_family_build_audit(
            (
                malformed_seed_classifier_entry,
                unhashable_seed_classifier_target,
                invalid_family_seed_classifier_target,
                non_tuple_seed_classifier_target,
            ),
            (),
        )

        self.assertFalse(malformed_seed_classifier.seed_classifier_ledger_well_formed)
        self.assertFalse(malformed_seed_classifier.proves_family_endpoint_observers)
        self.assertEqual(
            malformed_seed_classifier.malformed_seed_classifier_entries,
            (malformed_seed_classifier_entry,),
        )
        self.assertEqual(
            malformed_seed_classifier.invalid_seed_classifier_targets,
            (
                unhashable_seed_classifier_target,
                invalid_family_seed_classifier_target,
                non_tuple_seed_classifier_target,
            ),
        )
        self.assertEqual(
            malformed_seed_classifier.expected_endpoint_families_exact,
            (),
        )
        self.assertIn(
            "endpoint_observer_family_seed_classifier_malformed_entries",
            malformed_seed_classifier.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_seed_classifier_invalid_targets",
            malformed_seed_classifier.failure_reasons,
        )
        malformed_seed_classifier_wrapper = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            universal_k_endpoint_observer_family_build=malformed_seed_classifier,
        )
        malformed_seed_classifier_data = dict(
            malformed_seed_classifier_wrapper.routed_endpoint_obstruction_data
        )
        self.assertFalse(
            malformed_seed_classifier_data[
                "endpoint_observer_family_seed_classifier_ledger_well_formed"
            ]
        )
        self.assertEqual(
            malformed_seed_classifier_data[
                "endpoint_observer_family_seed_classifier_malformed_entries"
            ],
            (malformed_seed_classifier_entry,),
        )
        self.assertEqual(
            malformed_seed_classifier_data[
                "endpoint_observer_family_seed_classifier_invalid_targets"
            ],
            (
                unhashable_seed_classifier_target,
                invalid_family_seed_classifier_target,
                non_tuple_seed_classifier_target,
            ),
        )

        bad_auxiliary_ledgers = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets)
            + (
                ("U", endpoint_targets[0][1]),
                ("Z", endpoint_targets[0][1]),
                ("short",),
            ),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts)
            + (
                ("C", cutoff_readouts[0][1]),
                ("U", cutoff_readouts[0][1]),
                ("short",),
            ),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems)
            + (
                ("M", residual_theorems[0][1]),
                ("Z", residual_theorems[0][1]),
                ("short",),
            ),
        )

        self.assertFalse(bad_auxiliary_ledgers.proves_family_endpoint_observers)
        self.assertEqual(bad_auxiliary_ledgers.unproved_build_families, ())
        self.assertEqual(
            bad_auxiliary_ledgers.duplicate_endpoint_target_families,
            ("U",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.invalid_endpoint_target_families,
            ("Z",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.malformed_endpoint_target_rows,
            (("short",),),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.duplicate_cutoff_readout_families,
            ("C",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.extra_cutoff_readout_families,
            ("U",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.malformed_cutoff_readout_rows,
            (("short",),),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.duplicate_residual_theorem_families,
            ("M",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.invalid_residual_theorem_families,
            ("Z",),
        )
        self.assertEqual(
            bad_auxiliary_ledgers.malformed_residual_theorem_rows,
            (("short",),),
        )
        self.assertIn(
            "endpoint_observer_family_endpoint_targets_duplicate_families",
            bad_auxiliary_ledgers.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_cutoff_readouts_extra_families",
            bad_auxiliary_ledgers.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_residual_theorems_unknown_families",
            bad_auxiliary_ledgers.failure_reasons,
        )

        wrong_typed_auxiliary_ledgers = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=(
                ("U", "not_an_endpoint_target_audit"),
            )
            + tuple(endpoint_targets),
            cutoff_readout_audits_by_family=(
                ("C", "not_a_cutoff_readout_audit"),
            )
            + tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=(
                ("M", "not_a_residual_faithfulness_audit"),
            )
            + tuple(residual_theorems),
        )

        self.assertFalse(
            wrong_typed_auxiliary_ledgers.proves_family_endpoint_observers
        )
        self.assertEqual(wrong_typed_auxiliary_ledgers.unproved_build_families, ())
        self.assertEqual(
            wrong_typed_auxiliary_ledgers.malformed_endpoint_target_rows,
            (("U", "not_an_endpoint_target_audit"),),
        )
        self.assertEqual(
            wrong_typed_auxiliary_ledgers.malformed_cutoff_readout_rows,
            (("C", "not_a_cutoff_readout_audit"),),
        )
        self.assertEqual(
            wrong_typed_auxiliary_ledgers.malformed_residual_theorem_rows,
            (("M", "not_a_residual_faithfulness_audit"),),
        )
        self.assertIn(
            "endpoint_observer_family_endpoint_targets_malformed_rows",
            wrong_typed_auxiliary_ledgers.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_cutoff_readouts_malformed_rows",
            wrong_typed_auxiliary_ledgers.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_residual_theorems_malformed_rows",
            wrong_typed_auxiliary_ledgers.failure_reasons,
        )

        bad_detector_track_ledger = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows)
            + (
                UniversalKDetectorTrackInitializationRow(
                    endpoint_family="Z",
                    track_index=0,
                    assignment_rule="constant_identity_from_interval_seed",
                    dependencies=("interval_data", "routed_seed_state"),
                    local_assignment_template=((("A", 0, 0), group.identity),),
                ),
                ("not", "a_track_row"),
            ),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
        )

        self.assertFalse(bad_detector_track_ledger.proves_family_endpoint_observers)
        self.assertEqual(bad_detector_track_ledger.unproved_build_families, ())
        self.assertEqual(
            bad_detector_track_ledger.invalid_family_detector_track_initialization_families,
            ("Z",),
        )
        self.assertEqual(
            bad_detector_track_ledger.malformed_family_detector_track_initialization_rows,
            (("not", "a_track_row"),),
        )
        self.assertIn(
            "endpoint_observer_family_detector_tracks_unknown_families",
            bad_detector_track_ledger.failure_reasons,
        )
        self.assertIn(
            "endpoint_observer_family_detector_tracks_malformed_rows",
            bad_detector_track_ledger.failure_reasons,
        )

        duplicate_detector_track_ledger = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows) + (detector_rows[0],),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
        )

        self.assertFalse(
            duplicate_detector_track_ledger.proves_family_endpoint_observers
        )
        self.assertEqual(
            duplicate_detector_track_ledger.duplicate_family_detector_track_initialization_keys,
            (("U", 0),),
        )
        self.assertIn(
            "endpoint_observer_family_detector_tracks_duplicate_keys",
            duplicate_detector_track_ledger.failure_reasons,
        )

    def test_endpoint_observer_family_build_rechecks_current_kappa_and_interval(self):
        interval = one_color_identity_interval()
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
        )
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_states = (("U", seed_state),)
        keys = universal_k_signed_endpoint_required_entry_keys(interval, seed_states)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        group = cyclic_group(1)
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((seed_states[0], ()),),
            identity_rows=tuple(
                UniversalKWordPotentialIdentityRow(
                    entry_key=key,
                    next_seed_state=seed_state,
                    endpoint_value=group.identity,
                    artin_substitution=(),
                )
                for key in positive_keys
            ),
            normalized_seed_states=seed_states,
        )
        detector_rows = (
            UniversalKDetectorTrackInitializationRow(
                endpoint_family="U",
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), group.identity),),
            ),
        )
        endpoint_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            endpoint_group_orders=(("U", 1),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        residual_faithfulness = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            expected_residual_row_count=1,
            covered_residual_row_count=1,
            expected_residual_input_tuples=(("p",),),
            covered_residual_input_tuples=(("p",),),
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=seed_states,
            covered_endpoint_seed_states=seed_states,
            residual_rows=trivial_residual_faithfulness_rows(
                "U",
                seed_states=seed_states,
            ),
        )
        family_audit = universal_k_endpoint_observer_builds_by_family(
            interval,
            routed.universal_k_seed_classifier_entries,
            (("U", certificate),),
            detector_track_initialization_rows=detector_rows,
            endpoint_target_audits_by_family=(("U", endpoint_target),),
            residual_faithfulness_theorems_by_family=(("U", residual_faithfulness),),
        )
        wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_endpoint_observer_family_build=family_audit,
            universal_k_signed_endpoint_interval=interval,
        )
        wrapper_data = dict(wrapper.finite_obstruction_data)

        self.assertTrue(family_audit.proves_family_endpoint_observers)
        self.assertTrue(wrapper.endpoint_observer_family_build_matches_current_kappa)
        self.assertTrue(
            wrapper.endpoint_observer_family_build_entry_domain_matches_current_interval
        )
        self.assertTrue(wrapper.endpoint_observer_family_build_rows_match_current_interval)
        self.assertTrue(wrapper.endpoint_observer_family_build_closes_current_kappa)
        self.assertEqual(
            wrapper.endpoint_observer_family_build_closed_families,
            ("U",),
        )
        self.assertTrue(wrapper.system_u_closed_by_endpoint_observer_family_build)
        self.assertTrue(wrapper.system_u_closed_by_routed_certificate)
        self.assertTrue(wrapper.all_active_routed_endpoint_systems_closed)
        self.assertEqual(wrapper.unclosed_routed_endpoint_systems, ())
        self.assertEqual(
            wrapper.system_name,
            "closed_by_triangular_recovery_endpoint_observer_family_build",
        )
        self.assertEqual(wrapper.remaining_obligations, ())
        self.assertEqual(
            wrapper_data["endpoint_observer_family_build_closes_current_kappa"],
            True,
        )

        wrong_group = cyclic_group(2)
        wrong_certificate = UniversalKWordPotentialCertificate(
            endpoint_group=wrong_group,
            templates=((seed_states[0], ()),),
            identity_rows=tuple(
                UniversalKWordPotentialIdentityRow(
                    entry_key=key,
                    next_seed_state=seed_state,
                    endpoint_value=wrong_group.identity,
                    artin_substitution=(),
                )
                for key in positive_keys
            ),
            normalized_seed_states=seed_states,
        )
        wrong_detector_rows = (
            UniversalKDetectorTrackInitializationRow(
                endpoint_family="U",
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), wrong_group.identity),),
            ),
        )
        wrong_endpoint_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            endpoint_group_orders=(("U", len(wrong_group.elements)),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        wrong_target_family_audit = universal_k_endpoint_observer_builds_by_family(
            interval,
            routed.universal_k_seed_classifier_entries,
            (("U", wrong_certificate),),
            detector_track_initialization_rows=wrong_detector_rows,
            endpoint_target_audits_by_family=(("U", wrong_endpoint_target),),
            residual_faithfulness_theorems_by_family=(("U", residual_faithfulness),),
        )
        wrong_target_wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_endpoint_observer_family_build=wrong_target_family_audit,
            universal_k_signed_endpoint_interval=interval,
        )
        wrong_target_data = dict(wrong_target_wrapper.finite_obstruction_data)

        self.assertTrue(wrong_target_family_audit.proves_family_endpoint_observers)
        self.assertEqual(wrong_target_wrapper.current_u_tri_endpoint_group_order, 1)
        self.assertEqual(
            wrong_target_wrapper.endpoint_observer_family_build_u_target_group_order,
            2,
        )
        self.assertFalse(
            wrong_target_wrapper.endpoint_observer_family_build_uses_current_u_tri_target
        )
        self.assertFalse(
            wrong_target_wrapper.endpoint_observer_family_build_closes_current_kappa
        )
        self.assertFalse(
            wrong_target_wrapper.system_u_closed_by_endpoint_observer_family_build
        )
        self.assertEqual(wrong_target_wrapper.unclosed_routed_endpoint_systems, ("U",))
        self.assertEqual(
            wrong_target_wrapper.system_name,
            "system_u_triangular_recovery_unit_endpoint",
        )
        self.assertEqual(
            wrong_target_data["endpoint_observer_family_build_current_u_tri_group_order"],
            1,
        )
        self.assertEqual(
            wrong_target_data["endpoint_observer_family_build_u_target_group_order"],
            2,
        )
        self.assertFalse(
            wrong_target_data["endpoint_observer_family_build_uses_current_u_tri_target"]
        )
        self.assertIn(
            "endpoint_observer_family_build_current_u_tri_target_mismatch",
            wrong_target_data["endpoint_observer_family_build_failure_reasons"],
        )

        stale_wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_endpoint_observer_family_build=family_audit,
            universal_k_signed_endpoint_interval=one_color_flip_interval(),
        )
        stale_data = dict(stale_wrapper.finite_obstruction_data)

        self.assertTrue(
            stale_wrapper.endpoint_observer_family_build_matches_current_kappa
        )
        self.assertTrue(
            stale_wrapper.endpoint_observer_family_build_entry_domain_matches_current_interval
        )
        self.assertFalse(
            stale_wrapper.endpoint_observer_family_build_rows_match_current_interval
        )
        self.assertFalse(stale_wrapper.endpoint_observer_family_build_closes_current_kappa)
        self.assertEqual(
            stale_data["endpoint_observer_family_build_closes_current_kappa"],
            False,
        )
        self.assertNotEqual(
            stale_data["endpoint_observer_family_build_current_coordinate_failures"],
            (),
        )

    def test_endpoint_observer_family_build_closes_product_only_with_product_residual(self):
        interval = one_color_identity_interval()
        refinement = constant_map_kernel_system_k_refinement()
        profile, partial_closure, partial_route = (
            right_partial_constant_missing_row_profile_route_audits()
        )
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
        )
        seed_entries = routed.universal_k_seed_classifier_entries
        seed_state_by_family = {
            family: seed_state for _descriptor, (family, seed_state) in seed_entries
        }
        families = tuple(sorted(seed_state_by_family, key=repr))
        group = cyclic_group(1)
        certificates = []
        endpoint_targets = []
        cutoff_readouts = []
        residual_theorems = []
        detector_rows = []
        for family in families:
            seed_states = ((family, seed_state_by_family[family]),)
            keys = universal_k_signed_endpoint_required_entry_keys(interval, seed_states)
            positive_keys = tuple(key for key in keys if key[2] == 1)
            certificates.append(
                (
                    family,
                    UniversalKWordPotentialCertificate(
                        endpoint_group=group,
                        templates=((seed_states[0], ()),),
                        identity_rows=tuple(
                            UniversalKWordPotentialIdentityRow(
                                entry_key=key,
                                next_seed_state=seed_state_by_family[family],
                                endpoint_value=group.identity,
                                artin_substitution=(),
                            )
                            for key in positive_keys
                        ),
                        normalized_seed_states=seed_states,
                    ),
                )
            )
            detector_rows.append(
                UniversalKDetectorTrackInitializationRow(
                    endpoint_family=family,
                    track_index=0,
                    assignment_rule="constant_identity_from_interval_seed",
                    dependencies=("interval_data", "routed_seed_state", "strand_index"),
                    local_assignment_template=((("A", 0, 0), group.identity),),
                )
            )
            if family == "U":
                endpoint_targets.append(
                    (
                        family,
                        UniversalKEndpointTargetAudit(
                            expected_endpoint_families=(family,),
                            covered_endpoint_families=(family,),
                            endpoint_group_orders=((family, 1),),
                            braid_index_independent=True,
                            product_families_separated=True,
                        ),
                    )
                )
            else:
                endpoint_targets.append(
                    (
                        family,
                        UniversalKEndpointTargetAudit(
                            expected_endpoint_families=(family,),
                            covered_endpoint_families=(family,),
                            cutoff_degrees=((family, 2),),
                            braid_index_independent=True,
                            product_families_separated=True,
                        ),
                    )
                )
                cutoff_readouts.append(
                    (family, trivial_cutoff_readout_audit(seed_states, degree=2))
                )
            residual_theorems.append(
                (
                    family,
                    UniversalKResidualFaithfulnessAudit(
                        active_endpoint_families=(family,),
                        covered_endpoint_families=(family,),
                        expected_residual_row_count=1,
                        covered_residual_row_count=1,
                        expected_residual_input_tuples=(("p", family),),
                        covered_residual_input_tuples=(("p", family),),
                        endpoint_channels_exact=True,
                        identity_endpoint_data_forces_residual_identity=True,
                        braid_index_independent=True,
                        product_families_separated=True,
                        expected_endpoint_seed_states=seed_states,
                        covered_endpoint_seed_states=seed_states,
                        residual_rows=trivial_residual_faithfulness_rows(
                            family,
                            seed_states=seed_states,
                            input_tuples=(("p", family),),
                        ),
                    ),
                )
            )

        family_audit = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
        )
        no_product_wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
            universal_k_endpoint_observer_family_build=family_audit,
            universal_k_signed_endpoint_interval=interval,
        )

        self.assertEqual(no_product_wrapper.active_routed_endpoint_systems, ("U", "C"))
        self.assertTrue(family_audit.proves_family_endpoint_observers)
        self.assertFalse(family_audit.proves_family_endpoint_product_closure)
        self.assertFalse(
            no_product_wrapper.endpoint_observer_family_build_closes_current_kappa
        )
        self.assertEqual(no_product_wrapper.unclosed_routed_endpoint_systems, ("U", "C"))

        product_seed_states = tuple(
            (family, seed_state_by_family[family]) for family in families
        )
        product_input_tuples = tuple(("p", family) for family in families)
        product_residual_rows = ()
        for family in families:
            product_residual_rows += trivial_residual_faithfulness_rows(
                family,
                seed_states=((family, seed_state_by_family[family]),),
                input_tuples=(("p", family),),
            )
        product_residual = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=families,
            covered_endpoint_families=families,
            expected_residual_row_count=len(families),
            covered_residual_row_count=len(families),
            expected_residual_rows_by_family=tuple((family, 1) for family in families),
            covered_residual_rows_by_family=tuple((family, 1) for family in families),
            expected_residual_input_tuples=product_input_tuples,
            covered_residual_input_tuples=product_input_tuples,
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
            expected_endpoint_seed_states=product_seed_states,
            covered_endpoint_seed_states=product_seed_states,
            residual_rows=product_residual_rows,
        )
        family_audit_with_product = universal_k_endpoint_observer_builds_by_family(
            interval,
            seed_entries,
            tuple(certificates),
            detector_track_initialization_rows=tuple(detector_rows),
            endpoint_target_audits_by_family=tuple(endpoint_targets),
            cutoff_readout_audits_by_family=tuple(cutoff_readouts),
            residual_faithfulness_theorems_by_family=tuple(residual_theorems),
            product_residual_faithfulness_theorem=product_residual,
        )
        product_wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
            universal_k_endpoint_observer_family_build=family_audit_with_product,
            universal_k_signed_endpoint_interval=interval,
        )

        self.assertTrue(product_residual.proves_residual_faithfulness)
        self.assertTrue(
            family_audit_with_product.proves_family_endpoint_product_closure
        )
        self.assertTrue(product_wrapper.endpoint_observer_family_build_closes_current_kappa)
        self.assertEqual(
            set(product_wrapper.endpoint_observer_family_build_closed_families),
            {"U", "C"},
        )
        self.assertTrue(product_wrapper.system_u_closed_by_endpoint_observer_family_build)
        self.assertTrue(product_wrapper.system_c_closed_by_endpoint_observer_family_build)
        self.assertEqual(product_wrapper.unclosed_routed_endpoint_systems, ())
        self.assertTrue(product_wrapper.all_active_routed_endpoint_systems_closed)
        self.assertEqual(
            product_wrapper.system_name,
            "closed_by_endpoint_observer_family_build",
        )
        self.assertEqual(product_wrapper.remaining_obligations, ())

    def test_endpoint_observer_builder_rejects_omitted_positive_context(self):
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_key = ("U", seed_state)
        seed_entries = ((("*", "*", "L", "constant_map_kernel", (0, 1)), seed_key),)
        required_keys = universal_k_signed_endpoint_required_entry_keys(
            interval,
            (seed_key,),
        )
        positive_keys = tuple(key for key in required_keys if key[2] == 1)
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((seed_key, ()),),
            identity_rows=(
                UniversalKWordPotentialIdentityRow(
                    entry_key=positive_keys[0],
                    next_seed_state=seed_state,
                    endpoint_value=group.identity,
                    artin_substitution=(),
                ),
            ),
            normalized_seed_states=(seed_key,),
        )
        detector_rows = (
            UniversalKDetectorTrackInitializationRow(
                endpoint_family="U",
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), group.identity),),
            ),
        )

        build = universal_k_endpoint_observer_build(
            interval,
            seed_entries,
            certificate,
            detector_track_initialization_rows=detector_rows,
        )

        self.assertFalse(build.proves_endpoint_observer)
        self.assertIn("signed_generator_entries_missing", build.audit.failure_reasons)
        self.assertIn(
            "word_potential_certificate_entry_scope_mismatch",
            build.telescoping_detector_audit.failure_reasons,
        )
        family_audit = universal_k_endpoint_observer_family_build_audit(
            seed_entries,
            (("U", build),),
        )
        wrapper = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            universal_k_endpoint_observer_family_build=family_audit,
        )
        wrapper_data = dict(wrapper.routed_endpoint_obstruction_data)

        self.assertEqual(family_audit.unproved_build_families, ("U",))
        self.assertEqual(
            wrapper_data["endpoint_observer_family_build_row_failure_reasons"],
            (("U", build.audit.failure_reasons),),
        )
        self.assertIn(
            "signed_generator_entries_missing",
            wrapper_data["endpoint_observer_family_build_row_failure_reasons"][0][1],
        )

    def test_endpoint_observer_builder_rejects_malformed_identity_rows(self):
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_key = ("U", seed_state)
        seed_entries = ((("*", "*", "L", "constant_map_kernel", (0, 1)), seed_key),)
        detector_rows = (
            UniversalKDetectorTrackInitializationRow(
                endpoint_family="U",
                track_index=0,
                assignment_rule="constant_identity_from_interval_seed",
                dependencies=("interval_data", "routed_seed_state", "strand_index"),
                local_assignment_template=((("A", 0, 0), group.identity),),
            ),
        )
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((seed_key, ()),),
            identity_rows=(("not", "an_identity_row"),),
            normalized_seed_states=(seed_key,),
        )

        build = universal_k_endpoint_observer_build(
            interval,
            seed_entries,
            certificate,
            detector_track_initialization_rows=detector_rows,
        )

        self.assertEqual(build.positive_rows, ())
        self.assertFalse(build.proves_endpoint_observer)
        self.assertIn("signed_generator_entries_missing", build.audit.failure_reasons)
        self.assertIn(
            "word_potential_certificate_malformed_identity_row_objects",
            build.telescoping_detector_audit.failure_reasons,
        )

    def test_word_potential_certificate_reports_unhashable_keys_without_crashing(self):
        group = cyclic_group(2)
        bad_state = ("U", (["not-hashable"],))
        bad_key = ("U", (["not-hashable"],), 1, "*", "*", 0, 0)
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((bad_state, ()),),
            identity_rows=(
                UniversalKWordPotentialIdentityRow(
                    entry_key=bad_key,
                    next_seed_state=(["not-hashable"],),
                    endpoint_value=group.identity,
                ),
            ),
            normalized_seed_states=(bad_state,),
        )

        self.assertEqual(certificate.template_seed_states_exact, (bad_state,))
        self.assertEqual(certificate.identity_entry_keys_exact, (bad_key,))
        self.assertEqual(certificate.normalized_seed_states_exact, (bad_state,))
        self.assertEqual(certificate.malformed_template_seed_states, (bad_state,))
        self.assertEqual(certificate.malformed_identity_entry_keys, (bad_key,))
        self.assertEqual(certificate.malformed_normalized_seed_states, (bad_state,))
        self.assertFalse(certificate.word_potential_templates_verified)
        self.assertFalse(certificate.artin_substitutions_verified)
        self.assertFalse(certificate.initial_readouts_normalized)
        self.assertEqual(
            universal_k_signed_endpoint_transition_closure(
                ((("descriptor",), bad_state),),
                (),
            ),
            (bad_state,),
        )

        telescoping = UniversalKTelescopingDetectorAudit(
            expected_entry_keys=(bad_key,),
            covered_entry_keys=(bad_key,),
            expected_endpoint_seed_states=(bad_state,),
            covered_endpoint_seed_states=(bad_state,),
            expected_word_potential_seed_states=(bad_state,),
            covered_word_potential_seed_states=(bad_state,),
        )
        self.assertEqual(telescoping.expected_entry_keys_exact, (bad_key,))
        self.assertEqual(telescoping.malformed_expected_entry_keys, (bad_key,))
        self.assertEqual(telescoping.expected_endpoint_seed_states_exact, (bad_state,))
        self.assertEqual(
            telescoping.malformed_expected_endpoint_seed_states,
            (bad_state,),
        )
        self.assertEqual(
            telescoping.malformed_expected_word_potential_seed_states,
            (bad_state,),
        )
        self.assertFalse(telescoping.word_potential_seed_state_ledgers_well_formed)
        self.assertFalse(telescoping.proves_telescoping_detector_lift)

        telescoping_with_bad_certificate = UniversalKTelescopingDetectorAudit(
            expected_entry_keys=(bad_key,),
            covered_entry_keys=(bad_key,),
            expected_endpoint_seed_states=(bad_state,),
            covered_endpoint_seed_states=(bad_state,),
            detector_track_counts_by_family=(("U", 1),),
            expected_word_potential_seed_states=(bad_state,),
            covered_word_potential_seed_states=(bad_state,),
            detector_track_count=1,
            word_potential_certificate=certificate,
        )
        self.assertTrue(
            telescoping_with_bad_certificate.word_potential_seed_state_scope_matches_expected
        )
        self.assertTrue(
            telescoping_with_bad_certificate.word_potential_certificate_template_scope_exact
        )
        self.assertFalse(
            telescoping_with_bad_certificate.word_potential_templates_supplied
        )
        self.assertFalse(
            telescoping_with_bad_certificate.proves_telescoping_detector_lift
        )

    def test_signed_endpoint_positive_rows_must_be_monodromy_permutations(self):
        seed_a = ("*", "*", "left_constant_map_universal_kernel", "a")
        seed_b = ("*", "*", "left_constant_map_universal_kernel", "b")
        seed_entries = (
            (
                ("*", "*", "L", "constant_map_kernel", ("a",)),
                ("U", seed_a),
            ),
            (
                ("*", "*", "L", "constant_map_kernel", ("b",)),
                ("U", seed_b),
            ),
        )
        row_a = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_a,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=0,
            output_left=0,
            output_right=0,
            next_seed_state=seed_a,
            endpoint_value=0,
        )
        row_b = replace(row_a, seed_state=seed_b, next_seed_state=seed_a)
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_a), ("U", seed_b)),
            required_entry_keys=(row_a.entry_key, row_b.entry_key),
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(row_a, row_b),
            endpoint_group=cyclic_group(2),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            far_commutativity_verified=True,
        )

        self.assertFalse(audit.positive_monodromy_representation_verified)
        self.assertIn(
            "monodromy_context_not_permutation",
            tuple(
                failure[1]
                for failure in audit.positive_monodromy_permutation_failures
            ),
        )
        self.assertIn(
            "endpoint_monodromy_not_permutation_representation",
            audit.failure_reasons,
        )

    def test_word_potential_certificate_checks_finite_templates(self):
        group = cyclic_group(2)
        source_state = ("*", "*", "left_constant_map_universal_kernel")
        next_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        source_key = ("U", source_state)
        next_key = ("U", next_state)
        u_left = ("U", 0, 0)
        u_right = ("U", 0, 1)
        entry_key = ("U", source_state, 1, "*", "*", 0, 0)
        good_row = UniversalKWordPotentialIdentityRow(
            entry_key=entry_key,
            next_seed_state=next_state,
            endpoint_value=group.identity,
            artin_substitution=((u_right, ((u_left, 1),)),),
        )
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=(
                (source_key, ((u_left, 1),)),
                (next_key, ((u_right, 1),)),
            ),
            identity_rows=(good_row,),
            normalized_seed_states=(source_key,),
        )

        self.assertTrue(certificate.templates_use_only_current_longitudes)
        self.assertTrue(certificate.artin_substitutions_verified)
        self.assertTrue(certificate.identities_verified)
        self.assertTrue(certificate.coboundary_defects_constant)
        self.assertTrue(certificate.initial_readouts_normalized)

        sound_subset_certificate = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    detector_domain_assignments=(((u_left, group.identity),),),
                    detector_domain_sound=True,
                    detector_domain_soundness_witness=(
                        "reachable_detector_values_enumerated",
                    ),
                ),
            ),
        )
        self.assertTrue(sound_subset_certificate.detector_domains_sound)
        self.assertTrue(sound_subset_certificate.identities_verified)
        self.assertTrue(sound_subset_certificate.coboundary_defects_constant)

        unsound_subset_certificate = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    detector_domain_assignments=(((u_left, group.identity),),),
                ),
            ),
        )
        self.assertFalse(unsound_subset_certificate.detector_domains_sound)
        self.assertFalse(unsound_subset_certificate.identities_verified)
        self.assertFalse(unsound_subset_certificate.coboundary_defects_constant)
        self.assertEqual(
            tuple(
                failure[1]
                for failure in unsound_subset_certificate.detector_domain_failures
            ),
            (
                "detector_domain_subset_not_proved_sound",
                "detector_domain_soundness_witness_missing",
            ),
        )

        wrong_support_certificate = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    detector_domain_assignments=(
                        ((u_left, group.identity), (u_right, group.identity)),
                    ),
                    detector_domain_sound=True,
                    detector_domain_soundness_witness=(
                        "reachable_detector_values_enumerated",
                    ),
                ),
            ),
        )
        self.assertFalse(wrong_support_certificate.detector_domains_sound)
        self.assertIn(
            "detector_domain_assignment_extra_variables",
            tuple(
                failure[1]
                for failure in wrong_support_certificate.detector_domain_failures
            ),
        )

        wrong_endpoint = replace(good_row, endpoint_value=1)
        wrong_endpoint_certificate = replace(
            certificate,
            identity_rows=(wrong_endpoint,),
        )
        self.assertFalse(wrong_endpoint_certificate.identities_verified)
        self.assertFalse(wrong_endpoint_certificate.coboundary_defects_constant)
        self.assertEqual(
            tuple(
                failure[1]
                for failure in wrong_endpoint_certificate.coboundary_defect_failures
            ),
            ("word_potential_identity_mismatch",),
        )

        wrong_substitution = replace(
            good_row,
            artin_substitution=((u_right, ((u_right, 1),)),),
        )
        wrong_substitution_certificate = replace(
            certificate,
            identity_rows=(wrong_substitution,),
        )
        self.assertFalse(wrong_substitution_certificate.artin_substitutions_verified)
        self.assertIn(
            "artin_substitution_image_mismatch",
            tuple(
                failure[1]
                for failure in wrong_substitution_certificate.substitution_failures
            ),
        )

        malformed_sign_row = replace(
            good_row,
            entry_key=("U", source_state, 0, "*", "*", 0, 0),
        )
        malformed_sign_certificate = replace(
            certificate,
            identity_rows=(good_row, malformed_sign_row),
        )
        self.assertEqual(
            malformed_sign_certificate.malformed_identity_entry_keys,
            (malformed_sign_row.entry_key,),
        )
        self.assertFalse(malformed_sign_certificate.artin_substitutions_verified)
        self.assertFalse(malformed_sign_certificate.identities_verified)
        self.assertIn(
            "malformed_signed_entry_key",
            tuple(
                failure[1]
                for failure in malformed_sign_certificate.substitution_failures
            ),
        )

        raw_assignment_template = replace(
            certificate,
            templates=((source_key, ((("A", 0, 0), 1),)),),
        )
        self.assertFalse(
            raw_assignment_template.templates_use_only_current_longitudes
        )
        self.assertEqual(
            raw_assignment_template.raw_assignment_template_variables,
            (("A", 0, 0),),
        )

        malformed_letter_template = replace(
            certificate,
            templates=((source_key, ("not_a_letter",)),),
        )
        self.assertFalse(malformed_letter_template.word_potential_templates_verified)
        self.assertEqual(
            malformed_letter_template.template_word_failures,
            (
                (
                    source_key,
                    "invalid_word_potential_letter",
                    "not_a_letter",
                ),
            ),
        )

        malformed_template_row = replace(
            certificate,
            templates=(("not_a_template_pair",),),
        )
        self.assertEqual(
            malformed_template_row.malformed_template_rows,
            (("not_a_template_pair",),),
        )
        self.assertFalse(malformed_template_row.word_potential_templates_verified)
        self.assertFalse(malformed_template_row.coboundary_defects_constant)
        self.assertIn(
            "malformed_word_potential_template_row",
            tuple(failure[1] for failure in malformed_template_row.coboundary_defect_failures),
        )

        boolean_track_template = replace(
            certificate,
            templates=((source_key, ((("U", True, 0), 1),)),),
        )
        self.assertFalse(boolean_track_template.word_potential_templates_verified)
        self.assertEqual(
            boolean_track_template.invalid_template_variable_failures,
            (
                (
                    source_key,
                    "invalid_word_potential_variable",
                    ("U", True, 0),
                ),
            ),
        )

        boolean_position_template = replace(
            certificate,
            templates=((source_key, ((("U", 0, False), 1),)),),
        )
        self.assertFalse(boolean_position_template.word_potential_templates_verified)
        self.assertEqual(
            boolean_position_template.invalid_template_variable_failures,
            (
                (
                    source_key,
                    "invalid_word_potential_variable",
                    ("U", 0, False),
                ),
            ),
        )

        unhashable_template = replace(
            certificate,
            templates=((source_key, ((["U", 0, 0], 1),)),),
        )
        self.assertFalse(unhashable_template.word_potential_templates_verified)
        self.assertEqual(
            unhashable_template.invalid_template_variable_failures,
            (
                (
                    source_key,
                    "invalid_word_potential_variable",
                    ["U", 0, 0],
                ),
            ),
        )
        self.assertFalse(unhashable_template.initial_readouts_normalized)
        self.assertIn(
            "word_potential_normalization_invalid_template",
            tuple(
                failure[1] for failure in unhashable_template.normalization_failures
            ),
        )

        unhashable_detector_domain = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    detector_domain_assignments=(((["U", 0, 0], group.identity),),),
                    detector_domain_sound=True,
                    detector_domain_soundness_witness=(
                        "reachable_detector_values_enumerated",
                    ),
                ),
            ),
        )
        self.assertFalse(unhashable_detector_domain.detector_domains_sound)
        self.assertIn(
            "detector_domain_assignment_invalid_variable",
            tuple(
                failure[1]
                for failure in unhashable_detector_domain.detector_domain_failures
            ),
        )

        malformed_detector_domain_entry = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    detector_domain_assignments=((("not_a_pair",),),),
                    detector_domain_sound=True,
                    detector_domain_soundness_witness=(
                        "reachable_detector_values_enumerated",
                    ),
                ),
            ),
        )
        self.assertFalse(malformed_detector_domain_entry.detector_domains_sound)
        self.assertIn(
            "detector_domain_assignment_malformed_entry",
            tuple(
                failure[1]
                for failure in (
                    malformed_detector_domain_entry.detector_domain_failures
                )
            ),
        )

        malformed_substitution_row = replace(
            certificate,
            identity_rows=(
                replace(good_row, artin_substitution=("not_a_substitution_row",)),
            ),
        )
        self.assertFalse(malformed_substitution_row.artin_substitutions_verified)
        self.assertIn(
            "malformed_artin_substitution_row",
            tuple(
                failure[1] for failure in malformed_substitution_row.substitution_failures
            ),
        )

        unhashable_substitution_variable = replace(
            certificate,
            identity_rows=(
                replace(
                    good_row,
                    artin_substitution=((["A", 0, 0], ()),),
                ),
            ),
        )
        self.assertFalse(unhashable_substitution_variable.artin_substitutions_verified)
        self.assertIn(
            "invalid_artin_substitution_variable",
            tuple(
                failure[1]
                for failure in unhashable_substitution_variable.substitution_failures
            ),
        )
        telescoping_with_unhashable_substitution = UniversalKTelescopingDetectorAudit(
            expected_entry_keys=(entry_key,),
            covered_entry_keys=(entry_key,),
            expected_endpoint_seed_states=(source_key,),
            covered_endpoint_seed_states=(source_key,),
            detector_track_counts_by_family=(("U", 1),),
            detector_track_initialization_rows=(
                UniversalKDetectorTrackInitializationRow(
                    endpoint_family="U",
                    track_index=0,
                    assignment_rule="constant_identity_from_interval_seed",
                    dependencies=("interval_data", "routed_seed_state", "strand_index"),
                    local_assignment_template=((("A", 0, 0), group.identity),),
                ),
            ),
            expected_word_potential_seed_states=(source_key,),
            covered_word_potential_seed_states=(source_key,),
            detector_track_count=1,
            word_potential_certificate=unhashable_substitution_variable,
        )
        self.assertTrue(
            telescoping_with_unhashable_substitution.word_potential_raw_assignment_scope_verified
        )
        self.assertFalse(
            telescoping_with_unhashable_substitution.word_potential_artin_substitution_proved
        )
        self.assertFalse(
            telescoping_with_unhashable_substitution.proves_telescoping_detector_lift
        )

        malformed_identity_row_object = replace(
            certificate,
            identity_rows=(("not", "an_identity_row"),),
        )
        self.assertEqual(
            malformed_identity_row_object.malformed_identity_rows,
            (("not", "an_identity_row"),),
        )
        self.assertFalse(malformed_identity_row_object.artin_substitutions_verified)
        self.assertFalse(malformed_identity_row_object.identities_verified)
        self.assertFalse(malformed_identity_row_object.coboundary_defects_constant)
        self.assertIn(
            "malformed_word_potential_identity_row_object",
            tuple(
                failure[1]
                for failure in malformed_identity_row_object.coboundary_defect_failures
            ),
        )

    def test_word_potential_certificate_must_match_signed_rows(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = tuple(
            replace(row, endpoint_value=1)
            for row in identity_signed_endpoint_rows(keys)
        )
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=reachable,
            required_entry_keys=keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=rows,
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(audit.telescoping_detector_proved)
        self.assertEqual(
            tuple(
                failure[1]
                for failure in audit.telescoping_detector_signed_row_mismatches
            ),
            (
                "word_potential_row_mismatch",
            ) * len(tuple(key for key in keys if key[2] == 1)),
        )
        self.assertIn(
            "telescoping_detector_signed_row_mismatch",
            audit.failure_reasons,
        )

    def test_word_potential_certificate_scope_is_positive_only(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertEqual(
            telescoping.expected_positive_entry_keys_exact,
            tuple(sorted(set(positive_keys), key=repr)),
        )
        self.assertTrue(audit.telescoping_detector_scope_matches_required)
        self.assertTrue(audit.telescoping_detector_proved)
        self.assertEqual(audit.telescoping_detector_signed_row_mismatches, ())

    def test_negative_word_potential_rows_are_ignored_after_inverse_derivation(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        negative_key = next(key for key in keys if key[2] == -1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        bad_negative_identity = UniversalKWordPotentialIdentityRow(
            entry_key=negative_key,
            next_seed_state=("unreachable",),
            endpoint_value=99,
            artin_substitution=((("U", 99, 0), ((("A", 99, 0), 1),)),),
        )
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                identity_rows=certificate.identity_rows + (bad_negative_identity,),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertTrue(telescoping.word_potential_certificate.identities_verified)
        self.assertTrue(
            telescoping.word_potential_certificate.artin_substitutions_verified
        )
        self.assertTrue(audit.telescoping_detector_proved)
        self.assertEqual(audit.telescoping_detector_signed_row_mismatches, ())

    def test_negative_word_potential_diagnostics_must_stay_in_signed_domain(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        out_of_domain_negative_key = ("U", seed_state, -1, "*", "*", 99, 99)
        out_of_domain_negative_identity = UniversalKWordPotentialIdentityRow(
            entry_key=out_of_domain_negative_key,
            next_seed_state=seed_state,
            endpoint_value=group.identity,
            artin_substitution=(),
        )
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                identity_rows=(
                    certificate.identity_rows + (out_of_domain_negative_identity,)
                ),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertTrue(telescoping.proves_telescoping_detector_lift)
        self.assertTrue(audit.telescoping_detector_scope_matches_required)
        self.assertFalse(
            audit.telescoping_detector_diagnostic_entries_in_signed_domain
        )
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertEqual(
            audit.telescoping_detector_extra_diagnostic_entry_keys,
            (out_of_domain_negative_key,),
        )
        self.assertIn(
            "telescoping_detector_diagnostic_rows_outside_signed_domain",
            audit.failure_reasons,
        )

    def test_malformed_word_potential_identity_rows_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        malformed_identity = UniversalKWordPotentialIdentityRow(
            entry_key=("U", seed_state, 0, "*", "*", 0, 0),
            next_seed_state=seed_state,
            endpoint_value=group.identity,
            artin_substitution=(),
        )
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                identity_rows=certificate.identity_rows + (malformed_identity,),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "word_potential_certificate_malformed_identity_rows",
            audit.failure_reasons,
        )
        self.assertEqual(
            telescoping.word_potential_certificate.malformed_identity_entry_keys,
            (malformed_identity.entry_key,),
        )

    def test_malformed_word_potential_next_states_are_rejected_without_crashing(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        bad_next_state = (["not-hashable"],)
        malformed_next = replace(
            certificate.identity_rows[0],
            next_seed_state=bad_next_state,
        )
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                identity_rows=(malformed_next,) + certificate.identity_rows[1:],
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertEqual(
            telescoping.word_potential_certificate.malformed_identity_next_seed_states,
            ((malformed_next.entry_key, bad_next_state),),
        )
        self.assertFalse(
            telescoping.word_potential_certificate.artin_substitutions_verified
        )
        self.assertFalse(telescoping.word_potential_certificate.identities_verified)
        self.assertIn(
            "malformed_next_seed_state",
            tuple(
                failure[1]
                for failure in telescoping.word_potential_certificate.substitution_failures
            ),
        )
        self.assertIn(
            "malformed_next_seed_state",
            tuple(
                failure[1]
                for failure in telescoping.word_potential_certificate.identity_failures
            ),
        )
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "word_potential_certificate_malformed_next_seed_states",
            audit.failure_reasons,
        )

    def test_short_positive_word_potential_identity_rows_are_rejected(self):
        group = cyclic_group(2)
        source_state = ("*", "*", "left_constant_map_universal_kernel")
        source_key = ("U", source_state)
        malformed_positive_key = ("U", source_state, 1)
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=group,
            templates=((source_key, ()),),
            identity_rows=(
                UniversalKWordPotentialIdentityRow(
                    entry_key=malformed_positive_key,
                    next_seed_state=source_state,
                    endpoint_value=group.identity,
                    artin_substitution=(),
                ),
            ),
            normalized_seed_states=(source_key,),
        )

        self.assertEqual(
            certificate.malformed_identity_entry_keys,
            (malformed_positive_key,),
        )
        self.assertEqual(certificate.positive_identity_entry_keys_exact, ())
        self.assertFalse(certificate.artin_substitutions_verified)
        self.assertIn(
            "malformed_signed_entry_key",
            tuple(failure[1] for failure in certificate.substitution_failures),
        )

    def test_malformed_word_potential_rows_do_not_crash_failure_reasons(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        short_identity = UniversalKWordPotentialIdentityRow(
            entry_key=("U",),
            next_seed_state=seed_state,
            endpoint_value=group.identity,
            artin_substitution=((("U", 0, 0), ((("A", 0, 0), 1),)),),
        )
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                identity_rows=certificate.identity_rows + (short_identity,),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "word_potential_certificate_malformed_identity_rows",
            audit.failure_reasons,
        )
        self.assertEqual(
            telescoping.word_potential_track_scope_failures,
            (),
        )
        self.assertEqual(
            telescoping.word_potential_raw_assignment_scope_failures,
            (),
        )

    def test_malformed_word_potential_template_states_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        malformed_state = ("Z", seed_state)
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                templates=certificate.templates + ((malformed_state, ()),),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(
            telescoping.word_potential_certificate.word_potential_templates_verified
        )
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertEqual(
            telescoping.word_potential_certificate.malformed_template_seed_states,
            (malformed_state,),
        )
        self.assertIn(
            "word_potential_certificate_malformed_template_states",
            audit.failure_reasons,
        )

    def test_malformed_word_potential_normalized_states_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        certificate = telescoping.word_potential_certificate
        malformed_state = ("U", "not_a_tuple_seed_state")
        telescoping = replace(
            telescoping,
            word_potential_certificate=replace(
                certificate,
                normalized_seed_states=(
                    certificate.normalized_seed_states + (malformed_state,)
                ),
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(
            telescoping.word_potential_certificate.initial_readouts_normalized
        )
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertEqual(
            telescoping.word_potential_certificate.malformed_normalized_seed_states,
            (malformed_state,),
        )
        self.assertIn(
            "word_potential_certificate_malformed_normalized_states",
            audit.failure_reasons,
        )

    def test_malformed_word_potential_seed_state_ledgers_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        malformed_state = ("M", "not_a_tuple_seed_state")
        telescoping = replace(
            telescoping,
            expected_word_potential_seed_states=(
                telescoping.expected_word_potential_seed_states + (malformed_state,)
            ),
            covered_word_potential_seed_states=(
                telescoping.covered_word_potential_seed_states + (malformed_state,)
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(telescoping.word_potential_seed_state_ledgers_well_formed)
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn("word_potential_malformed_seed_states", audit.failure_reasons)

    def test_malformed_telescoping_seed_state_ledgers_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        malformed_state = ("Z", seed_state)
        telescoping = replace(
            telescoping,
            expected_endpoint_seed_states=(
                telescoping.expected_endpoint_seed_states + (malformed_state,)
            ),
            covered_endpoint_seed_states=(
                telescoping.covered_endpoint_seed_states + (malformed_state,)
            ),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertFalse(telescoping.endpoint_seed_state_ledgers_well_formed)
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "telescoping_detector_malformed_seed_states",
            audit.failure_reasons,
        )

    def test_malformed_telescoping_entry_ledgers_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        malformed_key = ("U", seed_state, 0, "*", "*", 0, 0)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        telescoping = replace(
            telescoping,
            expected_entry_keys=positive_keys + (malformed_key,),
            covered_entry_keys=positive_keys + (malformed_key,),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertTrue(audit.telescoping_detector_scope_matches_required)
        self.assertFalse(telescoping.entry_ledgers_well_formed)
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "telescoping_detector_malformed_entry_keys",
            audit.failure_reasons,
        )

    def test_short_positive_telescoping_entry_ledgers_are_rejected(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        positive_keys = tuple(key for key in keys if key[2] == 1)
        short_positive_key = ("U", seed_state, 1)
        rows = identity_signed_endpoint_rows(keys)
        group = cyclic_group(2)
        telescoping = trivial_telescoping_detector_audit(
            positive_keys,
            rows=rows,
            endpoint_group=group,
        )
        telescoping = replace(
            telescoping,
            expected_entry_keys=positive_keys + (short_positive_key,),
            covered_entry_keys=positive_keys + (short_positive_key,),
        )
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=group,
            telescoping_detector_audit=telescoping,
        )

        self.assertEqual(
            telescoping.expected_positive_entry_keys_exact,
            tuple(sorted(set(positive_keys), key=repr)),
        )
        self.assertFalse(telescoping.entry_ledgers_well_formed)
        self.assertFalse(audit.telescoping_detector_proved)
        self.assertIn(
            "telescoping_detector_malformed_entry_keys",
            audit.failure_reasons,
        )

    def test_signed_endpoint_audit_requires_family_scoped_endpoint_targets(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        positive_row = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        negative_row = replace(positive_row, sign=-1)
        required_entry_keys = (positive_row.entry_key, negative_row.entry_key)
        bare_endpoint_flag = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(bare_endpoint_flag.endpoint_targets_proved)
        self.assertFalse(bare_endpoint_flag.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "endpoint_target_audit_missing",
            bare_endpoint_flag.failure_reasons,
        )

        wrong_family_target = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("C"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(wrong_family_target.endpoint_target_scope_matches_required)
        self.assertFalse(wrong_family_target.endpoint_targets_proved)
        self.assertIn(
            "endpoint_target_scope_mismatch",
            wrong_family_target.failure_reasons,
        )

        duplicate_target = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(positive_row, negative_row),
            endpoint_targets_fixed=True,
            endpoint_target_audit=UniversalKEndpointTargetAudit(
                expected_endpoint_families=("U",),
                covered_endpoint_families=("U",),
                endpoint_group_orders=(("U", 1), ("U", 1)),
                braid_index_independent=True,
                product_families_separated=True,
            ),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(duplicate_target.endpoint_targets_proved)
        self.assertFalse(duplicate_target.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "endpoint_target_duplicate_target_families",
            duplicate_target.failure_reasons,
        )

        unknown_family_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("Z",),
            covered_endpoint_families=("Z",),
            endpoint_group_orders=(("Z", 1),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        self.assertFalse(unknown_family_target.family_ledgers_known)
        self.assertFalse(unknown_family_target.proves_endpoint_targets)
        self.assertIn(
            "endpoint_target_unknown_families",
            unknown_family_target.failure_reasons,
        )

        malformed_group_order_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            endpoint_group_orders=(("U", "two"),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        self.assertFalse(malformed_group_order_target.target_orders_positive)
        self.assertFalse(malformed_group_order_target.proves_endpoint_targets)
        self.assertEqual(
            malformed_group_order_target.malformed_endpoint_group_orders,
            (("U", "two"),),
        )
        self.assertIn(
            "endpoint_target_malformed_group_order",
            malformed_group_order_target.failure_reasons,
        )

        malformed_group_order_row_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("U",),
            covered_endpoint_families=("U",),
            endpoint_group_orders=(("U", 2, "extra"),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        self.assertFalse(malformed_group_order_row_target.target_size_rows_well_formed)
        self.assertFalse(malformed_group_order_row_target.proves_endpoint_targets)
        self.assertEqual(
            malformed_group_order_row_target.malformed_endpoint_group_order_rows,
            (("U", 2, "extra"),),
        )
        self.assertIn(
            "endpoint_target_malformed_group_order_rows",
            malformed_group_order_row_target.failure_reasons,
        )

        malformed_cutoff_degree_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("M",),
            covered_endpoint_families=("M",),
            cutoff_degrees=(("M", True),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        self.assertFalse(malformed_cutoff_degree_target.cutoff_degrees_positive)
        self.assertFalse(malformed_cutoff_degree_target.proves_endpoint_targets)
        self.assertEqual(
            malformed_cutoff_degree_target.malformed_cutoff_degrees,
            (("M", True),),
        )
        self.assertIn(
            "endpoint_target_malformed_cutoff_degree",
            malformed_cutoff_degree_target.failure_reasons,
        )

        malformed_cutoff_degree_row_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("M",),
            covered_endpoint_families=("M",),
            cutoff_degrees=(("M", 2, "extra"),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        self.assertFalse(malformed_cutoff_degree_row_target.target_size_rows_well_formed)
        self.assertFalse(malformed_cutoff_degree_row_target.proves_endpoint_targets)
        self.assertEqual(
            malformed_cutoff_degree_row_target.malformed_cutoff_degree_rows,
            (("M", 2, "extra"),),
        )
        self.assertIn(
            "endpoint_target_malformed_cutoff_degree_rows",
            malformed_cutoff_degree_row_target.failure_reasons,
        )

    def test_cutoff_readout_rejects_malformed_cutoff_degree_without_crashing(self):
        seed_state = ("C", ("*", "*", "continuation"))
        audit = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=(seed_state,),
            covered_cutoff_seed_states=(seed_state,),
            cutoff_degree="2",
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=seed_state,
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )

        self.assertFalse(audit.cutoff_degree_supplied)
        self.assertFalse(audit.readout_permutations_valid)
        self.assertFalse(audit.proves_exact_cutoff_readouts)
        self.assertIn("cutoff_degree_not_supplied", audit.failure_reasons)
        self.assertEqual(
            audit.invalid_readout_permutation_rows,
            ((seed_state, "cutoff_degree_not_supplied", "2"),),
        )

    def test_signed_endpoint_generator_audit_requires_full_entry_domain(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        first_positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        first_negative = replace(first_positive, sign=-1)
        second_positive = replace(first_positive, input_left=1, input_right=0)
        second_negative = replace(second_positive, sign=-1)
        required_entry_keys = (
            first_positive.entry_key,
            first_negative.entry_key,
            second_positive.entry_key,
            second_negative.entry_key,
        )
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=seed_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=required_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(first_positive, first_negative),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(audit.missing_signed_seed_keys, ())
        self.assertEqual(
            audit.missing_entry_keys,
            (second_negative.entry_key, second_positive.entry_key),
        )
        self.assertFalse(audit.signed_generator_domain_exact)
        self.assertFalse(audit.proves_signed_endpoint_generator_tables)
        self.assertIn("signed_generator_entries_missing", audit.failure_reasons)

    def test_signed_endpoint_entry_domain_is_derived_from_interval_fibres(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()

        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)

        self.assertEqual(len(keys), 8)
        self.assertIn(("U", seed_state, 1, "*", "*", 0, 0), keys)
        self.assertIn(("U", seed_state, -1, "*", "*", 1, 1), keys)

        rows = tuple(
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family=endpoint_family,
                seed_state=state,
                sign=sign,
                left_color=left_color,
                right_color=right_color,
                input_left=input_left,
                input_right=input_right,
                output_left=input_left,
                output_right=input_right,
                next_seed_state=state,
                endpoint_value=0,
            )
            for (
                endpoint_family,
                state,
                sign,
                left_color,
                right_color,
                input_left,
                input_right,
            ) in keys
        )
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=(
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable_seed_states=reachable,
            required_entry_keys=keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=rows[:-1],
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=rows,
                normalized_seed_states=(("U", seed_state),),
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(audit.missing_entry_keys, (keys[-1],))
        self.assertFalse(audit.proves_signed_endpoint_generator_tables)

    def test_signed_endpoint_audit_accepts_transition_reachable_state(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        next_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        reachable = (("U", seed_state), ("U", next_state))
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(
            keys,
            {
                ("U", seed_state): next_state,
                ("U", next_state): seed_state,
            },
        )
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=(
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable_seed_states=reachable,
            required_entry_keys=keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=rows,
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=rows,
                normalized_seed_states=(("U", seed_state),),
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(
            audit.transition_reachable_seed_states,
            tuple(sorted(reachable, key=repr)),
        )
        self.assertEqual(audit.unreachable_declared_seed_states, ())
        self.assertEqual(audit.missing_transition_reachable_seed_states, ())
        self.assertEqual(audit.extra_signed_seed_keys, ())
        self.assertTrue(audit.reachable_seed_state_closure_exact)
        self.assertTrue(audit.proves_signed_endpoint_generator_tables)

        over_normalized = replace(
            audit,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=rows,
            ),
        )
        self.assertFalse(
            over_normalized.word_potential_initial_seed_state_scope_exact
        )
        self.assertFalse(over_normalized.telescoping_detector_proved)
        self.assertFalse(over_normalized.proves_signed_endpoint_generator_tables)
        self.assertEqual(
            over_normalized.extra_initial_normalized_seed_states,
            (("U", next_state),),
        )
        self.assertIn(
            "word_potential_initial_seed_state_scope_not_exact",
            over_normalized.failure_reasons,
        )
        self.assertIn(
            "word_potential_initial_seed_states_extra",
            over_normalized.failure_reasons,
        )

    def test_signed_endpoint_transition_closure_is_derived_from_rows(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        next_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", seed_state),
            ),
        )
        row = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=next_state,
            endpoint_value=0,
        )

        self.assertEqual(
            universal_k_signed_endpoint_transition_closure(seed_entries, (row,)),
            tuple(sorted((("U", seed_state), ("U", next_state)), key=repr)),
        )

    def test_signed_endpoint_audit_rejects_unreachable_declared_state(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        unreachable_state = (
            "*",
            "*",
            "left_constant_map_universal_kernel",
            "unreachable",
        )
        reachable = (("U", seed_state), ("U", unreachable_state))
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        audit = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=(
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable_seed_states=reachable,
            required_entry_keys=keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=rows,
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(
            audit.transition_reachable_seed_states,
            (("U", seed_state),),
        )
        self.assertEqual(
            audit.unreachable_declared_seed_states,
            (("U", unreachable_state),),
        )
        self.assertEqual(audit.extra_signed_seed_keys, ())
        self.assertFalse(audit.reachable_seed_state_closure_exact)
        self.assertFalse(audit.signed_generator_domain_exact)
        self.assertFalse(audit.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "reachable_seed_states_have_unreachable_extras",
            audit.failure_reasons,
        )

    def test_signed_endpoint_generator_factory_derives_finite_checks(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        witnesses = {row.entry_key: () for row in rows}
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            (
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertEqual(audit.required_entry_keys_exact, keys)
        self.assertTrue(audit.coordinate_components_verified)
        self.assertTrue(audit.inverse_pairing_verified)
        self.assertTrue(audit.inverse_cancellation_verified)
        self.assertTrue(audit.positive_ybe_path_verified)
        self.assertTrue(audit.positive_ybe_cocycle_verified)
        self.assertTrue(audit.far_commutativity_verified)
        self.assertTrue(audit.two_strand_witness_domain_exact)
        self.assertTrue(audit.signed_two_strand_base_verified)
        self.assertTrue(audit.artin_homomorphism_update_verified)
        self.assertTrue(audit.telescoping_detector_proved)
        self.assertTrue(audit.endpoint_target_scope_matches_required)
        self.assertTrue(audit.endpoint_targets_proved)
        self.assertEqual(
            audit.endpoint_target_audit.endpoint_group_orders,
            (("U", 2),),
        )
        self.assertEqual(audit.coordinate_component_failures, ())
        self.assertEqual(audit.inverse_pairing_failures, ())
        self.assertEqual(audit.far_commutativity_failures, ())
        self.assertEqual(audit.two_strand_witness_domain_failures, ())
        self.assertEqual(audit.two_strand_base_failures, ())
        self.assertTrue(audit.proves_signed_endpoint_generator_tables)

    def test_signed_endpoint_generator_factory_requires_explicit_multi_family_targets(self):
        u_state = ("*", "*", "left_constant_map_universal_kernel")
        m_state = ("*", "*", "left")
        reachable = (("U", u_state), ("M", m_state))
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "constant_map_kernel",
                    ("*", (0, 1), "universal", "universal"),
                ),
                ("U", u_state),
            ),
            (
                (
                    "*",
                    "*",
                    "L",
                    "coordinate_side_unit_not_triangular",
                    ("left", "right", "colored_ybe"),
                ),
                ("M", m_state),
            ),
        )
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        witnesses = {row.entry_key: () for row in rows}
        cutoff = trivial_cutoff_readout_audit((("M", m_state),))
        residual_scope = trivial_endpoint_residual_action_scope(
            "U",
            "M",
            seed_states=reachable,
        )
        implicit_target = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=residual_scope,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertIsNone(implicit_target.endpoint_target_audit)
        self.assertFalse(implicit_target.endpoint_targets_proved)
        self.assertFalse(implicit_target.residual_action_scope.proves_residual_action_scope)
        self.assertFalse(implicit_target.proves_signed_endpoint_generator_tables)
        self.assertIn("endpoint_target_audit_missing", implicit_target.failure_reasons)
        self.assertIn(
            "residual_action_scope_family_row_counts_missing",
            implicit_target.failure_reasons,
        )

        explicit_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("M", "U"),
            covered_endpoint_families=("M", "U"),
            endpoint_group_orders=(("U", 2),),
            cutoff_degrees=(("M", 2),),
            braid_index_independent=True,
            product_families_separated=True,
        )
        explicit_target_missing_family_rows = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            endpoint_target_audit=explicit_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=residual_scope,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertTrue(explicit_target_missing_family_rows.endpoint_targets_proved)
        self.assertFalse(
            explicit_target_missing_family_rows.residual_faithfulness_proved
        )
        self.assertFalse(
            explicit_target_missing_family_rows.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            "residual_action_scope_family_row_counts_missing",
            explicit_target_missing_family_rows.failure_reasons,
        )

        missing_m_family_rows_scope = trivial_endpoint_residual_action_scope(
            "U",
            "M",
            seed_states=reachable,
            family_row_counts=(("U", 1), ("M", 0)),
        )
        missing_m_family_rows = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            endpoint_target_audit=explicit_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=missing_m_family_rows_scope,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(
            missing_m_family_rows.residual_action_scope.proves_residual_action_scope
        )
        self.assertFalse(missing_m_family_rows.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "residual_action_scope_family_row_counts_do_not_cover_active_families",
            missing_m_family_rows.failure_reasons,
        )

        scoped_residual = replace(
            missing_m_family_rows_scope,
            expected_residual_row_count=2,
            covered_residual_row_count=2,
            expected_residual_rows_by_family=(("U", 1), ("M", 1)),
            covered_residual_rows_by_family=(("U", 1), ("M", 1)),
        )
        proved = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            endpoint_target_audit=explicit_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=scoped_residual,
            residual_action_audit=trivial_endpoint_residual_action_audit(
                input_tuples=(("pU",), ("pM",)),
            ),
        )

        self.assertTrue(proved.residual_action_scope.proves_residual_action_scope)
        self.assertTrue(proved.proves_signed_endpoint_generator_tables)

        mismatched_target = replace(
            explicit_target,
            endpoint_group_orders=(("U", 3),),
        )
        group_mismatch = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            endpoint_target_audit=mismatched_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=scoped_residual,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        self.assertFalse(group_mismatch.endpoint_targets_proved)
        self.assertFalse(group_mismatch.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "endpoint_target_group_order_mismatch",
            group_mismatch.failure_reasons,
        )

        cutoff_degree_mismatch_target = replace(
            explicit_target,
            cutoff_degrees=(("M", 3),),
        )
        cutoff_degree_mismatch = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            endpoint_target_audit=cutoff_degree_mismatch_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=cutoff,
            residual_action_scope=scoped_residual,
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        self.assertTrue(cutoff_degree_mismatch.endpoint_targets_proved)
        self.assertFalse(cutoff_degree_mismatch.exact_cutoff_readouts_proved)
        self.assertFalse(
            cutoff_degree_mismatch.proves_signed_endpoint_generator_tables
        )
        self.assertEqual(
            cutoff_degree_mismatch.cutoff_target_degree_mismatches,
            (("M", 3, 2),),
        )
        self.assertIn(
            "cutoff_readout_target_degree_mismatch",
            cutoff_degree_mismatch.failure_reasons,
        )

    def test_product_endpoint_targets_require_family_supported_labels(self):
        u_state = ("*", "*", "left_constant_map_universal_kernel")
        c_state = ("*", "*", "continuation")
        reachable = (("U", u_state), ("C", c_state))
        seed_entries = (
            (("*", "*", "L", "constant_map_kernel", ("u",)), ("U", u_state)),
            (
                ("*", "*", "L", "partial_constant_hidden_rank_loss", ("c",)),
                ("C", c_state),
            ),
        )
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        product_group = direct_product_group((cyclic_group(2), cyclic_group(3)))
        rows = tuple(
            replace(row, endpoint_value=product_group.identity)
            for row in identity_signed_endpoint_rows(keys)
        )
        witnesses = {row.entry_key: () for row in rows}
        endpoint_target = UniversalKEndpointTargetAudit(
            expected_endpoint_families=("U", "C"),
            covered_endpoint_families=("U", "C"),
            endpoint_group_orders=(("U", 2), ("C", 3)),
            braid_index_independent=True,
            product_families_separated=True,
        )
        residual_scope = replace(
            trivial_endpoint_residual_action_scope(
                "U",
                "C",
                seed_states=reachable,
                family_row_counts=(("U", 1), ("C", 1)),
            ),
            expected_residual_row_count=2,
            covered_residual_row_count=2,
        )

        proved = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=product_group,
            witnesses=witnesses,
            endpoint_target_audit=endpoint_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=rows,
                endpoint_group=product_group,
            ),
            residual_action_scope=residual_scope,
            residual_action_audit=trivial_endpoint_residual_action_audit(
                input_tuples=(("pU",), ("pC",)),
            ),
        )

        self.assertTrue(proved.endpoint_group_order_matches_target_audit)
        self.assertEqual(proved.endpoint_group_target_families, ("U", "C"))
        self.assertTrue(proved.endpoint_group_family_support_proved)
        self.assertTrue(proved.endpoint_targets_proved)
        self.assertFalse(proved.proves_signed_endpoint_generator_tables)
        self.assertIn("cutoff_readout_audit_missing", proved.failure_reasons)

        bad_rows = tuple(
            replace(row, endpoint_value=(1, 0))
            if row.endpoint_family == "C"
            else row
            for row in rows
        )
        bad_support = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            bad_rows,
            endpoint_group=product_group,
            witnesses={row.entry_key: () for row in bad_rows},
            endpoint_target_audit=endpoint_target,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=bad_rows,
                endpoint_group=product_group,
            ),
            residual_action_scope=residual_scope,
            residual_action_audit=trivial_endpoint_residual_action_audit(
                input_tuples=(("pU",), ("pC",)),
            ),
        )

        self.assertFalse(bad_support.endpoint_group_family_support_proved)
        self.assertFalse(bad_support.endpoint_targets_proved)
        self.assertIn(
            "endpoint_value_has_off_family_components",
            tuple(
                failure[1]
                for failure in bad_support.endpoint_group_family_support_failures
            ),
        )
        self.assertIn(
            "endpoint_group_family_support_mismatch",
            bad_support.failure_reasons,
        )

    def test_signed_endpoint_generator_factory_reports_inexact_witness_domain(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        witnesses = {row.entry_key: () for row in rows}
        witnesses[("U", seed_state, 1, "*", "*", "extra", "extra")] = ()
        del witnesses[rows[0].entry_key]
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            (
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(audit.two_strand_witness_domain_exact)
        self.assertEqual(
            tuple(failure[1] for failure in audit.two_strand_witness_domain_failures),
            (
                "missing_two_strand_witness_domain_entry",
                "extra_two_strand_witness_domain_entry",
            ),
        )
        self.assertFalse(audit.signed_two_strand_base_verified)
        self.assertTrue(audit.telescoping_detector_proved)
        self.assertTrue(audit.proves_signed_endpoint_generator_tables)
        self.assertNotIn(
            "signed_two_strand_witness_domain_not_exact",
            audit.failure_reasons,
        )

    def test_signed_endpoint_generator_factory_reports_coordinate_failure(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        reachable = (("U", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        bad_rows = (
            replace(rows[0], output_left=1 if rows[0].output_left == 0 else 0),
            *rows[1:],
        )
        witnesses = {row.entry_key: () for row in bad_rows}
        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            (
                (
                    (
                        "*",
                        "*",
                        "L",
                        "constant_map_kernel",
                        ("*", (0, 1), "universal", "universal"),
                    ),
                    ("U", seed_state),
                ),
            ),
            reachable,
            bad_rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(audit.coordinate_components_verified)
        self.assertEqual(
            tuple(failure[1] for failure in audit.coordinate_component_failures),
            ("negative_coordinate_mismatch",),
        )
        self.assertFalse(audit.proves_signed_endpoint_generator_tables)
        self.assertIn("coordinate_components_not_verified", audit.failure_reasons)

    def test_signed_endpoint_cutoff_readouts_require_scoped_audit(self):
        seed_state = ("*", "*", "left", 0, "*", (0, 1), "*", (0, 1))
        reachable = (("C", seed_state),)
        interval = one_color_identity_interval()
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        witnesses = {row.entry_key: () for row in rows}
        seed_entries = (
            (
                (
                    "*",
                    "*",
                    "L",
                    "partial_constant_hidden_rank_loss",
                    (0, "*", (0, 1), "*", (0, 1), "universal"),
                ),
                ("C", seed_state),
            ),
        )
        bare_flag = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readouts_exact=True,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "C",
                seed_states=reachable,
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertTrue(bare_flag.cutoff_readouts_required)
        self.assertFalse(bare_flag.exact_cutoff_readouts_proved)
        self.assertFalse(bare_flag.proves_signed_endpoint_generator_tables)
        self.assertIn("cutoff_readout_audit_missing", bare_flag.failure_reasons)

        duplicate_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=reachable + reachable,
            covered_cutoff_seed_states=reachable,
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=reachable[0],
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )
        duplicate_cutoff_audit = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=duplicate_cutoff,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "C",
                seed_states=reachable,
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertFalse(duplicate_cutoff.proves_exact_cutoff_readouts)
        self.assertFalse(duplicate_cutoff_audit.proves_signed_endpoint_generator_tables)
        self.assertIn(
            "cutoff_readout_duplicate_seed_states",
            duplicate_cutoff_audit.failure_reasons,
        )

        malformed_cutoff_state = ("C", "not_a_tuple_seed_state")
        malformed_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=(malformed_cutoff_state,),
            covered_cutoff_seed_states=(malformed_cutoff_state,),
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=malformed_cutoff_state,
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )

        self.assertFalse(malformed_cutoff.cutoff_seed_ledgers_well_formed)
        self.assertFalse(malformed_cutoff.proves_exact_cutoff_readouts)
        self.assertIn(
            "cutoff_readout_malformed_seed_states",
            malformed_cutoff.failure_reasons,
        )
        self.assertIn(
            "cutoff_readout_malformed_row_states",
            malformed_cutoff.failure_reasons,
        )

        unhashable_cutoff_state = ("C", (["not-hashable"],))
        unhashable_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=(unhashable_cutoff_state,),
            covered_cutoff_seed_states=(unhashable_cutoff_state,),
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=unhashable_cutoff_state,
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )

        self.assertEqual(
            unhashable_cutoff.expected_cutoff_seed_states_exact,
            (unhashable_cutoff_state,),
        )
        self.assertEqual(unhashable_cutoff.missing_cutoff_seed_states, ())
        self.assertEqual(unhashable_cutoff.extra_cutoff_seed_states, ())
        self.assertEqual(unhashable_cutoff.missing_readout_row_seed_states, ())
        self.assertEqual(unhashable_cutoff.extra_readout_row_seed_states, ())
        self.assertFalse(unhashable_cutoff.cutoff_seed_ledgers_well_formed)
        self.assertFalse(unhashable_cutoff.proves_exact_cutoff_readouts)
        self.assertEqual(
            unhashable_cutoff.malformed_expected_cutoff_seed_states,
            (unhashable_cutoff_state,),
        )
        self.assertEqual(
            unhashable_cutoff.malformed_covered_cutoff_seed_states,
            (unhashable_cutoff_state,),
        )
        self.assertEqual(
            unhashable_cutoff.malformed_row_cutoff_seed_states,
            (unhashable_cutoff_state,),
        )
        self.assertIn(
            "cutoff_readout_malformed_seed_states",
            unhashable_cutoff.failure_reasons,
        )
        self.assertIn(
            "cutoff_readout_malformed_row_states",
            unhashable_cutoff.failure_reasons,
        )

        u_cutoff_state = ("U", ("*", "*", "left_constant_map_universal_kernel"))
        u_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=(u_cutoff_state,),
            covered_cutoff_seed_states=(u_cutoff_state,),
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=u_cutoff_state,
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )

        self.assertFalse(u_cutoff.cutoff_seed_ledgers_well_formed)
        self.assertEqual(
            u_cutoff.malformed_expected_cutoff_seed_states,
            (u_cutoff_state,),
        )
        self.assertEqual(
            u_cutoff.malformed_covered_cutoff_seed_states,
            (u_cutoff_state,),
        )
        self.assertEqual(
            u_cutoff.malformed_row_cutoff_seed_states,
            (u_cutoff_state,),
        )
        self.assertFalse(u_cutoff.proves_exact_cutoff_readouts)
        self.assertIn(
            "cutoff_readout_malformed_seed_states",
            u_cutoff.failure_reasons,
        )
        self.assertIn(
            "cutoff_readout_malformed_row_states",
            u_cutoff.failure_reasons,
        )

        boolean_only_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=reachable,
            covered_cutoff_seed_states=reachable,
            readouts_faithful=True,
            identity_cutoff_data_kills_channels=True,
            braid_index_independent=True,
        )
        self.assertFalse(boolean_only_cutoff.proves_exact_cutoff_readouts)
        self.assertIn(
            "cutoff_readout_rows_do_not_cover_expected_states",
            boolean_only_cutoff.failure_reasons,
        )

        bool_entry_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=reachable,
            covered_cutoff_seed_states=reachable,
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=reachable[0],
                    readout_permutation=(0, True),
                    killed_readout_permutation=(0, True),
                ),
            ),
            braid_index_independent=True,
        )
        self.assertFalse(
            bool_entry_cutoff.readout_rows[0].readout_is_permutation(2)
        )
        self.assertFalse(
            bool_entry_cutoff.readout_rows[0].killed_readout_is_permutation(2)
        )
        self.assertFalse(
            bool_entry_cutoff.readout_rows[0].identity_data_kills_channel(2)
        )
        self.assertFalse(bool_entry_cutoff.proves_exact_cutoff_readouts)
        self.assertIn(
            "cutoff_readout_permutations_invalid",
            bool_entry_cutoff.failure_reasons,
        )

        unkilled_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=reachable,
            covered_cutoff_seed_states=reachable,
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=reachable[0],
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(1, 0),
                ),
            ),
            braid_index_independent=True,
        )
        self.assertFalse(unkilled_cutoff.proves_exact_cutoff_readouts)
        self.assertEqual(unkilled_cutoff.unkilled_readout_rows, reachable)
        self.assertIn(
            "cutoff_readout_rows_not_killed_by_identity_data",
            unkilled_cutoff.failure_reasons,
        )

        mixed_state = ("*", "*", "left")
        mixed_reachable = (("C", seed_state), ("M", mixed_state))
        family_mismatch_cutoff = UniversalKCutoffReadoutAudit(
            expected_cutoff_seed_states=mixed_reachable,
            covered_cutoff_seed_states=reachable,
            cutoff_degree=2,
            readout_rows=(
                UniversalKCutoffReadoutRow(
                    cutoff_seed_state=reachable[0],
                    readout_permutation=(0, 1),
                    killed_readout_permutation=(0, 1),
                ),
            ),
            braid_index_independent=True,
        )
        self.assertEqual(
            family_mismatch_cutoff.expected_cutoff_families,
            ("C", "M"),
        )
        self.assertEqual(family_mismatch_cutoff.covered_cutoff_families, ("C",))
        self.assertEqual(family_mismatch_cutoff.row_cutoff_families, ("C",))
        self.assertEqual(family_mismatch_cutoff.missing_cutoff_families, ("M",))
        self.assertEqual(
            family_mismatch_cutoff.missing_readout_row_families,
            ("M",),
        )
        self.assertFalse(family_mismatch_cutoff.cutoff_family_scope_exact)
        self.assertFalse(family_mismatch_cutoff.proves_exact_cutoff_readouts)
        self.assertIn(
            "cutoff_readout_family_scope_mismatch",
            family_mismatch_cutoff.failure_reasons,
        )
        self.assertIn(
            "cutoff_readout_missing_families",
            family_mismatch_cutoff.failure_reasons,
        )
        self.assertIn(
            "cutoff_readout_missing_row_families",
            family_mismatch_cutoff.failure_reasons,
        )

        scoped_cutoff = trivial_cutoff_readout_audit(reachable)
        proved = universal_k_signed_endpoint_generator_audit(
            interval,
            seed_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(2),
            witnesses=witnesses,
            telescoping_detector_audit=trivial_telescoping_detector_audit(keys),
            cutoff_readout_audit=scoped_cutoff,
            residual_action_scope=trivial_endpoint_residual_action_scope(
                "C",
                seed_states=reachable,
            ),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )

        self.assertTrue(scoped_cutoff.proves_exact_cutoff_readouts)
        self.assertEqual(scoped_cutoff.expected_cutoff_families, ("C",))
        self.assertEqual(scoped_cutoff.covered_cutoff_families, ("C",))
        self.assertEqual(scoped_cutoff.row_cutoff_families, ("C",))
        self.assertTrue(scoped_cutoff.cutoff_family_scope_exact)
        self.assertEqual(proved.endpoint_target_audit.cutoff_degrees, (("C", 2),))
        self.assertEqual(proved.required_cutoff_families, ("C",))
        self.assertTrue(proved.cutoff_target_degrees_match_readout)
        self.assertTrue(proved.cutoff_readout_scope_matches_required)
        self.assertTrue(proved.exact_cutoff_readouts_proved)
        self.assertTrue(proved.proves_signed_endpoint_generator_tables)

    def test_signed_endpoint_coordinate_failures_check_positive_and_inverse_rows(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        interval = one_color_flip_interval()
        positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=1,
            output_right=0,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        negative = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=-1,
            left_color="*",
            right_color="*",
            input_left=1,
            input_right=0,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        bad_positive = replace(positive, output_left=0, output_right=1)
        bad_negative = replace(negative, output_left=1, output_right=0)

        self.assertEqual(
            universal_k_signed_endpoint_coordinate_failures(
                interval,
                (positive, negative),
            ),
            (),
        )
        failures = universal_k_signed_endpoint_coordinate_failures(
            interval,
            (bad_positive, bad_negative),
        )

        self.assertEqual(
            tuple(failure[1] for failure in failures),
            ("positive_coordinate_mismatch", "negative_coordinate_mismatch"),
        )

    def test_signed_endpoint_inverse_failures_check_bidirectional_pairing(self):
        source_state = ("*", "*", "left_constant_map_universal_kernel")
        target_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        interval = one_color_flip_interval()
        positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=source_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=1,
            output_right=0,
            next_seed_state=target_state,
            endpoint_value=0,
        )
        negative = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=target_state,
            sign=-1,
            left_color="*",
            right_color="*",
            input_left=1,
            input_right=0,
            output_left=0,
            output_right=1,
            next_seed_state=source_state,
            endpoint_value=0,
        )

        self.assertEqual(
            universal_k_signed_endpoint_inverse_failures(
                interval,
                (positive, negative),
            ),
            (),
        )

        self.assertEqual(
            tuple(
                failure[1]
                for failure in universal_k_signed_endpoint_inverse_failures(
                    interval,
                    (positive,),
                )
            ),
            ("missing_negative_inverse_row",),
        )

        bad_negative = replace(
            negative,
            output_left=1,
            output_right=1,
            next_seed_state=("wrong",),
        )
        failures = universal_k_signed_endpoint_inverse_failures(
            interval,
            (positive, bad_negative),
        )

        self.assertIn(
            "negative_inverse_does_not_return",
            tuple(failure[1] for failure in failures),
        )
        self.assertIn(
            "missing_positive_inverse_row",
            tuple(failure[1] for failure in failures),
        )

    def test_signed_endpoint_inverse_cancellation_failures_check_group_labels(self):
        source_state = ("*", "*", "left_constant_map_universal_kernel")
        target_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        interval = one_color_flip_interval()
        group = cyclic_group(3)
        positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=source_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=1,
            output_right=0,
            next_seed_state=target_state,
            endpoint_value=1,
        )
        negative = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=target_state,
            sign=-1,
            left_color="*",
            right_color="*",
            input_left=1,
            input_right=0,
            output_left=0,
            output_right=1,
            next_seed_state=source_state,
            endpoint_value=2,
        )

        self.assertEqual(
            universal_k_signed_endpoint_inverse_cancellation_failures(
                group,
                interval,
                (positive, negative),
            ),
            (),
        )

        bad_negative = replace(negative, endpoint_value=1)
        failures = universal_k_signed_endpoint_inverse_cancellation_failures(
            group,
            interval,
            (positive, bad_negative),
        )

        self.assertIn(
            "negative_inverse_label_mismatch",
            tuple(failure[1] for failure in failures),
        )
        self.assertIn(
            "positive_inverse_label_mismatch",
            tuple(failure[1] for failure in failures),
        )

        outside_group = replace(negative, endpoint_value=99)
        self.assertIn(
            "endpoint_value_outside_group",
            tuple(
                failure[1]
                for failure in universal_k_signed_endpoint_inverse_cancellation_failures(
                    group,
                    interval,
                    (positive, outside_group),
                )
            ),
        )

    def test_signed_endpoint_positive_ybe_failures_check_state_and_fibre_paths(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        interval = one_color_identity_interval()

        rows = tuple(
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family="U",
                seed_state=seed_state,
                sign=1,
                left_color="*",
                right_color="*",
                input_left=x,
                input_right=y,
                output_left=x,
                output_right=y,
                next_seed_state=seed_state,
                endpoint_value=0,
            )
            for x in interval.fibres["*"]
            for y in interval.fibres["*"]
        )

        self.assertEqual(
            universal_k_signed_endpoint_positive_ybe_failures(
                interval,
                (("U", seed_state),),
                rows,
            ),
            (),
        )
        missing_failures = universal_k_signed_endpoint_positive_ybe_failures(
            interval,
            (("U", seed_state),),
            rows[:-1],
        )
        self.assertIn(
            "missing_positive_ybe_row",
            tuple(failure[1] for failure in missing_failures),
        )

        left_state = ("*", "*", "left_constant_map_universal_kernel", "left")
        right_state = ("*", "*", "left_constant_map_universal_kernel", "right")
        state_rows = []
        for state in (seed_state, left_state, right_state):
            for x in interval.fibres["*"]:
                for y in interval.fibres["*"]:
                    next_state = state
                    if state == seed_state and (x, y) == (0, 1):
                        next_state = left_state
                    if state == seed_state and (x, y) == (1, 1):
                        next_state = right_state
                    state_rows.append(
                        UniversalKSignedEndpointGeneratorRow(
                            endpoint_family="U",
                            seed_state=state,
                            sign=1,
                            left_color="*",
                            right_color="*",
                            input_left=x,
                            input_right=y,
                            output_left=x,
                            output_right=y,
                            next_seed_state=next_state,
                            endpoint_value=0,
                        )
                    )

        failures = universal_k_signed_endpoint_positive_ybe_failures(
            interval,
            (("U", seed_state),),
            tuple(state_rows),
        )

        self.assertIn(
            "positive_ybe_terminal_mismatch",
            tuple(failure[1] for failure in failures),
        )

    def test_signed_endpoint_positive_ybe_cocycle_failures_check_group_labels(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        interval = one_color_identity_interval()
        group = cyclic_group(3)

        def rows_with_label(label_by_pair):
            return tuple(
                UniversalKSignedEndpointGeneratorRow(
                    endpoint_family="U",
                    seed_state=seed_state,
                    sign=1,
                    left_color="*",
                    right_color="*",
                    input_left=x,
                    input_right=y,
                    output_left=x,
                    output_right=y,
                    next_seed_state=seed_state,
                    endpoint_value=label_by_pair(x, y),
                )
                for x in interval.fibres["*"]
                for y in interval.fibres["*"]
            )

        self.assertEqual(
            universal_k_signed_endpoint_positive_ybe_cocycle_failures(
                group,
                interval,
                (("U", seed_state),),
                rows_with_label(lambda _x, _y: 0),
            ),
            (),
        )

        failures = universal_k_signed_endpoint_positive_ybe_cocycle_failures(
            group,
            interval,
            (("U", seed_state),),
            rows_with_label(lambda x, y: 1 if (x, y) == (0, 1) else 0),
        )

        self.assertIn(
            "positive_ybe_label_mismatch",
            tuple(failure[1] for failure in failures),
        )

    def test_signed_endpoint_far_commutativity_failures_check_disjoint_crossings(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        left_state = ("*", "*", "left_constant_map_universal_kernel", "left")
        right_state = ("*", "*", "left_constant_map_universal_kernel", "right")
        interval = one_color_identity_interval()
        group = cyclic_group(2)
        reachable = (("U", seed_state),)
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)

        self.assertEqual(
            universal_k_signed_endpoint_far_commutativity_failures(
                group,
                interval,
                reachable,
                identity_signed_endpoint_rows(keys),
            ),
            (),
        )

        noncommuting_reachable = (
            ("U", seed_state),
            ("U", left_state),
            ("U", right_state),
        )
        noncommuting_keys = universal_k_signed_endpoint_required_entry_keys(
            interval,
            noncommuting_reachable,
        )
        noncommuting_rows = []
        for row in identity_signed_endpoint_rows(noncommuting_keys):
            if row.seed_state == seed_state and row.sign == 1:
                if (row.input_left, row.input_right) == (0, 0):
                    row = replace(row, next_seed_state=left_state)
                if (row.input_left, row.input_right) == (1, 1):
                    row = replace(row, next_seed_state=right_state)
            noncommuting_rows.append(row)

        failures = universal_k_signed_endpoint_far_commutativity_failures(
            group,
            interval,
            noncommuting_reachable,
            tuple(noncommuting_rows),
        )

        self.assertIn(
            "far_commutativity_terminal_mismatch",
            tuple(failure[1] for failure in failures),
        )

    def test_label_cocycle_mismatches_are_diagnostic_after_path_checks(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        interval = one_color_identity_interval()
        group = symmetric_group(3)
        swap01 = (1, 0, 2)
        swap12 = (0, 2, 1)
        reachable = (("U", seed_state),)
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = []
        for row in identity_signed_endpoint_rows(keys):
            endpoint_value = group.identity
            if (row.input_left, row.input_right) == (0, 0):
                endpoint_value = swap01
            if (row.input_left, row.input_right) == (1, 1):
                endpoint_value = swap12
            rows.append(replace(row, endpoint_value=endpoint_value))

        audit = universal_k_signed_endpoint_generator_audit(
            interval,
            (),
            reachable,
            tuple(rows),
            endpoint_group=group,
        )

        self.assertTrue(audit.positive_ybe_path_verified)
        self.assertTrue(audit.positive_ybe_cocycle_verified)
        self.assertTrue(audit.positive_ybe_label_diagnostic_failures)
        self.assertTrue(audit.far_commutativity_verified)
        self.assertTrue(audit.far_commutativity_label_diagnostic_failures)
        self.assertFalse(audit.far_commutativity_path_failures)
        self.assertTrue(audit.signed_finite_row_checks_proved)

    def test_signed_endpoint_two_strand_base_failures_check_longitude_witnesses(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        group = cyclic_group(3)
        positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=1,
        )
        negative = replace(
            positive,
            sign=-1,
            input_left=1,
            input_right=0,
            output_left=1,
            output_right=0,
        )

        self.assertEqual(
            universal_k_signed_endpoint_two_strand_base_failures(
                group,
                (positive, negative),
                {
                    positive.entry_key: (((1, 0), 0, 1),),
                    negative.entry_key: (((0, 2), 1, 1),),
                },
            ),
            (),
        )

        failures = universal_k_signed_endpoint_two_strand_base_failures(
            group,
            (positive,),
            {},
        )

        self.assertEqual(
            tuple(failure[1] for failure in failures),
            ("missing_two_strand_base_witness",),
        )

        failures = universal_k_signed_endpoint_two_strand_base_failures(
            group,
            (positive,),
            {positive.entry_key: (((2, 0), 0, 1),)},
        )

        self.assertEqual(
            tuple(failure[1] for failure in failures),
            ("two_strand_base_value_mismatch",),
        )

        failures = universal_k_signed_endpoint_two_strand_base_failures(
            group,
            (positive,),
            {
                positive.entry_key: (((1, 0), 0, 1),),
                replace(positive, input_left=1).entry_key: (((1, 0), 0, 1),),
            },
        )

        self.assertIn(
            "extra_two_strand_base_witness",
            tuple(failure[1] for failure in failures),
        )

        domain_failures = universal_k_signed_endpoint_two_strand_witness_domain_failures(
            (positive,),
            {
                replace(positive, input_left=1).entry_key: (((1, 0), 0, 1),),
            },
        )

        self.assertEqual(
            tuple(failure[1] for failure in domain_failures),
            (
                "missing_two_strand_witness_domain_entry",
                "extra_two_strand_witness_domain_entry",
            ),
        )

    def test_signed_endpoint_artin_update_failures_check_witness_precomposition(self):
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        next_state = ("*", "*", "left_constant_map_universal_kernel", "next")
        interval = one_color_identity_interval()
        group = cyclic_group(3)
        positive = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=next_state,
            endpoint_value=1,
        )
        positive_target = replace(
            positive,
            seed_state=next_state,
            next_seed_state=seed_state,
        )
        negative = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=-1,
            left_color="*",
            right_color="*",
            input_left=1,
            input_right=0,
            output_left=1,
            output_right=0,
            next_seed_state=next_state,
            endpoint_value=1,
        )
        negative_target = replace(
            negative,
            seed_state=next_state,
            next_seed_state=seed_state,
        )

        self.assertEqual(
            universal_k_signed_endpoint_artin_update_failures(
                group,
                interval,
                (positive, positive_target, negative, negative_target),
                {
                    positive.entry_key: (((1, 0), 0, 1),),
                    positive_target.entry_key: (((0, 1), 0, 1),),
                    negative.entry_key: (((0, 2), 1, 1),),
                    negative_target.entry_key: (((2, 0), 1, 1),),
                },
            ),
            (),
        )

        failures = universal_k_signed_endpoint_artin_update_failures(
            group,
            interval,
            (positive, positive_target),
            {
                positive.entry_key: (((1, 0), 0, 1),),
                positive_target.entry_key: (((1, 0), 0, 1),),
            },
        )

        self.assertIn(
            "artin_update_witness_letter_mismatch",
            tuple(failure[1] for failure in failures),
        )

        failures = universal_k_signed_endpoint_artin_update_failures(
            group,
            interval,
            (positive,),
            {positive.entry_key: (((1, 0), 0, 1),)},
        )

        self.assertEqual(
            tuple(failure[1] for failure in failures),
            ("missing_artin_update_target_row",),
        )

    def test_post_linear_reports_signed_generator_table_audit(self):
        interval = one_color_identity_interval()
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
        )
        seed_state = ("*", "*", "left_constant_map_universal_kernel")
        row = UniversalKSignedEndpointGeneratorRow(
            endpoint_family="U",
            seed_state=seed_state,
            sign=1,
            left_color="*",
            right_color="*",
            input_left=0,
            input_right=1,
            output_left=0,
            output_right=1,
            next_seed_state=seed_state,
            endpoint_value=0,
        )
        underspecified_entry_keys = (row.entry_key, replace(row, sign=-1).entry_key)
        underspecified_signed_generators = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=routed.universal_k_seed_classifier_entries,
            reachable_seed_states=(("U", seed_state),),
            required_entry_keys=underspecified_entry_keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=(row, replace(row, sign=-1)),
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                underspecified_entry_keys
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        underspecified = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_signed_endpoint_generator=underspecified_signed_generators,
            universal_k_signed_endpoint_interval=interval,
        )

        self.assertTrue(
            underspecified_signed_generators.proves_signed_endpoint_generator_tables
        )
        self.assertIn(
            ("signed_endpoint_generator_entry_domain_matches_current_interval", False),
            underspecified.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_tables_proved", False),
            underspecified.finite_obstruction_data,
        )
        self.assertIn(
            "signed_entry_domain_mismatch_current_interval",
            dict(underspecified.finite_obstruction_data)[
                "signed_endpoint_generator_failure_reasons"
            ],
        )
        self.assertFalse(
            underspecified.system_u_closed_by_signed_endpoint_generator
        )
        self.assertNotEqual(underspecified.remaining_obligations, ())

        reachable = (("U", seed_state),)
        keys = universal_k_signed_endpoint_required_entry_keys(interval, reachable)
        rows = identity_signed_endpoint_rows(keys)
        signed_generators = universal_k_signed_endpoint_generator_audit(
            interval,
            routed.universal_k_seed_classifier_entries,
            reachable,
            rows,
            endpoint_group=cyclic_group(1),
            witnesses={row.entry_key: () for row in rows},
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                endpoint_group=cyclic_group(1),
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_signed_endpoint_generator=signed_generators,
            universal_k_signed_endpoint_interval=interval,
        )

        self.assertIn(
            ("signed_endpoint_generator_tables_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_matches_current_kappa", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_entry_domain_matches_current_interval", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_closes_current_kappa", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_closed_families", ("U",)),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_residual_faithfulness_verified", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_endpoint_targets_fixed", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "signed_endpoint_generator_endpoint_target_group_orders",
                (("U", 1),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_endpoint_target_audit_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_residual_action_rows", 1),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_residual_action_complete", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_failure_reasons", ()),
            audit.finite_obstruction_data,
        )
        self.assertTrue(audit.system_u_closed_by_signed_endpoint_generator)
        self.assertTrue(audit.all_active_routed_endpoint_systems_closed)
        self.assertEqual(audit.remaining_obligations, ())

        wrong_target_group = cyclic_group(2)
        wrong_target_signed_generators = universal_k_signed_endpoint_generator_audit(
            interval,
            routed.universal_k_seed_classifier_entries,
            reachable,
            rows,
            endpoint_group=wrong_target_group,
            witnesses={row.entry_key: () for row in rows},
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                endpoint_group=wrong_target_group,
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        wrong_target_audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_signed_endpoint_generator=wrong_target_signed_generators,
            universal_k_signed_endpoint_interval=interval,
        )
        wrong_target_data = dict(wrong_target_audit.finite_obstruction_data)

        self.assertTrue(
            wrong_target_signed_generators.proves_signed_endpoint_generator_tables
        )
        self.assertEqual(
            wrong_target_audit.current_u_tri_endpoint_group_order,
            1,
        )
        self.assertEqual(
            wrong_target_audit.signed_endpoint_generator_u_target_group_order,
            2,
        )
        self.assertFalse(
            wrong_target_audit.signed_endpoint_generator_uses_current_u_tri_target
        )
        self.assertFalse(
            wrong_target_audit.signed_endpoint_generator_closes_current_kappa
        )
        self.assertFalse(wrong_target_audit.system_u_closed_by_signed_endpoint_generator)
        self.assertEqual(wrong_target_audit.unclosed_routed_endpoint_systems, ("U",))
        self.assertEqual(
            wrong_target_audit.system_name,
            "system_u_triangular_recovery_unit_endpoint",
        )
        self.assertEqual(
            wrong_target_data["signed_endpoint_generator_current_u_tri_group_order"],
            1,
        )
        self.assertEqual(
            wrong_target_data["signed_endpoint_generator_u_target_group_order"],
            2,
        )
        self.assertFalse(
            wrong_target_data["signed_endpoint_generator_uses_current_u_tri_target"]
        )
        self.assertIn(
            "signed_endpoint_generator_current_u_tri_target_mismatch",
            wrong_target_data["signed_endpoint_generator_failure_reasons"],
        )

        forged_rows = tuple(
            replace(row, output_left=1)
            if row.sign == 1
            and row.input_left == 0
            and row.input_right == 0
            else row
            for row in rows
        )
        forged_signed_generators = UniversalKSignedEndpointGeneratorAudit(
            seed_classifier_entries=routed.universal_k_seed_classifier_entries,
            reachable_seed_states=reachable,
            required_entry_keys=keys,
            entry_domain_derived_from_interval=True,
            finite_row_checks_derived_from_tables=True,
            rows=forged_rows,
            endpoint_group=cyclic_group(2),
            endpoint_targets_fixed=True,
            endpoint_target_audit=trivial_endpoint_target_audit("U"),
            coordinate_components_verified=True,
            inverse_pairing_verified=True,
            inverse_cancellation_verified=True,
            positive_ybe_path_verified=True,
            positive_ybe_cocycle_verified=True,
            far_commutativity_verified=True,
            signed_two_strand_base_verified=True,
            artin_homomorphism_update_verified=True,
            telescoping_detector_audit=trivial_telescoping_detector_audit(
                keys,
                rows=forged_rows,
                endpoint_group=cyclic_group(2),
            ),
            residual_action_scope=trivial_endpoint_residual_action_scope("U"),
            residual_action_audit=trivial_endpoint_residual_action_audit(),
        )
        forged_wrapper = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            universal_k_signed_endpoint_generator=forged_signed_generators,
            universal_k_signed_endpoint_interval=interval,
        )
        forged_data = dict(forged_wrapper.finite_obstruction_data)

        self.assertTrue(
            forged_signed_generators.proves_signed_endpoint_generator_tables
        )
        self.assertFalse(
            forged_wrapper.signed_endpoint_generator_rows_match_current_interval
        )
        self.assertFalse(forged_wrapper.system_u_closed_by_signed_endpoint_generator)
        self.assertIn(
            "signed_row_checks_mismatch_current_interval",
            forged_data["signed_endpoint_generator_failure_reasons"],
        )
        self.assertNotEqual(
            forged_data["signed_endpoint_generator_current_coordinate_failures"],
            (),
        )

    def test_triangular_recovery_endpoint_witness_covers_routed_k_defect(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity
        endpoint = triangular_recovery_longitude_expression_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
            assignment=(generator, identity),
            expression=((1, 1),),
        )

        audit = triangular_recovery_endpoint_witness_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            ((("*", "*", "left_constant_map_universal_kernel"), endpoint),),
        )

        self.assertEqual(
            audit.routed_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertEqual(
            audit.witnessed_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertEqual(audit.missing_routed_keys, ())
        self.assertEqual(audit.extra_witness_keys, ())
        self.assertTrue(audit.all_endpoint_witnesses_match_observer)
        self.assertTrue(audit.proves_triangular_recovery_endpoint_witnesses)
        self.assertEqual(audit.failure_reasons, ())

    def test_triangular_recovery_endpoint_witness_reports_missing_routed_key(self):
        observer = triangular_recovery_unit_observer_audit(
            one_color_latin_unit_triangular_interval()
        )

        audit = triangular_recovery_endpoint_witness_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            (),
        )

        self.assertEqual(
            audit.missing_routed_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertFalse(audit.proves_triangular_recovery_endpoint_witnesses)
        self.assertEqual(
            audit.failure_reasons,
            ("routed_recovery_keys_not_covered",),
        )

    def test_triangular_recovery_symmetric_endpoint_fork_covers_routed_key(self):
        observer = triangular_recovery_unit_observer_audit(
            one_color_latin_unit_triangular_interval()
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (observer.unit_group_order,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = triangular_recovery_symmetric_endpoint_fork_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            endpoint_family,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )

        self.assertEqual(
            audit.routed_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertEqual(
            audit.supplied_covered_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertEqual(audit.missing_routed_keys, ())
        self.assertEqual(audit.extra_covered_keys, ())
        self.assertTrue(audit.endpoint_family_uses_recovery_unit_group)
        self.assertTrue(audit.proves_triangular_recovery_symmetric_endpoint_cutoff)
        self.assertEqual(audit.failure_reasons, ())

    def test_triangular_recovery_symmetric_endpoint_fork_reports_missing_key(self):
        observer = triangular_recovery_unit_observer_audit(
            one_color_latin_unit_triangular_interval()
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (observer.unit_group_order,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = triangular_recovery_symmetric_endpoint_fork_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            endpoint_family,
            (),
        )

        self.assertEqual(
            audit.missing_routed_keys,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )
        self.assertFalse(audit.proves_triangular_recovery_symmetric_endpoint_cutoff)
        self.assertEqual(
            audit.failure_reasons,
            ("routed_recovery_keys_not_covered",),
        )

    def test_recovery_endpoint_witness_closes_system_u_when_matching(self):
        interval = one_color_latin_unit_triangular_interval()
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        observer = refinement.triangular_recovery_unit_observer
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity
        endpoint = triangular_recovery_longitude_expression_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
            assignment=(generator, identity),
            expression=((1, 1),),
        )
        witness = triangular_recovery_endpoint_witness_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            ((("*", "*", "left_constant_map_universal_kernel"), endpoint),),
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            triangular_recovery_endpoint_witness=witness,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_triangular_recovery_endpoint_witness",
        )
        self.assertTrue(audit.system_u_closed_by_endpoint_witness)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            (
                "system_u_endpoint_defects",
                ((("*", "*"), "left_constant_map_universal_kernel"),),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("triangular_recovery_endpoint_witness_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("triangular_recovery_endpoint_missing_keys", ()),
            audit.finite_obstruction_data,
        )

    def test_recovery_symmetric_endpoint_fork_closes_system_u_when_matching(self):
        refinement = constant_map_kernel_only_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        observer = refinement.triangular_recovery_unit_observer
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (observer.unit_group_order,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )
        fork = triangular_recovery_symmetric_endpoint_fork_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            endpoint_family,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            triangular_recovery_symmetric_endpoint_fork=fork,
        )

        self.assertEqual(
            audit.system_name,
            "closed_by_triangular_recovery_symmetric_endpoint_fork",
        )
        self.assertTrue(audit.system_u_closed_by_symmetric_endpoint_fork)
        self.assertTrue(audit.system_u_closed_by_routed_certificate)
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertIn(
            ("triangular_recovery_symmetric_fork_cutoff_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("triangular_recovery_symmetric_fork_missing_keys", ()),
            audit.finite_obstruction_data,
        )

    def test_recovery_symmetric_endpoint_fork_does_not_hide_unclosed_continuation(
        self,
    ):
        refinement = constant_map_kernel_system_k_refinement()
        profile, partial_closure, partial_route = (
            right_partial_constant_missing_row_profile_route_audits()
        )
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        observer = refinement.triangular_recovery_unit_observer
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (observer.unit_group_order,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )
        fork = triangular_recovery_symmetric_endpoint_fork_audit(
            observer,
            ((("*", "*"), "left_constant_map_universal_kernel"),),
            endpoint_family,
            (("*", "*", "left_constant_map_universal_kernel"),),
        )

        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
            missing_triangular_row_profile=profile,
            missing_triangular_partial_constant_closure=partial_closure,
            missing_triangular_partial_constant_continuation_route=partial_route,
            triangular_recovery_symmetric_endpoint_fork=fork,
        )

        self.assertEqual(audit.system_name, "system_c_universal_continuation_endpoint")
        self.assertEqual(audit.active_routed_endpoint_systems, ("U", "C"))
        self.assertEqual(audit.unclosed_routed_endpoint_systems, ("C",))
        self.assertTrue(audit.system_u_closed_by_symmetric_endpoint_fork)
        self.assertFalse(audit.system_c_closed_by_endpoint_witness)
        self.assertTrue(audit.is_current_remaining_finite_system)
        self.assertEqual(
            audit.remaining_obligations,
            (
                "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
            ),
        )

    def test_missing_latin_kernel_labels_require_nontrivial_fibres(self):
        refinement = singleton_constant_map_non_surjective_refinement()

        self.assertEqual(refinement.status, "triangular_structural_inconsistency")
        self.assertEqual(refinement.active_missing_left_latin_row_defects, ())
        self.assertEqual(refinement.active_missing_right_latin_row_defects, ())
        self.assertIn(
            (("*", "*"), "left_constant_map_not_surjective"),
            refinement.missing_left_latin_row_defects,
        )
        self.assertNotIn(
            (("*", "*"), "left_constant_map_universal_kernel"),
            refinement.missing_left_latin_row_defects,
        )

    def test_unsupported_companion_block_image_is_structural_not_active_k(self):
        refinement = unsupported_companion_block_image_refinement()
        audit = PostLinearRemainingFiniteSystemAudit(refinement)

        self.assertEqual(refinement.status, "triangular_structural_inconsistency")
        self.assertIn(
            (("*", "*"), "left_companion_sections_injective_non_surjective"),
            refinement.missing_left_latin_row_defects,
        )
        self.assertEqual(refinement.active_missing_left_latin_row_defects, ())
        self.assertEqual(refinement.active_companion_block_image_support_rows, ())
        self.assertTrue(
            refinement.active_companion_block_images_have_constant_kernel_support
        )
        self.assertEqual(
            audit.unsupported_companion_block_image_rows,
            (("left", "*", "*"),),
        )
        self.assertTrue(audit.unsupported_companion_structural_contradiction_proved)
        self.assertFalse(audit.unsupported_companion_structural_obligation_active)
        derived = audit.effective_unsupported_companion_structural_contradiction
        self.assertIsNotNone(derived)
        self.assertEqual(
            tuple(row.closed_branch for row in derived.contradiction_rows),
            ("finite_triangular_bijection_cardinality_contradiction",),
        )
        self.assertEqual(
            audit.system_name,
            "closed_by_recorded_branch",
        )
        self.assertFalse(audit.is_current_remaining_finite_system)
        self.assertEqual(audit.remaining_obligations, ())
        self.assertEqual(audit.universal_k_row_normal_form_domain, ())
        self.assertEqual(audit.universal_k_seed_classifier_entries, ())

    def test_unsupported_companion_block_image_requires_contradiction_certificate(self):
        refinement = unsupported_companion_block_image_refinement()
        incomplete = UnsupportedCompanionStructuralContradictionAudit(
            expected_rows=(("left", "*", "*"),),
            covered_rows=(("left", "*", "*"),),
        )
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement,
            unsupported_companion_structural_contradiction=incomplete,
        )

        self.assertFalse(
            audit.unsupported_companion_structural_contradiction_proved
        )
        self.assertIn(
            "unsupported_companion_missing_contradiction_rows",
            incomplete.failure_reasons,
        )
        self.assertTrue(audit.unsupported_companion_structural_obligation_active)

        contradiction = UnsupportedCompanionStructuralContradictionAudit(
            expected_rows=(("left", "*", "*"),),
            covered_rows=(("left", "*", "*"),),
            contradiction_rows=(
                UnsupportedCompanionStructuralContradictionRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    witness_kind="already_closed_branch",
                    closed_branch="finite_triangular_bijection_cardinality_contradiction",
                ),
            ),
        )
        closed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            unsupported_companion_structural_contradiction=contradiction,
        )

        self.assertTrue(
            contradiction.proves_unsupported_companion_structural_contradiction
        )
        self.assertTrue(
            closed.unsupported_companion_structural_contradiction_proved
        )
        self.assertFalse(closed.unsupported_companion_structural_obligation_active)
        self.assertEqual(closed.system_name, "closed_by_recorded_branch")
        self.assertFalse(closed.is_current_remaining_finite_system)
        self.assertEqual(closed.remaining_obligations, ())

    def test_post_linear_routes_companion_block_image_by_constant_map_recovery(self):
        refinement = companion_block_system_k_refinement()
        closure = TriangularLatinDefectClosureAudit(
            rows=(
                TriangularLatinDefectClosureRow(
                    side="left",
                    defect="constant_map_kernel",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    fixed_input=None,
                    collapsed_inputs=(0, 1),
                    generated=generated("universal"),
                ),
            ),
        )
        route = TriangularConstantKernelRecoveryRouteAudit(
            rows=(
                TriangularConstantKernelRecoveryRouteRow(
                    side="left",
                    left_color="*",
                    right_color="*",
                    domain_color="*",
                    collapsed_inputs=(0, 1),
                    closure_kind="universal",
                    recovery_row_present=True,
                    recovery_formula_bijective=True,
                    witness_output_pairs=(
                        (0, ((0, 0),)),
                        (1, ((0, 1),)),
                    ),
                ),
            ),
        )
        raw = PostLinearRemainingFiniteSystemAudit(refinement)
        routed = PostLinearRemainingFiniteSystemAudit(
            refinement,
            triangular_latin_defect_closure=closure,
            triangular_constant_kernel_recovery_route=route,
        )

        self.assertIn(
            (
                "live_k_missing_latin_row_defects",
                (
                    (("*", "*"), "left_constant_map_universal_kernel"),
                    (("*", "*"), "left_companion_sections_injective_non_surjective"),
                    (("*", "*"), "no_right_triangular_row"),
                ),
            ),
            raw.finite_obstruction_data,
        )
        self.assertIn(
            (
                "active_companion_block_image_support_rows",
                (
                    (
                        "left",
                        ("*", "*"),
                        ("left_constant_map_universal_kernel",),
                    ),
                ),
            ),
            raw.finite_obstruction_data,
        )
        self.assertIn(
            (
                "active_companion_block_images_have_constant_kernel_support",
                True,
            ),
            raw.finite_obstruction_data,
        )
        self.assertNotIn(
            (
                "live_k_missing_latin_row_defects",
                (
                    (("*", "*"), "left_constant_map_universal_kernel"),
                    (("*", "*"), "left_companion_sections_constant"),
                    (("*", "*"), "left_companion_sections_injective_non_surjective"),
                    (("*", "*"), "no_right_triangular_row"),
                ),
            ),
            raw.finite_obstruction_data,
        )
        self.assertIn(
            ("live_k_missing_latin_row_defects", ((("*", "*"), "no_right_triangular_row"),)),
            routed.finite_obstruction_data,
        )
        constant_descriptor = (
            "*",
            "*",
            "L",
            "constant_map_kernel",
            ("*", (0, 1), "universal", "universal"),
        )
        companion_descriptor = (
            "*",
            "*",
            "L",
            "supported_companion_block_image",
            ("support_constant_map_kernel", "*", (0, 1), "universal"),
        )
        self.assertEqual(
            routed.universal_k_row_normal_form_domain,
            (constant_descriptor, companion_descriptor),
        )
        self.assertEqual(
            routed.universal_k_seed_classifier_entries,
            (
                (
                    constant_descriptor,
                    ("U", ("*", "*", "left_constant_map_universal_kernel")),
                ),
                (
                    companion_descriptor,
                    (
                        "U",
                        (
                            "*",
                            "*",
                            "left_companion_sections_injective_non_surjective",
                        ),
                    ),
                ),
            ),
        )

    def test_post_linear_side_dual_replacement_rows_record_nonlatin_right_defects(self):
        interval = one_color_right_triangular_nonlatin_interval()
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement_for(interval, colored_ybe=False),
            missing_triangular_row_profile=missing_triangular_row_profile_audit(
                interval
            ),
        )

        self.assertEqual(
            audit.k_left_side_dual_replacement_rows,
            (
                (
                    ("*", "*"),
                    "side_dual_right_triangular_nonlatin",
                    (
                        "right_opposite_sections_not_bijective",
                        "right_opposite_proper_kernel_visible",
                        "no_side_dual_left_latin_replacement",
                    ),
                    (),
                ),
            ),
        )

    def test_post_linear_side_dual_replacement_rows_record_missing_right_profile(self):
        interval = one_color_proper_rank_loss_interval()
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement_for(interval, colored_ybe=False),
            missing_triangular_row_profile=missing_triangular_row_profile_audit(
                interval
            ),
        )

        self.assertEqual(
            audit.k_left_side_dual_replacement_rows,
            (
                (
                    ("*", "*"),
                    "no_side_dual_right_triangular_replacement",
                    (
                        "no_right_triangular_row",
                        "no_side_dual_left_latin_replacement",
                    ),
                    ("proper_section_kernel_visible",),
                ),
            ),
        )

    def test_post_linear_records_coordinate_unit_missing_triangular_routes(self):
        interval = one_color_latin_unit_triangular_interval()
        audit = PostLinearRemainingFiniteSystemAudit(
            refinement_for(interval, colored_ybe=False),
            missing_triangular_row_profile=missing_triangular_row_profile_audit(
                interval
            ),
            missing_triangular_left_rack_cardinality=missing_triangular_left_rack_cardinality_audit(
                interval
            ),
            missing_triangular_coordinate_unit_routing=missing_triangular_coordinate_unit_routing_audit(
                interval
            ),
            missing_triangular_partial_constant_closure=missing_triangular_partial_constant_closure_audit(
                interval
            ),
            missing_triangular_partial_constant_continuation_route=missing_triangular_partial_constant_continuation_route_audit(
                interval
            ),
            universal_continuation_identity_routing=universal_continuation_identity_routing_audit(
                interval
            ),
        )

        self.assertIn(
            (
                "missing_triangular_coordinate_unit_routes",
                (
                    (
                        "*",
                        "*",
                        ("right",),
                        "triangular_row_present",
                        "coordinate_side_unit_not_triangular",
                        "mixed_unit_context",
                    ),
                ),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_coordinate_unit_unrouted_rows", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_partial_constant_closure_rows", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_triangular_left_rack_section_cardinality_failures",
                (),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_injective_non_surjective_rows", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_profile_unclassified_rows", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("missing_triangular_left_rack_cardinality_proved", True),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            (
                "missing_triangular_partial_constant_continuation_routes",
                (),
            ),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("universal_continuation_identity_unrouted_edges", ()),
            audit.finite_obstruction_data,
        )
        self.assertIn(
            ("universal_continuation_identity_routing_proved", True),
            audit.finite_obstruction_data,
        )

    def test_post_linear_remaining_finite_system_audit_routes_k_to_system_u_when_supplied(self):
        audit = PostLinearRemainingFiniteSystemAudit(
            active_system_k_refinement(),
            kink_completion_deficits_routed=True,
        )

        self.assertEqual(
            audit.system_name,
            "system_u_triangular_recovery_unit_endpoint",
        )
        self.assertTrue(audit.system_u_active)
        self.assertIn(("unit_group_order", 3), audit.finite_obstruction_data)
        self.assertEqual(
            audit.remaining_obligations,
            (
                "prove each routed triangular recovery endpoint composite lies in V_beta(U_tri)",
                "or upgrade one routed U_tri endpoint miss to a normalized-law sequence",
            ),
        )

    def test_direct_unit_longitude_status_is_preempted_by_kink_dichotomy(self):
        interval = one_color_latin_unit_triangular_interval()
        audit = NonlinearOverlapRefinementAudit(
            obstruction=exact_obstruction(),
            unit_collapse=TwoSidedUnitCollapseAudit(
                colored_ybe=False,
                continuation=continuation(),
                row_audits=section_unit_row_audits(interval),
            ),
            rank_profile=section_rank_profile_collapse_audit(interval),
            triangular_bundle=triangular_bundle_audit(interval),
            triangular_recovery=triangular_recovery_audit(interval),
            triangular_column=triangular_column_collapse_audit(interval),
            latin_triangular=LatinTriangularYBEAudit(row_audits=(), triple_audits=()),
            side_dual_latin_triangular=LatinTriangularYBEAudit(
                row_audits=(),
                triple_audits=(),
            ),
            rack_kink=RackKinkLatinTriangularCollapseAudit(
                base_rows_are_left_rack_form=True,
                left_translations_bijective=True,
                self_distributive=True,
                kink_predecessors={"*": "*"},
                latin_rows_present_for_all_pairs=True,
                latin_ybe_equations_hold=True,
                alpha_kink_identity_failures=(),
                kink_column_constancy_failures=(),
                non_singleton_latin_colors=("*",),
            ),
            side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
                side_opposite_local_interval(interval),
            ),
        )

        self.assertTrue(audit.triangular_recovery_unit_observer_ready)
        self.assertEqual(audit.rack_kink_completion_deficits, ())
        self.assertTrue(audit.direct_unit_longitude_status_preempted_by_kink_dichotomy)
        self.assertEqual(audit.status, "latin_triangular_kink_contradiction")
        self.assertNotEqual(
            audit.status,
            "triangular_recovery_unit_longitude_obstruction",
        )

    def test_post_linear_remaining_finite_system_function_uses_real_bottleneck_ledger(self):
        audit = post_linear_remaining_finite_system_audit(
            one_color_latin_unit_triangular_interval()
        )

        self.assertEqual(audit.system_name, "earlier_unrouted_status:not_corridor_target")
        self.assertFalse(audit.is_current_remaining_finite_system)

    def test_post_linear_function_derives_signed_endpoint_audit_from_inputs(self):
        residual_theorem = UniversalKResidualFaithfulnessAudit(
            active_endpoint_families=(),
            covered_endpoint_families=(),
            expected_residual_row_count=0,
            covered_residual_row_count=0,
            endpoint_channels_exact=True,
            identity_endpoint_data_forces_residual_identity=True,
            braid_index_independent=True,
            product_families_separated=True,
        )
        audit = post_linear_remaining_finite_system_audit(
            one_color_latin_unit_triangular_interval(),
            universal_k_signed_endpoint_group=cyclic_group(2),
            universal_k_residual_faithfulness_theorem=residual_theorem,
        )

        self.assertIsNotNone(audit.universal_k_signed_endpoint_generator)
        signed = audit.universal_k_signed_endpoint_generator
        self.assertEqual(
            signed.seed_classifier_entries,
            audit.universal_k_seed_classifier_entries,
        )
        self.assertTrue(signed.endpoint_targets_fixed)
        self.assertTrue(signed.residual_theorem_scope_matches_required)
        self.assertIn("no_routed_k_seed_states", signed.failure_reasons)

    def test_post_linear_function_builds_endpoint_observer_from_word_potential(self):
        certificate = UniversalKWordPotentialCertificate(
            endpoint_group=cyclic_group(2),
            templates=(),
            identity_rows=(),
            normalized_seed_states=(),
        )
        audit = post_linear_remaining_finite_system_audit(
            one_color_latin_unit_triangular_interval(),
            universal_k_word_potential_certificate=certificate,
            universal_k_word_potential_certificates_by_family=(("U", certificate),),
        )

        signed = audit.universal_k_signed_endpoint_generator
        self.assertIsNotNone(signed)
        self.assertIsNotNone(audit.universal_k_endpoint_observer)
        self.assertIsNotNone(audit.universal_k_endpoint_observer_family_build)
        self.assertIs(audit.universal_k_endpoint_observer.audit, signed)
        self.assertIs(
            signed.telescoping_detector_audit.word_potential_certificate,
            certificate,
        )
        self.assertEqual(signed.endpoint_group, certificate.endpoint_group)
        self.assertIn(
            ("signed_endpoint_generator_endpoint_observer_build_present", True),
            audit.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("signed_endpoint_generator_endpoint_observer_build_proved", False),
            audit.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_present", True),
            audit.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_extra_families", ("U",)),
            audit.routed_endpoint_obstruction_data,
        )
        self.assertIn("no_routed_k_seed_states", signed.failure_reasons)
        self.assertIn(
            "telescoping_detector_expected_positive_entry_keys_empty",
            signed.failure_reasons,
        )

    def test_post_linear_function_derives_identity_endpoint_observer_candidates(self):
        audit = post_linear_remaining_finite_system_audit(
            one_color_latin_unit_triangular_interval(),
            universal_k_identity_endpoint_observer_candidates=True,
        )

        family_build = audit.universal_k_endpoint_observer_family_build
        self.assertIsNotNone(family_build)
        self.assertIsNone(audit.universal_k_signed_endpoint_generator)
        self.assertEqual(family_build.expected_endpoint_families_exact, ())
        self.assertFalse(family_build.proves_family_endpoint_observers)
        self.assertIn(
            "endpoint_observer_family_builds_no_active_families",
            family_build.failure_reasons,
        )
        self.assertIn(
            ("endpoint_observer_family_build_present", True),
            audit.routed_endpoint_obstruction_data,
        )
        self.assertIn(
            ("endpoint_observer_family_build_proved", False),
            audit.routed_endpoint_obstruction_data,
        )

    def test_triangular_recovery_unit_observer_extends_recovery_rows_to_units(self):
        observer = triangular_recovery_unit_observer_audit(
            one_color_latin_unit_triangular_interval()
        )

        self.assertEqual(observer.row_count, 1)
        self.assertTrue(observer.all_recovery_formulas_bijective)
        self.assertTrue(observer.all_generators_are_units)
        self.assertTrue(observer.proves_fixed_unit_observer)
        self.assertEqual(observer.unit_group_order, 2)
        self.assertEqual(len(observer.universe), 4)

    def test_triangular_recovery_route_uses_existing_unit_composite_gate(self):
        interval = one_color_latin_unit_triangular_interval()

        visible = triangular_recovery_longitude_route_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
        )
        finite_failure = triangular_recovery_longitude_route_audit(
            interval,
            n=2,
            braid_word=(1, 1, 1, 1),
            factor_row_indices=(0,),
        )

        self.assertTrue(visible.endpoint_lies_in_recovery_unit_longitude_subgroup)
        self.assertTrue(visible.identity_longitudes_kill_recovery_endpoint)
        self.assertFalse(finite_failure.endpoint_lies_in_recovery_unit_longitude_subgroup)
        self.assertFalse(finite_failure.identity_longitudes_kill_recovery_endpoint)
        self.assertTrue(finite_failure.is_finite_recovery_unit_detector_failure)

    def test_triangular_recovery_longitude_expression_certifies_endpoint(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity

        audit = triangular_recovery_longitude_expression_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
            assignment=(generator, identity),
            expression=((1, 1),),
        )

        self.assertTrue(audit.factors_are_triangular_recovery_generators)
        self.assertTrue(audit.unit_expression.assignment_in_unit_group)
        self.assertEqual(audit.unit_expression.expression_value, generator)
        self.assertTrue(
            audit.endpoint_lies_in_recovery_unit_longitude_subgroup_by_expression
        )
        self.assertTrue(audit.proves_recovery_endpoint_by_longitude_expression)
        self.assertTrue(
            audit.identity_longitudes_kill_recovery_endpoint_by_expression
        )

    def test_triangular_recovery_longitude_expression_rejects_bad_certificate(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity

        audit = triangular_recovery_longitude_expression_audit(
            interval,
            n=2,
            braid_word=(1, 1, 1, 1),
            factor_row_indices=(0,),
            assignment=(generator, identity),
            expression=(),
        )

        self.assertTrue(audit.factors_are_triangular_recovery_generators)
        self.assertFalse(
            audit.endpoint_lies_in_recovery_unit_longitude_subgroup_by_expression
        )
        self.assertFalse(audit.proves_recovery_endpoint_by_longitude_expression)
        self.assertFalse(
            audit.identity_longitudes_kill_recovery_endpoint_by_expression
        )

    def test_triangular_recovery_detector_lift_hooks_use_recovery_unit_group(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        group = triangular_recovery_unit_group(interval)
        identity = group.identity
        generator = observer.generator_transformations[0]

        transition = triangular_recovery_detector_lift_transition_audit(
            interval,
            signed_generator=1,
            input_left=(generator, identity),
            input_right=(identity, identity),
            supplied_left=(identity, generator),
            supplied_right=(generator, identity),
        )
        braid = triangular_recovery_detector_lift_braid_audit(
            interval,
            initial_meridians=(generator, identity),
            braid_word=(1, 1),
            endpoint_expression=((1, 1),),
        )

        self.assertTrue(transition.row_matches_artin_detector)
        self.assertTrue(braid.proves_detector_lift_recursion)
        self.assertEqual(braid.endpoint_value, generator)

    def test_triangular_recovery_derived_series_lift_closes_solvable_unit_group(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        generator = observer.generator_transformations[0]
        identity = observer.monoid.identity
        stage_witness = (((generator, identity), 1, 1),)

        audit = triangular_recovery_derived_series_lift_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            factor_row_indices=(0,),
            stage_lifted_witnesses=(stage_witness,),
        )

        self.assertTrue(audit.factors_are_triangular_recovery_generators)
        self.assertEqual(audit.derived_lift.derived_subgroup_orders, (2, 1))
        self.assertTrue(audit.derived_lift.stage_count_matches_derived_series)
        self.assertTrue(audit.derived_lift.all_stage_lifts_pass)
        self.assertEqual(audit.residual_endpoint, identity)
        self.assertEqual(audit.perfect_residual_size, 1)
        self.assertTrue(audit.proves_recovery_endpoint_by_derived_lift)
        self.assertTrue(audit.solvable_unit_group_closed_by_supplied_lifts)

    def test_triangular_recovery_perfect_residual_route_handles_trivial_residual(self):
        interval = one_color_latin_unit_triangular_interval()
        observer = triangular_recovery_unit_observer_audit(interval)
        identity = observer.monoid.identity
        generator = observer.generator_transformations[0]

        closed = triangular_recovery_perfect_residual_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            residual_endpoint=identity,
        )
        miss = triangular_recovery_perfect_residual_audit(
            interval,
            n=2,
            braid_word=(1, 1),
            residual_endpoint=generator,
        )

        self.assertTrue(closed.residual_endpoint_is_recovery_unit)
        self.assertTrue(closed.residual_endpoint_is_in_perfect_residual)
        self.assertTrue(closed.proves_recovery_residual_endpoint_by_perfect_route)
        self.assertTrue(closed.identity_longitudes_kill_recovery_residual_endpoint)
        self.assertFalse(miss.residual_endpoint_is_in_perfect_residual)
        self.assertFalse(miss.proves_recovery_residual_endpoint_by_perfect_route)
        self.assertFalse(miss.is_finite_recovery_perfect_residual_detector_failure)


if __name__ == "__main__":
    unittest.main()
