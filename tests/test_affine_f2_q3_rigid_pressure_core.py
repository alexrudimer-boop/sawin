import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution
from run_affine_f2_q3_pressure_audit import _block_matrix
from tools.run_affine_f2_q3_rigid_pressure_core_audit import (
    affine_square_is_identity,
    generated_congruence_block_count,
    offset_tuple,
    quotient_rigidity_witness,
    valid_affine_offsets,
)
from ybe_domination import one_state_invariant_observer_partition
from ybe_domination import proper_subsolution_subsets


class AffineF2Q3RigidPressureCoreTests(unittest.TestCase):
    def test_generated_audit_records_repaired_bounded_prefix_pressure(self):
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_rigid_pressure_core_audit.json")
            .read_text(encoding="utf-8")
        )
        counts = report["counts"]

        self.assertEqual(counts["linear_ybe_block_count"], 26153)
        self.assertEqual(counts["affine_ybe_table_count"], 226241)
        self.assertEqual(counts["terminal_without_flip_count"], 58688)
        self.assertEqual(counts["rigid_structural_survivor_count"], 3360)

        candidate = report["first_rigid_pressure_candidate"]
        self.assertTrue(candidate["finite_prefix_pressure_repaired_by_size3_rack"])
        pressure = candidate["first_bounded_ordered_prefix_pressure"]
        self.assertEqual(pressure["detector_size"], 36)
        self.assertEqual(pressure["arity"], 2)
        self.assertTrue(pressure["obstruction_found"])
        self.assertEqual(pressure["first_witness_word"], [1, 1, 1, 1])

        repair = candidate["dihedral_size3_repair"]
        self.assertEqual(repair["detector_size"], 3)
        self.assertEqual(repair["detector_two_strand_order"], 3)
        self.assertTrue(repair["kernel_inclusion_holds_through_checked_arities"])
        self.assertTrue(repair["image_orders_match_through_checked_arities"])
        self.assertEqual(
            [row["joint_image_size"] for row in repair["checked_rows"]],
            [3, 24, 648],
        )
        tetrahedral = candidate["tetrahedral_size4_resolution"]
        self.assertEqual(tetrahedral["detector_size"], 4)
        self.assertTrue(tetrahedral["kernel_equality_all_arities"])
        self.assertEqual(
            tetrahedral["proof_artifact"],
            "proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md",
        )
        self.assertEqual(
            tetrahedral["operation_rows"],
            [
                [0, 2, 3, 1],
                [3, 1, 0, 2],
                [1, 3, 2, 0],
                [2, 0, 1, 3],
            ],
        )

    def test_first_candidate_satisfies_structural_filters(self):
        blocks = (10, 265, 220, 349)
        offset = 12
        matrix = _block_matrix(*blocks)
        solution = affine_solution(matrix, offset_tuple(offset), 3)

        self.assertIn(offset, valid_affine_offsets(blocks))
        self.assertFalse(affine_square_is_identity(blocks, offset))
        self.assertEqual(len(one_state_invariant_observer_partition(solution)), 1)
        self.assertEqual(proper_subsolution_subsets(solution), tuple())
        quotient_rigid, witness = quotient_rigidity_witness(solution)
        self.assertTrue(quotient_rigid, witness)

        for left_index, left in enumerate(solution.elements):
            for right in solution.elements[left_index + 1 :]:
                self.assertEqual(
                    generated_congruence_block_count(solution, (left, right)),
                    1,
                )


if __name__ == "__main__":
    unittest.main()
