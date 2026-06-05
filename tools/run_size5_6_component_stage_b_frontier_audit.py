from __future__ import annotations

import json
import sys
from dataclasses import asdict
from math import factorial
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_rigid_pressure_core_audit import rigid_pressure_core_row  # noqa: E402
from ybe_domination.stage_a_u_arrays import (  # noqa: E402
    row_catalogue_stage_a_enumeration_audit,
    solution_from_uv_arrays,
    stage_a_factorization_buckets,
    stage_b_component_solver_audit,
    stage_b_component_v_search_audit,
    stage_b_relation_gac_audit,
)

OUT_JSON = ROOT / "proofs" / "size5_6_component_stage_b_frontier_audit.json"
OUT_MD = ROOT / "proofs" / "size5_6_component_stage_b_frontier_audit.md"


def _u_frontier_rows(
    size: int,
    *,
    stage_a_max_nodes: int,
    stage_a_max_examples: int,
    max_component_solutions: int,
    max_v_examples: int,
    max_bucket_permutations: int,
) -> tuple[dict[str, object], ...]:
    stage_a = row_catalogue_stage_a_enumeration_audit(
        size,
        max_nodes=stage_a_max_nodes,
        max_examples=stage_a_max_examples,
    )
    rows = []
    for index, u_array in enumerate(stage_a.examples):
        buckets = stage_a_factorization_buckets(u_array)
        maximum_bucket_permutations = max(
            (factorial(len(bucket.cells)) for bucket in buckets),
            default=0,
        )
        if maximum_bucket_permutations > max_bucket_permutations:
            rows.append(
                {
                    "u_index": index,
                    "u_rows": u_array,
                    "maximum_bucket_permutations": maximum_bucket_permutations,
                    "stage_b_skipped_reason": (
                        "maximum bucket permutation count exceeds bound"
                    ),
                    "relation_gac": None,
                    "component_solver": None,
                    "component_search": None,
                    "solution_rows": [],
                }
            )
            continue
        relation_gac = stage_b_relation_gac_audit(u_array)
        component_solver = stage_b_component_solver_audit(
            u_array,
            max_component_solutions=max_component_solutions,
        )
        component_search = stage_b_component_v_search_audit(
            u_array,
            max_component_solutions=max_component_solutions,
            max_examples=max_v_examples,
        )
        solution_rows = []
        for v_index, v_array in enumerate(component_search.examples):
            solution = solution_from_uv_arrays(u_array, v_array)
            solution_rows.append(
                {
                    "name": f"size{size}_u{index}_v{v_index}",
                    "ybe": solution.is_ybe(),
                    "rigid_pressure_core_row": asdict(
                        rigid_pressure_core_row(
                            f"size{size}_u{index}_v{v_index}",
                            solution,
                            run_pressure_if_structural=False,
                        )
                    ),
                }
            )
        rows.append(
            {
                "u_index": index,
                "u_rows": u_array,
                "maximum_bucket_permutations": maximum_bucket_permutations,
                "stage_b_skipped_reason": None,
                "relation_gac": asdict(relation_gac),
                "component_solver": asdict(component_solver),
                "component_search": asdict(component_search),
                "solution_rows": solution_rows,
            }
        )
    return tuple(
        [
            {
                "size": size,
                "stage_a": asdict(stage_a),
                "u_rows": rows,
            }
        ]
    )


def build_report(
    *,
    stage_a_max_nodes: int = 1000,
    stage_a_max_examples: int = 3,
    max_component_solutions: int = 10000,
    max_v_examples: int = 3,
    max_bucket_permutations: int = 120,
) -> dict[str, object]:
    size_rows = []
    for size in (5, 6):
        size_rows.extend(
            _u_frontier_rows(
                size,
                stage_a_max_nodes=stage_a_max_nodes,
                stage_a_max_examples=stage_a_max_examples,
                max_component_solutions=max_component_solutions,
                max_v_examples=max_v_examples,
                max_bucket_permutations=max_bucket_permutations,
            )
        )
    return {
        "title": "Size 5/6 component Stage B frontier audit",
        "status": (
            "bounded execution audit, not an exhaustive size 5 or 6 search"
        ),
        "bounds": {
            "stage_a_max_nodes": stage_a_max_nodes,
            "stage_a_max_examples": stage_a_max_examples,
            "max_component_solutions": max_component_solutions,
            "max_v_examples": max_v_examples,
            "max_bucket_permutations": max_bucket_permutations,
        },
        "rows": size_rows,
        "conclusion": (
            "This run exercises the production component Stage B search on "
            "the first bounded Stage A size-5 and size-6 U-frontiers.  It is "
            "a smoke/frontier execution artifact: any surviving V completion "
            "is passed immediately into the rigid-core filter row, but a "
            "truncated Stage A row does not rule out later U arrays."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-everywhere-singular-rigid-core-theory_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Size 5/6 Component Stage B Frontier Audit",
        "",
        str(report["status"]),
        "",
        "## Bounds",
        "",
    ]
    for key, value in report["bounds"].items():
        lines.append(f"- {key}: `{value}`;")
    lines.extend(["", "## Size Rows", ""])
    for row in report["rows"]:
        stage_a = row["stage_a"]
        lines.extend(
            [
                f"### size {row['size']}",
                "",
                f"- Stage A nodes: `{stage_a['node_count']}`;",
                f"- Stage A MF-valid arrays: `{stage_a['multiset_factorization_count']}`;",
                f"- Stage A canonical arrays: `{stage_a['canonical_count']}`;",
                f"- Stage A emitted examples: `{stage_a['emitted_count']}`;",
                f"- Stage A truncated: `{stage_a['truncated']}`;",
                "",
            ]
        )
        for u_row in row["u_rows"]:
            if u_row["stage_b_skipped_reason"]:
                lines.extend(
                    [
                        f"#### U example {u_row['u_index']}",
                        "",
                        "- maximum bucket permutations: "
                        f"`{u_row['maximum_bucket_permutations']}`;",
                        f"- Stage B skipped: `{u_row['stage_b_skipped_reason']}`;",
                        "",
                    ]
                )
                continue
            relation_gac = u_row["relation_gac"]
            component_solver = u_row["component_solver"]
            component_search = u_row["component_search"]
            first_failures = tuple(
                solution_row["rigid_pressure_core_row"]["first_failed_filter"]
                for solution_row in u_row["solution_rows"]
            )
            lines.extend(
                [
                    f"#### U example {u_row['u_index']}",
                    "",
                    "- relation-GAC product: "
                    f"`{relation_gac['initial_domain_product']}` -> "
                    f"`{relation_gac['final_domain_product']}`;",
                    "- relation-GAC locally consistent: "
                    f"`{relation_gac['locally_consistent']}`;",
                    "- component solver global/noninv/accepted: "
                    f"`{component_solver['global_solution_count']}` / "
                    f"`{component_solver['global_noninv_solution_count']}` / "
                    f"`{component_solver['accepted_count']}`;",
                    "- component search exact/noninv/accepted/emitted: "
                    f"`{component_search['exact_cover_count']}` / "
                    f"`{component_search['noninvolutive_count']}` / "
                    f"`{component_search['accepted_count']}` / "
                    f"`{component_search['emitted_count']}`;",
                    f"- component search truncated: `{component_search['truncated']}`;",
                    f"- rigid first failed filters: `{first_failures}`;",
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
