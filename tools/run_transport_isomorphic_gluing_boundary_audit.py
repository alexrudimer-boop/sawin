from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    LocalInterval,
    branch_tags,
    local_master_bottleneck_summary,
    subsolution_fibre_transition_audit,
    subsolution_fibre_transport_isomorphism_audit,
    subsolution_fibre_transport_monodromy_audit,
)

OUT_JSON = ROOT / "proofs" / "transport_isomorphic_gluing_boundary_audit.json"
OUT_MD = ROOT / "proofs" / "transport_isomorphic_gluing_boundary_audit.md"


def identity_base_cyclic_transport_solution() -> FiniteBraidedSet:
    """Return the smallest product-like row with nontrivial transport monodromy."""

    colors = (0, 1)
    points = (0, 1, 2)
    elements = tuple(product(colors, points))
    table = {}
    for left_color, left_point in elements:
        for right_color, right_point in elements:
            table[((left_color, left_point), (right_color, right_point))] = (
                (left_color, right_point),
                (right_color, (left_point + 1) % 3),
            )
    return FiniteBraidedSet(elements, table)


def identity_base_cyclic_transport_interval() -> LocalInterval:
    colors = (0, 1)
    points = (0, 1, 2)
    fibres = {color: points for color in colors}
    base_R = {(left, right): (left, right) for left in colors for right in colors}
    table = {}
    for left_color, right_color, left_point, right_point in product(
        colors,
        colors,
        points,
        points,
    ):
        table[(left_color, right_color, left_point, right_point)] = (
            right_point,
            (left_point + 1) % 3,
        )
    return LocalInterval(colors, fibres, base_R, table)


def colour_partition(solution: FiniteBraidedSet):
    colors = sorted({color for color, _point in solution.elements})
    return tuple(
        frozenset(element for element in solution.elements if element[0] == color)
        for color in colors
    )


def _block_data(block) -> list[str]:
    return [repr(element) for element in sorted(block, key=repr)]


def build_report() -> dict:
    solution = identity_base_cyclic_transport_solution()
    partition = colour_partition(solution)
    transition = subsolution_fibre_transition_audit(solution, partition)
    transport = subsolution_fibre_transport_isomorphism_audit(solution, partition)
    monodromy = subsolution_fibre_transport_monodromy_audit(solution, partition)
    router = local_master_bottleneck_summary(
        identity_base_cyclic_transport_interval()
    )
    return {
        "name": "identity_base_cyclic_transport",
        "description": "r((a,x),(b,y))=((a,y),(b,x+1 mod 3))",
        "element_count": len(solution.elements),
        "is_ybe": solution.is_ybe(),
        "branch_tags": list(branch_tags(solution)),
        "partition": [_block_data(block) for block in partition],
        "all_mixed_transitions_product_like": (
            transition.all_mixed_transitions_product_like
        ),
        "all_mixed_transitions_swapped_product_like": (
            transition.all_mixed_transitions_swapped_product_like
        ),
        "all_mixed_rows_product_like": transport.all_mixed_rows_product_like,
        "all_product_like_rows_have_transport_isomorphisms": (
            transport.all_product_like_rows_have_transport_isomorphisms
        ),
        "all_rows_transport_isomorphic": monodromy.all_rows_transport_isomorphic,
        "all_transport_loop_groups_trivial": monodromy.all_loop_groups_trivial,
        "transport_edge_count": len(monodromy.edges),
        "transport_loop_group_orders": [
            {
                "block": _block_data(row.block),
                "loop_generator_count": row.loop_generator_count,
                "loop_group_order": row.loop_group_order,
            }
            for row in monodromy.rows
        ],
        "local_router_verdict": router.verdict,
        "local_router_product_branch": router.product_branch,
        "local_router_product_holonomy_details": (
            router.product_holonomy_details
        ),
        "local_router_detector_group_orders": (
            router.closed_detector_group_orders
        ),
        "local_router_detector_gaps": router.closed_detector_gaps,
        "local_router_remaining_obligation": router.remaining_obligation,
        "consequence": (
            "transport-isomorphic product-like rows do not force simultaneous "
            "identity-gauge normalization; this example has loop monodromy "
            "of order 3"
        ),
    }


def render_markdown(report: dict) -> str:
    orders = [
        row["loop_group_order"] for row in report["transport_loop_group_orders"]
    ]
    lines = [
        "# Transport-Isomorphic Gluing Boundary Audit",
        "",
        "This generated audit records a concrete transport-isomorphic",
        "product-like extension whose transport loop monodromy is nontrivial.",
        "",
        "Let",
        "",
        "```text",
        "X = {0,1} x Z/3",
        "r((a,x),(b,y)) = ((a,y),(b,x+1)).",
        "```",
        "",
        "The quotient by the first coordinate is the identity solution on two",
        "colours, and the two colour fibres are crossing-closed.",
        "",
        "## Audit",
        "",
        f"- element count: `{report['element_count']}`;",
        f"- YBE: `{report['is_ybe']}`;",
        f"- branch tags: `{report['branch_tags']}`;",
        f"- colour partition: `{report['partition']}`;",
        "- all mixed transitions product-like: "
        f"`{report['all_mixed_transitions_product_like']}`;",
        "- all mixed transitions swapped-product-like: "
        f"`{report['all_mixed_transitions_swapped_product_like']}`;",
        "- all product-like rows have transport isomorphisms: "
        f"`{report['all_product_like_rows_have_transport_isomorphisms']}`;",
        "- all rows transport-isomorphic: "
        f"`{report['all_rows_transport_isomorphic']}`;",
        "- transport edge count: "
        f"`{report['transport_edge_count']}`;",
        "- transport loop group orders: "
        f"`{orders}`;",
        "- all transport loop groups trivial: "
        f"`{report['all_transport_loop_groups_trivial']}`;",
        "- local router verdict: "
        f"`{report['local_router_verdict']}`;",
        "- local router product holonomy details: "
        f"`{report['local_router_product_holonomy_details']}`;",
        "- local router detector group orders: "
        f"`{report['local_router_detector_group_orders']}`;",
        "- local router detector gaps: "
        f"`{report['local_router_detector_gaps']}`.",
        "",
        "## Consequence",
        "",
        "This six-point solution satisfies the local transport-isomorphism",
        "part of the proposed gluing theorem, but the transport groupoid has",
        "loop monodromy of order `3`.  Therefore product-like",
        "transport-isomorphism does not by itself justify replacing every",
        "mixed transport by the identity in one global block gauge.",
        "",
        "The example is not being proposed as a Sawin counterexample.  It is",
        "one of the identity-base cyclic product rows already routed by",
        "`local_master_bottleneck_summary()` to `product_finite_g_branch`",
        "with detector group order `3`; see",
        "`proofs/identity_base_product_branch.md`.  Its role here is only to",
        "make the flatness obligation in",
        "`proofs/transport_isomorphic_gluing_boundary.md` explicit.",
    ]
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
