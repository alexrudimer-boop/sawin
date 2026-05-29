import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    commutator,
    free_word_power,
    law_braid_action_certificate,
    rack_solution,
    solution_from_local_interval,
    LocalInterval,
)


OUT = ROOT / "proofs" / "action_image_law_audit.json"


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


def summarize_solution(name, solution, word, arity):
    certificate = law_braid_action_certificate(
        solution, word, arity, max_subgroup_size=10000
    )
    return {
        "solution": name,
        "braid_index": certificate.braid_index,
        "tuple_count": certificate.tuple_count,
        "generator_image_subgroup_size": certificate.generator_image_subgroup_size,
        "generator_image_subgroup_exponent": certificate.generator_image_subgroup_exponent,
        "word_is_law_on_image_subgroup": certificate.word_is_law_on_image_subgroup,
        "evaluated_word_is_identity": certificate.evaluated_word_is_identity,
        "direct_braid_is_identity": certificate.direct_braid_is_identity,
        "direct_matches_evaluated": certificate.direct_matches_evaluated,
    }


def main():
    comm = commutator(free_word_power(0, 1), free_word_power(1, 1))
    solutions = {
        "trivial_rack_2": rack_solution([0, 1], lambda a, b: b),
        "dihedral_quandle_3": rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3),
        "one_colour_permutation_interval": solution_from_local_interval(
            one_color_permutation_interval()
        ).total,
    }
    rows = {
        name: summarize_solution(name, solution, comm, arity=2)
        for name, solution in solutions.items()
    }
    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
