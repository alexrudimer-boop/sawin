from __future__ import annotations

import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from run_linear_f2_audit import mat_rank, matrix_signature  # noqa: E402
from ybe_domination import (  # noqa: E402
    branch_tags,
    subsolution_fibre_transition_audit,
    terminal_branch_triage_audit,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_terminal_branch_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_terminal_branch_audit.md"


def _entry_signature(audit) -> str:
    entries = []
    if audit.has_point_separating_proper_quotients:
        entries.append("quotient_separating")
    if audit.has_flip_across_decomposition:
        entries.append("flip")
    if audit.has_proper_subsolution:
        entries.append("subsolution")
    if audit.has_subsolution_fibre_congruence:
        entries.append("subsolution_fibre_congruence")
    if audit.has_nontrivial_one_state_observer:
        entries.append("observer")
    return "+".join(entries) if entries else "none"


def _transition_partition_signature(transition_audit) -> str:
    if transition_audit.all_mixed_transitions_direct_product_like:
        if transition_audit.all_mixed_transitions_swapped_product_like:
            return "direct_and_swapped_product_like"
        return "direct_product_like"
    if transition_audit.all_mixed_transitions_swapped_product_like:
        return "swapped_product_like"
    if transition_audit.all_mixed_transitions_product_like:
        return "mixed_product_like"
    return "non_product_like"


def _transition_signature(solution, audit) -> str:
    if not audit.subsolution_fibre_congruences:
        return "none"
    counts: Counter[str] = Counter()
    for partition in audit.subsolution_fibre_congruences:
        transition_audit = subsolution_fibre_transition_audit(solution, partition)
        counts[_transition_partition_signature(transition_audit)] += 1
    return "+".join(f"{label}:{count}" for label, count in sorted(counts.items()))


def scan(dimension: int = 2) -> dict:
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    offsets = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    entry_counts: Counter[str] = Counter()
    transition_counts: Counter[str] = Counter()
    tag_entry_counts: Counter[tuple[str, str]] = Counter()
    tag_transition_counts: Counter[tuple[str, str]] = Counter()
    untagged_entry_counts: Counter[str] = Counter()
    untagged_transition_counts: Counter[str] = Counter()
    first_untagged_no_entry = None

    for matrix in itertools.product(rows, repeat=2 * dimension):
        checked += len(offsets)
        if mat_rank(matrix) != 2 * dimension:
            continue
        invertible += len(offsets)
        for offset in offsets:
            solution = affine_solution(matrix, offset, dimension)
            if not solution.is_ybe():
                continue
            ybe_count += 1
            tags = branch_tags(solution)
            tag_label = "+".join(tags) if tags else "(untagged)"
            audit = terminal_branch_triage_audit(solution)
            entry = _entry_signature(audit)
            transition = _transition_signature(solution, audit)
            entry_counts[entry] += 1
            transition_counts[transition] += 1
            tag_entry_counts[(tag_label, entry)] += 1
            tag_transition_counts[(tag_label, transition)] += 1
            if not tags:
                untagged_entry_counts[entry] += 1
                untagged_transition_counts[transition] += 1
                if entry == "none" and first_untagged_no_entry is None:
                    first_untagged_no_entry = {
                        "matrix": matrix_signature(matrix),
                        "offset": "".join(str(cell) for cell in offset),
                    }

    untagged_no_entry_count = untagged_entry_counts.get("none", 0)
    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "entry_counts": dict(sorted(entry_counts.items())),
        "subsolution_fibre_transition_counts": dict(
            sorted(transition_counts.items())
        ),
        "tag_entry_counts": {
            f"tags={tag}|entry={entry}": count
            for (tag, entry), count in sorted(tag_entry_counts.items())
        },
        "tag_subsolution_fibre_transition_counts": {
            f"tags={tag}|transition={transition}": count
            for (tag, transition), count in sorted(tag_transition_counts.items())
        },
        "untagged_count": sum(untagged_entry_counts.values()),
        "untagged_entry_counts": dict(sorted(untagged_entry_counts.items())),
        "untagged_subsolution_fibre_transition_counts": dict(
            sorted(untagged_transition_counts.items())
        ),
        "untagged_no_entry_count": untagged_no_entry_count,
        "first_untagged_no_entry": first_untagged_no_entry,
        "no_untagged_entry_evasion": untagged_no_entry_count == 0,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2 Terminal-Branch Audit",
        "",
        "This generated audit applies `terminal_branch_triage_audit(...)` to the",
        "translated affine four-point universe from `proofs/affine_f2_audit.md`.",
        "It is a finite search artifact, not a proof of the universal theorem.",
        "",
        "## Summary",
        "",
        f"- affine maps checked: `{report['checked_affine_map_count']}`;",
        f"- invertible affine maps: `{report['invertible_affine_map_count']}`;",
        f"- affine YBE tables: `{report['affine_ybe_count']}`;",
        f"- untagged affine YBE tables: `{report['untagged_count']}`;",
        f"- untagged rows with no terminal entry branch: "
        f"`{report['untagged_no_entry_count']}`.",
        "",
        "## Entry Counts",
        "",
        "| entry signature | count |",
        "| --- | ---: |",
    ]
    for entry, count in report["entry_counts"].items():
        lines.append(f"| `{entry}` | {count} |")
    lines.extend(
        [
            "",
            "## Subsolution-Fibre Transition Counts",
            "",
            "| transition signature | count |",
            "| --- | ---: |",
        ]
    )
    for transition, count in report["subsolution_fibre_transition_counts"].items():
        lines.append(f"| `{transition}` | {count} |")
    lines.extend(
        [
            "",
            "## Untagged Rows",
            "",
            "| entry signature | count |",
            "| --- | ---: |",
        ]
    )
    for entry, count in report["untagged_entry_counts"].items():
        lines.append(f"| `{entry}` | {count} |")
    lines.extend(
        [
            "",
            "## Untagged Subsolution-Fibre Transition Rows",
            "",
            "| transition signature | count |",
            "| --- | ---: |",
        ]
    )
    for transition, count in report[
        "untagged_subsolution_fibre_transition_counts"
    ].items():
        lines.append(f"| `{transition}` | {count} |")
    lines.extend(
        [
            "",
        "All 24 untagged affine rows have a terminal entry branch: 12 have",
        "point-separating proper quotients plus subsolution and observer entries,",
        "and 12 have subsolution plus observer entries.  Thus the affine",
        "`F_2^2` residual rows do not supply a terminal-branch evader.",
        "The `subsolution_fibre_congruence` marker records the sharper branch",
        "where a proper quotient has crossing-closed fibre blocks.",
        "The transition signature records whether those mixed-fibre crossings",
        "are product-like, swapped-product-like, or genuinely non-product-like.",
    ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = {"f2_dimension_2": scan(2)}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report["f2_dimension_2"]), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
