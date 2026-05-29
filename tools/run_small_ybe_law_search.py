import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import small_solution_summary


OUT = ROOT / "proofs" / "small_ybe_law_search.json"


def main():
    report = {
        "size_2_exhaustive": small_solution_summary(2),
        "size_3_prefix_50000": small_solution_summary(3, max_checked=50000),
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
