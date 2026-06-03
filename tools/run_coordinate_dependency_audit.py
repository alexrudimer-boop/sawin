import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    all_bijection_solutions,
    coordinate_dependency_branch_audit,
    solution_table_signature,
)


OUT_JSON = ROOT / "proofs" / "coordinate_dependency_audit.json"
OUT_MD = ROOT / "proofs" / "coordinate_dependency_audit.md"


def _profile_key(active_dependencies):
    return "+".join(active_dependencies) if active_dependencies else "none"


def _counter_dict(counter):
    return dict(sorted(counter.items(), key=lambda item: item[0]))


def _signature_record(solution, audit):
    return {
        "active_dependencies": list(audit.active_dependencies),
        "same_side_dependencies": list(audit.same_side_dependencies),
        "opposite_side_dependencies": list(audit.opposite_side_dependencies),
        "known_full_twist_reason": audit.known_full_twist_reason,
        "reason": audit.reason,
        "table_values": [list(pair) for pair in solution_table_signature(solution)],
    }


def size_summary(size, max_n):
    profile_counts = Counter()
    dependency_reason_counts = Counter()
    full_twist_reason_counts = Counter()
    unclosed_dependency_rows = []
    total = 0
    dependency_count = 0
    same_side_count = 0
    opposite_only_count = 0
    closed_dependency_count = 0
    max_full_twist_order = 1
    for solution in all_bijection_solutions(size):
        total += 1
        audit = coordinate_dependency_branch_audit(solution, max_n=max_n)
        profile_counts[_profile_key(audit.active_dependencies)] += 1
        if audit.known_full_twist_reason is not None:
            full_twist_reason_counts[audit.known_full_twist_reason] += 1
        max_full_twist_order = max(max_full_twist_order, max(audit.action_orders))
        if not audit.has_coordinate_dependency:
            continue
        dependency_count += 1
        if audit.has_same_side_dependency:
            same_side_count += 1
        elif audit.has_opposite_side_dependency:
            opposite_only_count += 1
        dependency_reason_counts[audit.reason or "unclosed"] += 1
        if audit.proves_coordinate_dependency_closed_branch:
            closed_dependency_count += 1
        elif len(unclosed_dependency_rows) < 5:
            unclosed_dependency_rows.append(_signature_record(solution, audit))
    return {
        "size": size,
        "max_n": max_n,
        "total_ybe_solutions": total,
        "coordinate_dependency_rows": dependency_count,
        "same_side_dependency_rows": same_side_count,
        "opposite_side_only_dependency_rows": opposite_only_count,
        "closed_coordinate_dependency_rows": closed_dependency_count,
        "unclosed_coordinate_dependency_rows": dependency_count - closed_dependency_count,
        "max_full_twist_prefix_order": max_full_twist_order,
        "profile_counts": _counter_dict(profile_counts),
        "coordinate_dependency_reason_counts": _counter_dict(dependency_reason_counts),
        "known_full_twist_reason_counts": _counter_dict(full_twist_reason_counts),
        "first_unclosed_dependency_rows": unclosed_dependency_rows,
    }


def audit_payload(sizes=(1, 2, 3), max_n=5):
    summaries = [size_summary(size, max_n) for size in sizes]
    return {
        "description": (
            "Exact tiny-corpus audit for finite bijective YBE tables with "
            "one-coordinate dependency profiles."
        ),
        "sizes": list(sizes),
        "max_n": max_n,
        "summaries": summaries,
        "all_dependency_rows_closed": all(
            summary["unclosed_coordinate_dependency_rows"] == 0
            for summary in summaries
        ),
        "finite_checks_derived_from_tables": True,
    }


def render_markdown(payload):
    lines = [
        "# Coordinate dependency audit",
        "",
        "This note records a narrow degenerate branch for the central",
        "full-twist obstruction route.  It is not a classification of all",
        "finite bijective set-theoretic YBE solutions.",
        "",
        "## Same-side collapse",
        "",
        "Let `R(x,y)=(f(x),h(x,y))` be a finite bijective YBE table whose",
        "first output depends only on `x`.  Bijectivity makes `f` a",
        "permutation and each map `h_x:y -> h(x,y)` a permutation.  Comparing",
        "the first coordinate in `R_12 R_23 R_12 = R_23 R_12 R_23` gives",
        "`f^2=f`, hence `f=id`.  The second coordinate then gives",
        "`h_x^2=h_x` for every `x`, so each permutation `h_x` is the",
        "identity.  Thus `R=id`.  Applying the side-opposite argument gives",
        "the dual case where the second output depends only on `y`.",
        "",
        "Therefore a same-side coordinate dependency cannot produce a",
        "nontrivial full-twist obstruction.",
        "",
        "## Opposite-side routing",
        "",
        "If the first output depends only on `y`, then bijectivity forces that",
        "one-variable first-coordinate map to be a permutation and also forces",
        "the second-coordinate maps in the remaining variable to be",
        "permutations.  The solution is nondegenerate.  The same argument",
        "applies when the second output depends only on `x`.  These rows are",
        "routed to the existing left-nondegenerate/guitar branch, whose",
        "central full-twist order is bounded through the derived rack.",
        "",
        "## Exact tiny-corpus census",
        "",
        f"- audited sizes: `{payload['sizes']}`;",
        f"- full-twist prefix: `1 <= n <= {payload['max_n']}`;",
        f"- all coordinate-dependency rows closed: `{payload['all_dependency_rows_closed']}`.",
        "",
    ]
    for summary in payload["summaries"]:
        lines.extend(
            [
                f"### Size {summary['size']}",
                "",
                f"- YBE tables: `{summary['total_ybe_solutions']}`;",
                f"- coordinate-dependency rows: `{summary['coordinate_dependency_rows']}`;",
                f"- same-side rows: `{summary['same_side_dependency_rows']}`;",
                (
                    "- opposite-side-only rows: "
                    f"`{summary['opposite_side_only_dependency_rows']}`;"
                ),
                (
                    "- unclosed coordinate-dependency rows: "
                    f"`{summary['unclosed_coordinate_dependency_rows']}`;"
                ),
                (
                    "- maximum checked full-twist order: "
                    f"`{summary['max_full_twist_prefix_order']}`."
                ),
                "",
                f"- profile counts: `{summary['profile_counts']}`;",
                (
                    "- coordinate-dependency reasons: "
                    f"`{summary['coordinate_dependency_reason_counts']}`;"
                ),
                (
                    "- known full-twist reasons: "
                    f"`{summary['known_full_twist_reason_counts']}`."
                ),
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence for the MO route",
            "",
            "A finite unbounded-central-full-twist counterexample, if it exists,",
            "must avoid these one-coordinate dependency profiles.  In particular",
            "it cannot be triangular in the elementary sense above; it must live",
            "in the genuinely remaining degenerate classes not already routed",
            "through the identity, permutation-form, rack, involutive,",
            "left-nondegenerate/guitar, or affine `F_2` guardrails.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    payload = audit_payload()
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
