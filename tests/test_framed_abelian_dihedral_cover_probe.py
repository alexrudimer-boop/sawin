from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "proofs" / "framed_abelian_dihedral_cover_probe.json"
AUDIT_MD = ROOT / "proofs" / "framed_abelian_dihedral_cover_probe.md"


class FramedAbelianDihedralCoverProbeTest(unittest.TestCase):
    def test_probe_certifies_doubled_dihedral_rows_in_arity_two(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertEqual(report["title"], "Framed abelian dihedral cover probe")
        self.assertEqual(report["arity"], 2)
        self.assertEqual(report["exponents_checked"], list(range(2, 9)))
        self.assertTrue(report["all_doubled_rows_certified"])
        self.assertFalse(report["proves_all_arity_theorem"])
        self.assertEqual(
            report["theorem_artifact"],
            "proofs/framed_abelian_dihedral_cover_theorem.md",
        )

        doubled_rows = [
            row for row in report["rows"]
            if row["detector_label"] == "doubled_Dih_C2e"
        ]
        self.assertEqual(len(doubled_rows), 7)
        for row in doubled_rows:
            self.assertEqual(row["rotation_order"], 2 * row["exponent"])
            self.assertFalse(row["audit"]["kernel_contains_nonidentity"])
            self.assertFalse(row["audit"]["truncated"])
            self.assertTrue(row["audit"]["kernel_containment_certified"])

    def test_probe_records_naive_even_parity_failures(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertIn(2, report["naive_failure_exponents"])
        self.assertIn(4, report["naive_failure_exponents"])
        self.assertNotIn(3, report["naive_failure_exponents"])
        self.assertNotIn(5, report["naive_failure_exponents"])

        row_by_key = {
            (row["exponent"], row["detector_label"]): row
            for row in report["rows"]
        }
        c4_naive = row_by_key[(4, "naive_Dih_Ce")]
        self.assertTrue(c4_naive["audit"]["kernel_contains_nonidentity"])
        self.assertEqual(c4_naive["audit"]["first_witness_word"], [1, 1, 1, 1])

    def test_markdown_records_scope_boundary(self) -> None:
        markdown = AUDIT_MD.read_text(encoding="utf-8")

        self.assertIn("Dih(C_{2e}) covers A_Ce", markdown)
        self.assertIn("naive", markdown)
        self.assertIn("even-exponent", markdown)
        self.assertIn("proves all-arity theorem: `False`", markdown)
        self.assertIn("separate theorem artifact", markdown)


if __name__ == "__main__":
    unittest.main()
