import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class AffineF2Q3SmallRackNativeDetectorTests(unittest.TestCase):
    def test_size_four_rack_24_matches_candidate_through_arity_five(self):
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_small_rack_native_detector_audit.json")
            .read_text(encoding="utf-8")
        )

        self.assertEqual(report["rack_representative_count"], 28)
        self.assertEqual(report["two_strand_viable_count"], 8)
        self.assertEqual(len(report["unobstructed_nontruncated_rows"]), 1)

        survivor = report["unobstructed_nontruncated_rows"][0]
        self.assertEqual(survivor["rack_index"], 24)
        self.assertEqual(survivor["rack_size"], 4)
        self.assertEqual(survivor["explored_state_count"], 77760)
        self.assertEqual(survivor["detector_image_order"], 77760)
        self.assertEqual(survivor["x_image_order"], 77760)
        self.assertFalse(survivor["obstruction_found"])

        promising = report["promising_rack"]
        self.assertEqual(promising["rack_index"], 24)
        self.assertTrue(promising["kernel_inclusion_holds_through_checked_arities"])
        self.assertTrue(promising["image_orders_match_through_checked_arities"])
        self.assertEqual(
            [row["x_image_order"] for row in promising["checked_rows"]],
            [3, 24, 648, 77760],
        )


if __name__ == "__main__":
    unittest.main()
