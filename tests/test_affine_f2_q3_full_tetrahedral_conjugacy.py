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
        self.assertTrue(report["all_checked_phi_bijective"])
        self.assertTrue(report["all_checked_p_equivariant"])
        self.assertTrue(report["all_checked_r_invariant"])
        self.assertTrue(report["all_checked_conjugacy"])
        for row in report["rows"]:
            n = row["arity"]
            self.assertEqual(row["phi_rank"], 3 * n)
            self.assertTrue(row["phi_bijective"])
            self.assertTrue(row["p_equivariant"])
            self.assertTrue(row["r_invariant"])
            self.assertTrue(row["phi_conjugates_generators"])


if __name__ == "__main__":
    unittest.main()
