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
    TwoSidedUnitCollapseAudit,
    latin_triangular_ybe_audit,
    nonlinear_overlap_obstruction_audit,
    nonlinear_overlap_refinement_audit,
    post_linear_remaining_finite_system_audit,
    rack_kink_latin_triangular_collapse_audit,
    right_rack_kink_latin_triangular_collapse_audit,
    section_rank_profile_collapse_audit,
    section_unit_row_audits,
    side_opposite_local_interval,
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
    triangular_recovery_longitude_expression_audit,
    triangular_recovery_longitude_route_audit,
    triangular_recovery_perfect_residual_audit,
    triangular_recovery_audit,
    triangular_recovery_unit_observer_audit,
    triangular_recovery_unit_group,
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
        domain_size=2,
        codomain_size=3,
        rank=2,
        kernel_blocks=((0,), (1,)),
        image=(0, 1),
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
            ("live_k_missing_latin_row_defects", ((("*", "*"), "no_right_triangular_row"),)),
            routed.finite_obstruction_data,
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
