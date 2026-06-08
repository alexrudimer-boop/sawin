"""Audit proper known-quotient factor closure for non-subdirect F3 rows."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    table_from_indices,
)
from run_linear_f3_skew_flip_monolith_audit import (  # noqa: E402
    solution_from_table,
)
from ybe_domination import (  # noqa: E402
    congruences,
    equality_congruence,
    quotient_factor_compression_audit,
    quotient_solution,
    universal_congruence,
)

SOURCE_JSON = ROOT / "proofs" / "linear_f3_skew_flip_monolith_audit.json"
OUT_JSON = ROOT / "proofs" / "linear_f3_nonsubdirect_quotient_factor_closure_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_nonsubdirect_quotient_factor_closure_audit.md"


def is_left_nondegenerate(solution) -> bool:
    elements = set(solution.elements)
    return all(
        {solution.R[(left, right)][0] for right in solution.elements} == elements
        for left in solution.elements
    )


def is_right_nondegenerate(solution) -> bool:
    elements = set(solution.elements)
    return all(
        {solution.R[(left, right)][1] for left in solution.elements} == elements
        for right in solution.elements
    )


def is_involutive(solution) -> bool:
    return all(
        solution.R[solution.R[(left, right)]] == (left, right)
        for left in solution.elements
        for right in solution.elements
    )


def is_rack_form(solution) -> bool:
    return all(
        solution.R[(left, right)][1] == left
        for left in solution.elements
        for right in solution.elements
    )


def known_dominated_reason(solution) -> str | None:
    if is_rack_form(solution):
        return "rack"
    if is_left_nondegenerate(solution) or is_right_nondegenerate(solution):
        return "nondegenerate"
    if is_involutive(solution):
        return "involutive"
    return None


def source_nonsubdirect_rows() -> list[dict]:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    return [
        row for row in source["rows"]
        if not row.get("monolith_is_nontrivial")
    ]


def run_audit() -> dict:
    rows = []
    failures = []
    distribution = Counter()
    quotient_reason_distribution = Counter()
    for source_row in source_nonsubdirect_rows():
        row_index = source_row["row_index"]
        matrix_indices = tuple(source_row["matrix_indices"])
        solution = solution_from_table(table_from_indices(matrix_indices))
        all_congruences = congruences(solution, max_size=7)
        equality = equality_congruence(solution.elements)
        universal = universal_congruence(solution.elements)
        selected_partitions = []
        selected_quotients = []
        rejected_quotient_count = 0
        for partition in all_congruences:
            if partition in (equality, universal):
                continue
            quotient = quotient_solution(solution, partition).quotient
            reason = known_dominated_reason(quotient)
            if reason is None:
                rejected_quotient_count += 1
                continue
            selected_partitions.append(partition)
            selected_quotients.append(
                {
                    "size": len(quotient.elements),
                    "reason": reason,
                    "block_sizes": sorted(len(block) for block in partition),
                }
            )
            quotient_reason_distribution[(len(quotient.elements), reason)] += 1

        compression = quotient_factor_compression_audit(solution, selected_partitions)
        certificate = compression.certificate
        finite_conditions = (
            None if certificate is None else certificate.finite_conditions_hold
        )
        row_ok = compression.proves_proper_quotient_compression
        row_payload = {
            "row_index": row_index,
            "matrix_indices": list(matrix_indices),
            "congruence_count": len(all_congruences),
            "known_dominated_factor_count": len(selected_partitions),
            "rejected_unknown_factor_count": rejected_quotient_count,
            "known_dominated_quotient_sizes": list(compression.quotient_sizes),
            "known_dominated_quotients": selected_quotients,
            "point_reconstruction_holds": compression.point_reconstruction_holds,
            "active_factor_finite_conditions_hold": finite_conditions,
            "certified_by_known_quotient_factor_product": row_ok,
        }
        distribution[
            (
                len(selected_partitions),
                tuple(compression.quotient_sizes),
                compression.point_reconstruction_holds,
                finite_conditions,
                row_ok,
            )
        ] += 1
        if not row_ok:
            failures.append(row_payload)
        rows.append(row_payload)

    distribution_rows = [
        {
            "case_count": count,
            "known_factor_count": key[0],
            "quotient_sizes": list(key[1]),
            "point_reconstruction_holds": key[2],
            "active_factor_finite_conditions_hold": key[3],
            "certified": key[4],
        }
        for key, count in sorted(distribution.items(), key=lambda item: (-item[1], item[0]))
    ]
    reason_rows = [
        {
            "quotient_size": key[0],
            "reason": key[1],
            "count": count,
        }
        for key, count in sorted(quotient_reason_distribution.items())
    ]
    report = {
        "family": "linear_f3_skew_over_flip_nonsubdirect_rows",
        "source_artifact": str(SOURCE_JSON.relative_to(ROOT)),
        "nonsubdirect_row_count": len(rows),
        "certified_row_count": sum(
            1 for row in rows if row["certified_by_known_quotient_factor_product"]
        ),
        "failure_count": len(failures),
        "failures": failures[:8],
        "distribution": distribution_rows,
        "known_quotient_reason_distribution": reason_rows,
        "rows": rows,
    }
    report["all_claimed_checks_passed"] = (
        report["nonsubdirect_row_count"] == 80
        and report["certified_row_count"] == 80
        and report["failure_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Nonsubdirect Quotient-Factor Closure Audit",
        "",
        "This generated audit closes the `80` non-subdirect rows in the",
        "six-point linear skew-over-flip degenerate non-involutive family.",
        "",
        "## Summary",
        "",
        f"- source artifact: `{report['source_artifact']}`;",
        f"- non-subdirect rows: `{report['nonsubdirect_row_count']}`;",
        f"- certified rows: `{report['certified_row_count']}`;",
        f"- failures: `{report['failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "For each row, the audit selects only proper quotient factors that are",
        "already known dominated: rack-form, nondegenerate, or involutive.",
        "Those selected quotients still reconstruct the original point and pass",
        "the active-factor finite certificate.",
        "",
        "## Known Quotient Reasons",
        "",
        "| quotient size | reason | count |",
        "|---:|---|---:|",
    ]
    for row in report["known_quotient_reason_distribution"]:
        lines.append(f"| {row['quotient_size']} | {row['reason']} | {row['count']} |")
    lines.extend(
        [
            "",
            "## Distribution",
            "",
            "| cases | known factors | quotient sizes | reconstructs | finite conditions | certified |",
            "|---:|---:|---|---|---|---|",
        ]
    )
    for row in report["distribution"]:
        lines.append(
            "| {case_count} | {known_factor_count} | {quotient_sizes} | "
            "{point_reconstruction_holds} | {active_factor_finite_conditions_hold} | "
            "{certified} |".format(**row)
        )
    if report["failures"]:
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(json.dumps(report["failures"], indent=2))
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 nonsubdirect quotient-factor closure audit failed")
    print("OK linear F3 nonsubdirect quotient-factor closure audit")
    print(f"nonsubdirect rows {report['nonsubdirect_row_count']}")
    print(f"certified rows {report['certified_row_count']}")


if __name__ == "__main__":
    main()
