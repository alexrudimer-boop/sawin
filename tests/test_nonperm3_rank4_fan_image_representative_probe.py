from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "proofs" / "nonperm3_rank4_fan_image_representative_probe.json"
AUDIT_MD = ROOT / "proofs" / "nonperm3_rank4_fan_image_representative_probe.md"


class Nonperm3Rank4FanImageRepresentativeProbeTest(unittest.TestCase):
    def test_json_records_representative_profiles(self) -> None:
        report = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))

        self.assertEqual(
            report["title"],
            "Nonpermutation size-3 rank-4 fan-image representative probe",
        )
        self.assertEqual(report["rank"], 4)
        self.assertEqual(report["arity"], 5)
        self.assertEqual(report["state_count"], 243)
        self.assertEqual(report["max_group_size"], 200000)
        self.assertEqual(
            report["representative_rows"],
            {
                "trivial_representative": 0,
                "abelian_representative": 6,
                "hard_representative": 15,
            },
        )

        trivial = report["rows"]["trivial_representative"]
        abelian = report["rows"]["abelian_representative"]
        hard = report["rows"]["hard_representative"]

        self.assertEqual(trivial["order"], 1)
        self.assertEqual(abelian["order"], 16)
        self.assertTrue(abelian["is_abelian"])
        self.assertEqual(hard["order"], 51840)
        self.assertEqual(hard["exponent"], 360)
        self.assertEqual(hard["generator_orders"], [3, 3, 3, 3])
        self.assertEqual(hard["generator_pair_product_orders"], [6, 6, 6, 6, 6, 6])
        self.assertFalse(hard["is_abelian"])

    def test_markdown_states_scope_limit(self) -> None:
        markdown = AUDIT_MD.read_text(encoding="utf-8")

        self.assertIn("rank-4 fan-image representative probe", markdown)
        self.assertIn("order 51840", markdown)
        self.assertIn("not a full rank-4 corpus classification", markdown)
        self.assertIn("next finite pressure point", markdown)


if __name__ == "__main__":
    unittest.main()

