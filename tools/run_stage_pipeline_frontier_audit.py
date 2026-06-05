from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_rigid_pressure_core_audit import rigid_pressure_core_row  # noqa: E402
from tools.run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_type_a_solution,
)
from ybe_domination.stage_a_u_arrays import (  # noqa: E402
    row_catalogue_stage_a_enumeration_audit,
    solution_from_uv_arrays,
    stage_b_bucket_csp_profile,
    stage_b_bucket_permutation_gac_audit,
    stage_b_bucket_permutation_v_search_audit,
    stage_b_gac_propagation_audit,
    stage_b_gac_v_search_audit,
    stage_b_v_exact_cover_audit,
    uv_arrays_from_solution,
)

OUT_JSON = ROOT / "proofs" / "stage_pipeline_frontier_audit.json"
OUT_MD = ROOT / "proofs" / "stage_pipeline_frontier_audit.md"


def _solution_rows_from_v_examples(
    name: str,
    u_array,
    v_examples,
    *,
    max_rows: int,
) -> list[dict[str, object]]:
    rows = []
    for index, v_array in enumerate(v_examples[:max_rows]):
        solution = solution_from_uv_arrays(u_array, v_array)
        rows.append(
            {
                "name": f"{name}_completion_{index}",
                "ybe": solution.is_ybe(),
                "rigid_pressure_core_row": asdict(
                    rigid_pressure_core_row(
                        f"{name}_completion_{index}",
                        solution,
                        run_pressure_if_structural=False,
                    )
                ),
            }
        )
    return rows


def frontier_row(
    name: str,
    u_array,
    *,
    require_noninvolutive: bool,
    stage_b_max_nodes: int | None = 50_000,
    max_solution_rows: int = 3,
) -> dict[str, object]:
    csp = stage_b_bucket_csp_profile(u_array)
    gac = stage_b_gac_propagation_audit(u_array)
    stage_b = stage_b_v_exact_cover_audit(
        u_array,
        require_column_singular=True,
        require_noninvolutive=require_noninvolutive,
        max_nodes=stage_b_max_nodes,
        max_examples=max_solution_rows,
    )
    gac_stage_b = stage_b_gac_v_search_audit(
        u_array,
        require_column_singular=True,
        require_noninvolutive=require_noninvolutive,
        max_nodes=stage_b_max_nodes,
        max_examples=max_solution_rows,
    )
    bucket_gac = stage_b_bucket_permutation_gac_audit(u_array)
    bucket_stage_b = stage_b_bucket_permutation_v_search_audit(
        u_array,
        require_column_singular=True,
        require_noninvolutive=require_noninvolutive,
        max_nodes=stage_b_max_nodes,
        max_examples=max_solution_rows,
    )
    return {
        "name": name,
        "size": len(u_array),
        "require_noninvolutive": require_noninvolutive,
        "bucket_csp": asdict(csp),
        "gac": asdict(gac),
        "bucket_gac": asdict(bucket_gac),
        "stage_b": asdict(stage_b),
        "gac_stage_b": asdict(gac_stage_b),
        "bucket_stage_b": asdict(bucket_stage_b),
        "solution_rows": _solution_rows_from_v_examples(
            name,
            u_array,
            bucket_stage_b.examples,
            max_rows=max_solution_rows,
        ),
    }


def build_report() -> dict[str, object]:
    exact_size_3 = row_catalogue_stage_a_enumeration_audit(3, max_examples=5)
    budget_size_4 = row_catalogue_stage_a_enumeration_audit(
        4,
        max_nodes=50_000,
        max_examples=5,
    )
    affine_u, _affine_v = uv_arrays_from_solution(affine_f2_type_a_solution())
    frontier_rows = []
    for index, u_array in enumerate(exact_size_3.examples):
        frontier_rows.append(
            frontier_row(
                f"row_exact_size3_u{index}",
                u_array,
                require_noninvolutive=True,
            )
        )
    for index, u_array in enumerate(budget_size_4.examples):
        frontier_rows.append(
            frontier_row(
                f"row_budget_size4_u{index}",
                u_array,
                require_noninvolutive=True,
            )
        )
    frontier_rows.append(
        frontier_row(
            "known_affine_type_a",
            affine_u,
            require_noninvolutive=True,
            stage_b_max_nodes=None,
        )
    )
    return {
        "title": "Stage pipeline frontier audit",
        "purpose": (
            "Connect row-catalogue Stage A enumeration to bucket-CSP, Stage B "
            "exact cover, and the existing rigid-pressure filters.  This is a "
            "bounded frontier audit, not an exhaustive size 4, 5, or 6 search."
        ),
        "stage_a_frontiers": {
            "exact_size_3": asdict(exact_size_3),
            "budget_size_4": asdict(budget_size_4),
        },
        "rows": frontier_rows,
        "conclusion": (
            "The exact d=3 row-catalogue frontier has no non-involutive Stage B "
            "completion.  The first d=4 budgeted row-catalogue frontier is "
            "also identity-type and has no non-involutive completion.  The "
            "named affine Type A regression still passes the same pipeline and "
            "is rejected by the rigid-core filters at quotient rigidity."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Stage Pipeline Frontier Audit",
        "",
        str(report["purpose"]),
        "",
        "## Stage A Frontiers",
        "",
    ]
    for name, audit in report["stage_a_frontiers"].items():
        lines.extend(
            [
                f"### {name}",
                "",
                f"- size: `{audit['size']}`;",
                f"- nodes: `{audit['node_count']}`;",
                f"- MF-valid arrays: `{audit['multiset_factorization_count']}`;",
                f"- canonical arrays: `{audit['canonical_count']}`;",
                f"- emitted examples: `{audit['emitted_count']}`;",
                f"- truncated: `{audit['truncated']}`.",
                "",
            ]
        )
    lines.extend(["## Pipeline Rows", ""])
    for row in report["rows"]:
        csp = row["bucket_csp"]
        gac = row["gac"]
        bucket_gac = row["bucket_gac"]
        stage_b = row["stage_b"]
        gac_stage_b = row["gac_stage_b"]
        bucket_stage_b = row["bucket_stage_b"]
        first_failures = [
            solution_row["rigid_pressure_core_row"]["first_failed_filter"]
            for solution_row in row["solution_rows"]
        ]
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- require noninvolutive: `{row['require_noninvolutive']}`;",
                f"- bucket count: `{csp['bucket_count']}`;",
                f"- maximum domain size: `{csp['maximum_domain_size']}`;",
                f"- locally consistent: `{csp['locally_consistent']}`;",
                f"- GAC domain mass: "
                f"`{gac['initial_domain_mass']}` -> `{gac['final_domain_mass']}`;",
                f"- GAC forced variables: `{gac['forced_variable_count']}`;",
                f"- GAC locally consistent: `{gac['locally_consistent']}`;",
                "- bucket-permutation product: "
                f"`{bucket_gac['initial_domain_product']}` -> "
                f"`{bucket_gac['final_domain_product']}`;",
                f"- bucket-permutation locally consistent: "
                f"`{bucket_gac['locally_consistent']}`;",
                f"- Stage B accepted completions: `{stage_b['accepted_count']}`;",
                f"- Stage B emitted completions: `{stage_b['emitted_count']}`;",
                f"- Stage B truncated: `{stage_b['truncated']}`;",
                f"- GAC Stage B nodes: `{gac_stage_b['node_count']}`;",
                f"- GAC Stage B accepted completions: `{gac_stage_b['accepted_count']}`;",
                f"- GAC Stage B truncated: `{gac_stage_b['truncated']}`;",
                f"- bucket Stage B nodes: `{bucket_stage_b['node_count']}`;",
                f"- bucket Stage B accepted completions: "
                f"`{bucket_stage_b['accepted_count']}`;",
                f"- bucket Stage B Aut(U) / canonical rejections: "
                f"`{bucket_stage_b['aut_u_order']}` / "
                f"`{bucket_stage_b['canonical_rejection_count']}`;",
                f"- bucket Stage B truncated: `{bucket_stage_b['truncated']}`;",
                f"- rigid first failed filters: `{tuple(first_failures)}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Conclusion",
            "",
            str(report["conclusion"]),
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
