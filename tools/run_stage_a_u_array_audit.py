from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_type_a_solution,
)
from ybe_domination import branch_tags, identity_solution, rack_solution  # noqa: E402
from ybe_domination.stage_a_u_arrays import (  # noqa: E402
    StageAUArrayProfile,
    canonical_u_array,
    relabel_u_array,
    stage_a_enumeration_audit,
    stage_a_profile_from_solution,
    u_array_from_solution,
)

OUT_JSON = ROOT / "proofs" / "stage_a_u_array_audit.json"
OUT_MD = ROOT / "proofs" / "stage_a_u_array_audit.md"


@dataclass(frozen=True)
class StageAAuditRow:
    name: str
    size: int
    branch_tags: tuple[str, ...]
    ybe: bool
    profile: StageAUArrayProfile


def example_rows() -> tuple[StageAAuditRow, ...]:
    examples = (
        ("identity_3", identity_solution((0, 1, 2))),
        ("trivial_rack_3", rack_solution((0, 1, 2), lambda _left, right: right)),
        ("dihedral_rack_3", rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)),
        ("size4_affine_type_a", affine_f2_type_a_solution()),
    )
    return tuple(
        StageAAuditRow(
            name=name,
            size=len(solution.elements),
            branch_tags=branch_tags(solution),
            ybe=solution.is_ybe(),
            profile=stage_a_profile_from_solution(solution),
        )
        for name, solution in examples
    )


def canonicalization_checks() -> dict[str, object]:
    solution = affine_f2_type_a_solution()
    u_array = u_array_from_solution(solution)
    relabeled = relabel_u_array(u_array, (2, 0, 3, 1))
    return {
        "example": "size4_affine_type_a",
        "original_word": list(sum((tuple(row) for row in u_array), ())),
        "relabeled_word": list(sum((tuple(row) for row in relabeled), ())),
        "canonical_equal": canonical_u_array(u_array) == canonical_u_array(relabeled),
    }


def build_report() -> dict[str, object]:
    rows = example_rows()
    exact_size_2 = stage_a_enumeration_audit(2, max_examples=10)
    exact_size_3 = stage_a_enumeration_audit(3, max_examples=10)
    budgeted_size_4 = stage_a_enumeration_audit(4, max_nodes=50_000, max_examples=3)
    return {
        "title": "Stage A U-array audit",
        "purpose": (
            "Record reusable Stage A checks for the size 5/6 "
            "everywhere-singular search: balanced U counts, singular U rows, "
            "Y1-derived A_xy feasibility, and simultaneous-relabeling "
            "canonicalization."
        ),
        "stage_a_constraints": [
            "each symbol occurs exactly d times in U",
            "each row map y -> U[x,y] is singular",
            "A_xy={v : L_{U[x,y]} L_v = L_x L_y} is nonempty for every cell",
            (
                "for every u, multiset{L_x L_y : L_x(y)=u} equals "
                "multiset{L_u L_v : v in X}"
            ),
            "U is canonicalized under simultaneous relabeling",
        ],
        "rows": [
            {
                "name": row.name,
                "size": row.size,
                "branch_tags": row.branch_tags,
                "ybe": row.ybe,
                "profile": asdict(row.profile),
            }
            for row in rows
        ],
        "canonicalization": canonicalization_checks(),
        "enumeration": {
            "exact_size_2": asdict(exact_size_2),
            "exact_size_3": asdict(exact_size_3),
            "budgeted_size_4": asdict(budgeted_size_4),
        },
        "conclusion": (
            "The Stage A code separates one-sided nondegenerate rack rows from "
            "everywhere-singular U-data.  The multiset-factorization law "
            "shrinks the exact size-3 canonical Stage A baseline from six "
            "A_xy-feasible arrays to one MF-valid array.  The budgeted size-4 "
            "run remains a truncated search, but all retained examples now "
            "satisfy the stronger Y1-plus-bijectivity law."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-stage-a-u-array-enumeration_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Stage A U-Array Audit",
        "",
        str(report["purpose"]),
        "",
        "## Constraints",
        "",
    ]
    for constraint in report["stage_a_constraints"]:
        lines.append(f"- {constraint};")
    lines.extend(["", "## Example Rows", ""])
    for row in report["rows"]:
        profile = row["profile"]
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- tags: `{row['branch_tags']}`;",
                f"- YBE: `{row['ybe']}`;",
                f"- balanced symbol counts: `{profile['balanced_symbol_counts']}`;",
                f"- rows singular: `{profile['rows_singular']}`;",
                f"- A_xy nonempty: `{profile['feasibility_nonempty']}`;",
                f"- multiset factorization: `{profile['multiset_factorization']}`;",
                f"- Stage A candidate: `{profile['stage_a_candidate']}`;",
                "- feasibility size range: "
                f"`{profile['minimum_feasibility_size']}..{profile['maximum_feasibility_size']}`;",
                f"- feasibility size counts: `{profile['feasibility_size_counts']}`;",
                f"- bucket count: `{profile['bucket_count']}`;",
                f"- maximum bucket size: `{profile['maximum_bucket_size']}`;",
                f"- canonical: `{profile['canonical']}`.",
                "",
            ]
        )
    canonical = report["canonicalization"]
    lines.extend(
        [
            "## Canonicalization Check",
            "",
            f"- example: `{canonical['example']}`;",
            f"- canonical equal after relabeling: `{canonical['canonical_equal']}`;",
            "",
            "## Enumeration Baseline",
            "",
        ]
    )
    enumeration = report["enumeration"]
    for name, audit in enumeration.items():
        lines.extend(
            [
                f"### {name}",
                "",
                f"- size: `{audit['size']}`;",
                f"- nodes: `{audit['node_count']}`;",
                f"- completed balanced arrays: `{audit['completed_balanced_count']}`;",
                f"- row-singular arrays: `{audit['row_singular_count']}`;",
                f"- A_xy feasible arrays: `{audit['feasibility_nonempty_count']}`;",
                "- multiset-factorization arrays: "
                f"`{audit['multiset_factorization_count']}`;",
                f"- canonical arrays: `{audit['canonical_count']}`;",
                f"- emitted examples: `{audit['emitted_count']}`;",
                f"- truncated: `{audit['truncated']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Conclusion",
            "",
            str(report["conclusion"]),
            "",
            "## Next Prompt",
            "",
            f"`{report['next_prompt']}`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
