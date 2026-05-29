import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    CongruenceInterval,
    all_bijection_solutions,
    branch_tags,
    commutator,
    congruences,
    first_moved_tuple,
    free_word_power,
    interval_covers,
    invisible_to_all_groups,
    is_involutive_solution,
    is_rack_type,
    law_word_on_last_strand,
    opposite_solution,
    right_coordinate_action_relation_failures,
    solution_from_local_interval,
    two_sided_kernel_symmetric_groups,
)


OUT = ROOT / "proofs" / "dual_green_audit.json"


def commutator_law_braid():
    word = commutator(free_word_power(0, 1), free_word_power(1, 1))
    return law_word_on_last_strand(word, arity=2)


def group_orders(groups):
    return [len(group.elements) for group in groups]


def summarize_solution_corpus(size):
    n, braid = commutator_law_braid()
    ybe_count = 0
    opposite_ybe_failure_count = 0
    right_relation_failure_count = 0
    commutator_mover_count = 0
    two_sided_blind_mover_count = 0
    max_two_sided_group_order = 0
    first_two_sided_blind = []
    for solution in all_bijection_solutions(size):
        ybe_count += 1
        if not opposite_solution(solution).is_ybe():
            opposite_ybe_failure_count += 1
        if right_coordinate_action_relation_failures(solution):
            right_relation_failure_count += 1
        groups = two_sided_kernel_symmetric_groups(solution, max_degree=3)
        if groups:
            max_two_sided_group_order = max(
                max_two_sided_group_order,
                max(group_orders(groups)),
            )
        moved = first_moved_tuple(solution, n, braid)
        if moved is None:
            continue
        commutator_mover_count += 1
        if invisible_to_all_groups(groups, n, braid):
            two_sided_blind_mover_count += 1
            if len(first_two_sided_blind) < 5:
                first_two_sided_blind.append(
                    {
                        "branch_tags": list(branch_tags(solution)),
                        "is_rack_type": is_rack_type(solution),
                        "is_involutive_solution": is_involutive_solution(solution),
                        "two_sided_group_orders": group_orders(groups),
                        "moved_tuple": {
                            "start": [repr(value) for value in moved[0]],
                            "image": [repr(value) for value in moved[1]],
                        },
                    }
                )
    return {
        "size": size,
        "ybe_count": ybe_count,
        "opposite_ybe_failure_count": opposite_ybe_failure_count,
        "right_relation_failure_count": right_relation_failure_count,
        "commutator_mover_count": commutator_mover_count,
        "two_sided_blind_mover_count": two_sided_blind_mover_count,
        "max_two_sided_group_order": max_two_sided_group_order,
        "first_two_sided_blind_movers": first_two_sided_blind,
    }


def summarize_local_minimal_corpus(size):
    n, braid = commutator_law_braid()
    local_minimal_cover_count = 0
    opposite_ybe_failure_count = 0
    right_relation_failure_count = 0
    commutator_mover_count = 0
    two_sided_blind_mover_count = 0
    max_two_sided_group_order = 0
    first_two_sided_blind = []
    for solution in all_bijection_solutions(size):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_cover_count += 1
            qmap = solution_from_local_interval(interval)
            total = qmap.total
            if not opposite_solution(total).is_ybe():
                opposite_ybe_failure_count += 1
            if right_coordinate_action_relation_failures(total):
                right_relation_failure_count += 1
            groups = two_sided_kernel_symmetric_groups(total, max_degree=3)
            if groups:
                max_two_sided_group_order = max(
                    max_two_sided_group_order,
                    max(group_orders(groups)),
                )
            moved = first_moved_tuple(total, n, braid)
            if moved is None:
                continue
            commutator_mover_count += 1
            if invisible_to_all_groups(groups, n, braid):
                two_sided_blind_mover_count += 1
                if len(first_two_sided_blind) < 5:
                    first_two_sided_blind.append(
                        {
                            "interval_total_branch_tags": list(branch_tags(total)),
                            "interval_total_is_involutive": is_involutive_solution(
                                total
                            ),
                            "two_sided_group_orders": group_orders(groups),
                            "moved_tuple": {
                                "start": [repr(value) for value in moved[0]],
                                "image": [repr(value) for value in moved[1]],
                            },
                        }
                    )
    return {
        "size": size,
        "local_minimal_cover_count": local_minimal_cover_count,
        "opposite_ybe_failure_count": opposite_ybe_failure_count,
        "right_relation_failure_count": right_relation_failure_count,
        "commutator_mover_count": commutator_mover_count,
        "two_sided_blind_mover_count": two_sided_blind_mover_count,
        "max_two_sided_group_order": max_two_sided_group_order,
        "first_two_sided_blind_movers": first_two_sided_blind,
    }


def main():
    n, braid = commutator_law_braid()
    report = {
        "commutator_law_braid": {"n": n, "word": list(braid)},
        "solution_scans": {
            "size_2_exhaustive": summarize_solution_corpus(2),
            "size_3_exhaustive": summarize_solution_corpus(3),
        },
        "local_minimal_scans": {
            "size_2_exhaustive": summarize_local_minimal_corpus(2),
            "size_3_exhaustive": summarize_local_minimal_corpus(3),
        },
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
