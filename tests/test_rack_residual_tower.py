import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import identity_solution, rack_residual_obstruction_audit, rack_solution


class RackResidualTowerTests(unittest.TestCase):
    def test_detector_equal_to_solution_has_trivial_residual_kernel(self):
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)

        audit = rack_residual_obstruction_audit(cyclic, cyclic, n=3)

        self.assertFalse(audit.truncated)
        self.assertFalse(audit.kernel_contains_nonidentity)
        self.assertFalse(audit.proves_fixed_width_domination_failure)

    def test_trivial_detector_finds_cyclic_rack_mover(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        detector = identity_solution(("z",))

        audit = rack_residual_obstruction_audit(solution, detector, n=2)

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.kernel_contains_nonidentity)
        self.assertTrue(audit.proves_fixed_width_domination_failure)
        self.assertEqual(audit.first_witness_word, (1,))
        self.assertNotEqual(audit.first_moved_tuple, audit.first_moved_tuple_image)


if __name__ == "__main__":
    unittest.main()
