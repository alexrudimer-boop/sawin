from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3FullTetrahedralConjugacyAuditTest(unittest.TestCase):
    def test_full_tetrahedral_conjugacy_certificate(self) -> None:
        report = json.loads(
            (
                ROOT
                / "proofs"
                / "affine_f2_q3_full_tetrahedral_conjugacy_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(report["max_arity"], 30)
        self.assertEqual(report["max_state_arity"], 6)
        self.assertTrue(report["all_checked_phi_bijective"])
        self.assertTrue(report["all_checked_p_equivariant"])
        self.assertTrue(report["all_checked_r_invariant"])
        self.assertTrue(report["all_checked_conjugacy"])
        self.assertTrue(report["all_state_checked_phi_bijective"])
        self.assertTrue(report["all_state_checked_p_equivariant"])
        self.assertTrue(report["all_state_checked_r_invariant"])
        self.assertTrue(report["all_state_checked_x_braid_relations"])
        for row in report["rows"]:
            n = row["arity"]
            self.assertEqual(row["phi_rank"], 3 * n)
            self.assertTrue(row["phi_bijective"])
            self.assertTrue(row["p_equivariant"])
            self.assertTrue(row["r_invariant"])
            self.assertTrue(row["phi_conjugates_generators"])
        self.assertEqual(
            [row["state_count"] for row in report["state_rows"]],
            [8, 64, 512, 4096, 32768, 262144],
        )
        for row in report["state_rows"]:
            self.assertTrue(row["phi_bijective_on_states"])
            self.assertTrue(row["p_equivariant_on_states"])
            self.assertTrue(row["r_invariant_on_states"])
            self.assertTrue(row["x_adjacent_braid_relations_on_states"])
            self.assertTrue(row["x_distant_commute_relations_on_states"])


if __name__ == "__main__":
    unittest.main()
