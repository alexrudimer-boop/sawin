"""Contextual audit for cached two-colour, fibre-2 representative totals."""

from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    LocalInterval,
    branch_tags,
    contextual_completion_data,
    contextual_readout_equivariance_failure,
    identity_extension_summary,
    orbit_readout_collision,
    solution_from_local_interval,
)

SOURCE_JSON = ROOT / "proofs" / "two_colour_fibre2_all_bases_audit.json"
OUT_JSON = ROOT / "proofs" / "two_colour_fibre2_contextual_audit.json"
OUT_MD = ROOT / "proofs" / "two_colour_fibre2_contextual_audit.md"


def _parse_repr(text: str):
    return ast.literal_eval(text)


def _tag_text(tags) -> str:
    return "+".join(tags) if tags else "(untagged)"


def _base_solution(base_signature) -> FiniteBraidedSet:
    elements = (0, 1)
    pairs = tuple((left, right) for left in elements for right in elements)
    table = {
        pair: tuple(image)
        for pair, image in zip(pairs, base_signature)
    }
    return FiniteBraidedSet(elements, table)


def _interval_from_payload(base_signature, interval_table) -> LocalInterval:
    base = _base_solution(base_signature)
    fibres = {color: (0, 1) for color in base.elements}
    table = {}
    for entry in interval_table:
        a, b = (_parse_repr(value) for value in entry["colors"])
        x, y = (_parse_repr(value) for value in entry["input"])
        u, v = (_parse_repr(value) for value in entry["output"])
        table[(a, b, x, y)] = (u, v)
    return LocalInterval(base.elements, fibres, base.R, table)


def _profile_key(row: dict) -> tuple:
    summary = row["contextual_summary"]
    return (
        row["tags_text"],
        row["source_row"]["retraction"],
        row["source_row"]["coretraction"],
        summary["left_monoid_size"],
        summary["right_monoid_size"],
        summary["class_count"],
        summary["forced_product_count"],
        tuple(summary["domain_sizes"]),
        summary["nontrivial_left_translation_count"],
        summary["identity_extension_witnesses_active_lifts"],
    )


def _profile_payload(key: tuple, count: int) -> dict:
    return {
        "case_count": count,
        "tags": key[0],
        "retraction": key[1],
        "coretraction": key[2],
        "left_monoid_size": key[3],
        "right_monoid_size": key[4],
        "contextual_class_count": key[5],
        "forced_product_count": key[6],
        "domain_sizes": list(key[7]),
        "nontrivial_left_translation_count": key[8],
        "identity_extension_witnesses_active_lifts": key[9],
    }


def iter_cached_representatives(source_payload: dict):
    for base_name, scan in source_payload["bases"].items():
        for source_key, payload in scan["first_examples"].items():
            interval = _interval_from_payload(
                scan["base_signature"],
                payload["interval_table"],
            )
            yield {
                "base_name": base_name,
                "source_key": source_key,
                "source_row": payload["row"],
                "interval": interval,
            }


def run_audit(max_arity: int) -> dict:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = []
    failures = []
    equivariance_failures = []
    orbit_failures = []
    profile_counts = Counter()
    tag_counts = Counter()

    for index, representative in enumerate(iter_cached_representatives(source)):
        interval = representative["interval"]
        if not interval.is_colored_ybe():
            raise AssertionError("cached representative is not colored-YBE")
        if not interval.is_local_minimal(max_fibre_size=2):
            raise AssertionError("cached representative is not local-minimal")
        total = solution_from_local_interval(interval).total
        tags = branch_tags(total)
        tag_counts[_tag_text(tags)] += 1
        data = contextual_completion_data(total)
        summary = identity_extension_summary(data)
        contextual_summary = asdict(summary)
        contextual_summary[
            "identity_extension_witnesses_active_lifts"
        ] = summary.identity_extension_witnesses_active_lifts
        row = {
            "representative_index": index,
            "base_name": representative["base_name"],
            "source_key": representative["source_key"],
            "source_row": representative["source_row"],
            "tags": list(tags),
            "tags_text": _tag_text(tags),
            "contextual_summary": contextual_summary,
            "equivariance_checks": [],
            "orbit_arity_checks": [],
        }
        key = _profile_key(row)
        profile_counts[key] += 1
        contextual_ok = (
            summary.conflict_count == 0
            and summary.partial_translations_injective
            and summary.balanced_domains
            and summary.identity_extension_total_permutations
            and summary.identity_extension_conjugacy_covariance
            and summary.full_forced_graph_local_covariance_failures == 0
        )
        if not contextual_ok:
            failures.append(row)
            rows.append(row)
            continue

        for arity in range(1, max_arity + 1):
            equivariance_result = contextual_readout_equivariance_failure(
                total,
                data,
                arity,
            )
            row["equivariance_checks"].append(equivariance_result)
            if equivariance_result.get("failure") is not None:
                equivariance_failures.append(
                    {
                        "row": row,
                        "result": equivariance_result,
                    }
                )
                break
            result = orbit_readout_collision(total, data, arity)
            row["orbit_arity_checks"].append(result)
            if result.get("collision") is not None:
                orbit_failures.append({"row": row, "result": result})
                break
        rows.append(row)

    profiles = [
        _profile_payload(key, count)
        for key, count in sorted(
            profile_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )
    ]
    source_totals = source["totals"]
    return {
        "corpus": "cached_two_colour_fibre2_all_base_representatives",
        "source_audit": str(SOURCE_JSON.relative_to(ROOT)),
        "source_totals": source_totals,
        "max_arity": max_arity,
        "representative_count": len(rows),
        "tag_counts": dict(sorted(tag_counts.items())),
        "profile_count": len(profiles),
        "profiles": profiles,
        "contextual_failure_count": len(failures),
        "contextual_failures": failures[:8],
        "equivariance_failure_count": len(equivariance_failures),
        "equivariance_failures": equivariance_failures[:8],
        "orbit_failure_count": len(orbit_failures),
        "orbit_failures": orbit_failures[:8],
        "rows": rows,
        "all_claimed_checks_passed": (
            source_totals["checked_table_count"] == 1_658_880
            and source_totals["colored_ybe_count"] == 629
            and source_totals["local_minimal_count"] == 120
            and len(rows) == 15
            and not failures
            and not equivariance_failures
            and not orbit_failures
        ),
    }


def write_markdown(report: dict) -> str:
    totals = report["source_totals"]
    lines = [
        "# Two-Colour Fibre-2 Contextual Representative Audit",
        "",
        "This generated audit consumes the representative interval tables",
        "retained by `two_colour_fibre2_all_bases_audit.json` and applies the",
        "generic two-sided contextual completion/readout helper to the",
        "corresponding four-point total YBE solutions.",
        "",
        "It is a representative audit, not a full-row contextual pass over all",
        "120 local-minimal totals.",
        "",
        "## Source Corpus",
        "",
        f"- source audit: `{report['source_audit']}`;",
        f"- local tables checked by source audit: `{totals['checked_table_count']}`;",
        f"- coloured-YBE local tables: `{totals['colored_ybe_count']}`;",
        f"- local-minimal totals: `{totals['local_minimal_count']}`;",
        "- source unknown universal-output examples: "
        f"`{totals['unknown_universal_output_example_count']}`.",
        "",
        "## Contextual Representative Checks",
        "",
        f"- cached representatives checked: `{report['representative_count']}`;",
        f"- tag counts: `{report['tag_counts']}`;",
        f"- contextual profile count: `{report['profile_count']}`;",
        f"- contextual completion failure count: `{report['contextual_failure_count']}`;",
        f"- identity-extension equivariance checked through arity: `{report['max_arity']}`;",
        f"- equivariance failure count: `{report['equivariance_failure_count']}`;",
        f"- orbit-injectivity checked through arity: `{report['max_arity']}`;",
        f"- orbit-injectivity failure count: `{report['orbit_failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Contextual Profiles",
        "",
        "| cases | tags | retraction | coretraction | M_L | M_R | P | forced | domains | nontriv L |",
        "|---:|---|---|---|---:|---:|---:|---:|---|---:|",
    ]
    for row in report["profiles"]:
        lines.append(
            "| {case_count} | {tags} | {retraction} | {coretraction} | "
            "{left_monoid_size} | {right_monoid_size} | "
            "{contextual_class_count} | {forced_product_count} | "
            "{domain_sizes} | {nontrivial_left_translation_count} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "The cached representatives include the untagged rows retained by the",
            "older two-colour/fibre-2 corridor audit.  None of these",
            "representatives exhibits an identity-extension, active-lift, or",
            "checked-arity equivariance or contextual readout obstruction.  This is finite",
            "candidate-search evidence only; it does not prove all-arity",
            "orbit separation or cover every one of the 120 local-minimal rows.",
        ]
    )
    if (
        report["contextual_failures"]
        or report["equivariance_failures"]
        or report["orbit_failures"]
    ):
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(
            json.dumps(
                {
                    "contextual": report["contextual_failures"],
                    "equivariance": report["equivariance_failures"],
                    "orbit": report["orbit_failures"],
                },
                indent=2,
            )
        )
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-arity", type=int, default=6)
    args = parser.parse_args()
    report = run_audit(args.max_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("two-colour fibre-2 contextual representative audit failed")
    print("OK two-colour fibre-2 contextual representative audit")
    print(f"representatives {report['representative_count']}")
    print(f"contextual profiles {report['profile_count']}")
    print(f"max arity {report['max_arity']}")


if __name__ == "__main__":
    main()
