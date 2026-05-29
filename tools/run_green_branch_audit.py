import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    TransformationMonoid,
    affine_cyclic_form,
    all_bijection_solutions,
    atom_action_summary,
    atom_descent_closure_summary,
    atom_quotient_inner_group,
    atom_quotient_rack_audit,
    atom_quotient_solution,
    atom_projection_summary,
    branch_tags,
    bounded_category_summary,
    coordinate_action_maps,
    coordinate_action_relation_failures,
    depth_observer_summary,
    green_branch_audits,
    is_involutive_solution,
    is_rack_type,
    kernel_action_summary,
    rack_solution,
    schutzenberger_summaries,
    solution_table_signature,
)


OUT = ROOT / "proofs" / "green_branch_audit.json"


def _try_atom_quotient_solution(audit):
    try:
        return atom_quotient_solution(audit)
    except ValueError:
        return None


def _try_atom_quotient_inner_group(audit):
    try:
        return atom_quotient_inner_group(audit)
    except ValueError:
        return None


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


def summarize_solution(solution):
    tau = coordinate_action_maps(solution)
    monoid = TransformationMonoid.generated(tau.values())
    audits = green_branch_audits(solution)
    schutzenberger_by_class = {
        summary.r_class: summary for summary in schutzenberger_summaries(solution)
    }
    kernel_action_by_class = {
        summary.r_class: summary for summary in kernel_action_summary(solution)
    }
    return {
        "element_count": len(solution.elements),
        "coordinate_action_relation_failure_count": len(
            coordinate_action_relation_failures(solution)
        ),
        "tau_maps": {repr(key): list(value) for key, value in tau.items()},
        "coordinate_monoid_size": len(monoid.elements),
        "r_class_count": len(monoid.r_classes()),
        "j_class_count": len(monoid.j_classes()),
        "regular_j_class_count": len(monoid.regular_j_classes()),
        "green_r_class_audits": [
            {
                "r_class_size": len(audit.r_class),
                "edge_germ_count": len(audit.edge_germs),
                "completed_row_count": len(audit.rows),
                "atom_count": len(audit.atom_partition),
                "branch_choice_failure_count": len(audit.branch_choice_failures),
                "atom_block_sizes": sorted(len(block) for block in audit.atom_partition),
                "atom_action": {
                    "supported_pair_count": atom_action.supported_pair_count,
                    "undefined_pair_count": atom_action.undefined_pair_count,
                    "well_defined": atom_action.well_defined,
                    "triangleright_failure_count": (
                        atom_action.triangleright_failure_count
                    ),
                    "triangleleft_failure_count": (
                        atom_action.triangleleft_failure_count
                    ),
                },
                "atom_descent_closure": {
                    "initial_atom_count": atom_descent_closure.initial_atom_count,
                    "closed_atom_count": atom_descent_closure.closed_atom_count,
                    "stable_depth": atom_descent_closure.stable_depth,
                    "added_related_pair_count": (
                        atom_descent_closure.added_related_pair_count
                    ),
                    "closes_without_coarsening": (
                        atom_descent_closure.closes_without_coarsening
                    ),
                    "well_defined_after_closure": (
                        atom_descent_closure.well_defined_after_closure
                    ),
                    "undefined_pair_count_after_closure": (
                        atom_descent_closure.undefined_pair_count_after_closure
                    ),
                    "proves_stable_atom_action": (
                        atom_descent_closure.proves_stable_atom_action
                    ),
                },
                "atom_quotient": {
                    "constructed": atom_quotient is not None,
                    "is_ybe": (
                        None if atom_quotient is None else atom_quotient.is_ybe()
                    ),
                    "right_rack_like": (
                        None
                        if atom_quotient is None
                        else all(
                            atom_quotient.R[(left, right)][0] == right
                            for left in atom_quotient.elements
                            for right in atom_quotient.elements
                        )
                    ),
                    "right_translations_bijective": (
                        atom_quotient_rack.right_translations_bijective
                    ),
                    "right_self_distributive": (
                        atom_quotient_rack.right_self_distributive
                    ),
                    "proves_right_rack_ybe_layer": (
                        atom_quotient_rack.proves_right_rack_ybe_layer
                    ),
                    "inner_group_order": (
                        None
                        if atom_inner_group is None
                        else len(atom_inner_group.elements)
                    ),
                },
                "atom_projection": {
                    "source_count": atom_summary.source_count,
                    "equality_source_count": atom_summary.equality_source_count,
                    "universal_source_count": atom_summary.universal_source_count,
                    "mixed_source_count": atom_summary.mixed_source_count,
                    "empty_source_count": atom_summary.empty_source_count,
                },
                "schutzenberger": {
                    "right_stabilizer_size": (
                        schutzenberger_by_class[audit.r_class].right_stabilizer_size
                    ),
                    "permutation_count": (
                        schutzenberger_by_class[audit.r_class].permutation_count
                    ),
                    "nonpermutation_stabilizer_count": (
                        schutzenberger_by_class[
                            audit.r_class
                        ].nonpermutation_stabilizer_count
                    ),
                    "permutation_group_closed": (
                        schutzenberger_by_class[audit.r_class].permutation_group_closed
                    ),
                    "globally_stabilizing_label_count": len(
                        schutzenberger_by_class[
                            audit.r_class
                        ].globally_stabilizing_labels
                    ),
                    "global_edge_germ_count": (
                        schutzenberger_by_class[audit.r_class].global_edge_germ_count
                    ),
                    "local_only_edge_germ_count": (
                        schutzenberger_by_class[audit.r_class].local_only_edge_germ_count
                    ),
                },
                "kernel_action": {
                    "kernel_block_count": len(
                        kernel_action_by_class[audit.r_class].kernel_partition
                    ),
                    "retained_label_count": len(
                        kernel_action_by_class[audit.r_class].retained_labels
                    ),
                    "induced_permutation_count": len(
                        kernel_action_by_class[audit.r_class].induced_permutations
                    ),
                    "induced_group_size": (
                        kernel_action_by_class[audit.r_class].induced_group_size
                    ),
                    "nonpermutation_label_count": (
                        kernel_action_by_class[
                            audit.r_class
                        ].nonpermutation_label_count
                    ),
                },
                "depth_observers": [
                    {
                        "max_depth": summary.max_depth,
                        "context_word_counts": list(summary.context_word_counts),
                        "undefined_profile_count": summary.undefined_profile_count,
                        "atom_profile_conflict_count": summary.atom_profile_conflict_count,
                        "hidden_profile_split_count": summary.hidden_profile_split_count,
                    }
                    for summary in (
                        depth_observer_summary(audit, depth)
                        for depth in range(0, 4)
                    )
                ],
                "bounded_categories": [
                    {
                        "max_depth": summary.max_depth,
                        "morphism_count": summary.morphism_count,
                        "truncated": summary.truncated,
                        "hidden_atom_trivial_loop_count": (
                            summary.hidden_atom_trivial_loop_count
                        ),
                        "hidden_bijective_loop_count": (
                            summary.hidden_bijective_loop_count
                        ),
                        "undefined_image_count": summary.undefined_image_count,
                    }
                    for summary in (
                        bounded_category_summary(audit, depth, morphism_limit=10000)
                        for depth in range(0, 3)
                    )
                ],
            }
            for audit in audits
            for atom_summary in (atom_projection_summary(audit),)
            for atom_action in (atom_action_summary(audit),)
            for atom_descent_closure in (atom_descent_closure_summary(audit),)
            for atom_quotient in (
                _try_atom_quotient_solution(audit),
            )
            for atom_quotient_rack in (atom_quotient_rack_audit(audit),)
            for atom_inner_group in (_try_atom_quotient_inner_group(audit),)
        ],
    }


def small_green_scan(size, max_checked=None):
    ybe_count = 0
    nonrack_count = 0
    direct_failure_count = 0
    atom_action_failure_solution_count = 0
    atom_action_undefined_pair_audit_count = 0
    atom_descent_closure_coarsening_solution_count = 0
    atom_descent_closure_failure_solution_count = 0
    atom_quotient_failure_solution_count = 0
    atom_quotient_non_ybe_solution_count = 0
    atom_quotient_non_right_rack_like_solution_count = 0
    atom_quotient_rack_law_failure_solution_count = 0
    depth2_atom_conflict_count = 0
    depth2_hidden_split_count = 0
    depth2_hidden_split_solution_count = 0
    depth2_hidden_split_involutive_solution_count = 0
    depth2_hidden_atom_trivial_loop_solution_count = 0
    depth2_hidden_bijective_loop_solution_count = 0
    depth2_hidden_atom_trivial_loop_involutive_solution_count = 0
    depth2_hidden_bijective_loop_involutive_solution_count = 0
    depth2_category_truncation_count = 0
    mixed_atom_projection_solution_count = 0
    mixed_atom_projection_involutive_solution_count = 0
    mixed_atom_projection_branch_tag_counts = {}
    local_only_edge_germ_solution_count = 0
    schutzenberger_non_group_action_solution_count = 0
    kernel_action_nonpermutation_solution_count = 0
    kernel_action_max_group_size = 0
    first_failures = []
    first_hidden_splits = []
    first_hidden_loops = []
    first_mixed_atom_projections = []
    for solution in all_bijection_solutions(size, max_checked=max_checked):
        ybe_count += 1
        rack_type = is_rack_type(solution)
        if not rack_type:
            nonrack_count += 1
        audits = green_branch_audits(solution)
        atom_summaries = [atom_projection_summary(audit) for audit in audits]
        schutzenberger = schutzenberger_summaries(solution)
        kernel_actions = kernel_action_summary(solution)
        if any(summary.nonpermutation_label_count for summary in kernel_actions):
            kernel_action_nonpermutation_solution_count += 1
        if kernel_actions:
            kernel_action_max_group_size = max(
                kernel_action_max_group_size,
                max(summary.induced_group_size for summary in kernel_actions),
            )
        has_mixed_atom_projection = any(
            summary.mixed_source_count for summary in atom_summaries
        )
        if has_mixed_atom_projection:
            mixed_atom_projection_solution_count += 1
            if is_involutive_solution(solution):
                mixed_atom_projection_involutive_solution_count += 1
            for tag in branch_tags(solution):
                mixed_atom_projection_branch_tag_counts[tag] = (
                    mixed_atom_projection_branch_tag_counts.get(tag, 0) + 1
                )
            if len(first_mixed_atom_projections) < 5:
                first_mixed_atom_projections.append(
                    {
                        "is_rack_type": rack_type,
                        "is_involutive_solution": is_involutive_solution(solution),
                        "branch_tags": list(branch_tags(solution)),
                        "affine_cyclic_form": affine_cyclic_form(solution),
                        "table_values": [
                            list(value) for value in solution_table_signature(solution)
                        ],
                        "mixed_source_counts": [
                            summary.mixed_source_count for summary in atom_summaries
                        ],
                    }
                )
        if any(summary.local_only_edge_germ_count for summary in schutzenberger):
            local_only_edge_germ_solution_count += 1
        if any(
            summary.nonpermutation_stabilizer_count
            or not summary.permutation_group_closed
            for summary in schutzenberger
        ):
            schutzenberger_non_group_action_solution_count += 1
        if any(audit.branch_choice_failures for audit in audits):
            direct_failure_count += 1
            if len(first_failures) < 3:
                first_failures.append(
                    [list(value) for value in solution_table_signature(solution)]
                )
        atom_action_summaries = [atom_action_summary(audit) for audit in audits]
        if any(not summary.well_defined for summary in atom_action_summaries):
            atom_action_failure_solution_count += 1
        atom_action_undefined_pair_audit_count += sum(
            1 for summary in atom_action_summaries if summary.undefined_pair_count
        )
        atom_descent_closures = [
            atom_descent_closure_summary(audit) for audit in audits
        ]
        if any(
            not summary.closes_without_coarsening
            for summary in atom_descent_closures
        ):
            atom_descent_closure_coarsening_solution_count += 1
        if any(
            not summary.proves_stable_atom_action
            for summary in atom_descent_closures
        ):
            atom_descent_closure_failure_solution_count += 1
        atom_quotients = [_try_atom_quotient_solution(audit) for audit in audits]
        atom_quotient_rack_audits = [
            atom_quotient_rack_audit(audit) for audit in audits
        ]
        if any(quotient is None for quotient in atom_quotients):
            atom_quotient_failure_solution_count += 1
        if any(
            quotient is not None and not quotient.is_ybe()
            for quotient in atom_quotients
        ):
            atom_quotient_non_ybe_solution_count += 1
        if any(
            quotient is not None
            and any(
                quotient.R[(left, right)][0] != right
                for left in quotient.elements
                for right in quotient.elements
            )
            for quotient in atom_quotients
        ):
            atom_quotient_non_right_rack_like_solution_count += 1
        if any(
            not audit.proves_right_rack_ybe_layer
            for audit in atom_quotient_rack_audits
        ):
            atom_quotient_rack_law_failure_solution_count += 1
        for audit in audits:
            summary = depth_observer_summary(audit, 2)
            depth2_atom_conflict_count += summary.atom_profile_conflict_count
            depth2_hidden_split_count += summary.hidden_profile_split_count
        category_summaries = [
            bounded_category_summary(audit, 2, morphism_limit=10000)
            for audit in audits
        ]
        if any(summary.truncated for summary in category_summaries):
            depth2_category_truncation_count += 1
        if any(summary.hidden_atom_trivial_loop_count for summary in category_summaries):
            depth2_hidden_atom_trivial_loop_solution_count += 1
            if is_involutive_solution(solution):
                depth2_hidden_atom_trivial_loop_involutive_solution_count += 1
            if len(first_hidden_loops) < 5:
                first_hidden_loops.append(
                    {
                        "is_rack_type": rack_type,
                        "is_involutive_solution": is_involutive_solution(solution),
                        "branch_tags": list(branch_tags(solution)),
                        "affine_cyclic_form": affine_cyclic_form(solution),
                        "table_values": [
                            list(value) for value in solution_table_signature(solution)
                        ],
                    }
                )
        if any(summary.hidden_bijective_loop_count for summary in category_summaries):
            depth2_hidden_bijective_loop_solution_count += 1
            if is_involutive_solution(solution):
                depth2_hidden_bijective_loop_involutive_solution_count += 1
        if any(depth_observer_summary(audit, 2).hidden_profile_split_count for audit in audits):
            depth2_hidden_split_solution_count += 1
            if is_involutive_solution(solution):
                depth2_hidden_split_involutive_solution_count += 1
            if len(first_hidden_splits) < 5:
                first_hidden_splits.append(
                    {
                        "is_rack_type": rack_type,
                        "is_involutive_solution": is_involutive_solution(solution),
                        "branch_tags": list(branch_tags(solution)),
                        "is_identity_table": all(
                            solution.R[(x, y)] == (x, y)
                            for x in solution.elements
                            for y in solution.elements
                        ),
                        "affine_cyclic_form": affine_cyclic_form(solution),
                        "table_values": [
                            list(value) for value in solution_table_signature(solution)
                        ],
                    }
                )
    return {
        "size": size,
        "max_checked": max_checked,
        "ybe_count": ybe_count,
        "nonrack_count": nonrack_count,
        "direct_branch_choice_failure_count": direct_failure_count,
        "atom_action_failure_solution_count": atom_action_failure_solution_count,
        "atom_action_undefined_pair_audit_count": atom_action_undefined_pair_audit_count,
        "atom_descent_closure_coarsening_solution_count": (
            atom_descent_closure_coarsening_solution_count
        ),
        "atom_descent_closure_failure_solution_count": (
            atom_descent_closure_failure_solution_count
        ),
        "atom_quotient_failure_solution_count": atom_quotient_failure_solution_count,
        "atom_quotient_non_ybe_solution_count": atom_quotient_non_ybe_solution_count,
        "atom_quotient_non_right_rack_like_solution_count": (
            atom_quotient_non_right_rack_like_solution_count
        ),
        "atom_quotient_rack_law_failure_solution_count": (
            atom_quotient_rack_law_failure_solution_count
        ),
        "depth2_atom_profile_conflict_count": depth2_atom_conflict_count,
        "depth2_hidden_profile_split_count": depth2_hidden_split_count,
        "depth2_hidden_profile_split_solution_count": depth2_hidden_split_solution_count,
        "depth2_hidden_split_involutive_solution_count": (
            depth2_hidden_split_involutive_solution_count
        ),
        "depth2_completed_category_truncation_count": depth2_category_truncation_count,
        "mixed_atom_projection_solution_count": mixed_atom_projection_solution_count,
        "mixed_atom_projection_involutive_solution_count": (
            mixed_atom_projection_involutive_solution_count
        ),
        "mixed_atom_projection_branch_tag_counts": dict(
            sorted(mixed_atom_projection_branch_tag_counts.items())
        ),
        "local_only_edge_germ_solution_count": local_only_edge_germ_solution_count,
        "schutzenberger_non_group_action_solution_count": (
            schutzenberger_non_group_action_solution_count
        ),
        "kernel_action_nonpermutation_solution_count": (
            kernel_action_nonpermutation_solution_count
        ),
        "kernel_action_max_group_size": kernel_action_max_group_size,
        "depth2_hidden_atom_trivial_loop_solution_count": (
            depth2_hidden_atom_trivial_loop_solution_count
        ),
        "depth2_hidden_bijective_loop_solution_count": (
            depth2_hidden_bijective_loop_solution_count
        ),
        "depth2_hidden_atom_trivial_loop_involutive_solution_count": (
            depth2_hidden_atom_trivial_loop_involutive_solution_count
        ),
        "depth2_hidden_bijective_loop_involutive_solution_count": (
            depth2_hidden_bijective_loop_involutive_solution_count
        ),
        "first_failure_signatures": first_failures,
        "first_hidden_split_signatures": first_hidden_splits,
        "first_hidden_loop_signatures": first_hidden_loops,
        "first_mixed_atom_projection_signatures": first_mixed_atom_projections,
    }


def main():
    examples = {
        "trivial_rack_2": rack_solution([0, 1], lambda a, b: b),
        "dihedral_quandle_3": rack_solution(
            [0, 1, 2], lambda a, b: (2 * a - b) % 3
        ),
        "size3_affine_commutator_candidate": size_three_affine_candidate(),
    }
    report = {
        "examples": {
            name: summarize_solution(solution) for name, solution in examples.items()
        },
        "small_scans": {
            "size_2_exhaustive": small_green_scan(2),
            "size_3_exhaustive": small_green_scan(3),
        },
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
