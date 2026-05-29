import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    braid_images_for_words,
    generated_permutation_subgroup,
    group_exponent,
    pure_braid_generator,
    rack_solution,
    solution_from_local_interval,
    LocalInterval,
)
from ybe_domination.finite_group import FiniteGroup


OUT = ROOT / "proofs" / "moving_image_growth_audit.json"


def permutation_group_from_subgroup(subgroup):
    elements = tuple(sorted(subgroup))
    identity = tuple(range(len(elements[0])))

    def compose(left, right):
        return tuple(left[right[i]] for i in range(len(left)))

    table = {(a, b): compose(a, b) for a in elements for b in elements}
    return FiniteGroup(elements, identity, table)


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


def size3_commutator_candidate():
    pairs = list(product(range(3), repeat=2))
    signature = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 2),
        (0, 2),
        (1, 2),
        (1, 1),
        (2, 1),
        (0, 1),
    ]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, signature)))


def summarize(solution, max_q, max_subgroup_size, max_tuple_count):
    rows = []
    for q in range(2, max_q + 1):
        tuple_count = len(solution.elements) ** q
        if tuple_count > max_tuple_count:
            rows.append(
                {
                    "braid_index": q,
                    "tuple_count": tuple_count,
                    "pure_generator_count": q - 1,
                    "subgroup_size_limit": max_subgroup_size,
                    "tuple_count_limit": max_tuple_count,
                    "skipped": True,
                    "skip_reason": "tuple_count exceeds configured audit limit",
                }
            )
            continue
        pure_generators = {i - 1: pure_braid_generator(i, q) for i in range(1, q)}
        images = braid_images_for_words(solution, q, pure_generators)
        row = {
            "braid_index": q,
            "tuple_count": tuple_count,
            "pure_generator_count": len(images),
            "subgroup_size_limit": max_subgroup_size,
            "tuple_count_limit": max_tuple_count,
            "skipped": False,
        }
        try:
            subgroup = generated_permutation_subgroup(
                images.values(), max_size=max_subgroup_size
            )
            group = permutation_group_from_subgroup(subgroup)
            row.update(
                {
                    "subgroup_size": len(subgroup),
                    "subgroup_exponent": group_exponent(group),
                    "truncated": False,
                }
            )
        except ValueError:
            row.update(
                {
                    "subgroup_size": f">{max_subgroup_size}",
                    "subgroup_exponent": None,
                    "truncated": True,
                }
            )
        rows.append(row)
    return rows


def main():
    solutions = {
        "trivial_rack_2": rack_solution([0, 1], lambda a, b: b),
        "dihedral_quandle_3": rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3),
        "one_colour_permutation_interval": solution_from_local_interval(
            one_color_permutation_interval()
        ).total,
        "size3_commutator_candidate": size3_commutator_candidate(),
    }
    report = {
        name: summarize(
            solution,
            max_q=5,
            max_subgroup_size=2000,
            max_tuple_count=30,
        )
        for name, solution in solutions.items()
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
