import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    CongruenceInterval,
    all_bijection_solutions,
    atom_projection_summary,
    bounded_category_summary,
    branch_tags,
    congruences,
    coordinate_kernel_seed_pairs,
    generated_admissible_congruence_audit,
    green_branch_audits,
    interval_covers,
    is_involutive_solution,
    is_rack_type,
    kernel_action_summary,
    schutzenberger_summaries,
    solution_from_local_interval,
    solution_table_signature,
)


OUT = ROOT / "proofs" / "local_minimal_green_audit.json"


def partition_signature(partition):
    return [
        sorted((repr(element) for element in block))
        for block in partition
    ]


def table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def scan_size(size):
    ybe_solution_count = 0
    cover_count = 0
    local_minimal_cover_count = 0
    semisplit_cover_count = 0
    semisplit_candidate_count = 0
    semisplit_failure_witness_count = 0
    depth2_category_truncation_count = 0
    hidden_loop_interval_count = 0
    hidden_loop_involutive_interval_count = 0
    hidden_bijective_loop_interval_count = 0
    hidden_bijective_loop_involutive_interval_count = 0
    hidden_loop_untagged_interval_count = 0
    hidden_bijective_loop_untagged_interval_count = 0
    hidden_loop_only_rack_tag_interval_count = 0
    hidden_bijective_loop_only_rack_tag_interval_count = 0
    mixed_atom_projection_interval_count = 0
    mixed_atom_projection_involutive_interval_count = 0
    mixed_atom_projection_branch_tag_counts = {}
    local_only_edge_germ_interval_count = 0
    schutzenberger_non_group_action_interval_count = 0
    kernel_action_nonpermutation_interval_count = 0
    kernel_action_max_group_size = 0
    hidden_loop_branch_tag_counts = {}
    hidden_bijective_loop_branch_tag_counts = {}
    first_untagged_hidden_intervals = []
    first_hidden_intervals = []
    first_mixed_atom_projection_intervals = []
    output_kernel_counts = {}
    universal_output_depth_counts = {}
    universal_output_hidden_loop_interval_count = 0
    universal_output_hidden_bijective_loop_interval_count = 0
    universal_output_mixed_atom_projection_interval_count = 0
    universal_output_untagged_interval_count = 0
    universal_output_branch_tag_counts = {}

    for solution in all_bijection_solutions(size):
        ybe_solution_count += 1
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            cover_count += 1
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            semisplit_audits = interval.semisplit_audits()
            semisplit_candidate_count += len(semisplit_audits)
            semisplit_failure_witness_count += sum(
                1
                for audit in semisplit_audits
                if not audit.admissible and audit.failure is not None
            )
            if any(audit.admissible for audit in semisplit_audits):
                semisplit_cover_count += 1
            if not interval.is_local_minimal():
                continue
            local_minimal_cover_count += 1
            interval_total = solution_from_local_interval(interval).total
            output_kernel_audit = generated_admissible_congruence_audit(
                interval,
                coordinate_kernel_seed_pairs(interval),
            )
            output_kernel_counts[output_kernel_audit.kind] = (
                output_kernel_counts.get(output_kernel_audit.kind, 0) + 1
            )
            if output_kernel_audit.kind == "universal":
                universal_output_depth_counts[output_kernel_audit.stable_depth] = (
                    universal_output_depth_counts.get(output_kernel_audit.stable_depth, 0)
                    + 1
                )
            green_audits = green_branch_audits(interval_total)
            atom_summaries = [atom_projection_summary(audit) for audit in green_audits]
            schutzenberger = schutzenberger_summaries(interval_total)
            kernel_actions = kernel_action_summary(interval_total)
            if any(summary.nonpermutation_label_count for summary in kernel_actions):
                kernel_action_nonpermutation_interval_count += 1
            if kernel_actions:
                kernel_action_max_group_size = max(
                    kernel_action_max_group_size,
                    max(summary.induced_group_size for summary in kernel_actions),
                )
            has_mixed_atom_projection = any(
                summary.mixed_source_count for summary in atom_summaries
            )
            if has_mixed_atom_projection:
                mixed_atom_projection_interval_count += 1
                if is_involutive_solution(interval_total):
                    mixed_atom_projection_involutive_interval_count += 1
                for tag in branch_tags(interval_total):
                    mixed_atom_projection_branch_tag_counts[tag] = (
                        mixed_atom_projection_branch_tag_counts.get(tag, 0) + 1
                    )
                if len(first_mixed_atom_projection_intervals) < 5:
                    first_mixed_atom_projection_intervals.append(
                        {
                            "original_table_values": table_signature(solution),
                            "lower_partition": partition_signature(lower),
                            "upper_partition": partition_signature(upper),
                            "interval_color_count": len(interval.colors),
                            "interval_total_element_count": len(interval_total.elements),
                            "interval_total_is_involutive": is_involutive_solution(
                                interval_total
                            ),
                            "interval_total_branch_tags": list(
                                branch_tags(interval_total)
                            ),
                            "mixed_source_counts": [
                                summary.mixed_source_count
                                for summary in atom_summaries
                            ],
                        }
                    )
            if any(summary.local_only_edge_germ_count for summary in schutzenberger):
                local_only_edge_germ_interval_count += 1
            if any(
                summary.nonpermutation_stabilizer_count
                or not summary.permutation_group_closed
                for summary in schutzenberger
            ):
                schutzenberger_non_group_action_interval_count += 1
            category_summaries = [
                bounded_category_summary(audit, 2, morphism_limit=10000)
                for audit in green_audits
            ]
            has_hidden_loop = any(
                summary.hidden_atom_trivial_loop_count
                for summary in category_summaries
            )
            has_hidden_bijective_loop = any(
                summary.hidden_bijective_loop_count
                for summary in category_summaries
            )
            if any(summary.truncated for summary in category_summaries):
                depth2_category_truncation_count += 1
            interval_involutive = is_involutive_solution(interval_total)
            interval_branch_tags = branch_tags(interval_total)
            if output_kernel_audit.kind == "universal":
                if not interval_branch_tags:
                    universal_output_untagged_interval_count += 1
                for tag in interval_branch_tags:
                    universal_output_branch_tag_counts[tag] = (
                        universal_output_branch_tag_counts.get(tag, 0) + 1
                    )
                if has_mixed_atom_projection:
                    universal_output_mixed_atom_projection_interval_count += 1
                if has_hidden_loop:
                    universal_output_hidden_loop_interval_count += 1
                if has_hidden_bijective_loop:
                    universal_output_hidden_bijective_loop_interval_count += 1
            if has_hidden_loop:
                hidden_loop_interval_count += 1
                for tag in interval_branch_tags:
                    hidden_loop_branch_tag_counts[tag] = (
                        hidden_loop_branch_tag_counts.get(tag, 0) + 1
                    )
                if not interval_branch_tags:
                    hidden_loop_untagged_interval_count += 1
                    if len(first_untagged_hidden_intervals) < 5:
                        first_untagged_hidden_intervals.append(
                            {
                                "original_table_values": table_signature(solution),
                                "lower_partition": partition_signature(lower),
                                "upper_partition": partition_signature(upper),
                                "interval_color_count": len(interval.colors),
                                "interval_total_element_count": len(interval_total.elements),
                            }
                        )
                if set(interval_branch_tags) <= {"rack_type"}:
                    hidden_loop_only_rack_tag_interval_count += 1
                if interval_involutive:
                    hidden_loop_involutive_interval_count += 1
                if len(first_hidden_intervals) < 5:
                    first_hidden_intervals.append(
                        {
                            "original_table_values": table_signature(solution),
                            "lower_partition": partition_signature(lower),
                            "upper_partition": partition_signature(upper),
                            "interval_color_count": len(interval.colors),
                            "interval_total_element_count": len(interval_total.elements),
                            "interval_total_is_rack_type": is_rack_type(interval_total),
                            "interval_total_is_involutive": interval_involutive,
                            "interval_total_branch_tags": list(interval_branch_tags),
                            "bounded_category_summaries": [
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
                                }
                                for summary in category_summaries
                            ],
                        }
                    )
            if has_hidden_bijective_loop:
                hidden_bijective_loop_interval_count += 1
                for tag in interval_branch_tags:
                    hidden_bijective_loop_branch_tag_counts[tag] = (
                        hidden_bijective_loop_branch_tag_counts.get(tag, 0) + 1
                    )
                if not interval_branch_tags:
                    hidden_bijective_loop_untagged_interval_count += 1
                if set(interval_branch_tags) <= {"rack_type"}:
                    hidden_bijective_loop_only_rack_tag_interval_count += 1
                if interval_involutive:
                    hidden_bijective_loop_involutive_interval_count += 1

    return {
        "size": size,
        "ybe_solution_count": ybe_solution_count,
        "cover_count": cover_count,
        "local_minimal_cover_count": local_minimal_cover_count,
        "semisplit_cover_count": semisplit_cover_count,
        "semisplit_candidate_count": semisplit_candidate_count,
        "semisplit_failure_witness_count": semisplit_failure_witness_count,
        "depth2_completed_category_truncation_count": depth2_category_truncation_count,
        "mixed_atom_projection_interval_count": mixed_atom_projection_interval_count,
        "mixed_atom_projection_involutive_interval_count": (
            mixed_atom_projection_involutive_interval_count
        ),
        "mixed_atom_projection_branch_tag_counts": dict(
            sorted(mixed_atom_projection_branch_tag_counts.items())
        ),
        "local_only_edge_germ_interval_count": local_only_edge_germ_interval_count,
        "schutzenberger_non_group_action_interval_count": (
            schutzenberger_non_group_action_interval_count
        ),
        "kernel_action_nonpermutation_interval_count": (
            kernel_action_nonpermutation_interval_count
        ),
        "kernel_action_max_group_size": kernel_action_max_group_size,
        "output_kernel_counts": dict(sorted(output_kernel_counts.items())),
        "universal_output_depth_counts": {
            str(depth): count
            for depth, count in sorted(universal_output_depth_counts.items())
        },
        "universal_output_hidden_atom_trivial_loop_interval_count": (
            universal_output_hidden_loop_interval_count
        ),
        "universal_output_hidden_bijective_loop_interval_count": (
            universal_output_hidden_bijective_loop_interval_count
        ),
        "universal_output_mixed_atom_projection_interval_count": (
            universal_output_mixed_atom_projection_interval_count
        ),
        "universal_output_untagged_interval_count": (
            universal_output_untagged_interval_count
        ),
        "universal_output_branch_tag_counts": dict(
            sorted(universal_output_branch_tag_counts.items())
        ),
        "depth2_hidden_atom_trivial_loop_interval_count": hidden_loop_interval_count,
        "depth2_hidden_atom_trivial_loop_involutive_interval_count": (
            hidden_loop_involutive_interval_count
        ),
        "depth2_hidden_bijective_loop_interval_count": hidden_bijective_loop_interval_count,
        "depth2_hidden_bijective_loop_involutive_interval_count": (
            hidden_bijective_loop_involutive_interval_count
        ),
        "depth2_hidden_atom_trivial_loop_untagged_interval_count": (
            hidden_loop_untagged_interval_count
        ),
        "depth2_hidden_bijective_loop_untagged_interval_count": (
            hidden_bijective_loop_untagged_interval_count
        ),
        "depth2_hidden_atom_trivial_loop_only_rack_tag_interval_count": (
            hidden_loop_only_rack_tag_interval_count
        ),
        "depth2_hidden_bijective_loop_only_rack_tag_interval_count": (
            hidden_bijective_loop_only_rack_tag_interval_count
        ),
        "depth2_hidden_loop_branch_tag_counts": dict(
            sorted(hidden_loop_branch_tag_counts.items())
        ),
        "depth2_hidden_bijective_loop_branch_tag_counts": dict(
            sorted(hidden_bijective_loop_branch_tag_counts.items())
        ),
        "first_hidden_intervals": first_hidden_intervals,
        "first_untagged_hidden_intervals": first_untagged_hidden_intervals,
        "first_mixed_atom_projection_intervals": first_mixed_atom_projection_intervals,
    }


def main():
    report = {
        "size_2_exhaustive": scan_size(2),
        "size_3_exhaustive": scan_size(3),
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
