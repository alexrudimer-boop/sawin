from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "proofs" / "framed_to_conjugation_b2_probe.json"
AUDIT_MD = ROOT / "proofs" / "framed_to_conjugation_b2_probe.md"


class FramedToConjugationB2ProbeTest(unittest.TestCase):
    def test_probe_records_two_strand_order_compatibility(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertEqual(report["title"], "Framed-to-conjugation two-strand probe")
        framed = {row["name"]: row for row in report["framed_rows"]}
        self.assertEqual(framed["A_C2"]["rack_size"], 4)
        self.assertEqual(framed["A_C2"]["sigma_order"], 4)
        self.assertEqual(framed["A_C2"]["sigma_squared_order"], 2)
        self.assertEqual(framed["T2 x A_C2"]["rack_size"], 8)
        self.assertEqual(framed["T2 x A_C2"]["sigma_order"], 4)

        conjugation = {row["name"]: row for row in report["conjugation_rows"]}
        self.assertEqual(conjugation["C2^conj"]["sigma_order"], 2)
        self.assertFalse(conjugation["C2^conj"]["b2_kernel_subset_framed_c2_kernel"])
        self.assertEqual(conjugation["S3^conj"]["sigma_order"], 12)
        self.assertTrue(conjugation["S3^conj"]["b2_kernel_subset_framed_c2_kernel"])
        self.assertEqual(conjugation["S4^conj"]["sigma_order"], 24)
        self.assertTrue(conjugation["S4^conj"]["b2_kernel_subset_framed_c2_kernel"])

        self.assertTrue(report["s3_b2_kernel_covers_framed_c2"])
        self.assertFalse(report["proves_higher_arity_conjugation_cover"])

    def test_markdown_records_boundary(self) -> None:
        markdown = AUDIT_MD.read_text(encoding="utf-8")

        self.assertIn("S3 B2 kernel covers framed C2: `True`", markdown)
        self.assertIn("proves higher-arity conjugation cover: `False`", markdown)
        self.assertIn("| S3^conj | 6 | 12 | 6 | True |", markdown)
        self.assertIn("only a two-strand compatibility check", markdown)


if __name__ == "__main__":
    unittest.main()
