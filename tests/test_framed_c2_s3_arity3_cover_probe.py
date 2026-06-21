from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "proofs" / "framed_c2_s3_arity3_cover_probe.json"
AUDIT_MD = ROOT / "proofs" / "framed_c2_s3_arity3_cover_probe.md"


class FramedC2S3Arity3CoverProbeTest(unittest.TestCase):
    def test_probe_records_arity_2_and_3_kernel_containments(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertEqual(report["title"], "Framed C2 versus S3 arity-3 cover probe")
        self.assertEqual(report["solution"], "A_C2")
        self.assertEqual(report["detector"], "S3^conj")
        self.assertEqual(report["arities_checked"], [2, 3])
        self.assertTrue(report["all_checked_kernel_containments_certified"])
        self.assertFalse(report["proves_all_arity_cover"])

        rows = {row["n"]: row for row in report["rows"]}
        self.assertEqual(rows[2]["joint_image_size"], 12)
        self.assertEqual(rows[2]["solution_image_size"], 4)
        self.assertEqual(rows[2]["detector_image_size"], 12)
        self.assertEqual(rows[2]["kernel_size"], 1)
        self.assertFalse(rows[2]["kernel_contains_nonidentity"])
        self.assertFalse(rows[2]["truncated"])
        self.assertTrue(rows[2]["kernel_containment_certified"])

        self.assertEqual(rows[3]["joint_image_size"], 279936)
        self.assertEqual(rows[3]["solution_image_size"], 48)
        self.assertEqual(rows[3]["detector_image_size"], 279936)
        self.assertEqual(rows[3]["kernel_size"], 1)
        self.assertFalse(rows[3]["kernel_contains_nonidentity"])
        self.assertFalse(rows[3]["truncated"])
        self.assertTrue(rows[3]["kernel_containment_certified"])

    def test_markdown_records_scope_boundary(self) -> None:
        markdown = AUDIT_MD.read_text(encoding="utf-8")

        self.assertIn("arities 2 and 3", markdown)
        self.assertIn("K_n(S3^conj) subset K_n(A_C2)", markdown)
        self.assertIn("for arity 2 and 3 only", markdown)
        self.assertIn("does not prove the all-arity", markdown)
        self.assertIn("| 3 | 279936 | 48 | 279936 | 1 | False | False | True |", markdown)


if __name__ == "__main__":
    unittest.main()
