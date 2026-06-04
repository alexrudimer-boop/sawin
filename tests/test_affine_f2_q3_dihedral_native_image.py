import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))


class AffineF2Q3DihedralNativeImageTests(unittest.TestCase):
    def test_generated_native_audit_records_d3_failure_at_arity_five(self):
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_dihedral_native_image_audit.json")
            .read_text(encoding="utf-8")
        )

        self.assertFalse(report["any_truncated"])
        self.assertFalse(report["all_computed_orders_match"])
        self.assertEqual(report["first_d3_failure_arity"], 5)

        rows = {row["arity"]: row for row in report["rows"]}
        self.assertEqual(rows[2]["d3_image_order"], 3)
        self.assertEqual(rows[2]["x_image_order"], 3)
        self.assertEqual(rows[3]["d3_image_order"], 24)
        self.assertEqual(rows[3]["x_image_order"], 24)
        self.assertEqual(rows[4]["d3_image_order"], 648)
        self.assertEqual(rows[4]["x_image_order"], 648)
        self.assertEqual(rows[5]["d3_image_order"], 51840)
        self.assertEqual(rows[5]["x_image_order"], 77760)

        witness = report["first_d3_kernel_witness"]
        self.assertFalse(witness["truncated"])
        self.assertEqual(witness["arity"], 5)
        self.assertEqual(witness["witness_word_length"], 25)
        self.assertEqual(
            witness["moved_zero_tuple_image"],
            [[1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 0], [0, 1, 1]],
        )


if __name__ == "__main__":
    unittest.main()
