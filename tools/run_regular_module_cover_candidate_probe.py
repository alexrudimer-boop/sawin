from __future__ import annotations

from dataclasses import asdict
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.artin_longitudes import artin_detector_rack  # noqa: E402
from ybe_domination.finite_group import build_group, cyclic_group, symmetric_group  # noqa: E402
from ybe_domination.rack_residual_tower import (  # noqa: E402
    group_conjugation_rack,
    rack_residual_obstruction_audit,
)
from ybe_domination.residual import action_permutation  # noqa: E402
from ybe_domination.semigroup_shadows import permutation_order  # noqa: E402


OUT_JSON = ROOT / "proofs" / "regular_module_cover_candidate_probe.json"
OUT_MD = ROOT / "proofs" / "regular_module_cover_candidate_probe.md"


def regular_module_semidirect(group):
    group_elements = tuple(group.elements)
    index = {element: i for i, element in enumerate(group_elements)}
    masks = tuple(range(1 << len(group_elements)))

    def act(element, mask: int) -> int:
        output = 0
        for basis in group_elements:
            if (mask >> index[basis]) & 1:
                output |= 1 << index[group.mul(element, basis)]
        return output

    elements = tuple((mask, element) for mask in masks for element in group_elements)

    def multiply(left, right):
        left_vector, left_group = left
        right_vector, right_group = right
        return (
            left_vector ^ act(left_group, right_vector),
            group.mul(left_group, right_group),
        )

    return build_group(elements, (0, group.identity), multiply)


def _sigma_order(solution) -> int:
    return permutation_order(action_permutation(solution, 2, (1,)))


def _residual_row(name: str, group, arity: int) -> dict[str, Any]:
    solution = artin_detector_rack(group, include_trivial_two=False)
    detector_group = regular_module_semidirect(group)
    detector = group_conjugation_rack(detector_group)
    audit = rack_residual_obstruction_audit(
        solution,
        detector,
        n=arity,
        state_limit=1_000_000,
    )
    return {
        "kind": "residual",
        "group": name,
        "group_order": len(group.elements),
        "detector_group_order": len(detector_group.elements),
        "arity": arity,
        "audit": {
            **asdict(audit),
            "kernel_containment_certified": (
                not audit.truncated and audit.kernel_contains_nonidentity is False
            ),
        },
    }


def _b2_order_row(name: str, group) -> dict[str, Any]:
    solution = artin_detector_rack(group, include_trivial_two=False)
    detector_group = regular_module_semidirect(group)
    detector = group_conjugation_rack(detector_group)
    solution_order = _sigma_order(solution)
    detector_order = _sigma_order(detector)
    return {
        "kind": "b2_order",
        "group": name,
        "group_order": len(group.elements),
        "detector_group_order": len(detector_group.elements),
        "arity": 2,
        "solution_sigma_order": solution_order,
        "detector_sigma_order": detector_order,
        "b2_kernel_containment_by_order": detector_order % solution_order == 0,
    }


def build_report() -> dict[str, Any]:
    rows = [
        _residual_row("C2", cyclic_group(2), 2),
        _residual_row("C2", cyclic_group(2), 3),
        _residual_row("C3", cyclic_group(3), 2),
        _b2_order_row("S3", symmetric_group(3)),
    ]
    residual_rows = [row for row in rows if row["kind"] == "residual"]
    return {
        "title": "Regular-module cover candidate probe",
        "candidate": "C_reg(G)=F_2[G] semidirect G",
        "rows": rows,
        "all_residual_rows_certified": all(
            row["audit"]["kernel_containment_certified"]
            for row in residual_rows
        ),
        "proves_regular_module_fox_separation": False,
        "frontier_artifact": (
            "proofs/regular_module_framed_to_conjugation_cover_theorem.md"
        ),
        "conclusion": (
            "The regular-module candidate passes the feasible residual checks "
            "for C2 and C3 and the B2 order check for S3.  This is evidence for "
            "the candidate only; the regular-module Artin longitude Fox "
            "separation lemma remains the proof obligation."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {report['title']}",
        "",
        report["conclusion"],
        "",
        "## Scope",
        "",
        f"- candidate: `{report['candidate']}`;",
        "- proves regular-module Fox separation: "
        f"`{report['proves_regular_module_fox_separation']}`;",
        f"- frontier artifact: `{report['frontier_artifact']}`;",
        "",
        "## Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend([f"### {row['group']} arity {row['arity']}", ""])
        lines.append(f"- kind: `{row['kind']}`;")
        lines.append(f"- group order: `{row['group_order']}`;")
        lines.append(f"- detector group order: `{row['detector_group_order']}`;")
        if row["kind"] == "residual":
            audit = row["audit"]
            lines.append(f"- joint image size: `{audit['joint_image_size']}`;")
            lines.append(f"- solution image size: `{audit['solution_image_size']}`;")
            lines.append(f"- detector image size: `{audit['detector_image_size']}`;")
            lines.append(f"- kernel size: `{audit['kernel_size']}`;")
            lines.append(
                "- kernel contains nonidentity: "
                f"`{audit['kernel_contains_nonidentity']}`;"
            )
            lines.append(f"- truncated: `{audit['truncated']}`;")
            lines.append(
                "- containment certified: "
                f"`{audit['kernel_containment_certified']}`;"
            )
        else:
            lines.append(
                f"- solution sigma order: `{row['solution_sigma_order']}`;"
            )
            lines.append(
                f"- detector sigma order: `{row['detector_sigma_order']}`;"
            )
            lines.append(
                "- B2 containment by order: "
                f"`{row['b2_kernel_containment_by_order']}`;"
            )
        lines.append("")
    lines.extend(
        [
            "## Boundary",
            "",
            "This probe does not prove the regular-module cover.  It only pins",
            "small positive instances and keeps the Fox-separation proof",
            "obligation explicit.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    OUT_JSON.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
