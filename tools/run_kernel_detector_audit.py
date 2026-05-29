import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    CongruenceInterval,
    FiniteBraidedSet,
    QuotientMap,
    all_bijection_solutions,
    branch_tags,
    bounded_words,
    commutator,
    congruences,
    detector_collision_failures,
    exact_detector_image_audit,
    first_moved_tuple,
    free_word_power,
    interval_covers,
    invisible_to_all_groups,
    identity_solution,
    is_identity_action,
    is_involutive_solution,
    is_rack_type,
    kernel_action_groups,
    kernel_symmetric_groups,
    law_word_on_last_strand,
    solution_from_local_interval,
    solution_table_signature,
)


OUT = ROOT / "proofs" / "kernel_detector_audit.json"
_BLIND_WORD_CACHE = {}


def size_three_affine_candidate():
    pairs = [(x, y) for x in range(3) for y in range(3)]
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


def commutator_law_braid():
    word = commutator(free_word_power(0, 1), free_word_power(1, 1))
    return law_word_on_last_strand(word, arity=2)


def moved_signature(moved):
    if moved is None:
        return None
    start, image = moved
    return {
        "start": [repr(value) for value in start],
        "image": [repr(value) for value in image],
    }


def summarize_solution(solution):
    n, braid = commutator_law_braid()
    moved = first_moved_tuple(solution, n, braid)
    actual_groups = kernel_action_groups(solution)
    symmetric_groups = kernel_symmetric_groups(solution, max_degree=3)
    return {
        "element_count": len(solution.elements),
        "is_rack_type": is_rack_type(solution),
        "is_involutive_solution": is_involutive_solution(solution),
        "branch_tags": list(branch_tags(solution)),
        "commutator_moves": moved is not None,
        "moved_tuple": moved_signature(moved),
        "actual_kernel_group_orders": [len(group.elements) for group in actual_groups],
        "symmetric_kernel_group_orders": [
            len(group.elements) for group in symmetric_groups
        ],
        "actual_kernel_groups_blind": invisible_to_all_groups(actual_groups, n, braid),
        "symmetric_kernel_groups_blind": invisible_to_all_groups(
            symmetric_groups, n, braid
        ),
    }


def exact_image_examples(solution):
    qmap = one_point_quotient(solution)
    groups = kernel_symmetric_groups(solution, max_degree=3)
    n2 = exact_detector_image_audit(qmap, qmap.quotient, groups, 2, state_limit=10000)
    n3 = exact_detector_image_audit(qmap, qmap.quotient, groups, 3, state_limit=1000)
    return {
        "n2": {
            "visited_state_count": n2.visited_state_count,
            "detector_state_count": n2.detector_state_count,
            "residual_state_count": n2.residual_state_count,
            "base_kernel_detector_state_count": n2.base_kernel_detector_state_count,
            "base_kernel_residual_state_count": n2.base_kernel_residual_state_count,
            "truncated": n2.truncated,
            "proves_fixed_n_implication": n2.proves_fixed_n_implication,
            "has_kernel_failure": n2.kernel_failure is not None,
            "has_collision_failure": n2.collision_failure is not None,
        },
        "n3_cap_1000": {
            "visited_state_count": n3.visited_state_count,
            "detector_state_count": n3.detector_state_count,
            "residual_state_count": n3.residual_state_count,
            "base_kernel_detector_state_count": n3.base_kernel_detector_state_count,
            "base_kernel_residual_state_count": n3.base_kernel_residual_state_count,
            "truncated": n3.truncated,
            "proves_fixed_n_implication": n3.proves_fixed_n_implication,
            "has_kernel_failure": n3.kernel_failure is not None,
            "has_collision_failure": n3.collision_failure is not None,
        },
    }


def one_point_quotient(solution):
    quotient = identity_solution(("*",))
    return QuotientMap(solution, quotient, {element: "*" for element in solution.elements})


def table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def groups_key(groups):
    return tuple(group.elements for group in groups)


def group_blind_words(groups, n, words):
    key = (groups_key(groups), n, tuple(words))
    if key not in _BLIND_WORD_CACHE:
        _BLIND_WORD_CACHE[key] = tuple(
            word for word in words if invisible_to_all_groups(groups, n, word)
        )
    return _BLIND_WORD_CACHE[key]


def first_residual_blind_mover(qmap, base_detector, groups, n, words):
    for word in group_blind_words(groups, n, words):
        if not is_identity_action(base_detector, n, word):
            continue
        moved = qmap.moved_residual_tuple(n, word)
        if moved is not None:
            return tuple(word), moved
    return None


def scan_solutions(size):
    n, braid = commutator_law_braid()
    ybe_count = 0
    commutator_mover_count = 0
    actual_kernel_blind_mover_count = 0
    symmetric_kernel_blind_mover_count = 0
    symmetric_kernel_visible_mover_count = 0
    first_actual_blind = []
    first_symmetric_blind = []
    for solution in all_bijection_solutions(size):
        ybe_count += 1
        moved = first_moved_tuple(solution, n, braid)
        if moved is None:
            continue
        commutator_mover_count += 1
        actual_groups = kernel_action_groups(solution)
        symmetric_groups = kernel_symmetric_groups(solution, max_degree=3)
        actual_blind = invisible_to_all_groups(actual_groups, n, braid)
        symmetric_blind = invisible_to_all_groups(symmetric_groups, n, braid)
        if actual_blind:
            actual_kernel_blind_mover_count += 1
            if len(first_actual_blind) < 5:
                first_actual_blind.append(
                    {
                        "branch_tags": list(branch_tags(solution)),
                        "is_rack_type": is_rack_type(solution),
                        "is_involutive_solution": is_involutive_solution(solution),
                        "actual_kernel_group_orders": [
                            len(group.elements) for group in actual_groups
                        ],
                        "symmetric_kernel_group_orders": [
                            len(group.elements) for group in symmetric_groups
                        ],
                        "table_values": table_signature(solution),
                        "moved_tuple": moved_signature(moved),
                    }
                )
        if symmetric_blind:
            symmetric_kernel_blind_mover_count += 1
            if len(first_symmetric_blind) < 5:
                first_symmetric_blind.append(
                    {
                        "branch_tags": list(branch_tags(solution)),
                        "is_rack_type": is_rack_type(solution),
                        "is_involutive_solution": is_involutive_solution(solution),
                        "symmetric_kernel_group_orders": [
                            len(group.elements) for group in symmetric_groups
                        ],
                        "table_values": table_signature(solution),
                        "moved_tuple": moved_signature(moved),
                    }
                )
        else:
            symmetric_kernel_visible_mover_count += 1
    return {
        "size": size,
        "ybe_count": ybe_count,
        "commutator_mover_count": commutator_mover_count,
        "actual_kernel_blind_mover_count": actual_kernel_blind_mover_count,
        "symmetric_kernel_blind_mover_count": symmetric_kernel_blind_mover_count,
        "symmetric_kernel_visible_mover_count": symmetric_kernel_visible_mover_count,
        "first_actual_kernel_blind_movers": first_actual_blind,
        "first_symmetric_kernel_blind_movers": first_symmetric_blind,
    }


def scan_bounded_words_on_solutions(size, n=3, max_word_length=4):
    words = bounded_words(n, max_word_length)
    ybe_count = 0
    actual_blind_solution_count = 0
    symmetric_blind_solution_count = 0
    symmetric_collision_solution_count = 0
    first_symmetric_blind = []
    first_symmetric_collisions = []
    for solution in all_bijection_solutions(size):
        ybe_count += 1
        qmap = one_point_quotient(solution)
        actual = first_residual_blind_mover(
            qmap,
            qmap.quotient,
            kernel_action_groups(solution),
            n,
            words,
        )
        symmetric = first_residual_blind_mover(
            qmap,
            qmap.quotient,
            kernel_symmetric_groups(solution, max_degree=3),
            n,
            words,
        )
        if actual:
            actual_blind_solution_count += 1
        if symmetric:
            symmetric_blind_solution_count += 1
            if len(first_symmetric_blind) < 5:
                word, moved = symmetric
                first_symmetric_blind.append(
                    {
                        "word": list(word),
                        "branch_tags": list(branch_tags(solution)),
                        "is_rack_type": is_rack_type(solution),
                        "is_involutive_solution": is_involutive_solution(solution),
                        "symmetric_kernel_group_orders": [
                            len(group.elements)
                            for group in kernel_symmetric_groups(
                                solution, max_degree=3
                            )
                        ],
                        "table_values": table_signature(solution),
                        "moved_tuple": moved_signature(moved[1:]),
                    }
                )
        collisions = detector_collision_failures(
            qmap,
            qmap.quotient,
            kernel_symmetric_groups(solution, max_degree=3),
            n,
            words,
            max_failures=1,
        )
        if collisions:
            symmetric_collision_solution_count += 1
            if len(first_symmetric_collisions) < 5:
                first = collisions[0]
                first_symmetric_collisions.append(
                    {
                        "first_word": list(first["first_word"]),
                        "second_word": list(first["second_word"]),
                        "branch_tags": list(branch_tags(solution)),
                        "is_rack_type": is_rack_type(solution),
                        "is_involutive_solution": is_involutive_solution(solution),
                        "symmetric_kernel_group_orders": [
                            len(group.elements)
                            for group in kernel_symmetric_groups(
                                solution, max_degree=3
                            )
                        ],
                        "table_values": table_signature(solution),
                    }
                )
    return {
        "size": size,
        "n": n,
        "max_word_length": max_word_length,
        "word_count": len(words),
        "ybe_count": ybe_count,
        "actual_kernel_blind_solution_count": actual_blind_solution_count,
        "symmetric_kernel_blind_solution_count": symmetric_blind_solution_count,
        "symmetric_kernel_collision_solution_count": symmetric_collision_solution_count,
        "first_symmetric_kernel_blind_solutions": first_symmetric_blind,
        "first_symmetric_kernel_collision_solutions": first_symmetric_collisions,
    }


def scan_local_minimal_intervals(size):
    n, braid = commutator_law_braid()
    local_minimal_cover_count = 0
    commutator_mover_interval_count = 0
    actual_kernel_blind_mover_interval_count = 0
    symmetric_kernel_blind_mover_interval_count = 0
    first_symmetric_blind = []
    for solution in all_bijection_solutions(size):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_cover_count += 1
            total = solution_from_local_interval(interval).total
            moved = first_moved_tuple(total, n, braid)
            if moved is None:
                continue
            commutator_mover_interval_count += 1
            actual_groups = kernel_action_groups(total)
            symmetric_groups = kernel_symmetric_groups(total, max_degree=3)
            if invisible_to_all_groups(actual_groups, n, braid):
                actual_kernel_blind_mover_interval_count += 1
            if invisible_to_all_groups(symmetric_groups, n, braid):
                symmetric_kernel_blind_mover_interval_count += 1
                if len(first_symmetric_blind) < 5:
                    first_symmetric_blind.append(
                        {
                            "interval_total_branch_tags": list(branch_tags(total)),
                            "interval_total_is_involutive": is_involutive_solution(total),
                            "symmetric_kernel_group_orders": [
                                len(group.elements) for group in symmetric_groups
                            ],
                            "moved_tuple": moved_signature(moved),
                        }
                    )
    return {
        "size": size,
        "local_minimal_cover_count": local_minimal_cover_count,
        "commutator_mover_interval_count": commutator_mover_interval_count,
        "actual_kernel_blind_mover_interval_count": (
            actual_kernel_blind_mover_interval_count
        ),
        "symmetric_kernel_blind_mover_interval_count": (
            symmetric_kernel_blind_mover_interval_count
        ),
        "first_symmetric_kernel_blind_mover_intervals": first_symmetric_blind,
    }


def scan_bounded_words_on_local_minimal_intervals(size, n=3, max_word_length=4):
    words = bounded_words(n, max_word_length)
    local_minimal_cover_count = 0
    actual_blind_interval_count = 0
    symmetric_blind_interval_count = 0
    symmetric_collision_interval_count = 0
    first_symmetric_blind = []
    first_symmetric_collisions = []
    for solution in all_bijection_solutions(size):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_cover_count += 1
            qmap = solution_from_local_interval(interval)
            actual = first_residual_blind_mover(
                qmap,
                qmap.quotient,
                kernel_action_groups(qmap.total),
                n,
                words,
            )
            symmetric = first_residual_blind_mover(
                qmap,
                qmap.quotient,
                kernel_symmetric_groups(qmap.total, max_degree=3),
                n,
                words,
            )
            if actual:
                actual_blind_interval_count += 1
            if symmetric:
                symmetric_blind_interval_count += 1
                if len(first_symmetric_blind) < 5:
                    word, moved = symmetric
                    first_symmetric_blind.append(
                        {
                            "word": list(word),
                            "interval_total_branch_tags": list(branch_tags(qmap.total)),
                            "interval_total_is_involutive": is_involutive_solution(
                                qmap.total
                            ),
                            "symmetric_kernel_group_orders": [
                                len(group.elements)
                                for group in kernel_symmetric_groups(
                                    qmap.total, max_degree=3
                                )
                            ],
                            "moved_base": [repr(value) for value in moved[0]],
                            "moved_tuple": moved_signature(moved[1:]),
                        }
                    )
            collisions = detector_collision_failures(
                qmap,
                qmap.quotient,
                kernel_symmetric_groups(qmap.total, max_degree=3),
                n,
                words,
                max_failures=1,
            )
            if collisions:
                symmetric_collision_interval_count += 1
                if len(first_symmetric_collisions) < 5:
                    first = collisions[0]
                    first_symmetric_collisions.append(
                        {
                            "first_word": list(first["first_word"]),
                            "second_word": list(first["second_word"]),
                            "interval_total_branch_tags": list(branch_tags(qmap.total)),
                            "interval_total_is_involutive": is_involutive_solution(
                                qmap.total
                            ),
                            "symmetric_kernel_group_orders": [
                                len(group.elements)
                                for group in kernel_symmetric_groups(
                                    qmap.total, max_degree=3
                                )
                            ],
                        }
                    )
    return {
        "size": size,
        "n": n,
        "max_word_length": max_word_length,
        "word_count": len(words),
        "local_minimal_cover_count": local_minimal_cover_count,
        "actual_kernel_blind_interval_count": actual_blind_interval_count,
        "symmetric_kernel_blind_interval_count": symmetric_blind_interval_count,
        "symmetric_kernel_collision_interval_count": (
            symmetric_collision_interval_count
        ),
        "first_symmetric_kernel_blind_intervals": first_symmetric_blind,
        "first_symmetric_kernel_collision_intervals": first_symmetric_collisions,
    }


def main():
    n, braid = commutator_law_braid()
    examples = {
        "size3_affine_commutator_candidate": size_three_affine_candidate(),
    }
    report = {
        "commutator_law_braid": {
            "n": n,
            "word": list(braid),
        },
        "examples": {
            name: summarize_solution(solution) for name, solution in examples.items()
        },
        "exact_image_examples": {
            name: exact_image_examples(solution) for name, solution in examples.items()
        },
        "small_scans": {
            "size_2_exhaustive": scan_solutions(2),
            "size_3_exhaustive": scan_solutions(3),
        },
        "local_minimal_scans": {
            "size_2_exhaustive": scan_local_minimal_intervals(2),
            "size_3_exhaustive": scan_local_minimal_intervals(3),
        },
        "bounded_word_scans": {
            "size_2_exhaustive_n3_len4": scan_bounded_words_on_solutions(2),
            "size_3_exhaustive_n3_len4": scan_bounded_words_on_solutions(3),
        },
        "bounded_local_minimal_scans": {
            "size_2_exhaustive_n3_len4": scan_bounded_words_on_local_minimal_intervals(2),
            "size_3_exhaustive_n3_len4": scan_bounded_words_on_local_minimal_intervals(3),
        },
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
