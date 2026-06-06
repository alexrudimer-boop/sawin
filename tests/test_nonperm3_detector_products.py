import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.nonperm3_detector_products import (
    detector_components_by_ybe_table,
    extract_detector_schema_records,
    nonpermutation_size3_flat_tables,
    normalize_rack_table,
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

        self.assertEqual(len(records), 3)
        self.assertEqual(len(grouped), 1)
        self.assertEqual(
            grouped[(0, 1, 6, 3, 4, 7, 2, 5, 8)],
            (
                ((0, 1), (0, 1)),
                ((0, 1, 2), (0, 1, 2), (0, 1, 2)),
            ),
        )

    def test_normalize_flat_rack_table(self):
        self.assertEqual(
            normalize_rack_table([0, 1, 0, 1]),
            ((0, 1), (0, 1)),
        )


if __name__ == "__main__":
    unittest.main()
