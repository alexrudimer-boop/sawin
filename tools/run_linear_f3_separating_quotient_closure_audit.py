"""Audit closure of monolith J-separating linear F3 subdirect rows."""

from __future__ import annotations

import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    table_from_indices,
)
from run_linear_f3_skew_flip_monolith_audit import (  # noqa: E402
    meet_partitions,
    solution_from_table,
)
from ybe_domination import (  # noqa: E402
    congruences,
    contextual_completion_data,
    equality_congruence,
    identity_extension_summary,
    quotient_solution,
    relative_contextual_separation_summary,
)

SOURCE_JSON = ROOT / "proofs" / "linear_f3_skew_flip_monolith_audit.json"
OUT_JSON = ROOT / "proofs" / "linear_f3_separating_quotient_closure_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_separating_quotient_closure_audit.md"


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


def canonical_table(solution) -> tuple[tuple[int, int], ...]:
    elements = tuple(solution.elements)
    best = None
    for old_to_new in itertools.permutations(range(len(elements))):
        new_to_old = [0] * len(elements)
        for old, new in enumerate(old_to_new):
            new_to_old[new] = old
        table = []
        for new_left in range(len(elements)):
            for new_right in range(len(elements)):
                old_left = elements[new_to_old[new_left]]
                old_right = elements[new_to_old[new_right]]
                out_left, out_right = solution.R[(old_left, old_right)]
                table.append(
                    (
                        old_to_new[elements.index(out_left)],
                        old_to_new[elements.index(out_right)],
                    )
                )
        candidate = tuple(table)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        raise ValueError("empty solution")
    return best


def partition_labels(partition) -> dict[int, int]:
    return {
        element: block_index
        for block_index, block in enumerate(partition)
        for element in block
    }


def monolith_for_solution(solution):
    all_congruences = congruences(solution, max_size=7)
    equality = equality_congruence(solution.elements)
    nontrivial = [
        partition
        for partition in all_congruences
        if partition != equality
    ]
    return all_congruences, meet_partitions(nontrivial)


def source_separating_rows() -> list[dict]:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = []
    for row in source["rows"]:
        monolith = row.get("monolith")
        if not monolith:
            continue
        relative = monolith.get("relative_separation")
        if (
            relative
            and relative.get("checked")
            and relative.get("proves_all_arity_injective")
            and not relative.get("collision_found")
        ):
            rows.append(row)
    return rows


def run_audit() -> dict:
    rows = []
    quotient_types = defaultdict(list)
    failures = []
    for source_row in source_separating_rows():
        row_index = source_row["row_index"]
        matrix_indices = tuple(source_row["matrix_indices"])
        solution = solution_from_table(table_from_indices(matrix_indices))
        data = contextual_completion_data(solution)
        identity_summary = identity_extension_summary(data)
        all_congruences, monolith = monolith_for_solution(solution)
        qmap = quotient_solution(solution, monolith)
        quotient = qmap.quotient
        labels = partition_labels(monolith)
        relative = relative_contextual_separation_summary(
            data,
            labels,
            max_vertices=2_000_000,
        )
        quotient_signature = canonical_table(quotient)
        quotient_type_key = json.dumps(quotient_signature)
        quotient_types[quotient_type_key].append(row_index)
        row_payload = {
            "row_index": row_index,
            "matrix_indices": list(matrix_indices),
            "monolith_blocks": [sorted(block) for block in monolith],
            "congruence_count": len(all_congruences),
            "contextual_class_count": data.class_count,
            "contextual_identity_extension_total_permutations": (
                identity_summary.identity_extension_total_permutations
            ),
            "contextual_identity_extension_covariance": (
                identity_summary.identity_extension_conjugacy_covariance
            ),
            "contextual_conflict_count": identity_summary.conflict_count,
            "relative_j_separation_checked": relative.checked,
            "relative_j_separation_proves_all_arity": (
                relative.proves_all_arity_injective
            ),
            "relative_j_collision_found": relative.collision_found,
            "relative_valid_vertex_count": relative.valid_vertex_count,
            "quotient_size": len(quotient.elements),
            "quotient_left_nondegenerate": is_left_nondegenerate(quotient),
            "quotient_right_nondegenerate": is_right_nondegenerate(quotient),
            "quotient_involutive": is_involutive(quotient),
            "quotient_canonical_type": quotient_type_key,
        }
        row_ok = (
            row_payload["contextual_identity_extension_total_permutations"]
            and row_payload["contextual_identity_extension_covariance"]
            and row_payload["contextual_conflict_count"] == 0
            and row_payload["relative_j_separation_checked"]
            and row_payload["relative_j_separation_proves_all_arity"]
            and not row_payload["relative_j_collision_found"]
            and row_payload["quotient_size"] == 4
            and row_payload["quotient_involutive"]
        )
        row_payload["certified_by_relative_involutive_quotient"] = row_ok
        if not row_ok:
            failures.append(row_payload)
        rows.append(row_payload)

    quotient_type_rows = [
        {
            "type_index": index,
            "case_count": len(row_indices),
            "row_indices": row_indices,
            "canonical_table": json.loads(signature),
        }
        for index, (signature, row_indices) in enumerate(
            sorted(quotient_types.items(), key=lambda item: item[1][0])
        )
    ]
    report = {
        "family": "linear_f3_skew_over_flip_monolith_j_separating_rows",
        "source_artifact": str(SOURCE_JSON.relative_to(ROOT)),
        "separating_row_count": len(rows),
        "certified_row_count": sum(
            1 for row in rows if row["certified_by_relative_involutive_quotient"]
        ),
        "failure_count": len(failures),
        "failures": failures[:8],
        "quotient_isomorphism_type_count": len(quotient_type_rows),
        "quotient_types": quotient_type_rows,
        "rows": rows,
    }
    report["all_claimed_checks_passed"] = (
        report["separating_row_count"] == 32
        and report["certified_row_count"] == 32
        and report["failure_count"] == 0
        and report["quotient_isomorphism_type_count"] == 2
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Separating Quotient Closure Audit",
        "",
        "This generated audit closes the monolith `J`-separating subdirect",
        "rows in the six-point linear skew-over-flip degenerate",
        "non-involutive family.",
        "",
        "## Summary",
        "",
        f"- source artifact: `{report['source_artifact']}`;",
        f"- separating rows: `{report['separating_row_count']}`;",
        f"- certified rows: `{report['certified_row_count']}`;",
        f"- failures: `{report['failure_count']}`;",
        "- quotient isomorphism types: "
        f"`{report['quotient_isomorphism_type_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "Each certified row has:",
        "",
        "- an identity-extension contextual rack completion preserving forced products;",
        "- all-arity injectivity of `(pi_mu^n,J_n)` from the finite relative graph;",
        "- an involutive four-point monolith quotient, hence a dominated quotient by the known involutive theorem.",
        "",
        "The relative contextual extension theorem then gives finite-rack",
        "domination of the six-point row.",
        "",
        "## Quotient Types",
        "",
        "| type | cases | rows |",
        "|---:|---:|---|",
    ]
    for row in report["quotient_types"]:
        lines.append(
            f"| {row['type_index']} | {row['case_count']} | {row['row_indices']} |"
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
        raise SystemExit("linear F3 separating quotient closure audit failed")
    print("OK linear F3 separating quotient closure audit")
    print(f"separating rows {report['separating_row_count']}")
    print(f"certified rows {report['certified_row_count']}")


if __name__ == "__main__":
    main()
