import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    LocalInterval,
    MissingTriangularCoordinateUnitRoute,
    MissingTriangularCoordinateUnitRoutingAudit,
    artin_permutation_defect_witness_audit,
    cyclic_group,
    descent_endpoint_repair_contract_audit,
    endpoint_artin_defect_audit,
    endpoint_artin_defect_coordinate_readout_audit,
    endpoint_artin_defect_residual_action_audit,
    endpoint_artin_defect_residual_readout_audit,
    endpoint_coordinate_readout_audit,
    endpoint_longitude_expression_audit,
    endpoint_product_artin_defect_audit,
    endpoint_product_longitude_expression_audit,
    endpoint_residual_action_audit,
    endpoint_residual_readout_audit,
    EndpointFamilySymmetricForkAudit,
    EndpointFamilySymmetricForkRow,
    EndpointFamilySymmetricSeedAudit,
    endpoint_family_symmetric_fork_audit,
    endpoint_family_symmetric_seed_audit,
    identity_solution,
    local_symmetric_normalized_law_prefix_witness_audit,
    lost_edge_external_routing_audit,
    mixed_unit_context_endpoint_witness_audit,
    mixed_unit_context_symmetric_endpoint_fork_audit,
    pure_braid_generator,
    QuotientMap,
    rack_solution,
    readout_descent_separation_audit,
    routed_lost_edge_endpoint_witness_audit,
    symmetric_repair_contract_bridge_audit,
    symmetric_group,
    terminal_gauge_longitude_expression_audit,
    terminal_gauge_product_longitude_expression_audit,
    terminal_gauge_telescoping_audit,
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


class EndpointFactorizationTests(unittest.TestCase):
    def test_single_endpoint_expression_certifies_membership(self):
        group = cyclic_group(3)

        audit = endpoint_longitude_expression_audit(
            group,
            n=2,
            braid_word=(1, 1),
            endpoint=1,
            assignment=(1, 0),
            expression=((1, 1),),
        )

        self.assertEqual(audit.group_order, 3)
        self.assertEqual(audit.endpoint, 1)
        self.assertTrue(audit.endpoint_in_group)
        self.assertTrue(audit.assignment_in_group)
        self.assertEqual(audit.expression_value, 1)
        self.assertTrue(audit.expression_matches_endpoint)
        self.assertTrue(audit.endpoint_lies_in_longitude_subgroup_by_expression)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertTrue(audit.identity_longitudes_kill_endpoint_by_expression)

    def test_artin_permutation_defect_builds_longitude_witness(self):
        group = symmetric_group(3)
        assignment = ((1, 0, 2), (0, 2, 1))
        word = ((0, 1), (1, 1))

        audit = artin_permutation_defect_witness_audit(
            group,
            n=2,
            braid_word=(1,),
            assignment=assignment,
            word=word,
        )

        self.assertEqual(
            audit.defect_word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertEqual(audit.defect_value, (2, 0, 1))
        self.assertEqual(audit.longitude_witness_value, audit.defect_value)
        self.assertEqual(len(audit.longitude_witness), 4)
        self.assertTrue(audit.witness_matches_defect)

    def test_endpoint_artin_defect_certifies_membership(self):
        group = symmetric_group(3)
        assignment = ((1, 0, 2), (0, 2, 1))
        word = ((0, 1), (1, 1))

        audit = endpoint_artin_defect_audit(
            group,
            n=2,
            braid_word=(1,),
            endpoint=(2, 0, 1),
            terms=((assignment, word, 1),),
        )

        self.assertEqual(audit.group_order, 6)
        self.assertEqual(audit.defect_values, ((2, 0, 1),))
        self.assertEqual(audit.defect_product_value, audit.endpoint)
        self.assertTrue(audit.defect_product_matches_endpoint)
        self.assertEqual(audit.longitude_witness_value, audit.endpoint)
        self.assertTrue(audit.longitude_witness_matches_defect_product)
        self.assertTrue(audit.endpoint_lies_in_longitude_subgroup_by_artin_defects)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertTrue(audit.identity_longitudes_kill_endpoint_by_artin_defects)

    def test_product_artin_defect_builds_literal_product_witness(self):
        group = symmetric_group(3)
        assignment = ((1, 0, 2), (0, 2, 1))
        word = ((0, 1), (1, 1))

        audit = endpoint_product_artin_defect_audit(
            (group,),
            n=2,
            braid_word=(1,),
            endpoints=((2, 0, 1),),
            terms_by_factor=(((assignment, word, 1),),),
        )

        self.assertEqual(audit.product_group_order, 6)
        self.assertEqual(audit.product_endpoint, ((2, 0, 1),))
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.product_witness_matches_endpoint)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_artin_defects
        )
        self.assertTrue(audit.proves_product_endpoint_detector_by_artin_defects)

    def test_artin_defect_residual_action_records_complete_supplied_rows(self):
        group = symmetric_group(3)
        assignment = ((1, 0, 2), (0, 2, 1))
        word = ((0, 1), (1, 1))
        endpoint_audit = endpoint_product_artin_defect_audit(
            (group,),
            n=2,
            braid_word=(1,),
            endpoints=((2, 0, 1),),
            terms_by_factor=(((assignment, word, 1),),),
        )
        coordinate = endpoint_artin_defect_coordinate_readout_audit(
            endpoint_audit,
            "a",
            "b",
        )
        residual = endpoint_artin_defect_residual_readout_audit((coordinate,))
        action = endpoint_artin_defect_residual_action_audit(
            2,
            (1,),
            (residual,),
            expected_row_count=1,
            expected_input_tuples=(("a",),),
        )

        self.assertFalse(coordinate.endpoint_tuple_is_identity)
        self.assertTrue(coordinate.identity_endpoints_fix_coordinate)
        self.assertTrue(coordinate.identity_longitudes_kill_coordinate_by_artin_defects)
        self.assertEqual(residual.input_tuple, ("a",))
        self.assertEqual(residual.output_tuple, ("b",))
        self.assertFalse(residual.residual_tuple_fixed)
        self.assertTrue(residual.identity_longitudes_kill_residual_tuple_by_artin_defects)
        self.assertEqual(action.row_count, 1)
        self.assertTrue(action.covers_expected_rows)
        self.assertTrue(action.braid_data_consistent)
        self.assertTrue(action.proves_supplied_rows_detector_implication)
        self.assertTrue(action.proves_complete_residual_action_implication)

        row_count_only = endpoint_artin_defect_residual_action_audit(
            2,
            (1,),
            (residual,),
            expected_row_count=1,
        )
        self.assertFalse(row_count_only.expected_input_tuple_domain_supplied)
        self.assertFalse(row_count_only.input_tuple_domain_exact)
        self.assertTrue(row_count_only.proves_supplied_rows_detector_implication)
        self.assertFalse(row_count_only.proves_complete_residual_action_implication)

    def test_artin_defect_residual_action_rejects_unfaithful_identity_endpoint_row(self):
        group = symmetric_group(3)
        endpoint_audit = endpoint_product_artin_defect_audit(
            (group,),
            n=2,
            braid_word=(1, -1),
            endpoints=(group.identity,),
            terms_by_factor=((),),
        )
        coordinate = endpoint_artin_defect_coordinate_readout_audit(
            endpoint_audit,
            "a",
            "b",
        )
        residual = endpoint_artin_defect_residual_readout_audit((coordinate,))
        action = endpoint_artin_defect_residual_action_audit(
            2,
            (1, -1),
            (residual,),
            expected_row_count=1,
            expected_input_tuples=(("a",),),
        )

        self.assertTrue(coordinate.endpoint_tuple_is_identity)
        self.assertFalse(coordinate.identity_endpoints_fix_coordinate)
        self.assertFalse(
            coordinate.identity_longitudes_kill_coordinate_by_artin_defects
        )
        self.assertFalse(action.all_identity_endpoints_fix_rows)
        self.assertFalse(action.all_identity_longitudes_kill_rows_by_artin_defects)
        self.assertFalse(action.residual_action_identity_on_supplied_rows)
        self.assertFalse(action.proves_supplied_rows_detector_implication)

    def test_artin_defect_endpoint_rejects_bad_display(self):
        group = symmetric_group(3)
        assignment = ((1, 0, 2), (0, 2, 1))
        word = ((0, 1), (1, 1))

        audit = endpoint_artin_defect_audit(
            group,
            n=2,
            braid_word=(1,),
            endpoint=group.identity,
            terms=((assignment, word, 1),),
        )

        self.assertTrue(audit.longitude_witness_matches_defect_product)
        self.assertFalse(audit.defect_product_matches_endpoint)
        self.assertFalse(audit.endpoint_lies_in_longitude_subgroup_by_artin_defects)

    def test_artin_defect_endpoint_rejects_bad_exponent(self):
        with self.assertRaises(ValueError):
            endpoint_artin_defect_audit(
                symmetric_group(3),
                n=2,
                braid_word=(1,),
                endpoint=(0, 1, 2),
                terms=((((1, 0, 2), (0, 2, 1)), ((0, 1),), 2),),
            )

    def test_product_endpoint_expression_builds_literal_product_witness(self):
        c2 = cyclic_group(2)
        c3 = cyclic_group(3)

        audit = endpoint_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1, 1),
            endpoints=(1, 1),
            assignments=((1, 0), (1, 0)),
            expressions=(((1, 1),), ((1, 1),)),
        )

        self.assertEqual(audit.group_orders, (2, 3))
        self.assertEqual(audit.product_group_order, 6)
        self.assertEqual(audit.product_endpoint, (1, 1))
        self.assertTrue(audit.all_endpoints_in_groups)
        self.assertTrue(audit.all_assignments_in_groups)
        self.assertTrue(audit.all_expressions_match_endpoints)
        self.assertEqual(len(audit.product_witness), 2)
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.product_witness_matches_endpoint)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertFalse(audit.identity_product_longitude_signature_by_factors)
        self.assertTrue(audit.identity_longitudes_kill_product_endpoint_by_expression)
        self.assertTrue(audit.proves_product_endpoint_detector_by_expression)

    def test_identity_product_longitudes_force_identity_endpoint(self):
        c2 = cyclic_group(2)
        c3 = cyclic_group(3)

        audit = endpoint_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            endpoints=(0, 0),
            assignments=((1, 0), (1, 0)),
            expressions=((), ()),
        )

        self.assertEqual(audit.product_witness, ())
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.identity_product_longitude_signature_by_factors)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertTrue(audit.identity_longitudes_kill_product_endpoint_by_expression)

    def test_bad_endpoint_expression_does_not_certify_product_membership(self):
        c2 = cyclic_group(2)
        c3 = cyclic_group(3)

        audit = endpoint_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            endpoints=(1, 0),
            assignments=((1, 0), (1, 0)),
            expressions=((), ()),
        )

        self.assertTrue(audit.identity_product_longitude_signature_by_factors)
        self.assertFalse(audit.factor_audits[0].expression_matches_endpoint)
        self.assertNotEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertFalse(audit.product_witness_matches_endpoint)
        self.assertFalse(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )

    def test_terminal_gauge_telescopes_in_nonabelian_group(self):
        group = symmetric_group(3)
        labels = (group.identity, (1, 0, 2), (0, 2, 1))

        audit = terminal_gauge_telescoping_audit(group, labels)

        self.assertTrue(audit.labels_in_group)
        self.assertTrue(audit.gauge_factors_in_group)
        self.assertEqual(audit.terminal_endpoint, labels[-1])
        self.assertEqual(audit.telescoped_gauge_product, labels[-1])
        self.assertTrue(audit.gauge_factors_match_label_differences)
        self.assertTrue(audit.telescoped_product_matches_endpoint)
        self.assertTrue(audit.proves_terminal_gauge_telescoping)

    def test_terminal_gauge_expression_certifies_endpoint(self):
        group = cyclic_group(3)

        audit = terminal_gauge_longitude_expression_audit(
            group,
            n=2,
            braid_word=(1, 1),
            labels=(0, 1),
            assignment=(1, 0),
            expression=((1, 1),),
        )

        self.assertEqual(audit.telescope_audit.terminal_endpoint, 1)
        self.assertTrue(audit.telescope_audit.proves_terminal_gauge_telescoping)
        self.assertTrue(
            audit.terminal_gauge_lies_in_longitude_subgroup_by_expression
        )
        self.assertTrue(audit.identity_longitudes_kill_terminal_gauge_by_expression)

    def test_terminal_gauge_product_expression_uses_one_product_detector(self):
        c2 = cyclic_group(2)
        c3 = cyclic_group(3)

        audit = terminal_gauge_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1, 1),
            labels_by_factor=((0, 1), (0, 1)),
            assignments=((1, 0), (1, 0)),
            expressions=(((1, 1),), ((1, 1),)),
        )

        self.assertEqual(audit.terminal_endpoint_tuple, (1, 1))
        self.assertTrue(audit.all_terminal_gauges_telescope)
        self.assertEqual(audit.endpoint_audit.product_endpoint, (1, 1))
        self.assertTrue(audit.endpoint_audit.product_witness_matches_endpoint)
        self.assertTrue(
            audit.terminal_gauge_tuple_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertTrue(
            audit.identity_longitudes_kill_terminal_gauge_tuple_by_expression
        )

    def test_terminal_gauge_rejects_bad_supplied_factors(self):
        group = cyclic_group(3)

        audit = terminal_gauge_longitude_expression_audit(
            group,
            n=2,
            braid_word=(1, 1),
            labels=(0, 1),
            assignment=(1, 0),
            expression=((1, 1),),
            gauge_factors=(2,),
        )

        self.assertFalse(audit.telescope_audit.gauge_factors_match_label_differences)
        self.assertFalse(audit.telescope_audit.proves_terminal_gauge_telescoping)
        self.assertFalse(
            audit.terminal_gauge_lies_in_longitude_subgroup_by_expression
        )
        self.assertFalse(audit.identity_longitudes_kill_terminal_gauge_by_expression)

    def test_routed_lost_edge_endpoint_witness_covers_routed_edges(self):
        interval = one_color_identity_interval()
        routing = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )
        edge = routing.routed_edges[0]
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )

        audit = routed_lost_edge_endpoint_witness_audit(
            routing,
            ((edge, endpoint),),
        )

        self.assertEqual(audit.routed_edges, routing.routed_edges)
        self.assertEqual(audit.witnessed_edges, routing.routed_edges)
        self.assertEqual(audit.missing_routed_edges, ())
        self.assertEqual(audit.extra_witness_edges, ())
        self.assertTrue(audit.all_endpoint_witnesses_visible)
        self.assertTrue(audit.all_routed_edges_have_endpoint_witnesses)
        self.assertTrue(audit.proves_routed_lost_edge_endpoint_visibility)

    def test_routed_lost_edge_endpoint_witness_reports_missing_edge(self):
        interval = one_color_identity_interval()
        routing = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )

        audit = routed_lost_edge_endpoint_witness_audit(routing, ())

        self.assertEqual(audit.witnessed_edges, ())
        self.assertEqual(audit.missing_routed_edges, routing.routed_edges)
        self.assertFalse(audit.all_routed_edges_have_endpoint_witnesses)
        self.assertFalse(audit.proves_routed_lost_edge_endpoint_visibility)

    def test_routed_lost_edge_endpoint_witness_rejects_bad_endpoint_display(self):
        interval = one_color_identity_interval()
        routing = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )
        edge = routing.routed_edges[0]
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )

        audit = routed_lost_edge_endpoint_witness_audit(
            routing,
            ((edge, endpoint),),
        )

        self.assertFalse(audit.all_endpoint_witnesses_visible)
        self.assertEqual(audit.missing_routed_edges, routing.routed_edges)
        self.assertFalse(audit.proves_routed_lost_edge_endpoint_visibility)

    def test_universal_continuation_identity_endpoint_witness_covers_edges(self):
        interval = one_color_identity_interval()
        identity_routing = universal_continuation_identity_routing_audit(interval)
        edge = identity_routing.routing.routed_edges[0]
        c2 = cyclic_group(2)
        endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )

        audit = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            ((edge, endpoint),),
        )

        self.assertTrue(audit.identity_routing_proved)
        self.assertTrue(audit.endpoint_witnesses_proved)
        self.assertTrue(audit.routed_witness_uses_identity_routing)
        self.assertEqual(audit.routed_edges, identity_routing.routing.routed_edges)
        self.assertEqual(audit.witnessed_edges, identity_routing.routing.routed_edges)
        self.assertEqual(audit.missing_identity_routed_edges, ())
        self.assertEqual(audit.extra_witness_edges, ())
        self.assertEqual(audit.failure_reasons, ())
        self.assertTrue(
            audit.proves_universal_continuation_identity_endpoint_witnesses
        )
        self.assertTrue(audit.proves_routed_lost_edge_endpoint_visibility)

    def test_universal_continuation_identity_endpoint_witness_reports_missing_edge(
        self,
    ):
        interval = one_color_identity_interval()
        identity_routing = universal_continuation_identity_routing_audit(interval)

        audit = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            (),
        )

        self.assertTrue(audit.identity_routing_proved)
        self.assertFalse(audit.endpoint_witnesses_proved)
        self.assertEqual(
            audit.missing_identity_routed_edges,
            identity_routing.routing.routed_edges,
        )
        self.assertEqual(audit.failure_reasons, ("endpoint_witnesses_not_proved",))
        self.assertFalse(
            audit.proves_universal_continuation_identity_endpoint_witnesses
        )

    def test_universal_continuation_identity_endpoint_witness_rejects_empty_route(
        self,
    ):
        interval = one_color_identity_interval()
        real = universal_continuation_identity_routing_audit(interval)
        empty_routing = type(real.routing)(
            dichotomy=real.routing.dichotomy,
            routing_labels=real.routing.routing_labels,
            routing_kernel=real.routing.routing_kernel,
            lost_edges=(),
            routed_edges=(),
            unrouted_edges=(),
        )
        identity_routing = type(real)(
            descent_labels=real.descent_labels,
            routing=empty_routing,
        )

        audit = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            (),
        )

        self.assertFalse(identity_routing.proves_identity_routed_universal_continuation)
        self.assertEqual(audit.routed_edges, ())
        self.assertFalse(audit.endpoint_witnesses_proved)
        self.assertEqual(
            audit.failure_reasons,
            ("identity_routing_not_proved", "endpoint_witnesses_not_proved"),
        )
        self.assertFalse(
            audit.proves_universal_continuation_identity_endpoint_witnesses
        )

    def test_universal_continuation_symmetric_endpoint_fork_covers_edges(self):
        interval = one_color_identity_interval()
        identity_routing = universal_continuation_identity_routing_audit(interval)
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2, 3),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = universal_continuation_identity_symmetric_endpoint_fork_audit(
            identity_routing,
            endpoint_family,
            identity_routing.routing.routed_edges,
        )

        self.assertTrue(audit.identity_routing_proved)
        self.assertEqual(audit.routed_edges, identity_routing.routing.routed_edges)
        self.assertEqual(
            audit.supplied_covered_edges,
            identity_routing.routing.routed_edges,
        )
        self.assertEqual(audit.missing_identity_routed_edges, ())
        self.assertEqual(audit.extra_covered_edges, ())
        self.assertTrue(
            audit.proves_universal_continuation_identity_symmetric_endpoint_cutoff
        )
        self.assertEqual(audit.failure_reasons, ())

    def test_universal_continuation_symmetric_endpoint_fork_reports_missing_edge(
        self,
    ):
        interval = one_color_identity_interval()
        identity_routing = universal_continuation_identity_routing_audit(interval)
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = universal_continuation_identity_symmetric_endpoint_fork_audit(
            identity_routing,
            endpoint_family,
            (),
        )

        self.assertEqual(
            audit.missing_identity_routed_edges,
            identity_routing.routing.routed_edges,
        )
        self.assertFalse(
            audit.proves_universal_continuation_identity_symmetric_endpoint_cutoff
        )
        self.assertEqual(
            audit.failure_reasons,
            ("identity_routed_edges_not_covered",),
        )

    def test_universal_continuation_symmetric_endpoint_fork_rejects_empty_route(
        self,
    ):
        interval = one_color_identity_interval()
        real = universal_continuation_identity_routing_audit(interval)
        empty_routing = type(real.routing)(
            dichotomy=real.routing.dichotomy,
            routing_labels=real.routing.routing_labels,
            routing_kernel=real.routing.routing_kernel,
            lost_edges=(),
            routed_edges=(),
            unrouted_edges=(),
        )
        identity_routing = type(real)(
            descent_labels=real.descent_labels,
            routing=empty_routing,
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = universal_continuation_identity_symmetric_endpoint_fork_audit(
            identity_routing,
            endpoint_family,
            (),
        )

        self.assertEqual(audit.routed_edges, ())
        self.assertFalse(audit.all_identity_routed_edges_covered)
        self.assertFalse(
            audit.proves_universal_continuation_identity_symmetric_endpoint_cutoff
        )
        self.assertEqual(
            audit.failure_reasons,
            ("identity_routing_not_proved", "identity_routed_edges_not_covered"),
        )

    def test_mixed_unit_context_endpoint_witness_covers_routed_contexts(self):
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
                    right_explanation="partial_constant_hidden_rank_loss",
                    left_unit_inputs=(0, 1),
                    left_nonunit_inputs=(),
                    right_unit_inputs=(0,),
                    right_nonunit_inputs=(1,),
                ),
            ),
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

        audit = mixed_unit_context_endpoint_witness_audit(
            routing,
            ((("*", "*", "left"), endpoint),),
        )

        self.assertEqual(audit.mixed_context_keys, (("*", "*", "left"),))
        self.assertEqual(audit.witnessed_mixed_context_keys, (("*", "*", "left"),))
        self.assertEqual(audit.missing_mixed_context_keys, ())
        self.assertEqual(audit.extra_witness_keys, ())
        self.assertTrue(audit.coordinate_unit_routing_proved)
        self.assertTrue(audit.all_endpoint_witnesses_visible)
        self.assertTrue(audit.proves_mixed_unit_context_endpoint_witnesses)
        self.assertEqual(audit.failure_reasons, ())

    def test_mixed_unit_context_endpoint_witness_reports_missing_context(self):
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
                    right_explanation="partial_constant_hidden_rank_loss",
                    left_unit_inputs=(0, 1),
                    left_nonunit_inputs=(),
                    right_unit_inputs=(0,),
                    right_nonunit_inputs=(1,),
                ),
            ),
        )

        audit = mixed_unit_context_endpoint_witness_audit(routing, ())

        self.assertEqual(audit.missing_mixed_context_keys, (("*", "*", "left"),))
        self.assertFalse(audit.proves_mixed_unit_context_endpoint_witnesses)
        self.assertEqual(audit.failure_reasons, ("mixed_context_keys_not_covered",))

    def test_mixed_unit_symmetric_endpoint_fork_covers_routed_contexts(self):
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
                    right_explanation="partial_constant_hidden_rank_loss",
                    left_unit_inputs=(0, 1),
                    left_nonunit_inputs=(),
                    right_unit_inputs=(0,),
                    right_nonunit_inputs=(1,),
                ),
            ),
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = mixed_unit_context_symmetric_endpoint_fork_audit(
            routing,
            endpoint_family,
            (("*", "*", "left"),),
        )

        self.assertEqual(audit.mixed_context_keys, (("*", "*", "left"),))
        self.assertEqual(audit.supplied_covered_keys, (("*", "*", "left"),))
        self.assertEqual(audit.missing_mixed_context_keys, ())
        self.assertEqual(audit.extra_covered_keys, ())
        self.assertTrue(audit.coordinate_unit_routing_proved)
        self.assertTrue(audit.proves_mixed_unit_context_symmetric_endpoint_cutoff)
        self.assertEqual(audit.failure_reasons, ())

    def test_mixed_unit_symmetric_endpoint_fork_reports_missing_context(self):
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
                    right_explanation="partial_constant_hidden_rank_loss",
                    left_unit_inputs=(0, 1),
                    left_nonunit_inputs=(),
                    right_unit_inputs=(0,),
                    right_nonunit_inputs=(1,),
                ),
            ),
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        audit = mixed_unit_context_symmetric_endpoint_fork_audit(
            routing,
            endpoint_family,
            (),
        )

        self.assertEqual(audit.missing_mixed_context_keys, (("*", "*", "left"),))
        self.assertFalse(audit.proves_mixed_unit_context_symmetric_endpoint_cutoff)
        self.assertEqual(audit.failure_reasons, ("mixed_context_keys_not_covered",))

    def test_repair_contract_accepts_identity_endpoint_witness_wrapper(self):
        interval = one_color_identity_interval()
        identity_routing = universal_continuation_identity_routing_audit(interval)
        descent = identity_routing.routing.dichotomy.seed_saturation.saturated_descent
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )
        edge_endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )
        routed = universal_continuation_identity_endpoint_witness_audit(
            identity_routing,
            ((identity_routing.routing.routed_edges[0], edge_endpoint),),
        )

        audit = descent_endpoint_repair_contract_audit(descent, action, routed)

        self.assertTrue(routed.proves_routed_lost_edge_endpoint_visibility)
        self.assertTrue(audit.routed_edges_visible)
        self.assertTrue(audit.routed_edge_descent_matches_supplied_descent)
        self.assertEqual(audit.failure_reasons, ())
        self.assertTrue(audit.proves_repair_contract_for_supplied_data)

    def test_product_endpoint_expression_requires_parallel_data(self):
        with self.assertRaises(ValueError):
            endpoint_product_longitude_expression_audit(
                (cyclic_group(2),),
                n=2,
                braid_word=(1, 1),
                endpoints=(1,),
                assignments=(),
                expressions=(((1, 1),),),
            )

    def test_invalid_assignment_is_reported_without_product_witness(self):
        c2 = cyclic_group(2)

        audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((2, 0),),
            expressions=(((1, 1),),),
        )

        self.assertTrue(audit.all_endpoints_in_groups)
        self.assertFalse(audit.all_assignments_in_groups)
        self.assertIsNone(audit.product_witness)
        self.assertIsNone(audit.product_witness_value)
        self.assertFalse(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )

    def test_identity_endpoint_readout_records_fixed_coordinate(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )

        readout = endpoint_coordinate_readout_audit(product_audit, "p", "p")

        self.assertTrue(readout.endpoint_tuple_is_identity)
        self.assertTrue(readout.coordinate_fixed)
        self.assertTrue(readout.identity_endpoints_fix_coordinate)
        self.assertTrue(readout.identity_longitudes_kill_coordinate_by_expression)

    def test_identity_endpoint_readout_detects_unfaithful_moved_coordinate(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )

        readout = endpoint_coordinate_readout_audit(product_audit, "p", "q")

        self.assertTrue(readout.endpoint_tuple_is_identity)
        self.assertFalse(readout.coordinate_fixed)
        self.assertFalse(readout.identity_endpoints_fix_coordinate)
        self.assertFalse(readout.identity_longitudes_kill_coordinate_by_expression)

    def test_residual_readout_bundles_endpoint_controlled_coordinates(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        first = endpoint_coordinate_readout_audit(product_audit, "a", "a")
        second = endpoint_coordinate_readout_audit(product_audit, "b", "b")

        residual = endpoint_residual_readout_audit((first, second))

        self.assertEqual(residual.input_tuple, ("a", "b"))
        self.assertEqual(residual.output_tuple, ("a", "b"))
        self.assertTrue(residual.residual_tuple_fixed)
        self.assertTrue(residual.identity_endpoints_fix_all_coordinates)
        self.assertTrue(
            residual.identity_longitudes_kill_residual_tuple_by_expression
        )

    def test_residual_action_audit_records_complete_supplied_rows(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "a", "a"),)
        )

        action = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("a",),),
        )

        self.assertEqual(action.row_count, 1)
        self.assertTrue(action.covers_expected_rows)
        self.assertTrue(action.braid_data_consistent)
        self.assertTrue(action.all_identity_endpoints_fix_rows)
        self.assertTrue(action.all_identity_longitudes_kill_rows_by_expression)
        self.assertTrue(action.residual_action_identity_on_supplied_rows)
        self.assertTrue(action.proves_supplied_rows_detector_implication)
        self.assertTrue(action.proves_complete_residual_action_implication)

        row_count_only = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout,),
            expected_row_count=1,
        )
        self.assertFalse(row_count_only.expected_input_tuple_domain_supplied)
        self.assertFalse(row_count_only.input_tuple_domain_exact)
        self.assertTrue(row_count_only.proves_supplied_rows_detector_implication)
        self.assertFalse(row_count_only.proves_complete_residual_action_implication)

    def test_residual_action_audit_can_check_exact_input_tuple_domain(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout_a = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "a", "a"),)
        )
        readout_b = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "b", "b"),)
        )

        exact = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout_a, readout_b),
            expected_row_count=2,
            expected_input_tuples=(("a",), ("b",)),
        )
        self.assertEqual(exact.supplied_input_tuples, (("a",), ("b",)))
        self.assertTrue(exact.expected_input_tuple_domain_supplied)
        self.assertTrue(exact.input_tuple_domain_exact)
        self.assertTrue(exact.proves_complete_residual_action_implication)

        duplicate_supplied = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout_a, readout_a),
            expected_row_count=2,
            expected_input_tuples=(("a",), ("b",)),
        )
        self.assertFalse(duplicate_supplied.input_tuple_domain_exact)
        self.assertEqual(duplicate_supplied.duplicate_supplied_input_tuples, (("a",),))
        self.assertEqual(duplicate_supplied.missing_input_tuples, (("b",),))
        self.assertFalse(
            duplicate_supplied.proves_complete_residual_action_implication
        )

    def test_descent_endpoint_repair_contract_accepts_supplied_certificates(self):
        interval = one_color_identity_interval()
        descent = readout_descent_separation_audit(
            interval,
            {"*": {0: "collapsed", 1: "collapsed"}},
        )
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )

        audit = descent_endpoint_repair_contract_audit(descent, action)

        self.assertTrue(descent.proves_descent_separation_readout)
        self.assertTrue(action.proves_complete_residual_action_implication)
        self.assertEqual(audit.failure_reasons, ())
        self.assertTrue(audit.proves_repair_contract_for_supplied_data)

    def test_symmetric_repair_contract_bridge_uses_left_regular_degree(self):
        interval = one_color_identity_interval()
        descent = readout_descent_separation_audit(
            interval,
            {"*": {0: "collapsed", 1: "collapsed"}},
        )
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )
        repair = descent_endpoint_repair_contract_audit(descent, action)

        bridge = symmetric_repair_contract_bridge_audit(
            repair,
            detector_group_order=2,
        )

        self.assertEqual(bridge.symmetric_degree, 2)
        self.assertEqual(bridge.symmetric_group_order, 2)
        self.assertEqual(bridge.symmetric_detector_rack_size, 8)
        self.assertTrue(bridge.left_regular_embedding_available)
        self.assertEqual(bridge.failure_reasons, ())
        self.assertTrue(bridge.proves_symmetric_detector_from_repair_contract)

    def test_symmetric_repair_contract_bridge_rejects_bad_inputs(self):
        interval = one_color_identity_interval()
        descent = readout_descent_separation_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
        )
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )
        repair = descent_endpoint_repair_contract_audit(descent, action)

        bridge = symmetric_repair_contract_bridge_audit(
            repair,
            detector_group_order=3,
            symmetric_degree=2,
        )

        self.assertFalse(bridge.repair_contract_proved)
        self.assertFalse(bridge.left_regular_embedding_available)
        self.assertEqual(
            bridge.failure_reasons,
            ("repair_contract_not_proved", "symmetric_degree_too_small"),
        )
        self.assertFalse(bridge.proves_symmetric_detector_from_repair_contract)

    def test_endpoint_family_symmetric_fork_records_positive_cutoff(self):
        audit = endpoint_family_symmetric_fork_audit(
            (2, 6, 3),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
        )

        self.assertEqual(audit.minimum_symmetric_degree, 6)
        self.assertEqual(audit.symmetric_degree, 6)
        self.assertTrue(audit.endpoint_group_orders_valid)
        self.assertTrue(audit.symmetric_degree_covers_endpoint_groups)
        self.assertTrue(audit.endpoint_rows_cover_factors)
        self.assertTrue(audit.endpoint_rows_supply_witnesses)
        self.assertTrue(audit.endpoint_rows_are_faithful)
        self.assertTrue(audit.endpoint_cutoff_proved)
        self.assertTrue(audit.faithful_endpoint_cutoff_proved)
        self.assertEqual(audit.failure_reasons, ())

        boolean_only = EndpointFamilySymmetricForkAudit(
            endpoint_group_orders=(2, 6, 3),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
            symmetric_degree=6,
        )
        self.assertFalse(boolean_only.endpoint_cutoff_proved)
        self.assertFalse(boolean_only.faithful_endpoint_cutoff_proved)
        self.assertIn("endpoint_family_rows_not_exact", boolean_only.failure_reasons)

        wrong_row = endpoint_family_symmetric_fork_audit(
            (2, 6, 3),
            all_endpoint_witnesses_supplied=True,
            endpoint_family_faithful=True,
            endpoint_rows=(
                EndpointFamilySymmetricForkRow(0, 2, True, True),
                EndpointFamilySymmetricForkRow(1, 5, True, True),
                EndpointFamilySymmetricForkRow(2, 3, True, True),
            ),
        )
        self.assertFalse(wrong_row.endpoint_cutoff_proved)
        self.assertIn("endpoint_family_row_order_mismatch", wrong_row.failure_reasons)

    def test_endpoint_family_symmetric_fork_records_tail_seed_prefix(self):
        audit = endpoint_family_symmetric_fork_audit(
            (2, 3),
            all_endpoint_witnesses_supplied=False,
            endpoint_family_faithful=True,
            symmetric_degree=2,
            failed_symmetric_degrees=(3, 4, 5),
        )

        self.assertEqual(audit.minimum_symmetric_degree, 3)
        self.assertFalse(audit.endpoint_cutoff_proved)
        self.assertTrue(audit.failed_degrees_are_tail_prefix)
        self.assertTrue(audit.proves_supplied_symmetric_tail_endpoint_seed_prefix)
        self.assertEqual(audit.failure_reasons, ("endpoint_witnesses_not_supplied", "symmetric_degree_too_small"))

    def test_endpoint_family_symmetric_fork_requires_faithfulness_for_local_use(self):
        audit = endpoint_family_symmetric_fork_audit(
            (),
            all_endpoint_witnesses_supplied=False,
            endpoint_family_faithful=False,
        )

        self.assertTrue(audit.endpoint_family_empty)
        self.assertTrue(audit.endpoint_cutoff_proved)
        self.assertFalse(audit.faithful_endpoint_cutoff_proved)
        self.assertFalse(audit.proves_supplied_symmetric_tail_endpoint_seed_prefix)
        self.assertEqual(audit.failure_reasons, ("endpoint_family_not_faithful",))

    def test_endpoint_family_symmetric_seed_attaches_endpoint_miss_to_local_row(self):
        total = rack_solution([0, 1, 2], lambda _left, right: (right + 1) % 3)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        base_detector = identity_solution(["q"])
        degree = 2
        local_prefix = local_symmetric_normalized_law_prefix_witness_audit(
            qmap,
            base_detector,
            degree,
            2,
            (1, 1, 1, 1),
            ("*", "*"),
            (0, 0),
            extra_strands=degree,
            fill_value=0,
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=False,
            endpoint_family_faithful=True,
            failed_symmetric_degrees=(2,),
        )

        audit = endpoint_family_symmetric_seed_audit(
            endpoint_family,
            local_prefix,
            degree,
            endpoint_channel_nonidentity=True,
            endpoint_miss_matches_residual_motion=True,
        )

        self.assertTrue(audit.uses_declared_symmetric_row)
        self.assertTrue(audit.right_stabilized_by_symmetric_degree)
        self.assertTrue(audit.symmetric_degree_covers_endpoint_family)
        self.assertTrue(audit.degree_is_declared_endpoint_failure)
        self.assertTrue(audit.local_prefix_is_symmetric_normalized_law_row)
        self.assertTrue(audit.endpoint_channel_miss_is_nonidentity)
        self.assertTrue(audit.endpoint_miss_matches_prefix_motion)
        self.assertTrue(audit.endpoint_miss_is_attached_to_prefix)
        self.assertTrue(audit.proves_one_endpoint_family_symmetric_seed)

        boolean_only = EndpointFamilySymmetricSeedAudit(
            endpoint_family,
            local_prefix,
            degree,
            endpoint_channel_nonidentity=True,
            endpoint_miss_matches_residual_motion=True,
        )
        self.assertFalse(boolean_only.endpoint_channel_miss_is_nonidentity)
        self.assertFalse(boolean_only.endpoint_miss_matches_prefix_motion)
        self.assertFalse(boolean_only.endpoint_miss_is_attached_to_prefix)
        self.assertFalse(boolean_only.proves_one_endpoint_family_symmetric_seed)

    def test_endpoint_family_symmetric_seed_requires_attachment_flags(self):
        total = rack_solution([0, 1], lambda _left, right: 1 - right)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        base_detector = identity_solution(["q"])
        local_prefix = local_symmetric_normalized_law_prefix_witness_audit(
            qmap,
            base_detector,
            1,
            2,
            pure_braid_generator(1, 2),
            ("*", "*"),
            (0, 0),
            extra_strands=1,
            fill_value=0,
        )
        endpoint_family = endpoint_family_symmetric_fork_audit(
            (2,),
            all_endpoint_witnesses_supplied=False,
            endpoint_family_faithful=True,
            failed_symmetric_degrees=(2,),
        )

        audit = endpoint_family_symmetric_seed_audit(
            endpoint_family,
            local_prefix,
            1,
            endpoint_channel_nonidentity=True,
            endpoint_miss_matches_residual_motion=False,
        )

        self.assertTrue(audit.local_prefix_is_symmetric_normalized_law_row)
        self.assertFalse(audit.symmetric_degree_covers_endpoint_family)
        self.assertFalse(audit.degree_is_declared_endpoint_failure)
        self.assertFalse(audit.endpoint_miss_is_attached_to_prefix)
        self.assertFalse(audit.proves_one_endpoint_family_symmetric_seed)

    def test_descent_endpoint_repair_contract_reports_descent_failure(self):
        interval = one_color_identity_interval()
        descent = readout_descent_separation_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
        )
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )

        audit = descent_endpoint_repair_contract_audit(descent, action)

        self.assertFalse(descent.proves_descent_separation_readout)
        self.assertEqual(audit.failure_reasons, ("descent_separation_not_proved",))
        self.assertFalse(audit.proves_repair_contract_for_supplied_data)

    def test_descent_endpoint_repair_contract_reports_endpoint_failure(self):
        interval = one_color_identity_interval()
        descent = readout_descent_separation_audit(
            interval,
            {"*": {0: "collapsed", 1: "collapsed"}},
        )
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "q"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )

        audit = descent_endpoint_repair_contract_audit(descent, action)

        self.assertTrue(descent.proves_descent_separation_readout)
        self.assertFalse(action.proves_complete_residual_action_implication)
        self.assertEqual(
            audit.failure_reasons,
            ("endpoint_action_detector_not_proved",),
        )
        self.assertFalse(audit.proves_repair_contract_for_supplied_data)

    def test_descent_endpoint_repair_contract_accepts_matching_routed_edges(self):
        interval = one_color_identity_interval()
        routing = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )
        descent = routing.dichotomy.seed_saturation.saturated_descent
        c2 = cyclic_group(2)
        edge = routing.routed_edges[0]
        edge_endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        routed_edges = routed_lost_edge_endpoint_witness_audit(
            routing,
            ((edge, edge_endpoint),),
        )
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )

        audit = descent_endpoint_repair_contract_audit(
            descent,
            action,
            routed_edges,
        )

        self.assertTrue(routed_edges.proves_routed_lost_edge_endpoint_visibility)
        self.assertTrue(audit.routed_edge_descent_matches_supplied_descent)
        self.assertEqual(audit.failure_reasons, ())
        self.assertTrue(audit.proves_repair_contract_for_supplied_data)

    def test_descent_endpoint_repair_contract_reports_routed_descent_mismatch(self):
        interval = one_color_identity_interval()
        routing = lost_edge_external_routing_audit(
            interval,
            {"*": {0: "zero", 1: "one"}},
            {"*": {0: "left", 1: "right"}},
        )
        mismatched_descent = readout_descent_separation_audit(
            one_color_flip_interval(),
            {"*": {0: "zero", 1: "one"}},
        )
        c2 = cyclic_group(2)
        edge = routing.routed_edges[0]
        edge_endpoint = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        routed_edges = routed_lost_edge_endpoint_witness_audit(
            routing,
            ((edge, edge_endpoint),),
        )
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, -1),
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "p", "p"),)
        )
        action = endpoint_residual_action_audit(
            2,
            (1, -1),
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("p",),),
        )

        audit = descent_endpoint_repair_contract_audit(
            mismatched_descent,
            action,
            routed_edges,
        )

        self.assertTrue(mismatched_descent.proves_descent_separation_readout)
        self.assertTrue(routed_edges.proves_routed_lost_edge_endpoint_visibility)
        self.assertFalse(audit.routed_edge_descent_matches_supplied_descent)
        self.assertEqual(audit.failure_reasons, ("routed_edge_descent_mismatch",))
        self.assertFalse(audit.proves_repair_contract_for_supplied_data)

    def test_residual_action_audit_requires_expected_row_coverage(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "a", "a"),)
        )

        action = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout,),
            expected_row_count=2,
            expected_input_tuples=(("a",), ("b",)),
        )

        self.assertFalse(action.covers_expected_rows)
        self.assertTrue(action.proves_supplied_rows_detector_implication)
        self.assertFalse(action.proves_complete_residual_action_implication)

    def test_residual_action_audit_rejects_inconsistent_braid_data(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "a", "a"),)
        )

        action = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("a",),),
        )

        self.assertFalse(action.braid_data_consistent)
        self.assertFalse(action.proves_supplied_rows_detector_implication)
        self.assertFalse(action.proves_complete_residual_action_implication)

    def test_readout_implication_is_vacuous_for_visible_product_longitudes(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1, 1),
            endpoints=(1,),
            assignments=((1, 0),),
            expressions=(((1, 1),),),
        )

        readout = endpoint_coordinate_readout_audit(product_audit, "p", "q")

        self.assertFalse(product_audit.identity_product_longitude_signature_by_factors)
        self.assertFalse(readout.endpoint_tuple_is_identity)
        self.assertFalse(readout.coordinate_fixed)
        self.assertTrue(readout.identity_endpoints_fix_coordinate)
        self.assertTrue(readout.identity_longitudes_kill_coordinate_by_expression)

    def test_residual_action_audit_rejects_unfaithful_identity_endpoint_row(self):
        c2 = cyclic_group(2)
        product_audit = endpoint_product_longitude_expression_audit(
            (c2,),
            n=2,
            braid_word=(1,) * 4,
            endpoints=(0,),
            assignments=((1, 0),),
            expressions=((),),
        )
        readout = endpoint_residual_readout_audit(
            (endpoint_coordinate_readout_audit(product_audit, "a", "b"),)
        )

        action = endpoint_residual_action_audit(
            2,
            (1,) * 4,
            (readout,),
            expected_row_count=1,
            expected_input_tuples=(("a",),),
        )

        self.assertFalse(action.all_identity_endpoints_fix_rows)
        self.assertFalse(action.all_identity_longitudes_kill_rows_by_expression)
        self.assertFalse(action.residual_action_identity_on_supplied_rows)
        self.assertFalse(action.proves_supplied_rows_detector_implication)

    def test_residual_action_audit_rejects_negative_expected_row_count(self):
        with self.assertRaises(ValueError):
            endpoint_residual_action_audit(
                2,
                (1, 1),
                (),
                expected_row_count=-1,
            )


if __name__ == "__main__":
    unittest.main()
