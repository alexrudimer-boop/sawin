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
from ybe_domination import identity_solution, rack_solution  # noqa: E402
from ybe_domination.stage_a_u_arrays import (  # noqa: E402
    stage_b_bucket_csp_profile,
    u_array_from_solution,
)

OUT_JSON = ROOT / "proofs" / "stage_b_bucket_csp_audit.json"
OUT_MD = ROOT / "proofs" / "stage_b_bucket_csp_audit.md"


def example_rows() -> tuple[dict[str, object], ...]:
    examples = (
        ("identity_3", identity_solution((0, 1, 2))),
        ("dihedral_rack_3", rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)),
        ("size4_affine_type_a", affine_f2_type_a_solution()),
    )
    rows = []
    for name, solution in examples:
        rows.append(
            {
                "name": name,
                "size": len(solution.elements),
                "source_solution_ybe": solution.is_ybe(),
                "profile": asdict(
                    stage_b_bucket_csp_profile(u_array_from_solution(solution))
                ),
            }
        )
    return tuple(rows)


def build_report() -> dict[str, object]:
    return {
        "title": "Stage B bucket-CSP audit",
        "purpose": (
            "Record the bucket-domain CSP precheck used before full Stage B "
            "backtracking: Hall all-different consistency per output u and "
            "local support for every Y2/Y3 triple."
        ),
        "checks": [
            "domain-size profile for variables W_xy=V[x,y]",
            "Hall all-different test on cells with fixed U[x,y]=u",
            "Y2/Y3 local support test for each triple (x,y,z)",
            "locally_consistent iff Hall succeeds and no Y2/Y3 triple is unsupported",
        ],
        "rows": list(example_rows()),
        "conclusion": (
            "The current examples all pass local bucket-CSP consistency.  The "
            "profile still distinguishes their domain geometry: identity has "
            "three 3-cell buckets, the dihedral rack has nine forced cells, "
            "and affine Type A has eight 2-cell buckets.  This is the next "
            "precheck layer before full d=5,6 Stage B search."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/2026-06-04-stage-b-bucket-csp_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Stage B Bucket-CSP Audit",
        "",
        str(report["purpose"]),
        "",
        "## Checks",
        "",
    ]
    for check in report["checks"]:
        lines.append(f"- {check};")
    lines.extend(["", "## Example Rows", ""])
    for row in report["rows"]:
        profile = row["profile"]
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- size: `{row['size']}`;",
                f"- source solution YBE: `{row['source_solution_ybe']}`;",
                f"- variable count: `{profile['variable_count']}`;",
                f"- bucket count: `{profile['bucket_count']}`;",
                f"- domain size counts: `{profile['domain_size_counts']}`;",
                f"- forced variables: `{profile['forced_variable_count']}`;",
                f"- maximum domain size: `{profile['maximum_domain_size']}`;",
                f"- Hall all-different ok: `{profile['hall_all_different_ok']}`;",
                "- unsupported Y2/Y3 triples: "
                f"`{profile['unsupported_y2_y3_triple_count']}`;",
                f"- locally consistent: `{profile['locally_consistent']}`.",
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
