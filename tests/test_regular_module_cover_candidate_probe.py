from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "proofs" / "regular_module_cover_candidate_probe.json"
AUDIT_MD = ROOT / "proofs" / "regular_module_cover_candidate_probe.md"


class RegularModuleCoverCandidateProbeTest(unittest.TestCase):
    def test_probe_records_positive_low_arity_rows(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertEqual(report["title"], "Regular-module cover candidate probe")
        self.assertEqual(report["candidate"], "C_reg(G)=F_2[G] semidirect G")
        self.assertTrue(report["all_residual_rows_certified"])
        self.assertFalse(report["proves_regular_module_fox_separation"])

        rows = {
            (row["group"], row["arity"], row["kind"]): row
            for row in report["rows"]
        }
        self.assertTrue(
            rows[("C2", 2, "residual")]["audit"]["kernel_containment_certified"]
        )
        self.assertTrue(
            rows[("C2", 3, "residual")]["audit"]["kernel_containment_certified"]
        )
        self.assertTrue(
            rows[("C3", 2, "residual")]["audit"]["kernel_containment_certified"]
        )
        self.assertTrue(
            rows[("S3", 2, "b2_order")]["b2_kernel_containment_by_order"]
        )

    def test_probe_records_expected_sizes(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
        rows = {
            (row["group"], row["arity"], row["kind"]): row
            for row in report["rows"]
        }

        c2_n3 = rows[("C2", 3, "residual")]
        self.assertEqual(c2_n3["detector_group_order"], 8)
        self.assertEqual(c2_n3["audit"]["joint_image_size"], 48)
        self.assertEqual(c2_n3["audit"]["solution_image_size"], 48)
        self.assertFalse(c2_n3["audit"]["truncated"])

        s3_b2 = rows[("S3", 2, "b2_order")]
        self.assertEqual(s3_b2["group_order"], 6)
        self.assertEqual(s3_b2["detector_group_order"], 384)
        self.assertEqual(s3_b2["solution_sigma_order"], 12)
        self.assertEqual(s3_b2["detector_sigma_order"], 24)

    def test_markdown_keeps_boundary_explicit(self) -> None:
        markdown = AUDIT_MD.read_text(encoding="utf-8")

        self.assertIn("does not prove the regular-module cover", markdown)
        self.assertIn("Fox-separation proof", markdown)
        self.assertIn("proves regular-module Fox separation: `False`", markdown)
        self.assertIn("### S3 arity 2", markdown)


if __name__ == "__main__":
    unittest.main()
