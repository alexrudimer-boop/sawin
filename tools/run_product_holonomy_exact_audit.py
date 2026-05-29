import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    LocalInterval,
    branch_tags,
    product_holonomy_exact_audit,
    product_holonomy_groups,
    solution_from_local_interval,
    symmetric_group,
)
from ybe_domination.product_permutation import _compose_maps, _invert_map  # noqa: E402


OUT_JSON = ROOT / "proofs" / "product_holonomy_exact_audit.json"
OUT_MD = ROOT / "proofs" / "product_holonomy_exact_audit.md"


def two_color_swapped_coboundary_interval():
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {(a, b): (a, b) for a in colors for b in colors}
    gauge = {
        0: {0: 0, 1: 1},
        1: {0: 1, 1: 0},
    }

    def compose(left, right):
        return {key: left[right[key]] for key in right}

    table = {}
    for a, b in product(colors, repeat=2):
        c, d = base_R[(a, b)]
        left_map = compose(_invert_map(gauge[c]), gauge[b])
        right_map = compose(_invert_map(gauge[d]), gauge[a])
        for x, y in product(points, repeat=2):
            table[(a, b, x, y)] = (left_map[y], right_map[x])
    return LocalInterval(colors, fibres, base_R, table)


def one_color_commuting_swapped_interval():
    points = (0, 1, 2)
    cycle = {0: 1, 1: 2, 2: 0}
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={
            ("*", "*", x, y): (cycle[y], cycle[x])
            for x in points
            for y in points
        },
    )


def two_color_identity_base_cyclic_interval():
    colors = (0, 1)
    points = (0, 1, 2)
    fibres = {0: points, 1: points}
    cycle = {0: 1, 1: 2, 2: 0}
    identity = {point: point for point in points}
    base_R = {(a, b): (a, b) for a in colors for b in colors}
    left = {
        (0, 0): identity,
        (0, 1): cycle,
        (1, 0): identity,
        (1, 1): identity,
    }
    right = {
        key: _compose_maps(cycle, _invert_map(mapping))
        for key, mapping in left.items()
    }
    table = {}
    for a, b in product(colors, repeat=2):
        for x, y in product(points, repeat=2):
            table[(a, b, x, y)] = (left[(a, b)][y], right[(a, b)][x])
    return LocalInterval(colors, fibres, base_R, table)


def two_color_known_nondegenerate_failure_interval():
    colors = (0, 1)
    points = (0, 1)
    fibres = {0: points, 1: points}
    base_R = {
        (0, 0): (0, 1),
        (0, 1): (1, 1),
        (1, 0): (0, 0),
        (1, 1): (1, 0),
    }
    rows = [
        ((0, 0, 0, 0), (0, 0)),
        ((0, 0, 0, 1), (1, 0)),
        ((0, 0, 1, 0), (0, 1)),
        ((0, 0, 1, 1), (1, 1)),
        ((0, 1, 0, 0), (0, 0)),
        ((0, 1, 0, 1), (1, 0)),
        ((0, 1, 1, 0), (0, 1)),
        ((0, 1, 1, 1), (1, 1)),
        ((1, 0, 0, 0), (0, 1)),
        ((1, 0, 0, 1), (1, 1)),
        ((1, 0, 1, 0), (0, 0)),
        ((1, 0, 1, 1), (1, 0)),
        ((1, 1, 0, 0), (0, 1)),
        ((1, 1, 0, 1), (1, 1)),
        ((1, 1, 1, 0), (0, 0)),
        ((1, 1, 1, 1), (1, 0)),
    ]
    return LocalInterval(colors, fibres, base_R, dict(rows))


def _failure_json(failure):
    if failure is None:
        return None
    return {
        "braid_word": list(failure.braid_word),
        "coordinate": failure.coordinate,
        "model_points": [repr(point) for point in failure.model_points],
        "closed_holonomy": list(failure.closed_holonomy),
    }


def _scenario_row(
    name,
    interval,
    branch,
    color_tuple,
    *,
    extra_groups=(),
    state_limit=10000,
):
    audit = product_holonomy_exact_audit(
        interval,
        branch,
        color_tuple,
        extra_groups=extra_groups,
        state_limit=state_limit,
    )
    total = solution_from_local_interval(interval).total
    return {
        "name": name,
        "branch": branch,
        "color_tuple": [repr(color) for color in color_tuple],
        "total_tags": list(branch_tags(total)),
        "raw_holonomy_group_orders": [
            len(target.group.elements)
            for target in product_holonomy_groups(interval, branch)
        ],
        "extra_group_orders": list(audit.extra_group_orders),
        "truncated": audit.truncated,
        "visited_state_count": audit.visited_state_count,
        "base_state_count": audit.base_state_count,
        "product_state_count": audit.product_state_count,
        "detector_state_count": audit.detector_state_count,
        "closed_state_count": audit.closed_state_count,
        "identity_detector_closed_state_count": audit.identity_detector_closed_state_count,
        "failure": _failure_json(audit.failure),
        "proves_fixed_tuple_kernel_implication": audit.proves_fixed_tuple_kernel_implication,
    }


def build_report():
    known_failure = two_color_known_nondegenerate_failure_interval()
    scenarios = [
        _scenario_row(
            "coboundary_normalizes_to_identity",
            two_color_swapped_coboundary_interval(),
            "swapped",
            (0, 1),
        ),
        _scenario_row(
            "one_color_pairwise_cyclic_exact",
            one_color_commuting_swapped_interval(),
            "swapped",
            ("*", "*"),
        ),
        _scenario_row(
            "identity_base_cyclic_exact",
            two_color_identity_base_cyclic_interval(),
            "swapped",
            (0, 1, 0),
        ),
        _scenario_row(
            "known_branch_raw_holonomy_failure",
            known_failure,
            "swapped",
            (0, 0),
        ),
        _scenario_row(
            "known_branch_augmented_by_symmetric_factor",
            known_failure,
            "swapped",
            (0, 0),
            extra_groups=(symmetric_group(4),),
        ),
    ]
    totals = {
        "scenario_count": len(scenarios),
        "truncation_count": sum(1 for row in scenarios if row["truncated"]),
        "failure_count": sum(1 for row in scenarios if row["failure"] is not None),
        "proved_fixed_tuple_count": sum(
            1 for row in scenarios if row["proves_fixed_tuple_kernel_implication"]
        ),
        "max_visited_state_count": max(row["visited_state_count"] for row in scenarios),
    }
    report = {"totals": totals, "scenarios": scenarios}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    totals = report["totals"]
    lines = [
        "# Product holonomy exact audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit applies the exact fixed-degree normalized",
        "holonomy image closure to representative product rows.  Unlike the",
        "bounded subgroup scan, it closes the whole finite braid image for the",
        "supplied degree and colour tuple, so it has no word-length cutoff for",
        "those fixed tuples.",
        "",
        "It is still finite diagnostic evidence only.  It is not an all-`n`",
        "proof, and it does not cover arbitrary fibres or arbitrary quotient",
        "colours.",
        "",
        "## Totals",
        "",
        f"Scenarios: `{totals['scenario_count']}`.",
        f"Truncations: `{totals['truncation_count']}`.",
        f"Scenarios with a raw failure: `{totals['failure_count']}`.",
        f"Scenarios proving the fixed-tuple implication: `{totals['proved_fixed_tuple_count']}`.",
        f"Maximum visited states: `{totals['max_visited_state_count']}`.",
        "",
    ]
    for row in report["scenarios"]:
        lines.extend(
            [
                f"## {row['name']}",
                "",
                f"Branch: `{row['branch']}`.",
                f"Colour tuple: `{row['color_tuple']}`.",
                f"Total tags: `{row['total_tags']}`.",
                f"Raw holonomy group orders: `{row['raw_holonomy_group_orders']}`.",
                f"Extra group orders: `{row['extra_group_orders']}`.",
                f"Truncated: `{row['truncated']}`.",
                f"Visited states: `{row['visited_state_count']}`.",
                f"Closed states: `{row['closed_state_count']}`.",
                (
                    "Identity-detector closed states: "
                    f"`{row['identity_detector_closed_state_count']}`."
                ),
                (
                    "Proves fixed-tuple implication: "
                    f"`{row['proves_fixed_tuple_kernel_implication']}`."
                ),
                f"Failure: `{row['failure']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "The exact audit confirms the normalized-holonomy conventions without",
            "a word-length cutoff on the displayed tuples.  It also records a",
            "guardrail: the raw normalized holonomy group can miss a fixed-degree",
            "closed label in a row whose total interval is already in a known",
            "nondegenerate/permutation branch.  Multiplying by the symmetric",
            "known-branch factor removes that displayed failure.",
            "",
            "Thus the product theorem target must keep its detector-product",
            "form: normalized holonomy groups plus the already-known cyclic,",
            "affine, coboundary, or whole-branch detector factors.  A product",
            "counterexample must defeat that full fixed detector product, not",
            "only the raw normalized holonomy group.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
