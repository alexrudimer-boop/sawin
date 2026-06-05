from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_type_a_solution,
)
from ybe_domination import identity_solution  # noqa: E402
from ybe_domination.stage_a_u_arrays import (  # noqa: E402
    stage_b_v_exact_cover_audit,
    uv_arrays_from_solution,
    uv_is_involutive,
    uv_pair_orthogonal,
    uv_y2_y3_hold,
    v_columns_singular,
)

OUT_JSON = ROOT / "proofs" / "stage_b_v_exact_cover_audit.json"
OUT_MD = ROOT / "proofs" / "stage_b_v_exact_cover_audit.md"


def example_report_rows() -> tuple[dict[str, object], ...]:
    examples = (
        ("identity_2", identity_solution((0, 1)), False),
        ("identity_3", identity_solution((0, 1, 2)), False),
        ("size4_affine_type_a", affine_f2_type_a_solution(), True),
    )
    rows = []
    for name, solution, require_noninvolutive in examples:
        u_array, v_array = uv_arrays_from_solution(solution)
        audit = stage_b_v_exact_cover_audit(
            u_array,
            require_column_singular=True,
            require_noninvolutive=require_noninvolutive,
            max_examples=None,
        )
        rows.append(
            {
                "name": name,
                "size": len(solution.elements),
                "source_solution_ybe": solution.is_ybe(),
                "source_pair_orthogonal": uv_pair_orthogonal(u_array, v_array),
                "source_column_singular": v_columns_singular(v_array),
                "source_y2_y3": uv_y2_y3_hold(u_array, v_array),
                "source_noninvolutive": not uv_is_involutive(u_array, v_array),
                "require_noninvolutive": require_noninvolutive,
                "actual_v_recovered": v_array in audit.examples,
                "audit": asdict(audit),
            }
        )
    return tuple(rows)


def build_report() -> dict[str, object]:
    return {
        "title": "Stage B V exact-cover audit",
        "purpose": (
            "Audit the second half of the size 5/6 search pipeline: for a "
            "fixed Stage A U-array satisfying multiset factorization, assign "
            "V[x,y] by bucket permutations C(u,P)->V(u,P), then enforce "
            "V-column singularity, Y2/Y3, and optional non-involutivity."
        ),
        "constraints": [
            "V[x,y] lies in the bucket domain V(U[x,y], L_x L_y)",
            "for every output pair (u,v), exactly one cell has (U,V)=(u,v)",
            "every V-column x -> V[x,y] is singular",
            "Y2 and Y3 hold for all triples",
            "optional r^2 != id filter is applied after Y2/Y3",
        ],
        "rows": list(example_report_rows()),
        "conclusion": (
            "The Stage B solver recovers identity completions in sizes 2 and "
            "3, and recovers the known size-4 affine Type A table as the "
            "unique non-involutive V-completion of its U among the two "
            "bucket-compatible Y2/Y3 completions.  This makes the U-then-V "
            "pipeline executable on concrete regression examples."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Stage B V Exact-Cover Audit",
        "",
        str(report["purpose"]),
        "",
        "## Constraints",
        "",
    ]
    for constraint in report["constraints"]:
        lines.append(f"- {constraint};")
    lines.extend(["", "## Example Rows", ""])
    for row in report["rows"]:
        audit = row["audit"]
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- source solution YBE: `{row['source_solution_ybe']}`;",
                f"- source pair orthogonal: `{row['source_pair_orthogonal']}`;",
                f"- source V-column singular: `{row['source_column_singular']}`;",
                f"- source Y2/Y3: `{row['source_y2_y3']}`;",
                f"- source noninvolutive: `{row['source_noninvolutive']}`;",
                f"- require noninvolutive: `{row['require_noninvolutive']}`;",
                f"- actual V recovered: `{row['actual_v_recovered']}`;",
                f"- nodes: `{audit['node_count']}`;",
                f"- exact-cover completions: `{audit['exact_cover_count']}`;",
                f"- column-singular completions: `{audit['column_singular_count']}`;",
                f"- Y2/Y3 completions: `{audit['y2_y3_count']}`;",
                f"- noninvolutive completions: `{audit['noninvolutive_count']}`;",
                f"- accepted completions: `{audit['accepted_count']}`;",
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
