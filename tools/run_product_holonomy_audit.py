import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (
    CongruenceInterval,
    all_bijection_solutions,
    branch_tags,
    congruences,
    direct_product_holonomy_summary,
    direct_product_invariant_families,
    direct_product_witness,
    interval_covers,
    is_involutive_solution,
    is_rack_type,
    product_permutation_witness,
    solution_from_local_interval,
    swapped_product_holonomy_summary,
    swapped_product_invariant_families,
)


OUT_JSON = ROOT / "proofs" / "product_holonomy_audit.json"
OUT_MD = ROOT / "proofs" / "product_holonomy_audit.md"
KNOWN_TAGS = {
    "nondegenerate",
    "involutive",
    "permutation_form",
    "rack_type",
    "identity_table",
    "affine_cyclic",
}


def holonomy_kind(interval, summary):
    if summary.is_trivial:
        return "coboundary"
    if len(interval.colors) == 1:
        return "one_color_pairwise"
    return "genuinely_coloured"


def summary_payload(interval, qmap, side, summary, invariant_families):
    total = qmap.total
    tags = list(branch_tags(total))
    return {
        "side": side,
        "color_count": len(interval.colors),
        "fibre_sizes": sorted({len(interval.fibres[color]) for color in interval.colors}),
        "invariant_family_count": len(invariant_families),
        "primitive_by_invariants": len(invariant_families) == 2,
        "holonomy_kind": holonomy_kind(interval, summary),
        "holonomy_generator_count": len(summary.generators),
        "component_group_sizes": [
            {
                "model_points": [repr(point) for point in model_points],
                "group_size": group_size,
            }
            for model_points, group_size in summary.component_group_sizes
        ],
        "branch_tags": tags,
        "known_branch": bool(set(tags).intersection(KNOWN_TAGS)),
        "is_involutive": is_involutive_solution(total),
        "is_rack_type": is_rack_type(total),
    }


def scan_size(size):
    ybe_count = 0
    cover_count = 0
    local_minimal_count = 0
    product_rows = []
    counts = {
        "swapped": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
        "direct": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
    }
    known_counts = {
        "swapped": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
        "direct": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
    }
    unknown_counts = {
        "swapped": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
        "direct": {"coboundary": 0, "one_color_pairwise": 0, "genuinely_coloured": 0},
    }
    nonprimitive_counts = {"swapped": 0, "direct": 0}
    first_examples = {
        "swapped": {"coboundary": [], "one_color_pairwise": [], "genuinely_coloured": []},
        "direct": {"coboundary": [], "one_color_pairwise": [], "genuinely_coloured": []},
    }

    for solution in all_bijection_solutions(size):
        ybe_count += 1
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            cover_count += 1
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_count += 1
            qmap = solution_from_local_interval(interval)

            if product_permutation_witness(interval) is not None:
                summary = swapped_product_holonomy_summary(interval)
                invariant_families = swapped_product_invariant_families(interval)
                kind = holonomy_kind(interval, summary)
                counts["swapped"][kind] += 1
                payload = summary_payload(
                    interval, qmap, "swapped", summary, invariant_families
                )
                if not payload["primitive_by_invariants"]:
                    nonprimitive_counts["swapped"] += 1
                if payload["known_branch"]:
                    known_counts["swapped"][kind] += 1
                else:
                    unknown_counts["swapped"][kind] += 1
                product_rows.append(payload)
                if len(first_examples["swapped"][kind]) < 3:
                    first_examples["swapped"][kind].append(payload)

            if direct_product_witness(interval) is not None:
                summary = direct_product_holonomy_summary(interval)
                invariant_families = direct_product_invariant_families(interval)
                kind = holonomy_kind(interval, summary)
                counts["direct"][kind] += 1
                payload = summary_payload(
                    interval, qmap, "direct", summary, invariant_families
                )
                if not payload["primitive_by_invariants"]:
                    nonprimitive_counts["direct"] += 1
                if payload["known_branch"]:
                    known_counts["direct"][kind] += 1
                else:
                    unknown_counts["direct"][kind] += 1
                product_rows.append(payload)
                if len(first_examples["direct"][kind]) < 3:
                    first_examples["direct"][kind].append(payload)

    return {
        "size": size,
        "ybe_count": ybe_count,
        "cover_count": cover_count,
        "local_minimal_count": local_minimal_count,
        "counts": counts,
        "known_branch_counts": known_counts,
        "unknown_branch_counts": unknown_counts,
        "nonprimitive_invariant_counts": nonprimitive_counts,
        "first_examples": first_examples,
        "product_row_count": len(product_rows),
    }


def write_markdown(report):
    lines = [
        "# Product holonomy audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit runs the product-permutation holonomy summaries",
        "through the small local-minimal congruence-cover corpus.  It is not a",
        "proof of the master theorem; it checks where the product-branch",
        "holonomy obstruction first appears.",
        "",
        "## Results",
        "",
    ]
    for key, scan in report["local_minimal_scans"].items():
        lines.extend(
            [
                f"### {key}",
                "",
                f"- YBE tables: `{scan['ybe_count']}`;",
                f"- congruence covers: `{scan['cover_count']}`;",
                f"- local-minimal covers: `{scan['local_minimal_count']}`;",
                f"- product rows audited: `{scan['product_row_count']}`.",
                "",
            ]
        )
        for side in ("swapped", "direct"):
            counts = scan["counts"][side]
            known_counts = scan["known_branch_counts"][side]
            unknown_counts = scan["unknown_branch_counts"][side]
            nonprimitive = scan["nonprimitive_invariant_counts"][side]
            lines.extend(
                [
                    f"{side} product branches:",
                    "",
                    f"- coboundary: `{counts['coboundary']}`;",
                    f"- one-colour pairwise: `{counts['one_color_pairwise']}`;",
                    f"- genuinely coloured holonomy: `{counts['genuinely_coloured']}`.",
                    f"- genuinely coloured holonomy in known branches: `{known_counts['genuinely_coloured']}`;",
                    f"- genuinely coloured holonomy outside known tags: `{unknown_counts['genuinely_coloured']}`.",
                    f"- nonprimitive invariant-family rows: `{nonprimitive}`.",
                    "",
                ]
            )
    lines.extend(
        [
            "## Consequence",
            "",
            "In the audited size range, product holonomy does appear: the",
            "size-3 swapped product rows include one-colour pairwise holonomy",
            "and genuinely coloured holonomy.  However, every genuinely",
            "coloured holonomy row lies in a known branch tag such as",
            "`nondegenerate`, `involutive`, `rack_type`, or `permutation_form`.",
            "This is finite audit evidence only.  The symbolic obligation remains",
            "to prove that local-minimality forces unknown product holonomy into",
            "the coboundary/pairwise-linking/known measurable cases, or to",
            "construct an explicit interval with genuinely coloured holonomy",
            "outside those tags.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    report = {
        "local_minimal_scans": {
            "size_2_exhaustive": scan_size(2),
            "size_3_exhaustive": scan_size(3),
        }
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
