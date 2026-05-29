import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    LocalInterval,
    braid_action_order,
    cyclic_group,
    has_identity_longitude_signature,
    lcm_upto,
    solution_from_local_interval,
    symmetric_group,
    two_strand_exponent_law_braid,
)


OUT = ROOT / "proofs" / "law_shortcut_audit.json"


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


def main():
    groups = {"C2": cyclic_group(2), "C3": cyclic_group(3), "S3": symmetric_group(3)}
    qmap = solution_from_local_interval(one_color_permutation_interval())
    pure_generator = (1, 1)
    action_order = braid_action_order(qmap.total, 2, pure_generator)
    rows = []
    for bound in range(1, 7):
        braid = two_strand_exponent_law_braid(bound)
        visible = []
        invisible = []
        for name, group in groups.items():
            if has_identity_longitude_signature(group, 2, braid):
                invisible.append(name)
            else:
                visible.append(name)
        moved = qmap.moved_residual_tuple(2, braid)
        rows.append(
            {
                "bound": bound,
                "lcm_1_to_bound": lcm_upto(bound),
                "braid_word_length": len(braid),
                "pure_generator_action_order": action_order,
                "moves_interval": moved is not None,
                "moved_tuple": repr(moved) if moved is not None else None,
                "longitude_invisible_groups": invisible,
                "longitude_visible_groups": visible,
            }
        )
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
