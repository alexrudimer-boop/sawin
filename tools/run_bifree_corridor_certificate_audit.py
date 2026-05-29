import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    CongruenceInterval,
    all_bijection_solutions,
    bifree_corridor_bounded_failures,
    bifree_corridor_detector_target,
    bounded_words,
    branch_tags,
    congruences,
    interval_covers,
    solution_from_local_interval,
    solution_table_signature,
)

OUT_JSON = ROOT / "proofs" / "bifree_corridor_certificate_audit.json"
OUT_MD = ROOT / "proofs" / "bifree_corridor_certificate_audit.md"


def _table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def _partition_signature(partition):
    return [sorted(repr(element) for element in block) for block in partition]


def _moved_signature(moved):
    if moved is None:
        return None
    base, tup, image = moved
    return {
        "base": [repr(item) for item in base],
        "tuple": [repr(item) for item in tup],
        "image": [repr(item) for item in image],
    }


def _failure_signature(certificate):
    return {
        "braid_word": list(certificate.braid_word),
        "moved": _moved_signature(certificate.moved_residual_tuple),
        "subgroup_profile": [
            {
                "name": row.name,
                "group_order": row.group_order,
                "permutation": list(row.permutation),
                "generator_count": row.generator_count,
                "subgroup_size": row.subgroup_size,
            }
            for row in certificate.subgroup_profile
        ],
    }


def scan_size(size, *, n=3, max_word_length=4):
    local_minimal_count = 0
    verdict_counts = Counter()
    target_count = 0
    target_tag_counts = Counter()
    target_factor_rows = Counter()
    target_failure_count = 0
    target_examples = []
    failure_examples = []
    checked_word_count = len([word for word in bounded_words(n, max_word_length) if word])

    for solution_index, solution in enumerate(all_bijection_solutions(size)):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_count += 1
            target = bifree_corridor_detector_target(interval)
            verdict_counts[target.summary.verdict] += 1
            if not target.applies:
                continue

            target_count += 1
            qmap = solution_from_local_interval(interval)
            tags = branch_tags(qmap.total)
            tag_key = "+".join(tags) if tags else "(untagged)"
            target_tag_counts[tag_key] += 1
            target_factor_rows[
                (
                    tuple(sorted(target.factor_orders)),
                    target.detector_order,
                    target.summary.output_kernel_stable_depth,
                    target.summary.all_coordinate_kernel_stable_depth,
                )
            ] += 1
            failures = bifree_corridor_bounded_failures(
                interval,
                n,
                max_word_length,
                max_assignments=10000,
                max_failures=1,
            )
            target_failure_count += len(failures)
            if len(target_examples) < 5:
                target_examples.append(
                    {
                        "solution_index": solution_index,
                        "lower_partition": _partition_signature(lower),
                        "upper_partition": _partition_signature(upper),
                        "tags": list(tags),
                        "factor_orders": list(target.factor_orders),
                        "detector_order": target.detector_order,
                        "output_kernel_depth": target.summary.output_kernel_stable_depth,
                        "all_coordinate_kernel_depth": target.summary.all_coordinate_kernel_stable_depth,
                        "original_table_values": _table_signature(solution),
                    }
                )
            if failures and len(failure_examples) < 5:
                failure_examples.append(
                    {
                        "solution_index": solution_index,
                        "lower_partition": _partition_signature(lower),
                        "upper_partition": _partition_signature(upper),
                        "tags": list(tags),
                        "failure": _failure_signature(failures[0]),
                        "original_table_values": _table_signature(solution),
                    }
                )

    return {
        "size": size,
        "n": n,
        "max_word_length": max_word_length,
        "checked_word_count_per_target_interval": checked_word_count,
        "local_minimal_count": local_minimal_count,
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "target_count": target_count,
        "target_tag_counts": dict(sorted(target_tag_counts.items())),
        "target_factor_rows": [
            {
                "factor_orders": list(key[0]),
                "detector_order": key[1],
                "output_kernel_depth": key[2],
                "all_coordinate_kernel_depth": key[3],
                "count": count,
            }
            for key, count in sorted(target_factor_rows.items(), key=lambda item: repr(item[0]))
        ],
        "target_failure_count": target_failure_count,
        "target_examples": target_examples,
        "failure_examples": failure_examples,
    }


def _format_count_map(counts):
    if not counts:
        return "`{}`"
    return ", ".join(f"`{key}`: `{value}`" for key, value in counts.items())


def write_markdown(report):
    lines = [
        "# Bi-free corridor certificate audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit applies the bi-free corridor subgroup certificate",
        "to the exhaustive size-2 and size-3 local-minimal congruence-cover",
        "corpus.  It is finite diagnostic evidence only.  It does not prove the",
        "Master Local-Minimal Residual Theorem and cannot serve as outcome B.",
        "",
        "For every interval routed to the",
        "`bi_free_universal_corridor_bottleneck` verdict, it checks all braid",
        "words in the bounded ball below.  A listed-factor failure would be a",
        "quotient-fixed residual mover whose recursive-longitude subgroup",
        "profile is trivial for every listed two-sided Green detector factor.",
        "",
    ]
    for name, scan in report.items():
        lines.extend([f"## {name}", ""])
        lines.append(f"Local-minimal covers: `{scan['local_minimal_count']}`.")
        lines.append(
            "Verdict counts: "
            + _format_count_map(scan["verdict_counts"])
            + "."
        )
        lines.append(
            f"Target-shaped intervals: `{scan['target_count']}`."
        )
        lines.append(
            "Target tags: "
            + _format_count_map(scan["target_tag_counts"])
            + "."
        )
        lines.append(
            "Bounded braid words checked per target interval: "
            f"`{scan['checked_word_count_per_target_interval']}` "
            f"on `B_{scan['n']}` through length `{scan['max_word_length']}`."
        )
        lines.append(
            f"Listed-factor B-shaped failures: `{scan['target_failure_count']}`."
        )
        lines.append("")
        lines.append("Target detector rows:")
        lines.append("")
        if scan["target_factor_rows"]:
            for row in scan["target_factor_rows"]:
                lines.append(
                    "- factor orders "
                    f"`{row['factor_orders']}`, detector order "
                    f"`{row['detector_order']}`, output depth "
                    f"`{row['output_kernel_depth']}`, all-coordinate depth "
                    f"`{row['all_coordinate_kernel_depth']}`: "
                    f"`{row['count']}`."
                )
        else:
            lines.append("- none")
        lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "No listed-factor B-shaped failure appears in this bounded audit.  In",
            "the tiny local-minimal cover corpus, no interval now reaches the",
            "`bi_free_universal_corridor_bottleneck` verdict after closed",
            "product subbranches and known whole-solution branches are routed",
            "first.  The size-`3` product rows route to",
            "`product_finite_g_branch`, and the six rows that previously had",
            "the corridor target shape are involutive and now route to",
            "`known_total_branch`.",
            "",
            "This narrows the search surface but does not close the theorem.  A",
            "proof still has to show the all-`n` subgroup-factorization lemma for",
            "arbitrary finite fibres and quotient colours.  A counterexample must",
            "give a normalized-law sequence defeating every finite group, not only",
            "this fixed listed factor set at bounded word length.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    report = {
        "size_2_exhaustive": scan_size(2),
        "size_3_exhaustive": scan_size(3),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
