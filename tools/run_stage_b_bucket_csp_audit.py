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
    stage_b_bucket_permutation_gac_audit,
    stage_b_bucket_permutation_v_search_audit,
    stage_b_bucket_constraint_hypergraph_audit,
    stage_b_bucket_column_singularity_possible,
    stage_b_bucket_noninvolutive_possible,
    stage_b_gac_propagation_audit,
    stage_b_gac_v_search_audit,
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
        u_array = u_array_from_solution(solution)
        bucket_gac = stage_b_bucket_permutation_gac_audit(u_array)
        rows.append(
            {
                "name": name,
                "size": len(solution.elements),
                "source_solution_ybe": solution.is_ybe(),
                "profile": asdict(stage_b_bucket_csp_profile(u_array)),
                "gac": asdict(stage_b_gac_propagation_audit(u_array)),
                "gac_noninvolutive_search": asdict(
                    stage_b_gac_v_search_audit(
                        u_array,
                        require_column_singular=True,
                        require_noninvolutive=True,
                        max_examples=3,
                    )
                ),
                "bucket_permutation_gac": asdict(bucket_gac),
                "bucket_column_singularity_possible": (
                    stage_b_bucket_column_singularity_possible(
                        u_array,
                        bucket_gac.domains,
                    )
                ),
                "bucket_noninvolutive_possible": (
                    stage_b_bucket_noninvolutive_possible(
                        u_array,
                        bucket_gac.domains,
                    )
                ),
                "bucket_constraint_hypergraph": asdict(
                    stage_b_bucket_constraint_hypergraph_audit(u_array)
                ),
                "bucket_permutation_search": asdict(
                    stage_b_bucket_permutation_v_search_audit(
                        u_array,
                        require_column_singular=True,
                        require_noninvolutive=True,
                        max_examples=3,
                    )
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
            "local support for every Y2/Y3 triple.  Also record the exact "
            "generalized arc-consistency propagation over bucket variables."
        ),
        "checks": [
            "domain-size profile for variables W_xy=V[x,y]",
            "Hall all-different test on cells with fixed U[x,y]=u",
            "Y2/Y3 local support test for each triple (x,y,z)",
            "locally_consistent iff Hall succeeds and no Y2/Y3 triple is unsupported",
            "exact GAC value deletion using dynamic Y2/Y3 implication supports",
            "singleton GAC domains are extracted and directly verified against Y2/Y3",
            "GAC-assisted Stage B branching for column-singular non-involutive completions",
            "early column-singularity feasibility rejection when a column has no possible duplicate value",
            "bucket-permutation GAC over whole bijections C(u,P)->B(u,P)",
            "bucket-permutation branching for column-singular non-involutive completions",
            "Aut(U)-aware canonical state rejection for bucket-permutation branches",
            "exact bucket-domain column-singularity feasibility before branching",
            "exact bucket-domain non-involutivity feasibility before branching",
            "remaining bucket-constraint hypergraph and connected components after bucket-GAC",
        ],
        "rows": list(example_rows()),
        "conclusion": (
            "The current examples all pass local bucket-CSP consistency.  The "
            "profile still distinguishes their domain geometry: identity has "
            "three 3-cell buckets, the dihedral rack has nine forced cells, "
            "and affine Type A has eight 2-cell buckets.  Exact GAC forces "
            "the dihedral rack table and preserves all values needed for the "
            "known affine Type A completion.  GAC-assisted branching recovers "
            "the unique non-involutive affine Type A completion in three "
            "search nodes.  The branch search also rejects any non-singleton "
            "state where some V-column can no longer become singular.  This "
            "is now refined by bucket-permutation GAC, which preserves whole "
            "bucket-bijection correlations and forces the identity example "
            "without cell-level branching.  The bucket search records Aut(U) "
            "and rejects noncanonical branch states under that stabilizer.  It "
            "also uses exact bucket-domain column feasibility, which rejects "
            "the dihedral rack regression as not column-singular, and exact "
            "non-involutivity feasibility, which rejects identity-type states "
            "as forced involutive.  The remaining hypergraph audit shows "
            "whether unresolved bucket choices decompose into independent "
            "components before full d=5,6 Stage B search."
        ),
        "next_prompt": "prompts/gpt55_pro/2026-06-04-stabilizer-component-solver-next-step_ask_now.md",
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
        gac = row["gac"]
        gac_search = row["gac_noninvolutive_search"]
        bucket_gac = row["bucket_permutation_gac"]
        bucket_search = row["bucket_permutation_search"]
        hypergraph = row["bucket_constraint_hypergraph"]
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
                f"- GAC final domain size counts: `{gac['final_domain_size_counts']}`;",
                f"- GAC initial/final domain mass: "
                f"`{gac['initial_domain_mass']}` / `{gac['final_domain_mass']}`;",
                "- GAC deletions, Hall/Y2-Y3: "
                f"`{gac['hall_value_deletion_count']}` / "
                f"`{gac['unsupported_value_deletion_count']}`;",
                f"- GAC forced variables: `{gac['forced_variable_count']}`;",
                f"- GAC all singleton: `{gac['all_singleton']}`;",
                f"- GAC singleton Y2/Y3 verified: "
                f"`{gac['singleton_y2_y3_verified']}`;",
                f"- GAC locally consistent: `{gac['locally_consistent']}`.",
                "- GAC non-involutive search nodes / accepted: "
                f"`{gac_search['node_count']}` / `{gac_search['accepted_count']}`;",
                f"- GAC non-involutive search truncated: `{gac_search['truncated']}`.",
                "- bucket-permutation domain product: "
                f"`{bucket_gac['initial_domain_product']}` -> "
                f"`{bucket_gac['final_domain_product']}`;",
                "- bucket-permutation domain size counts: "
                f"`{bucket_gac['final_domain_size_counts']}`;",
                "- bucket-permutation singleton/noninvolutive: "
                f"`{bucket_gac['all_singleton']}` / `{bucket_gac['noninvolutive']}`;",
                "- bucket-domain column-singularity possible: "
                f"`{row['bucket_column_singularity_possible']}`;",
                "- bucket-domain non-involutivity possible: "
                f"`{row['bucket_noninvolutive_possible']}`;",
                "- bucket hypergraph components / largest: "
                f"`{hypergraph['component_count']}` / "
                f"`{hypergraph['largest_component_size']}`;",
                "- bucket relation patterns YBE/column/noninv: "
                f"`{hypergraph['ybe_pattern_count']}` / "
                f"`{hypergraph['column_pattern_count']}` / "
                f"`{hypergraph['noninvolutive_witness_count']}`;",
                "- bucket hypergraph edge counts YBE/column/involutive: "
                f"`{hypergraph['ybe_hyperedge_count']}` / "
                f"`{hypergraph['column_hyperedge_count']}` / "
                f"`{hypergraph['involutive_hyperedge_count']}`;",
                "- bucket hypergraph column/noninv feasible: "
                f"`{hypergraph['column_singularity_possible']}` / "
                f"`{hypergraph['noninvolutive_possible']}`;",
                "- bucket-permutation search nodes / accepted: "
                f"`{bucket_search['node_count']}` / `{bucket_search['accepted_count']}`;",
                "- bucket-permutation Aut(U) / canonical rejections: "
                f"`{bucket_search['aut_u_order']}` / "
                f"`{bucket_search['canonical_rejection_count']}`;",
                f"- bucket-permutation search truncated: `{bucket_search['truncated']}`.",
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
