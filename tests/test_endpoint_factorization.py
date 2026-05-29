import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    cyclic_group,
    endpoint_coordinate_readout_audit,
    endpoint_longitude_expression_audit,
    endpoint_product_longitude_expression_audit,
    endpoint_residual_action_audit,
    endpoint_residual_readout_audit,
)


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
        self.assertFalse(audit.identity_longitudes_kill_product_endpoint_by_expression)

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
        )

        self.assertEqual(action.row_count, 1)
        self.assertTrue(action.covers_expected_rows)
        self.assertTrue(action.braid_data_consistent)
        self.assertTrue(action.all_identity_endpoints_fix_rows)
        self.assertTrue(action.all_identity_longitudes_kill_rows_by_expression)
        self.assertTrue(action.residual_action_identity_on_supplied_rows)
        self.assertTrue(action.proves_supplied_rows_detector_implication)
        self.assertTrue(action.proves_complete_residual_action_implication)

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
