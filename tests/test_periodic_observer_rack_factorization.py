import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_periodic_observer_rack_factorization_audit import build_report


class PeriodicObserverRackFactorizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_theorem_records_local_equations_and_kernel_conclusion(self):
        theorem = self.report["theorem"]

        self.assertEqual(theorem["name"], "Periodic observer-rack factorization")
        self.assertEqual(len(theorem["local_equations"]), 4)
        self.assertIn("ker rho^Y_n <= ker rho^X_n", theorem["conclusion"])
        self.assertTrue(any("injectivity" in step for step in theorem["proof_steps"]))

    def test_examples_include_s3_and_affine_tetrahedral_cases(self):
        examples = {row["name"]: row for row in self.report["examples"]}

        self.assertEqual(
            examples["observer_product_s3_conjugation"]["status"],
            "kernel equality",
        )
        self.assertEqual(examples["affine_f2_q3_tetrahedral"]["period"], 3)
        self.assertIn(
            "tetrahedral",
            examples["affine_f2_q3_tetrahedral"]["rack"],
        )
        self.assertEqual(
            examples["inert_observer_pointwise_subcase"]["artifact"],
            "proofs/inert_observer_rack_factor_audit.md",
        )

    def test_relationship_to_sawin_is_not_equivalence(self):
        relation = self.report["relationship_to_sawin"]

        self.assertIn("not an equivalent reformulation", relation["strictly_stronger_than_domination"])
        self.assertIn("pair automaton", relation["finite_checkability"])
        self.assertIn("sizes 5 and 6", self.report["next_computation"])
        self.assertTrue(self.report["next_prompt"].endswith("_ask_now.md"))


if __name__ == "__main__":
    unittest.main()
