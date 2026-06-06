import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.nonperm3_detector_products import (
    detector_components_by_ybe_table,
    detector_index_by_ybe_table,
    extract_detector_schema_records,
    nonpermutation_size3_flat_tables,
    normalize_rack_table,
    verify_width3_audit_payload,
)


class NonPerm3DetectorProductTests(unittest.TestCase):
    def test_nonpermutation_size_three_table_count(self):
        tables = nonpermutation_size3_flat_tables()

        self.assertEqual(len(tables), 55)
        self.assertEqual(len(set(tables)), 55)
        self.assertTrue(all(len(table) == 9 for table in tables))

    def test_extracts_and_deduplicates_schema_like_records(self):
        payload = {
            "positive_detector_schemas": [
                {
                    "id": "D1",
                    "ybe_table": "0 1 6 3 4 7 2 5 8",
                    "rack": {"table": ["0 1", "0 1"]},
                },
                {
                    "id": "D1-duplicate-target",
                    "ybe_table": [0, 1, 6, 3, 4, 7, 2, 5, 8],
                    "rack_table": [[0, 1], [0, 1]],
                },
                {
                    "id": "D2",
                    "ybe_table": [0, 1, 6, 3, 4, 7, 2, 5, 8],
                    "rack": {"table": [[0, 1, 2], [0, 1, 2], [0, 1, 2]]},
                },
            ],
            "metadata": {"rack": {"table": [[0]]}},
        }

        records = extract_detector_schema_records(payload)
        grouped = detector_components_by_ybe_table((payload,))
        detector_index = detector_index_by_ybe_table((payload,))

        self.assertEqual(len(records), 3)
        self.assertEqual(records[0].source_schema_ids, ("D1",))
        self.assertEqual(records[1].source_schema_ids, ("D1-duplicate-target",))
        self.assertEqual(records[2].source_schema_ids, ("D2",))
        self.assertEqual(len(grouped), 1)
        self.assertEqual(
            grouped[(0, 1, 6, 3, 4, 7, 2, 5, 8)],
            (
                ((0, 1), (0, 1)),
                ((0, 1, 2), (0, 1, 2), (0, 1, 2)),
            ),
        )
        self.assertEqual(
            tuple(
                component.source_schema_ids
                for component in detector_index[(0, 1, 6, 3, 4, 7, 2, 5, 8)]
            ),
            (("D1", "D1-duplicate-target"), ("D2",)),
        )

    def test_normalize_flat_rack_table(self):
        self.assertEqual(
            normalize_rack_table([0, 1, 0, 1]),
            ((0, 1), (0, 1)),
        )

    def test_current_import_gap_artifact_verifies_structurally(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads(
            (root / "proofs" / "nonperm3_detector_product_import_gap.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(verify_width3_audit_payload(payload), tuple())

    def test_width3_audit_row_verifier_checks_quotient_arithmetic(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads(
            (root / "proofs" / "nonperm3_detector_product_import_gap.json").read_text(
                encoding="utf-8"
            )
        )
        table = payload["detector_index"][0]["ybe_table"]
        row = {
            "ybe_table": table,
            "detector_component_count": 1,
            "detector_component_sizes": [2],
            "bound": 3,
            "arity": 4,
            "joint_image_size": 24,
            "kernel_image_size": 1,
            "parabolic_image_size": 1,
            "quotient_size": 1,
            "quotient_nontrivial": False,
            "seed_count": 0,
            "first_witness_word": None,
            "first_moved_tuple": None,
            "first_moved_tuple_image": None,
            "truncated": False,
        }
        payload["rows"] = [row]
        payload["row_count"] = 1
        payload["run_audit"] = True

        self.assertEqual(verify_width3_audit_payload(payload), tuple())

        bad_payload = deepcopy(payload)
        bad_payload["rows"][0]["quotient_size"] = 2
        failures = verify_width3_audit_payload(bad_payload)
        self.assertTrue(
            any("quotient_size arithmetic mismatch" in failure for failure in failures)
        )


if __name__ == "__main__":
    unittest.main()
