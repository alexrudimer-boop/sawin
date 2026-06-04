import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_minimal_rigid_core_exclusion_boundary import build_report


class MinimalRigidCoreExclusionBoundaryTests(unittest.TestCase):
    def test_exclusion_theorem_is_the_recorded_positive_endpoint(self):
        report = build_report()
        theorem = report["strict_smaller_theorem"]
        implication = report["implication"]

        self.assertEqual(theorem["name"], "Minimal rigid-core exclusion")
        self.assertEqual(len(theorem["conditions"]), 8)
        self.assertIn("no nontrivial total YBE quotient", theorem["conditions"][3])
        self.assertIn("no proper active-factor certificate", theorem["conditions"][7])
        self.assertIn("finite rack", implication["conclusion"])
        self.assertIn("minimal counterexample", implication["argument"])

    def test_negative_endpoint_requires_cofinal_rack_prefix_pressure(self):
        report = build_report()
        negative = report["negative_target"]

        self.assertIn("P_m", negative["rack_prefix"])
        self.assertIn("Gamma_{m,n}", negative["joint_image"])
        self.assertIn("N_{m,n}", negative["detector_kernel_image"])
        self.assertEqual(
            negative["cofinal_obstruction"],
            "for all m there exists n with N_{m,n}(X) != 1",
        )

    def test_current_status_does_not_claim_resolution(self):
        report = build_report()

        self.assertIn("not a proof", report["status"])
        self.assertTrue(
            any("No proof" in item for item in report["current_known_status"])
        )
        self.assertTrue(
            any("No finite table" in item for item in report["current_known_status"])
        )


if __name__ == "__main__":
    unittest.main()
