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
    congruences,
    flip_disjoint_union_solution,
    identity_solution,
    is_involutive_solution,
    subsolution_fibre_congruences,
    subsolution_fibre_transport_isomorphism_audit,
    terminal_branch_triage_audit,
)

OUT_JSON = ROOT / "proofs" / "product_like_transport_boundary_audit.json"
OUT_MD = ROOT / "proofs" / "product_like_transport_boundary_audit.md"


def affine_f2_type_a_solution() -> FiniteBraidedSet:
    elements = tuple(product((0, 1), repeat=2))
    table = {}
    for a, b in elements:
        for c, d in elements:
            table[((a, b), (c, d))] = (
                (d, (a + b + d) % 2),
                ((a + c + d + 1) % 2, (a + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def permutation_solution_with_toggle() -> FiniteBraidedSet:
    elements = (0, 1)
    return FiniteBraidedSet(
        elements,
        {(left, right): (right, 1 - left) for left in elements for right in elements},
    )


def type_b_flip_across_solution() -> FiniteBraidedSet:
    return flip_disjoint_union_solution(
        identity_solution((0, 1)),
        permutation_solution_with_toggle(),
        "T",
        "P",
    )


def _element_key(element) -> str:
    return repr(element)


def _block_data(block) -> list[str]:
    return sorted((_element_key(element) for element in block))


def _partition_data(partition) -> list[list[str]]:
    return [_block_data(block) for block in partition]


def _transport_map_data(transport_map) -> dict:
    return {
        "source_coordinate": transport_map.source_coordinate,
        "output_coordinate": transport_map.output_coordinate,
        "source_block": _block_data(transport_map.source_block),
        "target_block": _block_data(transport_map.target_block),
        "mapping": [
            [_element_key(source), _element_key(target)]
            for source, target in transport_map.mapping
        ],
        "is_well_defined": transport_map.is_well_defined,
        "is_bijection": transport_map.is_bijection,
        "is_subsolution_isomorphism": transport_map.is_subsolution_isomorphism,
    }


def _transport_row_data(row) -> dict:
    return {
        "input_left_block": _block_data(row.input_left_block),
        "input_right_block": _block_data(row.input_right_block),
        "direct_product_like": row.direct_product_like,
        "swapped_product_like": row.swapped_product_like,
        "direct_transport_isomorphism": row.direct_transport_isomorphism,
        "swapped_transport_isomorphism": row.swapped_transport_isomorphism,
        "product_like_transport_isomorphism": (
            row.product_like_transport_isomorphism
        ),
        "well_defined_maps": [
            _transport_map_data(transport_map)
            for transport_map in (
                row.first_from_left,
                row.first_from_right,
                row.second_from_left,
                row.second_from_right,
            )
            if transport_map.is_well_defined
        ],
    }


def _model_report(name: str, solution: FiniteBraidedSet) -> dict:
    all_congruences = tuple(congruences(solution))
    fibre_congruences = tuple(subsolution_fibre_congruences(solution))
    triage = terminal_branch_triage_audit(solution)
    transport_rows = []
    for partition in fibre_congruences:
        audit = subsolution_fibre_transport_isomorphism_audit(solution, partition)
        transport_rows.append(
            {
                "partition": _partition_data(partition),
                "all_mixed_rows_product_like": audit.all_mixed_rows_product_like,
                "all_product_like_rows_have_transport_isomorphisms": (
                    audit.all_product_like_rows_have_transport_isomorphisms
                ),
                "rows": [_transport_row_data(row) for row in audit.rows],
            }
        )
    return {
        "name": name,
        "element_count": len(solution.elements),
        "is_ybe": solution.is_ybe(),
        "is_involutive": is_involutive_solution(solution),
        "proper_congruence_count": len(triage.proper_congruences),
        "congruence_block_sizes": [
            [len(block) for block in partition] for partition in all_congruences
        ],
        "proper_subsolution_fibre_congruence_count": len(fibre_congruences),
        "proper_subsolution_fibre_congruences": [
            _partition_data(partition) for partition in fibre_congruences
        ],
        "has_flip_across_decomposition": triage.has_flip_across_decomposition,
        "has_nontrivial_one_state_observer": (
            triage.has_nontrivial_one_state_observer
        ),
        "transport_audits": transport_rows,
    }


def build_report() -> dict:
    return {
        "type_a_affine_f2": _model_report(
            "type_a_affine_f2",
            affine_f2_type_a_solution(),
        ),
        "type_b_flip_across": _model_report(
            "type_b_flip_across",
            type_b_flip_across_solution(),
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Product-Like Transport Boundary Audit",
        "",
        "This generated audit records the finite boundary between two",
        "subsolution-fibre mechanisms in the first size-four degenerate",
        "non-involutive examples.",
        "",
        "It is not a proof of Sawin's conjecture.  It proves only that finite",
        "YBE locality does not force product-like mixed transports to be",
        "isomorphisms of the internal block subsolutions.",
        "",
    ]
    for key, model in report.items():
        lines.extend(
            [
                f"## {model['name']}",
                "",
                f"- element count: `{model['element_count']}`;",
                f"- YBE: `{model['is_ybe']}`;",
                f"- involutive: `{model['is_involutive']}`;",
                f"- proper congruences: `{model['proper_congruence_count']}`;",
                "- congruence block-size profiles: "
                f"`{model['congruence_block_sizes']}`;",
                "- proper subsolution-fibre congruences: "
                f"`{model['proper_subsolution_fibre_congruence_count']}`;",
                "- flip-across decomposition: "
                f"`{model['has_flip_across_decomposition']}`;",
                "- nontrivial one-state observer: "
                f"`{model['has_nontrivial_one_state_observer']}`.",
                "",
                "| partition | product-like | transport isomorphism |",
                "| --- | --- | --- |",
            ]
        )
        for audit in model["transport_audits"]:
            lines.append(
                f"| `{audit['partition']}` | "
                f"`{audit['all_mixed_rows_product_like']}` | "
                f"`{audit['all_product_like_rows_have_transport_isomorphisms']}` |"
            )
        if not model["transport_audits"]:
            lines.append("| none | `False` | `False` |")
        lines.append("")

    lines.extend(
        [
            "## Consequence",
            "",
            "The Type A affine model has exactly one proper subsolution-fibre",
            "congruence, with block sizes `[2,2]`.  Its mixed rows are",
            "product-like, but the resulting one-coordinate transport maps are",
            "not isomorphisms of the two internal block subsolutions.  The only",
            "subsolution-fibre refinement that removes this obstruction is the",
            "equality congruence, which is not a proper compression.",
            "",
            "Thus Question B from the queued Pro prompt has a negative finite",
            "answer in this sense: product-like mixed transport is a real weaker",
            "condition than product-like transport by subsolution isomorphisms.",
            "The Type B flip-across model lies on the positive transport branch,",
            "while Type A requires the separate parity/fibre gauge.",
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
