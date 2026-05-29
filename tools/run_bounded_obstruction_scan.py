import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    LocalInterval,
    bounded_local_obstructions,
    cyclic_group,
    identity_solution,
    symmetric_group,
)


OUT = ROOT / "proofs" / "bounded_obstruction_scan.json"


def one_color_permutation_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    flip = {0: 1, 1: 0}
    table = {
        ("*", "*", x, y): (flip[y], x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, table)


def encode_obstructions(obstructions):
    return [
        {
            "braid_word": list(item.braid_word),
            "moved_base": repr(item.moved_base),
            "moved_tuple": repr(item.moved_tuple),
            "moved_image": repr(item.moved_image),
            "invisible_groups": list(item.invisible_groups),
            "visible_groups": list(item.visible_groups),
        }
        for item in obstructions.values()
    ]


def main():
    interval = one_color_permutation_interval()
    base_detector = identity_solution(["*"])
    scans = {}
    group_sets = {
        "trivial_only": {"trivial": cyclic_group(1)},
        "cyclic_2_3": {"C2": cyclic_group(2), "C3": cyclic_group(3)},
        "cyclic_2_3_and_S3": {
            "C2": cyclic_group(2),
            "C3": cyclic_group(3),
            "S3": symmetric_group(3),
        },
    }
    for name, groups in group_sets.items():
        obstructions = bounded_local_obstructions(
            interval,
            base_detector,
            groups,
            n=2,
            max_word_length=6,
        )
        scans[name] = {
            "group_count": len(groups),
            "n": 2,
            "max_word_length": 6,
            "obstruction_count": len(obstructions),
            "obstructions": encode_obstructions(obstructions),
        }
    OUT.write_text(json.dumps(scans, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
