import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    affine_cyclic_form,
    all_bijection_solutions,
    braid_images_for_words,
    braid_word_permutation_image,
    commutator,
    commutator_law_braid_moves,
    cyclic_group,
    free_word_power,
    generated_permutation_subgroup,
    group_exponent,
    is_rack_type,
    law_word_on_last_strand,
    longitude_identity_profile_for_law_braid,
    permutation_order,
    pure_braid_generator,
    solution_table_signature,
    symmetric_group,
)
from ybe_domination.finite_group import FiniteGroup


OUT = ROOT / "proofs" / "size3_candidate_detail.json"


def permutation_group_from_subgroup(subgroup):
    elements = tuple(sorted(subgroup))
    identity = tuple(range(len(elements[0])))

    def compose(left, right):
        return tuple(left[right[i]] for i in range(len(left)))

    table = {(a, b): compose(a, b) for a in elements for b in elements}
    return FiniteGroup(elements, identity, table)


def moved_tuple(solution, braid_index, braid_word):
    for tup in product(solution.elements, repeat=braid_index):
        image = solution.braid_action(braid_word, tup)
        if image != tup:
            return tup, image
    return None


def projection_form(solution):
    """Detect whether either output coordinate depends on only one input."""

    elements = solution.elements
    first_depends_only_on_y = all(
        len({solution.R[(x, y)][0] for x in elements}) == 1 for y in elements
    )
    first_depends_only_on_x = all(
        len({solution.R[(x, y)][0] for y in elements}) == 1 for x in elements
    )
    second_depends_only_on_y = all(
        len({solution.R[(x, y)][1] for x in elements}) == 1 for y in elements
    )
    second_depends_only_on_x = all(
        len({solution.R[(x, y)][1] for y in elements}) == 1 for x in elements
    )
    return {
        "first_depends_only_on_x": first_depends_only_on_x,
        "first_depends_only_on_y": first_depends_only_on_y,
        "second_depends_only_on_x": second_depends_only_on_x,
        "second_depends_only_on_y": second_depends_only_on_y,
    }


def candidate_records(max_checked=50000, limit=3):
    word = commutator(free_word_power(0, 1), free_word_power(1, 1))
    braid_index, braid_word = law_word_on_last_strand(word, arity=2)
    longitude_groups = {
        "C2": cyclic_group(2),
        "C3": cyclic_group(3),
        "C5": cyclic_group(5),
        "S3": symmetric_group(3),
    }
    longitude_invisible, longitude_visible = longitude_identity_profile_for_law_braid(
        longitude_groups, word, arity=2
    )
    records = []
    ybe_solutions_examined = 0
    for solution in all_bijection_solutions(3, max_checked=max_checked):
        ybe_solutions_examined += 1
        if is_rack_type(solution):
            continue
        if not commutator_law_braid_moves(solution):
            continue
        pure_generators = {i - 1: pure_braid_generator(i, braid_index) for i in range(1, braid_index)}
        images = braid_images_for_words(solution, braid_index, pure_generators)
        subgroup = generated_permutation_subgroup(images.values(), max_size=10000)
        subgroup_group = permutation_group_from_subgroup(subgroup)
        moved = moved_tuple(solution, braid_index, braid_word)
        commutator_image = braid_word_permutation_image(solution, braid_index, braid_word)
        records.append(
            {
                "table_order": [(x, y) for x in solution.elements for y in solution.elements],
                "table_values": [list(value) for value in solution_table_signature(solution)],
                "is_ybe": solution.is_ybe(),
                "is_rack_type": is_rack_type(solution),
                "affine_cyclic_form": affine_cyclic_form(solution),
                "projection_form": projection_form(solution),
                "commutator_braid_index": braid_index,
                "commutator_braid_word": list(braid_word),
                "commutator_longitude_invisible_groups": list(longitude_invisible),
                "commutator_longitude_visible_groups": list(longitude_visible),
                "moved_tuple": repr(moved[0]) if moved else None,
                "moved_image": repr(moved[1]) if moved else None,
                "commutator_action_support_size_at_q3": sum(
                    1 for index, image in enumerate(commutator_image) if image != index
                ),
                "commutator_action_order_at_q3": permutation_order(commutator_image),
                "pure_image_subgroup_size_at_q3": len(subgroup),
                "pure_image_subgroup_exponent_at_q3": group_exponent(subgroup_group),
            }
        )
        if len(records) >= limit:
            break
    return {
        "table_prefix_max_checked": max_checked,
        "ybe_solutions_examined_until_limit": ybe_solutions_examined,
        "candidate_count_returned": len(records),
        "records": records,
    }


def main():
    OUT.write_text(json.dumps(candidate_records(), indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
